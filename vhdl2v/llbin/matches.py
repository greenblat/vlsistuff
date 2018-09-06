
import string,types
KNOWNFUNCTIONS = string.split('ext sxt resize conv_std_logic_vector conv_integer unsigned')
def matches(List,Seq):
    if type(Seq)==types.ListType:
        return listMatches(List,Seq)
    if type(Seq)==types.TupleType:
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



def listMatches(List,Seq):
    if type(List)==types.IntType:
        List = str(List)
    if type(List)!=type(Seq): 
        return False
    if type(List)==types.StringType:
        if Seq=='?': return [List]
        return Seq==List
    if len(List)!=len(Seq): return False
    Res=[]
    for ind,Item in enumerate(List):
        V = listMatches(Item,Seq[ind])
        if not V: return False
        if type(V) in [types.ListType,types.TupleType]:
            Res.extend(V)
    return Res 

