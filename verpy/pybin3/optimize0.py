

import module_class
import logs

def zeroDriveRound(Mod,Ones,Round):
    logs.log_info("ZERODRIVE %s ones=%d" % (Round,len(Ones)))
    Mod.buildNetTable()
    Cnt = 0
    RM = []
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if (Dir == 'wire') and (Net in Mod.netTable):
            List = Mod.netTable[Net]
            if len(List) == 1:
#                logs.log_info("(%s) %d ONE %s %s" % (Round,Cnt,Net,List))
                Cnt += 1
                Inst,Type,Pin = List[0]
                if Inst in Ones:
#                    logs.log_info("REMOVE %s ONE %s %s" % (Round,Net,List))
                    Mod.insts.pop(Inst)
            elif len(List) == 0:
                logs.log_info("ZERO %s CONNECT %s" % (Round,Net))
        elif (Dir == 'wire') and (Net not in Mod.netTable):
#            logs.log_info("ZERO %s NOCONNS %s" % (Round,Net))
            RM.append(Net)
    for Net in RM:
        Mod.nets.pop(Net)


def bufx_round(Mod,Round):
    logs.log_info("BUFX_ROUND %s" % Round)
    Mod.buildNetTable()
    Cnt = 0
    Ones = []
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == 'bufx':
            if 'a' in Obj.conns:
                In = Obj.conns['a']
                Out = Obj.conns['x']
                if In.startswith('net_'):
                    List = Mod.netTable[In]
                    if len(List) == 2:
#                        logs.log_info(" (%d) TWO buf=%s in=%s out=%s  list=%s" % (Cnt,Inst,In,Out,List))   
                        Cnt += 1
                        if List[0][0] != Inst:
                            DrvInst = List[0][0]
                            DrvPin  = List[0][2]
                        else:
                            DrvInst = List[1][0]
                            DrvPin  = List[1][2]
                        Drv = Mod.insts[DrvInst]
                        Drv.conns[DrvPin] = Out
                        Ones.append(Inst)        
    return Ones                


def optimize0(Mod):
    Table2 = {}
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type in ['and2','or2']:
            if 'b' in Obj.conns:
                Ins = [Obj.Type,module_class.hashit(Obj.conns['a']),module_class.hashit(Obj.conns['b'])]
                Ins.sort()
                Ins = tuple(Ins)
                if 'x' in Obj.conns: 
                    X = Obj.conns['x']
    
                    if Ins not in Table2:
                        Table2[Ins] = [(Inst,X)]
                    else:
                        Table2[Ins].append((Inst,X))
    Saves = 0
    for Key in Table2:
        List = Table2[Key]
        if len(List) > 1:
#            print("KEY",Key,"LIST",Table2[Key])
            Saves += len(List)-1


def makeByBits(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Pins = list(Obj.conns.keys())
        for Pin in Pins:
            Expr = Obj.conns[Pin]
            if (type(Expr) is list) and (len(Expr) == 1): Expr = Expr[0]
#            print("DBG: inst=%s type=%s pin=%s expr=%s" % (Inst,Obj.Type,Pin,Expr))
            if not Expr:
               print("EMPTY CONN %s %s inst=%s pin=%s" % (Mod.Module,Obj.Type,Inst,Pin)) 
               Bits = []
            else:
                Bits = module_class.splitBits(Expr,Mod,64)
                if Bits[0] == 'bus': Bits.pop(0)
            if len(Bits)>1:
                Obj.conns.pop(Pin)
                Bits.reverse()
                for ind,Bit in enumerate(Bits):
                    Bit = Bit.replace('[','_')
                    Bit = Bit.replace(']','_')
                    Obj.conns['%s_%d_' % (Pin,ind)] = Bit
            elif len(Bits) == 1:
                Bit = module_class.hashit(Expr)
#                print("EXPR",Expr,Bit)
                Bit = Bit.replace('[','_')
                Bit = Bit.replace(']','_')
                Obj.conns[Pin] = Bit

    Nets = list(Mod.nets.keys())
    for Net in Nets:
        Dir,Wid = Mod.nets[Net]
        Bits = module_class.splitBits(Net,Mod,64)
        if len(Bits)>1:
            for Bit in Bits:
                Bit = Bit.replace('[','_')
                Bit = Bit.replace(']','_')
                Mod.nets[Bit] = Dir,1
            Mod.nets.pop(Net)


def similarGatesRound(Mod,Round):
    SIGNATURES = {}
    Removed = 0
    bufxs = 0
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Signature = getSignature(Obj)
        if Signature:
            if Signature in SIGNATURES:
                SIGNATURES[Signature].append(Inst)
            else:
                SIGNATURES[Signature] = [Inst]
    print("SIGN %s out of %s " % (len(list(SIGNATURES.keys())),len(list(Mod.insts.keys()))))
    for Signature in SIGNATURES:
        List = SIGNATURES[Signature]
        if len(List)>1:
            LL = Signature.split()
            if LL[0] == 'inv':
                Removed += mergeSimilars(Mod,List,LL[0])
            elif LL[0].startswith('and') or LL[0].startswith('or') :
                Removed += mergeSimilars(Mod,List,LL[0])
            elif LL[0] == 'bufx':
                bufxs += 1
            else:
                logs.log_info('SIMILAR %s  %s : %s' % (Round,Signature,List))
    logs.log_info("REMOVED %s SIMILARS %d, left %d bufx" % (Round,Removed,bufxs))
    return Removed

def mergeSimilars(Mod,List,Type):
    Xs = []
    Givens = 0
    Best = False
    Ins = []
    Removed = 0
    for Inst in List:
        Obj = Mod.insts[Inst]
        X = Obj.conns['x']
        Xs.append(X)
        if not Best: Best = X
        if not X.startswith('net_'):
            Best = X
            Givens += 1
        for Pin in Obj.conns:
            if Pin != 'x':
                Ins.append(Obj.conns[Pin])
    if Givens == 0:
        if Type == 'inv': 
            Out = '%s_n' % Ins[0]
        else:
            Out = Best
    elif Givens == 1:
        Out = Best
    else:
        logs.log_warning("TWO GIVENS for %s %s" % (Type,List))
        return 0

    for II in List[1:]:
        Mod.insts.pop(II)
        Removed += 1
    Mod.insts[List[0]].conns['x'] = Out
    Mod.buildNetTable()
    for X in Xs:
        if (X in Mod.netTable):
            Clist = Mod.netTable[X]
            for (Instx,Typex,Pinx) in Clist:
                if (Pinx != 'x')and(Instx in Mod.insts):
                    Mod.insts[Instx].conns[Pinx] = Out

    return Removed


def typeIsBasic(Type):
    if Type.startswith('and'): return True
    if Type.startswith('or'): return True
    if Type.startswith('inv'): return True
    if Type.startswith('bufx'): return True
    return False

def getSignature(Obj):
    Type = Obj.Type
    if not typeIsBasic(Type): return False
    Ins = []
    for Pin in Obj.conns:
        if (Pin != 'x'): Ins.append(Obj.conns[Pin])
    Ins.sort()
    Sign = '%s %s' % (Type,' '.join(Ins))
    return Sign
