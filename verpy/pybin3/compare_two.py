


def help_main(Env):
    Mod = Env.Current
    Orig = Mod.Module
    Mod.Module = 'dual_'+Mod.Module
    Mod.alwayses = []
    Mod.generates = []
    Mod.insts = {}
    Mod.hard_assigns = []

    Nets = list(Mod.nets.keys())
    for Net in Nets:
        Dir,Wid = Mod.nets[Net]
        if internalDir(Dir):
            Mod.nets.pop(Net)
    InstA = 'a_'+Orig
    InstB = 'b_'+Orig
    Mod.add_inst(InstA,InstA)
    Mod.add_inst(InstB,InstB)
    ObjA = Mod.insts[InstA]
    ObjB = Mod.insts[InstB]
    Nets = list(Mod.nets.keys())
    for Net in Nets:
        Dir,Wid = Mod.nets[Net]
        if 'output' in Dir:
            ObjA.conns[Net] = 'a_'+Net
            ObjB.conns[Net] = 'b_'+Net
            Mod.hard_assigns.append((Net,['==','a_'+Net,'b_'+Net],'',''))
            Mod.nets['a_'+Net] = 'wire',Wid
            Mod.nets['b_'+Net] = 'wire',Wid
        else:
            ObjA.conns[Net] = Net
            ObjB.conns[Net] = Net
    Fout = open('%s.v' % Mod.Module,'w')
    Mod.dump_verilog(Fout)
    Fout.close()


def internalDir(Dir):
    if 'input' in Dir: return False
    if 'inout' in Dir: return False
    if 'output' in Dir: return False
    return True

