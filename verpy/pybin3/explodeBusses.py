
import logs
import module_class


def help_main(Env):
    print(Env)
    print(list(Env.Modules.keys()))
    print(Env.Current)
    Mod = Env.Current
    work(Mod,Env.Modules)

def work(Mod,Sons):
    if list(Mod.parameters.keys())!=[]: 
        logs.log_error("explodeBusses must not encounter parameters")
        return
    if list(Mod.localparams.keys())!=[]: 
        logs.log_error("explodeBusses must not encounter parameters")
        return
    if Mod.generates!=[]: 
        logs.log_error("explodeBusses must not encounter generates")
        return
    if Mod.alwayses!=[]: 
        logs.log_error("explodeBusses must not encounter always")
        return

    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        Pins = list(Obj.conns.keys())
        for Pin in Pins:
            Sig = Obj.conns[Pin]
            SigSeq = signalSequence(Sig,Mod)
            if Type in Sons:
                PinSeq = signalSequence(Pin,Sons[Type])
            else:
                Tmod = module_class.module_class(Type)
                PinSeq = signalSequence(['subbus',Pin,(0,len(SigSeq)-1)],Tmod)
            Obj.conns.pop(Pin)
            print(">>>>>",PinSeq,SigSeq)
            while (SigSeq!=[])and(PinSeq!=[]):
                Pin0 = PinSeq.pop(0)
                Sig0 = SigSeq.pop(0)
                Obj.conns[Pin0] = Sig0
        Nets = list(Mod.nets.keys()) 
        for Net in Nets:
            Dir,Wid = Mod.nets[Net]
            SigSeq = signalSequence(Net,Mod)
            if len(SigSeq)>1:
                Mod.nets.pop(Net)
                for Sig in SigSeq:
                    Mod.nets[Sig] = Dir,0
        Pos = 0
        Len = len(Mod.hard_assigns)
        while Pos<Len:
            Dst,Src,AA,BB = Mod.hard_assigns[Pos]
            DstSeq = signalSequence(Dst,Mod)
            SrcSeq = signalSequence(Src,Mod)
            if (DstSeq)>1:
                Mod.hard_assigns.pop(Pos)
                for ind,DD in enumerate(DstSeq):
                    if len(SrcSeq)>ind:
                        Sr = SrcSeq[ind]
                    else:
                        Sr = 0
                    Mod.hard_assigns.append((DD,Sr,AA,BB))
            else:
                Pos += 1

def signalSequence(Sig,Mod):
    LL = bitByBit(Sig,Mod)
    print('XXXX',Sig,LL)
    for ind,Sig in enumerate(LL):
        if '[' in Sig:
            Sig = Sig.replace('[','_')
            Sig = Sig.replace(']','_')
            LL[ind] = Sig
    return LL


def bitByBit(Sig,Mod):
    if type(Sig) is str: 
        LL = explodeBus(Mod,Sig, "xx")
        LL0 = removePins(LL)
        return LL0
    elif type(Sig) is list:
        if Sig[0] == 'subbit':
            LL = explodeBus(Mod,Sig, "xx")
            LL0 = removePins(LL)
            return LL0
        elif Sig[0] == 'subbus':
            Bus = Sig[1]
            Ind = Sig[2]
            LL = explodeBus(Mod,Sig, "xx")
            LL0 = removePins(LL)
            return LL0
        elif Sig[0] == 'curly':
            LL = explodeBus(Mod,Sig, "xx")
            LL0 = removePins(LL)
            return LL0
        elif Sig[0] == 'sub_slicebit':
            Bus = Sig[1]
            _,Wid = Mod.nets[Bus]
            if len(Wid) == 4:
                Lo3,Hi3 = Wid[3]
                Res = []
                for II in range(Lo3,Hi3+1):
                    Now = "%s[%s][%s][%s]" % (Bus,Sig[2],Sig[3],II)
                    Res.append(Now)
                return Res
            else:
                logs.log_error('ILIASUB error wid=%s %s' % (Wid,Sig))
                return [Sig]

        else:
            logs.log_error('ILIA0 error %s' % str(Sig))

    logs.log_error('ILIA1 error %s' % str(Sig))
    return [Sig]

def removePins(List):
    Res = [] 
    for A,_ in List:
        Res.append(A)
    return Res


def explodeBus(Mod, Net, Pin):
    if not Net:
        return []
    elif type(Net) is str:
        if Net in Mod.nets:
            _, Wid = Mod.nets[Net]
            if Wid == 0:
                return [(Net, Pin)]
            elif type(Wid) is tuple:
                if len(Wid) == 2:
                    Low, High = Wid
                    return explodeBus(Mod,["subbus", Net, Low, High], Pin)
                if Wid[0] == "double":
                    Wid0 = Wid[1]
                    Wid1 = Wid[2]
                    Res = []
                    pinind = 0
                    for KK in range(Wid0[0],Wid0[1]):
                        for LL in range(Wid1[0],Wid1[1]):
                            Res.append( ("%s[%s][%s]" % (Net,KK,LL),"%s[%s]" % (Pin,pinind)))
                            pinind += 1
                    return Res
                if (Wid[0] == "packed")and(len(Wid)==3):
                    Wid0 = Wid[1]
                    Wid1 = Wid[2]
                    Res = []
                    pinind = 0
                    for KK in range(Wid0[0],Wid0[1]):
                        for LL in range(Wid1[0],Wid1[1]):
                            Res.append( ("%s[%s][%s]" % (Net,KK,LL),"%s[%s]" % (Pin,pinind)))
                            pinind += 1
                    return Res
                if (Wid[0] == "packed")and(len(Wid)==4):
                    Wid0 = Wid[1]
                    Wid1 = Wid[2]
                    Wid2 = Wid[3]
                    Res = []
                    pinind = 0
                    for KK in range(Wid0[0],Wid0[1]):
                        for LL in range(Wid1[0],Wid1[1]):
                            for JJ in range(Wid2[0],Wid2[1]):
                                Res.append( ("%s[%s][%s][%s]" % (Net,KK,LL,JJ),"%s[%s]" % (Pin,pinind)))
                                pinind += 1
                    return Res
                logs.log_error("explodeBus of net %s met strange width %s" % (Net,str(Wid)))

        return [(Net, Pin)]
    elif (type(Net) is list) and (Net[0] == "subbit"):
        _, Wid = Mod.nets[Net[1]]
        if Wid[0] in ['packed','double']:
            Wid1 = Wid[2]
            Res = []
            pinind = 0
            for LL in range(Wid1[0],Wid1[1]+1):
                Res.append( ("%s[%s][%s]" % (Net[1],Net[2],LL),"%s[%s]" % (Pin,pinind)))
                pinind += 1
            return Res

        return [(Net, Pin)]
    elif (type(Net) is list) and (Net[0] == "subbus"):
        Bus = Net[1]
        if len(Net) == 3:
            Lo, Hi = Net[2]
        else:
            Lo, Hi = Net[2], Net[3]
        Hi = eval(module_class.pr_expr(Hi),Mod.parameters)
        Lo = eval(module_class.pr_expr(Lo),Mod.parameters)
        Res = []
        run = 0
        for ind in range(Lo, Hi + 1):
            Res.append((f"{Bus}[{ind}]", f"{Pin}[{run}]"))
            run += 1
        return Res
    elif (type(Net) is list) and (Net[0] == "sub_slicebit"):
        Bus = Net[1]
        Ind0 = eval(module_class.pr_expr(Net[2]),Mod.parameters)
        Ind1 = eval(module_class.pr_expr(Net[3]),Mod.parameters)
        return [("%s[%s][%s]" % (Bus,Ind0,Ind1),Pin)]


    elif  (type(Net) is list) and (Net[0] == "curly"):
        Res = []
        for Item in Net[1:]:
            More = explodeBus(Bus,Item, Pin)
            for A, _ in More:
                Res.append(A)
        for ind, Item in enumerate(Res):
            Res[ind] = Item, f"{Pin}[{ind}]"
        return Res
    else:
        logs.log_error("explodeBus got %s" % str(Net))
        return []
        


