
import os,sys
def help_main(Env):
    for Module in Env.Modules:
        Mod = Env.Modules[Module]
        Mod.Module = 'dup_%s' % Module
        for Inst in Mod.insts:
            Obj = Mod.insts[Inst]
            Obj.Type = 'dup_%s' % Obj.Type
        if not os.path.exists('dups'):
            os.mkdir('dups')
        Fout = open('dups/dup_%s.v' % Module,'w')
        Mod.dump_verilog(Fout)
        Fout.close()





