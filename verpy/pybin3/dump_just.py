

from module_class import pr_wid

def help_main(Env):
    Mod = Env.Current
    Module = Mod.Module
    Fout = open('%s.inst' % Module,'w')
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if ('input' in Dir):
            Widi = pr_wid(Wid)
            Fout.write('wire %s %s;\n' % (Widi,Net))

    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if ('output' in Dir):
            Widi = pr_wid(Wid)
            Fout.write('wire %s %s;\n' % (Widi,Net))


    Fout.write('%s %s (\n' % (Module,Module))
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if ('input' in Dir) or ('output' in Dir):
            Fout.write('    ,.%s(%s)\n' % (Net,Net))
    Fout.write(');\n')
    Fout.close()
        
