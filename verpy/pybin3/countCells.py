

import logs
CELLS = {}
LEAFS = {}
SELFS = {}
KINDS = {}
def help_main(Env):
    Mod = Env.Current
    print("MODULE %s" % Mod.Module)
    countCells(Mod,Env)

    LL = []
    for Module in CELLS:
        if CELLS[Module]>1:
            LL.append((CELLS[Module],Module))

    LL.sort()
    LL.reverse()
    for Num,Module in LL:
        logs.log_info('%-70s = total=%6d  selfs=%6d  types=%6d' % (Module,Num,SELFS[Module],len(KINDS[Module])))

    report('',Mod.Module)

def report(Pref,Module):
    Num = CELLS[Module]
    logs.log_info('%s%-70s  %6d  %6d' % (Pref,Module,Num,SELFS[Module]))
    for Kind in KINDS[Module]:
        if Kind not in LEAFS:
            report(Pref+'       ',Kind)
    


def countCells(Mod,Env):
    Count = 0
    Leafs = 0
    Selfs = 0
    Kinds = []
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        if Type not in Kinds: Kinds.append(Type)
        if Type not in Env.Modules:
            CELLS[Type] = 1
            LEAFS[Type] = True
            Count += 1
            Selfs += 1
        elif (Type in LEAFS):
            Selfs += 1
            Count += 1
        else:
            countCells(Env.Modules[Type],Env)
            Count += CELLS[Type]
            if CELLS[Type]==1:
                LEAFS[Type] = True
                
        
    CELLS[Mod.Module] = Count
    SELFS[Mod.Module] = Selfs
    KINDS[Mod.Module] = Kinds


