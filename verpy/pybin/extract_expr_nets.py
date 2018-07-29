
import types
import logs
import traceback

Ops = ['%','>>','<<','^','!','~','!=','==','<=','<','>','&','&&','|','||','>=','question','+','-','*','/']

def extract_sigs(Src,All=False):
    if (Src==0)and(All):
        return [0]
    if not Src:
#        print traceback.print_stack()
        return []
    if type(Src)==types.StringType:
        if Src[0] in '0123456789':
            if All:
                return [Src]
            return []
        if Src=='*':
            if All:
                return [Src]
            return []

        if (Src in ['default']):
            return []
        return [Src]
    if type(Src)==types.IntType:
        if All:
            return [Src]
        return []
    if type(Src) in [types.TupleType,types.ListType]:
        if len(Src)==0:
            return []
        if (len(Src)>1)and(Src[1]=='token'):
            return [Src[0]]
        if Src[0]=='edge':
            return extract_sigs(Src[2],All)
        if Src[0]=='subbus':
            return [Src[1]]
        if Src[0]=='subbit':
            return [Src[1]]
        if Src[0]=='sub_slicebit':
            return [Src[1]]
        if Src[0] in ['const','bin','hex','dig','*']:
            if All:
                return [Src]
            return []
        if Src[0] in ['repeat']:
            return extract_sigs(Src[2])
        if Src[0] in ['list']:
            return assemble_from_list(Src[1:])
        if Src[0] in ['functioncall']:
            return assemble_from_list(Src[2])
    if type(Src)==types.ListType:
        if Src[0] in Ops+['curly']:
            L1 = map(extract_sigs,Src[1:])
            Flat1 = flat_list(L1)
            Result = list(set(Flat1))
            return Result
        if Src[0] in ['const','bin','hex','dig']:
            if All:
                return [Src]
            return []
        if (len(Src)==1):
            return extract_sigs(Src[0],All)
        if (Src[0]=='='):
            X = extract_sigs(Src[1],All)
            Y = extract_sigs(Src[2],All)
            return list(set(X+Y))
        return map(extract_sigs,Src)
            
    logs.log_err('extract_sigs %s'%str(Src))
    print traceback.print_stack()
    return []

def assemble_from_list(List):
    L1 = map(extract_sigs,List)
    Flat1 = flat_list(L1)
    Result = list(set(Flat1))
    return Result

def flat_list(In):
    res=[]
    for X in In:
        if type(X)==types.ListType:
            Y = flat_list(X)
            res.extend(Y)
        else:
            res.append(X)
    return res



