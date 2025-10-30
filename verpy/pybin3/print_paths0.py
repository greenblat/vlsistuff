
import module_class
BASICS = 'flipflop or2 and2 inv comparator adder subtractor mux2 select select_bus select_bus_lit comparator_lit or3 or4 and3 and4 bufx'.split()

def help_main(Env):
    Mod = Env.Current
    bringAll(Mod,Env)
    markZeroes(Mod)

def markZeroes(Mod):
    for Inp in Mod.nets:
        Dir,Wid = Mod.nets[Inp]
        Wid0 = Mod.sig_width(Inp)
        if Dir == 'input':
            Bits = module_class.splitBits(Inp,Mod,Wid0)
            for Bit in Bits:
                recordDepth(Bit,0,('in',Bit))
    for Flop in Mod.insts:
        Obj = Mod.insts[Flop]
        if Obj.Type == 'flipflop':
            Q = Obj.conns['q']
            Wid0 = module_class.expr_width(Q,Mod)
            Bits = module_class.splitBits(Inp,Mod,Wid0)
            for Bit in Bits:
                recordDepth(Bit,0,('ff',Bit))
DEPTHS = {}
def recordDepth(Sig,Depth,Why):
    Sig = Mod.pr_expr(Sig)
    if (Sig,Why) not in DEPTHS:
        DEPTHS[(Sig,Why)] = Depth
    else:
        Was = DEPTHS[(Sig,Why)]
        if Was<Depth:
            DEPTHS[(Sig,Why)] = Depth
        
    


def bringAll(Mod,Env):
    for Inst in Mod.insts:
        Type = Mod.insts[Inst].Type
        if Type not in BASICS:
            try_and_load_module(Type,Env)
            if Type in Env.Modules:
                Son = Env.Modules[Type]
                bringAll(Son,Env)

