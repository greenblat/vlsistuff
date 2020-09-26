

import module_class
import matches
import logs

def help_main(Env):
    Mod = Env.Current
    splitAlwayses(Mod)
    Blobs = blobify(Mod)
    for Blb in Blobs:
        print(Blb)

def blobify(Mod):
    Blobs = []
    for (Dst,Src,_,_) in Mod.hard_assigns:
        Sups = module_class.support_set(Src)
        Supd = module_class.support_set(Dst)
        Blobs.append((Supd,Sups,Dst,Src))
    return Blobs
    
def splitAlwayses(Mod):
    for Cond,Body,Alw in Mod.alwayses:
        Error = 'splitAlwayses failed Cond on %s'%str(Cond)
        
        Var0 =  matches.matches(Cond,'edge posedge ?')
        if Var0:
            print('var0 %s'%str(Var0))
            Error = False
        Var1 =  matches.matches(Cond,['list', ['edge', 'posedge', '?'], ['edge', 'negedge', '?']])
        if Var1:
            print('var1 %s'%str(Var1))
            Error = False

        Var2 =  matches.matches(Cond,'*')
        if Var2:
            print('var2 %s'%str(Var2))
            Error = False

        if Error:
            logs.log_error('splitAlwayses failed Cond on %s'%str(Cond))
            return
            
        Pairs = {}
        scanAlways(Body,True,Pairs) 
        logs.log_info('pairs %s %s %s %s'%(Var0,Var1,Var2,Pairs))


def scanAlways(Body,Cond,Pairs):
    Var0 =  matches.matches(Body,'<= ? ?')
    if Var0: 
        Dst,Src = Var0
        if Dst not in Pairs:
            Pairs[Dst] = [(Cond,Src)]
        else:
            Pairs[Dst].append((Cond,Src))
        return
        
    Var0 =  matches.matches(Body,'= ? ?')
    if Var0: 
        Dst,Src = Var0
        if Dst not in Pairs:
            Pairs[Dst] = [(Cond,Src)]
        else:
            Pairs[Dst].append((Cond,Src))
        return 



    Var0 =  matches.matches(Body,[ 'list','?' ])
    if Var0: 
        scanAlways(Var0[0],Cond,Pairs)
        return
    
    Var0 =  matches.matches(Body,[ 'ifelse','?','?','?' ])
    if Var0:
        scanAlways(Var0[1],['&&',Var0[0],Cond],Pairs)
        scanAlways(Var0[2],['&&',['!',Var0[0]],Cond],Pairs)
        return

    Var0 =  matches.matches(Body,[ 'if','?','?' ])
    if Var0: 
        scanAlways(Var0[1],['&&',Var0[0],Cond],Pairs)
        return


    logs.log_error('scan failed %s'%(str(Body)))
    return False

    


