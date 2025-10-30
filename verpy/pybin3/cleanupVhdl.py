
import logs
# make code more readable after VHDL -> Verilog translation.
Replaced = 0

def help_main(Env):
    global Replaced
    Mod = Env.Current

    Replace = gather0(Mod)
    Replaced = 1
    while Replaced != 0:
        Replaced = 0
        useReplaces(Mod,Replace)
        print("REPLACED0",Replaced)
    removeNotUsed(Mod)
    makeRegs(Mod)

    Fout = open('%s.tmp0' % Mod.Module,'w')
    Mod.dump_verilog(Fout)
    Fout.close()

    Replace = gather00(Mod)
    Replaced = 1
    while Replaced != 0:
        Replaced = 0
        useReplaces(Mod,Replace)
        print("REPLACED00",Replaced)
    removeNotUsed(Mod)
    makeRegs(Mod)
    Fout = open('%s.tmp1' % Mod.Module,'w')
    Mod.dump_verilog(Fout)
    Fout.close()

    Replace = gather1(Mod)
    Replaced = 1
    while Replaced != 0:
        Replaced = 0
        useReplaces(Mod,Replace)
        print("REPLACED2",Replaced)

    removeNotUsed(Mod)
    makeRegs(Mod)
    Mod.initials.append( ['functioncall','$display',['"path %s :  %%m"'% Mod.Module]])
    fixSubbuses(Mod)
    fixWires(Mod)
    Fout = open('%s.v' % Mod.Module,'w')
    Mod.dump_verilog(Fout)
    Fout.close()

def fixWires(Mod):
    for (Dst,Src,_,_) in Mod.hard_assigns:
        scanForInds(Dst,Mod)
        scanForInds(Src,Mod)

def scanForInds(Src,Mod):
    if type(Src) is str: return 
    if type(Src) is list:
        if Src[0] == 'question':
            scanForInds(Src[1],Mod)
            scanForInds(Src[2],Mod)
            scanForInds(Src[3],Mod)
            return
        if Src[0] == 'subbit':
            Ind = Src[2]
            Bus = Src[1]
            checkWires(Bus,Ind,Mod)
            return
        if Src[0] == 'subbus':
            Hi = Src[2][0]
            Lo = Src[2][1]
            Bus = Src[1]
            checkWires(Bus,Hi,Mod)
            checkWires(Bus,Lo,Mod)
            return
        if Src[0] in ['hex','bin']:
            return
        if Src[0] in OPS:
            scanForInds(Src[1],Mod)
            if len(Src) == 3: 
                scanForInds(Src[2],Mod)
            return
        if Src[0] in ['curly']:
            for Item in Src[1:]:
                scanForInds(Item,Mod)
            return
                
    logs.log_error('MISSED scanForInds %s' % str(Src))

OPS = '^ + - * & && | || ~ ! == != > < <= =< >='.split()

def checkWires(Bus,Ind,Mod):
    Dir,Wid = Mod.nets[Bus]
    if type(Wid) is tuple:
        if len(Wid) == 2:
            Hi = Wid[0]
            Lo = Wid[1]
            if (type(Hi) is int) and (type(Lo) is int) and (type(Ind) is int):
                if Ind>Hi:
                    Mod.nets[Bus] = Dir,(Ind,Lo)              
                if Ind<Lo:
                    Mod.nets[Bus] = Dir,(Hi,Ind)              
                return
    logs.log_error('checkWires %s %s %s' % (Bus,Ind,Wid))
    
def fixSubbuses(Mod):
    for ind,(Dst,Src,_,_) in enumerate(Mod.hard_assigns):
        Src2 = scanForSub(Src,Mod)
#        logs.log_info("FIXSUB %s = %s  (%s) " % (Dst,Src2,Src))
        Mod.hard_assigns[ind] = (Dst,Src2,'','')

    for ind,Alw in enumerate(Mod.alwayses):
        Body = Alw[1]
        Body2 = scanForSub(Body,Mod)
        Mod.alwayses[ind] = [Alw[0],Body2,Alw[2]]
        

SRCS = {}
def scanForSub(Src,Mod):
    if type(Src) is list:
        if Src[0] == 'subbus':
            if type(Src[1]) is not str:
                Txt = str(Src[1])
                if Txt in SRCS:
                    Src[1] = SRCS[Txt]
                    return Src
                Wid = Src[2][0] + Src[2][1]+1
                New = Mod.add_sig('','wire',(Wid-1,0))
                logs.log_info("NEWSIG SUBBUS 0 %s %s" % (New,Wid)) 
                Mod.hard_assigns.append( (New,Src[1],'','') )
                Src[1] = New
                SRCS[Txt] = New
                logs.log_info("NEWSRCSBUS %s %s %s" % (New,Wid,Txt))
                return Src
        elif Src[0] == 'subbit':
            if type(Src[1]) is not str:
                if Src[1][0] == 'bin':
                    Val = int(Src[1][2],2)
                    Bit = (Val>>Src[2]) & 1
                    Src = "1'b%d" % Bit
                    return Src
                else:
                    Width = Mod.exprWidth(Src[1])
                    Txt = str(Src[1])
                    if Txt in SRCS:
                        New = SRCS[Txt]
                    else:
                        New = Mod.add_sig('','wire',(Width-1,0))
                        logs.log_info("NEWSIG SUBBIT 2 %s %s" % (New,Width)) 
                        Mod.hard_assigns.append( (New,Src[1],'','') )
                        SRCS[Txt] = New
                        logs.log_info("NEWSRCSSIG %s %s %s" % (New,Width,Txt))
                    Src[1] = New
                    return Src
        elif Src[0] == 'question':
            Cond =  scanForSub(Src[1],Mod)
            Yes =  scanForSub(Src[2],Mod)
            No =  scanForSub(Src[3],Mod)
            if isOne(Yes) and isZero(No):
                WidY = Mod.exprWidth(Yes)
                WidN = Mod.exprWidth(No)
                Wid = max(WidY,WidN)
                print("QQQQ cond=%s yes=%s no=%s wids = %s %s" % (Cond,Yes,No,WidY,WidN))
                if Wid<2:
                    return Cond
                else:
                    return ['curly',['bin',Wid-1,0],Cond]
            return ['question',Cond,Yes,No] 
        else:
            for ind,Item in enumerate(Src):
                X = scanForSub(Item,Mod)
                Src[ind] = X
    return Src


def makeRegs(Mod):
    List = Mod.initials
    for LL in List:
        if type(LL) is list:
            for Item in LL:
                if (type(Item) is list) and (Item[0] == '='):
                    makeNetReg(Item[1],Mod)
def makeNetReg(Net,Mod):
    if Net not in Mod.nets:
        Mod.nets[Net] = 'reg',1
        return
    Was,Wid = Mod.nets[Net]
    if Was == 'wire': 
        Mod.nets[Net] = 'reg',Wid
    elif ('reg' not in Was):
        Mod.nets[Net] = '%s reg' % Was,Wid

def removeNotUsed(Mod):
    Times = countReferences(Mod)

    Nets = list(Mod.nets.keys())
    Removed = 0
    for Net in Nets:
        if isNnet(Net):
            if Net not in Times:
                Removed += 1
                Mod.nets.pop(Net)
        if (Net in ['false','true']): # and (Net in Times):
            if (Times[Net] == 1):
                Removed += 1
                Mod.nets.pop(Net)
                ind = 0
                while ind<len(Mod.hard_assigns):
                    (Dst,Src,_,_) = Mod.hard_assigns[ind]
                    if Dst == Net:
                        Mod.hard_assigns.pop(ind)
                    else:
                        ind += 1

            else:
                print("NET %s %d" % (Net, Times[Net]))
    print("REMOVED N nets %d" % Removed)

def countReferences(Mod):
    Times = {}
    for (Dst,Src,_,_) in Mod.hard_assigns:
        countRefs(Dst,Times)
        countRefs(Src,Times)
    for Alw in Mod.alwayses:
        countRefs(Alw,Times)
    for Alw in Mod.initials:
        countRefs(Alw,Times)
    return Times 

def useReplaces(Mod,Replace):
    for ind,(Dst,Src,_,_) in enumerate(Mod.hard_assigns):
        Dst0 = use_always_replace(Dst,Replace)
        Src0 = use_always_replace(Src,Replace)
#        print("USEDREPL dst= %s %s src=%s %s" % (Dst0,Dst,Src0,Src))
        Mod.hard_assigns[ind] = (Dst0,Src0,'','')
    for ind,Alw in enumerate(Mod.alwayses):
        Alw = use_always_replace(Alw,Replace)
        Mod.alwayses[ind]=Alw
    for ind,Init in enumerate(Mod.initials):
        Init = use_always_replace(Init,Replace)
        Mod.initials[ind]=Init
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            Sig1 = use_always_replace(Sig,Replace)
            Obj.conns[Pin] = Sig1
            


def use_always_replace(Alw,Replace):
    global Replaced
    if type(Alw) is str:
        if Alw in Replace: 
            Replaced += 1
#            print("ALW alw=%s rep=%s" % (Alw,Replace[Alw]))
            return Replace[Alw]

    if (type(Alw) is list)or(type(Alw) is tuple):
        if (Alw[0] == 'edge') and (Alw[1] == 'posedge') and (Alw[2][0] == '~'):
            Replaced += 1
            Alw = ['edge','negedge',Alw[2][1]]
#    if (type(Alw) is list) and Alw[0] in ['subbus']:
#        return Alw
    if type(Alw) is list:
        Res = []
#        if Alw[0] in ['<','=']:
#            Res = Alw[:2]
#            for Item in Alw[2:]:
#                New = use_always_replace(Item,Replace)
#                Res.append(New)
#            return Res
        for Item in Alw:
            New = use_always_replace(Item,Replace)
            Res.append(New)
        return Res
    if type(Alw) is tuple:
        Res = []
        for Item in Alw:
            New = use_always_replace(Item,Replace)
            Res.append(New)
        return tuple(Res)
            
    return Alw
            

def countRefs(Alw,Times):
    if type(Alw) is str:
        if Alw not in Times: Times[Alw] = 0
        Times[Alw] += 1
    if type(Alw) is list:
        for Item in Alw:
            countRefs(Item,Times)
        return Times
    if type(Alw) is tuple:
        Res = []
        for Item in Alw:
            countRefs(Item,Times)
        return Times
            
    return Times
            




def gather0(Mod,Level=0):
    ind = 0
    REPLACE = {}
    while ind<len(Mod.hard_assigns):
        Dst,Src,_,_ = Mod.hard_assigns[ind]
#        if isNnet(Dst) and (not isNnet(Src)) and (type(Src) is str):
        if isNnet(Dst) and (type(Src) is str)and ('[' not in Src):
            print("REPLACE %s %s" % (Dst,Src))
            REPLACE[Dst] = Src
            Mod.hard_assigns.pop(ind)
        else:
            ind += 1
    return REPLACE
HARDS = []
def gather00(Mod,Level=0):
    ind = 0
    REPLACE = {}
    while ind<len(Mod.hard_assigns):
        Dst,Src,_,_ = Mod.hard_assigns[ind]
        if isNnet(Dst) and (not isNnet(Src)):
            if (type(Src) is list) and (Src[0] != 'curly'):
                REPLACE[Dst] = Src
                HARDS.append((Dst,Src))
                print("REPLACE2 %s %s" % (Dst,Src))
                Mod.hard_assigns.pop(ind)
            else:
                ind += 1
        else:
            ind += 1
    
    return REPLACE



def gather1(Mod,Level=0):
    ind = 0
    REPLACE = {}
    while ind<len(Mod.hard_assigns):
        Dst,Src,_,_ = Mod.hard_assigns[ind]
        if isNnet(Src) and not isNnet(Dst) and (type(Dst) is str):
            REPLACE[Src] = Dst
            Mod.hard_assigns.pop(ind)
        else:
            ind += 1
    return REPLACE

def isOne(Expr):
    if Expr in [1,'1',"1'b1"]: return True
    if (type(Expr) is list) or ( type(Expr) is tuple):
        if Expr[0] == 'bin':
            return isOne(Expr[2])
        
    return False

def isZero(Expr):
    if Expr in [0,'0',"1'b0"]: return True
    if (type(Expr) is list) or ( type(Expr) is tuple):
        if Expr[0] == 'bin':
            return isZero(Expr[2])
    return False

def isNnet(Net):
    if type(Net) is not str: return False
    if Net[0] != 'n': return False
    return Net[1:].isnumeric()
