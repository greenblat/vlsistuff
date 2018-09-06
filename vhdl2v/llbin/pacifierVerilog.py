
import string,types
import  module_class
import logs

def pacifier(Mod):
    for Always in Mod.alwayses:
        Sense = Always[0]
        declareRegs(Mod,Always[1])

        if (len(Always[1])==2)and(Always[1][0]=='list'):
            Top = Always[1][1]
            if Top[0]=='ifelse':
                ClkRst = extractClkRst(Top)
                if type(ClkRst)==types.TupleType:
                    Clk,Rst = ClkRst
                    Always[0] = ['list',Clk,Rst]
                    Always[1][1][3][1] = '1'
            elif Top[0]=='if':
                ClkRst = extractClkRst(Top)
                if type(ClkRst)==types.TupleType:
                    Clk,_ = ClkRst
                    Always[0] = Clk
            else:
                Always[0]='*'

def extractClkRst(Top):
    if len(Top)==4:
        Vars =  matches(Top[1],'== ? ?')
        if Vars:
            Rst = Vars[0]
            if notZeroValue(Vars[1]):
                RR = ('edge','posedge',Rst)
            else:
                RR = ('edge','negedge',Rst)
        else: 
            return False
        if Top[3][0]=='if':
            Vars =  matches(Top[3][1],['&', ['functioncall', 'edge', ['?']], ['==', '?', '?']])
            if Vars and (len(Vars)==3) and (Vars[0]==Vars[1]):
                Clk = Vars[0]
                if notZeroValue(Vars[2]):
                    CC = ('edge','posedge',Clk)
                else:
                    CC = ('edge','negedge',Clk)
                return  CC,RR
            else:
               return False

            
    logs.log_info('extractClkRst %s %s %s %s'%(Top[0],Top[1],Top[3][0],Top[3][1]))
    return False



def declareRegs(Mod,Struct):
    Regs = scanForRegs(Struct)
    for Net in Regs:
        Dir,Wid = Mod.nets[Net]
        if Dir=='wire':
            Mod.nets[Net] = ('reg',Wid)
        elif Dir=='output':
            Mod.nets[Net] = ('output reg',Wid)
        else:
            logs.log_error('net %s tried to be reg'%Net)

def scanForRegs(Struct):
    Regs=[]
    if (type(Struct) ==  types.ListType)and(len(Struct)==1):
        return scanForRegs(Struct[0])
    if (type(Struct) ==  types.ListType)and(Struct[0]=='<='):
        Nets = module_class.support_set(Struct[1],False)
        for Net in Nets:
            if Net not in Regs: Regs.append(Net)
            return Regs
    if (type(Struct) ==  types.ListType)and(Struct[0]=='list'):
        for Item in Struct:
            More = scanForRegs(Item)
            for Net in More:
                if Net not in Regs: Regs.append(Net)
        return Regs
    if (type(Struct) ==  types.ListType):
        if (Struct[0]=='if'):
            return scanForRegs(Struct[2])
        if (Struct[0]=='ifelse'):
            More = scanForRegs(Struct[2])+scanForRegs(Struct[3])
            for Net in More:
                if Net not in Regs: Regs.append(Net)
            return Regs
        if (Struct[0]=='case'):
            LL = Struct[2]
            for Case in LL:
                PP = Case[1]
                More = scanForRegs(PP)
                for Net in More:
                    if Net not in Regs: Regs.append(Net)
            return Regs

    if type(Struct) in [types.StringType,types.IntType]: return []

    logs.log_error('scanForRegs encountered "%s"'%Struct)
    return Regs


KNOWNFUNCTIONS = string.split('ext sxt resize conv_std_logic_vector conv_integer unsigned')
def matches(List,Seq):
    if type(Seq)==types.ListType:
        return listMatches(List,Seq)
    Lseq = string.split(Seq)
    if len(List)!=len(Lseq): return False
    Vars=[]
    for ind,Iseq in enumerate(Lseq):
        if Iseq == '?': 
            Vars.append(List[ind])
        elif Iseq == '$': 
            Who = List[ind]
            if Who in KNOWNFUNCTIONS:
                Vars.append(List[ind])
            else:
                return False

        elif (Iseq!=List[ind]):
            return False
    if Vars==[]: return True 
    return Vars 
     
def notZeroValue(Val):
    if Val=='0': return False
    if Val=='1': return True
    try:
        X = eval(Val)
        if X!=0: return True
    except:
        return False

def listMatches(List,Seq):
    if type(List)!=type(Seq): return False
    if type(List)==types.StringType:
        if Seq=='?': return [List]
        return Seq==List
    if len(List)!=len(Seq): return False
    Res=[]
    for ind,Item in enumerate(List):
        V = listMatches(Item,Seq[ind])
        if not V: return False
        if type(V)==types.ListType:
            Res.extend(V)
    return Res
