
import logs
from module_class import support_set
def help_main(Env):
    Types = {}
    for Module in Env.Modules:
        Mod = Env.Modules[Module]
        logs.log_info('scan %s' % Module)
        gatherInstances(Mod,Types)
    reportInstances(Types)
#    connectivity(Mod)

def connectivity(Mod):
    buildConns(Mod)
    reportConns()

def reportConns():
    Nets = list(CONNS.keys())
    Nets.sort()
    for Net in Nets:
        if len(CONNS[Net]) > 10:
            logs.log_info('%5d %30s : %s'%(len(CONNS[Net]),Net,CONNS[Net][:10]))
        else:
            logs.log_info('%5d %30s : %s'%(len(CONNS[Net]),Net,CONNS[Net]))


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




def gatherInstances(Mod,Types):
    for Inst in Mod.insts.keys():
        Type =  Mod.insts[Inst].Type
        if Type not in Types: Types[Type] = 0
        Types[Type]  += 1

def reportInstances(Types):
    LL = []
    for Type in Types.keys():
        LL.append((Types[Type],Type))

    LL.sort()
    LL.reverse()
    Tot = 0
    Fout = open('mod.csv','w')
    for ind,(Many,Type) in enumerate(LL):
        Tot += Many
        logs.log_info('%5d        %6d  / %6d    %s'%(ind,Many,Tot,Type))
        Fout.write('%d,%d,%d,%s,,,\n'%(ind,Many,Tot,Type))
    Fout.close()
        
