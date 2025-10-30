
import os,sys,logs

Dict = {}
Values = {}
Pluses = {}
Follows = {}

def help_main(Env):
    Mod = Env.Current
    if '-state' not in sys.argv:
        logs.log_error('for coverage You need to have -state Bus param')
        return

    Ind = sys.argv.index('-state')
    Next = sys.argv[Ind+1]
    States = Next.split()
    for Prm in Mod.parameters:
        Dict[Prm] = evaluate(Dict,Mod.parameters[Prm])
    for Prm in Mod.localparams:
        Dict[Prm] = evaluate(Dict,Mod.localparams[Prm])
        
    for _,Body,_  in Mod.alwayses:
        scanDeep(Mod,Body,States,[])


    for State in Values:
        if State in Pluses:
            Set = Values[State]
            Foll = Follows[State]

            MinF = 99999999
            for Val in Foll:
                if type(Val[0]) is int:
                    MinF = min(MinF,Val[0])

            if (0,0) in Set:
                for ii in range(0,MinF):
                    Follows[State].append((ii,ii+1))
                    if (ii,ii) not in Set: Set.append((ii,ii))

    dump(Mod.Module,Values,Follows)


def dump(Module,Values,Follows):
    Fout = open('%s.map' % Module,'w')
    Fout.write('( module %s \n' % Module)
    Fout.write('    ( instance tb.dut.%s )\n' % Module )
    for State in Values:
        Fout.write('    ( statemachine %s ( bus %s )\n' % (State,State))
        Fout.write('        ( states\n')
        for (A,B) in Values[State]:
            Fout.write('            ( %s %s )\n' %(A,B))
        Fout.write('        )\n')
            
        Fout.write('        ( flows\n')
        for (A,B) in Follows[State]:
            Fout.write('            ( %s %s )\n' %(A,B))
        Fout.write('        )\n')
        Fout.write('    )\n')
            
    Fout.write(')\n')
    Fout.close()

def scanDeep(Mod,Body,States,Cond):
    if Body[0] == 'list':
        for Item in Body[1:]: scanDeep(Mod,Item,States,Cond)
        return
    if Body[0] == 'ifelse':
        scanDeep(Mod,Body[2],States,Cond+[Body[1]])
        scanDeep(Mod,Body[3],States,Cond+[('!',Body[1])])
        return
    if Body[0] == 'if':
        scanDeep(Mod,Body[2],States,Cond+[Body[1]])
        return
    if Body[0] == 'named_begin':
        scanDeep(Mod,Body[2],States,Cond)
        return
    if Body[0] == '<=':
        if (Body[1] in States):
            if isSimple(Body[2]):
                addStates(Mod,Body[1] ,Body[2],Cond)
            elif (Body[2][0] == 'question'):
                addStates(Mod,Body[1],Body[2][2],Cond)
                addStates(Mod,Body[1],Body[2][3],Cond)
            elif (Body[2][0] == '+'):
                Pluses[Body[1]] = True
            else:
                logs.log_error("BBB222 %s %s %s" % (Body[1],Body[2],Cond))
        return
    logs.log_error("BBB %s %s" % (Body,Cond))
        
        
def addStates(Mod,State ,Val,Cond):
    if State not in Values: Values[State] = []
    if State not in Follows: Follows[State] = []
    Prev = findPrev(State,Cond)
    if type(Val) is list:
        if Val[0] == 'question':
            addStates(Mod,State ,Val[2],Cond)
            addStates(Mod,State ,Val[3],Cond)
    elif Val in Dict:
        if (Val,Dict[Val]) not in Values[State]:
            Values[State].append((Val,Dict[Val]))
        if (Prev): Follows[State].append((Prev,Val))
    else:
        if (Val,Val) not in Values[State]:
            Values[State].append((Val,Val))
        if (Prev): Follows[State].append((Prev,Val))

def findPrev(State,Cond):
    for Item in Cond:
        if (Item[0] == '==') and (Item[1] == State):
            return Item[2]
    return False


def isSimple(Expr):
   if type(Expr) is str: return True
   if type(Expr) is int: return True
   if Expr[0] in ['bin','dig','hex']: return True

   return False

def evaluate(Dict,Expr):
    if type(Expr) is int: return Expr
    if Expr[0] == 'bin': return int(Expr[2],2)
    if Expr[0] == 'hex': return int(Expr[2],16)
    if Expr[0] == 'dig': return int(Expr[2],10)
    logs.log_error('evaluate failed on %s' % str(Expr))
    return 0
        



