
import logs
from module_class import support_set
def help_main(Env):
    Mod = Env.Current
    instances(Mod)
    connectivity(Mod)

def connectivity(Mod):
    buildConns(Mod)
    reportConns()

def reportConns():
    Nets = list(CONNS.keys())
    Nets.sort()
    for Net in Nets:
        logs.log_info('%30s : %s'%(Net,CONNS[Net]))


def buildConns(Mod):
    for Net in Mod.nets:
        Dir,_ = Mod.nets[Net]
        if 'input' in Dir:
            connect(Net,'input',Mod.Module,Mod.Module)
        if 'output' in Dir:
            connect(Net,'output',Mod.Module,Mod.Module)
        if 'inout' in Dir:
            connect(Net,'inout',Mod.Module,Mod.Module)
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        for Pin in Obj.conns:
            Con = Obj.conns[Pin]
            Sup = support_set(Con)
            for Net in Sup:
                connect(Net,Pin,Type,Inst)
CONNS = {}
def connect(Net,Pin,Type,Inst):
    if Net not in CONNS: CONNS[Net] = []
    CONNS[Net].append((Pin,Type,Inst))




def instances(Mod):
    Types = {}
    for Inst in Mod.insts.keys():
        Type =  Mod.insts[Inst].Type
        if Type not in Types: Types[Type] = 0
        Types[Type]  += 1
    LL = []
    for Type in Types.keys():
        LL.append((Types[Type],Type))

    LL.sort()
    LL.reverse()

    for Many,Type in LL:
        logs.log_info('        %6d     %s'%(Many,Type))

        
