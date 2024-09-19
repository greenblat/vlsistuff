


def help_main(Env):
    Mod = Env.Current
    Module = Mod.Module
    Fout = open('io_signals.py','w')
    Fout.write('#module: %s\n' % (Module))
    Fout.write("CLK = 'clk'\n")
    Fout.write("BASE = 'tb.dut'\n")
    Fout.write("INS = '''\n")
    for Net in Mod.nets:
        Dir,_ = Mod.nets[Net]
        if ('input' in Dir):
            Fout.write('   %s\n' % (Net))
    Fout.write("'''.split()\n")

    Fout.write("OUS = '''\n")
    for Net in Mod.nets:
        Dir,_ = Mod.nets[Net]
        if ('output' in Dir):
            Fout.write('   %s\n' % (Net))
    Fout.write("'''.split()\n")
    Fout.write('\n\n\n')
    Fout.close()
        
