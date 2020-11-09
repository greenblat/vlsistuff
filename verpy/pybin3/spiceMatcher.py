
import logs

MOSPATTERNS = {}


MOSPATTERNS['nand2'] = [ 'nmos ?i1 ?mid vss' ,'nmos ?i2 ?o ?mid'],[
     'pmos ?i1 ?o vdd'
    ,'pmos ?i2 ?o vdd'
    ],('nand2 i0=?i1 i1=?i2 o=?o')

MOSPATTERNS['nand3'] = [ 'nmos ?i1 ?mid0 vss' ,'nmos ?i2 ?mid1 ?mid0',  'nmos ?i3 ?mid1 ?o'],[
     'pmos ?i1 ?o vdd'
    ,'pmos ?i2 ?o vdd'
    ,'pmos ?i3 ?o vdd'
    ],('nand3 i0=?i1 i1=?i2 i3=?i2 o=?o')


MOSPATTERNS['inv'] = ['nmos ?g ?o vss'],['pmos ?g ?o vdd'],('inv i=?g o=?o')


MOSPATTERNS['trcmos'] = ['nmos ?en_n ?in_int vss','nmos ?en ?in ?in_int'],\
        ['pmos ?en_n ?in ?in_int'], ('and i0=?in i1=?en o=?in_int')

MOSPATTERNS['trcmos2'] = ['nmos ?en ?in ?in_int'],\
        ['pmos ?en_n ?in ?in_int','pmos ?en ?in_int vdd'], ('or i0=?in i1=?en_n o=?in_int')

MOSPATTERNS['trcmos3'] = ['nmos ?en ?in ?in_int'],\
        ['pmos ?en_n ?in ?in_int','pmos ?en ?in_int ?x'], ('or i0=?in i1=?en_n o=?in_int')

MOSPATTERNS['nor2'] = [
     'nmos ?i1 ?o vss'
    ,'nmos ?i2 ?o vss'
    ],[
     'pmos ?i1 ?o ?mid'
    ,'pmos ?i2 ?mid vdd'
    ],('nor2 i0=?i1 i1=?i2 o=?o')

MOSPATTERNS['nor3'] = [
     'nmos ?i1 ?o vss'
    ,'nmos ?i2 ?o vss'
    ,'nmos ?i3 ?o vss'
    ],[
     'pmos ?i1 ?o ?mid0'
    ,'pmos ?i2 ?mid0 ?mid1'
    ,'pmos ?i3 ?mid1 vdd'
    ],('nor3 i0=?i1 i1=?i2 i2=?i2 o=?o')



MOSPATTERNS['mux2a'] = [
      'nmos ?iclk ?net096 vss'
     ,'nmos ?iclkz ?net099 vss'
     ,'nmos ?net22 ?net14 ?net096'
     ,'nmos ?idin ?net14 ?net099'
],[
      'pmos ?iclk ?net098 vdd'
     ,'pmos ?idin ?net14 ?net098'
     ,'pmos ?iclkz ?net097 vdd'
     ,'pmos ?net22 ?net14 ?net097'
],('mux2a i0n=?idin i1n=?iclk  i0p=?net22 i1p=?iclkz o=?net14')


MOSPATTERNS['mux2b'] = [
     'nmos ?irstz ?net090 vss'
    ,'nmos ?net112 ?net091 ?net090'
    ,'nmos ?iclk ?net88 ?net091'
    ,'nmos ?iclk ?net093 vss'
    ,'nmos ?net22 ?net88 ?net093'
],[
     'pmos ?iclkz ?net094 vdd'
    ,'pmos ?net22 ?net88 ?net094'
    ,'pmos ?irstz ?net88 vdd'
    ,'pmos ?iclkz ?net88 ?net092'
    ,'pmos ?net112 ?net092 vdd'
],('mux2b i0n=?net22 i1n=?iclk  i2n=?irstz i0p=?net112 i1p=?iclkz i2p=?irstz  o=?net88')


MOSPATTERNS['mux2c'] = [
     'nmos ?irstz ?net090 vss'
    ,'nmos ?net112 ?net091 ?net090'
    ,'nmos ?iclkz ?net88 ?net091'
    ,'nmos ?net22 ?net88 ?net093'
    ,'nmos ?iclk ?net093 vss'
],[
     'pmos ?iclkz ?net094 vdd'
    ,'pmos ?net22 ?net88 ?net094'
    ,'pmos ?irstz ?net88 vdd'
    ,'pmos ?iclk ?net88 ?net092'
    ,'pmos ?net112 ?net092 vdd'
],('mux2c i0n=?net22 i1n=?iclk  i2n=?irstz i0p=?net112 i1p=?iclkz i2p=?irstz  o=?net88')

MOSPATTERNS['cap0'] = ['nmos ?g vss vss'],[],('cap o=?g')

MOSPATTERNS['mux4a'] = [
     'nmos ?net06  ?ivinn_0_ ?ovoutn'
    ,'nmos ?net017 ?ivinn_1_ ?ovoutn'
    ,'nmos ?net023 ?ivinn_2_ ?ovoutn'
    ,'nmos ?net022 ?ivinn_3_ ?ovoutn'
],[
     'pmos ?net04  ?ivinn_0_ ?ovoutn'
    ,'pmos ?net019 ?ivinn_1_ ?ovoutn'
    ,'pmos ?net025 ?ivinn_2_ ?ovoutn'
    ,'pmos ?net024 ?ivinn_3_ ?ovoutn'
],('mux4a o=?ovoutn i0=?ivinn_0_ i1=?ivinn_1_ i2=?ivinn_2_ i3=?ivinn_3_' )

MOSPATTERNS['muxff0'] = [
    'nmos ?rst_b ?net226 vss'
   ,'nmos ?clk ?net226 ?net240'
   ,'nmos ?rst ?net174 vss'
   ,'nmos ?net179 ?net174 ?net240'
   ,'nmos ?rst_b ?net228 ?vin'
   ,'nmos ?clk_b ?net174 ?net228'
],[
    'pmos ?rst ?net237 vdd'
   ,'pmos ?rst ?vin ?net229'
   ,'pmos ?clk_b ?net237 ?net239'
   ,'pmos ?clk ?net229 ?net174'
   ,'pmos ?net179 ?net239 ?net174'
],('muxff0 o=?net174 i0=?rst i1=?clk i2=?vin')

  
MOSPATTERNS['muxff1'] = [
    'nmos ?net174 ?net179 vss' 
    ,'nmos ?rst_b ?net231 ?net179'
    ,'nmos ?clk ?net182 ?net231'
    ,'nmos ?vout ?net182 ?net232'
    ,'nmos ?clk_b ?net214 ?net232'
    ,'nmos ?rst_b ?net214 vss'
],[
    'pmos ?net174 ?net179 vdd' 
   ,'pmos ?rst ?net199 vdd'
   ,'pmos ?clk ?net199 net200'
   ,'pmos ?rst ?net179 net230'
   ,'pmos ?vout ?net182 net200'
   ,'pmos ?rst_b ?net182 vdd'
   ,'pmos ?clk_b ?net182 net230'
],('muxff1 o=?vout i0=?rst i1=?clk i2=?net174')


MOSPATTERNS['latch0'] = [
    'nmos ?ltch_out ?ltch_in vss'
   ,'nmos ?en_n ?ltch_in ?midn'
   ,'nmos ?dat ?midn vss'

],[
    'pmos ?ltch_out ?ltch_in vdd'
   ,'pmos ?en ?ltch_in ?midp'
   ,'pmos ?dat ?midp vdd'

],('expression  o=?ltch_in expr="(dat && en_n) ? 0 : (!dat && !en) ? 1 : !ltch_out" ')





class Objx:
    def __init__(self,Type,Conns):
        self.Type = Type
        self.Conns = Conns
        self.params= {}


def tryMatchLogicFunc(Nmoses,Pmoses):
    Out =   goodLogicCandidate(Nmoses,Pmoses)
    if not Out: return False
    print('tryMatchLogicFunc',Nmoses,Pmoses)
    logs.setVar('paths',[])
    labelDepthMos(Nmoses,'vss',Out,[],[],[])
    logs.log_info('NPATHS %s'%str(logs.getVar('paths')))
    NPATHS = logs.getVar('paths')
    logs.setVar('paths',[])
    labelDepthMos(Pmoses,'vdd',Out,[],[],[])
    logs.log_info('PPATHS %s'%str(logs.getVar('paths')))
    PPATHS = logs.getVar('paths')
    return NPATHS,PPATHS,Out
    
def registerWin(Gates):
    Gates.sort()
    Was = logs.getVar('paths')
    if Gates not in Was:
        New = Was + [Gates]
        New.sort()
        logs.setVar('paths',New)
        print('registerWin',Gates)
    

def goodLogicCandidate(Nmoses,Pmoses):
    GP,GN,PS,NS = [],[],[],[]
    for Mos in Nmoses+Pmoses:
        Wmos = Mos.split()
        if Wmos[0] == 'nmos':
            if Wmos[2] not in NS: NS.append(Wmos[2])
            if Wmos[3] not in NS: NS.append(Wmos[3])
            if Wmos[1] not in GN: GN.append(Wmos[1])
        elif Wmos[0] == 'pmos':
            if Wmos[2] not in PS: PS.append(Wmos[2])
            if Wmos[3] not in PS: PS.append(Wmos[3])
            if Wmos[1] not in GP: GP.append(Wmos[1])
    Pbag = set(PS)
    Nbag = set(NS)

    Gpbag = set(GP)
    Gnbag = set(GN)

    Gbag = Gpbag-Gnbag

    X = Pbag.intersection(Nbag)
    if (len(X)==1)and(len(Gbag)==0):
        logs.log_info('CLUSTER out = %s   GG %s'%(X,Gbag))
        return list(X)[0]
    else:
        logs.log_info('CLUSTER inter = %s'%(X))
        return False


    
def labelDepthMos(Moses,Start,End,SofarMoses,SofarNets,SofarGates):
#    print('labelDepthMos',Moses,Start,End,'||||',SofarMoses,SofarNets,SofarGates)
    for Mos in Moses:
        Wmos = Mos.split()
        if Wmos[3] == Start:
            print('labelDepthMos3',Mos,'start',Start,End,'||||',SofarMoses,SofarNets,SofarGates)
            Up = Wmos[2]
            if Up==End:
                registerWin(SofarGates+[Wmos[1]])
                print('labelDepthMos3 win',Mos)
            elif (Up not in SofarNets):
                Down = Moses[:]
                Down.remove(Mos)
                DSofarMoses = SofarMoses + [Mos]
                DSofarNets  = SofarNets  + [Start]
                DSofarGates = SofarGates + [Wmos[1]]
                DSofarGates.sort()
                labelDepthMos(Down,Up,End,DSofarMoses,DSofarNets,DSofarGates)
        elif Wmos[2] == Start:
            print('labelDepthMos2',Mos,'start',Start,End,'||||',SofarMoses,SofarNets,SofarGates)
            Up = Wmos[3]
            if Up==End:
                registerWin(SofarGates+[Wmos[1]])
                print('labelDepthMos2 win',Mos)
            elif (Up not in SofarNets):
                Down = Moses[:]
                Down.remove(Mos)
                DSofarMoses = SofarMoses + [Mos]
                DSofarNets  = SofarNets  + [Start]
                DSofarGates = SofarGates + [Wmos[1]]
                DSofarGates.sort()
                labelDepthMos(Down,Up,End,DSofarMoses,DSofarNets,DSofarGates)
        






def matchCluster(Nmoses,Pmoses):
#    tryMatchLogicFunc(Nmoses,Pmoses)
    for Name in MOSPATTERNS:
        Npat,Ppat,Action = MOSPATTERNS[Name] 
        if (len(Npat)==len(Nmoses))and(len(Ppat)==len(Pmoses)):
            logs.setVar('pattern',Name)
            Match = matchDeep(Npat+Ppat,Nmoses+Pmoses,{},True)
            if Match:
                return activate(Action,Match)
    logs.log_info('pattern "%s %s" was not recognized'%(Nmoses,Pmoses))
    return False

def activate(Action,Match):

    Wact = Action.split()
    if Wact[0]=='expression':
        Wact = logs.splitQuotes(Action)

        CC = Wact[1].split('=')
        Pin = CC[0]
        Net = Match[CC[1]]
        Conns = [(Pin,Net)]
        Obj = Objx(Wact[0],Conns)

        CC = Wact[2].split('=')

        Obj.params[CC[0]] = CC[1]
        return [Obj]
    Conns = []
    for Conn in Wact[1:]:
        CC = Conn.split('=')
        Pin = CC[0]
        Net = Match[CC[1]]
        Conns.append((Pin,Net))

    Obj = Objx(Wact[0],Conns)
    logs.log_info('activation %s %s'%(Action,Match))
    return [Obj]

def matchDeep(Pat,Moses,Res={},Dbg=False):
    if Dbg: print('ENTER %s %s %s %s'%(logs.getVar('pattern'),Pat,Moses,Res))
    if (Pat==[])and(Moses==[]): return Res
    Pnow = Pat[0]
    for Mos in Moses:
        Res1 = matchMos(Pnow,Mos,Res,Dbg)
        if Res1:
            if Dbg: print('EE2 %s "%s" "%s" %s   %d %d '%(logs.getVar('pattern'),Pnow,Mos,Res1,len(Pat),len(Moses)))
            for Resx in Res1:
                Moses2 = Moses[:]
                Moses2.remove(Mos)
                Res2 = matchDeep(Pat[1:],Moses2,Resx,Dbg)
                if Res2: return Res2



    if Dbg: print('FAILED %s "%s" %s   %d %d '%(logs.getVar('pattern'),Pnow,Res,len(Pat),len(Moses)))
    return False
    

def matchMos(Pnow,Mos,Res,Dbg=False):
    Wmos = Mos.split()
    Wpat = Pnow.split()
    if Wmos[0]!=Wpat[0]: 
        if Dbg: print('matchMos false0 ',Wmos,Wpat)
        return False

    if Wmos[3] in ['vss','vdd']:
        if Wmos[3] != Wpat[3]: 
            if Dbg: print('matchMos false1 ',Wmos,Wpat)
            return False
    elif Wpat[3] in ['vss','vdd']:
        if Dbg: print('matchMos false1 ',Wmos,Wpat)
        return False

    if Wpat[1][0]=='?':
        if not Res: return False
        if Wpat[1] in Res:
            if Wmos[1] != Res[Wpat[1]]:
                if Dbg: print('matchMos false2 ',Wmos,Wpat)
                return False
        else:
            Res = Res.copy()
            Res[Wpat[1]] = Wmos[1]
    elif Wpat[1]!=Wmos[1]:
        if Dbg: print('matchMos false3 ',Wmos,Wpat)
        return False
    Res0 = matchMos23(Wpat,Wmos,Res,Dbg)    
    if Wmos[3] in ['vdd','vss']:
        return [Res0]
    Res1 = matchMos23(Wpat,[Wmos[0],Wmos[1],Wmos[3],Wmos[2]],Res,Dbg)    
    if Res1 and Res0:
        return [Res0,Res1]
    elif Res0:
        return [Res0]
    elif Res1:
        return [Res1]
    else: 
        return False

def matchMos23(Wpat,Wmos,Res,Dbg):
    if Wpat[2][0]=='?':
        if Wpat[2] in Res:
            if Wmos[2] != Res[Wpat[2]]:
                if Dbg: print('matchMos false4 ',Wmos,Wpat)
                return False
        else:
            Res = Res.copy()
            Res[Wpat[2]] = Wmos[2]
    elif Wpat[2]!=Wmos[2]:
        if Dbg: print('matchMos false5 ',Wmos,Wpat)
        return False
    
    if Wpat[3][0]=='?':
        if Wpat[3] in Res:
            if Wmos[3] != Res[Wpat[3]]:
                if Dbg: print('matchMos false6 ',Wmos,Wpat)
                return False
        else:
            Res = Res.copy()
            Res[Wpat[3]] = Wmos[3]
    elif Wpat[3]!=Wmos[3]:
        if Dbg: print('matchMos false7 ',Wmos,Wpat)
        return False
    
    if Dbg: print('matchMos true ',Wmos,Wpat,Res)
    return Res





    



def match(Pat,Wrds,Res={}):
    print('ENTER %s %s %s'%(Pat,Wrds,Res))
    if (Pat==[])and(Wrds==[]): return Res
    if Pat[0]==Wrds[0]:
        return match(Pat[1:],Wrds[1:],Res)

    if Pat[0][0]=='?':
        Key = Pat[0][1:]
        if Key in Res:
            Prev = Res[Key]
            if Prev != Wrds[0]: 
                if Wrds[0] in Res.values():
                    Reverse = reverseDict(Res)

                    


                print('EXIT1',Pat[0],Wrds[0],Res)
                return False
            return match(Pat[1:],Wrds[1:],Res)
        else:
            Dres = Res.copy()
            Dres[Pat[0][1:]] = Wrds[0]
            return match(Pat[1:],Wrds[1:],Dres)

    print('EXIT2',Pat[0],Wrds[0],Res)
    return False


def matchBasics(Nmoses,Pmoses):
    Invs,Nmoses0,Pmoses0 = matchBasicInvs(Nmoses,Pmoses)
    Cmoses,Nmoses1,Pmoses1 = matchBasicCmos(Nmoses0,Pmoses0)
    Caps = []
    Nmoses2 = []
    for Nmos in Nmoses1:
        Wrds = Nmos.split()
        if (Wrds[2]==Wrds[3])and(Wrds[2]=='vss'):
            Caps.append('cap %s'%Wrds[1])
        else:
            Nmoses2.append(Nmos)
            
    Res =  {'inv':Invs,'cmos':Cmoses,'nmos':Nmoses2,'pmos':Pmoses1}
    if Caps!=[]:
        Res['cap'] = Caps
    return Res

def matchBasicInvs(Nmoses,Pmoses):
    Invs0 = {}
    Invs = []
    Nmoses0 = Nmoses[:] 
    for Mos in Nmoses0:
        Wmos = Mos.split()
        if Wmos[3]=='vss':
            Key = Wmos[1],Wmos[2]
            Invs0[Key] = Mos
    Pmoses0 = Pmoses[:]
    for Mos in Pmoses:
        Wmos = Mos.split()
        if Wmos[3]=='vdd':
            Key = Wmos[1],Wmos[2]
            if Key in Invs0:
                Invs.append('inv %s %s'%(Wmos[2],Wmos[1]))
                Nmos = Invs0[Key]
                Nmoses0.remove(Nmos)
                Pmoses0.remove(Mos)
    return Invs,Nmoses0,Pmoses0

def matchBasicCmos(Nmoses,Pmoses):
    Cmoses0 = {}
    Cmoses = []
    Nmoses0 = Nmoses[:] 
    for Mos in Nmoses0:
        Wmos = Mos.split()
        if Wmos[3]!='vss':
            Key = Wmos[2],Wmos[3]
            Cmoses0[Key] = Mos,Wmos[1]
    Pmoses0 = Pmoses[:]
    for Mos in Pmoses:
        Wmos = Mos.split()
        if Wmos[3]!='vdd':
            Pg = Wmos[1]
            Key = Wmos[2],Wmos[3]
            Key2 = Wmos[3],Wmos[2]
            if Key in Cmoses0:
                Nmos,Ng = Cmoses0[Key]
                Nmoses0.remove(Nmos)
                Pmoses0.remove(Mos)
                Cmoses.append('cmos %s %s %s %s'%(Ng,Pg,Wmos[2],Wmos[3]))
            elif Key2 in Cmoses0:
                Nmos,Ng = Cmoses0[Key]
                Nmoses0.remove(Nmos)
                Pmoses0.remove(Mos)
                Cmoses.append('cmos %s %s %s %s'%(Ng,Pg,Wmos[2],Wmos[3]))
    return Cmoses,Nmoses0,Pmoses0

PATTERNS2 = {}


def matchLevel2(Clust):
    Len = 0
    for Key in Clust:
        Len += len(Clust[Key])
    for Name in PATTERNS2:
        Items,Action = PATTERNS2[Name]
        if (len(Items)<=Len):
            logs.setVar('pattern',Name)
            Clust = matchDeep2(Items,Clust,Action,{},True)
    return Clust


def matchDeep2(Pat,Clust,Action,Res={},Dbg=False):
    if Dbg: print('ENTER %s %s %s %s'%(logs.getVar('pattern'),Pat,Moses,Res))
    if (Pat==[])and(Moses==[]): return Res
    Pnow = Pat[0]
    for Mos in Moses:
        Res1 = matchMos(Pnow,Mos,Res,Dbg)
        if Res1:
            if Dbg: print('EE2 %s "%s" "%s" %s   %d %d '%(logs.getVar('pattern'),Pnow,Mos,Res1,len(Pat),len(Moses)))
            for Resx in Res1:
                Moses2 = Moses[:]
                Moses2.remove(Mos)
                Res2 = matchDeep(Pat[1:],Moses2,Resx,Dbg)
                if Res2: return Res2



    if Dbg: print('FAILED %s "%s" %s   %d %d '%(logs.getVar('pattern'),Pnow,Res,len(Pat),len(Moses)))
    return False






