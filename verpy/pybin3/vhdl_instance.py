



def help_main(Env):
    Mod = Env.Current
    Fout = open('%s.vhd' % Mod.Module,'w')
    Fout.write('-- generated by  vhdl_instance.py extension of pyver.py  Ilia greenblat@mac.com\n')
    Fout.write('-- intended to help with integration into VHDL envir\n')
    Fout.write('entity %s is\n' % Mod.Module)
    Fout.write('   port(\n')
    Inps,Outs = prepExternals(Mod)
    for Net,Wid in Inps:
        if Wid==0:
            Fout.write('        %s : in std_logic;\n' % Net)
        else:
            Fout.write('        %s : in std_logic_vector ( %s downto 0);\n' % (Net,Wid))
    Fout.write('-------------\n')
    for Net,Wid in Outs:
        if Wid==0:
            Fout.write('        %s : out std_logic;\n' % Net)
        else:
            Fout.write('        %s : out std_logic_vector ( %s downto 0);\n' % (Net,Wid))
    Fout.write('   );\n')
    Fout.write('end entity %s;\n' % Mod.Module)
    Fout.write('\n\n\n')

    Fout.write('component %s is\n' % Mod.Module)
    Fout.write('   port(\n')
    Inps,Outs = prepExternals(Mod)
    for Net,Wid in Inps:
        if Wid==0:
            Fout.write('        %s : in std_logic;\n' % Net)
        else:
            Fout.write('        %s : in std_logic_vector ( %s downto 0);\n' % (Net,Wid))
    Fout.write('-------------\n')
    for Net,Wid in Outs:
        if Wid==0:
            Fout.write('        %s : out std_logic;\n' % Net)
        else:
            Fout.write('        %s : out std_logic_vector ( %s downto 0);\n' % (Net,Wid))
    Fout.write('   );\n')
    Fout.write('end component;\n')
    Fout.write('\n\n\n')


    Fout.write('%s : %s port map(\n' % (Mod.Module,Mod.Module))
    for Net,Wid in Inps + Outs[:-1]:
        Fout.write('        %s => %s,\n' % (Net,Net))
    Fout.write('        %s => %s\n' % (Outs[-1][0],Outs[-1][0]))
    Fout.write(');\n')
    Fout.write('\n\n\n')









    Fout.close()


def prepExternals(Mod):
    Inps = []
    Outs = []
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if 'input' in Dir:
            if type(Wid) is tuple:
                Inps.append((Net,Wid[0]))
            else:
                Inps.append((Net,0))
        elif 'output' in Dir:
            if type(Wid) is tuple:
                Outs.append((Net,Wid[0]))
            else:
                Outs.append((Net,0))
    Inps.sort()
    Outs.sort()
    return Inps,Outs