

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
                logs.log_info("(%d) ONE %s %s" % (Cnt,Net,List))
                Cnt += 1
                Inst,Type,Pin = List[0]
                if Inst in Ones:
                    logs.log_info("REMOVE ONE %s %s" % (Net,List))
                    Mod.insts.pop(Inst)
            elif len(List) == 0:
                logs.log_info("ZERO CONNECT %s" % (Net))
        elif (Dir == 'wire') and (Net not in Mod.netTable):
            logs.log_info("ZERO NOCONNS %s" % (Net))
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
            In = Obj.conns['a']
            Out = Obj.conns['x']
            if In.startswith('net_'):
                List = Mod.netTable[In]
                if len(List) == 2:
                    logs.log_info(" (%d) TWO buf=%s in=%s out=%s  list=%s" % (Cnt,Inst,In,Out,List))   
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
            Ins = [Obj.Type,module_class.hashit(Obj.conns['a']),module_class.hashit(Obj.conns['b'])]
            Ins.sort()
            Ins = tuple(Ins)

            X = Obj.conns['x']

            if Ins not in Table2:
                Table2[Ins] = [(Inst,X)]
            else:
                Table2[Ins].append((Inst,X))
    Saves = 0
    for Key in Table2:
        List = Table2[Key]
        if len(List) > 1:
            print("KEY",Key,"LIST",Table2[Key])
            Saves += len(List)-1


def makeByBits(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Pins = list(Obj.conns.keys())
        for Pin in Pins:
            Expr = Obj.conns[Pin]
            if (type(Expr) is list) and (len(Expr) == 1): Expr = Expr[0]
            print("DBG: inst=%s type=%s pin=%s expr=%s" % (Inst,Obj.Type,Pin,Expr))
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

