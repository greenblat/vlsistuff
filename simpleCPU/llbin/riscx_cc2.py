#!/usr/bin/env python3
"""
riscx_cc2.py — C compiler for simpleCPU (32-bit RISC, 32 registers)

Supported C subset
──────────────────
  Types:    int, int*  (32-bit)
  Globals:  int x;  int arr[N];
  Locals:   int x;  int x = expr;  int arr[N];  int *p;
  Ops:      + - * & | ^ ~ ! << >>  (all compound: += -= *= &= |= ^= <<= >>=)
            ++ --  (prefix and postfix)
  Compare:  == != < > <= >=   Logical: && ||
  Control:  if/else  while  do-while  for  break  continue  return
  Builtins (no declaration needed):
    __stop()                   STOP
    __nop(imm8)                NOP with immediate (literal only)
    __finish_good()            FINISH_GOOD
    __finish_bad()             FINISH_BAD
    __load(addr)               → mem[addr]
    __store(addr, val)         mem[addr] = val
    __ext_load(addr)           → ext_mem[addr]  (ext_field=1)
    __ext_store(addr, val)     ext_mem[addr] = val (ext_field=1)
    __sleep(duration)          SLEEP reg, 0
    __opcode(0xXXXXXXXX)      emit raw word (literal only)

Register ABI
────────────
  R0       return value
  R1–R6    arguments (caller-saved)
  R7–R26   locals / callee-saved  (max 20 vars per function)
  R27      zero register (init 0 at startup, never written)
  R28–R30  scratch (caller-saved)
  R31      software stack pointer, init 0xFFFC, grows down

Memory map (byte addresses, 4-byte aligned)
────────────────────────────────────────────
  0x0000–0x7FFC  program code
  0x8000–0xFFFC  global / static data

Branch encoding
───────────────
  PC += sign_extend(imm9)  where imm9 is a signed byte offset
  Range ±255 bytes; auto-expanded to BRANCH(inv)+8 / JUMP for longer ranges.

Flags (set by SUB, used by BRANCH.cond)
────────────────────────────────────────
  0=always  1=eq  2=ne  3=lt  4=gt  5=le  6=ge
"""

import sys, re
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, Set

# ═══════════════════════════════════════════════════════════════════════════════
#  ISA ENCODINGS  (verified against riscx_decoder.v / riscx_asm_coding.py)
# ═══════════════════════════════════════════════════════════════════════════════

COND_ALWAYS              = 0
COND_EQ, COND_NE         = 1, 2
COND_LT, COND_GT         = 3, 4
COND_LE, COND_GE         = 5, 6

INV_COND = {
    COND_EQ: COND_NE, COND_NE: COND_EQ,
    COND_LT: COND_GE, COND_GE: COND_LT,
    COND_GT: COND_LE, COND_LE: COND_GT,
    COND_ALWAYS: COND_ALWAYS,
}
COND_NAME = {0:'always', 1:'eq', 2:'ne', 3:'lt', 4:'gt', 5:'le', 6:'ge'}

# branch-to-false-label condition for each comparison operator (sub L,R)
_CMP_FALSE = {
    '==': COND_NE,  '!=': COND_EQ,
    '<' : COND_GE,  '>=': COND_LT,
    '>' : COND_LE,  '<=': COND_GT,
}

def _m(n: int, bits: int) -> int:
    return n & ((1 << bits) - 1)

# fixed-encoding instructions
def enc_stop():                    return 0xfb8b3adf
def enc_finish_good():             return 0xfb8b3ade
def enc_finish_bad():              return 0xfb8b3add
def enc_return():                  return 0xfb8b3adc
def enc_nop(imm8=0):               return 0xfb8b3b00 | _m(imm8, 8)
def enc_neg(dst):                  return 0xfb8b3ae0 | _m(dst, 5)
def enc_move(dst, src):            return 0xfb8b3c00 | (_m(src,5)<<5) | _m(dst,5)

# memory
def enc_load(dst, src, off8=0):    return 0xfb980000 | (_m(off8,8)<<10) | (_m(src,5)<<5) | _m(dst,5)
def enc_store(base, src, off8=0):  return 0xfb900000 | (_m(off8,8)<<10) | (_m(src,5)<<5) | _m(base,5)
def enc_ext_load(dst,src,off8=0):  return 0xfb9c0000 | (_m(off8,8)<<10) | (_m(src,5)<<5) | _m(dst,5)
def enc_ext_store(base,src,off8=0):return 0xfb940000 | (_m(off8,8)<<10) | (_m(src,5)<<5) | _m(base,5)
def enc_loadabs(dst, addr16):      return 0xfbe00000 | (_m(addr16,16)<<5) | _m(dst,5)
def enc_storeabs(src, addr16):     return 0xfbc00000 | (_m(addr16,16)<<5) | _m(src,5)

# control
def enc_call(addr16):              return 0xfb8f0000 | _m(addr16,16)
def enc_jump(addr16):              return 0xfb8e0000 | _m(addr16,16)
def enc_branch(cond, imm9):        return 0xfb8b7000 | (_m(imm9,9)<<3) | _m(cond,3)
def enc_sleep(dst, imm16=0):       return 0xfba00000 | (_m(imm16,15)<<5) | _m(dst,5)  # bit20=0 (RTL fix)

# load-immediate (unchanged)
def enc_loadi(dst, imm20):         return 0xfe000000 | (_m(imm20,20)<<5) | _m(dst,5)
def enc_loadih(dst, imm20):        return 0xfc000000 | (_m(imm20,20)<<5) | _m(dst,5)

# immediate ALU
def enc_addi(dst, imm10):          return 0xfb8d8000 | (_m(imm10,10)<<5) | _m(dst,5)
def enc_subi(dst, imm10):          return 0xfb8d0000 | (_m(imm10,10)<<5) | _m(dst,5)
def enc_muli(dst, imm10):          return 0xfb8c8000 | (_m(imm10,10)<<5) | _m(dst,5)
def enc_andi(dst, imm10):          return 0xfb8c0000 | (_m(imm10,10)<<5) | _m(dst,5)
def enc_ori(dst,  imm10):          return 0xfb8b8000 | (_m(imm10,10)<<5) | _m(dst,5)

# register ALU
def enc_add(dst, src):             return 0xfb8b6800 | (_m(src,5)<<5) | _m(dst,5)
def enc_sub(dst, src):             return 0xfb8b6400 | (_m(src,5)<<5) | _m(dst,5)
def enc_mul(dst, src):             return 0xfb8b6c00 | (_m(src,5)<<5) | _m(dst,5)
def enc_and(dst, src):             return 0xfb8b6000 | (_m(src,5)<<5) | _m(dst,5)
def enc_or(dst,  src):             return 0xfb8b5c00 | (_m(src,5)<<5) | _m(dst,5)
def enc_xor(dst, src):             return 0xfb8b5800 | (_m(src,5)<<5) | _m(dst,5)

# shifts by immediate
def enc_shiftl(dst, imm5):         return 0xfb8b4400 | (_m(imm5,5)<<5) | _m(dst,5)
def enc_shiftr(dst, imm5):         return 0xfb8b4800 | (_m(imm5,5)<<5) | _m(dst,5)
def enc_shiftar(dst, imm5):        return 0xfb8b4000 | (_m(imm5,5)<<5) | _m(dst,5)

# shifts by register
def enc_shiftl_r(dst, src):        return 0xfb8b4c00 | (_m(src,5)<<5) | _m(dst,5)
def enc_shiftr_r(dst, src):        return 0xfb8b5400 | (_m(src,5)<<5) | _m(dst,5)
def enc_shiftar_r(dst, src):       return 0xfb8b5000 | (_m(src,5)<<5) | _m(dst,5)

# ── register names ────────────────────────────────────────────────────────────
R_RET  = 0
R_ARG  = list(range(1, 7))    # R1..R6  arguments
R_LOC  = list(range(7, 27))   # R7..R26 callee-saved locals (max 20 per fn)
R_ZERO = 27                   # constant 0
R_T0   = 28                   # scratch / caller-saved
R_T1   = 29
R_T2   = 30
R_SP   = 31                   # software stack pointer

GLOBAL_BASE = 0x8000

# ═══════════════════════════════════════════════════════════════════════════════
#  DISASSEMBLER  (used only for listing output)
# ═══════════════════════════════════════════════════════════════════════════════

def disasm(w: int) -> str:
    w &= 0xFFFFFFFF
    dst  = w & 0x1f
    src  = (w >> 5) & 0x1f
    off8 = (w >> 10) & 0xff
    i5   = (w >> 5) & 0x1f
    i10  = (w >> 5) & 0x3ff
    i20  = (w >> 5) & 0xfffff
    a16  = w & 0xffff
    raw9 = (w >> 3) & 0x1ff
    i9   = raw9 - 512 if raw9 >= 256 else raw9
    cond = w & 7

    def r(n):  return f'r{n}'
    def h(n):  return f'0x{n:x}'
    def cn():  return COND_NAME.get(cond, str(cond))

    if w == 0xfb8b3adf: return 'STOP'
    if w == 0xfb8b3ade: return 'FINISH_GOOD'
    if w == 0xfb8b3add: return 'FINISH_BAD'
    if w == 0xfb8b3adc: return 'RETURN'
    if (w & 0xffffff00) == 0xfb8b3b00: return f'NOP {h(w&0xff)}'
    if (w & 0xffffffe0) == 0xfb8b3ae0: return f'NEG {r(dst)}'
    if (w & 0xfffffc00) == 0xfb8b3c00: return f'MOVE {r(dst)}, {r(src)}'
    if (w & 0xfffc0000) == 0xfb9c0000:   # EXT_LOAD (bit18 set)
        return f'EXT_LOAD {r(dst)}, [{r(src)}+{h(off8)}]' if off8 else f'EXT_LOAD {r(dst)}, [{r(src)}]'
    if (w & 0xfffc0000) == 0xfb940000:   # EXT_STORE (bit18 set)
        return f'EXT_STORE [{r(dst)}+{h(off8)}], {r(src)}' if off8 else f'EXT_STORE [{r(dst)}], {r(src)}'
    if (w & 0xfff80000) == 0xfb980000:
        return f'LOAD {r(dst)}, [{r(src)}+{h(off8)}]' if off8 else f'LOAD {r(dst)}, [{r(src)}]'
    if (w & 0xfff80000) == 0xfb900000:
        return f'STORE [{r(dst)}+{h(off8)}], {r(src)}' if off8 else f'STORE [{r(dst)}], {r(src)}'
    if (w & 0xffe00000) == 0xfbe00000: return f'LOADABS  {r(dst)}, {h((w>>5)&0xffff)}'
    if (w & 0xffe00000) == 0xfbc00000: return f'STOREABS {h((w>>5)&0xffff)}, {r(dst)}'
    if (w & 0xffff0000) == 0xfb8f0000: return f'CALL {h(a16)}'
    if (w & 0xffff0000) == 0xfb8e0000: return f'JUMP {h(a16)}'
    if (w & 0xfffff000) == 0xfb8b7000: return f'BRANCH.{cn()} {i9:+d}'
    if (w & 0xffff8000) == 0xfb8d8000: return f'ADDI {r(dst)}, {h(i10)}'
    if (w & 0xffff8000) == 0xfb8d0000: return f'SUBI {r(dst)}, {h(i10)}'
    if (w & 0xffff8000) == 0xfb8c8000: return f'MULI {r(dst)}, {h(i10)}'
    if (w & 0xffff8000) == 0xfb8c0000: return f'ANDI {r(dst)}, {h(i10)}'
    if (w & 0xffff8000) == 0xfb8b8000: return f'ORI  {r(dst)}, {h(i10)}'
    if (w & 0xfe000000) == 0xfe000000: return f'LOADI  {r(dst)}, {h(i20)}'
    if (w & 0xfe000000) == 0xfc000000: return f'LOADIH {r(dst)}, {h(i20)}'
    if (w & 0xfffffc00) == 0xfb8b6c00: return f'MUL {r(dst)}, {r(src)}'
    if (w & 0xfffffc00) == 0xfb8b6800: return f'ADD {r(dst)}, {r(src)}'
    if (w & 0xfffffc00) == 0xfb8b6400: return f'SUB {r(dst)}, {r(src)}'
    if (w & 0xfffffc00) == 0xfb8b6000: return f'AND {r(dst)}, {r(src)}'
    if (w & 0xfffffc00) == 0xfb8b5c00: return f'OR  {r(dst)}, {r(src)}'
    if (w & 0xfffffc00) == 0xfb8b5800: return f'XOR {r(dst)}, {r(src)}'
    if (w & 0xfffffc00) == 0xfb8b5400: return f'SHIFTR_R  {r(dst)}, {r(src)}'
    if (w & 0xfffffc00) == 0xfb8b5000: return f'SHIFTAR_R {r(dst)}, {r(src)}'
    if (w & 0xfffffc00) == 0xfb8b4c00: return f'SHIFTL_R  {r(dst)}, {r(src)}'
    if (w & 0xfffffc00) == 0xfb8b4800: return f'SHIFTR  {r(dst)}, {h(i5)}'
    if (w & 0xfffffc00) == 0xfb8b4400: return f'SHIFTL  {r(dst)}, {h(i5)}'
    if (w & 0xfffffc00) == 0xfb8b4000: return f'SHIFTAR {r(dst)}, {h(i5)}'
    if (w & 0xfff00000) == 0xfba00000:
        imm = (w >> 5) & 0x7fff
        return f'SLEEP {r(dst)}, {imm}' if imm else f'SLEEP {r(dst)}'
    return f'?? {w:#010x}'

# ═══════════════════════════════════════════════════════════════════════════════
#  LEXER
# ═══════════════════════════════════════════════════════════════════════════════

KEYWORDS = {'int','void','if','else','while','do','for','break','continue','return'}

@dataclass
class Token:
    kind: str   # KW ID NUM OP PUNCT EOF
    val:  Any
    line: int

    def __repr__(self):
        return f'Token({self.kind},{self.val!r},L{self.line})'

def lex(src: str) -> List[Token]:
    toks: List[Token] = []
    i, line = 0, 1

    while i < len(src):
        c = src[i]
        # whitespace / newline
        if c == '\n':
            line += 1; i += 1; continue
        if c.isspace():
            i += 1; continue
        # line comment
        if src[i:i+2] == '//':
            while i < len(src) and src[i] != '\n': i += 1
            continue
        # block comment
        if src[i:i+2] == '/*':
            i += 2
            while i < len(src)-1 and src[i:i+2] != '*/':
                if src[i] == '\n': line += 1
                i += 1
            i += 2; continue
        # number: hex or decimal
        if c.isdigit() or (c == '0' and i+1 < len(src) and src[i+1] in 'xX'):
            if src[i:i+2] in ('0x','0X'):
                j = i+2
                while j < len(src) and src[j] in '0123456789abcdefABCDEF': j += 1
                toks.append(Token('NUM', int(src[i:j],16), line)); i = j
            else:
                j = i
                while j < len(src) and src[j].isdigit(): j += 1
                toks.append(Token('NUM', int(src[i:j]), line)); i = j
            continue
        # identifier / keyword
        if c.isalpha() or c == '_':
            j = i
            while j < len(src) and (src[j].isalnum() or src[j]=='_'): j += 1
            word = src[i:j]
            toks.append(Token('KW' if word in KEYWORDS else 'ID', word, line))
            i = j; continue
        # multi-char operators (longest match first)
        three = src[i:i+3]
        if three in ('<<=', '>>='):
            toks.append(Token('OP', three, line)); i += 3; continue
        two = src[i:i+2]
        if two in ('==','!=','<=','>=','<<','>>','&&','||',
                   '+=','-=','*=','&=','|=','^=','++','--'):
            toks.append(Token('OP', two, line)); i += 2; continue
        # single-char operators
        if c in '+-*/%&|^~!<>=':
            toks.append(Token('OP', c, line)); i += 1; continue
        if c in '(){};,[]':
            toks.append(Token('PUNCT', c, line)); i += 1; continue
        raise SyntaxError(f"line {line}: unexpected character '{c}'")

    toks.append(Token('EOF', None, line))
    return toks

# ═══════════════════════════════════════════════════════════════════════════════
#  AST NODES
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class Num:      val: int
@dataclass
class Var:      name: str
@dataclass
class ArrIdx:   name: str;  idx: Any
@dataclass
class AddrOf:   expr: Any
@dataclass
class Deref:    expr: Any
@dataclass
class BinOp:    op: str;    left: Any;   right: Any
@dataclass
class UnOp:     op: str;    expr: Any
@dataclass
class PreInc:   op: str;    expr: Any    # op: '++' or '--'
@dataclass
class PostInc:  op: str;    expr: Any    # op: '++' or '--'
@dataclass
class Call:     name: str;  args: List
@dataclass
class Assign:   target: Any; val: Any

@dataclass
class IfStmt:      cond: Any; then: list; els: list
@dataclass
class WhileStmt:   cond: Any; body: list
@dataclass
class DoWhileStmt: body: list; cond: Any
@dataclass
class ForStmt:     init: Any; cond: Any; step: Any; body: list
@dataclass
class RetStmt:     expr: Any
@dataclass
class BreakStmt:   pass
@dataclass
class ContinueStmt: pass

@dataclass
class VarDecl:
    name:     str
    ptr:      bool = False
    arr_size: int  = 0
    init:     Any  = None   # optional initializer expression

@dataclass
class Function:
    name:     str
    params:   List[str]
    decls:    List[VarDecl]
    body:     list
    ret_void: bool = False

@dataclass
class GlobalVar:
    name: str
    size: int = 1

@dataclass
class Program:
    globals: List[GlobalVar]
    funcs:   List[Function]

# ═══════════════════════════════════════════════════════════════════════════════
#  PARSER
# ═══════════════════════════════════════════════════════════════════════════════

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos    = 0

    # ── token primitives ─────────────────────────────────────────────────────

    def peek(self)    -> Token: return self.tokens[self.pos]
    def advance(self) -> Token: t = self.tokens[self.pos]; self.pos += 1; return t

    def expect(self, kind: str, val=None) -> Token:
        t = self.advance()
        if t.kind != kind or (val is not None and t.val != val):
            exp = f"'{val}'" if val else kind
            raise SyntaxError(f"line {t.line}: expected {exp}, got '{t.val}'")
        return t

    def match(self, kind: str, val=None) -> Optional[Token]:
        t = self.peek()
        if t.kind == kind and (val is None or t.val == val):
            return self.advance()
        return None

    # ── top-level ────────────────────────────────────────────────────────────

    def parse_program(self) -> Program:
        globs: List[GlobalVar] = []
        funcs: List[Function]  = []
        while self.peek().kind != 'EOF':
            typ, _ptr = self.parse_type()
            name = self.expect('ID').val
            if self.match('PUNCT', '('):
                funcs.append(self._parse_function_body(typ, name))
            elif self.match('PUNCT', '['):
                sz = self.expect('NUM').val
                self.expect('PUNCT', ']')
                self.expect('PUNCT', ';')
                globs.append(GlobalVar(name, sz))
            else:
                self.expect('PUNCT', ';')
                globs.append(GlobalVar(name, 1))
        return Program(globs, funcs)

    def parse_type(self):
        t = self.advance()
        if t.kind != 'KW' or t.val not in ('int','void'):
            raise SyntaxError(f"line {t.line}: expected type, got '{t.val}'")
        is_ptr = bool(self.match('OP', '*'))
        return t.val, is_ptr

    def _parse_function_body(self, typ: str, name: str) -> Function:
        params: List[str] = []
        while not self.match('PUNCT', ')'):
            _t, _p = self.parse_type()
            if self.peek().kind == 'OP' and self.peek().val == '*':
                self.advance()
            params.append(self.expect('ID').val)
            self.match('PUNCT', ',')
        self.expect('PUNCT', '{')
        decls: List[VarDecl] = []
        while self.peek().kind == 'KW' and self.peek().val == 'int':
            decls.extend(self._parse_var_decls())
        body = []
        while not self.match('PUNCT', '}'):
            body.append(self.parse_stmt())
        return Function(name, params, decls, body, ret_void=(typ=='void'))

    def _parse_var_decls(self) -> List[VarDecl]:
        """Parse one 'int ..., ...;' declaration line."""
        self.expect('KW', 'int')
        decls = []
        while True:
            is_ptr = bool(self.match('OP', '*'))
            vname  = self.expect('ID').val
            if self.match('PUNCT', '['):
                sz = self.expect('NUM').val
                self.expect('PUNCT', ']')
                decls.append(VarDecl(vname, is_ptr, sz, None))
            else:
                init = self.parse_expr() if self.match('OP', '=') else None
                decls.append(VarDecl(vname, is_ptr, 0, init))
            if not self.match('PUNCT', ','):
                break
        self.expect('PUNCT', ';')
        return decls

    # ── statements ───────────────────────────────────────────────────────────

    def parse_stmt(self) -> Any:
        t = self.peek()
        if t.kind == 'KW':
            if t.val == 'if':       return self._parse_if()
            if t.val == 'while':    return self._parse_while()
            if t.val == 'do':       return self._parse_do_while()
            if t.val == 'for':      return self._parse_for()
            if t.val == 'return':
                self.advance()
                e = None if self.peek().val == ';' else self.parse_expr()
                self.expect('PUNCT', ';')
                return RetStmt(e)
            if t.val == 'break':
                self.advance(); self.expect('PUNCT', ';')
                return BreakStmt()
            if t.val == 'continue':
                self.advance(); self.expect('PUNCT', ';')
                return ContinueStmt()
        if self.peek().kind == 'PUNCT' and self.peek().val == '{':
            return self._parse_block_as_compound()
        expr = self.parse_expr()
        self.expect('PUNCT', ';')
        return expr

    def _parse_block_as_compound(self):
        self.expect('PUNCT', '{')
        stmts = []
        while not self.match('PUNCT', '}'):
            stmts.append(self.parse_stmt())
        return stmts   # list of stmts (handled by caller unrolling)

    def parse_block(self) -> list:
        if self.match('PUNCT', '{'):
            stmts = []
            while not self.match('PUNCT', '}'):
                s = self.parse_stmt()
                if isinstance(s, list):
                    stmts.extend(s)
                else:
                    stmts.append(s)
            return stmts
        s = self.parse_stmt()
        return s if isinstance(s, list) else [s]

    def _parse_if(self) -> IfStmt:
        self.expect('KW', 'if')
        self.expect('PUNCT', '(')
        cond = self.parse_expr()
        self.expect('PUNCT', ')')
        then = self.parse_block()
        els  = self.parse_block() if self.match('KW', 'else') else []
        return IfStmt(cond, then, els)

    def _parse_while(self) -> WhileStmt:
        self.expect('KW', 'while')
        self.expect('PUNCT', '('); cond = self.parse_expr(); self.expect('PUNCT', ')')
        return WhileStmt(cond, self.parse_block())

    def _parse_do_while(self) -> DoWhileStmt:
        self.expect('KW', 'do')
        body = self.parse_block()
        self.expect('KW', 'while')
        self.expect('PUNCT', '('); cond = self.parse_expr(); self.expect('PUNCT', ')')
        self.expect('PUNCT', ';')
        return DoWhileStmt(body, cond)

    def _parse_for(self) -> ForStmt:
        self.expect('KW', 'for'); self.expect('PUNCT', '(')
        init = None if self.peek().val == ';' else self.parse_expr()
        self.expect('PUNCT', ';')
        cond = None if self.peek().val == ';' else self.parse_expr()
        self.expect('PUNCT', ';')
        step = None if self.peek().val == ')' else self.parse_expr()
        self.expect('PUNCT', ')')
        return ForStmt(init, cond, step, self.parse_block())

    # ── expressions ──────────────────────────────────────────────────────────

    def parse_expr(self)    -> Any: return self._parse_assign()

    def _parse_assign(self) -> Any:
        left = self._parse_lor()
        t    = self.peek()
        cmp  = {'+=':'+','-=':'-','*=':'*','&=':'&','|=':'|','^=':'^',
                '<<=':'<<','>>=':'>>'}
        if t.kind == 'OP' and t.val in ('=', *cmp):
            op = self.advance().val
            rhs = self._parse_assign()
            if op != '=': rhs = BinOp(cmp[op], left, rhs)
            return Assign(left, rhs)
        return left

    def _parse_lor(self)   -> Any: return self._binop(self._parse_land,  ('||',))
    def _parse_land(self)  -> Any: return self._binop(self._parse_eq,    ('&&',))
    def _parse_eq(self)    -> Any: return self._binop(self._parse_rel,   ('==','!='))
    def _parse_rel(self)   -> Any: return self._binop(self._parse_bitor, ('<','>','<=','>='))
    def _parse_bitor(self) -> Any: return self._binop(self._parse_bitxor,('|',))
    def _parse_bitxor(self)-> Any: return self._binop(self._parse_bitand,('^',))
    def _parse_bitand(self)-> Any: return self._binop(self._parse_shift, ('&',))
    def _parse_shift(self) -> Any: return self._binop(self._parse_add,   ('<<','>>'))
    def _parse_add(self)   -> Any: return self._binop(self._parse_mul,   ('+','-'))
    def _parse_mul(self)   -> Any: return self._binop(self._parse_unary, ('*',))

    def _binop(self, sub, ops) -> Any:
        left = sub()
        while self.peek().kind == 'OP' and self.peek().val in ops:
            op = self.advance().val; left = BinOp(op, left, sub())
        return left

    def _parse_unary(self) -> Any:
        t = self.peek()
        if t.kind == 'OP':
            if t.val == '-': self.advance(); return UnOp('-', self._parse_unary())
            if t.val == '+': self.advance(); return self._parse_unary()
            if t.val == '~': self.advance(); return UnOp('~', self._parse_unary())
            if t.val == '!': self.advance(); return UnOp('!', self._parse_unary())
            if t.val == '*': self.advance(); return Deref(self._parse_unary())
            if t.val == '&': self.advance(); return AddrOf(self._parse_unary())
            if t.val == '++': self.advance(); return PreInc('++', self._parse_unary())
            if t.val == '--': self.advance(); return PreInc('--', self._parse_unary())
        return self._parse_postfix()

    def _parse_postfix(self) -> Any:
        base = self._parse_primary()
        while True:
            if self.match('PUNCT', '['):
                idx = self.parse_expr(); self.expect('PUNCT', ']')
                base = ArrIdx(base.name, idx) if isinstance(base, Var) \
                       else Deref(BinOp('+', base, BinOp('*', idx, Num(4))))
            elif self.peek().kind == 'OP' and self.peek().val == '++':
                self.advance(); base = PostInc('++', base)
            elif self.peek().kind == 'OP' and self.peek().val == '--':
                self.advance(); base = PostInc('--', base)
            else:
                break
        return base

    def _parse_primary(self) -> Any:
        t = self.peek()
        if t.kind == 'NUM':
            self.advance(); return Num(t.val)
        if t.kind == 'ID':
            self.advance(); name = t.val
            if self.match('PUNCT', '('):
                args = []
                while not self.match('PUNCT', ')'):
                    args.append(self.parse_expr()); self.match('PUNCT', ',')
                return Call(name, args)
            return Var(name)
        if t.kind == 'PUNCT' and t.val == '(':
            self.advance(); e = self.parse_expr(); self.expect('PUNCT', ')'); return e
        raise SyntaxError(f"line {t.line}: unexpected token '{t.val}'")

# ═══════════════════════════════════════════════════════════════════════════════
#  CODE ITEMS  (intermediate representation fed to assembler)
# ═══════════════════════════════════════════════════════════════════════════════

class WordI:
    __slots__ = ('word','note')
    def __init__(self, word, note=''): self.word = word & 0xFFFFFFFF; self.note = note

class LabelI:
    __slots__ = ('name',)
    def __init__(self, name): self.name = name

class BranchI:
    __slots__ = ('cond','lbl','note')
    def __init__(self, cond, lbl, note=''): self.cond=cond; self.lbl=lbl; self.note=note

class JumpI:
    __slots__ = ('lbl','note')
    def __init__(self, lbl, note=''): self.lbl=lbl; self.note=note

class CallI:
    __slots__ = ('lbl','note')
    def __init__(self, lbl, note=''): self.lbl=lbl; self.note=note

# ═══════════════════════════════════════════════════════════════════════════════
#  CODE GENERATOR
# ═══════════════════════════════════════════════════════════════════════════════

class CodeGen:
    def __init__(self, prog: Program):
        self.prog      = prog
        self.code:     List[Any] = []
        self._lbl_n    = 0

        self.glob_addr: Dict[str, int] = {}   # global/static var → byte addr
        self._next_glob = GLOBAL_BASE

        # per-function state
        self.local_reg:  Dict[str, int] = {}  # local var → register
        self._epi_lbl:   Optional[str]  = None
        self._n_saves:   int            = 0

        # loop context stack: list of (break_lbl, continue_lbl)
        self._loop_stack: List[tuple] = []

    # ── label factory ────────────────────────────────────────────────────────

    def _lbl(self, hint='') -> str:
        self._lbl_n += 1
        return f'_L{self._lbl_n}_{hint}' if hint else f'_L{self._lbl_n}'

    # ── emit helpers ─────────────────────────────────────────────────────────

    def _emit(self, word: int, note=''):  self.code.append(WordI(word, note))
    def _lbl_emit(self, name: str):       self.code.append(LabelI(name))
    def _br(self, cond, lbl, note=''):    self.code.append(BranchI(cond, lbl, note))
    def _jmp(self, lbl, note=''):         self.code.append(JumpI(lbl, note))
    def _call(self, lbl, note=''):        self.code.append(CallI(lbl, note))

    def _load_imm(self, dst: int, val: int, note=''):
        """Load any 32-bit constant into dst (1 or 2 instructions)."""
        val &= 0xFFFFFFFF
        lo20 = val & 0xFFFFF
        if val == lo20:
            self._emit(enc_loadi(dst, lo20), note or f'r{dst}={val:#x}')
        else:
            hi20 = (val >> 12) & 0xFFFFF
            self._emit(enc_loadi(dst, lo20),  note or f'r{dst}[19:0]={lo20:#x}')
            self._emit(enc_loadih(dst, hi20), f'r{dst}={val:#010x}')

    def _scratch(self, *avoid: int) -> int:
        """Return first scratch register (R_T0/T1/T2) not in avoid set."""
        for r in (R_T0, R_T1, R_T2):
            if r not in avoid:
                return r
        raise RuntimeError("no scratch register available")

    # ── variable access ──────────────────────────────────────────────────────

    def _load_var(self, dst: int, name: str):
        if name in self.local_reg:
            if self.local_reg[name] != dst:
                self._emit(enc_move(dst, self.local_reg[name]), f'r{dst}={name}')
        elif name in self.glob_addr:
            self._emit(enc_loadabs(dst, self.glob_addr[name]), f'r{dst}=g:{name}')
        else:
            raise NameError(f"undefined variable '{name}'")

    def _store_var(self, name: str, src: int):
        if name in self.local_reg:
            if self.local_reg[name] != src:
                self._emit(enc_move(self.local_reg[name], src), f'{name}=r{src}')
        elif name in self.glob_addr:
            self._emit(enc_storeabs(src, self.glob_addr[name]), f'g:{name}=r{src}')
        else:
            raise NameError(f"undefined variable '{name}'")

    def _addr_of(self, dst: int, name: str):
        if name in self.glob_addr:
            self._load_imm(dst, self.glob_addr[name], f'&{name}')
        else:
            raise NameError(f"cannot take address of '{name}' (locals are in registers)")

    # ── array helpers ────────────────────────────────────────────────────────

    def _arr_base(self, name: str) -> int:
        if name in self.glob_addr:
            return self.glob_addr[name]
        raise NameError(f"undefined array '{name}'")

    def _gen_arr_addr(self, dst: int, base: int, idx):
        """Compute byte address of base[idx] into dst."""
        if isinstance(idx, Num):
            self._load_imm(dst, base + idx.val * 4)
        else:
            ir = self._scratch(dst)
            self._gen_expr(idx, ir)
            self._emit(enc_shiftl(ir, 2), 'idx*4')
            self._load_imm(dst, base)
            self._emit(enc_add(dst, ir), 'base+idx*4')

    def _gen_arr_load(self, dst: int, base: int, idx):
        """Load global array element arr[idx] into dst."""
        if isinstance(idx, Num):
            boff = idx.val * 4
            if boff < 256:
                self._load_imm(dst, base)
                self._emit(enc_load(dst, dst, boff), f'[{boff:#x}]')
            else:
                self._load_imm(dst, base + boff)
                self._emit(enc_load(dst, dst, 0))
        else:
            ir = self._scratch(dst)
            self._gen_expr(idx, ir)
            self._emit(enc_shiftl(ir, 2), 'idx*4')
            self._load_imm(dst, base)
            self._emit(enc_add(dst, ir), 'base+idx*4')
            self._emit(enc_load(dst, dst, 0), 'arr[idx]')

    def _gen_arr_store(self, base: int, idx, val_reg: int):
        """Store val_reg into global array element arr[idx]."""
        if isinstance(idx, Num):
            boff = idx.val * 4
            ir = self._scratch(val_reg)
            if boff < 256:
                self._load_imm(ir, base)
                self._emit(enc_store(ir, val_reg, boff))
            else:
                self._load_imm(ir, base + boff)
                self._emit(enc_store(ir, val_reg, 0))
        else:
            ar = self._scratch(val_reg)
            ir = self._scratch(val_reg, ar)
            self._gen_expr(idx, ir)
            self._emit(enc_shiftl(ir, 2), 'idx*4')
            self._load_imm(ar, base)
            self._emit(enc_add(ar, ir), 'base+idx*4')
            self._emit(enc_store(ar, val_reg, 0), 'arr[idx]=val')

    def _gen_ptr_load(self, dst: int, ptr_reg: int, idx):
        """Load *(ptr + idx*4) into dst."""
        if isinstance(idx, Num):
            boff = idx.val * 4
            if ptr_reg != dst:
                self._emit(enc_move(dst, ptr_reg))
            if boff < 256:
                self._emit(enc_load(dst, dst, boff), f'ptr[{idx.val}]')
            else:
                ir = self._scratch(dst)
                self._load_imm(ir, boff)
                self._emit(enc_add(dst, ir))
                self._emit(enc_load(dst, dst, 0))
        else:
            ir = self._scratch(dst)
            self._gen_expr(idx, ir)
            self._emit(enc_shiftl(ir, 2), 'idx*4')
            if ptr_reg != dst:
                self._emit(enc_move(dst, ptr_reg))
            self._emit(enc_add(dst, ir), 'ptr+idx*4')
            self._emit(enc_load(dst, dst, 0))

    # ── expression generation ────────────────────────────────────────────────

    def _gen_expr(self, node, dst: int) -> int:
        """Emit code placing the result of node into register dst. Returns dst."""

        if isinstance(node, Num):
            self._load_imm(dst, node.val)

        elif isinstance(node, Var):
            self._load_var(dst, node.name)

        elif isinstance(node, AddrOf):
            inner = node.expr
            if isinstance(inner, Var):
                self._addr_of(dst, inner.name)
            elif isinstance(inner, ArrIdx):
                self._gen_arr_addr(dst, self._arr_base(inner.name), inner.idx)
            else:
                raise NotImplementedError("& applied to unsupported expression")

        elif isinstance(node, Deref):
            self._gen_expr(node.expr, dst)
            self._emit(enc_load(dst, dst, 0), f'*r{dst}')

        elif isinstance(node, ArrIdx):
            name = node.name
            if name in self.glob_addr:
                self._gen_arr_load(dst, self.glob_addr[name], node.idx)
            elif name in self.local_reg:
                self._gen_ptr_load(dst, self.local_reg[name], node.idx)
            else:
                raise NameError(f"undefined '{name}'")

        elif isinstance(node, Call):
            self._gen_call(node, dst)

        elif isinstance(node, UnOp):
            self._gen_expr(node.expr, dst)
            if node.op == '-':
                self._emit(enc_neg(dst))
            elif node.op == '~':
                self._emit(enc_neg(dst))
                self._emit(enc_subi(dst, 1), '~x = -x-1')
            elif node.op == '!':
                t_lbl = self._lbl('nt'); d_lbl = self._lbl('nd')
                sc = self._scratch(dst)
                self._emit(enc_move(sc, dst))
                self._emit(enc_sub(sc, R_ZERO), 'test')
                self._br(COND_EQ, t_lbl)
                self._load_imm(dst, 0); self._jmp(d_lbl)
                self._lbl_emit(t_lbl); self._load_imm(dst, 1)
                self._lbl_emit(d_lbl)

        elif isinstance(node, PreInc):
            delta = Num(1) if node.op == '++' else Num(-1 & 0xFFFFFFFF)
            self._gen_assign(Assign(node.expr, BinOp('+', node.expr, delta)), dst)

        elif isinstance(node, PostInc):
            # evaluate current value into dst, then inc/dec the variable
            self._gen_expr(node.expr, dst)
            sc = self._scratch(dst)
            self._emit(enc_move(sc, dst))
            if node.op == '++':
                self._emit(enc_addi(sc, 1))
            else:
                self._emit(enc_subi(sc, 1))
            self._gen_store_target(node.expr, sc)

        elif isinstance(node, BinOp):
            self._gen_binop(node, dst)

        elif isinstance(node, Assign):
            self._gen_assign(node, dst)

        else:
            raise NotImplementedError(f"_gen_expr: {type(node).__name__}")

        return dst

    def _gen_store_target(self, target, src: int):
        """Store src into an lvalue target (used by post-increment)."""
        if isinstance(target, Var):
            self._store_var(target.name, src)
        elif isinstance(target, Deref):
            addr_r = self._scratch(src)
            self._gen_expr(target.expr, addr_r)
            self._emit(enc_store(addr_r, src, 0))
        elif isinstance(target, ArrIdx):
            name = target.name
            if name in self.glob_addr:
                self._gen_arr_store(self.glob_addr[name], target.idx, src)
            elif name in self.local_reg:
                ir = self._scratch(src)
                self._gen_expr(target.idx, ir)
                self._emit(enc_shiftl(ir, 2))
                ar = self._scratch(src, ir)
                self._emit(enc_move(ar, self.local_reg[name]))
                self._emit(enc_add(ar, ir))
                self._emit(enc_store(ar, src, 0))
            else:
                raise NameError(f"undefined '{name}'")
        else:
            raise NotImplementedError(f"store to {type(target).__name__}")

    def _gen_binop(self, node: BinOp, dst: int):
        op = node.op

        # ── short-circuit logical ─────────────────────────────────────────
        if op == '&&':
            f_lbl = self._lbl('andf'); d_lbl = self._lbl('andd')
            sc = self._scratch(dst)
            self._gen_expr(node.left, dst)
            self._emit(enc_move(sc, dst)); self._emit(enc_sub(sc, R_ZERO))
            self._br(COND_EQ, f_lbl)
            self._gen_expr(node.right, dst)
            self._emit(enc_move(sc, dst)); self._emit(enc_sub(sc, R_ZERO))
            self._br(COND_EQ, f_lbl)
            self._load_imm(dst, 1); self._jmp(d_lbl)
            self._lbl_emit(f_lbl); self._load_imm(dst, 0)
            self._lbl_emit(d_lbl); return

        if op == '||':
            t_lbl = self._lbl('ort'); d_lbl = self._lbl('ord')
            sc = self._scratch(dst)
            self._gen_expr(node.left, dst)
            self._emit(enc_move(sc, dst)); self._emit(enc_sub(sc, R_ZERO))
            self._br(COND_NE, t_lbl)
            self._gen_expr(node.right, dst)
            self._emit(enc_move(sc, dst)); self._emit(enc_sub(sc, R_ZERO))
            self._br(COND_NE, t_lbl)
            self._load_imm(dst, 0); self._jmp(d_lbl)
            self._lbl_emit(t_lbl); self._load_imm(dst, 1)
            self._lbl_emit(d_lbl); return

        # ── shift by constant ─────────────────────────────────────────────
        if isinstance(node.right, Num) and op in ('<<', '>>'):
            n = node.right.val & 31
            self._gen_expr(node.left, dst)
            self._emit((enc_shiftl if op == '<<' else enc_shiftar)(dst, n))
            return

        # ── immediate ALU ─────────────────────────────────────────────────
        if isinstance(node.right, Num) and op in ('+','-','*','&','|'):
            v = node.right.val & 0xFFFFFFFF
            if v > 0x7FFFFFFF: v -= 0x100000000
            self._gen_expr(node.left, dst)
            if op == '+' and  0 <= v <=  1023: self._emit(enc_addi(dst,  v)); return
            if op == '+' and -1023 <= v < 0:   self._emit(enc_subi(dst, -v)); return
            if op == '-' and  0 <= v <=  1023: self._emit(enc_subi(dst,  v)); return
            if op == '-' and -1023 <= v < 0:   self._emit(enc_addi(dst, -v)); return
            if op == '*' and  0 <= v <=  1023: self._emit(enc_muli(dst,  v)); return
            if op == '&' and  0 <= v <=  1023: self._emit(enc_andi(dst,  v)); return
            if op == '|' and  0 <= v <=  1023: self._emit(enc_ori (dst,  v)); return
            # fall through to general form

        # ── general two-register form ─────────────────────────────────────
        # If right sub-expression is complex (not a Num/Var), we must protect
        # the left value in dst by saving it to the software stack first.
        sc = self._scratch(dst)

        def _simple(n): return isinstance(n, (Num, Var))

        if not _simple(node.right):
            self._gen_expr(node.left, dst)
            self._emit(enc_subi(R_SP, 4),       'push')
            self._emit(enc_store(R_SP, dst, 0), 'save L')
            self._gen_expr(node.right, sc)
            self._emit(enc_load(dst, R_SP, 0),  'restore L')
            self._emit(enc_addi(R_SP, 4),       'pop')
        else:
            self._gen_expr(node.left,  dst)
            self._gen_expr(node.right, sc)

        reg_ops = {'+': enc_add, '-': enc_sub, '*': enc_mul,
                   '&': enc_and, '|': enc_or,  '^': enc_xor,
                   '<<': enc_shiftl_r, '>>': enc_shiftar_r}
        if op in reg_ops:
            self._emit(reg_ops[op](dst, sc)); return

        if op in _CMP_FALSE:
            # boolean materialise: result = (L cmp R) ? 1 : 0
            fc = _CMP_FALSE[op]
            tc = INV_COND[fc]
            csc = self._scratch(dst, sc)
            self._emit(enc_move(csc, dst))
            self._emit(enc_sub(csc, sc), f'cmp {op}')
            t_lbl = self._lbl('ct'); d_lbl = self._lbl('cd')
            self._br(tc, t_lbl)
            self._load_imm(dst, 0); self._jmp(d_lbl)
            self._lbl_emit(t_lbl); self._load_imm(dst, 1)
            self._lbl_emit(d_lbl); return

        raise NotImplementedError(f"binop '{op}'")

    def _gen_assign(self, node: Assign, dst: int):
        target = node.target

        if isinstance(target, Var):
            self._gen_expr(node.val, dst)
            self._store_var(target.name, dst)

        elif isinstance(target, Deref):
            self._gen_expr(node.val, dst)
            addr_r = self._scratch(dst)
            self._gen_expr(target.expr, addr_r)
            self._emit(enc_store(addr_r, dst, 0), '*ptr=val')

        elif isinstance(target, ArrIdx):
            name = target.name
            self._gen_expr(node.val, R_T2)
            if name in self.glob_addr:
                self._gen_arr_store(self.glob_addr[name], target.idx, R_T2)
            elif name in self.local_reg:
                ptr_reg = self.local_reg[name]
                if isinstance(target.idx, Num) and target.idx.val * 4 < 256:
                    self._emit(enc_store(ptr_reg, R_T2, target.idx.val*4))
                else:
                    ir = self._scratch(R_T2)
                    self._gen_expr(target.idx, ir)
                    self._emit(enc_shiftl(ir, 2))
                    ar = self._scratch(R_T2, ir)
                    self._emit(enc_move(ar, ptr_reg))
                    self._emit(enc_add(ar, ir))
                    self._emit(enc_store(ar, R_T2, 0), 'ptr[idx]=val')
            else:
                raise NameError(f"undefined '{name}'")
            if dst != R_T2:
                self._emit(enc_move(dst, R_T2))
        else:
            raise NotImplementedError(f"assignment to {type(target).__name__}")

    # ── builtins ─────────────────────────────────────────────────────────────

    def _gen_call(self, node: Call, dst: int):
        name = node.name
        nargs = len(node.args)

        if name == '__stop':
            self._emit(enc_stop(), '__stop()'); return
        if name == '__finish_good':
            self._emit(enc_finish_good(), '__finish_good()'); return
        if name == '__finish_bad':
            self._emit(enc_finish_bad(), '__finish_bad()'); return
        if name == '__nop':
            if nargs != 1 or not isinstance(node.args[0], Num):
                raise ValueError('__nop(imm8) requires a literal constant')
            self._emit(enc_nop(node.args[0].val & 0xFF)); return
        if name == '__opcode':
            if nargs != 1 or not isinstance(node.args[0], Num):
                raise ValueError('__opcode(0xXXX) requires a literal constant')
            self._emit(node.args[0].val & 0xFFFFFFFF, '__opcode'); return
        if name == '__load':
            if nargs != 1: raise ValueError('__load(addr) takes 1 arg')
            self._gen_expr(node.args[0], dst)
            self._emit(enc_load(dst, dst, 0), '__load'); return
        if name == '__store':
            if nargs != 2: raise ValueError('__store(addr,val) takes 2 args')
            self._gen_expr(node.args[0], R_T0)
            self._gen_expr(node.args[1], R_T1)
            self._emit(enc_store(R_T0, R_T1, 0), '__store'); return
        if name == '__ext_load':
            if nargs != 1: raise ValueError('__ext_load(addr) takes 1 arg')
            self._gen_expr(node.args[0], dst)
            self._emit(enc_ext_load(dst, dst, 0), '__ext_load'); return
        if name == '__ext_store':
            if nargs != 2: raise ValueError('__ext_store(addr,val) takes 2 args')
            self._gen_expr(node.args[0], R_T0)
            self._gen_expr(node.args[1], R_T1)
            self._emit(enc_ext_store(R_T0, R_T1, 0), '__ext_store'); return
        if name == '__sleep':
            if nargs != 1: raise ValueError('__sleep(duration) takes 1 arg')
            self._gen_expr(node.args[0], R_T0)
            self._emit(enc_sleep(R_T0, 0), '__sleep'); return

        # regular function call
        if nargs > 6:
            raise ValueError(f"'{name}': max 6 arguments")
        for i, arg in enumerate(node.args):
            self._gen_expr(arg, R_ARG[i])
        self._call(name)
        if dst != R_RET:
            self._emit(enc_move(dst, R_RET), f'{name}()')

    # ── condition branch helper ───────────────────────────────────────────────

    def _gen_cond_false(self, cond, false_lbl: str):
        """Branch to false_lbl when cond is false (zero)."""
        if isinstance(cond, BinOp) and cond.op in _CMP_FALSE:
            br_cond = _CMP_FALSE[cond.op]
            self._gen_expr(cond.left,  R_T0)
            self._emit(enc_move(R_T2, R_T0))
            self._gen_expr(cond.right, R_T1)
            self._emit(enc_sub(R_T2, R_T1), f'cmp {cond.op}')
            self._br(br_cond, false_lbl)
        else:
            self._gen_expr(cond, R_T0)
            self._emit(enc_move(R_T2, R_T0))
            self._emit(enc_sub(R_T2, R_ZERO), 'test!=0')
            self._br(COND_EQ, false_lbl)

    # ── statements ───────────────────────────────────────────────────────────

    def _gen_stmt(self, stmt):
        if isinstance(stmt, list):
            for s in stmt: self._gen_stmt(s)
            return

        if isinstance(stmt, IfStmt):
            end_lbl  = self._lbl('endif')
            else_lbl = self._lbl('else') if stmt.els else end_lbl
            self._gen_cond_false(stmt.cond, else_lbl)
            for s in stmt.then: self._gen_stmt(s)
            if stmt.els:
                self._jmp(end_lbl)
                self._lbl_emit(else_lbl)
                for s in stmt.els: self._gen_stmt(s)
            self._lbl_emit(end_lbl)

        elif isinstance(stmt, WhileStmt):
            top = self._lbl('wtop'); ext = self._lbl('wend')
            self._loop_stack.append((ext, top))
            self._lbl_emit(top)
            self._gen_cond_false(stmt.cond, ext)
            for s in stmt.body: self._gen_stmt(s)
            self._jmp(top)
            self._lbl_emit(ext)
            self._loop_stack.pop()

        elif isinstance(stmt, DoWhileStmt):
            top = self._lbl('dtop'); cont = self._lbl('dcont'); ext = self._lbl('dend')
            self._loop_stack.append((ext, cont))
            self._lbl_emit(top)
            for s in stmt.body: self._gen_stmt(s)
            self._lbl_emit(cont)
            self._gen_cond_false(stmt.cond, ext)
            self._jmp(top)
            self._lbl_emit(ext)
            self._loop_stack.pop()

        elif isinstance(stmt, ForStmt):
            top = self._lbl('ftop'); cont = self._lbl('fcont'); ext = self._lbl('fend')
            if stmt.init: self._gen_stmt(stmt.init)
            self._loop_stack.append((ext, cont))
            self._lbl_emit(top)
            if stmt.cond: self._gen_cond_false(stmt.cond, ext)
            for s in stmt.body: self._gen_stmt(s)
            self._lbl_emit(cont)
            if stmt.step: self._gen_stmt(stmt.step)
            self._jmp(top)
            self._lbl_emit(ext)
            self._loop_stack.pop()

        elif isinstance(stmt, RetStmt):
            if stmt.expr is not None:
                self._gen_expr(stmt.expr, R_RET)
            else:
                self._load_imm(R_RET, 0)
            if self._n_saves > 0:
                self._jmp(self._epi_lbl, 'return')
            else:
                self._emit(enc_return(), 'RETURN')

        elif isinstance(stmt, BreakStmt):
            if not self._loop_stack:
                raise SyntaxError("'break' outside loop")
            self._jmp(self._loop_stack[-1][0], 'break')

        elif isinstance(stmt, ContinueStmt):
            if not self._loop_stack:
                raise SyntaxError("'continue' outside loop")
            self._jmp(self._loop_stack[-1][1], 'continue')

        else:
            # expression statement
            self._gen_expr(stmt, R_T0)

    # ── function ─────────────────────────────────────────────────────────────

    def _gen_function(self, fn: Function):
        n_params = len(fn.params)
        n_scalar = sum(1 for d in fn.decls if d.arr_size == 0)
        n_regs   = n_params + n_scalar
        if n_regs > len(R_LOC):
            raise ValueError(f"'{fn.name}': too many params+locals (max {len(R_LOC)})")

        # register assignments
        reg_map: Dict[str, int] = {}
        for i, p in enumerate(fn.params):
            reg_map[p] = R_LOC[i]

        loc_idx = n_params
        for decl in fn.decls:
            if decl.arr_size > 0:
                # local array → static allocation in global data area
                addr = self._next_glob
                self._next_glob += decl.arr_size * 4
                self.glob_addr[decl.name] = addr
            else:
                reg_map[decl.name] = R_LOC[loc_idx]
                loc_idx += 1

        epi = self._lbl(f'{fn.name}_epi')
        self._epi_lbl  = epi
        self._n_saves  = n_regs
        self.local_reg = reg_map

        self._lbl_emit(fn.name)

        # prologue: allocate frame, save callee-save registers
        if n_regs > 0:
            frame = n_regs * 4
            self._emit(enc_subi(R_SP, frame), f'frame {frame:#x}')
            for i in range(n_regs):
                self._emit(enc_store(R_SP, R_LOC[i], i*4), f'save r{R_LOC[i]}')
            for i in range(n_params):
                self._emit(enc_move(R_LOC[i], R_ARG[i]), f'{fn.params[i]}=arg{i}')

        # local variable initializers (order: declaration order, skipping params)
        loc_idx2 = n_params
        for decl in fn.decls:
            if decl.arr_size == 0 and decl.init is not None:
                self._gen_expr(decl.init, R_LOC[loc_idx2])
            if decl.arr_size == 0:
                loc_idx2 += 1

        # body
        for s in fn.body:
            self._gen_stmt(s)

        # implicit return 0
        self._load_imm(R_RET, 0, 'implicit return 0')

        # epilogue: restore registers, free frame, return
        self._lbl_emit(epi)
        if n_regs > 0:
            frame = n_regs * 4
            for i in range(n_regs):
                self._emit(enc_load(R_LOC[i], R_SP, i*4), f'restore r{R_LOC[i]}')
            self._emit(enc_addi(R_SP, frame), f'free {frame:#x}')
        self._emit(enc_return(), 'RETURN')

        self.local_reg = {}
        self._epi_lbl  = None
        self._n_saves  = 0

    # ── program entry ─────────────────────────────────────────────────────────

    def generate(self) -> List[Any]:
        # allocate globals
        for g in self.prog.globals:
            self.glob_addr[g.name] = self._next_glob
            self._next_glob += g.size * 4

        # startup stub: init zero-reg and SP, call main, STOP
        self._lbl_emit('__start')
        self._emit(enc_loadi(R_ZERO, 0),   'R27=0 (zero reg)')
        self._load_imm(R_SP, 0xFFFC,       'R31=SP')
        self._call('main')
        self._emit(enc_stop(), 'STOP')

        for fn in self.prog.funcs:
            self._gen_function(fn)

        return self.code

# ═══════════════════════════════════════════════════════════════════════════════
#  ASSEMBLER  (two-pass, branch relaxation)
# ═══════════════════════════════════════════════════════════════════════════════

def _item_words(item, long_set: Set[int]) -> int:
    if isinstance(item, LabelI):  return 0
    if isinstance(item, BranchI): return 2 if id(item) in long_set else 1
    return 1

def assemble(code: List[Any]) -> List[int]:
    long_set: Set[int] = set()

    for _ in range(12):
        # pass 1: label addresses
        labels: Dict[str, int] = {}
        pc = 0
        for item in code:
            if isinstance(item, LabelI):
                labels[item.name] = pc * 4
            else:
                pc += _item_words(item, long_set)

        # pass 2: check branch reach
        changed = False
        pc = 0
        for item in code:
            if isinstance(item, LabelI): continue
            if isinstance(item, BranchI):
                tgt = labels.get(item.lbl)
                if tgt is None: raise NameError(f"undefined label '{item.lbl}'")
                off = tgt - pc * 4
                if not (-256 <= off <= 255) and id(item) not in long_set:
                    long_set.add(id(item)); changed = True
            pc += _item_words(item, long_set)
        if not changed: break
    else:
        raise RuntimeError("branch relaxation did not converge")

    # final encoding pass
    labels = {}
    pc = 0
    for item in code:
        if isinstance(item, LabelI):
            labels[item.name] = pc * 4
        else:
            pc += _item_words(item, long_set)

    words: List[int] = []
    pc = 0
    for item in code:
        if isinstance(item, LabelI): continue

        if isinstance(item, WordI):
            words.append(item.word); pc += 1

        elif isinstance(item, BranchI):
            tgt = labels[item.lbl]
            if id(item) in long_set:
                words.append(enc_branch(INV_COND[item.cond], 8))   # skip 2 words (+8 bytes)
                words.append(enc_jump(tgt & 0xFFFF))
                pc += 2
            else:
                words.append(enc_branch(item.cond, tgt - pc*4))
                pc += 1

        elif isinstance(item, JumpI):
            tgt = labels.get(item.lbl)
            if tgt is None: raise NameError(f"undefined label '{item.lbl}'")
            words.append(enc_jump(tgt & 0xFFFF)); pc += 1

        elif isinstance(item, CallI):
            tgt = labels.get(item.lbl)
            if tgt is None: raise NameError(f"undefined label '{item.lbl}'")
            words.append(enc_call(tgt & 0xFFFF)); pc += 1

        else:
            raise AssertionError(f"unknown item type {type(item).__name__}")

    return words

# ═══════════════════════════════════════════════════════════════════════════════
#  LISTING  (human-readable .lst file)
# ═══════════════════════════════════════════════════════════════════════════════

def make_listing(code:      List[Any],
                 glob_addr: Dict[str, int],
                 prog:      Program) -> str:
    # recompute long-branch set for listing (mirrors assemble())
    long_set: Set[int] = set()
    for _ in range(12):
        labels: Dict[str, int] = {}; pc = 0
        for item in code:
            if isinstance(item, LabelI): labels[item.name] = pc * 4
            else: pc += _item_words(item, long_set)
        changed = False; pc = 0
        for item in code:
            if isinstance(item, LabelI): continue
            if isinstance(item, BranchI):
                tgt = labels.get(item.lbl, 0)
                if not (-256 <= tgt-pc*4 <= 255) and id(item) not in long_set:
                    long_set.add(id(item)); changed = True
            pc += _item_words(item, long_set)
        if not changed: break

    lines: List[str] = []

    # header: global data map
    if glob_addr:
        lines.append('; ┌─ Global / Static Data ──────────────────────────────┐')
        lines.append(f'; │ {"Name":<18}  {"Addr":>6}  {"Words":>5}  {"Type":<12} │')
        lines.append('; ├─────────────────────────────────────────────────────┤')
        for name, addr in glob_addr.items():
            size = next((g.size for g in prog.globals if g.name == name), 1)
            typ  = f'int[{size}]' if size > 1 else 'int'
            lines.append(f'; │ {name:<18}  0x{addr:04x}  {size:>5}  {typ:<12} │')
        lines.append('; └─────────────────────────────────────────────────────┘')
        lines.append('')

    # instruction listing
    pc = 0
    for item in code:
        if isinstance(item, LabelI):
            lines.append(f'\n{item.name}:')
            continue

        addr = pc * 4

        if isinstance(item, WordI):
            mnem = disasm(item.word)
            note = f'  ; {item.note}' if item.note else ''
            lines.append(f'  [{addr:06x}]  {item.word:08x}  {mnem:<30}{note}')
            pc += 1

        elif isinstance(item, BranchI):
            tgt = labels.get(item.lbl, 0)
            cn  = COND_NAME.get(item.cond, str(item.cond))
            if id(item) in long_set:
                inv = COND_NAME.get(INV_COND[item.cond], '')
                w0  = enc_branch(INV_COND[item.cond], 8)
                w1  = enc_jump(tgt & 0xFFFF)
                lines.append(f'  [{addr:06x}]  {w0:08x}  BRANCH.{inv} +8  ; long → {item.lbl}')
                lines.append(f'  [{addr+4:06x}]  {w1:08x}  JUMP 0x{tgt:04x}  ; → {item.lbl}')
                pc += 2
            else:
                off = tgt - addr
                w   = enc_branch(item.cond, off)
                lbl_info = f'{item.lbl}  (off {off:+d})'
                note = f'  ; {item.note}' if item.note else ''
                lines.append(f'  [{addr:06x}]  {w:08x}  BRANCH.{cn} {lbl_info}{note}')
                pc += 1

        elif isinstance(item, JumpI):
            tgt = labels.get(item.lbl, 0)
            w   = enc_jump(tgt & 0xFFFF)
            lines.append(f'  [{addr:06x}]  {w:08x}  JUMP 0x{tgt:04x}  → {item.lbl}')
            pc += 1

        elif isinstance(item, CallI):
            tgt = labels.get(item.lbl, 0)
            w   = enc_call(tgt & 0xFFFF)
            lines.append(f'  [{addr:06x}]  {w:08x}  CALL 0x{tgt:04x}  → {item.lbl}')
            pc += 1

    return '\n'.join(lines)

# ═══════════════════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def compile_file(src_path: str, out_base: Optional[str] = None):
    import pathlib
    src  = pathlib.Path(src_path).read_text()
    base = out_base or src_path.rsplit('.', 1)[0]

    tokens = lex(src)
    prog   = Parser(tokens).parse_program()
    cg     = CodeGen(prog)
    code   = cg.generate()
    words  = assemble(code)

    hex_path = base + '.hex'
    lst_path = base + '.lst'

    pathlib.Path(hex_path).write_text(''.join(f'{w:08x}\n' for w in words))
    pathlib.Path(lst_path).write_text(make_listing(code, cg.glob_addr, prog))

    print(f'hex     → {hex_path}  ({len(words)} words)')
    print(f'listing → {lst_path}')
    if cg.glob_addr:
        print('global/static data:')
        for name, addr in cg.glob_addr.items():
            size = next((g.size for g in prog.globals if g.name == name), 1)
            tag  = f'[{size}]' if size > 1 else ''
            print(f'  {name}{tag:<8}  @ {addr:#06x}')


def main():
    import argparse
    ap = argparse.ArgumentParser(
        description='riscx_cc2 — C compiler for simpleCPU (emits .hex + .lst)')
    ap.add_argument('src', help='C source file')
    ap.add_argument('-o',  metavar='BASE', default=None,
                    help='output base name  (default: strip .c extension)')
    args = ap.parse_args()
    try:
        compile_file(args.src, args.o)
    except (SyntaxError, NameError, ValueError, NotImplementedError) as e:
        print(f'error: {e}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
