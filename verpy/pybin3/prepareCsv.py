
# prepare csv lines of module for using integrator 

def help_main(Env):
    Line = ['module','net','dir','width','signame']
    Lines = [Line]
    Nets = {}
    for Module in Env.Modules:
        Mod = Env.Modules[Module]
        for Net in Mod.nets:
            Dir,Wid = Mod.nets[Net]
            if Net not in Nets:
                Nets[Net] = []
            Nets[Net].append( (Dir,Module) )
            if externalDir(Dir):
                Bits = Mod.sig_width(Net)
                Line = [Module,Net,externalDir(Dir),str(Bits),Net]
                Lines.append(Line)
    Fout = open('xcons.csv','w')
    for line in Lines:
        Str = ','.join(line)
        Fout.write('%s\n' % Str)
    Fout.close()


def externalDir(Dir):
    if 'input' in Dir: return 'i'
    if 'output' in Dir: return 'o'
    return False



