

import os
from module_class import pr_wid

Path0 = 'tb.dut.canc_fdcl.xl_serial.canc_xl_errors'
Path1 = 'tb.dup.canc_fdcl.xl_serial.canc_xl_errors'

Path0 = 'tb.dut.canc_fdcl.xl_serial'
Path1 = 'tb.dup.canc_fdcl.xl_serial'

Outputs = False
Pref = 'er'
Pref = 'se'


def help_main(Env):
    Mod = Env.Current
    Mod.hard_assigns = []
    Mod.alwayses = []
    Mod.insts = {}
    Fout = open('sigs.inc','w')
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if ('input' in Dir) or ('sign_version' in Net):
            pass
        else:
            Wids = pr_wid(Wid)
            Fout.write('wire %s %s_a_%s  = %s.%s;\n' % (Wids,Pref,Net,Path0,Net))
            Fout.write('wire %s %s_b_%s  = %s.%s;\n' % (Wids,Pref,Net,Path1,Net))
            Fout.write('wire cmp_%s_%s  = %s_a_%s != %s_b_%s;\n' % (Pref,Net,Pref,Net,Pref,Net))
            
    Fout.close()            
