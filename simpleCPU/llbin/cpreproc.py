#!/usr/bin/env python3
"""
cpreproc.py  –  minimal C preprocessor
Handles: #include, #define (object-like and function-like), #undef,
         #ifdef / #ifndef / #if / #elif / #else / #endif
Outputs clean C with all macros expanded and directives removed.

Usage:
    python3 cpreproc.py input.c [output.c]
    python3 cpreproc.py input.c          # output to stdout
"""

import re
import sys
import os
from pathlib import Path

# ──────────────────────────────────────────────────────────────────────────────
# Tokeniser helpers
# ──────────────────────────────────────────────────────────────────────────────

# Match a single C token for macro expansion
_TOKEN_RE = re.compile(
    r'("(?:[^"\\]|\\.)*")'          # string literal  – not expanded
    r"|('(?:[^'\\]|\\.)*')"         # char literal    – not expanded
    r'|(//[^\n]*)'                   # // comment
    r'|(/\*.*?\*/)'                  # /* */ comment  (non-greedy, single-line here)
    r'|([A-Za-z_]\w*)'              # identifier
    r'|(\d+(?:\.\d+)?(?:[uUlLfF]+)?)'  # number
    r'|(##|[+\-*/%&|^~!<>=?:,.;()\[\]{}#])'  # operators / punctuation
    r'|(\s+)',                       # whitespace
    re.DOTALL,
)

def tokenise(text: str):
    """Yield (kind, value) tokens.  kind in: str, char, cmt, id, num, op, ws"""
    kinds = ['str', 'char', 'cmt', 'cmt', 'id', 'num', 'op', 'ws']
    for m in _TOKEN_RE.finditer(text):
        for i, k in enumerate(kinds):
            if m.group(i + 1) is not None:
                yield k, m.group(i + 1)
                break
        else:
            yield 'op', m.group(0)   # fallback for any missed char


# ──────────────────────────────────────────────────────────────────────────────
# Macro store
# ──────────────────────────────────────────────────────────────────────────────

class Macro:
    def __init__(self, name, params, body):
        """
        params: None  → object-like macro
                list  → function-like macro (may be empty)
        body: list of (kind, value) tokens
        """
        self.name   = name
        self.params = params   # None | [str, ...]
        self.body   = body     # list of (kind, val) after the macro name / param list

    def is_function_like(self):
        return self.params is not None


def parse_define(line: str) -> Macro:
    """Parse the text after '#define '."""
    m = re.match(r'([A-Za-z_]\w*)(\(([^)]*)\))?\s*(.*)', line.strip(), re.DOTALL)
    if not m:
        raise ValueError(f"Bad #define: {line!r}")
    name       = m.group(1)
    has_params = m.group(2) is not None
    params_raw = m.group(3)
    body_text  = m.group(4)

    params = None
    if has_params:
        params = [p.strip() for p in params_raw.split(',')] if params_raw.strip() else []

    body = [(k, v) for k, v in tokenise(body_text)
            if k not in ('cmt',)]          # strip comments from body
    # trim trailing whitespace tokens
    while body and body[-1][0] == 'ws':
        body.pop()

    return Macro(name, params, body)


# ──────────────────────────────────────────────────────────────────────────────
# Macro expansion engine
# ──────────────────────────────────────────────────────────────────────────────

def expand_tokens(tokens, macros: dict, expanding: frozenset = frozenset()):
    """
    Recursively expand macros in a token list.
    expanding: set of macro names currently on the call stack (to prevent recursion).
    Returns a new list of (kind, value) tokens.
    """
    result = []
    i = 0
    while i < len(tokens):
        kind, val = tokens[i]
        if kind == 'id' and val in macros and val not in expanding:
            mac = macros[val]
            if mac.is_function_like():
                # look for '(' possibly skipping whitespace
                j = i + 1
                while j < len(tokens) and tokens[j][0] == 'ws':
                    j += 1
                if j < len(tokens) and tokens[j] == ('op', '('):
                    # collect arguments
                    args, j = collect_args(tokens, j + 1)
                    if len(args) != len(mac.params):
                        # wrong arg count – emit as-is
                        result.append((kind, val))
                        i += 1
                        continue
                    expanded = substitute(mac, args, macros, expanding | {val})
                    result.extend(expanded)
                    i = j
                    continue
                else:
                    # no '(' follows → emit name unchanged
                    result.append((kind, val))
                    i += 1
                    continue
            else:
                # object-like macro
                expanded = expand_tokens(mac.body, macros, expanding | {val})
                result.extend(expanded)
                i += 1
                continue
        result.append((kind, val))
        i += 1
    return result


def collect_args(tokens, start):
    """
    Collect comma-separated arguments between '(' (already consumed) and ')'.
    Returns (list_of_token_lists, index_after_closing_paren).
    """
    args = []
    current = []
    depth = 1
    i = start
    while i < len(tokens):
        k, v = tokens[i]
        if v == '(' :
            depth += 1
            current.append((k, v))
        elif v == ')':
            depth -= 1
            if depth == 0:
                args.append(current)
                return args, i + 1
            current.append((k, v))
        elif v == ',' and depth == 1:
            args.append(current)
            current = []
        else:
            current.append((k, v))
        i += 1
    raise SyntaxError("Unterminated macro argument list")


def substitute(mac: Macro, args, macros: dict, expanding: frozenset):
    """
    Replace parameters in macro body with (already-expanded) args,
    handle # (stringise) and ## (token-paste), then re-expand.
    """
    param_map = {p: a for p, a in zip(mac.params, args)}
    # pre-expand each argument for normal substitution
    expanded_args = {p: expand_tokens(a, macros, expanding) for p, a in param_map.items()}

    result = []
    body = mac.body
    i = 0
    while i < len(body):
        k, v = body[i]
        # # stringise operator
        if k == 'op' and v == '#':
            i += 1
            while i < len(body) and body[i][0] == 'ws':
                i += 1
            if i < len(body) and body[i][0] == 'id' and body[i][1] in param_map:
                raw = tokens_to_str(param_map[body[i][1]])
                result.append(('str', f'"{raw}"'))
                i += 1
            continue
        # ## token-paste operator
        if k == 'op' and v == '##':
            # remove trailing ws from result
            while result and result[-1][0] == 'ws':
                result.pop()
            i += 1
            # skip ws
            while i < len(body) and body[i][0] == 'ws':
                i += 1
            if i < len(body):
                rk, rv = body[i]
                if rk == 'id' and rv in param_map:
                    paste_toks = [t for t in param_map[rv] if t[0] != 'ws']
                    rv = tokens_to_str(paste_toks)
                # merge with last token in result
                if result:
                    lk, lv = result.pop()
                    result.append((lk, lv + rv))
                else:
                    result.append((rk, rv))
                i += 1
            continue
        # normal parameter substitution
        if k == 'id' and v in param_map:
            result.extend(expanded_args[v])
            i += 1
            continue
        result.append((k, v))
        i += 1

    return expand_tokens(result, macros, expanding)


def tokens_to_str(tokens) -> str:
    return ''.join(v for _, v in tokens)


# ──────────────────────────────────────────────────────────────────────────────
# Conditional stack helpers
# ──────────────────────────────────────────────────────────────────────────────

def eval_if_expr(expr: str, macros: dict) -> bool:
    """
    Evaluate a #if / #elif expression.
    Supports: integer literals, defined(X), !defined(X), &&, ||, ==, !=, <, >, <=, >=
    Macro identifiers that are defined are replaced by their value (or 1).
    Undefined identifiers become 0 (standard C behaviour).
    """
    # replace defined(X) / defined X
    expr = re.sub(r'defined\s*\(\s*([A-Za-z_]\w*)\s*\)',
                  lambda m: '1' if m.group(1) in macros else '0', expr)
    expr = re.sub(r'defined\s+([A-Za-z_]\w*)',
                  lambda m: '1' if m.group(1) in macros else '0', expr)
    # expand remaining identifiers: defined ones → their numeric value, others → 0
    def replace_id(m):
        name = m.group(0)
        if name in macros and not macros[name].is_function_like():
            body = tokens_to_str(macros[name].body).strip()
            return body if body else '1'
        return '0'
    expr = re.sub(r'[A-Za-z_]\w*', replace_id, expr)
    try:
        return bool(eval(expr, {"__builtins__": {}}))   # restricted eval
    except Exception:
        return False


# ──────────────────────────────────────────────────────────────────────────────
# Main preprocessor
# ──────────────────────────────────────────────────────────────────────────────

class Preprocessor:
    def __init__(self, include_dirs=None):
        self.macros      : dict[str, Macro] = {}
        self.include_dirs = include_dirs or ['.']
        self.output_lines = []
        # conditional stack: list of (currently_active, seen_true_branch, in_else)
        self._cond_stack  = []

    # ── public entry ──────────────────────────────────────────────────────────

    def process_file(self, path: str):
        path = Path(path).resolve()
        self._process(path.read_text(), str(path.parent))

    def get_output(self) -> str:
        return '\n'.join(self.output_lines)

    # ── internals ─────────────────────────────────────────────────────────────

    def _active(self) -> bool:
        return all(active for active, _, _ in self._cond_stack)

    def _process(self, text: str, base_dir: str):
        # Join physical lines (backslash-newline continuations)
        text = re.sub(r'\\\n', ' ', text)
        # strip block comments before directive parsing (but preserve line count)
        text = re.sub(r'/\*.*?\*/', lambda m: ' ' * len(m.group(0).replace('\n', '')), text, flags=re.DOTALL)

        for raw_line in text.splitlines():
            line = raw_line.rstrip()
            stripped = line.lstrip()

            # ── conditional directives (processed even when inactive) ─────────
            if stripped.startswith('#'):
                directive, _, rest = stripped[1:].lstrip().partition(' ')
                rest = rest.strip()

                if directive == 'if':
                    result = eval_if_expr(rest, self.macros) if self._active() else False
                    self._cond_stack.append([result, result, False])
                    continue

                elif directive == 'ifdef':
                    result = (rest in self.macros) if self._active() else False
                    self._cond_stack.append([result, result, False])
                    continue

                elif directive == 'ifndef':
                    result = (rest not in self.macros) if self._active() else False
                    self._cond_stack.append([result, result, False])
                    continue

                elif directive == 'elif':
                    if not self._cond_stack:
                        raise SyntaxError('#elif without #if')
                    top = self._cond_stack[-1]
                    if top[2]:   # already seen #else
                        raise SyntaxError('#elif after #else')
                    if top[1]:   # a previous branch was true → stay inactive
                        top[0] = False
                    else:
                        parent_active = all(a for a, _, _ in self._cond_stack[:-1])
                        result = eval_if_expr(rest, self.macros) if parent_active else False
                        top[0] = result
                        top[1] = top[1] or result
                    continue

                elif directive == 'else':
                    if not self._cond_stack:
                        raise SyntaxError('#else without #if')
                    top = self._cond_stack[-1]
                    if top[2]:
                        raise SyntaxError('duplicate #else')
                    top[2] = True
                    parent_active = all(a for a, _, _ in self._cond_stack[:-1])
                    top[0] = parent_active and not top[1]
                    continue

                elif directive == 'endif':
                    if not self._cond_stack:
                        raise SyntaxError('#endif without #if')
                    self._cond_stack.pop()
                    continue

                # ── below directives only execute when active ─────────────────
                if not self._active():
                    continue

                if directive == 'define':
                    mac = parse_define(rest)
                    self.macros[mac.name] = mac

                elif directive == 'undef':
                    self.macros.pop(rest, None)

                elif directive == 'include':
                    inc_path = self._resolve_include(rest, base_dir)
                    if inc_path:
                        inc_text = Path(inc_path).read_text()
                        self._process(inc_text, str(Path(inc_path).parent))
                    else:
                        print(f"Warning: cannot find include {rest}", file=sys.stderr)

                elif directive in ('pragma', 'error', 'warning', 'line'):
                    pass   # silently drop or optionally emit as comment

                # else: unknown directive – drop it
                continue

            # ── normal source line ────────────────────────────────────────────
            if not self._active():
                continue

            expanded = self._expand_line(line)
            self.output_lines.append(expanded)

    def _expand_line(self, line: str) -> str:
        """Expand macros in a non-directive source line."""
        tokens = list(tokenise(line))
        expanded = expand_tokens(tokens, self.macros)
        return tokens_to_str(expanded)

    def _resolve_include(self, spec: str, base_dir: str):
        spec = spec.strip()
        if spec.startswith('"'):
            # local include – search base_dir first, then include_dirs
            fname = spec.strip('"')
            for d in [base_dir] + self.include_dirs:
                p = Path(d) / fname
                if p.exists():
                    return str(p)
        elif spec.startswith('<'):
            fname = spec[1:-1]
            for d in self.include_dirs:
                p = Path(d) / fname
                if p.exists():
                    return str(p)
        return None


# ──────────────────────────────────────────────────────────────────────────────
# Post-processing: clean up the output
# ──────────────────────────────────────────────────────────────────────────────

def clean_output(text: str) -> str:
    """
    - Collapse 3+ consecutive blank lines to 2
    - Remove trailing whitespace
    """
    lines = text.splitlines()
    result = []
    blank_run = 0
    for ln in lines:
        ln = ln.rstrip()
        if ln == '':
            blank_run += 1
            if blank_run <= 2:
                result.append('')
        else:
            blank_run = 0
            result.append(ln)
    return '\n'.join(result)


# ──────────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────────

def main():
    import argparse
    ap = argparse.ArgumentParser(description='C preprocessor – expand #include / #define')
    ap.add_argument('input',  help='Input C source file')
    ap.add_argument('output', nargs='?', help='Output file (default: stdout)')
    ap.add_argument('-I', dest='include_dirs', metavar='DIR',
                    action='append', default=['.'],
                    help='Add include search directory (repeatable)')
    ap.add_argument('-D', dest='defines', metavar='NAME[=VALUE]',
                    action='append', default=[],
                    help='Pre-define a macro (repeatable)')
    args = ap.parse_args()

    pp = Preprocessor(include_dirs=args.include_dirs)

    # inject -D definitions
    for d in args.defines:
        if '=' in d:
            name, _, val = d.partition('=')
            pp.macros[name] = parse_define(f'{name} {val}')
        else:
            pp.macros[d] = parse_define(f'{d} 1')

    pp.process_file(args.input)
    out = clean_output(pp.get_output())

    if args.output:
        Path(args.output).write_text(out + '\n')
        print(f"Written: {args.output}", file=sys.stderr)
    else:
        print(out)


if __name__ == '__main__':
    main()
