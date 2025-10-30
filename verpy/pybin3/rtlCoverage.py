



def help_main(Env):
    Mod = Env.Current
    List = []
    Fout = open('%s.txt' % Mod.Module,'w')
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if Dir in ['wire','reg']:
            if (Wid in [0,1,'0','1']):
                print('%s : %s ' % (Mod.Module,Net))
                List.append(Net)
    
    List.sort()
    for Net in List:
        Fout.write('net %s %s\n' % (Mod.Module,Net))    
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        Fout.write('instance %s %s %s\n' % (Mod.Module,Type,Inst))
    Fout.close()

    Lparams = {}
    for Lparam in Mod.localparams:
        Val = Mod.localparams[Lparam]
        if (type(Val) is tuple) or (type(Val) is list):
            if Val[0] == 'bin': Val = int(Val[2],2)
            elif Val[0] == 'hex': Val = int(Val[2],16)
            elif Val[0] == 'dig': Val = int(Val[2],10)
        Lparams[Lparam] = Val


    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if Dir in ['reg','output reg']:
            if (type(Wid) is tuple) or (type(Wid) is list): 
                Values = gatherAssigns(Mod,Net)
                Res = []
                for Value in Values:
                    if type(Value) is int:
                        Res.append((Value,Value))
                    elif Value[0] in '+-*':
                        pass
                    elif (type(Value) is str) and (Value in Lparams):
                        Res.append((Value,Lparams[Value]))
                    else:
                        Res.append((Value,Value))
                print(Net,Res)
                        
                        

def gatherAssigns(Mod,Net):
    Res = []
    for Alw in Mod.alwayses:
        _,Body,_ = Alw
        Vals = gatherDeep(Body,Net)
        for Val in Vals:
            if Val not in Res: Res.append(Val)
    return Res

def gatherDeep(Body,Net):
    if Body[0] in ['<=','=']:
        if Body[1] == Net:
            Val = Body[2]
            if (type(Val) is tuple) or (type(Val) is list):
                if Val[0] == 'bin': Val = int(Val[2],2)
                elif Val[0] == 'hex': Val = int(Val[2],16)
                elif Val[0] == 'dig': Val = int(Val[2],10)
            return [Val]
        return []
    if Body[0] == 'list':
        Res = []
        for Item in Body[1:]:
            More = gatherDeep(Item,Net)
            Res.extend(More)
        return Res
    if Body[0] == 'ifelse':
        Yes = gatherDeep(Body[2],Net)
        No = gatherDeep(Body[3],Net)
        return Yes+No
    if Body[0] == 'if':
        Yes = gatherDeep(Body[2],Net)
        return Yes
            
    print('FAILED %s' % str(Body))
    return []


    
