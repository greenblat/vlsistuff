
import importlib
import sys,os
import module_class
import logs

def run(Mod,Env):
    Patfile = Env.params['-patterns'][0]
    Path0 = os.path.abspath(Patfile)
    Fname = os.path.basename(Path0)
    Path = os.path.dirname(Path0)
    Fname = Fname.replace('.py','')
    sys.path.append(Path)
    PatSet = importlib.import_module(Fname)
    hashitModule(Mod)
    addBulks(Mod)
    Mod.buildNetTable()
    Patid = False
    if '-patid' in Env.params:
        Patid = Env.params['-patid']
    Ok = True
    Dones = 0
    while Ok:
        Ok = False
        Run = 0
        while Run < len(PatSet.Pattern):
            if (not Patid or (str(Run) in Patid)):
                Rule,Targets,Pattern =  PatSet.Pattern[Run]
                if Targets == 'procedure':
                    Dones = eval('%s(Mod)' % Rule)
                    Ok = Dones>0
                    Run += 1
                else:
                    if type(Targets) is str:
                        Targets = [Targets]
                    logs.setVar('target',Targets[0])
                    Dict,Participants = checkPattern(Pattern,Mod)
                    if Dict:
                        logs.log_info('try apply %s rule' % (Rule))
                        Res = applyDict(Mod,Targets,Dict,Participants)
                        Mod.buildNetTable()
                        Ok = True
                        Dones += 1
                        Details = detailsOfInsts(Mod,Res)
                        logs.log_info('apply %s rule new= %s    <-- %s' % (Rule,Details,Participants))
                    else:
                        Run += 1
            else:
                Run += 1

    dehashitModule(Mod)
    return Dones

def addBulks(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if logicType(Obj.Type): 
            if 'nbulk' not in Obj.conns:    
                Obj.conns['nbulk'] = 'gnd'
            if 'pbulk' not in Obj.conns:    
                Obj.conns['pbulk'] = 'vcc'


def detailsOfInsts(Mod,Res):
    Str = ''
    for Type,Inst in Res:
        if Inst in Mod.insts:
            Obj = Mod.insts[Inst]
            Str += '( %s %s ' % (Type,Inst)
            Pins = list(Obj.conns.keys())
            Pins.sort()
            for Pin in Pins:
                Str += ' %s=%s' % (Pin,Obj.conns[Pin])
            Str += ' )' 
    return Str
def checkPattern(Pattern,Mod):
    Dict,Participants = matchPattern(Pattern,Mod,{},[],0)
    return Dict,Participants

def matchPattern(Pattern,Mod,Dict,Participants,Deep):
    if Pattern == []:
        return Dict,Participants
    Pat0 = Pattern[0]
    wrds = Pat0.split()
    Key = wrds[0]
    Target = logs.getVar('target')
    if (Key[0] in '23456789'):
        Many = int(Key[:-1])
        if wrds[1] in Dict:
            Sig = Dict[wrds[1]]
            List = Mod.netTable[hashit(Sig)]
            if len(List) != Many:
                return False,False
            return matchPattern(Pattern[1:],Mod,Dict,Participants,Deep+1)
        else:
            for Net in Mod.netTable:
                List = Mod.netTable[Net]
                if len(List) == Many:
                    Dict[wrds[1]] = Net
                    DD,PP =  matchPattern(Pattern[1:],Mod,Dict,Participants,Deep+1)
                    if DD: return DD,PP
            return False,False
    else:            
        for Type in Mod.typesTable:
            if compatibleType(Type,Key):
                ListInsts = Mod.typesTable[Type]
                for Inst in ListInsts:
                    runDict = Dict.copy()
                    if (Inst not in Participants) and (Inst in Mod.insts):
                        Obj = Mod.insts[Inst]
                        if compatibleType(Obj.Type,Key):
                            Ok = True
                            AllIns,NotIns = extractInputs(wrds[1:])
                            for PP in NotIns:
                                if PP.startswith('>'):
                                    Conn = PP[1:]
                                    Out = outputNet(Obj)
                                    Ok = Ok and mergeDict(Out,Conn,runDict)
                                elif '=' in PP:
                                    PPS = PP.split('=')
                                    Pin,Conn = PPS
                                    Out = Obj.conns[Pin]
                                    Ok = Ok and mergeDict(Out,Conn,runDict)
                            if Ok:
                                if AllIns != []:
                                    Ins = inputNets(Obj)
                                    if (len(Ins) == len(AllIns)):
                                        if (len(Ins)==1) and mergeDict(Ins[0],AllIns[0],runDict):
                                            DD,PP =  matchPattern(Pattern[1:],Mod,runDict.copy(),Participants+[Inst],Deep+1)
                                            if DD: return DD,PP
                                        else:
                                            Permutations = permutations(Ins)
                                            for Perm in Permutations:
                                                DD = runDict.copy()
                                                MM = mergeDict(Perm,AllIns,DD)
                                                if MM:
                                                    DD,PP =  matchPattern(Pattern[1:],Mod,DD,Participants+[Inst],Deep+1)
                                                    if DD: return DD,PP
                                else:    
                                    DD,PP =  matchPattern(Pattern[1:],Mod,runDict.copy(),Participants+[Inst],Deep+1)
                                    if DD: return DD,PP
                    
    return False,False                    
    
def extractInputs(wrds):
    Ins,Nots = [],[]
    for wrd in wrds:
        if wrd[0] == '<':
            Ins.append(wrd[1:])
        else:
            Nots.append(wrd)
    return Ins,Nots

def mergeDict(Out,Conn,Dict):
    if type(Conn) is str:
        if Conn in Dict:
            return Dict[Conn] == Out
        Dict[Conn] = Out
        return True
    else:
        for ind,Con in enumerate(Conn):
            OO = Out[ind]
            Ok = mergeDict(OO,Con,Dict)
            if not Ok: return False
        return True

def inputNets(Obj):
    if logicType(Obj.Type): 
        Res = []
        for Pin in Obj.conns:
            if Pin[0] == 'i':
                Res.append(Obj.conns[Pin])
        return Res
    if isMos(Obj.Type) or (Obj.Type == 'cmos'):
        Res = [Obj.conns['i'],Obj.conns['o']]
        return Res
    logs.log_error('inputNets %s' % Obj.Type)
    return []

def isMos(Type):
    return Type in ['nmos','pmos']

def outputNet(Obj):
    if logicType(Obj.Type): 
        for Pin in Obj.conns:
            if Pin[0] == 'o':
                Sig = Obj.conns[Pin]
                return Sig


def hashit(Net):
    return module_class.hashit(Net)

BasicLogic = 'and nand or nor xor xnor inv buf'.split()
def logicType(Type):
    if Type in BasicLogic: return True
    if Type[:-1] in BasicLogic: return True
    if Type[:-2] in BasicLogic: return True
    if 'ig_'+Type in BasicLogic: return True
    return False

def compatibleType(Type,Pat):
    if Type == Pat: return True
    if Pat in ['and','nand','or','nor','xor','xnor']:
        return Type.startswith(Pat)
    if Type.startswith('ig_'): return compatibleType(Type[3:],Pat)
    return False

def applyDict(Mod,Targets,Dict,Participants):
    Res = []
    for Target in Targets:
        ww = Target.split()
        if ww[0] == 'rename':
            renameNets(Mod,Dict[ww[1]],Dict[ww[2]])
        else: 
            if '#' in ww[-1]: ww.pop(-1)
            Obj = Mod.add_inst(ww[0],'')
            Res.append((Obj.Type,Obj.Name))
            for wrd in ww[1:]:
                ps = wrd.split('=')
                if ps[1] not in Dict:
                    Dict[ps[1]] = Mod.add_sig('','wire',0)
                Obj.conns[ps[0]] = Dict[ps[1]]
         
            for Was in Participants:
                if Was in Mod.insts:
                    Mod.insts.pop(Was)

    renameNets(Mod,False,False)
    return Res

def renameNets(Mod,From,To):
    Used = {}
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            if From and (Sig == From):
                Obj.conns[Pin] = To
                logs.log_info('replace pin=%s  %s to %s in %s %s' % (Pin,From,To,Inst,Obj.Type))
            else:
                Used[Sig] = True
    for Net in list(Mod.nets.keys()):
        if Net not in Used:
            Dir,_ = Mod.nets[Net]
            if ('input' not in Dir) and ('output' not in Dir) and ('inout' not in Dir):
                Mod.nets.pop(Net)
    drivingNull(Mod)

def drivingNull(Mod):
    Mod.buildNetTable()
    dones = 0
    for Net in list(Mod.netTable.keys()):
        List = Mod.netTable[Net]
        if (Net not in ['vcc','gnd']) and (len(List) == 1) and (List[0][1] not in ['input','output','inout']):
            [Inst,Type,Pin] = List[0] 
            Obj = Mod.insts[Inst]
            if Net == outputNet(Obj):
                Mod.insts.pop(Inst)
                Mod.netTable.pop(Net)
                Mod.nets.pop(Net)
                dones += 1
    return dones

def dehashitModule(Mod):
    Mod.buildNetTable()
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type in ['nmos','pmos']:
            if 'bulk' in Obj.conns:
                Bulk = Obj.conns['bulk']
                if Obj.conns['o'] == Bulk:
                    Obj.conns['o'] = Obj.conns['i']
                    Obj.conns['i'] = Bulk

    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = dehashit(Obj.conns[Pin])
            Obj.conns[Pin] = Sig
        if 'bulk' in Obj.conns:
            Power = Obj.conns['bulk']
            Mod.nets[Power] = 'input',0
        if 'pbulk' in Obj.conns:
            Power = Obj.conns['pbulk']
            Mod.nets[Power] = 'input',0
        if 'nbulk' in Obj.conns:
            Power = Obj.conns['nbulk']
            Mod.nets[Power] = 'input',0

    for Net in list(Mod.nets.keys()):
        Dir,Wid = Mod.nets[Net]
        if Net not in Mod.netTable:
            Mod.nets.pop(Net)
        else:           
            Len = len(Mod.netTable[Net])
            if (Dir in ['input','output']) and (Len == 2) and ('[' in Net):
                Mod.nets.pop(Net)
    


def dehashit(Sig):
    if '[' not in Sig: return Sig
    Sig = Sig.replace('[',' ')
    Sig = Sig.replace(']',' ')
    ww = Sig.split()
    return ['subbit',ww[0],ww[1]]


def hashitModule(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = hashit(Obj.conns[Pin])
            Obj.conns[Pin] = Sig

    for Net in list(Mod.nets.keys()):
        Dir,Wid = Mod.nets[Net]
        if Wid in [0,1]:
           pass 
        elif type(Wid) is tuple:
            (Hi,Lo) = Wid
            for ii in range(Lo,Hi+1):
                Mod.nets['%s[%s]' % (Net,ii)] = Dir,0


FriendsAnd = 'and2 and3 and4 and5 and6 and7 and8 and9 and10'.split()
FriendsOr = 'or2 or3 or4 or5 or6 or7 or8 or9 or10'.split()
FriendsNand = 'nand2 nand3 nand4 nand5 nand6 nand7 nand8 nand9 nand10'.split()
FriendsNor = 'nor2 nor3 nor4 nor5 nor6 nor7 nor8 nor9 nor10'.split()
def followingAndsOrs(Mod):
    A = followingWork(Mod,FriendsAnd,'and')
    B = followingWork(Mod,FriendsOr,'or')
    C = identicalLogicGates(Mod,FriendsAnd+FriendsOr+FriendsNor+FriendsNand)
    D = drivingNull(Mod)
    E = and2inv(Mod,FriendsAnd)+and2inv(Mod,FriendsOr)
    return A+B+C+D+E

def and2inv(Mod,Friends):
    dones = 0
    Used = []
    Mod.buildNetTable()
    for Type in Friends:
        if Type in Mod.typesTable:
            Insts = Mod.typesTable[Type]
            for Inst in Insts:
                if (Inst in Mod.insts) and (Inst not in Used):
                    Obj = Mod.insts[Inst]
                    Out = outputNet(Obj)                
                    if is2XNet(Out,Mod):
                        List = Mod.netTable[Out]
                        if List[0][0] == Inst:
                            Inst2,Type2,Pin2 = List[1]
                        else:
                            Inst2,Type2,Pin2 = List[0]
                        if Type2 == 'inv':
                            Newtype = invertedType(Type)
                        elif Type2 == 'buf':
                            Newtype = Type
                        else:
                            Newtype = False
                        if Newtype:
                            Obj.Type = Newtype
                            Obj2 = Mod.insts[Inst2]
                            Out2 = outputNet(Obj2)                
                            Obj.conns['o1'] = Out2
                            Mod.insts.pop(Inst2)
                            dones += 1
    return dones

def invertedType(Type):
    if Type.startswith('and'): return 'n'+Type
    if Type.startswith('nand'): return Type[1:]
    if Type.startswith('or'): return 'n'+Type
    if Type.startswith('nor'): return Type[1:]
                            
    
def identicalLogicGates(Mod,Friends):
    Used = []
    dones = 0
    Keep = {}
    Mod.buildNetTable()
    for Type in Friends:
        if Type in Mod.typesTable:
            Insts = Mod.typesTable[Type]
            for Inst in Insts:
                if (Inst in Mod.insts) and (Inst not in Used):
                    Obj = Mod.insts[Inst]
                    Ins = inputNets(Obj)
                    Ins.sort()
                    Out = outputNet(Obj)                
                    Key = Type,tuple(Ins)
                    if Key not in Keep: Keep[Key] = []
                    Keep[Key].append((Inst,Out))
    Renames = []
    for Type,Ins in Keep:
        List = Keep[(Type,Ins)]
        if len(List) > 1:
            Out = List[0][1]
            Inst = List[0][0]
            Obj = Mod.insts[Inst]
            for Inst2,Out2 in List[1:]:
                Obj2 = Mod.insts[Inst2]
                mergeBulks(Obj,Obj2)
                Mod.insts.pop(Inst2)
                Renames.append((Out2,Out))

    for From,To in Renames:
        renameNets(Mod,From,To)
        dones += 1
    return dones

def mergeBulks(Obj,Obj2):
    if 'pbulk' not in Obj.conns:
        if 'pbulk' in Obj2.conns:
            Obj.conns['pbulk'] = Obj2.conns['pbulk']
        
    if 'nbulk' not in Obj.conns:
        if 'nbulk' in Obj2.conns:
            Obj.conns['nbulk'] = Obj2.conns['nbulk']
    
def followingWork(Mod,Friends,Base):
    Used = []
    dones = 0
    Mod.buildNetTable()
    for Type in Friends:
        if Type in Mod.typesTable:
            Ands = Mod.typesTable[Type]
            for And in Ands:
                if (And in Mod.insts) and (And not in Used):
                    Obj = Mod.insts[And]
                    Out = outputNet(Obj)                
                    LL = Mod.netTable[Out]
                    if len(LL)>=2:
                        if And == LL[0][0]:
                            And2,Type2,Pin2 = LL[1]
                        else:
                            And2,Type2,Pin2 = LL[0]
                        if (Type2 in Friends) and (Pin2[0] == 'i') and (And2 in Mod.insts) and (And2 not in Used):
                            Ins1 = inputNets(Obj)
                            Ins2 = inputNets(Mod.insts[And2])
                            Ins2.remove(Out)
                            Ins = Ins1 + Ins2
                            Type3 = Base + str(len(Ins))
                            Out3 = outputNet(Mod.insts[And2])
                            New = Mod.add_inst_conns(Type3,'',[('o1',Out3)])
                            for ind,Inx in enumerate(Ins):
                                New.conns['i%s' % (1+ind)] = Inx
                            Obj2 = Mod.insts[And2]
                            mergeBulks(New,Obj)
                            mergeBulks(New,Obj2)
                            Mod.insts.pop(And2)
                            Used.append(And)
                            Used.append(And2)
                            dones += 1
    if dones>0:
        return followingWork(Mod,Friends,Base)
    return 0
                        
                
def is2XNet(Out,Mod):
    if Mod.is_external(Out): return False
    return len(Mod.netTable[Out]) == 2
        



import itertools

def permutations(list1):
    return list(itertools.permutations(list1))


