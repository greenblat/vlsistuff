



import logs
from module_class import hashit


def pr_expr(Net):
    if type(Net) is list:
        return '%s[%s]' % (Net[1],Net[2])
    return Net

def help_main(Env):
    Mod = Env.Current
    Mod.buildNetTable()
    Destinations = {}
    Distances = {}
    Sources = {}
    initial(Mod,Destinations,Distances,Sources)
    run_deep_all(Mod,Destinations,Distances)
    reportPaths(Mod,Distances,Sources)
def reportPaths(Mod,Distances,Sources):
    List = []
    for Net in Distances:
        Dist,From = Distances[Net]
        List.append((Dist,Net,From))

    List.sort()
    List.reverse()
    for Dist,Net,From in List:
        if Dist>0:
            if hashit(Net) in Sources:
                Inst,Type = Sources[hashit(Net)]
                logs.log_info('%6d %20s %20s %20s      %s' % (Dist,pr_expr(Net),Inst,Type,pr_expr(From)))


def run_deep_all(Mod,Destinations,Distances):
    Actives = list(Distances.keys())
    run_deep(Mod,Destinations,Distances,Actives)
    

def run_deep(Mod,Destinations,Distances,Actives):
    Down = []
    for Net in Actives:
        if hashit(Net) in Mod.netTable:
            Conns = Mod.netTable[hashit(Net)]
            Base,Q = Distances[hashit(Net)]
            Dist = 1+Base
            for Inst,Type,Pin in Conns:
                if isInpPin(Pin,Type):
                    Opin = outPin(Type)
                    if Opin:
                        Osig = Mod.insts[Inst].conns[Opin]
                        if hashit(Osig) in Distances:
                            Now,From = Distances[hashit(Osig)]
                        else:
                            Now = 0
                        if hashit(Osig) in Destinations:
                            if Dist > Now: Distances[hashit(Osig)] = Dist,Q
                        elif Dist > Now: 
                            Distances[hashit(Osig)] = Dist,Q
                            if Osig not in Down:
                                Down.append(Osig)
    if (Down!=[]):
        logs.log_info('Deeper %d' % len(Down))
        run_deep(Mod,Destinations,Distances,Down)
                                
                        

def outPin(Type):
    if isBasicType(Type): return 'Y'
    return False
    

def isInpPin(Pin,Type):
    if isBasicType(Type):
        return Pin != 'Y'
#    if 'DFF' in Type:
#        return Pin == 'D'
    return False

def isBasicType(Type):
    for Sub in 'AND NAND OR NOR XOR XNOR BUF INV'.split():
        if Type.startswith(Sub): return True
    return False

# netTable[Net].append((Inst,Type,Pin))


def initial(Mod,Destinations,Distances,Sources):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        if 'DFF' in Type:
            Q = Obj.conns['Q']
            Distances[hashit(Q)] = 0,Q
            D = Obj.conns['D']
            Destinations[hashit(D)] = True
            Sources[hashit(D)] = Inst,Type


