



import logs

def help_main(Env):
    Mod = Env.Current
    Types = {}
    for Inst in Mod.insts:
        Type = Mod.insts[Inst].Type
        if Type not in Types: Types[Type] = 0
        Types[Type] += 1
    List = []
    for Type in Types:
        Many = Types[Type]
        List.append((Many,Type))
    List.sort()
    Fout = open("%s.hier" % Mod.Module,"w")
    for Many,Type in List:
        Fout.write('%s ->  %s [label="%s"] ;\n' % (Mod.Module,Type,Many))
    Fout.close()




