
# in gatelevel or rtl, insert gated clock cells.
# not a trivial problem. 
# thinking about it.

from skywaterLib import cellLib

from scan_rtl import  scan_statements,is_edged_timing,get_sensitivity_list,compute1

def help_main(Env):
    Mod = Env.Current
    rtlLevelClocks(Mod)

def rtlLevelClocks(Mod):
    always_assigns(Mod)



def always_assigns(Mod):
    Alw = 1
    for Always in Mod.alwayses:
        if len(Always) in [2,3]:
            if is_edged_timing(Always[0]):
                Time = Always[0]
                scan_statements(Mod,Always[1],gatedclk,[],[])



def gatedclk(Current,Item,Params,Stack):
    print("ITEM",Item,'IFELSES', Stack)

def gateLevelClocks(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if isFlipFlop(Obj.Type):
            Dpin,Qpin,Cpin = flopPins(Obj.Type)        
            Dsig = Obj.conns[Dpin]
            Qsig = Obj.conns[Qpin]
            Csig = Obj.conns[Cpin]

def isFlipFlop(Type):
    if Type not in cellLib: return False
    desc = cellLib[Type]
    return desc.Job == 'flipflop'

def flopPins(Type):
    return



