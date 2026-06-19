# simpleCPU — User Guide

> Covers the simpleCPU hardware architecture and the `riscx_cc2.py` C compiler.

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Memory Map](#2-memory-map)
3. [Register File](#3-register-file)
4. [Hardware Call Stack](#4-hardware-call-stack)
5. [Flags and Conditions](#5-flags-and-conditions)
6. [Instruction Set Reference](#6-instruction-set-reference)
7. [Instruction Encoding Summary](#7-instruction-encoding-summary)
8. [CPU Signals and Reset](#8-cpu-signals-and-reset)
9. [The C Compiler — riscx_cc2.py](#9-the-c-compiler--riscx_cc2py)
10. [Supported C Subset](#10-supported-c-subset)
11. [Compiler ABI](#11-compiler-abi)
12. [Built-in Functions](#12-built-in-functions)
13. [Listing File Format](#13-listing-file-format)
14. [Complete Example](#14-complete-example)
15. [Known Limitations](#15-known-limitations)

---

## 1. Architecture Overview

simpleCPU is a 32-bit RISC processor with:

| Property | Value |
|---|---|
| Data width | 32 bits |
| Registers | 32 general-purpose registers (R0–R31) |
| Program counter | 16-bit, word-aligned (byte address) |
| Program space | 0x0000 – 0x7FFC (32 KB) |
| Data space | 0x8000 – 0xFFFC (32 KB) |
| Hardware call stack | 5 entries (16-bit return addresses) |
| Instruction size | 32 bits (fixed) |
| Memory interface | word-addressed, one transaction per instruction |

The CPU is synchronous (rising-edge clock), with active-low reset `rst_n`. An external `mem_ready` handshake stalls the pipeline if memory is slow.

---

## 2. Memory Map

All addresses are **byte addresses**; all accesses are **32-bit word-aligned**.

```
0x0000 ──────────────────────
         Program code
         (max 8192 words / 32 KB)
0x7FFC ──────────────────────
0x8000 ──────────────────────
         Global & static data
         (scalars first, then arrays)
         Software stack grows DOWN
         from 0xFFFC
0xFFFC ──────────────────────
```

The compiler places:
- Globals/statics starting at **0x8000**, allocated in declaration order.
- The software stack pointer (R31) initialised to **0xFFFC**, growing downward.

---

## 3. Register File

| Register(s) | Name | Role |
|---|---|---|
| R0 | `ret` | Function return value |
| R1 – R6 | `arg0`–`arg5` | Function arguments (caller-saved) |
| R7 – R26 | `loc0`–`loc19` | Local variables (callee-saved, max 20 per function) |
| R27 | `zero` | Always 0 — written once at startup, never again |
| R28 – R30 | `t0`–`t2` | Scratch / temporaries (caller-saved) |
| R31 | `sp` | Software stack pointer, init `0xFFFC` |

**Callee-save convention**: any function that uses R7–R26 saves them on the software stack in the prologue and restores them in the epilogue.

---

## 4. Hardware Call Stack

CALL pushes `PC+4` onto a 5-entry hardware stack and jumps to the target. RETURN pops the top entry back into PC.

```
Maximum call nesting depth: 5 levels
(startup → fn1 → fn2 → fn3 → fn4 → fn5)
```

> **Important:** Exceeding 5 nested CALLs silently corrupts the return address — the hardware does not detect overflow.

Recursive functions are not supported unless you manage return addresses in software.

---

## 5. Flags and Conditions

Flags are set by the **SUB** instruction (`dst − src`). No other instruction affects flags.

| Flag index | Condition | Meaning (after SUB dst, src) |
|---|---|---|
| 0 | `always` | Always true |
| 1 | `eq` | dst == src |
| 2 | `ne` | dst != src |
| 3 | `lt` | dst < src (signed) |
| 4 | `gt` | dst > src (signed) |
| 5 | `le` | dst <= src (signed) |
| 6 | `ge` | dst >= src (signed) |

BRANCH takes the branch when `flags[cond] == 1`.

### Condition implementation (RTL)

```verilog
flags[0] <= 1;
flags[1] <= (result == 0);
flags[2] <= (result != 0);
flags[3] <= result[31];                          // LT: negative
flags[4] <= (!result[31]) && (result != 0);      // GT: positive and nonzero
flags[5] <= result[31] || (result == 0);         // LE: negative or zero
flags[6] <= !result[31];                         // GE: non-negative
```

where `result = regf[dst] − regf[src]`.

---

## 6. Instruction Set Reference

### 6.1 Data Movement

| Mnemonic | Operation | Notes |
|---|---|---|
| `LOADI  dst, imm20` | `R[dst] = zero_ext(imm20)` | Loads bits [19:0] |
| `LOADIH dst, imm20` | `R[dst][31:12] = imm20` | Loads bits [31:12]; combine with LOADI for 32-bit constants |
| `MOVE   dst, src` | `R[dst] = R[src]` | |
| `NEG    dst` | `R[dst] = -R[dst]` | Two's complement negate |
| `LOADABS  dst, addr16` | `R[dst] = mem[addr16]` | Direct 16-bit absolute address |
| `STOREABS addr16, src` | `mem[addr16] = R[src]` | Direct 16-bit absolute address |

**Loading 32-bit constants** requires two instructions:
```
LOADI  dst, val[19:0]     ; bits 19..0
LOADIH dst, val[31:12]    ; bits 31..12  (overlapping bit 12 is OR'd in)
```

The compiler emits LOADI alone when `val ≤ 0xFFFFF`, or the LOADI+LOADIH pair for larger values.

### 6.2 Memory Access

| Mnemonic | Operation |
|---|---|
| `LOAD  dst, [src + off8]` | `R[dst] = mem[R[src] + off8*1]`  (off8 is byte offset) |
| `STORE [base + off8], src` | `mem[R[base] + off8*1] = R[src]` |
| `EXT_LOAD  dst, [src + off8]` | Same as LOAD but `ext_field=1` (external bus) |
| `EXT_STORE [base + off8], src` | Same as STORE but `ext_field=1` (external bus) |

`off8` is an unsigned 8-bit byte offset (range 0–255). For larger offsets compute the address in a register and use `off8=0`.

### 6.3 Arithmetic and Logic

| Mnemonic | Operation |
|---|---|
| `ADD  dst, src` | `R[dst] += R[src]` |
| `SUB  dst, src` | `R[dst] -= R[src]`  *(also sets flags)* |
| `MUL  dst, src` | `R[dst] *= R[src]` |
| `AND  dst, src` | `R[dst] &= R[src]` |
| `OR   dst, src` | `R[dst] \|= R[src]` |
| `XOR  dst, src` | `R[dst] ^= R[src]` |
| `ADDI dst, imm10` | `R[dst] += imm10` (unsigned 10-bit) |
| `SUBI dst, imm10` | `R[dst] -= imm10` (unsigned 10-bit) |
| `MULI dst, imm10` | `R[dst] *= imm10` |
| `ANDI dst, imm10` | `R[dst] &= imm10` |
| `ORI  dst, imm10` | `R[dst] \|= imm10` |

### 6.4 Shifts

| Mnemonic | Operation |
|---|---|
| `SHIFTL  dst, imm5` | `R[dst] <<= imm5` (logical) |
| `SHIFTR  dst, imm5` | `R[dst] >>= imm5` (logical) |
| `SHIFTAR dst, imm5` | `R[dst] >>= imm5` (arithmetic, sign-extended) |
| `SHIFTL_R  dst, src` | `R[dst] <<= R[src]` |
| `SHIFTR_R  dst, src` | `R[dst] >>= R[src]` (logical) |
| `SHIFTAR_R dst, src` | `R[dst] >>= R[src]` (arithmetic) |

### 6.5 Control Flow

| Mnemonic | Operation |
|---|---|
| `BRANCH.cond offset9` | If `flags[cond]`, `PC += sign_ext(offset9)` |
| `JUMP addr16` | `PC = addr16` (unconditional) |
| `CALL addr16` | Push `PC+4`; `PC = addr16` |
| `RETURN` | Pop stack → PC |

**Branch offset** is a **signed byte offset** from the branch instruction itself:
- Range: −256 to +255 bytes (−64 to +63 instructions).
- The compiler auto-expands out-of-range branches to a `BRANCH(inv)+8 / JUMP target` pair.

### 6.6 Special Instructions

| Mnemonic | Operation |
|---|---|
| `NOP imm8` | No operation; `imm8` visible on `nop_result` output |
| `STOP` | Assert `stop_code` output; CPU halts |
| `FINISH_GOOD` | Assert `finish_good` output |
| `FINISH_BAD` | Assert `finish_bad` output |
| `SLEEP reg` | Stall CPU for `R[reg]` cycles; asserts `sleeping` output |

---

## 7. Instruction Encoding Summary

All opcodes are 32 bits. Fields that matter for the compiler:

| Field | Bits | Description |
|---|---|---|
| `dst` | [4:0] | Destination / base register |
| `src` | [9:5] | Source register |
| `off8` | [17:10] | 8-bit byte offset (LOAD/STORE) |
| `imm5` | [9:5] | 5-bit immediate (shifts) |
| `imm9` | [11:3] | 9-bit signed branch offset |
| `imm10` | [14:5] | 10-bit immediate (ALU) |
| `imm16` | [15:0] | 16-bit address (CALL/JUMP) |
| `imm20` | [24:5] | 20-bit immediate (LOADI/LOADIH) |
| `cond` | [2:0] | Branch condition (0–6) |
| `ext` | [18] | External-bus flag (LOAD/STORE) |

### Base opcodes (new decoder)

```
STOP        0xfb8b3adf    RETURN      0xfb8b3adc
FINISH_GOOD 0xfb8b3ade    NOP         0xfb8b3b00 | imm8
FINISH_BAD  0xfb8b3add    NEG         0xfb8b3ae0 | dst
MOVE        0xfb8b3c00    LOAD        0xfb980000
STORE       0xfb900000    EXT_LOAD    0xfb9c0000
EXT_STORE   0xfb940000    CALL        0xfb8f0000
JUMP        0xfb8e0000    BRANCH      0xfb8b7000
ADDI        0xfb8d8000    SUBI        0xfb8d0000
MULI        0xfb8c8000    ANDI        0xfb8c0000
ORI         0xfb8b8000    ADD         0xfb8b6800
SUB         0xfb8b6400    MUL         0xfb8b6c00
AND         0xfb8b6000    OR          0xfb8b5c00
XOR         0xfb8b5800    SHIFTL      0xfb8b4400
SHIFTR      0xfb8b4800    SHIFTAR     0xfb8b4000
SHIFTL_R    0xfb8b4c00    SHIFTR_R    0xfb8b5400
SHIFTAR_R   0xfb8b5000    LOADI       0xfe000000
LOADIH      0xfc000000    LOADABS     0xfbe00000
STOREABS    0xfbc00000    SLEEP       0xfba00000
```

---

## 8. CPU Signals and Reset

```
clk       — rising-edge clock
rst_n     — active-low synchronous reset
irq       — interrupt request (jumps to irq_addr)
irq_addr  — 16-bit interrupt vector
mem_rd    — memory read strobe
mem_wr    — memory write strobe
mem_fetch — instruction fetch strobe
mem_addr  — 32-bit memory address
mem_wdata — 32-bit write data
mem_rdata — 32-bit read data
mem_ready — stall when low
stop_code    — pulsed when STOP executes
finish_good  — pulsed when FINISH_GOOD executes
finish_bad   — pulsed when FINISH_BAD executes
sleeping     — high while SLEEP stall is active
external_access — high when LOAD/STORE has ext_field=1
nop_result   — imm8 field of last NOP
running      — high when not reset and not stopped
```

On reset (`rst_n=0`): PC←0, all registers clear, stack clears.

On reset release: execution begins at address **0x0000**. The compiler places a startup stub there that initialises R27=0, R31=0xFFFC, then calls `main`.

---

## 9. The C Compiler — riscx_cc2.py

### Installation

No installation needed. Requires Python 3.9+.

```bash
python3 riscx_cc2.py source.c          # output: source.hex + source.lst
python3 riscx_cc2.py source.c -o out   # output: out.hex + out.lst
```

### Output files

| File | Description |
|---|---|
| `.hex` | One opcode per line in hex — load with `$readmemh("file.hex", mem)` |
| `.lst` | Human-readable listing with addresses, hex opcodes, and mnemonics |

---

## 10. Supported C Subset

### Types

```c
int     // 32-bit signed integer — the only scalar type
int*    // 32-bit pointer (byte address)
```

No `char`, `short`, `long`, `float`, `double`, `struct`, or `typedef`.

### Declarations

```c
// Global scalars and arrays (file scope)
int g;
int arr[16];

// Local scalars with optional initialiser
int x;
int y = 42;
int z = foo() + 1;

// Local arrays — allocated in static data (not on stack)
int buf[8];

// Local pointer
int *p;
```

### Operators

| Category | Operators |
|---|---|
| Arithmetic | `+` `-` `*` |
| Bitwise | `&` `\|` `^` `~` |
| Shift | `<<` `>>` (right shift is arithmetic / sign-extending) |
| Comparison | `==` `!=` `<` `>` `<=` `>=` |
| Logical | `&&` `\|\|` `!` |
| Assignment | `=` `+=` `-=` `*=` `&=` `\|=` `^=` `<<=` `>>=` |
| Increment | `++x` `x++` `--x` `x--` |
| Address / deref | `&var` `*ptr` |
| Array index | `arr[i]` `ptr[i]` |

### Control Flow

```c
if (cond) { ... }
if (cond) { ... } else { ... }

while (cond) { ... }

do { ... } while (cond);

for (init; cond; step) { ... }

break;        // exit innermost loop
continue;     // jump to next iteration
return expr;
return;       // void function
```

### Functions

```c
// Up to 6 int/int* parameters, int or void return
int add(int a, int b) { return a + b; }
void init(int *buf, int n) { ... }
```

- Maximum 20 local scalar variables per function (uses R7–R26).
- Maximum call nesting: **5 levels** (hardware stack limit).
- Recursion is **not supported**.

---

## 11. Compiler ABI

### Register usage

| Register | Role | Saved by |
|---|---|---|
| R0 | Return value | — |
| R1–R6 | Arguments 0–5 | Caller |
| R7–R26 | Local variables | Callee |
| R27 | Zero (always 0) | — |
| R28–R30 | Scratch temporaries | Caller |
| R31 | Stack pointer (0xFFFC, grows ↓) | — |

### Function call sequence

```
Caller:           evaluate args into R1–R6
                  CALL target
                  (result in R0 after return)

Callee prologue:  SUBI R31, frame_size       ; allocate frame
                  STORE [R31+0], R7           ; save used locals
                  STORE [R31+4], R8
                  ...
                  MOVE R7, R1                 ; copy arg0 → local reg
                  MOVE R8, R2                 ; copy arg1 → local reg

Callee epilogue:  LOAD R7, [R31+0]            ; restore locals
                  LOAD R8, [R31+4]
                  ...
                  ADDI R31, frame_size        ; free frame
                  RETURN
```

### Global variable access

Globals and local arrays are accessed via `LOADABS`/`STOREABS` using their fixed byte address. The compiler prints the address table to stdout and includes it in the listing header.

### Software stack

R31 is used as a downward-growing stack for:
1. Saving/restoring callee-save registers (R7–R26) in function prologues/epilogues.
2. Temporarily spilling values when evaluating complex nested expressions (e.g., `a * (b + c * d)`).

---

## 12. Built-in Functions

These require no declaration and map directly to single instructions.

| Built-in | Emitted instruction | Notes |
|---|---|---|
| `__stop()` | `STOP` | Halts the CPU |
| `__finish_good()` | `FINISH_GOOD` | Signals successful completion |
| `__finish_bad()` | `FINISH_BAD` | Signals failure |
| `__nop(imm8)` | `NOP imm8` | `imm8` must be a **literal constant** |
| `__load(addr)` | `LOAD dst, [addr+0]` | Read word from data memory |
| `__store(addr, val)` | `STORE [addr], val` | Write word to data memory |
| `__ext_load(addr)` | `EXT_LOAD dst, [addr]` | Read from external bus |
| `__ext_store(addr, val)` | `EXT_STORE [addr], val` | Write to external bus |
| `__sleep(duration)` | `SLEEP R_T0` | Stall for `duration` cycles |
| `__opcode(0xXXXXXXXX)` | raw word | Emit literal opcode; arg must be a **literal constant** |

### Examples

```c
__stop();                        // halt
__finish_good();                 // signal TB pass
__nop(0x5A);                     // NOP with tag 0x5A on nop_result pin
__store(0x8100, 42);             // mem[0x8100] = 42
int v = __load(0x8100);          // v = mem[0x8100]
__ext_store(0xFF00, status);     // write to external peripheral
__sleep(1000);                   // wait 1000 cycles
__opcode(0xfb8b3adf);            // manually emit STOP
```

---

## 13. Listing File Format

The `.lst` file contains:

### Header — global data map

```
; ┌─ Global / Static Data ──────────────────────────────┐
; │ Name                  Addr  Words  Type         │
; ├─────────────────────────────────────────────────────┤
; │ result              0x8000      1  int          │
; │ data                0x8004      8  int[8]       │
; └─────────────────────────────────────────────────────┘
```

### Instruction listing

```
__start:
  [000000]  fe00001b  LOADI  r27, 0x0                 ; R27=0 (zero reg)
  [000004]  fe1fff9f  LOADI  r31, 0xfffc              ; R31=SP
  [000008]  fb8f0118  CALL 0x0118  → main
  [00000c]  fb8b3adf  STOP                            ; STOP

main:
  [000118]  fb8d011f  SUBI r31, 0x8                   ; frame 0x8
  ...
  [00019c]  fb8b7085  BRANCH.le _L13_else  (off +16)
  ...
```

Column format:

```
  [address]  opcode  mnemonic                         ; annotation
```

- **address** — byte address in hex
- **opcode** — 32-bit instruction word in hex
- **mnemonic** — decoded instruction
- **annotation** — compiler hint (variable name, operation)

---

## 14. Complete Example

### Source: `demo.c`

```c
/* simpleCPU demo — compute sum of squares */

int result;           /* global output variable */

int square(int x) {
    return x * x;
}

int sum_sq(int n) {
    int i;
    int acc = 0;
    for (i = 1; i <= n; i++) {
        acc += square(i);
    }
    return acc;
}

int main() {
    result = sum_sq(10);   /* 1+4+9+...+100 = 385 */
    __finish_good();
    return 0;
}
```

### Compile

```bash
python3 riscx_cc2.py demo.c
```

Output:
```
hex     → demo.hex  (N words)
listing → demo.lst
global/static data:
  result          @ 0x8000
```

### Load in simulation (Verilog)

```verilog
initial $readmemh("demo.hex", mem);
```

### Verify result

After `finish_good` fires, read address `0x8000` from memory — it should contain `385` (0x181).

---

## 15. Known Limitations

### Language

| Limitation | Workaround |
|---|---|
| No `char`, `short`, `float` | Use `int` everywhere |
| No `struct` or `union` | Use parallel arrays |
| No `typedef` | — |
| No multi-dimensional arrays | Use `arr[row * COLS + col]` |
| Local arrays are static (not on stack) | Name collisions across calls: avoid recursive use |
| Max 20 locals per function | Split large functions |
| Max 6 function arguments | Pack extra args into a global struct workaround |
| No `sizeof`, no casting syntax | — |
| Right shift `>>` is **arithmetic** (sign-extending) | Use `& 0x7FFFFFFF` after shift if unsigned needed |
| No string literals | — |

### Hardware

| Limitation | Detail |
|---|---|
| Max call depth: 5 | Hardware stack has 5 entries |
| No recursion | Hardware stack does not detect overflow |
| No interrupts in compiled code | IRQ jumps to `irq_addr` bypassing the ABI |
| Branch range ±255 bytes | Compiler auto-expands; no programmer action needed |
| SLEEP `imm15` must be 0 | Compiler always uses `imm=0`; full duration in register |

### Compiler

| Limitation | Detail |
|---|---|
| One source file | No multi-file compilation; use `cpreproc.py` for `#include`/`#define` |
| No optimiser | Every expression goes through scratch registers |
| No dead-code elimination | Implicit `return 0` at function end always emitted |
