


import logs

def help_main(Env):
    Mod = Env.Current
    Mod.recompute_instance_wires(Env)
    File = open('%s.wired' % Mod.Module,'w')
    Mod.dump_verilog(File)
    File.close()
