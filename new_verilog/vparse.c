/*
 * vparse.c  --  Verilog / SystemVerilog (synthesizable subset) reader.
 *
 * Reads one or more Verilog files and prints a Python data structure
 * (or JSON with -json) that represents the design.
 *
 *   modules = {
 *     'name': {
 *        'kind'       : 'module' | 'interface' | 'package' | 'program',
 *        'line'       : line number of the header,
 *        'nets'       : { name: {'dir','type','signed','packed','width','unpacked','line',...} },
 *        'assigns'    : [ (dst, src_expr, {'line':..,'delay':..,'decl':True,..}), ... ],
 *        'always'     : [ {'kind':'always_ff', 'when':[('posedge','clk'),...], 'code':[...]}, ...],
 *        'localparams': { name: {'value':expr, 'eval':int, 'type':..} },
 *        'parameters' : { name: {'value':expr, 'eval':int, 'type':..} },
 *        'structures' : { name: {'kind':'struct'|'union','packed':bool,'fields':{...},'width':N} },
 *        'initials'   : [ {'kind':'initial'|'final', 'code':[...]}, ...],
 *        'typedefs'   : { name: {'kind':'enum'|'alias', ...} },
 *        'instances'  : { inst: {'module':m, 'params':{..}|[..], 'conns':{..}|[..]} },
 *        'generates'  : [ {'kind':'for'|'if'|'case'|'block', ..., 'body':{module-like dict}} ],
 *        'functions'  : { name: {'kind':'function'|'task','nets':{..ports have dir input/output..},'code':[...]} },
 *        'imports'    : ['pkg::*', ...],
 *     }, ...
 *   }
 *
 * Expressions are nested tuples, operator first:
 *     'a'                         identifier (plain string)
 *     5                           unsized decimal number (int)
 *     ('const', 8, 'h', 'ff', 255)  sized/based literal: width, base, digits, value|None
 *     ('fill', '1')  ('real','1.5')  ('time','10ns')  ('string','text')
 *     ('+', a, b)  ('-', a)  ('&', a)  ('?:', c, a, b)
 *     ('bitsel', x, i)  ('partsel', x, hi, lo)  ('partsel+', x, base, w)  ('partsel-', ...)
 *     ('member', x, 'field')  ('concat', a, b, ...)  ('repl', n, ('concat', ...))
 *     ('call', 'fname', args...)  ('cast', type, expr)  ('pattern', items...)
 *     ('inside', x, items...)
 *
 * Statements (inside 'code' lists):
 *     ('<=', dst, src)  ('=', dst, src)  ('+=', dst, src)  ('++', dst)
 *     ('if', cond, [then], [else])
 *     ('case', 'case'|'casez'|'casex', expr, [ ([labels], [stmts]) | ('default', [stmts]) ])
 *     ('for', init, cond, step, [body])  ('while', c, [b])  ('repeat', n, [b])  ('forever', [b])
 *     ('delay', d, [b])  ('wait_event', events, [b])  ('wait', c, [b])
 *     ('systask', '$display', args...)  ('call', 'task', args...)
 *     ('begin', 'label', [stmts])  ('declare', name, netinfo)  ('disable', x) ...
 *
 * Build:   cc -O2 -o vparse vparse.c
 * Usage:   vparse [-o out.py] [-json] [-DNAME[=VAL]] [-Idir] file.v [file2.sv ...]
 *          (file name "-" reads standard input)
 *          --split : each module goes to its own file tmppy/<module>.py
 *                    (tmppy/<module>.json with -json), written as soon as
 *                    the module has been read; each file holds
 *                    modules = {'<module>': {...}}
 *
 * Streaming: input is read line by line, and each module is printed (and
 * flushed) as soon as its endmodule has been read; its memory is then
 * released.  Packages stay in memory because later modules use their types.
 * File-level items outside any module are printed last, as '$unit'.
 *
 * Not parsed (skipped): modport contents, specify, covergroups, classes,
 * concurrent assertions, properties/sequences.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdarg.h>
#include <setjmp.h>
#include <stddef.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <errno.h>

/* ================================================================ utils */

static void *xmalloc(size_t n) {
    void *p = malloc(n ? n : 1);
    if (!p) { fprintf(stderr, "out of memory\n"); exit(2); }
    return p;
}
static void *xrealloc(void *p, size_t n) {
    p = realloc(p, n ? n : 1);
    if (!p) { fprintf(stderr, "out of memory\n"); exit(2); }
    return p;
}
static char *xstrndup(const char *s, size_t n) {
    char *p = xmalloc(n + 1);
    memcpy(p, s, n); p[n] = 0; return p;
}
static char *xstrdup(const char *s) { return xstrndup(s, strlen(s)); }
static char *sfmt(const char *fmt, ...) {
    va_list ap; va_start(ap, fmt);
    int n = vsnprintf(NULL, 0, fmt, ap); va_end(ap);
    char *s = xmalloc(n + 1);
    va_start(ap, fmt); vsnprintf(s, n + 1, fmt, ap); va_end(ap);
    return s;
}

typedef struct { char *s; size_t n, cap; } Buf;
static void bput(Buf *b, const char *s, size_t n) {
    if (b->n + n + 1 > b->cap) {
        b->cap = (b->n + n + 1) * 2;
        b->s = xrealloc(b->s, b->cap);
    }
    memcpy(b->s + b->n, s, n); b->n += n; b->s[b->n] = 0;
}
static void bputc(Buf *b, char c) { bput(b, &c, 1); }
static void bputs(Buf *b, const char *s) { bput(b, s, strlen(s)); }
static char *bstr(Buf *b) { return b->s ? b->s : xstrdup(""); }

static int is_in(const char *s, const char **list) {
    for (; *list; list++) if (!strcmp(s, *list)) return 1;
    return 0;
}

static const char *cur_file = "?";
static int nerrors = 0, nwarnings = 0;

static void warn(int line, const char *fmt, ...) {
    va_list ap; va_start(ap, fmt);
    fprintf(stderr, "%s:%d: warning: ", cur_file, line);
    vfprintf(stderr, fmt, ap); fputc('\n', stderr);
    va_end(ap); nwarnings++;
}

static char *read_file(const char *fn) {
    FILE *f = fopen(fn, "rb");
    if (!f) return NULL;
    Buf b = {0}; char tmp[65536]; size_t n;
    while ((n = fread(tmp, 1, sizeof tmp, f)) > 0) bput(&b, tmp, n);
    fclose(f);
    return bstr(&b);
}

/* ================================================================ memory pools
 * Nodes are allocated from a pool.  Each module gets its own pool which is
 * released as soon as the module has been printed, so memory use stays
 * bounded by the largest module, not by the size of the input.
 * Packages and file-level ($unit) items live in the persistent pool because
 * later modules refer to their types and constants.
 */
typedef struct Pool Pool;
typedef union PHdr {
    struct { union PHdr *prev, *next; Pool *pool; } h;
    max_align_t align;
} PHdr;
struct Pool { PHdr head; int init; };
static Pool persistent_pool, module_pool;
static Pool *curpool = &persistent_pool;

static void pool_link(Pool *p, PHdr *h) {
    if (!p->init) { p->head.h.prev = p->head.h.next = &p->head; p->init = 1; }
    h->h.pool = p;
    h->h.next = p->head.h.next; h->h.prev = &p->head;
    p->head.h.next->h.prev = h; p->head.h.next = h;
}
static void pool_unlink(PHdr *h) { h->h.prev->h.next = h->h.next; h->h.next->h.prev = h->h.prev; }
static void *palloc(size_t n) {
    PHdr *h = xmalloc(sizeof(PHdr) + n);
    pool_link(curpool, h);
    return h + 1;
}
static void *prealloc(void *q, size_t n) {
    if (!q) return palloc(n);
    PHdr *h = (PHdr *)q - 1;
    Pool *p = h->h.pool;
    pool_unlink(h);
    h = xrealloc(h, sizeof(PHdr) + n);
    pool_link(p, h);
    return h + 1;
}
static char *pstrdup(const char *s) { size_t n = strlen(s); char *p = palloc(n + 1); memcpy(p, s, n + 1); return p; }
static void pool_free(Pool *p) {
    if (!p->init) return;
    PHdr *h = p->head.h.next;
    while (h != &p->head) { PHdr *n = h->h.next; free(h); h = n; }
    p->head.h.prev = p->head.h.next = &p->head;
}

/* ================================================================ nodes */

typedef enum { N_NONE, N_BOOL, N_INT, N_STR, N_LIST, N_TUPLE, N_DICT } NKind;
typedef struct Node Node;
struct Node {
    NKind k;
    long long i;
    char *s;
    int n, cap;
    Node **items;
    char **keys;
};

static Node NONE_NODE = { N_NONE, 0, NULL, 0, 0, NULL, NULL };
static Node *nnew(NKind k) { Node *n = palloc(sizeof *n); memset(n, 0, sizeof *n); n->k = k; return n; }
static Node *None(void) { return &NONE_NODE; }
static Node *Int(long long v) { Node *n = nnew(N_INT); n->i = v; return n; }
static Node *Bool(int b) { Node *n = nnew(N_BOOL); n->i = b != 0; return n; }
static Node *Str(const char *s) { Node *n = nnew(N_STR); n->s = pstrdup(s); return n; }
static Node *List(void) { return nnew(N_LIST); }
static Node *Dict(void) { return nnew(N_DICT); }

static void grow(Node *c) {
    if (c->n == c->cap) {
        c->cap = c->cap ? c->cap * 2 : 4;
        c->items = prealloc(c->items, c->cap * sizeof(Node *));
        if (c->k == N_DICT) c->keys = prealloc(c->keys, c->cap * sizeof(char *));
    }
}
static Node *add(Node *c, Node *v) { grow(c); c->items[c->n++] = v; return c; }
static Node *tup(Node *first, ...) {
    Node *t = nnew(N_TUPLE);
    va_list ap; va_start(ap, first);
    for (Node *x = first; x; x = va_arg(ap, Node *)) add(t, x);
    va_end(ap);
    return t;
}
static Node *dget(Node *d, const char *k) {
    for (int i = 0; i < d->n; i++) if (!strcmp(d->keys[i], k)) return d->items[i];
    return NULL;
}
static void dset(Node *d, const char *k, Node *v) {
    for (int i = 0; i < d->n; i++) if (!strcmp(d->keys[i], k)) { d->items[i] = v; return; }
    grow(d); d->keys[d->n] = pstrdup(k); d->items[d->n++] = v;
}
static void ddel(Node *d, const char *k) {
    for (int i = 0; i < d->n; i++) if (!strcmp(d->keys[i], k)) {
        memmove(d->keys + i, d->keys + i + 1, (d->n - i - 1) * sizeof(char *));
        memmove(d->items + i, d->items + i + 1, (d->n - i - 1) * sizeof(Node *));
        d->n--; return;
    }
}
/* remove keys whose value is None or an empty container */
static void prune(Node *d) {
    for (int i = 0; i < d->n; ) {
        Node *v = d->items[i];
        if (v->k == N_NONE || ((v->k == N_LIST || v->k == N_DICT) && v->n == 0)) ddel(d, d->keys[i]);
        else i++;
    }
}

/* ================================================================ preprocessor */

typedef struct { char *name; int np; char **params; char **defs; char *body; } Macro;
static Macro *macros; static int nmacros, capmacros;
static char **incdirs; static int nincdirs;

#define MAXIF 256
static int if_active[MAXIF], if_taken[MAXIF], if_depth;

static Macro *find_macro(const char *name) {
    for (int i = 0; i < nmacros; i++) if (!strcmp(macros[i].name, name)) return &macros[i];
    return NULL;
}
static void define_macro(const char *name, int np, char **params, char **defs, const char *body) {
    Macro *m = find_macro(name);
    if (!m) {
        if (nmacros == capmacros) { capmacros = capmacros ? capmacros * 2 : 32; macros = xrealloc(macros, capmacros * sizeof(Macro)); }
        m = &macros[nmacros++];
        m->name = xstrdup(name);
    }
    m->np = np; m->params = params; m->defs = defs; m->body = xstrdup(body);
}
static void undef_macro(const char *name) {
    for (int i = 0; i < nmacros; i++) if (!strcmp(macros[i].name, name)) { macros[i] = macros[--nmacros]; return; }
}

static int pp_on(void) { return if_depth == 0 || if_active[if_depth - 1]; }
static int pp_parent_on(void) { return if_depth <= 1 || if_active[if_depth - 2]; }

static const char *DIRECTIVES[] = {
    "define", "undef", "ifdef", "ifndef", "elsif", "else", "endif", "include", "timescale",
    "default_nettype", "resetall", "celldefine", "endcelldefine", "nounconnected_drive",
    "unconnected_drive", "pragma", "line", "begin_keywords", "end_keywords", "undefineall",
    "default_decay_time", "default_trireg_strength", "delay_mode_distributed",
    "delay_mode_path", "delay_mode_unit", "delay_mode_zero", NULL };

/* remove // and block comments; keep newlines so line numbers survive */
static char *strip_comments(const char *p) {
    Buf b = {0};
    while (*p) {
        if (*p == '"') {
            bputc(&b, *p++);
            while (*p && *p != '"' && *p != '\n') {
                if (*p == '\\' && p[1]) { bput(&b, p, 2); p += 2; continue; }
                bputc(&b, *p++);
            }
            if (*p == '"') bputc(&b, *p++);
            continue;
        }
        if (p[0] == '/' && p[1] == '/') { while (*p && *p != '\n') p++; continue; }
        if (p[0] == '/' && p[1] == '*') {
            p += 2;
            while (*p && !(p[0] == '*' && p[1] == '/')) { if (*p == '\n') bputc(&b, '\n'); p++; }
            if (*p) p += 2;
            bputc(&b, ' ');
            continue;
        }
        bputc(&b, *p++);
    }
    return bstr(&b);
}

static const char *read_word(const char *p, char *buf, size_t max) {
    size_t n = 0;
    while (*p == ' ' || *p == '\t') p++;
    while ((isalnum((unsigned char)*p) || *p == '_' || *p == '$') && n + 1 < max) buf[n++] = *p++;
    buf[n] = 0;
    return p;
}

static char *trim(char *s) {
    while (*s && isspace((unsigned char)*s)) s++;
    size_t n = strlen(s);
    while (n > 0 && isspace((unsigned char)s[n - 1])) s[--n] = 0;
    return s;
}

static void expand(const char *s, Buf *out, int depth, int lineno);

static void expand_macro_use(Macro *m, char **args, int na, Buf *out, int depth, int lineno) {
    Buf b = {0};
    const char *q = m->body;
    while (*q) {
        if (q[0] == '`' && q[1] == '"') { bputc(&b, '"'); q += 2; continue; }
        if (q[0] == '`' && q[1] == '`') { q += 2; continue; }
        if (q[0] == '`' && (isalpha((unsigned char)q[1]) || q[1] == '_')) {
            bputc(&b, *q++);
            while (isalnum((unsigned char)*q) || *q == '_' || *q == '$') bputc(&b, *q++);
            continue;
        }
        if (*q == '"') {
            bputc(&b, *q++);
            while (*q && *q != '"') { if (*q == '\\' && q[1]) bputc(&b, *q++); bputc(&b, *q++); }
            if (*q) bputc(&b, *q++);
            continue;
        }
        if (isalpha((unsigned char)*q) || *q == '_') {
            const char *st = q;
            while (isalnum((unsigned char)*q) || *q == '_' || *q == '$') q++;
            int found = 0;
            for (int i = 0; i < m->np; i++) {
                if (strlen(m->params[i]) == (size_t)(q - st) && !strncmp(m->params[i], st, q - st)) {
                    const char *a = (i < na && args[i][0]) ? args[i] : (m->defs[i] ? m->defs[i] : "");
                    bputs(&b, a); found = 1; break;
                }
            }
            if (!found) bput(&b, st, q - st);
            continue;
        }
        bputc(&b, *q++);
    }
    if (depth > 64) { warn(lineno, "macro expansion too deep (`%s)", m->name); return; }
    expand(bstr(&b), out, depth + 1, lineno);
}

static void expand(const char *s, Buf *out, int depth, int lineno) {
    while (*s) {
        if (*s == '"') {
            bputc(out, *s++);
            while (*s && *s != '"') { if (*s == '\\' && s[1]) bputc(out, *s++); bputc(out, *s++); }
            if (*s) bputc(out, *s++);
            continue;
        }
        if (*s == '\\') {           /* escaped identifier: copy verbatim */
            while (*s && !isspace((unsigned char)*s)) bputc(out, *s++);
            continue;
        }
        if (*s == '`' && (isalpha((unsigned char)s[1]) || s[1] == '_')) {
            const char *q = s + 1;
            while (isalnum((unsigned char)*q) || *q == '_' || *q == '$') q++;
            char *name = xstrndup(s + 1, q - s - 1);
            s = q;
            Macro *m = find_macro(name);
            if (!m) {
                if (is_in(name, DIRECTIVES)) warn(lineno, "directive `%s in the middle of a line ignored", name);
                else if (!strcmp(name, "__LINE__")) { char t[32]; snprintf(t, sizeof t, "%d", lineno); bputs(out, t); }
                else if (!strcmp(name, "__FILE__")) { bputc(out, '"'); bputs(out, cur_file); bputc(out, '"'); }
                else warn(lineno, "undefined macro `%s", name);
                continue;
            }
            char *args[64]; int na = 0;
            if (m->np >= 0) {
                const char *r = s;
                while (*r == ' ' || *r == '\t') r++;
                if (*r == '(') {
                    r++;
                    for (;;) {
                        Buf a = {0}; int dep = 0;
                        while (*r) {
                            if (*r == '"') {
                                bputc(&a, *r++);
                                while (*r && *r != '"') { if (*r == '\\' && r[1]) bputc(&a, *r++); bputc(&a, *r++); }
                                if (*r) bputc(&a, *r++);
                                continue;
                            }
                            if ((*r == ',' || *r == ')') && dep == 0) break;
                            if (*r == '(' || *r == '[' || *r == '{') dep++;
                            if (*r == ')' || *r == ']' || *r == '}') dep--;
                            bputc(&a, *r++);
                        }
                        if (na < 64) args[na++] = trim(bstr(&a));
                        if (*r == ',') { r++; continue; }
                        if (*r == ')') r++;
                        else warn(lineno, "unterminated arguments for macro `%s", name);
                        break;
                    }
                    s = r;
                } else if (m->np > 0) {
                    warn(lineno, "macro `%s needs arguments", name);
                }
            }
            expand_macro_use(m, args, na, out, depth, lineno);
            continue;
        }
        bputc(out, *s++);
    }
}

static void process_text(const char *text, Buf *out, const char *fname, int flatten, int depth);

static void do_include(const char *p, Buf *out, const char *fname, int lineno, int depth) {
    while (*p == ' ' || *p == '\t') p++;
    char close = *p == '"' ? '"' : *p == '<' ? '>' : 0;
    if (!close) { warn(lineno, "bad `include"); return; }
    p++;
    const char *e = strchr(p, close);
    if (!e) { warn(lineno, "bad `include"); return; }
    char *fn = xstrndup(p, e - p);
    char *path = NULL, *src = NULL;
    if (fn[0] == '/') { path = fn; src = read_file(path); }
    if (!src) {
        const char *sl = strrchr(fname, '/');
        path = sl ? sfmt("%.*s/%s", (int)(sl - fname), fname, fn) : xstrdup(fn);
        src = read_file(path);
    }
    for (int i = 0; !src && i < nincdirs; i++) { path = sfmt("%s/%s", incdirs[i], fn); src = read_file(path); }
    if (!src) { warn(lineno, "cannot open include file '%s' (skipped)", fn); return; }
    if (depth > 32) { warn(lineno, "include nesting too deep"); return; }
    process_text(strip_comments(src), out, path, 1, depth + 1);
}

static void handle_line(const char *line, Buf *out, const char *fname, int lineno, int depth) {
    const char *s = line;
    while (*s == ' ' || *s == '\t' || *s == '\r') s++;
    if (*s == '`') {
        char w[64]; const char *p = read_word(s + 1, w, sizeof w);
        if (is_in(w, DIRECTIVES)) {
            char name[512];
            if (!strcmp(w, "ifdef") || !strcmp(w, "ifndef")) {
                read_word(p, name, sizeof name);
                int d = find_macro(name) != NULL;
                if (w[2] == 'n') d = !d;
                if (if_depth >= MAXIF) { warn(lineno, "`ifdef nesting too deep"); return; }
                int par = pp_on();
                if_active[if_depth] = par && d; if_taken[if_depth] = d; if_depth++;
                return;
            }
            if (!strcmp(w, "elsif")) {
                if (!if_depth) { warn(lineno, "`elsif without `ifdef"); return; }
                read_word(p, name, sizeof name);
                int d = find_macro(name) != NULL, par = pp_parent_on();
                if (if_taken[if_depth - 1]) if_active[if_depth - 1] = 0;
                else { if_active[if_depth - 1] = par && d; if (d) if_taken[if_depth - 1] = 1; }
                return;
            }
            if (!strcmp(w, "else")) {
                if (!if_depth) { warn(lineno, "`else without `ifdef"); return; }
                if_active[if_depth - 1] = pp_parent_on() && !if_taken[if_depth - 1];
                if_taken[if_depth - 1] = 1;
                return;
            }
            if (!strcmp(w, "endif")) {
                if (!if_depth) warn(lineno, "`endif without `ifdef"); else if_depth--;
                return;
            }
            if (!pp_on()) return;
            if (!strcmp(w, "define")) {
                p = read_word(p, name, sizeof name);
                int np = -1; char **params = NULL, **defs = NULL;
                if (*p == '(') {
                    np = 0; p++;
                    params = xmalloc(64 * sizeof(char *)); defs = xmalloc(64 * sizeof(char *));
                    while (*p && *p != ')') {
                        while (*p == ' ' || *p == '\t' || *p == ',') p++;
                        char pn[256]; p = read_word(p, pn, sizeof pn);
                        while (*p == ' ' || *p == '\t') p++;
                        char *def = NULL;
                        if (*p == '=') {
                            p++; const char *st = p; int dep = 0;
                            while (*p && !((*p == ',' || *p == ')') && dep == 0)) {
                                if (*p == '(') dep++;
                                if (*p == ')') dep--;
                                p++;
                            }
                            def = trim(xstrndup(st, p - st));
                        }
                        if (pn[0] && np < 64) { params[np] = xstrdup(pn); defs[np] = def; np++; }
                        else if (!pn[0] && *p && *p != ')' && *p != ',') p++;
                    }
                    if (*p == ')') p++;
                }
                define_macro(name, np, params, defs, trim(xstrdup(p)));
                return;
            }
            if (!strcmp(w, "undef")) { read_word(p, name, sizeof name); undef_macro(name); return; }
            if (!strcmp(w, "undefineall")) { nmacros = 0; return; }
            if (!strcmp(w, "include")) { do_include(p, out, fname, lineno, depth); return; }
            return; /* other directives: ignore the whole line */
        }
    }
    if (!pp_on()) return;
    expand(line, out, 0, lineno);
}

static void process_text(const char *p, Buf *out, const char *fname, int flatten, int depth) {
    int lineno = 1;
    while (*p) {
        Buf line = {0}; int extra = 0;
        for (;;) {
            const char *e = strchr(p, '\n');
            size_t len = e ? (size_t)(e - p) : strlen(p), l2 = len;
            while (l2 > 0 && p[l2 - 1] == '\r') l2--;
            if (l2 > 0 && p[l2 - 1] == '\\' && e) {
                bput(&line, p, l2 - 1); bputc(&line, ' ');
                p = e + 1; extra++;
                continue;
            }
            bput(&line, p, len);
            p = e ? e + 1 : p + len;
            break;
        }
        handle_line(bstr(&line), out, fname, lineno, depth);
        for (int i = 0; i <= extra; i++) bputc(out, flatten ? ' ' : '\n');
        lineno += 1 + extra;
        free(line.s);
    }
}

/* ================================================================ lexer */

typedef enum { T_EOF, T_ID, T_NUM, T_STR, T_OP } TK;
typedef struct { TK k; char *s; int line; char *attr; } Tok;
static Tok **toks; static int ntoks, captoks, P;
static char *pending_attr;

static const char *OPS[] = {
    "<<<=", ">>>=", "===", "!==", "==?", "!=?", "<<<", ">>>", "<<=", ">>=", "|->", "|=>", "<->",
    "->>", "==", "!=", "&&", "||", "<=", ">=", "<<", ">>", "**", "~&", "~|", "~^", "^~", "+:",
    "-:", "::", "++", "--", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "->", ".*", "##", NULL };

static void push_tok(TK k, const char *s, size_t n, int line) {
    if (ntoks == captoks) { captoks = captoks ? captoks * 2 : 1024; toks = xrealloc(toks, captoks * sizeof(Tok *)); }
    Tok *t = xmalloc(sizeof *t);
    toks[ntoks++] = t;
    t->k = k; t->s = xstrndup(s, n); t->line = line; t->attr = pending_attr; pending_attr = NULL;
}

static int isbasechar(char c) { return c && strchr("bBoOdDhH", c); }
static int isnumdigit(char c) { return c && (isxdigit((unsigned char)c) || strchr("xXzZ?_", c)); }

static char *carry; static int carry_line;   /* unfinished (* attribute *) spanning lines */

/* tokenize one chunk of preprocessed text, appending to toks[] */
static void tokenize_chunk(const char *p, int line) {
    for (;;) {
        while (*p && isspace((unsigned char)*p)) { if (*p == '\n') line++; p++; }
        if (!*p) break;
        const char *st = p;
        /* attribute (* ... *) but not @(*) */
        if (p[0] == '(' && p[1] == '*') {
            const char *q = p + 2;
            while (*q == ' ' || *q == '\t') q++;
            if (*q != ')') {
                const char *e = strstr(p + 2, "*)");
                if (e) {
                    for (const char *x = p; x < e; x++) if (*x == '\n') line++;
                    char *raw = xstrndup(p + 2, e - p - 2);
                    free(pending_attr);
                    pending_attr = xstrdup(trim(raw));
                    free(raw);
                    p = e + 2;
                    continue;
                }
                carry = xstrdup(p); carry_line = line;   /* finish with the next line */
                return;
            }
        }
        if (isalpha((unsigned char)*p) || *p == '_' || *p == '$') {
            while (isalnum((unsigned char)*p) || *p == '_' || *p == '$') p++;
            push_tok(T_ID, st, p - st, line);
            continue;
        }
        if (*p == '\\') {
            p++; st = p;
            while (*p && !isspace((unsigned char)*p)) p++;
            push_tok(T_ID, st, p - st, line);
            continue;
        }
        if (isdigit((unsigned char)*p)) {
            const char *q = p; int isreal = 0, unit = 0;
            while (isdigit((unsigned char)*q) || *q == '_') q++;
            if (*q == '.' && isdigit((unsigned char)q[1])) { q++; while (isdigit((unsigned char)*q) || *q == '_') q++; isreal = 1; }
            if ((*q == 'e' || *q == 'E') && (isdigit((unsigned char)q[1]) || ((q[1] == '+' || q[1] == '-') && isdigit((unsigned char)q[2])))) {
                q += 2; while (isdigit((unsigned char)*q)) q++; isreal = 1;
            }
            static const char *units[] = { "fs", "ps", "ns", "us", "ms", "s", NULL };
            for (int i = 0; units[i]; i++) {
                size_t l = strlen(units[i]);
                if (!strncmp(q, units[i], l) && !(isalnum((unsigned char)q[l]) || q[l] == '_')) { q += l; unit = 1; break; }
            }
            if (!isreal && !unit) {
                const char *r = q;
                while (*r == ' ' || *r == '\t') r++;
                if (*r == '\'') {
                    const char *b = r + 1;
                    if (*b == 's' || *b == 'S') b++;
                    if (isbasechar(*b)) {
                        b++;
                        while (*b == ' ' || *b == '\t') b++;
                        while (isnumdigit(*b)) b++;
                        Buf t = {0};
                        bput(&t, p, q - p);
                        for (const char *x = r; x < b; x++) if (*x != ' ' && *x != '\t') bputc(&t, *x);
                        push_tok(T_NUM, t.s, t.n, line);
                        p = b;
                        continue;
                    }
                }
            }
            push_tok(T_NUM, p, q - p, line);
            p = q;
            continue;
        }
        if (*p == '\'') {
            const char *b = p + 1;
            if (*b == 's' || *b == 'S') b++;
            if (isbasechar(*b)) {
                b++;
                while (*b == ' ' || *b == '\t') b++;
                while (isnumdigit(*b)) b++;
                Buf t = {0};
                for (const char *x = p; x < b; x++) if (*x != ' ' && *x != '\t') bputc(&t, *x);
                push_tok(T_NUM, t.s, t.n, line);
                p = b;
                continue;
            }
            if (p[1] && strchr("01xXzZ", p[1]) && !(isalnum((unsigned char)p[2]) || p[2] == '_')) {
                push_tok(T_NUM, p, 2, line); p += 2; continue;
            }
            if (p[1] == '{') { push_tok(T_OP, p, 2, line); p += 2; continue; }
            push_tok(T_OP, p, 1, line); p++;
            continue;
        }
        if (*p == '"') {
            p++; st = p;
            while (*p && *p != '"') { if (*p == '\\' && p[1]) p++; if (*p == '\n') line++; p++; }
            push_tok(T_STR, st, p - st, line);
            if (*p) p++;
            continue;
        }
        int matched = 0;
        for (int i = 0; OPS[i]; i++) {
            size_t l = strlen(OPS[i]);
            if (!strncmp(p, OPS[i], l)) { push_tok(T_OP, p, l, line); p += l; matched = 1; break; }
        }
        if (matched) continue;
        push_tok(T_OP, p, 1, line); p++;
    }
}

/* ---------------------------------------------------------------- streaming input */

static FILE *in_f;
static int in_line, in_comment, in_eof, eof_pushed;

/* strip comments from one physical line; *inc carries block-comment state */
static char *strip_line(const char *p, int *inc) {
    Buf b = {0};
    while (*p) {
        if (*inc) {
            const char *e = strstr(p, "*/");
            if (!e) break;
            p = e + 2; *inc = 0; bputc(&b, ' ');
            continue;
        }
        if (*p == '"') {
            bputc(&b, *p++);
            while (*p && *p != '"') {
                if (*p == '\\' && p[1]) { bput(&b, p, 2); p += 2; continue; }
                bputc(&b, *p++);
            }
            if (*p == '"') bputc(&b, *p++);
            continue;
        }
        if (p[0] == '/' && p[1] == '/') break;
        if (p[0] == '/' && p[1] == '*') { *inc = 1; p += 2; continue; }
        bputc(&b, *p++);
    }
    return bstr(&b);
}

/* read one logical line (joining backslash continuations), preprocess and tokenize it */
static int feed(void) {
    if (in_eof) return 0;
    Buf lg = {0};
    char *raw = NULL; size_t cap = 0;
    int nphys = 0, first = in_line + 1;
    for (;;) {
        ssize_t n = getline(&raw, &cap, in_f);
        if (n < 0) {
            if (!nphys) {
                in_eof = 1; free(raw);
                if (carry) { warn(carry_line, "unterminated attribute"); free(carry); carry = NULL; }
                return 0;
            }
            break;
        }
        in_line++; nphys++;
        while (n > 0 && (raw[n - 1] == '\n' || raw[n - 1] == '\r')) raw[--n] = 0;
        char *s = strip_line(raw, &in_comment);
        size_t l = strlen(s);
        while (l > 0 && (s[l - 1] == ' ' || s[l - 1] == '\t')) l--;
        if (l > 0 && s[l - 1] == '\\') { bput(&lg, s, l - 1); bputc(&lg, ' '); free(s); continue; }
        bputs(&lg, s); free(s);
        break;
    }
    free(raw);
    Buf out = {0};
    int tline = first;
    if (carry) { bputs(&out, carry); bputc(&out, ' '); free(carry); carry = NULL; tline = carry_line; }
    handle_line(bstr(&lg), &out, cur_file, first, 0);
    tokenize_chunk(bstr(&out), tline);
    free(lg.s); free(out.s);
    return 1;
}

static void ensure_tok(int i) {
    while (ntoks <= i && !eof_pushed)
        if (!feed()) { push_tok(T_EOF, "", 0, in_line); eof_pushed = 1; }
}

/* forget tokens the parser has finished with */
static void drop_consumed(void) {
    if (P > ntoks) P = ntoks;
    for (int i = 0; i < P; i++) { free(toks[i]->s); free(toks[i]->attr); free(toks[i]); }
    memmove(toks, toks + P, (ntoks - P) * sizeof(Tok *));
    ntoks -= P; P = 0;
}

/* ================================================================ parser infrastructure */

static const char *NET_TYPES[] = { "wire", "tri", "wand", "wor", "triand", "trior", "tri0", "tri1",
    "supply0", "supply1", "uwire", "trireg", NULL };
static const char *DATA_TYPES[] = { "reg", "logic", "bit", "byte", "shortint", "int", "longint",
    "integer", "time", "real", "realtime", "shortreal", "string", "genvar", "event", "chandle", "void", NULL };
static const char *DIRS[] = { "input", "output", "inout", "ref", NULL };
static const char *GATES[] = { "and", "nand", "or", "nor", "xor", "xnor", "not", "buf", "bufif0",
    "bufif1", "notif0", "notif1", "nmos", "pmos", "cmos", "rnmos", "rpmos", "rcmos", "tran", "rtran",
    "tranif0", "tranif1", "rtranif0", "rtranif1", "pullup", "pulldown", NULL };
static const char *STRENGTHS[] = { "supply0", "supply1", "strong0", "strong1", "pull0", "pull1",
    "weak0", "weak1", "highz0", "highz1", "small", "medium", "large", NULL };
static const char *ALWAYS_KW[] = { "always", "always_ff", "always_comb", "always_latch", NULL };
static const char *UNIT_END[] = { "endmodule", "endinterface", "endpackage", "endprogram", NULL };
static const char *RESERVED[] = {
    "alias", "always", "always_comb", "always_ff", "always_latch", "assert", "assign", "assume",
    "automatic", "begin", "bind", "break", "case", "casex", "casez", "class", "clocking", "const",
    "constraint", "continue", "cover", "covergroup", "deassign", "default", "defparam", "disable",
    "do", "edge", "else", "end", "endcase", "endclass", "endclocking", "endfunction", "endgenerate",
    "endgroup", "endinterface", "endmodule", "endpackage", "endprogram", "endproperty",
    "endsequence", "endspecify", "endtask", "enum", "export", "extends", "final", "for", "force",
    "foreach", "forever", "fork", "function", "generate", "if", "iff", "import", "initial", "inside",
    "interface", "join", "join_any", "join_none", "localparam", "macromodule", "modport", "module",
    "negedge", "package", "packed", "parameter", "posedge", "priority", "program", "property",
    "release", "repeat", "return", "sequence", "signed", "specify", "static", "struct", "task",
    "typedef", "union", "unique", "unique0", "unsigned", "var", "wait", "while", "with", "type",
    "scalared", "vectored", "restrict", "timeunit", "timeprecision", NULL };
static const char *ITEM_KW[] = {
    "always", "always_ff", "always_comb", "always_latch", "initial", "final", "assign", "function",
    "task", "input", "output", "inout", "wire", "reg", "logic", "tri", "integer", "parameter",
    "localparam", "typedef", "generate", "endgenerate", "genvar", "module", "endmodule", "interface",
    "endinterface", "package", "endpackage", "program", "endprogram", NULL };

static int is_reserved(const char *s) {
    return is_in(s, RESERVED) || is_in(s, NET_TYPES) || is_in(s, DATA_TYPES) || is_in(s, DIRS) || is_in(s, GATES);
}

static jmp_buf *errjb;

static Tok *pk(int o) { int i = P + o; ensure_tok(i); if (i >= ntoks) i = ntoks - 1; return toks[i]; }
static Tok *cur(void) { return pk(0); }
static int tis(Tok *t, const char *s) { return (t->k == T_ID || t->k == T_OP) && !strcmp(t->s, s); }
static int is(const char *s) { return tis(cur(), s); }
static void adv(void) { if (cur()->k != T_EOF) P++; }
static int accept(const char *s) { if (is(s)) { adv(); return 1; } return 0; }

static void perr(const char *fmt, ...) {
    Tok *t = cur();
    va_list ap; va_start(ap, fmt);
    fprintf(stderr, "%s:%d: error: ", cur_file, t->line);
    vfprintf(stderr, fmt, ap);
    fprintf(stderr, " (near '%s')\n", t->k == T_EOF ? "<EOF>" : t->s);
    va_end(ap);
    if (++nerrors > 200) { fprintf(stderr, "too many errors, giving up\n"); exit(1); }
    longjmp(*errjb, 1);
}
static void expect(const char *s) { if (!accept(s)) perr("expected '%s'", s); }
static char *expect_id(void) {
    if (cur()->k != T_ID) perr("expected identifier");
    char *s = cur()->s; adv(); return s;
}

static void skip_balanced(void) {      /* at '(' '[' or '{' : skip through the matching closer */
    int d = 0;
    do {
        if (cur()->k == T_EOF) perr("unbalanced brackets");
        if (is("(") || is("[") || is("{") || is("'{")) d++;
        else if (is(")") || is("]") || is("}")) d--;
        adv();
    } while (d > 0);
}
static void skip_to_semi(void) {
    int d = 0;
    while (cur()->k != T_EOF) {
        if (is("(") || is("[") || is("{") || is("'{")) d++;
        else if (is(")") || is("]") || is("}")) d--;
        else if (is(";") && d <= 0) { adv(); return; }
        adv();
    }
}
static void skip_until(const char *kw) {
    while (cur()->k != T_EOF && !is(kw)) adv();
    adv();
    if (accept(":")) adv();
}

/* ================================================================ contexts */

typedef struct Ctx Ctx;
struct Ctx {
    Node *mod;
    Node *ports, *nets, *assigns, *always, *localparams, *parameters, *structures, *initials,
         *typedefs, *instances, *generates, *functions, *imports;
    Node *pvals;    /* name -> Int : evaluated constants (not printed) */
    Ctx *parent;
};

static char **seen_names; static int nseen;
static void emit_entry(const char *name, Node *mod);
static Ctx *unit_ctx;
static char **pkg_names; static Ctx **pkg_ctxs; static int npkgs;
static int anon_count;

static Ctx *new_ctx(Ctx *parent, const char *kind) {
    Ctx *c = palloc(sizeof *c); memset(c, 0, sizeof *c);
    c->parent = parent;
    c->mod = Dict();
    dset(c->mod, "kind", kind ? Str(kind) : None());
    dset(c->mod, "line", None());
#define K(f, name, ctor) c->f = ctor(); dset(c->mod, name, c->f);
    c->ports = List();   /* port order kept internally, not printed */
    K(nets, "nets", Dict)
    K(assigns, "assigns", List)
    K(always, "always", List)
    K(localparams, "localparams", Dict)
    K(parameters, "parameters", Dict)
    K(structures, "structures", Dict)
    K(initials, "initials", List)
    K(typedefs, "typedefs", Dict)
    K(instances, "instances", Dict)
    K(generates, "generates", List)
    K(functions, "functions", Dict)
    K(imports, "imports", List)
#undef K
    c->pvals = Dict();
    return c;
}

static Ctx *find_pkg(const char *name) {
    for (int i = 0; i < npkgs; i++) if (!strcmp(pkg_names[i], name)) return pkg_ctxs[i];
    return NULL;
}

/* kind 0: constant value (Int) ; kind 1: type (struct / typedef entry) */
static Node *sym_in(Ctx *x, const char *name, int kind) {
    if (kind == 0) { Node *v = dget(x->pvals, name); return (v && v->k == N_INT) ? v : NULL; }
    Node *v = dget(x->structures, name);
    return v ? v : dget(x->typedefs, name);
}
static Node *find_sym(Ctx *c, const char *name, int kind) {
    const char *cc = strstr(name, "::");
    if (cc) {
        Ctx *p = find_pkg(xstrndup(name, cc - name));
        return p ? sym_in(p, cc + 2, kind) : NULL;
    }
    for (Ctx *x = c; x; x = x->parent) {
        Node *v = sym_in(x, name, kind);
        if (v) return v;
        for (int i = 0; i < x->imports->n; i++) {
            const char *imp = x->imports->items[i]->s, *q = strstr(imp, "::");
            if (!q) continue;
            if (strcmp(q + 2, "*") && strcmp(q + 2, name)) continue;
            Ctx *p = find_pkg(xstrndup(imp, q - imp));
            if (p && (v = sym_in(p, name, kind))) return v;
        }
    }
    if (kind == 1)  /* lenient: a type from any package */
        for (int i = 0; i < npkgs; i++) { Node *v = sym_in(pkg_ctxs[i], name, kind); if (v) return v; }
    return NULL;
}
static Node *find_type(Ctx *c, const char *name) { return find_sym(c, name, 1); }

/* ================================================================ constant evaluation */

static int ceval(Ctx *c, Node *e, long long *out) {
    long long a, b, x;
    switch (e->k) {
    case N_INT: *out = e->i; return 1;
    case N_STR: { Node *v = find_sym(c, e->s, 0); if (v) { *out = v->i; return 1; } return 0; }
    case N_TUPLE: break;
    default: return 0;
    }
    if (e->n < 1 || e->items[0]->k != N_STR) return 0;
    const char *op = e->items[0]->s;
    if (!strcmp(op, "const")) { if (e->items[4]->k == N_INT) { *out = e->items[4]->i; return 1; } return 0; }
    if (!strcmp(op, "cast")) return ceval(c, e->items[2], out);
    if (!strcmp(op, "call") && e->n == 3 && !strcmp(e->items[1]->s, "$clog2")) {
        if (!ceval(c, e->items[2], &a)) return 0;
        x = 0; while ((1LL << x) < a) x++;
        *out = x; return 1;
    }
    if (!strcmp(op, "?:") && e->n == 4) {
        if (!ceval(c, e->items[1], &a)) return 0;
        return ceval(c, a ? e->items[2] : e->items[3], out);
    }
    if (e->n == 2) {
        if (!ceval(c, e->items[1], &a)) return 0;
        if (!strcmp(op, "-")) *out = -a;
        else if (!strcmp(op, "+")) *out = a;
        else if (!strcmp(op, "~")) *out = ~a;
        else if (!strcmp(op, "!")) *out = !a;
        else return 0;
        return 1;
    }
    if (e->n == 3) {
        if (!ceval(c, e->items[1], &a) || !ceval(c, e->items[2], &b)) return 0;
        if (!strcmp(op, "+")) *out = a + b;
        else if (!strcmp(op, "-")) *out = a - b;
        else if (!strcmp(op, "*")) *out = a * b;
        else if (!strcmp(op, "/")) { if (!b) return 0; *out = a / b; }
        else if (!strcmp(op, "%")) { if (!b) return 0; *out = a % b; }
        else if (!strcmp(op, "**")) { x = 1; for (long long i = 0; i < b && i < 64; i++) x *= a; *out = x; }
        else if (!strcmp(op, "<<") || !strcmp(op, "<<<")) *out = a << b;
        else if (!strcmp(op, ">>") || !strcmp(op, ">>>")) *out = a >> b;
        else if (!strcmp(op, "&")) *out = a & b;
        else if (!strcmp(op, "|")) *out = a | b;
        else if (!strcmp(op, "^")) *out = a ^ b;
        else if (!strcmp(op, "==")) *out = a == b;
        else if (!strcmp(op, "!=")) *out = a != b;
        else if (!strcmp(op, "<")) *out = a < b;
        else if (!strcmp(op, "<=")) *out = a <= b;
        else if (!strcmp(op, ">")) *out = a > b;
        else if (!strcmp(op, ">=")) *out = a >= b;
        else if (!strcmp(op, "&&")) *out = a && b;
        else if (!strcmp(op, "||")) *out = a || b;
        else return 0;
        return 1;
    }
    return 0;
}

static long long dim_size(Ctx *c, Node *d) {
    long long a, b;
    if (d->k != N_TUPLE || d->n != 2) return -1;
    if (!ceval(c, d->items[0], &a) || !ceval(c, d->items[1], &b)) return -1;
    return (a > b ? a - b : b - a) + 1;
}

typedef struct { char *type; int expl; int sgn; int is_net; Node *packed; } TInfo;

static long long base_width(Ctx *c, const char *type) {
    if (!type) return 1;
    const char *t = strrchr(type, ' ');
    t = t ? t + 1 : type;
    if (is_in(t, NET_TYPES) || !strcmp(t, "reg") || !strcmp(t, "logic") || !strcmp(t, "bit")) return 1;
    if (!strcmp(t, "byte")) return 8;
    if (!strcmp(t, "shortint")) return 16;
    if (!strcmp(t, "int") || !strcmp(t, "integer")) return 32;
    if (!strcmp(t, "longint") || !strcmp(t, "time")) return 64;
    if (is_in(t, DATA_TYPES)) return -1;
    Node *e = find_type(c, type);
    if (e) { Node *w = dget(e, "width"); if (w && w->k == N_INT) return w->i; }
    return -1;
}
static long long type_width(Ctx *c, TInfo *ti) {
    long long w = base_width(c, ti->type);
    if (w < 0) return -1;
    for (int i = 0; ti->packed && i < ti->packed->n; i++) {
        long long s = dim_size(c, ti->packed->items[i]);
        if (s < 0) return -1;
        w *= s;
    }
    return w;
}

/* ================================================================ expressions */

static Node *parse_expr(void);
static Node *parse_unary(void);

static Node *num_node(const char *t) {
    const char *q = strchr(t, '\'');
    Buf b = {0};
    if (!q) {
        size_t l = strlen(t);
        if (l && isalpha((unsigned char)t[l - 1])) return tup(Str("time"), Str(t), NULL);
        if (strpbrk(t, ".eE")) return tup(Str("real"), Str(t), NULL);
        for (const char *x = t; *x; x++) if (*x != '_') bputc(&b, *x);
        long long v = strtoll(bstr(&b), NULL, 10);
        free(b.s);
        return Int(v);
    }
    Node *w = None();
    if (q != t) {
        for (const char *x = t; x < q; x++) if (*x != '_') bputc(&b, *x);
        w = Int(atoll(bstr(&b)));
        free(b.s);
    }
    const char *p = q + 1; int sg = 0;
    if (*p == 's' || *p == 'S') { sg = 1; p++; }
    if (!isbasechar(*p)) return tup(Str("fill"), Str(q + 1), NULL);
    char base = tolower((unsigned char)*p++);
    Buf d = {0};
    for (; *p; p++) if (*p != '_') bputc(&d, tolower((unsigned char)*p));
    char *digits = bstr(&d);
    int bits = base == 'b' ? 1 : base == 'o' ? 3 : base == 'h' ? 4 : 0;
    unsigned long long v = 0; int ok = digits[0] != 0, nbits = 0;
    for (char *x = digits; *x && ok; x++) {
        int dv;
        if (isdigit((unsigned char)*x)) dv = *x - '0';
        else if (*x >= 'a' && *x <= 'f') dv = *x - 'a' + 10;
        else { ok = 0; break; }
        if (bits) {
            if (dv >= (1 << bits)) { ok = 0; break; }
            v = (v << bits) | dv; nbits += bits;
            if (nbits > 64 && v >> 63) ok = 0;
        } else {
            if (dv > 9) { ok = 0; break; }
            v = v * 10 + dv;
        }
    }
    char bs[3] = { 0 }; if (sg) { bs[0] = 's'; bs[1] = base; } else bs[0] = base;
    Node *r = tup(Str("const"), w, Str(bs), Str(digits), ok && v <= (unsigned long long)9223372036854775807LL ? Int((long long)v) : None(), NULL);
    free(digits);
    return r;
}

static Node *parse_concat(void) {
    expect("{");
    if (is("<<") || is(">>")) {          /* streaming concatenation */
        char *op = cur()->s; adv();
        Node *sz = None();
        if (!is("{")) sz = parse_unary();
        Node *inner = parse_concat();
        expect("}");
        return tup(Str("stream"), Str(op), sz, inner, NULL);
    }
    Node *first = parse_expr();
    if (is("{")) {
        Node *inner = parse_concat();
        expect("}");
        return tup(Str("repl"), first, inner, NULL);
    }
    Node *c = tup(Str("concat"), first, NULL);
    while (accept(",")) add(c, parse_expr());
    expect("}");
    return c;
}

static Node *parse_pattern(void) {      /* after '{ */
    Node *p = tup(Str("pattern"), NULL);
    if (accept("}")) return p;
    do {
        if (accept("default")) { expect(":"); add(p, tup(Str("default"), parse_expr(), NULL)); continue; }
        Node *e = parse_expr();
        if (is("{")) { Node *inner = parse_concat(); e = tup(Str("repl"), e, inner, NULL); }
        if (accept(":")) e = tup(Str("key"), e, parse_expr(), NULL);
        add(p, e);
    } while (accept(","));
    expect("}");
    return p;
}

static Node *parse_primary(void) {
    Tok *t = cur();
    if (t->k == T_NUM) { adv(); return num_node(t->s); }
    if (t->k == T_STR) { adv(); return tup(Str("string"), Str(t->s), NULL); }
    if (accept("(")) {
        Node *e = parse_expr();
        if (accept(":")) { Node *typ = parse_expr(); expect(":"); parse_expr(); e = typ; }
        expect(")");
        return e;
    }
    if (is("{")) return parse_concat();
    if (accept("'{")) return parse_pattern();
    if (t->k == T_ID) {
        if (is_reserved(t->s) && !tis(pk(1), "'")) perr("unexpected keyword '%s' in expression", t->s);
        char *name = t->s; adv();
        while (is("::")) { adv(); name = sfmt("%s::%s", name, expect_id()); }
        if (is("(") && !is_reserved(name)) {
            adv();
            Node *c = tup(Str("call"), Str(name), NULL);
            if (!is(")")) do {
                if (is(",") || is(")")) add(c, None()); else add(c, parse_expr());
            } while (accept(","));
            expect(")");
            return c;
        }
        return Str(name);
    }
    perr("unexpected token in expression");
    return NULL;
}

static Node *parse_postfix(Node *e) {
    for (;;) {
        if (is("[")) {
            adv();
            Node *a = parse_expr();
            if (accept(":")) e = tup(Str("partsel"), e, a, parse_expr(), NULL);
            else if (accept("+:")) e = tup(Str("partsel+"), e, a, parse_expr(), NULL);
            else if (accept("-:")) e = tup(Str("partsel-"), e, a, parse_expr(), NULL);
            else e = tup(Str("bitsel"), e, a, NULL);
            expect("]");
            continue;
        }
        if (is(".") && pk(1)->k == T_ID) { adv(); e = tup(Str("member"), e, Str(expect_id()), NULL); continue; }
        if (is("'") && tis(pk(1), "(")) { adv(); adv(); Node *x = parse_expr(); expect(")"); e = tup(Str("cast"), e, x, NULL); continue; }
        break;
    }
    return e;
}

static const char *UNOPS[] = { "+", "-", "!", "~", "&", "~&", "|", "~|", "^", "~^", "^~", NULL };

static Node *parse_unary(void) {
    Tok *t = cur();
    if (t->k == T_OP) {
        for (int i = 0; UNOPS[i]; i++) if (!strcmp(t->s, UNOPS[i])) {
            adv();
            Node *o = parse_unary();
            return tup(Str(UNOPS[i]), o, NULL);
        }
        if (is("++") || is("--")) { adv(); Node *o = parse_unary(); return tup(Str(t->s), o, NULL); }
    }
    return parse_postfix(parse_primary());
}

static struct { const char *op; int prec; } BINOPS[] = {
    { "||", 1 }, { "&&", 2 }, { "|", 3 }, { "^", 4 }, { "^~", 4 }, { "~^", 4 }, { "&", 5 },
    { "==", 6 }, { "!=", 6 }, { "===", 6 }, { "!==", 6 }, { "==?", 6 }, { "!=?", 6 },
    { "<", 7 }, { "<=", 7 }, { ">", 7 }, { ">=", 7 }, { "inside", 7 },
    { "<<", 8 }, { ">>", 8 }, { "<<<", 8 }, { ">>>", 8 }, { "+", 9 }, { "-", 9 },
    { "*", 10 }, { "/", 10 }, { "%", 10 }, { "**", 11 }, { NULL, 0 } };

static int binprec(Tok *t) {
    if (t->k != T_OP && !(t->k == T_ID && !strcmp(t->s, "inside"))) return -1;
    for (int i = 0; BINOPS[i].op; i++) if (!strcmp(t->s, BINOPS[i].op)) return BINOPS[i].prec;
    return -1;
}

static Node *parse_bin(int minp) {
    Node *l = parse_unary();
    for (;;) {
        Tok *t = cur();
        int p = binprec(t);
        if (p < 0 || p < minp) break;
        char *op = t->s; adv();
        if (!strcmp(op, "inside")) {
            Node *n = tup(Str("inside"), l, NULL);
            expect("{");
            do {
                if (accept("[")) { Node *a = parse_expr(); expect(":"); Node *b = parse_expr(); expect("]"); add(n, tup(Str("range"), a, b, NULL)); }
                else add(n, parse_expr());
            } while (accept(","));
            expect("}");
            l = n;
            continue;
        }
        Node *r = parse_bin(p + 1);
        l = tup(Str(op), l, r, NULL);
    }
    return l;
}

static Node *parse_expr(void) {
    Node *c = parse_bin(1);
    if (accept("?")) {
        Node *a = parse_expr();
        expect(":");
        Node *b = parse_expr();
        return tup(Str("?:"), c, a, b, NULL);
    }
    return c;
}

static Node *parse_lvalue(void) {
    if (is("{")) return parse_postfix(parse_concat());
    if (cur()->k != T_ID) perr("expected lvalue");
    return parse_postfix(parse_primary());
}

static Node *parse_dim(void) {
    expect("[");
    if (accept("]")) return tup(None(), None(), NULL);
    if (is("$") && tis(pk(1), "]")) { adv(); adv(); return tup(None(), Str("$"), NULL); }
    Node *a = parse_expr(), *r;
    if (accept(":")) r = tup(a, parse_expr(), NULL);
    else if (a->k == N_INT) r = tup(Int(0), Int(a->i - 1), NULL);
    else r = tup(Int(0), tup(Str("-"), a, Int(1), NULL), NULL);
    expect("]");
    return r;
}

static Node *parse_delay(void) {       /* after '#' */
    if (accept("(")) {
        Node *e = parse_expr();
        while (accept(",")) parse_expr();
        expect(")");
        return e;
    }
    Tok *t = cur();
    if (t->k == T_NUM) { adv(); return num_node(t->s); }
    if (t->k == T_ID) { adv(); return Str(t->s); }
    perr("bad delay value");
    return NULL;
}

static Node *parse_event(void) {       /* after '@' */
    if (accept("*")) return Str("*");
    if (accept("(")) {
        if (is("*") && tis(pk(1), ")")) { adv(); adv(); return Str("*"); }
        Node *l = List();
        do {
            const char *edge = "level";
            if (accept("posedge")) edge = "posedge";
            else if (accept("negedge")) edge = "negedge";
            else if (accept("edge")) edge = "edge";
            Node *e = parse_expr();
            if (accept("iff")) parse_expr();
            add(l, tup(Str(edge), e, NULL));
        } while (accept("or") || accept(","));
        expect(")");
        return l;
    }
    Node *l = List();
    add(l, tup(Str("level"), Str(expect_id()), NULL));
    return l;
}

/* ================================================================ types & declarations */

static Node *parse_struct_body(Ctx *c, int line);
static Node *parse_enum_body(Ctx *c, int line);

static int looks_user_type(Ctx *c) {
    Tok *t = cur(), *n = pk(1);
    if (t->k != T_ID || is_reserved(t->s)) return 0;
    if (tis(n, "::")) return 1;
    if (n->k == T_ID && !is_reserved(n->s)) return 1;
    if (tis(n, "[")) return find_type(c, t->s) != NULL;
    return 0;
}

static int parse_type(Ctx *c, TInfo *ti, int allow_user) {
    memset(ti, 0, sizeof *ti);
    ti->packed = List();
    Buf tb = {0}; int any = 0, var = 0;
    for (;;) {
        Tok *t = cur();
        if (t->k != T_ID) break;
        if (is_in(t->s, NET_TYPES) || is_in(t->s, DATA_TYPES)) {
            if (is_in(t->s, NET_TYPES)) ti->is_net = 1;
            if (tb.n) bputc(&tb, ' ');
            bputs(&tb, t->s); adv(); any = 1;
            continue;
        }
        if (!strcmp(t->s, "var")) { adv(); any = var = 1; continue; }
        if (!strcmp(t->s, "const") || !strcmp(t->s, "automatic") || !strcmp(t->s, "static")) { adv(); continue; }
        if (!strcmp(t->s, "signed")) { ti->sgn = 1; adv(); any = 1; continue; }
        if (!strcmp(t->s, "unsigned")) { adv(); any = 1; continue; }
        if (!tb.n && (!strcmp(t->s, "struct") || !strcmp(t->s, "union"))) {
            char *nm = sfmt("anon_struct_%d", ++anon_count);
            dset(c->structures, nm, parse_struct_body(c, t->line));
            bputs(&tb, nm); any = 1;
            continue;
        }
        if (!tb.n && !strcmp(t->s, "enum")) {
            char *nm = sfmt("anon_enum_%d", ++anon_count);
            dset(c->typedefs, nm, parse_enum_body(c, t->line));
            bputs(&tb, nm); any = 1;
            continue;
        }
        if (allow_user && !tb.n && looks_user_type(c)) {
            char *name = t->s; adv();
            while (accept("::")) name = sfmt("%s::%s", name, expect_id());
            bputs(&tb, name); any = 1;
            continue;
        }
        break;
    }
    if (is("(") && pk(1)->k == T_ID && is_in(pk(1)->s, STRENGTHS)) skip_balanced();
    while (accept("vectored") || accept("scalared")) ;
    while (is("[")) { add(ti->packed, parse_dim()); any = 1; }
    if (is("#")) { adv(); parse_delay(); }
    if (!tb.n && var) bputs(&tb, "logic");
    ti->type = tb.n ? pstrdup(tb.s) : NULL;
    free(tb.s);
    ti->expl = tb.n > 0;
    return any;
}

static Node *make_net(Ctx *c, const char *dir, TInfo *ti, Node *unp, int line, const char *attr) {
    Node *n = Dict();
    if (dir) dset(n, "dir", Str(dir));
    dset(n, "type", ti->type ? Str(ti->type) : None());
    dset(n, "signed", Bool(ti->sgn));
    dset(n, "packed", ti->packed ? ti->packed : List());
    long long w = type_width(c, ti);
    dset(n, "width", w >= 0 ? Int(w) : None());
    dset(n, "unpacked", unp ? unp : List());
    if (line > 0) dset(n, "line", Int(line));
    if (attr) dset(n, "attrs", Str(attr));
    return n;
}

static void add_net(Node *nets, const char *name, Node *n, int expl) {
    Node *e = dget(nets, name);
    if (!e) { dset(nets, name, n); return; }
    /* merge (non-ANSI style:  output q;  reg [7:0] q;) */
    Node *d = dget(n, "dir");
    if (d && strcmp(d->s, "internal")) dset(e, "dir", d);
    if (expl) dset(e, "type", dget(n, "type"));
    Node *pk_ = dget(n, "packed");
    if (pk_ && pk_->n) { dset(e, "packed", pk_); dset(e, "width", dget(n, "width")); }
    else if (expl && dget(n, "width")->k == N_INT && dget(e, "width")->k != N_INT) dset(e, "width", dget(n, "width"));
    if (dget(n, "signed")->i) dset(e, "signed", Bool(1));
    Node *u = dget(n, "unpacked");
    if (u && u->n) dset(e, "unpacked", u);
    Node *init = dget(n, "init");
    if (init) dset(e, "init", init);
}

/* declaration after optional direction: [type] [dims] name [dims] [= expr] {, ...} ; */
static void parse_decl(Ctx *c, Node *nets, const char *dir, int module_level) {
    int line = cur()->line;
    char *attr = cur()->attr;
    if (dir) adv();
    TInfo ti;
    parse_type(c, &ti, 1);
    int expl = ti.expl;
    if (!ti.type) { ti.type = "wire"; ti.is_net = 1; }
    if (cur()->k != T_ID) perr("expected declaration name");
    do {
        char *name = expect_id();
        Node *unp = List();
        while (is("[")) add(unp, parse_dim());
        Node *n = make_net(c, dir ? dir : "internal", &ti, unp, line, attr);
        if (accept("=")) {
            Node *e = parse_expr();
            if (module_level && ti.is_net) {
                Node *a = Dict();
                dset(a, "line", Int(line)); dset(a, "decl", Bool(1));
                if (attr) dset(a, "attrs", Str(attr));
                add(c->assigns, tup(Str(name), e, a, NULL));
            } else dset(n, "init", e);
        }
        add_net(nets, name, n, expl);
    } while (accept(","));
    expect(";");
}

static Node *parse_struct_body(Ctx *c, int line) {
    int isunion = is("union");
    adv();
    accept("tagged");
    int packed = accept("packed"), sg = 0;
    if (accept("signed")) sg = 1; else accept("unsigned");
    expect("{");
    Node *fields = Dict();
    long long total = 0; int known = 1;
    while (!accept("}")) {
        if (cur()->k == T_EOF) perr("unterminated struct");
        accept("rand"); accept("randc");
        TInfo ti;
        if (!parse_type(c, &ti, 1)) perr("expected struct field type");
        if (!ti.type) ti.type = "logic";
        do {
            char *fn = expect_id();
            Node *unp = List();
            while (is("[")) add(unp, parse_dim());
            Node *f = make_net(c, NULL, &ti, unp, 0, NULL);
            if (!unp->n) ddel(f, "unpacked");
            if (accept("=")) dset(f, "init", parse_expr());
            dset(fields, fn, f);
            Node *w = dget(f, "width");
            if (w->k == N_INT && !unp->n) { if (isunion) { if (w->i > total) total = w->i; } else total += w->i; }
            else known = 0;
        } while (accept(","));
        expect(";");
    }
    Node *s = Dict();
    dset(s, "kind", Str(isunion ? "union" : "struct"));
    dset(s, "packed", Bool(packed));
    dset(s, "signed", Bool(sg));
    dset(s, "fields", fields);
    dset(s, "width", known ? Int(total) : None());
    dset(s, "line", Int(line));
    return s;
}

static Node *parse_enum_body(Ctx *c, int line) {
    expect("enum");
    TInfo bt;
    parse_type(c, &bt, 1);
    if (!bt.type && !bt.packed->n) bt.type = "int";
    expect("{");
    Node *vals = Dict();
    long long next = 0; int known = 1;
    do {
        if (is("}")) break;
        char *n = expect_id();
        if (is("[")) skip_balanced();
        Node *v;
        if (accept("=")) {
            Node *e = parse_expr(); long long x;
            if (ceval(c, e, &x)) { v = Int(x); next = x + 1; known = 1; }
            else { v = e; known = 0; }
        } else v = known ? Int(next++) : None();
        dset(vals, n, v);
        if (v->k == N_INT) dset(c->pvals, n, v);
    } while (accept(","));
    expect("}");
    Node *e = Dict();
    dset(e, "kind", Str("enum"));
    dset(e, "type", bt.type ? Str(bt.type) : None());
    dset(e, "packed", bt.packed);
    long long w = type_width(c, &bt);
    dset(e, "width", w >= 0 ? Int(w) : None());
    dset(e, "values", vals);
    dset(e, "line", Int(line));
    return e;
}

static void parse_typedef(Ctx *c) {
    int line = cur()->line;
    expect("typedef");
    if (is("struct") || is("union")) {
        Node *s = parse_struct_body(c, line);
        char *n = expect_id();
        while (is("[")) parse_dim();
        expect(";");
        dset(c->structures, n, s);
        return;
    }
    if (is("enum")) {
        Node *e = parse_enum_body(c, line);
        char *n = expect_id();
        expect(";");
        dset(c->typedefs, n, e);
        return;
    }
    if (cur()->k == T_ID && tis(pk(1), ";")) { adv(); adv(); return; }                 /* forward */
    if (cur()->k == T_ID && pk(1)->k == T_ID && tis(pk(2), ";") && is_reserved(cur()->s) && !is_in(cur()->s, DATA_TYPES)) { adv(); adv(); adv(); return; }
    TInfo ti;
    parse_type(c, &ti, 1);
    char *n = expect_id();
    Node *unp = List();
    while (is("[")) add(unp, parse_dim());
    expect(";");
    Node *a = Dict();
    dset(a, "kind", Str("alias"));
    dset(a, "type", ti.type ? Str(ti.type) : None());
    dset(a, "signed", Bool(ti.sgn));
    dset(a, "packed", ti.packed);
    long long w = type_width(c, &ti);
    dset(a, "width", w >= 0 ? Int(w) : None());
    if (unp->n) dset(a, "unpacked", unp);
    dset(a, "line", Int(line));
    dset(c->typedefs, n, a);
}

static void add_param(Ctx *c, Node *dict, const char *name, TInfo *ti, Node *val, int line, int is_type) {
    Node *p = Dict();
    dset(p, "value", val);
    long long v;
    if (!is_type && val->k != N_NONE && ceval(c, val, &v)) { dset(p, "eval", Int(v)); dset(c->pvals, name, Int(v)); }
    if (is_type) dset(p, "type", Str("type"));
    else if (ti && ti->type) dset(p, "type", Str(ti->type));
    if (ti && ti->packed && ti->packed->n) dset(p, "packed", ti->packed);
    if (ti && ti->sgn) dset(p, "signed", Bool(1));
    dset(p, "line", Int(line));
    dset(dict, name, p);
}

/* header: after '#(' up to and including ')' ; body: after parameter/localparam up to ';' */
static void parse_params(Ctx *c, Node *dict, int header) {
    TInfo ti; int have = 0;
    memset(&ti, 0, sizeof ti);
    if (header && accept(")")) return;
    for (;;) {
        int line = cur()->line;
        if (header) {
            if (accept("parameter")) { dict = c->parameters; have = 0; }
            else if (accept("localparam")) { dict = c->localparams; have = 0; }
        }
        if (accept("type")) {
            char *n = expect_id();
            Node *v = None();
            if (accept("=")) { TInfo t2; parse_type(c, &t2, 1); v = t2.type ? Str(t2.type) : None(); }
            add_param(c, dict, n, NULL, v, line, 1);
        } else {
            TInfo t2;
            if (parse_type(c, &t2, 1)) { ti = t2; have = 1; }
            char *n = expect_id();
            while (is("[")) parse_dim();
            Node *v = None();
            if (accept("=")) v = parse_expr();
            add_param(c, dict, n, have ? &ti : NULL, v, line, 0);
        }
        if (!accept(",")) break;
    }
    expect(header ? ")" : ";");
}

/* ANSI port list after '(' ; consumes ')' */
static void parse_port_list(Ctx *c, Node *nets, Node *portnames, int is_func) {
    if (accept(")")) return;
    Tok *t = cur();
    if (!is_func && ((t->k == T_ID && !is_reserved(t->s) && (tis(pk(1), ",") || tis(pk(1), ")") || tis(pk(1), "["))
                      && !find_type(c, t->s)) || is("."))) {
        /* non-ANSI header: list of port names */
        do {
            if (accept(".")) { char *n = expect_id(); if (is("(")) skip_balanced(); if (portnames) add(portnames, Str(n)); }
            else if (is("{")) { skip_balanced(); }
            else {
                char *n = expect_id();
                while (is("[")) skip_balanced();
                if (portnames) add(portnames, Str(n));
            }
        } while (accept(","));
        expect(")");
        return;
    }
    const char *dir = is_func ? "input" : "inout";
    TInfo prev;
    memset(&prev, 0, sizeof prev);
    prev.type = is_func ? "logic" : "wire"; prev.packed = List();
    do {
        int line = cur()->line;
        char *attr = cur()->attr;
        t = cur();
        if (t->k == T_ID && is_in(t->s, DIRS)) {
            dir = t->s; adv();
            TInfo ti; parse_type(c, &ti, 1);
            if (!ti.expl) { ti.type = is_func ? "logic" : "wire"; ti.is_net = 1; }
            prev = ti;
        } else if (t->k == T_ID && !strcmp(t->s, "interface")) {
            adv();
            char *mp = NULL;
            if (accept(".")) mp = expect_id();
            char *n = expect_id();
            while (is("[")) parse_dim();
            Node *nd = Dict();
            dset(nd, "dir", Str("interface")); dset(nd, "type", Str("interface"));
            dset(nd, "modport", mp ? Str(mp) : None()); dset(nd, "line", Int(line));
            dset(nets, n, nd);
            if (portnames) add(portnames, Str(n));
            continue;
        } else if (!is_func && t->k == T_ID && !is_reserved(t->s) &&
                   ((tis(pk(1), ".") && pk(2)->k == T_ID && pk(3)->k == T_ID) ||
                    (pk(1)->k == T_ID && !is_reserved(pk(1)->s) && !find_type(c, t->s)))) {
            /* interface port:  my_if.mp bus   or   my_if bus */
            char *ifn = t->s, *mp = NULL; adv();
            if (accept(".")) mp = expect_id();
            char *n = expect_id();
            while (is("[")) parse_dim();
            Node *nd = Dict();
            dset(nd, "dir", Str("interface")); dset(nd, "type", Str(ifn));
            dset(nd, "modport", mp ? Str(mp) : None()); dset(nd, "line", Int(line));
            dset(nets, n, nd);
            if (portnames) add(portnames, Str(n));
            continue;
        } else {
            TInfo ti;
            if (parse_type(c, &ti, 1)) {
                if (!ti.expl) { ti.type = prev.type; ti.expl = prev.expl; ti.is_net = prev.is_net; }
                prev = ti;
            }
        }
        char *n = expect_id();
        Node *unp = List();
        while (is("[")) add(unp, parse_dim());
        Node *nd = make_net(c, dir, &prev, unp, line, attr);
        if (accept("=")) dset(nd, "default", parse_expr());
        add_net(nets, n, nd, 1);
        if (portnames) add(portnames, Str(n));
    } while (accept(","));
    expect(")");
}

/* ================================================================ statements */

static Node *parse_stmt(Ctx *c);

static Node *as_list(Node *s) {
    if (s->k == N_LIST) return s;
    Node *l = List();
    if (s->k != N_NONE) add(l, s);
    return l;
}
static void append_stmt(Node *l, Node *s) {
    if (s->k == N_NONE) return;
    if (s->k == N_LIST) { for (int i = 0; i < s->n; i++) add(l, s->items[i]); return; }
    add(l, s);
}

static const char *ASSIGN_OPS[] = { "=", "<=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=",
    "<<=", ">>=", "<<<=", ">>>=", NULL };

static Node *parse_simple_assign(void) {
    if (is("++") || is("--")) { char *op = cur()->s; adv(); return tup(Str(op), parse_lvalue(), NULL); }
    Node *lv = parse_lvalue();
    if (is("++") || is("--")) { char *op = cur()->s; adv(); return tup(Str(op), lv, NULL); }
    Tok *o = cur();
    if (o->k == T_OP && is_in(o->s, ASSIGN_OPS)) { adv(); return tup(Str(o->s), lv, parse_expr(), NULL); }
    perr("expected assignment");
    return NULL;
}

static int stmt_is_decl(Ctx *c) {
    Tok *t = cur();
    (void)c;
    if (t->k != T_ID) return 0;
    if (tis(pk(1), "'")) return 0;       /* cast, e.g. void'(f()) */
    if (is_in(t->s, DATA_TYPES) || is_in(t->s, NET_TYPES) || !strcmp(t->s, "automatic") ||
        !strcmp(t->s, "static") || !strcmp(t->s, "var") || !strcmp(t->s, "struct") ||
        !strcmp(t->s, "union") || !strcmp(t->s, "enum") || !strcmp(t->s, "const")) return 1;
    if (is_reserved(t->s)) return 0;
    if (tis(pk(1), "::") && pk(2)->k == T_ID && pk(3)->k == T_ID) return 1;
    if (pk(1)->k == T_ID && !is_reserved(pk(1)->s)) return 1;
    return 0;
}

static Node *parse_block(Ctx *c) {
    expect("begin");
    char *label = NULL;
    if (accept(":")) label = expect_id();
    Node *l = List();
    while (!is("end")) {
        if (cur()->k == T_EOF) perr("missing 'end'");
        append_stmt(l, parse_stmt(c));
    }
    adv();
    if (accept(":")) expect_id();
    return label ? tup(Str("begin"), Str(label), l, NULL) : l;
}

static Node *parse_case(Ctx *c, const char *qual) {
    char *kind = cur()->s; adv();
    expect("(");
    Node *e = parse_expr();
    expect(")");
    accept("inside");
    Node *items = List();
    while (!accept("endcase")) {
        if (cur()->k == T_EOF) perr("missing 'endcase'");
        if (accept("default")) {
            accept(":");
            add(items, tup(Str("default"), as_list(parse_stmt(c)), NULL));
            continue;
        }
        Node *labels = List();
        do {
            if (accept("[")) { Node *a = parse_expr(); expect(":"); Node *b = parse_expr(); expect("]"); add(labels, tup(Str("range"), a, b, NULL)); }
            else add(labels, parse_expr());
        } while (accept(","));
        expect(":");
        add(items, tup(labels, as_list(parse_stmt(c)), NULL));
    }
    return tup(Str("case"), Str(qual ? sfmt("%s %s", qual, kind) : kind), e, items, NULL);
}

static Node *parse_stmt(Ctx *c) {
    Tok *t = cur();
    if (t->k == T_EOF) perr("unexpected end of file");
    if (accept(";")) return None();
    if (t->k == T_ID) {
        const char *s = t->s;
        if (!is_reserved(s) && tis(pk(1), ":") && s[0] != '$') {
            adv(); adv();
            return tup(Str("label"), Str(s), as_list(parse_stmt(c)), NULL);
        }
        if (!strcmp(s, "begin")) return parse_block(c);
        if (!strcmp(s, "fork")) {
            adv();
            if (accept(":")) expect_id();
            Node *l = List();
            while (!is("join") && !is("join_any") && !is("join_none")) {
                if (cur()->k == T_EOF) perr("missing 'join'");
                append_stmt(l, parse_stmt(c));
            }
            char *k = cur()->s; adv();
            if (accept(":")) expect_id();
            return tup(Str("fork"), Str(k), l, NULL);
        }
        const char *qual = NULL;
        if (!strcmp(s, "unique") || !strcmp(s, "unique0") || !strcmp(s, "priority")) { qual = s; adv(); t = cur(); s = t->s; }
        if (!strcmp(s, "if")) {
            adv(); expect("(");
            Node *cond = parse_expr();
            expect(")");
            Node *th = as_list(parse_stmt(c)), *el = List();
            if (accept("else")) el = as_list(parse_stmt(c));
            return tup(Str("if"), cond, th, el, NULL);
        }
        if (!strcmp(s, "case") || !strcmp(s, "casez") || !strcmp(s, "casex")) return parse_case(c, qual);
        if (qual) perr("expected 'if' or 'case' after '%s'", qual);
        if (!strcmp(s, "for")) {
            adv(); expect("(");
            Node *init = None(), *cond = None(), *step = None();
            if (!is(";")) {
                while (cur()->k == T_ID && (is_in(cur()->s, DATA_TYPES) || is("automatic") || is("var"))) adv();
                init = parse_simple_assign();
                while (accept(",")) parse_simple_assign();
            }
            expect(";");
            if (!is(";")) cond = parse_expr();
            expect(";");
            if (!is(")")) { step = parse_simple_assign(); while (accept(",")) parse_simple_assign(); }
            expect(")");
            return tup(Str("for"), init, cond, step, as_list(parse_stmt(c)), NULL);
        }
        if (!strcmp(s, "while") || !strcmp(s, "repeat") || !strcmp(s, "foreach")) {
            adv(); expect("(");
            Node *e = parse_expr();
            expect(")");
            return tup(Str(s), e, as_list(parse_stmt(c)), NULL);
        }
        if (!strcmp(s, "forever")) { adv(); return tup(Str("forever"), as_list(parse_stmt(c)), NULL); }
        if (!strcmp(s, "do")) {
            adv();
            Node *b = as_list(parse_stmt(c));
            expect("while"); expect("(");
            Node *e = parse_expr();
            expect(")"); expect(";");
            return tup(Str("dowhile"), b, e, NULL);
        }
        if (!strcmp(s, "wait")) {
            adv();
            if (accept("fork")) { expect(";"); return tup(Str("wait"), Str("fork"), NULL); }
            expect("(");
            Node *e = parse_expr();
            expect(")");
            return tup(Str("wait"), e, as_list(parse_stmt(c)), NULL);
        }
        if (!strcmp(s, "disable")) {
            adv();
            Node *e = accept("fork") ? Str("fork") : parse_expr();
            expect(";");
            return tup(Str("disable"), e, NULL);
        }
        if (!strcmp(s, "return")) {
            adv();
            Node *e = is(";") ? None() : parse_expr();
            expect(";");
            return tup(Str("return"), e, NULL);
        }
        if (!strcmp(s, "break") || !strcmp(s, "continue")) { adv(); expect(";"); return tup(Str(s), None(), NULL); }
        if (!strcmp(s, "assign") || !strcmp(s, "force")) {
            adv();
            Node *lv = parse_lvalue();
            expect("=");
            Node *rv = parse_expr();
            expect(";");
            return tup(Str(s), lv, rv, NULL);
        }
        if (!strcmp(s, "deassign") || !strcmp(s, "release")) {
            adv();
            Node *lv = parse_lvalue();
            expect(";");
            return tup(Str(s), lv, NULL);
        }
        if (!strcmp(s, "assert") || !strcmp(s, "assume") || !strcmp(s, "cover")) {
            adv();
            if (is("property") || is("final") || is("#")) { skip_to_semi(); return tup(Str(s), Str("property"), NULL); }
            expect("(");
            Node *cond = parse_expr();
            expect(")");
            Node *pass = None(), *fail = None();
            if (!accept(";")) {
                if (!is("else")) pass = parse_stmt(c);
                if (accept("else")) fail = parse_stmt(c);
            }
            return tup(Str(s), cond, as_list(pass), as_list(fail), NULL);
        }
        if (!strcmp(s, "typedef")) { parse_typedef(c); return None(); }
        if (!strcmp(s, "parameter") || !strcmp(s, "localparam")) {
            adv();
            parse_params(c, s[0] == 'l' ? c->localparams : c->parameters, 0);
            return None();
        }
        if (s[0] == '$') {
            adv();
            Node *n = tup(Str("systask"), Str(s), NULL);
            if (accept("(")) {
                if (!is(")")) do {
                    if (is(",") || is(")")) add(n, None()); else add(n, parse_expr());
                } while (accept(","));
                expect(")");
            }
            expect(";");
            return n;
        }
        if (stmt_is_decl(c)) {
            Node *d = Dict();
            parse_decl(c, d, NULL, 0);
            Node *l = List();
            for (int i = 0; i < d->n; i++) add(l, tup(Str("declare"), Str(d->keys[i]), d->items[i], NULL));
            return l;
        }
    }
    if (accept("#")) { Node *d = parse_delay(); return tup(Str("delay"), d, as_list(parse_stmt(c)), NULL); }
    if (accept("@")) { Node *e = parse_event(); return tup(Str("wait_event"), e, as_list(parse_stmt(c)), NULL); }
    if (accept("->")) { Node *e = parse_expr(); expect(";"); return tup(Str("trigger"), e, NULL); }
    if (is("++") || is("--")) { Node *a = parse_simple_assign(); expect(";"); return a; }

    /* assignment or task call */
    Node *lv = parse_lvalue();
    if (accept(";")) {
        if (lv->k == N_STR) return tup(Str("call"), lv, NULL);
        if (lv->k == N_TUPLE && !strcmp(lv->items[0]->s, "call")) return lv;
        return tup(Str("expr"), lv, NULL);
    }
    if (is("++") || is("--")) { char *op = cur()->s; adv(); expect(";"); return tup(Str(op), lv, NULL); }
    Tok *o = cur();
    if (o->k == T_OP && is_in(o->s, ASSIGN_OPS)) {
        adv();
        if (accept("#")) parse_delay();                 /* intra-assignment timing dropped */
        else if (accept("@")) parse_event();
        else if (accept("repeat")) { expect("("); parse_expr(); expect(")"); expect("@"); parse_event(); }
        Node *rv = parse_expr();
        expect(";");
        return tup(Str(o->s), lv, rv, NULL);
    }
    perr("expected assignment or ';'");
    return NULL;
}

/* ================================================================ module items */

static void parse_item(Ctx *c);
static void parse_items(Ctx *c, const char *term);

static void parse_assign(Ctx *c) {
    int line = cur()->line;
    char *attr = cur()->attr;
    expect("assign");
    Node *strength = NULL, *delay = NULL;
    if (is("(") && pk(1)->k == T_ID && is_in(pk(1)->s, STRENGTHS)) {
        Buf b = {0}; adv();
        while (!is(")") && cur()->k != T_EOF) { bputs(&b, cur()->s); adv(); }
        expect(")");
        strength = Str(bstr(&b));
    }
    if (accept("#")) delay = parse_delay();
    do {
        Node *lv = parse_lvalue();
        expect("=");
        Node *rv = parse_expr();
        Node *a = Dict();
        dset(a, "line", Int(line));
        if (delay) dset(a, "delay", delay);
        if (strength) dset(a, "strength", strength);
        if (attr) dset(a, "attrs", Str(attr));
        add(c->assigns, tup(lv, rv, a, NULL));
    } while (accept(","));
    expect(";");
}

static void parse_always(Ctx *c) {
    Tok *t = cur();
    char *kind = t->s, *attr = t->attr;
    int line = t->line;
    adv();
    Node *when = None();
    if (!strcmp(kind, "always_comb") || !strcmp(kind, "always_latch")) when = Str("*");
    if (accept("@")) when = parse_event();
    else if (!strcmp(kind, "always") && accept("#")) when = tup(Str("delay"), parse_delay(), NULL);
    Node *code = as_list(parse_stmt(c));
    Node *a = Dict();
    dset(a, "kind", Str(kind));
    dset(a, "when", when);
    dset(a, "code", code);
    dset(a, "line", Int(line));
    if (attr) dset(a, "attrs", Str(attr));
    add(c->always, a);
}

static void parse_initial(Ctx *c) {
    Tok *t = cur();
    char *kind = t->s, *attr = t->attr;
    int line = t->line;
    adv();
    Node *a = Dict();
    dset(a, "kind", Str(kind));
    dset(a, "code", as_list(parse_stmt(c)));
    dset(a, "line", Int(line));
    if (attr) dset(a, "attrs", Str(attr));
    add(c->initials, a);
}

static void parse_function(Ctx *c) {
    int line = cur()->line;
    int istask = is("task");
    adv();
    while (accept("automatic") || accept("static")) ;
    TInfo ti;
    memset(&ti, 0, sizeof ti); ti.packed = List();
    if (!istask) parse_type(c, &ti, 1);
    if (!istask && !ti.type) ti.type = "logic";
    char *name = expect_id();
    while (accept("::") || accept(".")) name = sfmt("%s.%s", name, expect_id());
    Ctx *fc = new_ctx(c, NULL);
    if (accept("(")) parse_port_list(fc, fc->nets, NULL, 1);
    expect(";");
    Node *code = List();
    const char *endkw = istask ? "endtask" : "endfunction";
    while (!is(endkw)) {
        if (cur()->k == T_EOF) perr("missing '%s'", endkw);
        Tok *t = cur();
        if (t->k == T_ID && is_in(t->s, DIRS)) { parse_decl(fc, fc->nets, t->s, 0); continue; }
        if (stmt_is_decl(fc)) { parse_decl(fc, fc->nets, NULL, 0); continue; }
        append_stmt(code, parse_stmt(fc));
    }
    adv();
    if (accept(":")) expect_id();
    Node *f = Dict();
    dset(f, "kind", Str(istask ? "task" : "function"));
    if (!istask) {
        dset(f, "type", Str(ti.type));
        dset(f, "signed", Bool(ti.sgn));
        dset(f, "packed", ti.packed);
        long long w = type_width(c, &ti);
        dset(f, "width", w >= 0 ? Int(w) : None());
    }
    dset(f, "nets", fc->nets);
    if (fc->parameters->n) dset(f, "parameters", fc->parameters);
    if (fc->localparams->n) dset(f, "localparams", fc->localparams);
    dset(f, "code", code);
    dset(f, "line", Int(line));
    dset(c->functions, name, f);
}

static Node *parse_conn_list(void) {     /* inside ( ... ) ; does not consume ')' */
    if (is(")")) return Dict();
    if (is(".") || is(".*")) {
        Node *d = Dict();
        do {
            if (accept(".*")) { dset(d, "*", Str("*")); continue; }
            expect(".");
            char *p = expect_id();
            if (accept("(")) {
                Node *v = None();
                if (!is(")")) v = parse_expr();
                expect(")");
                dset(d, p, v);
            } else dset(d, p, Str(p));
        } while (accept(","));
        return d;
    }
    Node *l = List();
    do {
        if (is(",") || is(")")) add(l, None()); else add(l, parse_expr());
    } while (accept(","));
    return l;
}

static int is_instance_start(void) {
    Tok *n = pk(1);
    if (tis(n, "#") || tis(n, "(")) return 1;
    if (n->k == T_ID && !is_reserved(n->s)) {
        int j = 2;
        while (tis(pk(j), "[")) {
            int d = 0;
            do {
                if (tis(pk(j), "[")) d++;
                else if (tis(pk(j), "]")) d--;
                j++;
                if (pk(j)->k == T_EOF) return 0;
            } while (d > 0);
        }
        return tis(pk(j), "(");
    }
    return 0;
}

static void parse_instance(Ctx *c) {
    Tok *t = cur();
    int line = t->line;
    char *mod = t->s, *attr = t->attr;
    adv();
    Node *params = Dict();
    if (accept("#")) {
        if (accept("(")) { params = parse_conn_list(); expect(")"); }
        else parse_delay();
    }
    if (is("(") && pk(1)->k == T_ID && is_in(pk(1)->s, STRENGTHS)) skip_balanced();
    if (accept("#")) parse_delay();
    do {
        char *iname;
        if (cur()->k == T_ID) iname = expect_id();
        else iname = sfmt("%s_%d_%d", mod, line, ++anon_count);
        Node *arr = List();
        while (is("[")) add(arr, parse_dim());
        expect("(");
        Node *conns = parse_conn_list();
        expect(")");
        Node *i = Dict();
        dset(i, "module", Str(mod));
        dset(i, "params", params);
        dset(i, "conns", conns);
        if (arr->n) dset(i, "array", arr);
        dset(i, "line", Int(line));
        if (attr) dset(i, "attrs", Str(attr));
        dset(c->instances, iname, i);
    } while (accept(","));
    expect(";");
}

static Node *parse_gen_body(Ctx *c, char **label) {
    Ctx *sub = new_ctx(c, NULL);
    *label = NULL;
    if (accept("begin")) {
        if (accept(":")) *label = expect_id();
        parse_items(sub, "end");
        expect("end");
        if (accept(":")) expect_id();
    } else parse_item(sub);
    prune(sub->mod);
    return sub->mod;
}

static void parse_generate_construct(Ctx *c) {
    Tok *t = cur();
    int line = t->line;
    char *label = NULL;
    Node *g = Dict();
    if (accept("for")) {
        expect("(");
        accept("genvar");
        Node *init = parse_simple_assign();
        expect(";");
        Node *cond = parse_expr();
        expect(";");
        Node *step = parse_simple_assign();
        expect(")");
        Node *body = parse_gen_body(c, &label);
        dset(g, "kind", Str("for"));
        dset(g, "label", label ? Str(label) : None());
        dset(g, "init", init); dset(g, "cond", cond); dset(g, "step", step);
        dset(g, "body", body);
    } else if (accept("if")) {
        expect("(");
        Node *cond = parse_expr();
        expect(")");
        Node *th = parse_gen_body(c, &label);
        char *l2 = NULL;
        Node *el = None();
        if (accept("else")) el = parse_gen_body(c, &l2);
        dset(g, "kind", Str("if"));
        dset(g, "cond", cond);
        dset(g, "label", label ? Str(label) : None());
        dset(g, "then", th);
        dset(g, "else", el);
        dset(g, "else_label", l2 ? Str(l2) : None());
    } else if (is("case") || is("casez") || is("casex")) {
        char *k = cur()->s; adv();
        expect("(");
        Node *e = parse_expr();
        expect(")");
        Node *items = List();
        while (!accept("endcase")) {
            if (cur()->k == T_EOF) perr("missing 'endcase'");
            Node *labels;
            if (accept("default")) { accept(":"); labels = Str("default"); }
            else {
                labels = List();
                do add(labels, parse_expr()); while (accept(","));
                expect(":");
            }
            char *lb;
            Node *body = parse_gen_body(c, &lb);
            add(items, tup(labels, body, NULL));
        }
        dset(g, "kind", Str(k));
        dset(g, "expr", e);
        dset(g, "items", items);
    } else {    /* begin ... end */
        Node *body = parse_gen_body(c, &label);
        dset(g, "kind", Str("block"));
        dset(g, "label", label ? Str(label) : None());
        dset(g, "body", body);
    }
    dset(g, "line", Int(line));
    add(c->generates, g);
}

static void parse_import(Ctx *c) {
    expect("import");
    do {
        char *p = expect_id();
        expect("::");
        char *n = accept("*") ? "*" : expect_id();
        add(c->imports, Str(sfmt("%s::%s", p, n)));
    } while (accept(","));
    expect(";");
}

static void parse_item(Ctx *c) {
    Tok *t = cur();
    if (t->k == T_OP) {
        if (accept(";")) return;
        perr("unexpected '%s'", t->s);
    }
    if (t->k != T_ID) perr("unexpected token");
    const char *s = t->s;
    if (is_in(s, DIRS)) { parse_decl(c, c->nets, s, 1); return; }
    if (!strcmp(s, "parameter") || !strcmp(s, "localparam")) {
        adv();
        parse_params(c, s[0] == 'l' ? c->localparams : c->parameters, 0);
        return;
    }
    if (!strcmp(s, "typedef")) { parse_typedef(c); return; }
    if (!strcmp(s, "assign")) { parse_assign(c); return; }
    if (is_in(s, ALWAYS_KW)) { parse_always(c); return; }
    if (!strcmp(s, "initial") || !strcmp(s, "final")) { parse_initial(c); return; }
    if (!strcmp(s, "function") || !strcmp(s, "task")) { parse_function(c); return; }
    if (!strcmp(s, "generate") || !strcmp(s, "endgenerate")) { adv(); return; }
    if (!strcmp(s, "for") || !strcmp(s, "if") || !strcmp(s, "case") || !strcmp(s, "casez") ||
        !strcmp(s, "casex") || !strcmp(s, "begin")) { parse_generate_construct(c); return; }
    if (!strcmp(s, "import")) { parse_import(c); return; }
    if (!strcmp(s, "export") || !strcmp(s, "modport") || !strcmp(s, "defparam") ||
        !strcmp(s, "default") || !strcmp(s, "timeunit") || !strcmp(s, "timeprecision") ||
        !strcmp(s, "alias") || !strcmp(s, "bind") || !strcmp(s, "nettype") ||
        !strcmp(s, "assert") || !strcmp(s, "assume") || !strcmp(s, "cover") ||
        !strcmp(s, "restrict") || !strcmp(s, "specparam")) { skip_to_semi(); return; }
    static const char *blocks[][2] = {
        { "specify", "endspecify" }, { "covergroup", "endgroup" }, { "property", "endproperty" },
        { "sequence", "endsequence" }, { "clocking", "endclocking" }, { "class", "endclass" },
        { "checker", "endchecker" }, { "config", "endconfig" }, { "primitive", "endprimitive" },
        { "table", "endtable" }, { NULL, NULL } };
    for (int i = 0; blocks[i][0]; i++) if (!strcmp(s, blocks[i][0])) { skip_until(blocks[i][1]); return; }
    if (!strcmp(s, "module") || !strcmp(s, "interface") || !strcmp(s, "program")) {
        warn(t->line, "nested %s skipped", s);
        char *endkw = sfmt("end%s", s);
        skip_until(endkw);
        return;
    }
    if (is_in(s, GATES)) { parse_instance(c); return; }
    if (is_in(s, NET_TYPES) || is_in(s, DATA_TYPES) || !strcmp(s, "var") || !strcmp(s, "struct") ||
        !strcmp(s, "union") || !strcmp(s, "enum") || !strcmp(s, "signed") || !strcmp(s, "const")) {
        parse_decl(c, c->nets, NULL, 1);
        return;
    }
    if (!is_reserved(s)) {
        if (tis(pk(1), ":")) { adv(); adv(); return; }     /* label of a skipped construct */
        if (is_instance_start()) parse_instance(c);
        else parse_decl(c, c->nets, NULL, 1);               /* user-typed declaration */
        return;
    }
    perr("unexpected keyword '%s'", s);
}

static int is_proc_start(const char *s) {
    return is_in(s, ALWAYS_KW) || !strcmp(s, "initial") || !strcmp(s, "final") ||
           !strcmp(s, "function") || !strcmp(s, "task") || !strcmp(s, "for") || !strcmp(s, "if") ||
           !strcmp(s, "begin") || !strcmp(s, "case") || !strcmp(s, "casez") || !strcmp(s, "casex");
}

/* error recovery: skip from the start of the failed item to the next plausible item */
static void recover(int start, const char *term) {
    const char *s = toks[start]->s;
    int proc = is_proc_start(s);
    int depth = (!strcmp(s, "function") || !strcmp(s, "task") || !strcmp(s, "begin")) ? 1 : 0;
    P = start + 1;
    ensure_tok(P);
    if (P >= ntoks) P = ntoks - 1;
    while (cur()->k != T_EOF) {
        Tok *t = cur();
        if (t->k == T_ID && is_in(t->s, UNIT_END)) return;
        if (is("begin") || is("fork") || is("case") || is("casez") || is("casex") || is("function") || is("task")) depth++;
        else if (is("end") || is("join") || is("join_any") || is("join_none") || is("endcase") ||
                 is("endfunction") || is("endtask")) {
            if (depth == 0 && is("end") && !strcmp(term, "end")) return;
            depth--;
            adv();
            if (depth <= 0) { depth = 0; if (accept(":")) adv(); }
            continue;
        }
        if (depth == 0) {
            if (is(term)) return;
            if (t->k == T_ID && is_in(t->s, ITEM_KW)) return;
            if (!proc && is(";")) { adv(); return; }
        }
        adv();
    }
}

static void parse_items(Ctx *c, const char *term) {
    while (!is(term) && cur()->k != T_EOF) {
        if (cur()->k == T_ID && is_in(cur()->s, UNIT_END)) return;
        int start = P;
        jmp_buf jb, *save = errjb;
        errjb = &jb;
        if (setjmp(jb) == 0) parse_item(c);
        else recover(start, term);
        errjb = save;
        if (P == start) adv();
    }
}

static void parse_module(void) {
    Tok *t = cur();
    char *volatile kind = t->s;
    int line = t->line;
    adv();
    if (!strcmp(kind, "macromodule")) kind = "module";
    while (accept("automatic") || accept("static")) ;
    char *name = expect_id();
    int is_pkg = !strcmp(kind, "package");
    curpool = is_pkg ? &persistent_pool : &module_pool;
    Ctx *c = new_ctx(unit_ctx, kind);
    dset(c->mod, "line", Int(line));
    for (int i = 0; i < nseen; i++) if (!strcmp(seen_names[i], name)) warn(line, "%s '%s' redefined", kind, name);
    seen_names = xrealloc(seen_names, (nseen + 1) * sizeof(char *));
    seen_names[nseen++] = xstrdup(name);
    if (is_pkg) {
        pkg_names = xrealloc(pkg_names, (npkgs + 1) * sizeof(char *));
        pkg_ctxs = xrealloc(pkg_ctxs, (npkgs + 1) * sizeof(Ctx *));
        pkg_names[npkgs] = xstrdup(name); pkg_ctxs[npkgs] = c; npkgs++;
    }
    char *endkw = sfmt("end%s", kind);
    jmp_buf jb, *save = errjb;
    errjb = &jb;
    if (setjmp(jb) == 0) {
        while (is("import")) parse_import(c);
        if (accept("#")) { expect("("); parse_params(c, c->parameters, 1); }
        if (accept("(")) parse_port_list(c, c->nets, c->ports, 0);
        expect(";");
    } else {
        while (cur()->k != T_EOF && !is(";") && !is(endkw)) adv();
        accept(";");
    }
    errjb = save;
    parse_items(c, endkw);
    if (!accept(endkw)) { fprintf(stderr, "%s:%d: error: missing '%s' for %s '%s'\n", cur_file, cur()->line, endkw, kind, name); nerrors++; }
    else if (P + 1 < ntoks && is(":")) { adv(); adv(); }  /* "endmodule : name" -- only look at
                                                         tokens already read, so we never wait for
                                                         more input before printing */
    emit_entry(name, c->mod);            /* print it now ... */
    if (!is_pkg) pool_free(&module_pool); /* ... and forget it */
    curpool = &persistent_pool;
}

static void parse_file(void) {
    while (cur()->k != T_EOF) {
        drop_consumed();
        int start = P;
        jmp_buf jb, *save = errjb;
        errjb = &jb;
        if (setjmp(jb) == 0) {
            if (is("module") || is("macromodule") || is("interface") || is("package") || is("program")) parse_module();
            else parse_item(unit_ctx);
        } else recover(start, ";");
        errjb = save;
        if (curpool != &persistent_pool) { pool_free(&module_pool); curpool = &persistent_pool; }
        if (P == start) adv();
    }
}

/* ================================================================ output */

static int json_mode = 0;

static void pstr(Buf *b, const char *s) {
    char q = json_mode ? '"' : '\'';
    bputc(b, q);
    for (; *s; s++) {
        unsigned char ch = (unsigned char)*s;
        if (ch == (unsigned char)q || ch == '\\') { bputc(b, '\\'); bputc(b, ch); }
        else if (ch == '\n') bputs(b, "\\n");
        else if (ch == '\t') bputs(b, "\\t");
        else if (ch < 32 || ch == 127) { char t[8]; snprintf(t, sizeof t, json_mode ? "\\u%04x" : "\\x%02x", ch); bputs(b, t); }
        else bputc(b, ch);
    }
    bputc(b, q);
}

static int emit_inline(Buf *b, Node *n, size_t limit) {
    char tmp[32];
    switch (n->k) {
    case N_NONE: bputs(b, json_mode ? "null" : "None"); break;
    case N_BOOL: bputs(b, n->i ? (json_mode ? "true" : "True") : (json_mode ? "false" : "False")); break;
    case N_INT: snprintf(tmp, sizeof tmp, "%lld", n->i); bputs(b, tmp); break;
    case N_STR: pstr(b, n->s); break;
    case N_LIST: case N_TUPLE: {
        int tuple = n->k == N_TUPLE && !json_mode;
        bputc(b, tuple ? '(' : '[');
        for (int i = 0; i < n->n; i++) {
            if (i) bputs(b, ", ");
            if (!emit_inline(b, n->items[i], limit)) return 0;
        }
        if (tuple && n->n == 1) bputc(b, ',');
        bputc(b, tuple ? ')' : ']');
        break;
    }
    case N_DICT:
        bputc(b, '{');
        for (int i = 0; i < n->n; i++) {
            if (i) bputs(b, ", ");
            pstr(b, n->keys[i]); bputs(b, ": ");
            if (!emit_inline(b, n->items[i], limit)) return 0;
        }
        bputc(b, '}');
        break;
    }
    return b->n <= limit;
}

static void indent(Buf *b, int n) { while (n-- > 0) bputc(b, ' '); }

static void emit(Buf *b, Node *n, int ind) {
    if (n->k == N_NONE || n->k == N_BOOL || n->k == N_INT || n->k == N_STR || n->n == 0) {
        emit_inline(b, n, (size_t)-1);
        return;
    }
    Buf t = {0};
    size_t budget = ind < 70 ? (size_t)(130 - ind) : 60;
    if (emit_inline(&t, n, budget)) { bput(b, t.s, t.n); free(t.s); return; }
    free(t.s);
    int tuple = n->k == N_TUPLE && !json_mode;
    char open = n->k == N_DICT ? '{' : tuple ? '(' : '[';
    char close = n->k == N_DICT ? '}' : tuple ? ')' : ']';
    bputc(b, open); bputc(b, '\n');
    for (int i = 0; i < n->n; i++) {
        indent(b, ind + 4);
        if (n->k == N_DICT) { pstr(b, n->keys[i]); bputs(b, ": "); }
        emit(b, n->items[i], ind + 4);
        if (!json_mode || i < n->n - 1) bputc(b, ',');
        bputc(b, '\n');
    }
    indent(b, ind); bputc(b, close);
}

static FILE *fo;
static int nemitted;
static int split_mode;
static const char *SPLIT_DIR = "tmppy";

/* --split: write one module into SPLIT_DIR/<name>.py (or .json) */
static void emit_split(const char *name, Node *mod) {
    Buf fn = {0};
    bputs(&fn, SPLIT_DIR); bputc(&fn, '/');
    for (const char *p = name; *p; p++)          /* keep the file name shell-safe */
        bputc(&fn, (isalnum((unsigned char)*p) || *p == '_' || *p == '-' || *p == '.') ? *p : '_');
    bputs(&fn, json_mode ? ".json" : ".py");
    Buf b = {0};
    if (json_mode) bputs(&b, "{\n");
    else {
        bputs(&b, "# Generated by vparse from: "); bputs(&b, cur_file);
        bputs(&b, "\nmodules = {\n");
    }
    indent(&b, 4); pstr(&b, name); bputs(&b, ": ");
    emit(&b, mod, 4);
    bputs(&b, json_mode ? "\n}\n" : ",\n}\n");
    FILE *f = fopen(fn.s, "w");
    if (!f) { fprintf(stderr, "error: cannot write '%s': %s\n", fn.s, strerror(errno)); nerrors++; }
    else {
        fwrite(b.s, 1, b.n, f);
        fclose(f);
        printf("%s\n", fn.s);                  /* report each file as it is written */
        fflush(stdout);
    }
    free(b.s); free(fn.s);
    nemitted++;
}

static void emit_entry(const char *name, Node *mod) {
    if (split_mode) { emit_split(name, mod); return; }
    Buf b = {0};
    if (nemitted && json_mode) bputs(&b, ",\n");
    indent(&b, 4);
    pstr(&b, name);
    bputs(&b, ": ");
    emit(&b, mod, 4);
    if (!json_mode) bputs(&b, ",\n");
    fwrite(b.s, 1, b.n, fo);
    fflush(fo);
    free(b.s);
    nemitted++;
}

/* ================================================================ main */

static void usage(void) {
    fprintf(stderr,
        "usage: vparse [-o out.py] [-json] [--split] [-DNAME[=VAL]] [-Idir] file.v|- [file.sv ...]\n"
        "  Parses Verilog/SystemVerilog and prints a Python dict 'modules'\n"
        "  (or JSON with -json) describing every module.\n"
        "  --split  write each module to its own file tmppy/<module>.py (.json with -json)\n"
        "           instead of one combined output; prints each file name as it is written.\n");
    exit(2);
}

int main(int argc, char **argv) {
    const char *outf = NULL;
    char **files = xmalloc(argc * sizeof(char *));
    int nfiles = 0;
    for (int i = 1; i < argc; i++) {
        char *a = argv[i];
        if (!strcmp(a, "-o")) { if (++i >= argc) usage(); outf = argv[i]; }
        else if (!strcmp(a, "-json")) json_mode = 1;
        else if (!strcmp(a, "--split") || !strcmp(a, "-split")) split_mode = 1;
        else if (!strncmp(a, "-D", 2) || !strncmp(a, "+define+", 8)) {
            char *d = xstrdup(a[1] == 'D' ? a + 2 : a + 8);
            char *eq = strchr(d, '=');
            if (eq) *eq = 0;
            define_macro(d, -1, NULL, NULL, eq ? eq + 1 : "");
        }
        else if (!strncmp(a, "-I", 2)) {
            const char *d = a[2] ? a + 2 : (++i < argc ? argv[i] : NULL);
            if (!d) usage();
            incdirs = xrealloc(incdirs, (nincdirs + 1) * sizeof(char *));
            incdirs[nincdirs++] = xstrdup(d);
        }
        else if (!strncmp(a, "+incdir+", 8)) {
            incdirs = xrealloc(incdirs, (nincdirs + 1) * sizeof(char *));
            incdirs[nincdirs++] = xstrdup(a + 8);
        }
        else if (!strcmp(a, "-h") || !strcmp(a, "--help")) usage();
        else if (a[0] == '-' && a[1]) { fprintf(stderr, "unknown option %s\n", a); usage(); }
        else files[nfiles++] = a;
    }
    if (!nfiles) usage();

    if (split_mode) {
        if (outf) fprintf(stderr, "warning: -o ignored with --split\n");
        outf = NULL;
        if (mkdir(SPLIT_DIR, 0777) != 0 && errno != EEXIST) {
            fprintf(stderr, "error: cannot create directory '%s': %s\n", SPLIT_DIR, strerror(errno));
            return 2;
        }
        fo = NULL;
    } else {
    fo = outf ? fopen(outf, "w") : stdout;
    if (!fo) { fprintf(stderr, "error: cannot write '%s'\n", outf); return 2; }
    if (json_mode) fputs("{\n", fo);
    else {
        fputs("# Generated by vparse from:", fo);
        for (int f = 0; f < nfiles; f++) fprintf(fo, " %s", files[f]);
        fputs("\nmodules = {\n", fo);
    }
    fflush(fo);
    }

    unit_ctx = new_ctx(NULL, "unit");

    for (int f = 0; f < nfiles; f++) {
        int is_stdin = !strcmp(files[f], "-");
        cur_file = is_stdin ? "<stdin>" : files[f];
        in_f = is_stdin ? stdin : fopen(files[f], "r");
        if (!in_f) { fprintf(stderr, "error: cannot read '%s'\n", files[f]); nerrors++; continue; }
        in_line = in_comment = in_eof = eof_pushed = 0;
        if_depth = 0;
        P = 0;
        parse_file();
        if (if_depth) warn(in_line, "unterminated `ifdef");
        P = ntoks; drop_consumed();
        if (!is_stdin) fclose(in_f);
    }

    int unit_used = 0;
    for (int i = 0; i < unit_ctx->mod->n; i++) {
        Node *v = unit_ctx->mod->items[i];
        if ((v->k == N_LIST || v->k == N_DICT) && v->n) unit_used = 1;
    }
    if (unit_used) emit_entry("$unit", unit_ctx->mod);
    if (!split_mode) {
        fputs(json_mode ? (nemitted ? "\n}\n" : "}\n") : "}\n", fo);
        if (outf) fclose(fo);
    }
    if (nerrors) fprintf(stderr, "%d error(s), %d warning(s)\n", nerrors, nwarnings);
    return nerrors ? 1 : 0;
}
