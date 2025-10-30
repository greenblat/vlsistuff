



def help_main(Env):
    Mod = Env.Current
    Mod.buildNetTable()
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if 'input' in Dir:
            travel(Net,Mod,[('input',Net)])
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == 'flipflop':
            for Pin in Obj.conns:
                if Pin[0] == 'q':
                    Net = Obj.conns[Pin]
                    travel(Net,Mod,[('qq',Pin,Net)])

def travel(Net,Mod,Sofar):
    if isOutput(Net,Mod):
        print("OUT %s %s" % (Net,Sofar))
        return
    if Net in Mod.netTable:
        List = Mod.netTable[Net]
        for (Inst,Type,Pin) in List:
            if Type in GATELEVEL:
                PL = GATELEVEL[Type]
                if isInputPin(Type,Pin):
                    if Type == 'flipflop':
                        print("QQIN %s %s" % (Net,Sofar+[('dd',Pin,Type,Inst)]))
                        return
                    else:
                        Obj = Mod.insts[Inst]    
                        for Px in Obj.conns:
                            if isOutputPin(Type,Px):
                                Out = Obj.conns[Px]
                                travel(Out,Mod,Sofar+[(Type,Px,Out)])

            elif (Type != 'input'):
                print("SONS",Type,Pin)

def isInputPin(Type,Pin):
    PL = GATELEVEL[Type]
    if Type == 'input': return False
    if Type == 'flipflop':
        return Pin[0] != 'q'
    return Pin[0] != 'x'
    
def isOutputPin(Type,Pin):
    PL = GATELEVEL[Type]
    if Type == 'flipflop':
        return Pin[0] == 'q'
    return Pin[0] == 'x'
    
def isOutput(Net,Mod):
    if Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        return 'output' in Dir
    return False

GATELEVEL = {}
GATELEVEL['bufx'] = [('a'),('x')]
GATELEVEL['inv'] = [('a'),('x')]
GATELEVEL['or2'] = [('a','b'),('x')]
GATELEVEL['or3'] = [('a','b','c'),('x')]
GATELEVEL['or4'] = [('a','b','c','d'),('x')]
GATELEVEL['and2'] = [('a','b'),('x')]
GATELEVEL['and3'] = [('a','b','c'),('x')]
GATELEVEL['and4'] = [('a','b','c','d'),('x')]
GATELEVEL['adder'] = [('a','b'),('x')]
GATELEVEL['multiplier'] = [('a','b'),('x')]
GATELEVEL['subtractor'] = [('a','b'),('x')]
GATELEVEL['mux2'] = [('a','b','sel'),('x')]
GATELEVEL['select'] = [('a','b','sel'),('x')]
GATELEVEL['select_bus'] = [('a','b','sel'),('x')]
GATELEVEL['select_bus_lit'] = [('a','sel'),('x')]
GATELEVEL['comparator'] = [('a','b'),('x')]
GATELEVEL['comparator_lit'] = [('a'),('x')]
GATELEVEL['flipflop'] = [('d','en'),('q'),('clk','rst_n')]


                    
