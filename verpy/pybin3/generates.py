'''
    explicit build of generate statements in verilog
    loop unrolling, if, ifelse, assigns and instances
'''
import logs
import module_class as mdcl
def help_main(Env):
    Mod = Env.Current
    Mod.Genvars = {}
    for Gen in Mod.generates:
        gen_execute(Gen,Mod)
    Mod.generates = []

def evalx(Expr,Mod):
    Gen = mdcl.pr_expr(cleanList(Expr))
    return eval(Gen,Mod.parameters,Mod.Genvars)


def gen_execute(Gen,Mod):
    if Gen[0] == 'for':
        Gen[1] = mdcl.pr_expr(cleanList(Gen[1]))
        Gen[2] = mdcl.pr_expr(cleanList(Gen[2]))
        Gen[3] = mdcl.pr_expr(cleanList(Gen[3]))
        Gen[4] = cleanList(Gen[4])
        exec(Gen[1],Mod.parameters,Mod.Genvars)
        while evalx(Gen[2],Mod):
            gen_execute(Gen[4],Mod)
            exec(Gen[3],None,Mod.Genvars)
    elif Gen[0] == 'list':
        for Item in Gen[1:]:
            gen_execute(Item,Mod)
    elif Gen[0] == 'ifelse':
        if evalx(Gen[1],Mod):
            gen_execute(Gen[2],Mod)
        else:
            gen_execute(Gen[3],Mod)
    elif Gen[0] == 'if':
        if evalx(Gen[1],Mod):
            gen_execute(Gen[2],Mod)
    elif Gen[0] == 'assigns':
        LL = Gen[1]
        if LL[0] == 'list':
            for Ass in LL[1:]:
                do_assign(Ass,Mod)
    elif Gen[0] == 'instance':
        do_instance(Gen[1:],Mod)
    else:
        logs.log_error('GEN EXECUTE got %d %s' % (len(Gen),str(Gen)))


def cleanList(Item):
    if type(Item) is list:
        if (len(Item)==2) and (Item[0] == 'list'):
            Ret = cleanList(Item[1])
            return Ret
    return Item            

def do_instance(Code,Mod):
    Type = Code[0]
    Inst = Code[1]
    Run = 0
    while Inst+'_'+str(Run) in Mod.insts:
        Run += 1
    Inst = Inst+'_'+str(Run)
    Mod.add_inst(Type,Inst)
    Obj = Mod.insts[Inst]
    Obj.params = Code[2]
    for Pin,Sig in Code[3]:
        Sig2 = cleanGenVars(Sig,Mod)
        Obj.conns[Pin] = Sig2

def do_assign(Code,Mod):
    Dst = Code[1]
    Src = Code[2]
    Dst2 = cleanGenVars(Dst,Mod)
    Src2 = cleanGenVars(Src,Mod)
    Mod.hard_assigns.append((Dst2,Src2,'',''))


def cleanGenVars(Expr,Mod):
    if type(Expr) is str:
        if Expr in Mod.Genvars:
            return Mod.Genvars[Expr]
        return Expr
    if type(Expr) is list:
        Res = []
        for Item in Expr:
            Item2 = cleanGenVars(Item,Mod)
            Res.append(Item2)
        return Res 

    if type(Expr) is tuple:
        Lexpr = list(Expr)
        Res = cleanGenVars(Lexpr,Mod)
        return tuple(Res)

    return Expr


