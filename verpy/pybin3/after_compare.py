
import logs


def help_main(Env):
    Mod = Env.Current
    Mod.buildNetTable()
    Many = len(list(Mod.insts.keys()))
    logs.log_ensure(Many==0,'%s %d' % (Mod.Module,Many))
    for Net in Mod.nets:
        Dir,_ = Mod.nets[Net]
        if 'output' in Dir:
            if Net in Mod.netTable:
                logs.log_info('%s : %s' % (Net,Mod.netTable[Net]))
            
