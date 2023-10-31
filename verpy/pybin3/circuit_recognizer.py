

import logs
import clusterizer
import copy
import module_class
import patterns3

Patterns = []
Patterns.append(([['nmos', 'in0', 'wire16', 'out'], ['nmos', 'in1', 'gnd', 'wire16'], ['pmos', 'in0', 'vcc', 'out'], ['pmos', 'in1', 'vcc', 'out']],['ig_nand2 o=out i1=in0 i2=in1']))
Patterns.append(([['nmos', 'in0', 'gnd', 'out'], ['pmos', 'in0', 'vcc', 'out']],['ig_inv o=out i=in0 pbulk=vcc nbulk=gnd']))
Patterns.append(([['nmos', 'D0', 'net01', 'gnd'], ['nmos', 'D1', 'net04', 'gnd'], ['nmos', 'SL0', 'net03', 'net04'], ['nmos', 'SL0N', 'net03', 'net01'], ['pmos', 'D0', 'net02', 'vcc'], ['pmos', 'D1', 'net05', 'vcc'], ['pmos', 'SL0', 'net03', 'net02'], ['pmos', 'SL0N', 'net03', 'net05']],['ig_mux2 out=net03 sel=SL0 selb=SL0N in0=D0 in1=D1']))

Patterns.append(([['nmos', 'in0', 'wire16', 'out'], ['nmos', 'in1', 'wire1', 'wire16'], ['nmos', 'in2', 'gnd', 'wire1'], ['pmos', 'in0', 'vcc', 'out'], ['pmos', 'in1', 'vcc', 'out'], ['pmos', 'in2', 'vcc', 'out']],['ig_nand3 out=o in0=i1 in1=i2 in2=i3']))

Patterns.append(( [['nmos', 'in0', 'gnd', 'out'], ['nmos', 'in1', 'gnd', 'out'], ['pmos', 'in0', 'wire25', 'out'], ['pmos', 'in1', 'vcc', 'wire25']]
                  ,['ig_nor2 out=o in0=i1 in1=i1']))
Patterns.append(( [['nmos', 'in0', 'gnd', 'out'], ['nmos', 'in1', 'gnd', 'out'], ['nmos', 'in2', 'gnd', 'out'], ['pmos', 'in0', 'wire3', 'wire25'], ['pmos', 'in1', 'wire25', 'out'], ['pmos', 'in2', 'vcc', 'wire3']]
    ,['ig_nor3 out=out in0=in0 in1=in1 in2=in2']))

Patterns.append((  [['nmos', 'in0', 'wire16', 'out'], ['nmos', 'in1', 'wire1', 'wire16'], ['nmos', 'in2', 'wire7', 'wire1'], ['nmos', 'in3', 'gnd', 'wire7'], ['pmos', 'in0', 'vcc', 'out'], ['pmos', 'in1', 'vcc', 'out'], ['pmos', 'in2', 'vcc', 'out'], ['pmos', 'in3', 'vcc', 'out']]
    ,['ig_nand4  o=out i1=in0 i2=in1 i3=in2 i4=in3 nbulk=gnd pbulk=vcc']))

# Patterns.append(( [['nmos', 'dinb', 'gnd', 'outleft'], ['pmos', 'dinb', 'wire17', 'outleft'], ['pmos', 'outright', 'vcc', 'wire17']],['half_lvsh dinb outleft outright nbulk=gnd pbulk=vcc']))

Patterns.append(( [['nmos', 'en', 'wire77', 'out'], ['nmos', 'in', 'gnd', 'wire77'], ['pmos', 'in', 'vcc', 'wire74'], ['pmos', 'wire88', 'wire74', 'out']]
    ,['ig_trinv ngate=en pgate=wire88 i=in o=out nbulk=gnd pbulk=vcc']))

Patterns.append((  [['nmos', 'en', 'gnd', 'wire77'], ['nmos', 'in', 'wire77', 'out'], ['pmos', 'in', 'wire74', 'out'], ['pmos', 'wire87', 'vcc', 'wire74']]
    ,['ig_trinv ngate=en ngate=wire87 i=in o=out nbulk=gnd pbulk=vcc']))

Patterns2 = []
Patterns2.append(( [['cmos', 'sel', 'wire96', 'in1', 'gnd', 'out', 'vcc'], ['cmos', 'wire96', 'sel', 'in0', 'gnd', 'out', 'vcc'], ['inv', 'sel', 'wire96']],['ig_mux2o out=net03 sel=sel  in0=in0 in1=in1']))


Patterns3 = []
Patterns3.append(( ['ig_nand2 qq0 qq1 set','ig_nand2 qq1 qq0 rst'],['latch_sr qq0 qq1 set rst'] ))
Patterns3.append(( ['ig_nor2 qq0 qq1 set','ig_nor2 qq1 qq0 rst'],['latch_sr qq0 qq1 set rst'] ))
Patterns3.append(( ['ig_nor3 qq qqb set rst0','ig_nor2 qqb qq rst'],['latch_sr qq0=qq0 qq1=qqb set=set rst=rst rst0=rst0'] ))

def help_main(Env):
    Mod = Env.Current
    if len(Mod.insts.keys())> (5* (len(Patterns)+len(Patterns2))):
        Fout = open('%s.vcir' % Mod.Module,'w')
        Mod.dump_verilog(Fout)
        Fout.close()
        return
    Orig = copy.deepcopy(Mod)
    Env.DontFlattens = 'nmos pmos cmos inv buf nand2 nand3 nor2 nor3'.split()
    clusterizer.flattenDeep(Mod,Env)
    normalizeMosPins(Mod)
#    dbg0(Mod,'before')
    clusterizer.parallels(Mod,['nmos','pmos'])
#    dbg0(Mod,'after0')
    parallels2(Mod)
    dbg0(Mod,'after1')

    Dones = patterns3.run(Mod,Env)
    print("PATTERNS3 %s dones" % Dones)
#    dbg0(Mod,'after2')
#    Clusters = clusterizer.clusterFind2(Mod)
#    for Line,Participants in Clusters:
#        Dict,Target = scanPatterns(Line)
#        if Dict:
#            applyDict(Mod,Line,Dict,Target,Participants)
#            Dones += 1
#        else:
#            logs.log_error('pattern failed %s' % str(Line))
#
    Cline = clusterizer.cline0(Mod)
#    if len(Cline) > 1:
#        Dict,Target = scanPatterns2(Cline)
#        if Dict:
#            applyDict(Mod,Cline,Dict,Target,[])
#            Dones += 1
#        else:
#            logs.log_error('pattern2 failed %s' % str(Cline))

    retype_to_ig(Mod)
#    if Dones == 0: Mod = Orig
    Fout = open('%s.vcir' % Mod.Module,'w')
    Cline2 = []
    for LL in Cline:
        Str = ' '.join(LL)
        Cline2.append(Str)
    Fout.write('//pattern %s\n' % Cline2)
    Mod.buildNetTable()
    for Net in Mod.netTable:
        Fout.write('//pattern %s %d %s\n' % (Net,len(Mod.netTable[Net]),Mod.netTable[Net]))
    Mod.dump_verilog(Fout)
    Fout.close()
Logics = '''buf inv and2 and3 and4 and5 and6 or2 or3 or4 or5 or6 nand2 nand3 nand4 nand5 nand6 
    nor2 nor3 nor4 nor5 nor6 xnor2 xnor3 xnor4 xnor5 xnor6 xor2 xor3 xor4 xor5 xor6
    or7 or8 or9 or10 nor7 nor8 nor9 nor10 
    and7 and8 and9 and10 nand7 nand8 nand9 nand10 
'''.split()
def retype_to_ig(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == 'nmos': Obj.Type = 'ig_nmos'
        if Obj.Type == 'pmos': Obj.Type = 'ig_pmos'
        if Obj.Type in Logics: Obj.Type = 'ig_'+Obj.Type

Moses = ['nmos','pmos','dgvnfet','dgvpfet','nfet','pfet','dgxnfet','dgxpfet','dgnfet','dgpfet']
def isMos(Type):
    if Type in NOTMOS: return False
    return Type in Moses
def isNmos(Type):
    if Type in NOTMOS: return False
    return ('nmos' in Type) or ('nfet' in Type)
def isPmos(Type):
    if Type in NOTMOS: return False
    return ('pmos' in Type) or ('pfet' in Type)
def voltage(Type):
    if Type in ['nfet','pfet']: return "1.2"
    if Type in ['dgvnfet','dgvpfet']: return "1.8"
    if Type in ['dgxnfet','dgxpfet']: return "3.3"
    return "1.8"





NOTMOS = {}
def normalizeMosPins(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if (Obj.Type == 'nmos') and ('bulk' not in Obj.conns): Obj.conns['bulk'] = 'gnd'
        if (Obj.Type == 'pmos') and ('bulk' not in Obj.conns): Obj.conns['bulk'] = 'vcc'
        if isNmos(Obj.Type) or isPmos(Obj.Type):
            if isNmos(Obj.Type): Obj.Type = 'nmos'
            if isPmos(Obj.Type): Obj.Type = 'pmos'
            if 'D' in Obj.conns:
                Obj.conns['o'] = Obj.conns['D']
                Obj.conns.pop('D')
            if 'd' in Obj.conns:
                Obj.conns['o'] = Obj.conns['d']
                Obj.conns.pop('d')
            if 's' in Obj.conns:
                Obj.conns['i'] = Obj.conns['s']
                Obj.conns.pop('s')
            if 'gate' in Obj.conns:
                Obj.conns['g'] = Obj.conns['gate']
                Obj.conns.pop('gate')
            if 'S' in Obj.conns:
                Obj.conns['i'] = Obj.conns['S']
                Obj.conns.pop('S')
            if 'G' in Obj.conns:
                Obj.conns['g'] = Obj.conns['G']
                Obj.conns.pop('G')
            if 'B' in Obj.conns:
                Obj.conns['bulk'] = Obj.conns['B']
                Obj.conns.pop('B')
            if 'bulk' not in Obj.conns:
                NOTMOS[Obj.Type] = True


def scanPatterns2(Line):
    for Pattern in Patterns2:
        if len(Pattern[0]) == len(Line):
            Dict = matchPattern(Pattern[0],Line,{})
            if Dict: 
                print("DICT",Dict)
                return Dict,Pattern[1]
    return False,False


def scanPatterns(Line):
    for Pattern in Patterns:
        if len(Pattern[0]) == len(Line):
            Dict = matchPattern(Pattern[0],Line,{})
            if Dict: 
                print("DICT",Dict)
                return Dict,Pattern[1]
    return False,False

def applyDict(Mod,Line,Dict,Target,Participants):
    wrds  = Target[0].split()
    Obj = Mod.add_inst(wrds[0],'')
    for wrd in wrds[1:]:
        ww = wrd.split('=')
        print(ww,wrd,'XXXXX',Obj.conns,Obj.Type)
        if len(ww) == 1:
            Obj.conns[ww[0]] = Dict[ww[0]]
        else:
            Obj.conns[ww[0]] = Dict[ww[1]]

    for Mos in Participants:
        if Mos in Mod.insts:
            Mod.insts.pop(Mos)


def matchPattern(Pattern,Line,Dict):
    if Pattern == []: 
        print("OKx",len(Pattern),Dict)
        return Dict
    Pat0 = Pattern[0]
    for ind,Item in enumerate(Line):
        Dict0 = Dict.copy()
        Dict1 = Dict.copy()
#        print("matchMos",len(Pattern),Pat0,Item,Dict0)
        if matchMos(Pat0,Item,Dict0,0):
            Line0 =  Line[:]
            Line0.pop(ind)
            Ok = matchPattern(Pattern[1:],Line0,Dict0.copy())            
            if Ok: 
                print("OK0",len(Pattern),Pat0,Item,Ok)
                return Ok
            print("fail0 matchMos",len(Pattern),Pat0,Item,Dict0)
        if matchMos(Pat0,Item,Dict1,1):
            Line0 =  Line[:]
            Line0.pop(ind)
            Ok = matchPattern(Pattern[1:],Line0,Dict1.copy())            
            if Ok: 
                print("OK1",len(Pattern),Pat0,Item,Ok)
                return Ok
            print("fail1 matchMos",len(Pattern),Pat0,Item,Dict1)
        
    return False

def matchMos(Pat,Item,Dict,Which):
    if Pat[0] != Item[0]: return False
    if Pat[1] in Dict:
        if (Dict[Pat[1]] != Item[1]): return False
    else:
        Dict[Pat[1]] = Item[1]

    if Pat[2] in Dict:
        Act = Dict[Pat[2]]
        if Act not in Item[2:]: return False
    else:
        print("NNN0",Which,'item3=',Item[3],'item2=',Item[2],'pat[2]=',Pat[2],Dict)

        if Which:
            if Item[3] in Dict.values():  return False
            Dict[Pat[2]] = Item[3]
        else:
            if Item[2] in Dict.values():  return False
            Dict[Pat[2]] = Item[2]

    print("MATCH0",Which,Dict,Pat,Item)

    if Pat[3] in Dict:
        Act = Dict[Pat[3]]
        if Act not in Item[2:]: return False
    else:
        if Which:
            if Item[2] in Dict: return False
            Dict[Pat[3]] = Item[2]
        else:
            if Item[3] in Dict: return False
            Dict[Pat[3]] = Item[3]
    print("MATCH",Dict,Pat,Item)
    return Dict


def dbg0(Mod,When):
    Fout = open(When,'w')
    Mod.dump_verilog(Fout)
    Fout.close()
                 
def longSerials(Mod,isNmos):
    Mod.buildNetTable()
    Res = {}
    for Inst0 in Mod.insts:
        Obj0 = Mod.insts[Inst0]
        if isNmos(Obj0.Type):
            SD0 = getSD(Obj0)
            Bulk = Obj0.conns['bulk']
            if Bulk in SD0: 
                SD0.remove(Bulk)
                Mid0 = SD0[0]
                Insts = [Inst0]
                Gates = [module_class.hashit(Mod.insts[Inst0].conns['g'])]
                Ok = True 
                while Ok and is2Xnet(Mid0,Mod):
                    Inst1 = otherMos(Mod,Inst0,Mid0)
                    if Inst1:
                        Mid1 = otherSide(Mod,Inst1,Mid0)
                        Mid0 = Mid1 
                        Inst0 = Inst1
                        Insts.append(Inst1)
                        Gates.append(module_class.hashit(Mod.insts[Inst0].conns['g']))
                    else:
                        Ok = False
                if len(Insts)>=2:     
                    Gates.sort()
                    Gates = tuple(Gates)
                    if (Mid0,Bulk,Gates) not in Res: Res[(Mid0,Bulk,Gates)] = []
                    Res[(Mid0,Bulk,Gates)].append((Insts))
    return Res

def parallels2(Mod):
    longsN = longSerials(Mod,isNmos)
    longsP = longSerials(Mod,isPmos)
    parallels2work(Mod,longsN)
    parallels2work(Mod,longsP)

def parallels2work(Mod,longs):
    for Out,Bulk,Gates in longs:
        List = longs[(Out,Bulk,Gates)]
        if len(List)>1:
            for LL in List[1:]:
                for Inst in LL:
                    Mod.insts.pop(Inst)
            

def __getSD(Obj):
    try:
        S = module_class.hashit(Obj.conns['i'])
        D = module_class.hashit(Obj.conns['o'])
        Res = [S,D]
        Res.sort()
        return Res
    except:
        logs.log_error('getSD on %s %s got %s' % (Obj.Name,Obj.Type,Obj.conns))
        return [0,0]

def getSD(Obj):
    S = module_class.hashit(Obj.conns['i'])
    D = module_class.hashit(Obj.conns['o'])
    Res = [S,D]
    Res.sort()
    return Res

def is2Xnet(Net,Mod):
    NN = module_class.hashit(Net)
    if NN in Mod.netTable:
        List = Mod.netTable[NN]
        if len(List) != 2: return False
        if List[0][0] == Mod.Module: return False
        if List[1][0] == Mod.Module: return False
        return True 
    return False 

def otherMos(Mod,Inst,Mid):
    List = Mod.netTable[Mid]
    LL = [] 
    for Instx,Typex,Pinx in List:
        if (Instx != Mod.Module)and isMos(Typex):
            LL.append(Instx)
    if (len(LL) == 2) and (Inst in LL): 
        LL.remove(Inst)
        return LL[0]
    return False
         

def otherMos(Mod,Inst,Mid):
    List = Mod.netTable[Mid]
    LL = [] 
    for Instx,Typex,Pinx in List:
        if (Instx != Mod.Module)and isMos(Typex):
            LL.append(Instx)
    if (len(LL) == 2) and (Inst in LL): 
        LL.remove(Inst)
        return LL[0]
    return False
     

def otherSide(Mod,Inst,One):
    Obj = Mod.insts[Inst]
    Sh = module_class.hashit(Obj.conns['i'])
    Dh = module_class.hashit(Obj.conns['o'])
    if One == Sh: return Dh 
    if One == Dh: return Sh 
    logs.log_error('otherSide %s %s %s %s' % (Mod.Module,Inst,One,Obj.conns))
    return One





