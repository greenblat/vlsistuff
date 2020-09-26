#! /usr/bin/python

import os,sys
import logs
import db0
import traceback

from scan_rtl import  scan_statements,is_edged_timing,get_sensitivity_list,compute1
from extract_expr_nets import extract_sigs
from rtl_width import get_width,get_width2
from module_class import pexpr
from executes import try_and_load_module


def help_main(Env):
    if Env.Current==None:
        logs.log_err('no module to work on')
        return
    Inps,Outs=make_picture(Env.Current)
    make_schematic(Env.Current,Inps,Outs)
    
def make_schematic(Current,Inps,Outs):
    Fout = open('%s.zdraw'%Current.Module,'w')
    Fout.write('schematic %s\n'%Current.Module)
    for ind,Inp in enumerate(Inps):
        Fout.write('inst input %s xy=1.0,%.f\n'%(Inp,ind*2+1))
        Fout.write('param %s name %s xy=0.0,%.f\n'%(Inp,Inp,ind*2+1))
    for ind,Out in enumerate(Outs):
        Fout.write('inst output %s xy=30.0,%.f\n'%(Out,ind*2+1))
        Fout.write('param %s name %s xy=32.0,%.f\n'%(Out,Out,ind*2+1))
    WireInd=0
    Conns={}
    www = 0
    for ind,Inst in enumerate(Current.insts.keys()):
        Obj = Current.insts[Inst]
        Type = Obj.Type
        if Type in ['nmos','pmos']:
            Obj.conns['i']=Obj.conns['s']
            Obj.conns['o']=Obj.conns['d']
            for Pin in ['s','d','b']:
                Obj.conns.pop(Pin)
            if Type=='pmos':
                Fout.write('inst %s %s xy=10.0,%.f rot=r90\n'%(Type,Inst,ind*3+1))
            else:
                Fout.write('inst %s %s xy=10.0,%.f rot=fr270\n'%(Type,Inst,ind*3+1))
        elif Type in ['inv']:
            Obj.conns['i1']=Obj.conns['i']
            Obj.conns['o1']=Obj.conns['o']
            for Pin in ['i','o']:
                Obj.conns.pop(Pin)
            Fout.write('inst %s %s xy=10.0,%.f\n'%(Type,Inst,ind*3+1))
        else:
            Fout.write('inst %s %s xy=10.0,%.f\n'%(Type,Inst,ind*3+1))

        for Prm in Obj.params:
            Val = Obj.params[Prm]
            Fout.write('params %s %s %s xy=10.0,%.f\n'%(Inst,Prm,Val,ind*3+1))
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            if not Sig:
                pass
            elif Sig in Inps+Outs:
                Fout.write('wire www%d %s %s.%s\n'%(www,Sig,Inst,Pin))
                www += 1
            elif (Sig not in Conns):
                Conns[Sig]=[(Inst,Pin)]
            else:
                Conns[Sig].append((Inst,Pin))
    for Sig in Conns:
        List = Conns[Sig]
        if len(List)==2:
            (I0,P0)=List[0]
            (I1,P1)=List[1]
            Fout.write('wire wire%d %s.%s %s.%s\n'%(www,I0,P0,I1,P1))
            www += 1
        elif (len(List)>2):
            Fout.write('inst node %s xy=20.0,%d\n'%(Sig,www+10))
            for (I0,P0) in List:
                Fout.write('wire wire%d %s %s.%s \n'%(www,Sig,I0,P0))
                www += 1


    Fout.write('end\n')




def make_picture(Current):
    Inps=[]
    Outs=[]
    Mxin = 0
    Mxout = 0
    for Net in Current.nets:
        (Dir,Wid)=Current.nets[Net]
        if 'input' in Dir:
            Inps.append(Net)
            Mxin = max(Mxin,len(Net))
        if 'output' in Dir:
            Outs.append(Net)
            Mxout = max(Mxout,len(Net))
        if 'inout' in Dir:
            Outs.append(Net)
            Mxout = max(Mxout,len(Net))
    Inps.sort()
    Outs.sort()
    Fout = open('%s.zpic'%Current.Module,'w')
    Fout.write('picture %s\n'%Current.Module)
    Max = max(len(Inps),len(Outs))
    PinSpace=1.0
    H1 = Max*PinSpace + 1.0
    Mxl1 = Mxin+Mxout+1
    Mxl = max(Mxl1,len(Current.Module))
    W1 = max(3,Mxl/2.9)
    Fout.write('pic_aline list=0.5,0,0.5,%.1f,%.1f,%.1f,%.1f,0,0.5,0\n'%(H1,W1,H1,W1))
    Off = (H1-(len(Inps)-1)*PinSpace)/2
    for ind,Name in enumerate(Inps):
        Fout.write('pic_line list=0,%.1f,0.5,0\n'%(Off+ind*PinSpace))
        Fout.write('pic_pin %s i xy=0,%.1f\n'%(Name,Off+ind*PinSpace))
        Fout.write('pic_text %s xy=0.6,%.1f\n'%(Name,Off+ind*PinSpace))
        
#    Off = 0.5 + (Max-len(Outs))/2.0
    Off = (H1-(len(Outs)-1)*PinSpace)/2
    for ind,Name in enumerate(Outs):
        Fout.write('pic_line list=%.1f,%.1f,0.5,0\n'%(W1,Off+ind*1))
        Fout.write('pic_pin %s i xy=%.1f,%.1f\n'%(Name,W1+0.5,Off+ind*1))
        Fout.write('pic_text %s xy=%.1f,%.1f align=right\n'%(Name,W1,Off+ind*1))
    Fout.write('pic_text %s xy=%.1f,%.1f\n'%(Current.Module,0.5,H1+0.2))
    Fout.write('end\n')
    Fout.close()
    return Inps,Outs


