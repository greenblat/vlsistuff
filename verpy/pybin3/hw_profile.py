
import logs

def help_main(Env):
    Mod = Env.Current
    profile(Mod)
    for Root in Env.Modules:
        if Root != Env.Current:
            Mod = Env.Modules[Root]
            profile(Mod)


def profile(Mod):
    Types = {}
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        if Type not in Types: Types[Type] = 0
        Types[Type] += 1
    LL = []
    for Type in Types:
        Num = Types[Type]
        LL.append((Num,Type))
    LL.sort()
    LL.reverse()
    logs.log_info('----------------------')
    logs.log_info('  %s  ' % Mod.Module)
    for Num,Type in LL:
        logs.log_info('%5d : %s' % (Num,Type))


