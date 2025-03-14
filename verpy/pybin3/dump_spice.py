

import logs
import os
import sys


def help_main(Env):
    Fout = open("cadence.spice","w")
    Fout.write("* CDL netlist generated by IG\n")
    for Module in Env.Modules:
        Mod = Env.Modules[Module]
        dump_spice(Mod,Fout)
    dump_protos(Fout)
    Fout.close()

def dump_spice(Mod,Fout):
    dump_header(Mod,Fout)
    dump_instances(Mod,Fout)
    Fout.write('.ENDS\n')

PROTOTYPES = {}
def dump_instances(Mod,Fout):
    for Inst in Mod.insts:
        Conns = []
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            Sig = prspice(Sig)
            Conns.append((Pin,Sig))
        Conns.sort()
        Fout.write('X%s' % relax(Inst))
        for Pin,Sig in Conns:
            Fout.write(' %s' % Sig)
        Fout.write(' VDD GND / %s\n' % Obj.Type)
        PP = []
        for Pin,Sig in Conns:
            PP.append(Pin)
        PP.extend(['VDD','GND'])
        Proto = ' '.join(PP)
        PROTOTYPES[Obj.Type] = Proto

def dump_protos(Fout):
    Cells = list(PROTOTYPES.keys())
    Cells.sort()
    for Cell in Cells:
        Fout.write('* .SUBCKT %s %s\n' % (Cell,PROTOTYPES[Cell]))



def relax(Inst):
    if Inst[0] == '\\': Inst = Inst[1:]
    for Chr in '/.[]':
        Inst = Inst.replace(Chr,'_')
    return Inst
def prspice(Sig):
    if type(Sig) is str: return Sig
    if Sig[0] == 'subbit':
        return "%s<%02d>" % (Sig[1],Sig[2])
    print("ERROR %s" % str(Sig))
    return str(Sig)


def dump_header(Mod,Fout):
    Fout.write(".SUBCKT %s " % Mod.Module)
    Nets = []
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if external(Dir):
            if type(Wid) is int:
                Nets.append((Net,dirLetter(Dir)))
            else:
                Fr,To = Wid
                for Ind in range(Fr,To-1,-1):
                    Nets.append(('%s<%02d>' % (Net,Ind),dirLetter(Dir)))


    Nets.sort()
    for Net,_ in Nets:
        Fout.write(' %s' % (Net))
    Fout.write('VDD GND\n')
    Fout.write("*.PININFO ")
    for Net,Dir in Nets:
        Fout.write(' %s:%s' % (Net,Dir))
    Fout.write('VDD:I GND:I\n')
    
            
def external(Dir):
    if 'input' in Dir: return True
    if 'inout' in Dir: return True
    if 'output' in Dir: return True
    return False

def dirLetter(Dir):
    if 'input' in Dir: return "I"
    if 'inout' in Dir: return "B"
    if 'output' in Dir: return "O"

