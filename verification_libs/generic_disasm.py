#! /usr/bin/python
import os,sys,string
codings={}
codings["load"]=['1', '0', '1', '1', '0', '1', '1', '1', '1', 'loffset[5]', 'loffset[4]', 'loffset[3]', 'loffset[2]', 'loffset[1]', 'loffset[0]', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["and"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', '0', '0', '1', '1', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["compare"]=['1', '0', '1', '1', '0', '1', '0', '1', '1', 'condreg[5]', 'condreg[4]', 'condreg[3]', 'condreg[2]', 'condreg[1]', 'condreg[0]', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["jump_comp"]=['1', '0', '1', '1', '1', 'offset2[5]', 'offset2[4]', 'offset2[3]', 'offset2[2]', 'offset2[1]', 'offset2[0]', 'bit[3]', 'bit[2]', 'bit[1]', 'bit[0]', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'offset[4]', 'offset[3]', 'offset[2]', 'offset[1]', 'offset[0]']
codings["tofloat"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', '0', '0', '0', '0', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["sub_lit"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', '0', '1', '1', '1', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["mul_lit"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', '1', '0', '0', '1', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["jump"]=['1', '0', '1', '1', '0', '1', '0', '1', '0', 'pol', 'condreg[5]', 'condreg[4]', 'condreg[3]', 'condreg[2]', 'condreg[1]', 'condreg[0]', 'bit[3]', 'bit[2]', 'bit[1]', 'bit[0]', 'offset[11]', 'offset[10]', 'offset[9]', 'offset[8]', 'offset[7]', 'offset[6]', 'offset[5]', 'offset[4]', 'offset[3]', 'offset[2]', 'offset[1]', 'offset[0]']
codings["finish"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '0', '1', '1', '1', '0', '1', '1', '0', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0']
codings["sqsum"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', '0', '1', '1', '0', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["select"]=['1', '0', '1', '1', '0', '1', '1', '0', '1', 'condreg[5]', 'condreg[4]', 'condreg[3]', 'condreg[2]', 'condreg[1]', 'condreg[0]', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["add_lit"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', '1', '0', '0', '0', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["sub"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', '1', '0', '1', '1', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["min"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', '0', '1', '0', '0', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["neg"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '0', '1', '1', '1', '0', '1', '1', '0', '1', '1', '1', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["imm"]=['1', '1', 'sign', 'exp[7]', 'exp[6]', 'exp[5]', 'exp[4]', 'exp[3]', 'exp[2]', 'exp[1]', 'exp[0]', 'mant[15]', 'mant[14]', 'mant[13]', 'mant[12]', 'mant[11]', 'mant[10]', 'mant[9]', 'mant[8]', 'mant[7]', 'mant[6]', 'mant[5]', 'mant[4]', 'mant[3]', 'mant[2]', 'mant[1]', 'mant[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["sqrt"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '0', '1', '1', '1', '0', '1', '1', '1', '0', '0', '1', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["arctan"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '0', '1', '1', '1', '0', '1', '1', '1', '0', '1', '1', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["add"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', '1', '1', '0', '0', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["abs"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '0', '1', '1', '1', '0', '1', '1', '1', '0', '0', '0', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["mul"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', '1', '1', '0', '1', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["sin"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '0', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["store"]=['1', '0', '1', '1', '0', '1', '1', '1', '0', 'loffset[5]', 'loffset[4]', 'loffset[3]', 'loffset[2]', 'loffset[1]', 'loffset[0]', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["toint"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', '0', '0', '0', '1', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["arcsin"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '0', '1', '1', '1', '0', '1', '1', '1', '1', '0', '0', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["max"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', '0', '1', '0', '1', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["div_lit"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', '1', '0', '1', '0', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["nop"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '0', '1', '1', '1', '0', '1', '1', '0', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
codings["mod"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', '1', '1', '1', '0', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["distance"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '1', 'src2[4]', 'src2[3]', 'src2[2]', 'src2[1]', 'src2[0]', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["cos"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '0', '1', '1', '1', '0', '1', '1', '1', '1', '1', '0', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["round"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '0', '1', '1', '1', '1', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["normpi"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '0', '1', '1', '1', '0', '1', '1', '1', '0', '1', '0', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["arccos"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '0', '1', '1', '1', '0', '1', '1', '1', '1', '0', '1', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["selectbit"]=['1', '0', '1', '1', '0', '1', '1', '0', '0', 'condreg[5]', 'condreg[4]', 'condreg[3]', 'condreg[2]', 'condreg[1]', 'condreg[0]', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["div"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', '1', '1', '1', '1', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
codings["or"]=['1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1', '0', '0', '1', '0', 'src1[5]', 'src1[4]', 'src1[3]', 'src1[2]', 'src1[1]', 'src1[0]', 'src0[5]', 'src0[4]', 'src0[3]', 'src0[2]', 'src0[1]', 'src0[0]', 'dst[4]', 'dst[3]', 'dst[2]', 'dst[1]', 'dst[0]']
def disasm(Code):
    if ((Code & 0xff800000)==0xb7800000):
         return "load     %s"%(fields_extr(Code,codings["load"]))
    if ((Code & 0xfffe0000)==0xb4a60000):
         return "and      %s"%(fields_extr(Code,codings["and"]))
    if ((Code & 0xff800000)==0xb5800000):
         return "compare  %s"%(fields_extr(Code,codings["compare"]))
    if ((Code & 0xf8000000)==0xb8000000):
         return "jump_comp %s"%(fields_extr(Code,codings["jump_comp"]))
    if ((Code & 0xfffe0000)==0xb4a00000):
         return "tofloat  %s"%(fields_extr(Code,codings["tofloat"]))
    if ((Code & 0xfffe0000)==0xb4ae0000):
         return "sub_lit  %s"%(fields_extr(Code,codings["sub_lit"]))
    if ((Code & 0xfffe0000)==0xb4b20000):
         return "mul_lit  %s"%(fields_extr(Code,codings["mul_lit"]))
    if ((Code & 0xff800000)==0xb5000000):
         return "jump     %s"%(fields_extr(Code,codings["jump"]))
    if ((Code & 0xffffffff)==0xb49db7fe):
         return "finish   %s"%(fields_extr(Code,codings["finish"]))
    if ((Code & 0xfffe0000)==0xb4ac0000):
         return "sqsum    %s"%(fields_extr(Code,codings["sqsum"]))
    if ((Code & 0xff800000)==0xb6800000):
         return "select   %s"%(fields_extr(Code,codings["select"]))
    if ((Code & 0xfffe0000)==0xb4b00000):
         return "add_lit  %s"%(fields_extr(Code,codings["add_lit"]))
    if ((Code & 0xfffe0000)==0xb4b60000):
         return "sub      %s"%(fields_extr(Code,codings["sub"]))
    if ((Code & 0xfffe0000)==0xb4a80000):
         return "min      %s"%(fields_extr(Code,codings["min"]))
    if ((Code & 0xfffff800)==0xb49db800):
         return "neg      %s"%(fields_extr(Code,codings["neg"]))
    if ((Code & 0xc0000000)==0xc0000000):
         return "imm      %s"%(fields_extr(Code,codings["imm"]))
    if ((Code & 0xfffff800)==0xb49dc800):
         return "sqrt     %s"%(fields_extr(Code,codings["sqrt"]))
    if ((Code & 0xfffff800)==0xb49dd800):
         return "arctan   %s"%(fields_extr(Code,codings["arctan"]))
    if ((Code & 0xfffe0000)==0xb4b80000):
         return "add      %s"%(fields_extr(Code,codings["add"]))
    if ((Code & 0xfffff800)==0xb49dc000):
         return "abs      %s"%(fields_extr(Code,codings["abs"]))
    if ((Code & 0xfffe0000)==0xb4ba0000):
         return "mul      %s"%(fields_extr(Code,codings["mul"]))
    if ((Code & 0xfffff800)==0xb49df800):
         return "sin      %s"%(fields_extr(Code,codings["sin"]))
    if ((Code & 0xff800000)==0xb7000000):
         return "store    %s"%(fields_extr(Code,codings["store"]))
    if ((Code & 0xfffe0000)==0xb4a20000):
         return "toint    %s"%(fields_extr(Code,codings["toint"]))
    if ((Code & 0xfffff800)==0xb49de000):
         return "arcsin   %s"%(fields_extr(Code,codings["arcsin"]))
    if ((Code & 0xfffe0000)==0xb4aa0000):
         return "max      %s"%(fields_extr(Code,codings["max"]))
    if ((Code & 0xfffe0000)==0xb4b40000):
         return "div_lit  %s"%(fields_extr(Code,codings["div_lit"]))
    if ((Code & 0xffffffff)==0xb49db7ff):
         return "nop      %s"%(fields_extr(Code,codings["nop"]))
    if ((Code & 0xfffe0000)==0xb4bc0000):
         return "mod      %s"%(fields_extr(Code,codings["mod"]))
    if ((Code & 0xffc00000)==0xb4c00000):
         return "distance %s"%(fields_extr(Code,codings["distance"]))
    if ((Code & 0xfffff800)==0xb49df000):
         return "cos      %s"%(fields_extr(Code,codings["cos"]))
    if ((Code & 0xfffe0000)==0xb49e0000):
         return "round    %s"%(fields_extr(Code,codings["round"]))
    if ((Code & 0xfffff800)==0xb49dd000):
         return "normpi   %s"%(fields_extr(Code,codings["normpi"]))
    if ((Code & 0xfffff800)==0xb49de800):
         return "arccos   %s"%(fields_extr(Code,codings["arccos"]))
    if ((Code & 0xff800000)==0xb6000000):
         return "selectbit %s"%(fields_extr(Code,codings["selectbit"]))
    if ((Code & 0xfffe0000)==0xb4be0000):
         return "div      %s"%(fields_extr(Code,codings["div"]))
    if ((Code & 0xfffe0000)==0xb4a40000):
         return "or       %s"%(fields_extr(Code,codings["or"]))
    return "*%08x"%(Code)
OpcodeWidth = 32

def int2bin(Int,Len):
    if (Int==0):
        res= '0' 
        while (len(res)<Len):
            res = '0'+res
        return res 
    res = ''
    while (Int):
        if (Int&1):
            res = '1'+res 
        else:   
            res = '0'+res 
        Int=Int>>1
    while (len(res)<Len):
        res = '0'+res
    return res 


def fields_extr(Code,List):
    Fields={}
    Str = int2bin(Code,OpcodeWidth)
    L1 = list(Str)
    for i in range(OpcodeWidth):
        Tok = List[i]
        if (Tok[0] not in '01'):
            Bit = int(L1[i],2)
            if ('[' in Tok):
                ww = string.split(Tok,'[')
                Key = ww[0]
                Ind = int(ww[1][:-1])
                if Key not in Fields:
                    Fields[Key]=0
                Fields[Key] |= (Bit<<Ind)
            else:
                Fields[Tok]=Bit
    res=''
    for Key in Fields:
        res += ' %s=0x%x'%(Key,Fields[Key])

    return res 

def main():
    Fname = sys.argv[1]
    if len(sys.argv)>2:
        Foutname = sys.argv[2]
    else:
        Foutname = 'dis.listing'
    print 'i take rom file "%s"  as input file and produce "%s" as output'%(Fname,Foutname)
    load_rom(Fname)
    Fout=open(Foutname,'w')
    run_disasm(Fout)
    Fout.close()

def run_disasm(Fout):
    for Addr,Code in enumerate(Program):
        Txt2 = disasm(Code)
        Str = '0x%04x : %08x  %s\n'%(Addr,Code,Txt2)
        print Str,
        Fout.write(Str)

Program=[]
def load_rom(Fname):
    File = open(Fname)
    Addr=0
    while 1:
        line = File.readline()
        if (len(line)==0):
            return
        if "//" in line: line=line[:line.index("//")]
        wrds = string.split(line)
        for wrd in wrds:
            if (wrd[0]=='@'):
                Addr = int(wrd[1:],16)
            else:
                Data = int(wrd,16)
                while len(Program)<=Addr:
                    Program.append(0)
                Program[Addr]=Data
                Addr += 1

if __name__=='__main__':
    main()

