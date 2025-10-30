

import module_class


def help_main(Env):
    Mod = Env.Current
    Mod.insts = {}
    Mod.hard_assigns = []
    Mod.alwayses = {}

    Org = Mod.add_inst('org_%s' % Mod.Module,'org_%s' % Mod.Module)
    Dup = Mod.add_inst('dup_%s' % Mod.Module,'dup_%s' % Mod.Module)

    Nets = list(Mod.nets.keys())
    for Net in  Nets:
        Dir,Wid = Mod.nets[Net]
        if 'output' in Dir:
            Org.conns[Net]=Net
            Dup.conns[Net]='dup_'+Net
            Mod.nets[Net] = 'output',Wid
            Mod.nets['dup_'+Net] = 'wire',Wid
            Mod.nets['diff_'+Net] = 'wire',0
            Hard = ('diff_'+Net,('!=','dup_'+Net,Net),'','')
            Mod.hard_assigns.append(Hard)
        elif 'input' in Dir:
            Org.conns[Net]=Net
            Dup.conns[Net]=Net
        else:
            Mod.nets.pop(Net)

    Fout = open('diff_'+Mod.Module+'.v','w')
    Mod.dump_verilog(Fout)
    Fout.close()

