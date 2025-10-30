
FLOPS = {}
FLOPS['scs130ms_dfrtp_1'] = ('D','Q')
FLOPS['scs130ms_dfxtp_1'] = ('D','Q')
FLOPS['scs130ms_dfstp_1'] = ('D','Q')
FLOPS['DFF'] = ('D','Q')
FLOPS['DFFR'] = ('D','Q')
FLOPS['DFFS'] = ('D','Q')
import logs
REPLACE = {}
def help_main(Env):
    Mod = Env.Current
    for Inst in  Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type in FLOPS:
            D,Q = FLOPS[Obj.Type]
            DD = Obj.conns[D]
            QQ = Obj.conns[Q]
            if (DD[0] == '_') and (DD[-1] == '_'):
                New = outx(QQ)
                Obj.conns[D] = New
                REPLACE[str(DD)] = New
    ties(Mod)
    REMOVE = []
    for Inst in  Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == 'blkbox':
            In = Obj.conns['a']
            Out = Obj.conns['x']
            if (type(In) is list) and (In[0] == 'curly'):
                Mod.hard_assigns.append((Out,In,'',''))
            else:
                REPLACE[str(In)] = Out
            REMOVE.append(Inst)

    for Inst in REMOVE:
        Mod.insts.pop(Inst)

    for Inst in  Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            if str(Sig) in REPLACE:
                Obj.conns[Pin] = REPLACE[str(Sig)]
                print("REPLACE %s" % str(Sig))
                Bus = getBus(Sig)
    for ind,(Dst,Src,_,_) in enumerate(Mod.hard_assigns):
        Src1 = useReplaces(Src,REPLACE)
        Mod.hard_assigns[ind] = Dst,Src1,'',''
            



    for Sig in REPLACE:                
        Bus = getBus(Sig)
        if Bus in Mod.nets:
            Mod.nets.pop(Bus)

    Fout = open('glv2/%s.v' % Mod.Module,'w')
    Mod.dump_verilog(Fout)
    Fout.close()

def outx(QQ):
    if type(QQ) is str: return 'prev_'+QQ

    if type(QQ) is list:
        return [QQ[0],'prev_'+QQ[1],QQ[2]]
    if type(QQ) is tuple:
        return (QQ[0],'prev_'+QQ[1],QQ[2])

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

