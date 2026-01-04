
FLOPS = {}
FLOPS['scs130ms_dfrtp_1'] = ('D','Q')
FLOPS['scs130ms_dfxtp_1'] = ('D','Q')
FLOPS['scs130ms_dfstp_1'] = ('D','Q')
FLOPS['DFF'] = ('D','Q')
FLOPS['DFFR'] = ('D','Q')
FLOPS['DFFS'] = ('D','Q')

from skywaterLib import cellLib
from skywaterHelp import *
import module_class

def isSynWire(Wire):
    if type(Wire) is str:
        return (Wire[0] == '_') and (Wire[-1] == '_')

    if type(Wire) is list:
        if Wire[0] == 'subbit':
            return isSynWire(Wire[1])
    return Wire


for Cell in cellLib:
    if isFlipFlop(Cell):
        Desc = cellLib[Cell]
        Jobs = list(Desc.pinsJobs.keys())
        if 'clock' in Jobs: Jobs.pop('clock')
        if '_1' in Cell:
            if 'D' not in Jobs: 
                if 'D' in Desc.Pins:
                    print('cellLib["%s"].set_pin_job("D","data")' % Cell)
            if 'DE' not in Jobs: 
                if 'DE' in Desc.Pins:
                    print('cellLib["%s"].set_pin_job("DE","data")' % Cell)


import logs
REPLACE = {}
def help_main(Env):
    Mod = Env.Current
    dumpv(Mod,'aaa')
    removeXassigns(Mod)
    removeParams(Mod)
 
    dumpv(Mod,'aa0')
#    for Dst,Src,_,_ in Mod.hard_assigns:
#        logs.log_info('HASSIGN %s %s ' % (Dst,Src))



    for Inst in  Mod.insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        if isFlipFlop(Type):
            Dpin =  libDataPin(Type)
            Qpin =  libOutputPin(Type)
            DD = Obj.conns[Dpin]
            QQ = Obj.conns[Qpin]
            if isSynWire(DD):
                New = outx(QQ)
                Obj.conns[Dpin] = New
                REPLACE[str(DD)] = New
            DEpin =  libDataEnablePin(Type)
            if DEpin:
                DD = Obj.conns[DEpin]
                QQ = Obj.conns[Qpin]
                if isSynWire(DD):
                    New = outxe(QQ,'eprev_')
                    Obj.conns[DEpin] = New
                    REPLACE[str(DD)] = New
                
    ties(Mod)
    REMOVE = []
    for Inst in  Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == 'blkbox':
            In = Obj.conns['a']
            Out = Obj.conns['x']
            Mod.hard_assigns.append((Out,In,'',''))
            REMOVE.append(Inst)

    for Inst in REMOVE:
        Mod.insts.pop(Inst)

#    for Inst in  Mod.insts:
#        Obj = Mod.insts[Inst]
#        for Pin in Obj.conns:
#            Sig = Obj.conns[Pin]
#            if (type(Sig) is list) and (Sig[0] == 'curly'):
#                Res = ['curly']
#                for Item in Sig[1:]:
#                    if str(Item) in REPLACE:
#                        Res.append(REPLACE[str(Item)])
#                    else:
#                        Res.append(Item)
#                Obj.conns[Pin] = Res
#            elif str(Sig) in REPLACE:
#                Obj.conns[Pin] = REPLACE[str(Sig)]
#                Bus = getBus(Sig)
#    for ind,(Dst,Src,_,_) in enumerate(Mod.hard_assigns):
#        Src1 = useReplaces(Src,REPLACE)
#        Mod.hard_assigns[ind] = Dst,Src1,'',''
            



    for Sig in REPLACE:                
        Bus = getBus(Sig)
        if Bus in Mod.nets:
            Mod.nets.pop(Bus)

    dumpv(Mod,'aa1')
    simplifyInsts(Mod)
    dumpv(Mod,'aa2')
    dealAssigns(Mod)
    dumpv(Mod,'aa3')
    makeBufs(Mod)
    renameOutxInventeds(Mod)
    Fout = open('glv2/%s.v' % Mod.Module,'w')
    Mod.dump_verilog(Fout)
    Fout.close()

def dumpv(Mod,Name):
    Fout = open('%s.v' % Name,'w')
    Mod.dump_verilog(Fout)
    Fout.close()
    


def outx(QQ,Prev='prev_'):
    if type(QQ) is str: return Prev+QQ

    if type(QQ) is list:
        return [QQ[0],Prev+QQ[1],QQ[2]]
    if type(QQ) is tuple:
        return (QQ[0],Prev+QQ[1],QQ[2])

    return 'ERROR'


def getBus(Dst):
    if type(Dst) is str: return Dst
    if (type(Dst) is  list) or (type(Dst) is  tuple):
        logs.log_info('>>>>> %s' % str(Dst))
        return Dst[1]

    logs.log_error('getBus got %s' % str(Dst))
    return 'xxx'

def useReplaces(Src,REPLACE):
    if type(Src) is str:
        if Src in REPLACE: return REPLACE[Src]
        return Src

    if type(Src) is int: return Src

    if (type(Src) is list)or(type(Src) is tuple):
        if Src[0] in ['dig','bin','hex']: return Src
        if str(Src) in REPLACE: return REPLACE[str(Src)]
        if Src[0] in ['subbit','subbus']: return Src
        if Src[0] in ['|','||','&&','&','^','curly']:
            for ind,X in enumerate(Src[1:]):
                Y = useReplaces(X,REPLACE)
                Src[ind+1] = Y
            return Src

    logs.log_error('useReplaces got %s' % str(Src))
    return Src
    
def ties(Mod):
    List  = list(Mod.insts.keys())
    VCC,GND = False,False
    for Inst in List:
        Obj = Mod.insts[Inst]
        if Obj.Type == 'TIELO':
            Sig = Obj.conns['Y']
            REPLACE[str(Sig)] = 'gnd'
            Mod.insts.pop(Inst)
            GND = True
        elif Obj.Type == 'TIEHI':
            Sig = Obj.conns['Y']
            REPLACE[str(Sig)] = 'vcc'
            Mod.insts.pop(Inst)
            VCC = True
    if VCC: Mod.nets['vcc'] = 'wire',1
    if GND: Mod.nets['gnd'] = 'wire',1


def removeXassigns(Mod):
    ind = 0
    while ind < len(Mod.hard_assigns):
        Dst,Src,_,_ = Mod.hard_assigns[ind]
        if (type(Src) is str) and ("'hx" in Src):
            Mod.hard_assigns.pop(ind)
            ind -= 1

        ind += 1

def renameOutxInventeds(Mod):
    ind = 0
    RENAMES = {}
    REMOVES = []
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == 'BUF':
            Dst = Obj.conns['X']
            Src = Obj.conns['A']
            if (type(Src) is str) and (type(Dst) is str): 
                if ('invented' in Dst) and ('outx_invented' in Src):
                    if Src.endswith(Dst):
                        RENAMES[Src] = Dst
                        REMOVES.append(Inst)
            else:
                logs.log_info("RRR000RR %s %s" % (Dst,Src))

    for Inst in REMOVES:
        Mod.insts[Inst]

    useRenames(Mod,RENAMES)

def useRenames(Mod,RENAMES):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            if (type(Sig) is str) and (Sig in RENAMES):
                New = RENAMES[Sig]
                Obj.conns[Pin] = New
                if (type(Sig) is str) and (Sig in Mod.nets): Mod.nets.pop(Sig)
                logs.log_info("RENAMED %s %s %s" % (Inst,Sig,New))

def removeParams(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Obj.params = {}

def simplifyInsts(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            Sig2 = simplifySig(Sig)
            Obj.conns[Pin] = Sig
            

def simplifySig(Sig):
    if type(Sig) is str: return Sig
    if type(Sig) is int: return Sig
    if Sig[0] == 'subbit':
        return module_class.hashit(Sig)
    if Sig[0] == 'curly':
        Res = ['curly']
        for Item in Sig[1:]:
            New = simplifySig(Item)
            Res.append(New)
        return Res             
    return Sig


def normalize(Sig):
    return Sig

def explodeBus(Sig,Mod):
    if Sig in [0,'0','gnd']:
        return ['gnd']
    if Sig in [1,'1','vcc']:
        return ['vcc']
    if (type(Sig) is str) and (Sig in Mod.nets):
        _,Wid = Mod.nets[Sig]
        if (type(Wid) is tuple) and (len(Wid) ==2):
            Hi = int(Wid[0])
            Lo = int(Wid[1])
            return explodeBus(['subbus',normalize(Sig),Hi,Lo],Mod)
        elif (Wid == 0):
            pass
        else:
            logs.log_error("explodeBus got %s  %s" % (Sig,Wid))  
           
    elif (type(Sig) is str) and (Sig[0] in '123456789'):
        if "'" in Sig:
            ww = Sig.split("'")
            Wid = int(ww[0])
            Val0 = ww[1][1:]
            if 'x' in Val0: Val = 0
            elif ww[1][0] == 'h': Val = int(ww[1][1:],16)
            elif ww[1][0] == 'd': Val = int(ww[1][1:],10)
            elif ww[1][0] == 'b': Val = int(ww[1][1:],2)
            Seq = list(logs.binx(Val,Wid))
            return Seq
        return [Sig]
    elif (type(Sig) is list) and (Sig[0] == 'subbit'):
        Sigx = '%s[%s]' % (normalize(Sig[1]),Sig[2])
        return [Sigx] 
    elif (type(Sig) is list) and (Sig[0] == 'subbus'):
        if len(Sig)==3:
            Hi = int(Sig[2][0])
            Lo = int(Sig[2][1])
        else:
            Hi = int(Sig[2])
            Lo = int(Sig[3])
        Res = []
        for Ind in range(Hi,Lo-1,-1):
            Res.append('%s[%s]' % (normalize(Sig[1]),Ind))
        return Res
    elif (type(Sig) is list) and (Sig[0] == 'curly'):
        Res = []
        for Item in Sig[1:]:
            Part = explodeBus(Item,Mod)
            Res.extend(Part)
        return Res
    elif (type(Sig) is list) and (Sig[0] == 'hex'):
        if Sig[2][0] == 'x':
            if str(Sig[1]) == '1': return 'gnd'
            if type(Sig[2]) is str:
                Res = []
                for ii in range(len(Sig[2])):
                    Res.append('gnd')
                return Res
            logs.log_error("XXXXXXXXXX %s %s" % (Sig[2],Sig))
    elif (type(Sig) is list) and (Sig[0] == 'bin'):
        if Sig[1] in ['1',1]:
            if str(Sig[2]) == '1': return ['vcc']
            if str(Sig[2]) == '0': return ['gnd']
    if (type(Sig) is str):
        Sig1 = normalize(Sig)
        return [Sig1]
    else:
        logs.log_error('explodeBus got "%s" in %s ' % (Sig,Mod.Module))
        return [Sig]
    

def dealAssigns(Mod):
    Ind = 0
    Limit = len(Mod.hard_assigns)
    Adds = []
    while Ind < len(Mod.hard_assigns):
        Dst,Src,X,Y = Mod.hard_assigns[Ind]
        Dseq = explodeBus(Dst,Mod)
        Sseq = explodeBus(Src,Mod)
        if '0' in Dseq:
            logs.log_error("OOOOOOOOOOOO %s %s" % (Dseq,Dst))
        elif (len(Dseq) == 1) and (len(Sseq) == 1):
            if Dseq[0] != Sseq[0]:
                Mod.hard_assigns[Ind] = Dseq[0],Sseq[0],X,Y
        elif (len(Dseq)  == len(Sseq)):
            Mod.hard_assigns.pop(Ind)
            Ind -= 1
            for ind,D in enumerate(Dseq):
                S = Sseq[ind]
                Adds.append((Mod.pr_expr(D),Mod.pr_expr(S),X,Y))
        else:
            Mod.hard_assigns.pop(Ind)
            Ind -= 1
            for ind,D in enumerate(Dseq):
                if len(Sseq)>ind:
                    S = Sseq[ind]
                else:
                    S = 0
                if D != '0':
                    Adds.append((Mod.pr_expr(D),Mod.pr_expr(S),X,Y))
        Ind +=1
    Mod.hard_assigns.extend(Adds)

def makeBufs(Mod):
    Ind = 0
    while Ind<len(Mod.hard_assigns):
        Dst,Src,_,_ = Mod.hard_assigns[Ind]
        if (type(Dst) is str) and (type(Src) is str):
            Mod.hard_assigns.pop(Ind)
            Ind -= 1
            Obj = Mod.add_inst('BUF','')
            Obj.conns['A'] = Mod.pr_expr(Src)
            Obj.conns['X'] = Mod.pr_expr(Dst)
        Ind += 1
            




