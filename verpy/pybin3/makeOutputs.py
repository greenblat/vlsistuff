


def help_main(Env):
    Mod = Env.Current
    Vfile = open('WIRES')
    All = Vfile.read()
    Wires = All.split()
    Vfile.close()

    for Wire in Wires:
        if Wire in Mod.nets:
            Dir,Wid = Mod.nets[Wire]
            New = 'oo_'+Wire
            Mod.nets[New] = 'output',Wid
            Mod.hard_assigns.append([New,Wire,'',''])
    Mod.Module = 'oo_'+Mod.Module
    File = open('%s.v' % Mod.Module,'w')
    Mod.dump_verilog(File)
    File.close()

