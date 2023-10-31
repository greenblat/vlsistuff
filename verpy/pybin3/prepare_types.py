


def help_main(Env):
    Mod = Env.Current
    Types = []
    for Inst in Mod.insts:
        Type = Mod.insts[Inst].Type
        if Type not in Types: Types.append(Type)

    File = open('%s.types' % Mod.Module,'w')
    Types.sort()
    for Type in Types:
        File.write('DIR/%s.v  \\\n' % Type)
    File.close()
