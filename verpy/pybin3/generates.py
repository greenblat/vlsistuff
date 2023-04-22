'''
    explicit build of generate statements in verilog
    loop unrolling, if, ifelse, assigns and instances
'''
import copy
import logs
import module_class as mdcl
def help_main(Env):
    Modules = list(Env.Modules.keys())
    for Module in Modules:
        Mod = Env.Modules[Module]
        Mod.OriginalName = Module
    round(Env,Modules,[])
    dump(Env)

def round(Env,Modules,Dones):
    for Module in Modules:
        if Module not in Dones:
            Mod = Env.Modules[Module]
            print("XXXXX",Module,Mod.OriginalName)
            Mod.Genvars = {}
            for Gen in Mod.generates:
                gen_execute(Gen,Mod,Env)
            Mod.generates = []
            Dones.append(Module)
    
    Now = list(Env.Modules.keys())
    Down = []
    for Module in Now:
        if Module not in Dones:
            Down.append(Module)
    print("DOWN",Down)
    if Down != []:
        round(Env,Down,Dones)

def dump(Env):
    Top = Env.Current
    File = open('%s.gen.v' % Top.Module,'w') 
    for Module in Env.Modules:
        if '__builtins__' in Env.Modules[Module].parameters:
            Env.Modules[Module].parameters.pop('__builtins__')
        print("MODULE params=%s" % Env.Modules[Module].parameters)
        Env.Modules[Module].dump_verilog(File)

    File.close()

def work_module(Mod):
    Mod.Genvars = {}
    for Gen in Mod.generates:
        gen_execute(Gen,Mod)
    Mod.generates = []



def evalx(Expr,Mod):
    Gen = mdcl.pr_expr(cleanList(Expr))
    return eval(Gen,Mod.parameters,Mod.Genvars)


def gen_execute(Gen,Mod,Env):
    if Gen[0] == 'genvar':
        Mod.Genvars[Gen[1]] = 0
    elif Gen[0] == 'named_begin':
        BlkName = Gen[1]
        gen_execute(Gen[2],Mod,Env)
    elif Gen[0] == 'for':
        Gen[1] = mdcl.pr_expr(cleanList(Gen[1]))
        Gen[2] = mdcl.pr_expr(cleanList(Gen[2]))
        Gen[3] = mdcl.pr_expr(cleanList(Gen[3]))
        Gen[4] = cleanList(Gen[4])
        exec(Gen[1],Mod.parameters,Mod.Genvars)
        while evalx(Gen[2],Mod):
            gen_execute(Gen[4],Mod,Env)
            exec(Gen[3],None,Mod.Genvars)
    elif Gen[0] == 'case':
        Key = Gen[1]
        List = Gen[2]
        for What, Stmnts in List:
            if evalx(What,Mod) == evalx(Key,Mod):
                gen_execute(Stmnts,Mod,Sons)



    elif Gen[0] == 'list':
        for Item in Gen[1:]:
            gen_execute(Item,Mod,Env)
    elif Gen[0] == 'ifelse':
        if evalx(Gen[1],Mod):
            gen_execute(Gen[2],Mod,Env)
        else:
            gen_execute(Gen[3],Mod,Env)
    elif Gen[0] == 'if':
        if evalx(Gen[1],Mod):
            gen_execute(Gen[2],Mod,Env)
    elif Gen[0] == 'assigns':
        LL = Gen[1]
        if LL[0] == 'list':
            for Ass in LL[1:]:
                do_assign(Ass,Mod)
    elif Gen[0] == 'instance':
        do_instance(Gen[1:],Mod,Env)
    elif type(Gen[0]) is list:
        for Item in Gen:
            gen_execute(Item,Mod,Env)
            
    else:
        logs.log_error('GEN EXECUTE got %d %s' % (len(Gen),str(Gen)))


def cleanList(Item):
    if type(Item) is list:
        if (len(Item)==2) and (Item[0] == 'list'):
            Ret = cleanList(Item[1])
            return Ret
    return Item            

def do_instance(Code,Mod,Env):
    Type = Code[0]
    Inst = Code[1]
    Run = 0
    while Inst+'_'+str(Run) in Mod.insts:
        Run += 1
    Inst = Inst+'_'+str(Run)
    InstParams = {}
    for (Prm,Val) in Code[2]:
        Valx = evalx(Val,Mod)
        InstParams[Prm] = Valx
    if Type == Mod.OriginalName:
        Ptype = paramType(Mod,Type,InstParams)
        if Ptype == Type:
            logs.log_error("recursive generate of %s must have parameters" % Type)
            return
        else:
            NewMod = copy.deepcopy(Mod)
            NewMod.Module = Ptype
            NewMod.OriginalName = Type
            for Prm in InstParams:
                NewMod.parameters[Prm] = InstParams[Prm]
            Env.Modules[Ptype] = NewMod
#            for Inst0 in NewMod.insts:
#                Type0 = NewMod.insts[Inst0]
#                if Type0 == Type:
                    
        
            

    if Type == Mod.Module:
        Ptype = paramType(Mod,Type,InstParams)
        Mod.add_inst(Ptype,Inst)
    else:
        Mod.add_inst(Type,Inst)

    Obj = Mod.insts[Inst]
    Obj.params = InstParams

    for Pin,Sig in Code[3]:
        Sig2 = cleanGenVars(Sig,Mod)
        Obj.conns[Pin] = Sig2



def paramType(Mod,Type,Params):
    Keys = list(Params.keys())
    Keys.sort()
    for Key in Keys:
        Val = Params[Key]
        Type += '_'+Key+str(Val)
    return Type


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


