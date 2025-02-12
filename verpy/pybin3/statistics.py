
import sys,os
import logs
from module_class import support_set
try:
    import skywaterLib as libx
except:
    libx = False
print("LIBX",libx)
if not libx:
    try:
        import cellLibrary as libx
    except:
        libx = False
    
def getGateCount(Cell):
    return eval(libx.cellLib[Cell].properties['area'])

def help_main(Env):
    Types = {}
    for Module in Env.Modules:
        Mod = Env.Modules[Module]
        logs.log_info('scan %s' % Module)
        gatherInstances(Mod,Types)
    Lib = False
#    if '-celllibrary' in Env.params:
#        Lib = Env.params['-celllibrary'][0]
        
    if '-report' in Env.params:
        Dir = Env.params['-report'][0]
        if not os.path.exists(Dir):
            os.mkdir(Dir)
        Fout = open('%s/%s.insts' % (Dir,Module),'w')
        saveInstances(Module,Types,Fout)
        return
    OneGate = getGateCount('scs130ms_nand2_2')
    reportInstances(Types,Lib,OneGate)
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


def saveInstances(Module,Types,Fout):
    LL = []
    for Type in Types.keys():
        LL.append((Types[Type],Type))

    LL.sort()
    LL.reverse()
    for Num,Type in LL:
        Fout.write('%s %s %s\n' % (Module,Type,Num))
    Fout.close()


def gatherInstances(Mod,Types):
    for Inst in Mod.insts.keys():
        Type =  Mod.insts[Inst].Type
        if Type not in Types: Types[Type] = 0
        Types[Type]  += 1

def reportInstances(Types,Lib,OneGate):
    LL = []
    for Type in Types.keys():
        LL.append((Types[Type],Type))

    LL.sort()
    LL.reverse()
    Tot = 0
    TotArea = 0
    TotGates = 0
    Fout = open('mod.csv','w')
    Fout.write('index,many,tot,type,cell,totcell,totarea,gate,gates,totgates\n')
    for ind,(Many,Type) in enumerate(LL):
        Area = 0
        if libx:
            if Type in libx.cellLib:
                Area = eval(libx.cellLib[Type].properties['area'])
        Tot += Many
        Area0 = Many*Area
        TotArea += Area0
        logs.log_info('%5d        %6d  / %6d    %s'%(ind,Many,Tot,Type))
        Gate = Area / OneGate
        ThisGates = Gate * Many
        TotGates += ThisGates
        Fout.write('%d,%d,%d,%s,%.4f,%.3f,%.2f,%.2f,%.2f,%.2f,\n'%(ind,Many,Tot,Type,Area,Area0,TotArea,Gate,ThisGates,TotGates))
    Fout.close()
        
