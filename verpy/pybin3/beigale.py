



import module_class


def help_main(Env):
    Mod = Env.Current
    Mod.alwayses = []
    Mod.insts = {}
    Mod.generates = []
    Mod.hard_assigns = []
    Nets = list(Mod.nets.keys())
    for Net in Nets:
        Dir,_ = Mod.nets[Net]
        if ('input' not in Dir) and ('output' not in Dir) and('inout' not in Dir):
            Mod.nets.pop(Net)

    Fout = open('%s.empty'%Mod.Module,'w')
    Mod.dump_verilog(Fout)
    Fout.close()


