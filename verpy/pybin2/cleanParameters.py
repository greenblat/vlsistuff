'''
cleanParameters computes all parameters and defines. and puts
final number there.


'''

import types,string


def help_main(Env):
    if Env.Current==None:
        logs.log_err('no module to work on')
        return
    Mod = Env.Current
    cleanParameters(Mod)
    Fout = open('%s.clnv'%Mod.Module,'w')
    Mod.dump_verilog(Fout)
    Fout.close()






def cleanParameters(Mod):
    cleanNetParameters(Mod)
    cleanInstParameters(Mod)


def cleanInstParameters(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        res = {}
        for Param in Obj.params:
            Expr= Obj.params[Param]
            Val = compute0(Mod,Expr)
            res[Param]=Val
        Obj.params = res            

        



def cleanNetParameters(Mod):
    for Net in Mod.nets:
        (Dir,Wid) = Mod.nets[Net]
        if type(Wid)==types.IntType:
            pass
        elif len(Wid)==2:
            Widh = compute0(Mod,Wid[0])
            Widl = compute0(Mod,Wid[1])
            Mod.nets[Net]=(Dir,[Widh,Widl])
        else:
            print 'cleanParameters bad width "%s"'%str(Wid)

def compute0(Mod,Wid):
    if type(Wid)==types.IntType: return Wid
    if type(Wid)==types.ListType:
        if len(Wid)==1:
            return compute0(Mod,Wid[0])
        if Wid[0] in ['-','*','+','/']:
            A = compute0(Mod,Wid[1])
            B = compute0(Mod,Wid[2])
            return  eval('%s%s%s'%(A,Wid[0],B))
        if Wid[0] in ['>']:
            A = compute0(Mod,Wid[1])
            B = compute0(Mod,Wid[2])
            return  int(eval('%s%s%s'%(A,Wid[0],B)))
            
        if Wid[0] == 'functioncall':
            if Wid[1]=='$clog2':
                Val = compute0(Mod,Wid[2][0])
                X = len(bin(Val))-2
                return X




    if type(Wid)==types.StringType:
        if Wid in Mod.parameters:
            return compute0(Mod,Mod.parameters[Wid])



    print 'bad wid = %s'%str(Wid)
    return 0

