# make module with instance of the module
import module_class
def help_main(Env):
    Mod = Env.Current
    New = module_class.module_class('wrap')
    Obj = New.add_inst(Mod.Module,Mod.Module)
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if module_class.is_external_dir(Dir):
            New.nets[Net] = Dir,Wid
            Obj.conns[Net] = Net

    File = open('wrap.v','w')
    New.dump_verilog(File)
    File.close()





