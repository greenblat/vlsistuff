
import string
import sys
import logs

PMOS =  ['pdmos_tran','pmos_tran','pmos']
NMOS =  ['ndmos_tran','nmos_tran','nmos']
VDDRENAMES = [('VDDA','vdd'),('VSSA','vss'),('vdd30_to_dm','vdd'),('vdd33','vdd'),('vdd30','vdd'),('dvss','vss'),('dvddh','vdd'),('dvdd','vdd'),('avddh','vdd'),('avss','vss')]
VDDS = {}

LOGICALS = ('and or nand nor inv xor xnor buf').split()
COMPLEXS = ['mux2','srlatch','latch']
Dbg = False
Dbg = True

def help_main(Env):
    Env.DontFlattens.extend(['nmos_tran','pmos_tran'])
    Mod = Env.Current
    Mod.nets['vdd'] = ('wire',0)
    Mod.nets['vss'] = ('wire',0)
    TR = []
    for Log in LOGICALS: TR.append((Log,Log+'net'))
    useTranslations(TR,Mod,True)
    writeOut(Mod,'stp0',Dbg)
    DIRS,BUSSED = removeBusses(Mod)
    extractPowers(Mod)
    orientSimpleMoses(Mod)
    writeOut(Mod,'stp1',Dbg)
    sameTrans(Mod)
    writeOut(Mod,'stp1a',Dbg)
    tieLowHigh(Mod)
    writeOut(Mod,'stp2a',Dbg)
    shortMos(Mod)
    writeOut(Mod,'stp2',Dbg)

    stupidSerials(Mod)
    orientSimpleMoses(Mod)
    writeOut(Mod,'stp2c',Dbg)

    splitDesignClusters(Mod)
    simpleInverters(Mod)
    simpleCmos(Mod)
    orphanWires(Mod)
    writeOut(Mod,'xmod',Dbg)



    simpleInverters(Mod)
    followInvs(Mod)
    simpleNands(Mod)
    simpleTinvs(Mod)
    simpleCmos(Mod)
    simpleLatches(Mod)
    followAndsOrs(Mod)
    writeOut(Mod,'stp3',Dbg)
    simpleParallels(Mod,'nmos','or')
    simpleParallels(Mod,'pmos','and')
    writeOut(Mod,'stp4a',Dbg)
    simpleSerials(Mod,'nmos','and')
    simpleSerials(Mod,'pmos','or')
    writeOut(Mod,'stp4b',Dbg)
    simpleParallels(Mod,'nmos','or')
    simpleParallels(Mod,'pmos','and')
    writeOut(Mod,'stp4c',Dbg)
    simpleSerials(Mod,'nmos','and')
    simpleSerials(Mod,'pmos','or')
    writeOut(Mod,'stp4',Dbg)



    simpleMergeSames(Mod,'and')
    simpleMergeSames(Mod,'or')
    writeOut(Mod,'stp4a',Dbg)
    simpleMergeSames(Mod,'inv')
    followAndsOrs(Mod)
    writeOut(Mod,'stp5',Dbg)
    simpleInverters(Mod)
    followInvs(Mod)
    crossMos(Mod)
    writeOut(Mod,'stp6',Dbg)
    simpleMergeFollows(Mod,'and')
    simpleMergeFollows(Mod,'or')

    simpleMergeSames(Mod,'and')
    simpleMergeSames(Mod,'or')
    simpleInverters(Mod)
    writeOut(Mod,'stp6a',Dbg)
    removeOrphans(Mod,True)
    writeOut(Mod,'stp6b',Dbg)
    followAndsOrs(Mod)
    writeOut(Mod,'stp7',Dbg)
    assignPortDirs(Mod)
    writeOut(Mod,'stp8',Dbg)
    simpleCmos(Mod)
    cmosAnd(Mod)
    writeOut(Mod,'stp9',Dbg)
    orphanWires(Mod)
    writeOut(Mod,'stp10',Dbg)
    srLatch1(Mod)
    writeOut(Mod,'stp11',Dbg)
    assignPortDirs(Mod)
    complexMux(Mod)
    cmosMux(Mod)
    finalTristate(Mod)
    writeOut(Mod,'stp12',Dbg)

    restoreBusses(Mod,BUSSED,DIRS)
    useVssVdd(Mod)
    writeOut(Mod,'stp13',Dbg)
    reportMap(Mod)
    turnGatesToAssigns(Mod)
    writeOut(Mod,'stp14',Dbg)
    turnMosesToAssigns(Mod)
    retypePrimitives(Mod)
    writeOut(Mod,'newv',True)

import spiceMatcher
def splitDesignClusters(Mod):
    Mod.prepareNetTable()
    Clusters = []
    Used= []

    for Mos in Mod.insts:
        Obj = Mod.insts[Mos]
        if (Obj.Type in  ('nmos','pmos'))and (Mos not in Used):
            S = Obj.conns['s']
            D = Obj.conns['d']
            All = travelMosSD([S,D],[Mos],Mod)
            Used.extend(All)
            Clusters.append(All)
    logs.log_info('design split into %d clusters'%len(Clusters))
    for Clust in Clusters:
        Nmoses,Pmoses = clusterPattern(Clust,Mod)
        LogicFunc = spiceMatcher.tryMatchLogicFunc(Nmoses,Pmoses)
        if LogicFunc:
            Npaths,Ppaths = LogicFunc
            for Inst in Clust: Mod.insts.pop(Inst)
            Inst = inventInst('logicgate')
            Conns = []
            Mod.add_inst_conns('logicgate',Inst,Conns)
            Mod.add_inst_param(Inst,'func0',str(Npaths))
            Mod.add_inst_param(Inst,'func1',str(Ppaths))
        else:
            Recognized = spiceMatcher.matchCluster(Nmoses,Pmoses)
            if Recognized:
                for Inst in Clust:
                    Mod.insts.pop(Inst)
                for Objx in Recognized:
                    Mod.add_inst_conns(Objx.Type,inventInst(Objx.Type),Objx.Conns)
            else:
                Clust2 = spiceMatcher.matchBasics(Nmoses,Pmoses)
                logs.log_info('FAILED clust\n',2)
                for Key in Clust2:
                    for Item in Clust2[Key]:
                        logs.log_info('%s : %s'%(Key,Item),2)
#                for Mos in Nmoses:
#                    logs.log_info('    %s'%Mos,2)
#                logs.log_info('',2)
#                for Mos in Pmoses:
#                    logs.log_info('    %s'%Mos,2)
                logs.log_info('\n\n\n',2)
                
                

def clusterPattern(Clust,Mod):
    def signatureMos(Obj):
        Str = ' %s %s %s %s'%(Obj.Type,Obj.conns['g'],Obj.conns['s'],Obj.conns['d'])
        return Str


    Ns = []
    Ps = []
    for Mos in Clust:
        Obj = Mod.insts[Mos]
        if Obj.Type == 'nmos': Ns.append(signatureMos(Obj))
        if Obj.Type == 'pmos': Ps.append(signatureMos(Obj))
    Pattern = Ns,Ps
    return Pattern


def travelMosSD(Nets,Moses,Mod):
    if Nets==[]: return Moses
    Dnets = []
    Dmoses = []
    for Net in Nets:
        if (Net not in ['vss','vdd']):
            for (Inst,Type,Pin) in Mod.netTable[Net]:
                if (Type in ('nmos','pmos'))and(Pin in ('s','d'))and(Inst not in Moses)and(Inst not in Dmoses):
                    S = Mod.insts[Inst].conns['s']
                    D = Mod.insts[Inst].conns['d']
                    if (S not in ['vss','vdd']):Dnets.append(S) 
                    if (D not in ['vss','vdd']):Dnets.append(D) 
                    Dmoses.append(Inst)
    return travelMosSD(Dnets,Dmoses+Moses,Mod)        




            


def dumpNeural(Mod):
    Fout = open('%s.neural'%Mod.Module,'w')
    Renames = {}
    logs.setVar('int_code',100)
    logs.setVar('ext_code',1000)
    def codeit(Net):
        if Net=='vdd': return 20000
        if Net=='vss': return 10000
        if Net in Renames: return Renames[Net]
        if internalNet(Net,Mod):
            Code = logs.getVar('int_code')
            logs.setVar('int_code',Code+1)
            Renames[Net] = Code
            return Code
        else:
            Code = logs.getVar('ext_code')
            logs.setVar('ext_code',Code+1)
            Renames[Net] = Code
            return Code

    for Nmos in Mod.insts:
        Obj = Mod.insts[Nmos]
        if Obj.Type=='nmos':
            Fout.write('1 %d %d %d '%(codeit(Obj.conns['g']),codeit(Obj.conns['s']),codeit(Obj.conns['d'])))

    for Pmos in Mod.insts:
        Obj = Mod.insts[Pmos]
        if Obj.Type=='pmos':
            Fout.write('2 %d %d %d '%(codeit(Obj.conns['g']),codeit(Obj.conns['s']),codeit(Obj.conns['d'])))
    Fout.write('\n')
    for Net in Renames:
        Fout.write('# %s %d\n'%(Net,Renames[Net]))
    Fout.close()






def stupidSerials(Mod):
    for II in range(3):
        Mod.prepareNetTable()
        for Net in Mod.netTable:
            Conns = Mod.netTable[Net]
            if internalNet(Net,Mod)and(len(Conns)==2):
                Inst0 = Conns[0][0]
                Inst1 = Conns[1][0]
                print('>>>>>>',Net,Inst0,Inst1)
                if (Conns[0][1]==Conns[1][1])and(Conns[0][1] in ('nmos','pmos')):
                    if (Inst0 in Mod.insts)and(Inst1 in Mod.insts):
                        G0 = Mod.insts[Inst0].conns['g']
                        G1 = Mod.insts[Inst1].conns['g']
                        if (G0==G1):
                            I0 = otherNet(Inst0,Conns[0][2],Mod)
                            I1 = otherNet(Inst1,Conns[1][2],Mod)
                            Mod.add_inst_conns(Conns[0][1],Inst0+'_'+Inst1,[('g',G0),('s',I0),('d',I1),('b',Mod.insts[Inst0].conns['b'])])
                            Mod.insts.pop(Inst0)
                            Mod.insts.pop(Inst1)
        

def retypePrimitives(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == 'nmos' : Obj.Type = 'nmos_gate'
        if Obj.Type == 'pmos' : Obj.Type = 'pmos_gate'
        if Obj.Type == 'cmos' : Obj.Type = 'cmos_gate'
        
def reportMap(Mod):
    Mod.prepareNetTable()
    Maps = makeMap(Mod)
    for Net in Mod.netTable:
        if Net in Maps:
            logs.log_info('MAP %s %s %s'%(Net,Maps[Net],Mod.netTable[Net]))

def help_main_old(Env):
    Mod = Env.Current
    writeOut(Mod,'stp0',Dbg)
    useTranslations(VDDRENAMES,Mod,True)
    extractPowers(Mod)
    writeOut(Mod,'stp1',Dbg)
    removeBusses(Mod)

    Ok = 1
    while (Ok>0):
        Ok = scanDesignForPattern(Mod)
    Ok = 1
    while (Ok>0):
        Ok = scanDesignForPattern(Mod)
    writeOut(Mod,'stp2',Dbg)
    recognizePattern2(InvInv_pattern,Mod)
    removeOrphans(Mod)
    writeOut(Mod,'stp3',Dbg)
    gateMerges(Mod)
    writeOut(Mod,'stp4',Dbg)
    orphanWires(Mod)
    writeOut(Mod,'stp5',Dbg)
    recognizeSRlatch(Mod)
    extractCmosMux(Mod)
    writeOut(Mod,'stp6',Dbg)
    recognizePattern2(XOR_pattern,Mod)
    gateMerges(Mod)
    removeOrphans(Mod)

    recognizePattern2(Dlatch_pattern,Mod)
    writeOut(Mod,'stp7',Dbg)
    recognizePattern2(Dlatch2_pattern,Mod)
    recognizePattern2(Dlatch3_pattern,Mod)
    writeOut(Mod,'stp8',Dbg)
    recognizePattern2(Dff_pattern,Mod)
    writeOut(Mod,'stp9',Dbg)
    scanGates(Mod,True)
    orphanWires(Mod)
    ncInverters(Mod)
    writeOut(Mod,'stp10',Dbg)
    consecutiveInverters(Mod)
    removeOrphans(Mod)
    writeOut(Mod,'stp11',Dbg)
    renameBackToOriginalVdd(Mod)
    turnGatesToAssigns(Mod)
    writeOut(Mod,'newv')

def writeOut(Mod,Ext = 'v',Dbg=True):
    if not Dbg: return
    Fout = open('%s.%s'%(Mod.Module,Ext),'w')
    Mod.dump_verilog(Fout)
    Fout.close()

def register(Dir,Key,Val):
    if Key not in Dir: 
        Dir[Key]=[Val]
    else:
        Dir[Key].append(Val)


def net_is_external(Sig,Mod):
    Dir,Wid = Mod.nets[Sig]
    return is_external_dir(Dir)

def is_external_dir(Dir):
    return ('input' in Dir)or('output' in Dir)or('inout' in Dir)

def useVssVdd(Mod):
    Mod.prepareNetTable()
    if 'vss' in Mod.netTable:
        for (Inst,Type,Pin) in Mod.netTable['vss']:
            Mod.insts[Inst].conns[Pin] = ('bin',1,0)
    if 'vdd' in Mod.netTable:
        for (Inst,Type,Pin) in Mod.netTable['vdd']:
            Mod.insts[Inst].conns[Pin] = ('bin',1,1)



def assignPortDirs(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type in LOGICALS:
            Out = Obj.conns['o']
            Dir,Wid = Mod.nets[Out]
            if Dir=='inout': 
                Mod.nets[Out] = ('output',Wid)
    Mod.prepareNetTable()
    for Net in Mod.netTable:
        Dir,Wid = Mod.nets[Net]
        if Dir=='inout': 
            Dir = 'input'
            for (Inst,Type,Pin) in Mod.netTable[Net]:
                if Type not in LOGICALS:
                    Dir = 'inout'
        
            Mod.nets[Net] = (Dir,Wid)
            
def gsd(Obj):
     G = Obj.conns['g']
     S = Obj.conns['s']
     D = Obj.conns['d']
     return G,S,D
    
def crossMos(Mod):
    Pkeys,Nkeys = {},{}
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == 'pmos':
            G,S,D = gsd(Obj)
            register(Pkeys,G,(Inst,S,D))
        if Obj.Type == 'nmos':
            G,S,D = gsd(Obj)
            if D=='vss':
                register(Nkeys,S,(Inst,G))
    
    for G1 in Pkeys:
        Inst1,S1,D1 = Pkeys[G1][0]
        if S1 in Pkeys:
            Inst2,S2,D2 = Pkeys[S1][0]
            Found = True
            if   (S1==S2):  Up,Down1,Down2 =S1,D1,D2
            elif (S1==D2):  Up,Down1,Down2 =S1,D1,S2
            elif (D1==S2):  Up,Down1,Down2 =D1,S1,D2
            elif (D1==D2):  Up,Down1,Down2 =D1,S1,S2
            else: Found=False
                
            if Found and (Inst1 in Mod.insts):
                if (Down1 in Nkeys)and(Down2 in Nkeys):
                    Nmos1,NG1 = Nkeys[Down1][0]
                    Nmos2,NG2 = Nkeys[Down2][0] 
                    Inv1 = inventInst('inv')
                    Inv2 = inventInst('inv')
                    Mod.add_inst_conns('inv',Inv1,[('i',NG1),('o',Down1)])
                    Mod.add_inst_conns('inv',Inv2,[('i',NG2),('o',Down2)])
                    print('>>>>',NG1,NG2,Down1,Down2)                            
                    removeInsts([Nmos1,Nmos2,Inst1,Inst2],Mod)
                
            





def shortMos(Mod):
    Remove = []
    Translates = []
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == 'nmos':
             G,S,D = gsd(Obj)
             if (G==S)or(G==D):
                if (S=='vss')or net_is_external(S,Mod): 
                    Translates.append((D,S))
                else:
                    Translates.append((S,D))
                Remove.append(Inst) 
        if Obj.Type == 'pmos':
             G,S,D = gsd(Obj)
             if (G==S)or(G==D):
                if (S=='vdd')or net_is_external(S,Mod): 
                    Translates.append((D,S))
                else:
                    Translates.append((S,D))
                Remove.append(Inst) 
    removeInsts(Remove,Mod)
    useTranslations(Translates,Mod,True)

def simpleMergeFollows(Mod,Kind):
    Dones = 1
    while Dones>0:
        Dones = simpleMergeFollowsRound(Mod,Kind)

def simpleMergeFollowsRound(Mod,Kind):
    Keys = {}
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == Kind:
            Out,Ins = getConns(Inst,Mod)
            Ins.sort()
            register(Keys,Out,(Inst,Ins))
    dones = 0 
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == Kind:
            Out,Ins = getConns(Inst,Mod)
            for In in Ins:
                if In in Keys:
                    Val = Keys[In]
                    More = Val[0][1]
                    Ins2 = Ins[:]
                    Ins2.remove(In)
                    Ins2.extend(More)
                    Conns = {}
                    Conns['o'] = Out
                    for ind,In in enumerate(Ins2): Conns['i%d'%ind] = In
                    Obj.conns = Conns
                    dones += 1
    return dones

def renumerate(Ins):
    Ins.sort()
    Res = []
    for ind,In in enumerate(Ins):
        Res.append(('i%d'%ind,In))
    return Res



def simpleMergeSames(Mod,Kind):
    Keys = {}
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == Kind:
            Out,Ins = getConns(Inst,Mod)
            Ins.sort()
            Key = tuple(Ins)
            register(Keys,Key,(Inst,Out))
    Translates = []
    for Key in Keys:
        LL = Keys[Key]
        if len(LL)>1:
            Out0 = LL[0][1]
            for Inst,Out1 in LL[1:]:
                Translates.append((Out1,Out0))
                Mod.insts.pop(Inst)
    useTranslations(Translates,Mod)


def srLatch1(Mod):
    Invs = {} 
    Pvdds =  {}
    Nvsss =  {}
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == 'inv':
            I = Obj.conns['i']
            O = Obj.conns['o']
            register(Invs,I,(O,Inst))
            register(Invs,O,(I,Inst))
        if (Obj.Type == 'nmos')and(Obj.conns['d']=='vss'):
            register(Nvsss,Obj.conns['s'],(Obj.conns['g'],Inst))
        if (Obj.Type == 'pmos')and(Obj.conns['d']=='vdd'):
            register(Pvdds,Obj.conns['s'],(Obj.conns['g'],Inst))

    for Net in Invs:
        if (Net in Pvdds)and(Net in Nvsss)and(len(Invs[Net])>1):
            Other  = Invs[Net][1][0]
            if Other in Invs:
                Set = Nvsss[Net][0][0]
                Clr = Pvdds[Net][0][0]
                New = inventInst('srlatch')
                Mod.add_inst_conns('srlatch',New,[('qn',Net),('q',Other),('set',Set),('clrn',Clr)])
                Mod.insts.pop(Nvsss[Net][0][1])
                Mod.insts.pop(Pvdds[Net][0][1])
                Mod.insts.pop(Invs[Net][0][1])
                Mod.insts.pop(Invs[Net][1][1])
                makeOut(Other,Mod)
                makeOut(Net,Mod)

def makeOut(Net,Mod):
    Dir,Wid = Mod.nets[Net]
    if Dir=='inout':
        Mod.nets[Net] = 'output',Wid


            
def cmosAnd(Mod):
     Pgates = {}
     Ngates = {}
     for Inst in Mod.insts:
         Obj = Mod.insts[Inst]
         if Obj.Type == 'cmos':
             Pg = Obj.conns['gp']
             Ng = Obj.conns['gn']
             I = Obj.conns['i']
             O = Obj.conns['o']
             register(Pgates,Pg,(I,O,Inst))        
             register(Ngates,Ng,(I,O,Inst))        
     Remove = []
     for Inst in Mod.insts:
         Obj = Mod.insts[Inst]
         if Obj.Type == 'nmos':
             G,S,D = gsd(Obj)
             if (G in Pgates)and(D=='vss'):
                 I,O,Cmos = Pgates[G][0]
                 if (I==S):
                     In0,O0 = O,I
                 elif (O==S):
                     In0,O0 = I,O
                 else:
                     In0,O0 = False,False
                 if In0:                    
                     Minst = inventInst('and')
                     Gn = Mod.insts[Cmos].conns['gn']
                     Mod.add_inst_conns('and',Minst,[('o',O0),('i0',In0),('i1',Gn)])
                     Mod.insts.pop(Cmos)
                     Remove.append(Inst)
         if Obj.Type == 'pmos':
             G,S,D = gsd(Obj)
             if (G in Ngates):
                 I,O,Cmos = Ngates[G][0]
                 if (I in [D,S]):
                     In0,O0 = O,I
                 elif (O in [D,S]):
                     In0,O0 = I,O
                 else:
                     In0,O0 = False,False
                     
                 if In0:                    
                     Minst = inventInst('and')
                     Gp = Mod.insts[Cmos].conns['gp']
                     Mod.add_inst_conns('or',Minst,[('o',O0),('i0',In0),('i1',Gp)])
                     Mod.insts.pop(Cmos)
                     Remove.append(Inst)
     removeInsts(Remove,Mod)



def simpleSerials(Mod,Mos,Kind):
    Dones = 1
    while Dones>0:
        Dones = simpleSerialsRound(Mod,Mos,Kind)


def simpleSerialsRound(Mod,Mos,Kind):
    Keys = {}
    Mod.prepareNetTable()

    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == Mos:
            G,S,D = gsd(Obj)
            B = Obj.conns['b']
            register(Keys,S,(Inst,G,D,B))
            register(Keys,D,(Inst,G,S,B))
    dones = 0        
    for Net in Keys:
        LL = Keys[Net]
        if (len(LL)==2) and (not net_is_external(Net,Mod)) and (len(Mod.netTable[Net])==2):
            if (LL[0][0] in Mod.insts)and(LL[1][0] in Mod.insts):
                Mod.insts.pop(LL[0][0])
                Mod.insts.pop(LL[1][0])
                G0 = LL[0][1]
                G1 = LL[1][1]
                Minst = inventInst('%s_%s'%(Kind,Mos))
                if G1!=G0:
                    NewGate = inventInst('g_%s_%s'%(Kind,Mos))
                    Conns = [('o',NewGate),('i0',G0),('i1',G1)]
                    Inst = inventInst('%s_%s'%(Kind,Mos))
                    Mod.add_inst_conns(Kind,Inst,Conns)
                else:
                    NewGate = G0
                NewS = LL[0][2]
                NewD = LL[1][2]
                NewB = LL[0][3]
                if NewS==NewB:
                    NewS = LL[1][2]
                    NewD =  LL[0][2]
                Mod.add_inst_conns(Mos,Minst,[('g',NewGate),('s',NewS),('d',NewD),('b',NewB)])
                dones +=1
                        
    return dones


def tieLowHigh(Mod):
    Pkeys = {}
    Nkeys = {}
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == 'pmos':
            G,S,D = gsd(Obj)
            if (G==S)and(D=='vdd'):
                register(Pkeys,G,Inst)
            
        if Obj.Type == 'nmos':
            G,S,D = gsd(Obj)
            if (G==S)and(D=='vss'):
                register(Nkeys,G,Inst)
    Remove,Translates = [],[]
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == 'pmos':
            G,S,D = gsd(Obj)
            if (D=='vdd')and(G in Nkeys):
                Translates.append((S,'vdd'))
                Remove.append(Inst)
                Remove.append(Nkeys[G][0])
            
        if Obj.Type == 'nmos':
            G,S,D = gsd(Obj)
            if (D=='vss')and(G in Pkeys):
                Translates.append((S,'vss'))
                Remove.append(Inst)
                Remove.append(Pkeys[G][0])

    removeInsts(Remove,Mod)
    for (Net,Pwr) in Translates:
        Buf = inventInst('buf')
        Mod.add_inst_conns('buf',Buf,[('i',Pwr),('o',Net)])
        print('>>IIIIII>>>',Buf,Net,Pwr)

#    useTranslations(Translates,Mod,True)




def simpleCmos(Mod):
    Pkeys = {}
    Nkeys = {}
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type in PMOS:
            G,S,D = gsd(Obj)
            GS = tuple(sorted((S,D)))
            register(Pkeys,GS,(Inst,G))
            
        if Obj.Type in NMOS:
            G,S,D = gsd(Obj)
            GS = tuple(sorted((S,D)))
            register(Nkeys,GS,(Inst,G))
            
    for Key in Pkeys:
        if Key in Nkeys:
            Ln = Nkeys[Key]
            Lp = Pkeys[Key]
            if (len(Ln)==1)and(len(Lp)==1):
                Mod.insts.pop(Ln[0][0])
                Mod.insts.pop(Lp[0][0])
                Mod.add_inst_conns('cmos','_'.join((Ln[0][0],Lp[0][0])),[('i',Key[0]),('o',Key[1]),('gn',Ln[0][1]),('gp',Lp[0][1])])


def simpleParallels(Mod,Mos,Kind):
    Keys = {}
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == Mos:
            G,S,D = gsd(Obj)
            LL = tuple(sorted([S,D]))
            register(Keys,LL,(Inst,G))

    for Key in Keys:
        LL = Keys[Key]
        if len(LL)>1:
            Insts = []
            Gates = []
            
            for Inst,Ga in LL:
                if Ga not in Gates: Gates.append(Ga)
                Insts.append(Inst)
                
            
            Insts.sort()
            Left = Insts[0]
            for Inst in Insts[1:]: Mod.insts.pop(Inst)
            Inst = inventInst('%s_%s'%(Kind,Mos))
            if len(Gates)>1:
                NewGate = inventInst('g_%s_%s'%(Kind,Mos))
                Ins = [('o',NewGate)]
                for ind,Gate in enumerate(Gates):
                    Ins.append(('i%d'%ind,Gate))
                Mod.add_inst_conns(Kind,Inst,Ins)
                Mod.insts[Left].conns['g'] = NewGate



def simpleInverters(Mod):
    Pkeys = {}
    Nkeys = {}
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type in PMOS:
            G,S,D = gsd(Obj)
            if (D=='vdd'):
                register(Pkeys,(G,S),Inst)
            
        if Obj.Type in NMOS:
            G,S,D = gsd(Obj)
            if (D=='vss'):
                register(Nkeys,(G,S),Inst)
            
    for Key in Pkeys:
        if Key in Nkeys:
            Ln = Nkeys[Key]
            Lp = Pkeys[Key]
            if (len(Ln)==1)and(len(Lp)==1):
                Mod.insts.pop(Ln[0])
                Mod.insts.pop(Lp[0])
                Mod.add_inst_conns('inv','_'.join((Ln[0],Lp[0])),[('i',Key[0]),('o',Key[1])])

def finalTristate(Mod):
    Mod.prepareNetTable()
    Maps = makeMap(Mod)
    for Net in Maps:
        Map = Maps[Net]
        if 'nsd1psd1' in Map:
            LLL = Mod.netTable[Net]
            LLN = justType(LLL,'nmos')
            LLP = justType(LLL,'pmos')
            Nmos,_,Pinn = LLN[0]
            Pmos,_,Pinp = LLP[0]
            I0 = otherNet(Nmos,Pinn,Mod)
            I1 = otherNet(Pmos,Pinp,Mod)
            if (I0=='vss')and(I1=='vdd'):
                Gn = Mod.insts[Nmos].conns['g']
                Gp = Mod.insts[Pmos].conns['g']
                Mod.add_inst_conns('nor',inventInst('nor'),[('o',Net),('i0',Gn),('i1',Gp)])
                removeInsts([Nmos,Pmos],Mod)

    

def cmosMux(Mod):
    Mod.prepareNetTable()
    Maps = makeMap(Mod)
    for Net in Maps:
        Map = Maps[Net]
        if Map in ['cm2li1','cm2li2','cm2ext1']:
            LLL = Mod.netTable[Net]
            LL2 = justType(LLL,'cmos')
            Cmos0,_,Pin0 = LL2[0]
            Cmos1,_,Pin1 = LL2[1]
            Gn0 = Mod.insts[Cmos0].conns['gn']
            Gp0 = Mod.insts[Cmos0].conns['gn']
            Gn1 = Mod.insts[Cmos1].conns['gp']
            Gp1 = Mod.insts[Cmos1].conns['gp']
            if (Gn0==Gp1)and(Gn1==Gp0):
                I0 = otherNet(Cmos0,Pin0,Mod)
                I1 = otherNet(Cmos1,Pin1,Mod)
                Mod.add_inst_conns('mux2',inventInst('mux'),[('o',Net),('i0',I0),('i1',I1),('s',Gn1)])
                removeInsts([Cmos0,Cmos1],Mod)



def complexMux(Mod):
    Mod.prepareNetTable()
    Maps = makeMap(Mod)
    for Net in Maps:
        Map = Maps[Net]
        if Map in ['cm1li1nsd1psd1','cm1li2nsd1psd1','cm1li3nsd1psd1']:
            LLL = Mod.netTable[Net]
            Nmos,_,Pnmos = justType(LLL,'nmos')[0]
            Cmos,_,Pcmos = justType(LLL,'cmos')[0]
            Pmos,_,Ppmos = justType(LLL,'pmos')[0]
            Onetn = otherNet(Nmos,Pnmos,Mod)
            Onetp = otherNet(Pmos,Ppmos,Mod)
            Icmos = otherNet(Cmos,Pcmos,Mod)
            if (Onetn=='vss')and(Onetp=='vdd'):
                print('PPPMOS',Pmos)
                Up = Mod.insts[Pmos].conns['g']
                Thr = Mod.insts[Cmos].conns['gn']
                X = inventInst('omid')
                Mod.add_inst_conns('nand',inventInst('nand'),[('i0',Up),('i1',X),('o',Net)])
                Mod.add_inst_conns('nand',inventInst('nand'),[('i0',Icmos),('i1',Thr),('o',X)])
                removeInsts([Nmos,Pmos,Cmos],Mod)

def simpleTinvs(Mod):
    Mod.prepareNetTable()
    Map = makeMap(Mod)
    Nkeys,Pkeys = {},{}
    for Net in Map:
        Okn = twonmos(Net,Map,Mod)
        Okp = twopmos(Net,Map,Mod)
        if Okn:
            Out,Ng0,Ng1,Nmos0,Nmos1 = Okn
            register(Nkeys,Out,(Ng0,Ng1,Nmos0,Nmos1))
        if Okp:
            Out,Pg0,Pg1,Pmos0,Pmos1 = Okp
            register(Pkeys,Out,(Pg0,Pg1,Pmos0,Pmos1))
            
    for Out in Nkeys:
        if Out in Pkeys:
            for (Ng0,Ng1,Nmos0,Nmos1) in  Nkeys[Out]:
                for (Pg0,Pg1,Pmos0,Pmos1) in  Pkeys[Out]:
                    In,Dn = common([Ng0,Ng1],[Pg0,Pg1])
                    if In and inverted(Dn[0],Dn[1],Mod) and all_present([Pmos0,Pmos1,Nmos0,Nmos1],Mod):
                        removeInsts([Pmos0,Pmos1,Nmos0,Nmos1],Mod)
                        Tinv = inventInst('tinv')
                        Mod.add_inst_conns('tinv',Tinv,[('i',In),('o',Out),('g',Dn[0])])
                
def all_present(List,Mod):
    for Inst in List:
        if Inst not in Mod.insts: return False
    return True

def common(List0,List1):
    for L0 in List0:
        if L0 in List1:
            List0.remove(L0)
            List1.remove(L0)
            return L0,List0+List1
    return False,False

def twonmos(Net,Map,Mod):
    if Map[Net]!='nsd2': return False
    LL = Mod.netTable[Net]
    Nmos0,_,Pin0 = LL[0]
    Nmos1,_,Pin1 = LL[1]
    Onet0 = otherNet(Nmos0,Pin0,Mod)
    Onet1 = otherNet(Nmos1,Pin1,Mod)
    if (Onet0=='vss'): Out = Onet1
    elif (Onet1=='vss'): Out = Onet0
    else: return False
    Ng0 = Mod.insts[Nmos0].conns['g']
    Ng1 = Mod.insts[Nmos1].conns['g']
    return Out,Ng0,Ng1,Nmos0,Nmos1

def twopmos(Net,Map,Mod):
    if Map[Net]!='psd2': return False
    LL = Mod.netTable[Net]
    Pmos0,_,Pin0 = LL[0]
    Pmos1,_,Pin1 = LL[1]
    Onet0 = otherNet(Pmos0,Pin0,Mod)
    Onet1 = otherNet(Pmos1,Pin1,Mod)
    if (Onet0=='vdd'): Out = Onet1
    elif (Onet1=='vdd'): Out = Onet0
    else: return False
    Pg0 = Mod.insts[Pmos0].conns['g']
    Pg1 = Mod.insts[Pmos1].conns['g']
    return Out,Pg0,Pg1,Pmos0,Pmos1

def inverted(Net0,Net1,Mod):
    LL = Mod.netTable[Net0]
    for (Inst,Type,Pin) in LL:
        if Type=='inv':
            if (Pin=='i')and(Net1 == Mod.insts[Inst].conns['o']): return True
            if (Pin=='o')and(Net1 == Mod.insts[Inst].conns['i']): return True
    return False

def simpleLatches(Mod):    
    Mod.prepareNetTable()
    Tinvs = {}
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == 'tinv':
            Out = Obj.conns['o']
            In = Obj.conns['i']
            G = Obj.conns['g']
            register(Tinvs,Out,(Inst,In,G))

    for Out in Tinvs:
        if len(Tinvs[Out])==1:
            (Inst,In,G) = Tinvs[Out][0]
            if inverted(In,Out,Mod):
                LLL = Mod.netTable[Out]
                Cmoses = justType(LLL,'cmos')
                print('JJJJJ')
                if len(Cmoses)==1:
                    Cmos,_,Pin = Cmoses[0]
                    Gp = Mod.insts[Cmos].conns['gp']
                    Gn = Mod.insts[Cmos].conns['gn']
                    II = otherNet(Cmos,Pin,Mod)
                    if Gp == G:
                        removeInsts([Inst,Cmos],Mod)
                        Mod.add_inst_conns('latch',inventInst('latch'),[('o',Out),('i',II),('g',Gn)])
                        

    for Out in Tinvs:
        if len(Tinvs[Out])==1:
            (Inst,In,G) = Tinvs[Out][0]
            LLL = Mod.netTable[Out]
            Invs = justType(LLL,'inv')
            for InvB,_,PinB in Invs:
                if PinB == 'o':
                    II = Mod.insts[InvB].conns['i']
                    for InvF,_,PinF in Invs:
                        if PinF == 'i':
                            OO = Mod.insts[InvF].conns['o']
                            if OO == II:
                                removeInsts([Inst,InvB],Mod)                         
                                Mod.add_inst_conns('latch',inventInst('latch'),[('o',Out),('i',In),('g',G)])



    for Out in Tinvs:
        if len(Tinvs[Out])==2:
            (Inst0,In0,G0) = Tinvs[Out][0]
            (Inst1,In1,G1) = Tinvs[Out][1]
            if inverted(G0,G1,Mod):
                removeInsts([Inst0,Inst1],Mod)
                if inverted(Out,In0,Mod):
                    Mod.add_inst_conns('latch',inventInst('latch'),[('o',Out),('i',In1),('g',G1)])
                elif inverted(Out,In1,Mod):
                    Mod.add_inst_conns('latch',inventInst('latch'),[('o',Out),('i',In0),('g',G0)])
                else:
                    Mod.add_inst_conns('mux2',inventInst('mux'),[('o',Out),('i0',In0),('i1',In1),('s',G1)])




def simpleNands(Mod):
    Mod.prepareNetTable()
    Map = makeMap(Mod)
    for Net in Map:
        Okn = twonmos(Net,Map,Mod)
        if Okn:
            Out,Ng0,Ng1,Nmos0,Nmos1 = Okn
            if Out and ('nsd1psd2' in Map[Out]):
                LLO = Mod.netTable[Out]
                Pmoses = justType(LLO,'pmos')
                Pmos0,_,PPin0 = LLO[0]
                Pmos1,_,PPin1 = LLO[1]
                Ng0 = Mod.insts[Nmos0].conns['g']
                Ng1 = Mod.insts[Nmos1].conns['g']
                Pg0 = Mod.insts[Pmos0].conns['g']
                Pg1 = Mod.insts[Pmos1].conns['g']
                if sorted((Ng0,Ng1))==sorted((Pg0,Pg1)):
                    if (otherNet(Pmos0,PPin0,Mod)=='vdd')and (otherNet(Pmos1,PPin1,Mod)=='vdd'):
                        Mod.insts.pop(Pmos0)
                        Mod.insts.pop(Pmos1)
                        Mod.insts.pop(Nmos0)
                        Mod.insts.pop(Nmos1)
                        Mod.add_inst_conns('nand',False,[('o',Out),('i0',Ng0),('i1',Ng1)])
                                        

def justType(List,Type):
    res = []
    for Inst,Typex,Pin in List:
        if Typex==Type:
            res.append((Inst,Type,Pin))
    return res

def otherNet(Mos,Pin,Mod):
    if Pin=='s': return Mod.insts[Mos].conns['d']
    if Pin=='d': return Mod.insts[Mos].conns['s']
    if Pin=='i': return Mod.insts[Mos].conns['o']
    if Pin=='o': return Mod.insts[Mos].conns['i']
    return False

def makeMap(Mod):
    Maps = {}
    for Net in Mod.nets:
        if not internalNet(Net,Mod): 
            Maps[Net] = {'ext':1}

    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        if Type == 'nmos':
            G,S,D = gsd(Obj)
            mapit(Maps,G,'gn')
            mapit(Maps,S,'nsd')
            mapit(Maps,D,'nsd')
        elif Type == 'pmos':
            G,S,D = gsd(Obj)
            mapit(Maps,G,'gp')
            mapit(Maps,S,'psd')
            mapit(Maps,D,'psd')
        elif Type == 'cmos':
            mapit(Maps,Obj.conns['gn'],'li')
            mapit(Maps,Obj.conns['gp'],'li')
            mapit(Maps,Obj.conns['i'],'cm')
            mapit(Maps,Obj.conns['o'],'cm')
        elif Type in LOGICALS+COMPLEXS:
            for Pin in Obj.conns:
                if 'o' in Pin:
                    mapit(Maps,Obj.conns[Pin],'lo')
                else:
                    mapit(Maps,Obj.conns[Pin],'li')
        else:
            for Pin in Obj.conns:
                mapit(Maps,Obj.conns[Pin],'x')
    Maps2 = {}
    for Net in Maps:
        Sign = Maps[Net]
        Keys = list(Sign.keys())
        Keys.sort()
        Res = ''
        for Key in Keys:
            Num = Sign[Key]
            Res += '%s%s'%(Key,Num)
        Maps2[Net] = Res
    return Maps2            

def mapit(Maps,Net,Kind):        
    if Net not in Maps: Maps[Net] = {}
    Was = Maps[Net]
    if Kind not in Was:
        Was[Kind]=1
    else:
        Was[Kind] += 1


    
def followInvs(Mod):
    Invs = {}
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type=='inv':
            I = Obj.conns['i']
            O = Obj.conns['o']
            if internalNet(O,Mod): 
                Invs[O] = (I,Inst)
    print('INVS %s '%(str(Invs)))
    for OO in Invs.keys():
        Mid,Inst0 = Invs[OO]
        if (Inst0 in Mod.insts) and (Mid in Invs):
            II,Inst1 = Invs[Mid]
            if II!=OO:
#                Mod.insts.pop(Inst0)
                useTranslations([(OO,II)],Mod,True)
                Mod.insts[Inst0].conns['o'] = OO

            
    


def sameTrans(Mod):
    Pkeys = {}
    Nkeys = {}
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type in PMOS:
            Key = buildSameKey(Obj) 
            if Key not in Pkeys: 
                Pkeys[Key] = [Inst]
            else:
                Pkeys[Key].append(Inst)
        if Obj.Type in NMOS:
            Key = buildSameKey(Obj) 
            if Key not in Nkeys: 
                Nkeys[Key] = [Inst]
            else:
                Nkeys[Key].append(Inst)

    for Key in Nkeys:
        List = sorted(Nkeys[Key])
        if len(List)>1:
            for Inst in List[1:]:
                Mod.insts.pop(Inst)

    for Key in Pkeys:
        List = sorted(Pkeys[Key])
        if len(List)>1:
            for Inst in List[1:]:
                Mod.insts.pop(Inst)



def buildSameKey(Obj):
    G,S,D = gsd(Obj)
    LKey = [G]+sorted([S,D])
    Key = ' '.join(LKey)
    return Key



def orientSimpleMoses(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type in PMOS:
            if (Obj.conns['s'] == 'vdd')and(Obj.conns['d'] != 'vdd'):
                Obj.conns['s'] = Obj.conns['d']
                Obj.conns['d'] = 'vdd'
        if Obj.Type in NMOS:
            if (Obj.conns['s'] == 'vss')and(Obj.conns['d'] != 'vss'):
                Obj.conns['s'] = Obj.conns['d']
                Obj.conns['d'] = 'vss'


def extractPowers(Mod):
    Mod.Vdd = []
    Mod.Vss = []
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type in PMOS:
            if 'b' in Obj.conns:
                VDD = Obj.conns['b']
                if  VDD not in Mod.Vdd: Mod.Vdd.append(VDD)
                Obj.conns['b'] = 'vdd'
                for  Pin in Obj.conns:
                    Sig = Obj.conns[Pin]
                    if Sig == VDD: Obj.conns[Pin]='vdd'
            Obj.Type = 'pmos'
        if Obj.Type in NMOS:
            if 'b' in Obj.conns:
                VSS = Obj.conns['b']
                if  VSS not in Mod.Vss: Mod.Vss.append(VSS)
                Obj.conns['b'] = 'vss'
                for  Pin in Obj.conns:
                    Sig = Obj.conns[Pin]
                    if Sig == VSS: Obj.conns[Pin]='vss'
            Obj.Type = 'nmos'





def transistor(Inst,Mod):
    Obj = Mod.insts[Inst]
    if Obj.Type not in PMOS+NMOS: return False
    G,S,D = gsd(Obj)
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
    if type(Net) is list: return False
    if type(Net) is tuple: return False
    if Net not in Mod.nets: return False
    Dir,_ = Mod.nets[Net]
    if not internalNet(Net,Mod): return False
    if (len(Mod.netTable[Net])!=2): return False
    return True
        

    
# ?Nx - any net
# ?Xx - 2x net 
# ?Ix - 2x net 
# Pattern "MOS GATE S D B"

def cmos_and(Dict,Insts,Mod):
    logs.log_info('cmos_and %s %s'%(Insts,Dict))
    cmos(Dict,Insts[:2],Mod)
    Cmosinst = '_'.join(Insts[:2])
    if Cmosinst in list(Mod.insts.keys()):
        if Mod.insts[Insts[2]].conns['g'] == Mod.insts[Cmosinst].conns['gp']:
            if Mod.insts[Insts[2]].conns['s'] in [Mod.insts[Cmosinst].conns['i'],Mod.insts[Cmosinst].conns['o']]:
                I0 = Mod.insts[Cmosinst].conns['gn']
                if Mod.insts[Insts[2]].conns['s']==Mod.insts[Cmosinst].conns['i']:
                    I1 = Mod.insts[Cmosinst].conns['o']
                    O = Mod.insts[Cmosinst].conns['i']
                else:
                    I1 = Mod.insts[Cmosinst].conns['i']
                    O = Mod.insts[Cmosinst].conns['o']
                Mod.add_inst_conns('and','_'.join(Insts),[('i0',I0),('i1',I1),('o',O)])
                Mod.insts.pop(Insts[2])
                Mod.insts.pop(Cmosinst)

def cmos_or(Dict,Insts,Mod):
    logs.log_info('cmos_or %s %s'%(Insts,Dict))
    cmos(Dict,Insts[:2],Mod)
    Cmosinst = '_'.join(Insts[:2])
    if Cmosinst in list(Mod.insts.keys()):
        
        if Mod.insts[Insts[2]].conns['g'] == Mod.insts[Cmosinst].conns['gn']:
            if Mod.insts[Insts[2]].conns['s'] in [Mod.insts[Cmosinst].conns['i'],Mod.insts[Cmosinst].conns['o']]:
                I0 = Mod.insts[Cmosinst].conns['gp']
                if Mod.insts[Insts[2]].conns['s']==Mod.insts[Cmosinst].conns['i']:
                    I1 = Mod.insts[Cmosinst].conns['o']
                    O = Mod.insts[Cmosinst].conns['i']
                else:
                    I1 = Mod.insts[Cmosinst].conns['i']
                    O = Mod.insts[Cmosinst].conns['o']
                Mod.add_inst_conns('or','_'.join(Insts),[('i0',I0),('i1',I1),('o',O)])
                Mod.insts.pop(Insts[2])
                Mod.insts.pop(Cmosinst)
                


def cmos(Dict,Insts,Mod):
    logs.log_info('cmos %s %s'%(Insts,Dict))
    Gp,Sp,Dp = gsd(Mod.insts[Insts[0]])
    Gn,Sn,Dn = gsd(Mod.insts[Insts[1]])
    SDp = [Sp,Dp]
    SDp.sort()
    SDn = [Sn,Dn]
    SDn.sort()
    if (SDn==SDp):
        removeInsts(Insts,Mod)
        Mod.add_inst_conns('cmos','_'.join(Insts),[('i',Sp),('o',Dp),('gn',Gn),('gp',Gp)])

def inverter(Dict,Insts,Mod):
    logs.log_info('inverter %s %s'%(Insts,Dict))
    removeInsts(Insts,Mod)
    Mod.add_inst_conns('inv','_'.join(Insts),[('i',Dict['?N1']),('o',Dict['?N2'])])



def parallel_nmos(Dict,Insts,Mod):
    G0 = Mod.insts[Insts[0]].conns['g']
    G1 = Mod.insts[Insts[1]].conns['g']
    Mod.insts.pop(Insts[1])
    if G0==G1: return
    Gate = mergeNames(G0,G1,'g',Mod)
#    Gate = '%s_%s_g'%(G0,G1)
    Mod.add_inst_conns('or','_'.join(Insts),[('i0',G0),('i1',G1),('o',Gate)])
    Mod.insts[Insts[0]].conns['g']=Gate


def mergeNames(G0,G1,Let,Mod):
    if (type(G0) is str)and(type(G1) is str):
        Net =  '%s_%s_%s'%(G0,G1,Let)
    else:
        Net = inventInst('net_%s'%Let)
    Mod.nets[Net] = ('wire',0)
    return Net

def parallel_pmos(Dict,Insts,Mod):
    G0 = Mod.insts[Insts[0]].conns['g']
    G1 = Mod.insts[Insts[1]].conns['g']
    Mod.insts.pop(Insts[1])
    if G0==G1: return
    Gate = mergeNames(G0,G1,'g',Mod)
#    Gate = '%s_%s_g'%(G0,G1)
    Mod.add_inst_conns('and','_'.join(Insts),[('i0',G0),('i1',G1),('o',Gate)])
    Mod.insts[Insts[0]].conns['g']=Gate


def serial_nmos(Dict,Insts,Mod):
    logs.log_info('serial_nmos %s %s'%(Insts,Dict))
    Mod.insts.pop(Insts[1])
    if Dict['?X1']==Mod.insts[Insts[0]].conns['s']:
        Mod.insts[Insts[0]].conns['s']=Dict['?N4']
    else:
        Mod.insts[Insts[0]].conns['d']=Dict['?N4']

    if Dict['?N1']==Dict['?N3']: return
#    Gate = '%s_%s_g'%(Dict['?N1'],Dict['?N3'])
    Gate = mergeNames(Dict['?N1'],Dict['?N3'],'g',Mod)
    Mod.add_inst_conns('and','_'.join(Insts),[('i0',Dict['?N1']),('i1',Dict['?N3']),('o',Gate)])
    Mod.insts[Insts[0]].conns['g']=Gate

def tielow(Dict,Insts,Mod):
    logs.log_info('tielow %s %s'%(Insts,Dict))
    Mos = Insts[0]
    N1 = Dict['?N1']
    Mod.insts.pop(Mos)
    Mod.add_inst_conns('buf',Mos,[('i','0'),('o',N1)])

def tiehigh(Dict,Insts,Mod):
    logs.log_info('tiehigh %s %s'%(Insts,Dict))
    Mos = Insts[0]
    N1 = Dict['?N1']
    Mod.insts.pop(Mos)
    Mod.add_inst_conns('buf',Mos,[('i','1'),('o',N1)])

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
#    Gate = '%s_%s_g'%(Dict['?N1'],Dict['?N3'])
    Gate = mergeNames(Dict['?N1'],Dict['?N3'],'g',Mod)
    Mod.add_inst_conns('or','_'.join(Insts),[('i0',Dict['?N1']),('i1',Dict['?N3']),('o',Gate)])
    Mod.insts[Insts[0]].conns['g']=Gate







def cross_mos(Dict,Insts,Mod):
    logs.log_info('cross_mos %s %s'%(Dict,Insts))
    Mod.add_inst_conns('cross_mos',inventInst('cross'),[('i0',Dict['?I0']),('i1',Dict['?I1']),('q0',Dict['?Q0']),('q1',Dict['?Q1'])])
    for Inst in Insts: Mod.insts.pop(Inst)

# nmos G S D B 
# pmos G S D B 
Pattern0 = (('nmos ?N1 ?N2 vss vss','pmos ?N1 ?N2 vdd vdd'),inverter)
Pattern1 = (('nmos ?N1 ?I1 ?I2 vss','nmos ?N2 ?I1 ?I2 vss'),parallel_nmos)
Pattern2 = (('pmos ?N1 ?I1 ?I2 vdd','pmos ?N2 ?I1 ?I2 vdd'),parallel_pmos)
Pattern3 = (('nmos ?N1 ?N2 ?X1 vss','nmos ?N3 ?X1 ?N4 vss'),serial_nmos)
Pattern4 = (('pmos ?N1 ?N2 ?X1 vdd','pmos ?N3 ?X1 ?N4 vdd'),serial_pmos)
Pattern50 = (('pmos ?N1 ?N2 ?N3 vdd','nmos ?N4 ?N2 ?N3 vss','nmos ?N1 ?N2 vss vss'),cmos_and)
Pattern51 = (('pmos ?N1 ?N2 ?N3 vdd','nmos ?N4 ?N2 ?N3 vss','pmos ?N4 ?N2 vdd vdd'),cmos_or)
Pattern52 = (('pmos ?N1 ?N2 ?N3 vdd','nmos ?N4 ?N2 ?N3 vss','pmos ?N4 ?N3 vdd vdd'),cmos_or)
Pattern5 = (('pmos ?N1 ?N2 ?N3 vdd','nmos ?N4 ?N2 ?N3 vss'),cmos)
Pattern6 = (['pmos ?N1 ?N1 vdd vdd'],short_mos)
Pattern7 = (['nmos ?N1 ?N1 vss vss'],short_mos)
Pattern8 = (['pmos ?N1 vdd ?N1 vdd'],short_mos)
Pattern9 = (['nmos ?N1 vss ?N1 vss'],short_mos)
Pattern10 = (['nmos vdd ?N1 vss vss'],tielow)
Pattern11 = (['pmos vss ?N1 vdd vdd'],tiehigh)
PatternCross = ([
      'pmos ?Q0 vdd ?Q1 vdd'
     ,'pmos ?Q1 vdd ?Q0 vdd'
     ,'nmos ?I0 vss ?Q1 vss'
     ,'nmos ?I1 vss ?Q0 vss'

    ],cross_mos)


PATTERNS0 = [Pattern1,Pattern2]
PATTERNS2 = [Pattern51]
PATTERNS = [Pattern0,Pattern1,Pattern2,Pattern3,Pattern4,Pattern50,Pattern51,Pattern5,Pattern6,Pattern7,Pattern8,Pattern9,PatternCross]

PATTERNS1 = [Pattern10,Pattern11]
    

def scanDesignForPattern(Mod):
    Dones = 0
    for Pattern in PATTERNS0:
        Dones += scanPattern(Pattern,Mod)
    for Pattern in PATTERNS2:
        Dones += scanPattern(Pattern,Mod)
    for Pattern in PATTERNS:
        Dones += scanPattern(Pattern,Mod)
    for Pattern in PATTERNS1:
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
    Wrds = Look.split()
    Keys = list(Mod.insts.keys())
    for Inst in Keys:
        if (Inst in Mod.insts)and(Inst not in Insts):
            Obj = Mod.insts[Inst]
#            print('<><>',Inst,LL,Wrds[0],Obj.Type,PMOS,NMOS,Obj.conns)
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
    Pins = list(Obj.conns.keys())
    for Pin in Pins:
        if Pin[0]=='i': Obj.conns.pop(Pin)

def addInputs(Sigs,Obj):
    for ind,Sig in enumerate(Sigs):
        Obj.conns['i%d'%ind]=Sig

def getConns(Inst,Mod):
    Obj = Mod.insts[Inst]
    Out = Obj.conns['o']
    Ins = []
    Ins2 = []
    Ins3 = []
    for Pin in Obj.conns:   
        if Pin!='o':
            Inx = Obj.conns[Pin]
            if type(Inx) is list:
                Ins2.append(Inx)
            elif type(Inx) is tuple:
                Ins3.append(Inx)
            else:
                Ins.append(Inx)
    Ins.sort()
    Ins2.sort()
    Ins3.sort()
    return Out,Ins+Ins2+Ins3

def removeOrphans(Mod,Dbg=False):
    Dones = 0
    Mod.prepareNetTable()
    Insts = list(Mod.insts.keys())
    for Inst in Insts:
        Obj  = Mod.insts[Inst]
        if Obj.Type in LOGICALS:
            Out = Obj.conns['o']
            if internalNet(Out,Mod):
                if (type(Out) is str) and (len(Mod.netTable[Out])==1):
                    if Dbg:
                        logs.log_info('ORPHAN remove %s out=%s nettbl=%s'%(Inst,Out,Mod.netTable[Out]))

                    Mod.insts.pop(Inst)
                    if Out in Mod.nets: 
                        Mod.nets.pop(Out)
                        Dones += 1
                elif (type(Out) is list) and (len(Mod.netTable[tuple(Out)])==1):
                    Mod.insts.pop(Inst)
                    if Out in Mod.nets: 
                        Mod.nets.pop(Out)
                        Dones += 1
    if Dones>0:
        removeOrphans(Mod)


            
def internalNet(Net,Mod):
    if type(Net) is list:
        if Net[0] == 'subbit':
            Net = Net[1]
    if Net not in Mod.nets: return True
    Dir,_ = Mod.nets[Net]
    if 'input' in Dir: return False
    if 'output' in Dir: return False
    if 'inout' in Dir: return False
    if Net in ['vdd','vss']: return False
    return True

def useTranslations(Translates,Mod,Force=False):
    Table = {}
    for (Sig0,Sig1) in Translates:
        if Force:
            Table[Sig0]=Sig1
        elif internalNet(Sig0,Mod):
            Table[Sig0]=Sig1
        elif internalNet(Sig1,Mod):
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
        
#    print('TATATA',Table)
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            if (type(Sig) is str) and (Sig in Table):
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
    Keys = list(Mod.insts.keys())
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
    Nets = list(Mod.nets.keys())
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
    Outs = list(Nors.keys())
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
                    Mod.add_conn(New,'set',Ins0[0])
                else:
                    Mod.add_inst_conns('or',New+'_sor',[('o',New+'_s')])
                    Mod.add_conn(New,'set',New+'_s')
                    for ind,In in enumerate(Ins0):
                        Mod.add_con(New+'_sor','i%d'%ind,In)

                if len(Ins1)==1:
                    Mod.add_conn(New,'rst',Ins1[0])
                else:
                    Mod.add_inst_conns('or',New+'_ror',[('o',New+'_r')])
                    Mod.add_conn(New,'rst',New+'_r')
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

    Mod.add_inst_conns('dlatch',inventInst('dlatch'),[('qn',Dict['?N1']),('q',Dict['?N6']),('d',Din),('rb',RB),('clk',Clk)])
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
    Mod.add_inst_conns('dlatch',inventInst('dlatch'),[('qn',''),('q',Dict['?N6']),('d',Din),('rb',RB),('clk',Clk)])
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

    Mod.add_inst_conns('dlatch',inventInst('dlatch'),[('qn',Dict['?QB']),('q',Dict['?Q']),('d',Din),('rb',RB),('clk',Clk)])
    for Inst in Insts: Mod.insts.pop(Inst)

def Dff(Dict,Insts,Mod):
    logs.log_info('Dff %s %s'%(Insts,Dict))

    Mod.add_inst_conns('dff',inventInst('dff'),[('mid',Dict['?Q0']),('midn',Dict['?QN0']),('qn',Dict['?QN']),('q',Dict['?Q']),('d',Dict['?D0']),('rb',Dict['?RB']),('clk',Dict['?C1'])])
    for Inst in Insts: Mod.insts.pop(Inst)

def invinv(Dict,Insts,Mod):
    D0 = Dict['?D0']
    D1 = Dict['?D1']
    logs.log_info('invinv %s %s    %s   %s'%(D0,D1,Mod.netTable[D0],Mod.netTable[D1]))
    Gn,Gp,Insts2 = invinvDriver(D0,Insts,Mod)
    if Gn:
        removeInsts(Insts2,Mod)
        Mod.add_inst_conns('srlatch',inventInst('srlatch'),[('clr',Gn),('setn',Gp),('qn',D1),('q',D0)])
        return

    Gn,Gp,Insts2 = invinvDriver(D1,Insts,Mod)
    if Gn:
        removeInsts(Insts2,Mod)
        Mod.add_inst_conns('srlatch',inventInst('srlatch'),[('clr',Gn),('setn',Gp),('qn',D0),('q',D1)])
        return

def invinvDriver(DD,Insts,Mod):
    LL = Mod.netTable[DD]
    Gn,Gp = False,False
    Insts2 = Insts[:]
    for Inst,Type,Pin in LL:
        Obj = Mod.insts[Inst]
        if (Type=='nmos')and(Pin=='s'):
            if Obj.conns['d']=='vss':
                Gn = Obj.conns['g']
                Insts2.append(Inst)
        if (Type=='nmos')and(Pin=='d'):
            if Obj.conns['s']=='vss':
                Gn = Obj.conns['g']
                Insts2.append(Inst)

        if (Type=='pmos')and(Pin=='s'):
            if Obj.conns['d']=='vdd':
                Gp = Obj.conns['g']
                Insts2.append(Inst)
            
        if (Type=='pmos')and(Pin=='d'):
            if Obj.conns['s']=='vdd':
                Gp = Obj.conns['g']
                Insts2.append(Inst)
            
    if Gn and Gp:
        return Gn,Gp,Insts2
    return False,False,False



def cmos_And(Dict,Insts,Mod):
    And = inventInst('and')
    Mod.add_inst_conns('and',And,[('o',Dict['?OO']),('i0',Dict['?II']),('i1',Dict['?GN'])])
    removeInsts(Insts,Mod)

def removeInsts(Insts,Mod):
    for Inst in Insts:
        if Inst in Mod.insts:
            Mod.insts.pop(Inst)

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
        Xnor = inventInst('xnor')
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

InvInv_pattern = ((
    'inv  i=?D0 o=?D1'
    ,'inv  i=?D1 o=?D0'
#    ,'nmos g=?GN s=?D0 d=vss b=vss'
#    ,'pmos g=?GP s=?D0 d=vdd b=vdd'
),invinv)



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
    Wrds = Look.split()
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
        Keys = list(Mod.insts.keys())
        for Inst in Keys:
            if (Inst in Mod.insts)and(Inst not in Insts):
                Obj = Mod.insts[Inst]
                if matchingType(Obj.Type,Wrds[0]):
                    Copy = copyDict(Dic)
                    Fail = False
                    for Wrd in Wrds[1:]:
                        PinTag = Wrd.split('=')
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
def inventInst(Base):
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
    if 'inout' in Dir: return Net
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
#            print('LLL',Lins)
#            Lins.sort()
            return [Type] + Lins
        elif (Pin=='o')and(Type == 'mux2'):
            return Net



    logs.log_error('FAILED buildFunctionDeep "%s" %s %s'%(Net,Dir,Conns))
    return Net

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

def turnMosesToAssigns(Mod):
    Insts = list(Mod.insts.keys())
    for Inst in Insts:
        Obj = Mod.insts[Inst]
        if (Obj.Type == 'nmos'):
            G,S,D = gsd(Obj)
            if D=='vss':
                Mod.insts.pop(Inst)
                Mod.add_hard_assign(S,('question',G,0,('bin',1,'z')))
                
        if (Obj.Type == 'pmos'):
            G,S,D = gsd(Obj)
            if D=='vdd':
                Mod.insts.pop(Inst)
                Mod.add_hard_assign(S,('question',G,('bin',1,'z'),1))
                




def turnGatesToAssigns(Mod):
    Assigns = {}
    Translates = []
    Insts = list(Mod.insts.keys())
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
    Keys = list(Mod.insts.keys())
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
            O = tuplize(O)
            I = tuplize(I)
            InvsO[O] = (Inst,I)
            InvsI[I] = (Inst,O)
    for OO in list(InvsO.keys()):
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


def tuplize(Sig):
    if (type(Sig) is list): return tuple(Sig)
    return Sig

def travelBack(OO,InvsO,Deep):
    _,II = InvsO[OO]
    if II not in InvsO: return Deep+1,II
    if (Deep>10): return Deep,II
    return travelBack(II,InvsO,Deep+1)


def renameBackToOriginalVdd(Mod):
    for From,To in VDDRENAMES:
        VDDS[From]=To
    print('renameBackToOriginalVdd')
    for Net in Mod.nets:
        if Net in VDDS:
            print('>renameBack>>>',Net,VDDS[From])
def removeBusses(Mod):
    DIRS,BUSSED = {},{}
    List = list(Mod.nets.keys())
    for Net in List:
        Dir,Wid = Mod.nets[Net]
        if (type(Wid) is tuple)and(len(Wid)==2):
            H,L = Wid
            for Ind in range(L,H+1):
                Sig = '%s_%s_'%(Net,Ind)
                Mod.nets[Sig] = Dir,0
            Mod.nets.pop(Net)
            BUSSED[Net] = H,L
            DIRS[Net] = Dir
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            if type(Sig) is list:
                if Sig[0]=='subbit':
                    Obj.conns[Pin] = '%s_%s_'%(Sig[1],Sig[2])
                    if Sig[1] not in BUSSED: 
                        print('>>>>>>Sig',Sig)
                        BUSSED[Sig[1]] = int(Sig[2]),int(Sig[2])
                    else:
                        H,L = BUSSED[Sig[1]]
                        H = max(H,int(Sig[2]))
                        L = max(L,int(Sig[2]))
                        BUSSED[Net] = H,L
    return DIRS,BUSSED

def restoreBusses(Mod,BUSSED,DIRS):
    for Kind in ['nand','nor']:
        if Kind in BUSSED:
            BUSSED.pop(Kind)
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            ww = Sig.split('_')
            if (len(ww)>=3) and (Sig[-1]=='_'):
                Ind = int(ww[-2])
                Bus = '_'.join(ww[:-2])
                
                if (Bus in BUSSED):
                    print('>>222>>>>',Bus,ww)
                    Ind = int(ww[-2])
                    Obj.conns[Pin] = ('subbit',ww[0],Ind)
        
    for Bus in BUSSED:
        H,L = BUSSED[Bus]
        if Bus not in DIRS: DIRS[Bus]='wire'
        Dir = DIRS[Bus]
        Mod.add_sig(Bus,Dir,(H,L))

    Sigs = list(Mod.nets.keys())
    for Sig in Sigs:
        ww = Sig.split('_')
        if (len(ww)>=3) and (Sig[-1]=='_'):
            Bus = '_'.join(ww[:-2])
            if Bus in BUSSED:
                Mod.nets.pop(Sig)
        
def followAndsOrs(Mod):
    Mod.prepareNetTable()
    for Net in Mod.netTable:
        LL = Mod.netTable[Net]
        if len(LL)==2:
            if (LL[0][1]== 'inv')and  (LL[0][2]== 'i')and (LL[1][1] in ['and','or','nand','nor']) and (LL[1][2] == 'o'):
                Inv = LL[0][0]
                Gate = LL[1][0]
                Type = LL[1][1]
                Ok = True
            elif (LL[1][1]== 'inv')and (LL[1][2]== 'i')and (LL[0][1] in ['and','or','nand','nor']) and (LL[0][2] == 'o'):
                Inv = LL[1][0]
                Gate = LL[0][0]
                Type = LL[0][1]
                Ok = True
            else:
                Ok = False
            if Ok:
                if Type[0] == 'n': 
                    Newtype = Type[1:]
                else:
                    Newtype = 'n'+Type
                Mod.insts[Gate].Type = Newtype
                Newout = Mod.insts[Inv].conns['o']
                Mod.insts[Gate].conns['o'] = Newout

                if internalNet(Net,Mod): Mod.insts.pop(Inv)




