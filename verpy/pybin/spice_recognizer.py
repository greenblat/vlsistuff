
import string
import sys
import logs

PMOS =  ['pdmos_tran']
NMOS =  ['ndmos_tran']

LOGICALS = string.split('and or nand nor inv xor xnor')
def help_main(Env):
    Mod = Env.Current
    useTranslations([('vdd30_to_dm','vdd'),('vdd33','vdd'),('vdd30','vdd'),('dvss','vss'),('dvddh','vdd'),('dvdd','vdd'),('avddh','vdd'),('avss','vss')],Mod,True)
    writeOut(Mod,'stp0')
    Ok = 1
    while (Ok>0):
        Ok = scanDesignForPattern(Mod)
    Ok = 1
    while (Ok>0):
        Ok = scanDesignForPattern(Mod)
    removeOrphans(Mod)
    writeOut(Mod,'stp1x')
    gateMerges(Mod)
    writeOut(Mod,'stp1y')
    orphanWires(Mod)
    writeOut(Mod,'stp1')
    recognizeSRlatch(Mod)
    extractCmosMux(Mod)
    writeOut(Mod,'stp2')
    recognizePattern2(XOR_pattern,Mod)
    gateMerges(Mod)
    removeOrphans(Mod)

    recognizePattern2(Dlatch_pattern,Mod)
    writeOut(Mod,'stp3')
    recognizePattern2(Dlatch2_pattern,Mod)
    recognizePattern2(Dlatch3_pattern,Mod)
    writeOut(Mod,'stp4')
    recognizePattern2(Dff_pattern,Mod)
    writeOut(Mod,'stp5')
    scanGates(Mod,True)
    orphanWires(Mod)
    ncInverters(Mod)
    writeOut(Mod,'stp6')
    consecutiveInverters(Mod)
    removeOrphans(Mod)
    writeOut(Mod,'stp7')

    turnGatesToAssigns(Mod)
    writeOut(Mod,'newv')

def writeOut(Mod,Ext = 'v'):
    Fout = open('%s.%s'%(Mod.Module,Ext),'w')
    Mod.dump_verilog(Fout)
    Fout.close()




def extractPowers(Mod):
    Mod.Vdd = []
    Mod.Vss = []
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type in PMOS:
            if 'b' in Obj.conns:
                VDD = Obj.conns['b']
                if  VDD not in Mod.Vdd: Mod.Vdd.append(VDD)
        if Obj.Type in NMOS:
            if 'b' in Obj.conns:
                VSS = Obj.conns['b']
                if  VSS not in Mod.Vss: Mod.Vss.append(VSS)





def transistor(Inst,Mod):
    Obj = Mod.insts[Inst]
    if Obj.Type not in PMOS+NMOS: return False
    S = Obj.conns['s']
    D = Obj.conns['d']
    G = Obj.conns['g']
    B = Obj.conns['b']
    L1 = [S,D]
    L1.sort()
    if B in L1: 
        Pref = 'supply'
    else:
        Pref = ''
    if Obj.Type in PMOS: Type = 'pmos'+Pref
    if Obj.Type in NMOS: Type = 'nmos'+Pref
    return (L1,G,Type,Inst)

def extractTrans(Mod):
    for Inst in Mod.insts:
        Tran =  transistor(Inst,Mod)
        if Tran: 
            if 'pmos' in Tran[2]:
                Pmoses.append(Tran)
            elif 'nmos' in Tran[2]:
                Nmoses.append(Tran)

    


def x2nets(Mod):
    X2 = []
    Mod.prepareNetTable()
    for Net in Mod.netTable:
        if x2net(Net,Mod):
            X2.append(Net)
    return X2            

def x2net(Net,Mod):
#    if Net not in Mod.nets: return True
    Dir,_ = Mod.nets[Net]
    if not internalNet(Net,Mod): return False
    if (len(Mod.netTable[Net])!=2): return False
    return True
        

    
# ?Nx - any net
# ?Xx - 2x net 
# ?Ix - 2x net 
# Pattern "MOS GATE S D B"

def cmos(Dict,Insts,Mod):
    logs.log_info('cmos %s %s'%(Insts,Dict))
    Gp = Mod.insts[Insts[0]].conns['g']
    Gn = Mod.insts[Insts[1]].conns['g']
    Sp = Mod.insts[Insts[0]].conns['s']
    Dp = Mod.insts[Insts[0]].conns['d']
    Sn = Mod.insts[Insts[1]].conns['s']
    Dn = Mod.insts[Insts[1]].conns['d']
    SDp = [Sp,Dp]
    SDp.sort()
    SDn = [Sn,Dn]
    SDn.sort()
    if (SDn==SDp):
        Mod.insts.pop(Insts[0])
        Mod.insts.pop(Insts[1])
        Mod.add_inst_conns('cmos',string.join(Insts,'_'),[('i',Sp),('o',Dp),('gn',Gn),('gp',Gp)])

def inverter(Dict,Insts,Mod):
    logs.log_info('inverter %s %s'%(Insts,Dict))
    Mod.insts.pop(Insts[0])
    Mod.insts.pop(Insts[1])
    Mod.add_inst_conns('inv',string.join(Insts,'_'),[('i',Dict['?N1']),('o',Dict['?N2'])])



def parallel_nmos(Dict,Insts,Mod):
    G0 = Mod.insts[Insts[0]].conns['g']
    G1 = Mod.insts[Insts[1]].conns['g']
    Mod.insts.pop(Insts[1])
    if G0==G1: return
    Gate = '%s_%s_g'%(G0,G1)
    Mod.add_inst_conns('or',string.join(Insts,'_'),[('i0',G0),('i1',G1),('o',Gate)])
    Mod.insts[Insts[0]].conns['g']=Gate




def parallel_pmos(Dict,Insts,Mod):
    G0 = Mod.insts[Insts[0]].conns['g']
    G1 = Mod.insts[Insts[1]].conns['g']
    Mod.insts.pop(Insts[1])
    if G0==G1: return
    Gate = '%s_%s_g'%(G0,G1)
    Mod.add_inst_conns('and',string.join(Insts,'_'),[('i0',G0),('i1',G1),('o',Gate)])
    Mod.insts[Insts[0]].conns['g']=Gate


def serial_nmos(Dict,Insts,Mod):
    logs.log_info('serial_nmos %s %s'%(Insts,Dict))
    Mod.insts.pop(Insts[1])
    if Dict['?X1']==Mod.insts[Insts[0]].conns['s']:
        Mod.insts[Insts[0]].conns['s']=Dict['?N4']
    else:
        Mod.insts[Insts[0]].conns['d']=Dict['?N4']

    if Dict['?N1']==Dict['?N3']: return
    Gate = '%s_%s_g'%(Dict['?N1'],Dict['?N3'])
    Mod.add_inst_conns('and',string.join(Insts,'_'),[('i0',Dict['?N1']),('i1',Dict['?N3']),('o',Gate)])
    Mod.insts[Insts[0]].conns['g']=Gate

def short_mos(Dict,Insts,Mod):
    logs.log_info('short_mos %s %s'%(Insts,Dict))
    Mos = Insts[0]
    Obj = Mod.insts[Mos]
    N1 = Dict['?N1']
    Mod.insts.pop(Mos)
    if Obj.Type in PMOS:
        useTranslations([(N1,'vdd')],Mod,True)
    if Obj.Type in NMOS:
        useTranslations([(N1,'vss')],Mod,True)


def serial_pmos(Dict,Insts,Mod):
    logs.log_info('serial_pmos %s %s'%(Insts,Dict))
    Mod.insts.pop(Insts[1])
    if Dict['?X1']==Mod.insts[Insts[0]].conns['s']:
        Mod.insts[Insts[0]].conns['s']=Dict['?N4']
    else:
        Mod.insts[Insts[0]].conns['d']=Dict['?N4']

    if Dict['?N1']==Dict['?N3']: return
    Gate = '%s_%s_g'%(Dict['?N1'],Dict['?N3'])
    Mod.add_inst_conns('or',string.join(Insts,'_'),[('i0',Dict['?N1']),('i1',Dict['?N3']),('o',Gate)])
    Mod.insts[Insts[0]].conns['g']=Gate


def cross_mos(Dict,Insts,Mod):
    logs.log_info('cross_mos %s %s'%(Dict,Insts))
    Mod.add_inst_conns('cross_mos',invent_inst('cross'),[('i0',Dict['?I0']),('i1',Dict['?I1']),('q0',Dict['?Q0']),('q1',Dict['?Q1'])])
    for Inst in Insts: Mod.insts.pop(Inst)


Pattern0 = (('nmos ?N1 ?N2 vss vss','pmos ?N1 ?N2 vdd vdd'),inverter)
Pattern1 = (('nmos ?N1 ?I1 ?I2 vss','nmos ?N2 ?I1 ?I2 vss'),parallel_nmos)
Pattern2 = (('pmos ?N1 ?I1 ?I2 vdd','pmos ?N2 ?I1 ?I2 vdd'),parallel_pmos)
Pattern3 = (('nmos ?N1 ?N2 ?X1 vss','nmos ?N3 ?X1 ?N4 vss'),serial_nmos)
Pattern4 = (('pmos ?N1 ?N2 ?X1 vdd','pmos ?N3 ?X1 ?N4 vdd'),serial_pmos)
Pattern5 = (('pmos ?N1 ?N2 ?N3 vdd','nmos ?N4 ?N2 ?N3 vss'),cmos)
Pattern6 = (['pmos ?N1 ?N1 vdd vdd'],short_mos)
Pattern7 = (['nmos ?N1 ?N1 vss vss'],short_mos)
Pattern8 = (['pmos ?N1 vdd ?N1 vdd'],short_mos)
Pattern9 = (['nmos ?N1 vss ?N1 vss'],short_mos)
PatternCross = ([
      'pmos ?Q0 vdd ?Q1 vdd'
     ,'pmos ?Q1 vdd ?Q0 vdd'
     ,'nmos ?I0 vss ?Q1 vss'
     ,'nmos ?I1 vss ?Q0 vss'

    ],cross_mos)

PATTERNS = [Pattern0,Pattern1,Pattern2,Pattern3,Pattern4,Pattern5,Pattern6,Pattern7,Pattern8,Pattern9,PatternCross]

    

def scanDesignForPattern(Mod):
    Dones = 0
    for Pattern in PATTERNS:
        Dones += scanPattern(Pattern,Mod)
    Dones += scanGates(Mod)
    return Dones

def scanPattern(Pattern,Mod):
    Dic = {}
    LL = list(Pattern[0])
    return lookForMatch(LL,Dic,[],Pattern[1],Mod)

def lookForMatch(LL,Dic,Insts,Job,Mod):
    Dones = 0
    if LL==[]: 
        usePattern(Dic,Job,Insts,Mod)
        return Dones+1
    Look = LL[0]
    Wrds = string.split(Look)
    Keys = Mod.insts.keys()
    for Inst in Keys:
        if (Inst in Mod.insts)and(Inst not in Insts):
            Obj = Mod.insts[Inst]
            if  ((Wrds[0]=='pmos')and(Obj.Type in PMOS))or((Wrds[0]=='nmos')and(Obj.Type in NMOS)): 
                Copy = copyDict(Dic)
                if isMatch(Obj.conns['g'],Wrds[1],Copy,Mod)and isMatch(Obj.conns['b'],Wrds[4],Copy,Mod):
                    S = Obj.conns['s']
                    D = Obj.conns['d']
                    if is2Match([S,D],Wrds[2:4],Copy,Mod): 
                        Dones += lookForMatch(LL[1:],Copy,Insts+[Inst],Job,Mod)
    return 0

def is2Match(Sigs,Pats,Dic,Mod):
    Copy = copyDict(Dic)
    if isMatch(Sigs[0],Pats[0],Copy,Mod) and isMatch(Sigs[1],Pats[1],Copy,Mod):
        isMatch(Sigs[0],Pats[0],Dic,Mod)
        isMatch(Sigs[1],Pats[1],Dic,Mod)
        return True
        
    Copy = copyDict(Dic)
    if isMatch(Sigs[0],Pats[1],Copy,Mod) and isMatch(Sigs[1],Pats[0],Copy,Mod):
        isMatch(Sigs[0],Pats[1],Dic,Mod)
        isMatch(Sigs[1],Pats[0],Dic,Mod)
        return True
    
    return False

def copyDict(Dict):
    Res = {}
    for Key in Dict.keys(): Res[Key]=Dict[Key]
    return Res

def isMatch(Sig,Pat,Dic,Mod):
    if Sig==Pat: return True
    if Pat[0] != '?' : return False

    if Pat in Dic:
        Prev = Dic[Pat]
        if Sig != Prev: return False
        return True

    if Pat[1]=='X':
        if is2X(Sig,Mod):
            Dic[Pat]=Sig
            return True
    
    if Pat[1] in ['N','I','S','Q','D','R','C']:
        Dic[Pat]=Sig
        return True
    return False
    
def is2X(Sig,Mod):  
    List = x2nets(Mod)
    return Sig in List
        
def usePattern(Dict,Job,Insts,Mod):
    Job(Dict,Insts,Mod)


def scanGates(Mod,alsoInvs=False):
    Ands,Ors,Invs = [],[],[]
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type=='and': 
            Ands.append(Inst)
        elif Obj.Type=='or': 
            Ors.append(Inst)
        elif Obj.Type=='inv': 
            Invs.append(Inst)
    Dones = dealWithGates(Ands,Mod)
    Dones += dealWithGates(Ors,Mod)
    if alsoInvs:
        Dones += mergeSames(Invs,Mod)
    return Dones
        


def dealWithGates(List,Mod):
    Dones = 0
    List0 = List[:]
    while List!=[]:
        Inst0 = List.pop(0)
        if Inst0 in Mod.insts:
            Out0,Ins0 = getConns(Inst0,Mod)
            for Inst1 in List:
                if Inst1 in Mod.insts:
                    Out1,Ins1 = getConns(Inst1,Mod)
                    if Out0 in Ins1:
                        Obj1 = Mod.insts[Inst1]
                        Ins1.remove(Out0)
                        for In in Ins0: 
                            if In not in Ins1: Ins1.append(In)
                        Ins1.sort()
                        rmInputs(Obj1)
                        addInputs(Ins1,Obj1)
                        Dones += 1
                    
                    if Out1 in Ins0:
                        Obj0 = Mod.insts[Inst0]
                        Ins0.remove(Out1)
                        for In in Ins1: 
                            if In not in Ins0: Ins0.append(In)
                        Ins0.sort()
                        rmInputs(Obj0)
                        addInputs(Ins0,Obj0)
                        Dones += 1
    Dones += mergeSames(List0,Mod)
    return Dones

def mergeSames(List0,Mod):
    Translates = []
    Dones = 0
    while List0!=[]:
        Inst0 = List0.pop(0)
        if Inst0 in Mod.insts:
            Out0,Ins0 = getConns(Inst0,Mod)
            for Inst1 in List0:
                if Inst1 in Mod.insts:
                    Out1,Ins1 = getConns(Inst1,Mod)
                    if Ins0==Ins1:
                        Mod.insts.pop(Inst1)
                        Translates.append((Out1,Out0))
                        Dones += 1

    useTranslations(Translates,Mod) 
    return Dones
            
def rmInputs(Obj):
    Pins = Obj.conns.keys()
    for Pin in Pins:
        if Pin[0]=='i': Obj.conns.pop(Pin)

def addInputs(Sigs,Obj):
    for ind,Sig in enumerate(Sigs):
        Obj.conns['i%d'%ind]=Sig

def getConns(Inst,Mod):
    Obj = Mod.insts[Inst]
    Out = Obj.conns['o']
    Ins = []
    for Pin in Obj.conns:   
        if Pin!='o':
            Ins.append(Obj.conns[Pin])
    Ins.sort()
    return Out,Ins

def removeOrphans(Mod):
    Dones = 0
    Mod.prepareNetTable()
    Insts = Mod.insts.keys()
    for Inst in Insts:
        Obj  = Mod.insts[Inst]
        if Obj.Type in LOGICALS:
            Out = Obj.conns['o']
            if internalNet(Out,Mod) and (len(Mod.netTable[Out])==1):
                Mod.insts.pop(Inst)
                if Out in Mod.nets: 
                    Mod.nets.pop(Out)
                    Dones += 1
    if Dones>0:
        removeOrphans(Mod)


            
def internalNet(Net,Mod):
    if Net not in Mod.nets: return True
    Dir,_ = Mod.nets[Net]
    if 'input' in Dir: return False
    if 'output' in Dir: return False
    if 'inout' in Dir: return False
    return True

def useTranslations(Translates,Mod,Force=False):
    Table = {}
    for (Sig0,Sig1) in Translates:
        if Force:
            Table[Sig0]=Sig1
        elif not internalNet(Sig0,Mod):
            Table[Sig0]=Sig1
        elif not internalNet(Sig1,Mod):
            Table[Sig1]=Sig0
        else:
            Table[Sig0]=Sig1

    for From in Table:
        To = Table[From]
        if (To not in Mod.nets):
            if (From in Mod.nets):
                Mod.nets[To] = Mod.nets[From]
            else:
                Mod.nets[To] = ('wire',0)
        

    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            if Sig in Table:
                Obj.conns[Pin] = Table[Sig]

def gateMerges(Mod):
    Invs = {}
    for Inst in Mod.insts:
        Obj =  Mod.insts[Inst]
        if Obj.Type=='inv':
            Out,Ins = getConns(Inst,Mod)
            Invs[Ins[0]]=(Inst,Out)            
    LOGS = LOGICALS[:]
    LOGS.remove('inv')
    Keys = Mod.insts.keys()
    for Inst in Keys:
        if Inst in Mod.insts:
            Obj  = Mod.insts[Inst]
            if Obj.Type in LOGS:
                Out = Obj.conns['o']
                if (Out in Invs) and is2X(Out,Mod):
                    Obj.conns['o']=Invs[Out][1]
                    Mod.insts.pop(Invs[Out][0])
                    Mod.nets.pop(Out)
                    if Obj.Type=='xnor':
                        Obj.Type = 'xor'
                    elif Obj.Type[0]=='n':
                        Obj.Type = Obj.Type[1:]
                    else:
                        Obj.Type = 'n'+Obj.Type
def orphanWires(Mod):
    Mod.prepareNetTable()
    Nets = Mod.nets.keys()
    for Net in Nets:
        if internalNet(Net,Mod) and (Net not in Mod.netTable):
            Mod.nets.pop(Net)

def recognizeSRlatch(Mod):
    Nors = {}
    for Inst in Mod.insts:
        Obj  = Mod.insts[Inst]
        if Obj.Type == 'nor':
            Out,Ins = getConns(Inst,Mod)
            Nors[Out] = (Inst,Ins)
    Outs = Nors.keys()
    while Outs!=[]:
        Out0 = Outs.pop(0)
        Nor0,Ins0 = Nors[Out0]
        for Out1 in Outs:
            Nor1,Ins1 = Nors[Out1]
            if (Out1 in Ins0) and (Out0 in Ins1):
                Mod.insts.pop(Nor0)
                Mod.insts.pop(Nor1)
                Outs.pop(Outs.index(Out1))
                New = '%s_%s'%(Nor0,Nor1)
                Mod.add_inst_conns('srlatch',New,[('qn',Out0),('q',Out1)])
                Ins0.remove(Out1)
                Ins1.remove(Out0)
                if len(Ins0)==1:
                    Mod.add_conn(New,'s',Ins0[0])
                else:
                    Mod.add_inst_conns('or',New+'_sor',[('o',New+'_s')])
                    Mod.add_conn(New,'s',New+'_s')
                    for ind,In in enumerate(Ins0):
                        Mod.add_con(New+'_sor','i%d'%ind,In)

                if len(Ins1)==1:
                    Mod.add_conn(New,'r',Ins1[0])
                else:
                    Mod.add_inst_conns('or',New+'_ror',[('o',New+'_r')])
                    Mod.add_conn(New,'r',New+'_r')
                    for ind,In in enumerate(Ins0):
                        Mod.add_con(New+'_ror','i%d'%ind,In)
                    
def extractType(Type,Mod):                
    Insts = {}
    for Inst in Mod.insts:
        Obj  = Mod.insts[Inst]
        if Obj.Type == Type:
            Out,Ins = getConns(Inst,Mod)
            Insts[Out] = (Inst,Ins)
    return Insts 

def extractCmosMux(Mod):
    Insts = []
    for Inst in Mod.insts:
        Obj  = Mod.insts[Inst]
        if Obj.Type == 'cmos':
            I = Obj.conns['i']
            O = Obj.conns['o']
            Gn = Obj.conns['gn']
            Gp = Obj.conns['gp']
            Insts.append((Inst,I,O,Gn,Gp))
    Muxes = []
    while Insts!=[]:
        (Inst0,I0,O0,Gn0,Gp0) = Insts.pop(0)
        for ind,(Inst1,I1,O1,Gn1,Gp1) in enumerate(Insts):
            if (Gn0==Gp1)and(Gn1==Gp0):
                Found = True
                if (I0==I1):
                    Mod.add_inst_conns('mux2','mux_'+I0,[('o',I0),('i0',O0),('i1',O1),('s0',Gn0),('s1',Gp0)])
                elif (I0==O1):
                    Mod.add_inst_conns('mux2','mux_'+I0,[('o',I0),('i0',O0),('i1',I1),('s0',Gn0),('s1',Gp0)])
                elif (O0==I1):
                    Mod.add_inst_conns('mux2','mux_'+O0,[('o',O0),('i0',I0),('i1',O1),('s0',Gn0),('s1',Gp0)])
                elif (O0==O1):
                    Mod.add_inst_conns('mux2','mux_'+O0,[('o',O0),('i0',I0),('i1',I1),('s0',Gn0),('s1',Gp0)])
                else:
                    Found = False
                if Found:
                    Insts.pop(ind)
                    Mod.insts.pop(Inst0)
                    Mod.insts.pop(Inst1)


def Dlatch( Dict,Insts,Mod):
    logs.log_info('dlatch %s %s'%(Insts,Dict))
    if Dict['?N4'] == Dict['?N40']:
        Din = Dict['?N41']
        Clk = Dict['?S1']
    elif Dict['?N4'] == Dict['?N41']:
        Din = Dict['?N40']
        Clk = Dict['?S0']
    if Dict['?N6']==Dict['?N2']:
        RB = Dict['?N3']
    elif Dict['?N6']==Dict['?N3']:
        RB = Dict['?N2']

    Mod.add_inst_conns('dlatch',invent_inst('dlatch'),[('qn',Dict['?N1']),('q',Dict['?N6']),('d',Din),('rb',RB),('clk',Clk)])
    for Inst in Insts: Mod.insts.pop(Inst)

def Dlatch3( Dict,Insts,Mod):
    logs.log_info('dlatch3 %s %s'%(Insts,Dict))
    if Dict['?N1']==Dict['?N40']:
        Din = Dict['?N41']
        Clk = Dict['?S1']
    elif Dict['?N1']==Dict['?N41']:
        Din = Dict['?N40']
        Clk = Dict['?S0']

    if Dict['?N6']==Dict['?N2']:
        RB = Dict['?N3']
    elif Dict['?N6']==Dict['?N3']:
        RB = Dict['?N2']
    Mod.add_inst_conns('dlatch',invent_inst('dlatch'),[('qn',''),('q',Dict['?N6']),('d',Din),('rb',RB),('clk',Clk)])
    for Inst in Insts: Mod.insts.pop(Inst)

def Dlatch2( Dict,Insts,Mod):
    logs.log_info('dlatch2 %s %s'%(Insts,Dict))
    Dont = False
    if Dict['?Ny']==Dict['?N1']:
        RB = Dict['?Ny']
        Din = Dict['?Nz']
    elif Dict['?Nz']==Dict['?N1']:
        RB = Dict['?Nz']
        Din = Dict['?Ny']
    elif Dict['?Ny']==Dict['?N2']:
        RB = Dict['?Ny']
        Din = Dict['?Nz']
    elif Dict['?Nz']==Dict['?N2']:
        RB = Dict['?Nz']
        Din = Dict['?Ny']
    else:
        logs_error("Dlatch2 %s %s %s %s %s"%(Dict['?Ny'],Dict['?Nz'],Dict['?N1'],Dict['?N2']))
        Din = 'ERROR'
        RB = 'ERROR'
        Dont = True


    if Dict['?Nx']==Dict['?N20']:
        Clk = Dict['?S0']
    elif Dict['?Nx']==Dict['?N21']:
        Clk = Dict['?S1']

    Mod.add_inst_conns('dlatch',invent_inst('dlatch'),[('qn',Dict['?QB']),('q',Dict['?Q']),('d',Din),('rb',RB),('clk',Clk)])
    for Inst in Insts: Mod.insts.pop(Inst)

def Dff(Dict,Insts,Mod):
    logs.log_info('Dff %s %s'%(Insts,Dict))

    Mod.add_inst_conns('dff',invent_inst('dff'),[('mid',Dict['?Q0']),('midn',Dict['?QN0']),('qn',Dict['?QN']),('q',Dict['?Q']),('d',Dict['?D0']),('rb',Dict['?RB']),('clk',Dict['?C1'])])
    for Inst in Insts: Mod.insts.pop(Inst)

def tryXor(Dict,Insts,Mod):
    if Dict['?Nnd']=='vss':
        ShareN = Dict['?Nns']
    elif Dict['?Nns']=='vss':
        ShareN = Dict['?Nnd']
    else:
        return
    if Dict['?Npd']=='vdd':
        ShareP = Dict['?Nps']
    elif Dict['?Nps']=='vss':
        ShareP = Dict['?Npd']
    else:
        return
    if ShareN!=ShareP: return
    Gaten = buildFunction(Dict['?Nng'],Mod)
    Gatep = buildFunction(Dict['?Npg'],Mod)
    if (not Gaten)or(not Gatep): return
    Mapping0 = {}
    Ok0 = logicMatcher(Gaten,Mapping0,XNOR0function)
    Mapping1 = {}
    Ok1 = logicMatcher(Gatep,Mapping1,XNOR1function)
    if Ok0 and Ok1 and (Mapping0==Mapping1):
        Xnor = invent_inst('xnor')
        Mod.add_inst_conns('xnor',Xnor,[('o',ShareP)])
        ind = 0;
        for Key in Mapping0:
            In = Mapping0[Key]
            Mod.add_conn(Xnor,'i%s'%ind,In)
            ind += 1
        for Inst in Insts: 
            Obj = Mod.insts[Inst]
            if Obj.Type in PMOS+NMOS:
                Mod.insts.pop(Inst)

Dlatch3_pattern = (
    ('mux2 i0=?N40 i1=?N41 o=?N6 s0=?S0 s1=?S1'
    ,'and o=?N1 i0=?N2 i1=?N3'
    ,'! anyone ?N1 ?N40 ?N41'
    ,'! anyone ?N6 ?N2 ?N3')
    ,Dlatch3)

Dlatch_pattern = ( 
    ('nand o=?N1 i0=?N2 i1=?N3'
    ,'inv  i=?N1 o=?N4'
    ,'mux2 i0=?N40 i1=?N41 o=?N6 s0=?S0 s1=?S1'
    ,'! anyone ?N4 ?N40 ?N41'
    ,'! anyone ?N6 ?N2 ?N3'),Dlatch)

Dlatch2_pattern = (
    (
     'mux2 i0=?N20 i1=?N21 o=?N4 s0=?S0 s1=?S1'
    ,'inv  i=?N4 o=?Q'
    ,'nand o=?QB i0=?N1 i1=?N2'
    ,'! anyone ?Q ?N1 ?N2'
    ,'! anyone ?QB ?N20 ?N21'
    ,'nand o=?Nx i0=?Ny i1=?Nz'
    ,'! anyone ?Nx ?N20 ?N21'
    ),Dlatch2)
    
Dff_pattern = ( (
     'dlatch  clk=?C0 d=?D0 q=?Q0 qn=?QN0 rb=?RB' 
    ,'dlatch  clk=?C1 d=?D1 q=?Q qn=?QN rb=?RB' 
    ,'! anyone ?D1 ?Q0 ?QN0'
    ,'! different ?C0  ?C1'
    ),Dff)

XOR_pattern = ((
    'pmos g=?Npg s=?Nps d=?Npd b=?Npb'
    ,'! anyone ?Npb ?Nps ?Npd'

    ,'nmos g=?Nng s=?Nns d=?Nnd b=?Nnb'
    ,'! anyone ?Nnb ?Nns ?Nnd'

    ,'! different ?Npg ?Nng'

    ,'! share  ?Nps ?Npd | ?Nns ?Nnd'

    ),tryXor)

def recognizePattern2(Pattern,Mod):
    Job = Pattern[1]
    Dic = {}
    LL = list(Pattern[0])
    lookForMatch2(LL,Dic,[],Job,Mod)


def lookForMatch2(LL,Dic,Insts,Job,Mod):
    Dones = 0
    if LL==[]: 
        usePattern(Dic,Job,Insts,Mod)
        return Dones+1
    Look = LL[0]
    Wrds = string.split(Look)
    if Wrds[0]=='!':
        GotIt = False
        Copy = copyDict(Dic)
        if Wrds[1]=='anyone':
            Base = Wrds[2]
            Vbase = Dic[Base]
            for Wrd in Wrds[3:]:
                if Vbase == Dic[Wrd]:
                    GotIt = True
        elif Wrds[1]=='different':
            Copy = copyDict(Dic)
            AA = Dic[Wrds[2]]
            BB = Dic[Wrds[3]]
            if AA!=BB:
                GotIt = True
        elif Wrds[1]=='share':
            Grp0,Grp1 = splitGroups(Wrds[2:])
            GotIt =  shareSomething(Grp0,Grp1,Dic)
        else:
            logs.log_error('lookForMatch2 go %s'%str(LL))
        if GotIt:
             Dones += lookForMatch2(LL[1:],Dic,Insts,Job,Mod)
    else:
        Keys = Mod.insts.keys()
        for Inst in Keys:
            if (Inst in Mod.insts)and(Inst not in Insts):
                Obj = Mod.insts[Inst]
                if matchingType(Obj.Type,Wrds[0]):
                    Copy = copyDict(Dic)
                    Fail = False
                    for Wrd in Wrds[1:]:
                        PinTag = string.split(Wrd,'=')
                        [Pin,Tag] = PinTag
                        Sig = Obj.conns[Pin]
                        if not isMatch(Sig,Tag,Copy,Mod): 
                            Fail = True
                    if not Fail:
                        Dones += lookForMatch2(LL[1:],Copy,Insts+[Inst],Job,Mod)
    return 0

def matchingType(Type,Pattern):
    if Type==Pattern: return True
    if (Type in PMOS)and(Pattern=='pmos'): return True
    if (Type in NMOS)and(Pattern=='nmos'): return True
    return False



Instances = {}
def invent_inst(Base):
    if Base not in Instances: Instances[Base]=0
    Inst = '%s_%s'%(Base,Instances[Base])
    Instances[Base] += 1
    return Inst


def splitGroups(List):
    Grp0,Grp1 = [],[]
    state = 'first'
    for Item in List:
        if state=='first':
            if Item=='|': state='second'
            else:
                Grp0.append(Item)
        elif state=='second':
            Grp1.append(Item)
    return Grp0,Grp1
            
def shareSomething(Grp0,Grp1,Dic):
    GV0 = []
    for Key in Grp0:
        Val = Dic[Key]
        GV0.append(Val) 
    for Key in Grp1:
        Val = Dic[Key]
        if Val in GV0: return Val
    return False
    
def buildFunction(Net,Mod):
    Mod.prepareNetTable()
    Funcs = {}
    Func = buildFunctionDeep(Net,Funcs,Mod)
    return Func

def buildFunctionDeep(Net,Funcs,Mod):
    Dir,_ = Mod.nets[Net]
    if 'input' in Dir: return Net
    if Net in ['vdd','vss']: return Net
    if Net not in Mod.netTable: return Net
    if Net in Funcs: return Funcs[Net]
    Conns = Mod.netTable[Net]
    for Inst,Type,Pin in Conns:
        if (Pin=='o')and(Type in LOGICALS):
            Lins = []
            Obj = Mod.insts[Inst]
            for Pin in Obj.conns:
                if Pin!='o':
                    In = Obj.conns[Pin]
                    Fin = buildFunctionDeep(In,Funcs,Mod)
                    Lins.append(Fin)
            Lins.sort()
            return [Type] + Lins
        elif (Pin=='o')and(Type == 'mux2'):
            return Net




    logs.log_error('FAILED buildFunctionDeep "%s" %s'%(Net,Conns))
    return 'ERROR'

def logicMatcher(Func,Dict,Pattern):
    if (Func==[])and(Pattern==[]): return True
    if (type(Func) is str)and(type(Pattern) is str):
        if (Pattern in Dict)and(Func!=Dict[Pattern]): 
            return False
        Dict[Pattern]=Func
        return True

    if (not Func) or (Func[0]!=Pattern[0]): 
        return False
    if len(Func)!=len(Pattern): 
        return False
    for ind,Fitem in enumerate(Func[1:]):
        Pitem = Pattern[ind+1]
        if not logicMatcher(Fitem,Dict,Pitem): return False
    return True
    
XNOR0function = ['or', ['and', ['inv', 'ia'], ['inv', 'ib']], ['and', 'ia', 'ib']]
XNOR1function = ['and', ['or', ['inv', 'ia'], 'ib'], ['or', ['inv', 'ib'], 'ia']]


VERFUNC = {'and':'&','or':'|','inv':'~','xor':'^','xnor':':','nand':'&','nor':'|','buf':''}
VERPREF = ['nand','nor','xnor']

def turnGatesToAssigns(Mod):
    Assigns = {}
    Translates = []
    Insts = Mod.insts.keys()
    for Inst in Insts:
        Obj = Mod.insts[Inst]
        if Obj.Type in LOGICALS+['buf']:
            Out,Ins = getConns(Inst,Mod)
            Head = VERFUNC[Obj.Type]
            Func = [Head]+Ins
            if Obj.Type in VERPREF:
                Func = ['!',Func]

            Sfunc = str(Func)
            if Sfunc in Assigns:
                Translates.append((Out,Assigns[Sfunc]))
            elif (Obj.Type=='buf'):
                Mod.add_hard_assign(Out,Ins[0])
                Assigns[Ins[0]] = Out
            else:
                Mod.add_hard_assign(Out,Func)
                Assigns[Sfunc] = Out
            Mod.insts.pop(Inst)
    useTranslations(Translates,Mod,True)


def ncInverters(Mod):
    Mod.prepareNetTable()
    Keys = Mod.insts.keys()
    for Nc in Keys:
        if Mod.insts[Nc].Type in ['mimcap_woum_1p5_sin_rf','nc2']:
            Cap = Mod.insts[Nc].conns['pin0']
            WhoList = Mod.netTable[Cap]
            for Inst,Type,Pin in WhoList:
                if (Type=='inv')and(Pin=='o'):
                    Obj = Mod.insts[Inst]
                    Obj.Type = 'cap_inv'
                    Mod.insts.pop(Nc)
                elif (Type=='cross_mos')and(Pin[0]=='q'):
                    Obj = Mod.insts[Inst]
                    Obj.Type = 'cap_cross_mos'
                    Mod.insts.pop(Nc)
                elif (Type=='cap_cross_mos')and(Pin[0]=='q'):
                    Mod.insts.pop(Nc)
                    
            
    



def consecutiveInverters(Mod):
    InvsO={}
    InvsI={}
    for Inst in Mod.insts:
        if Mod.insts[Inst].Type=='nc2':
            return
        elif Mod.insts[Inst].Type=='inv':
            O = Mod.insts[Inst].conns['o']
            I = Mod.insts[Inst].conns['i']
            InvsO[O] = (Inst,I)
            InvsI[I] = (Inst,O)
    for OO in InvsO.keys():
        Deep,II = travelBack(OO,InvsO,0)
        if Deep==1:
            pass
        elif (Deep & 1)==1:
            Inv,_ = InvsO[OO]
            Mod.insts[Inv].conns['i']=II
        elif (Deep & 1)==0:
            Inv,_ = InvsO[OO]
            Mod.insts[Inv].conns['i']=II
            Mod.insts[Inv].Type='buf'




def travelBack(OO,InvsO,Deep):
    _,II = InvsO[OO]
    if II not in InvsO: return Deep+1,II
    return travelBack(II,InvsO,Deep+1)


