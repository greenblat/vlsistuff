
import logs
def help_main(Env):
    print('>>>>>',dir(Env))
    Mod = Env.Current
    Types = {}
    for Inst in Mod.insts.keys():
        Type =  Mod.insts[Inst].Type
        if Type not in Types: Types[Type] = 0
        Types[Type]  += 1
    LL = []
    for Type in Types.keys():
        LL.append((Types[Type],Type))

    LL.sort()
    LL.reverse()

    for Many,Type in LL:
        logs.log_info('        %6d     %s'%(Many,Type))

        
