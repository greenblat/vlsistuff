

import logs

TABLE = {}

def help_main(Env):
    Mod = Env.Current
    Mod.buildNetTable()
    Starts = starts(Mod)
    print(len(Starts))
    Net,Src = Starts[1]
#    for Net,Src in Starts:
    TABLE[Net] = 0,Src
    travelDeep(Net,0,Mod,[Net])

def travelDeep(Net,Deep,Mod,Path):
    logs.log_info(">>try %s %s %s" % (Net,Deep,Path))
    if isOutput(Net,Mod):
        logs.log_info('output %s %s' % (Net,Deep))

    List = Mod.netTable[Net]
    Deeper = []
    for (Inst,Type,Pin) in List:
        if Type == 'input':
            pass
        elif Type in FLOPS: 
            logs.log_info('flop %s %s %s %s' % (Net,Deep,Inst,Path))
        elif isInputPin(Type,Pin):
            Obj = Mod.insts[Inst]
            for Pin in Obj.conns:
                Sig = Obj.conns[Pin]
                if (Sig in Path)and (Path.index(Sig) < (len(Path)-1)):
                    logs.log_info('LOOP? %s %d  ->(%s,%s)  %s' % (Net,Deep,Pin,Type,Path))
                elif Sig not in TABLE:
                    TABLE[Sig] = Deep+1,Type
                    Deeper.append(Sig)
                else:
                    Was,_ = TABLE[Sig]
                    if Was<Deep:
                        TABLE[Sig] = Deep+1,Type
                        Deeper.append(Sig)
    logs.log_info("DEEPER %s %s" % (Deep,len(Deeper)))
    for Sig1 in Deeper:
        travelDeep(Sig1,Deep+1,Mod,Path+[Sig1])


        




def starts(Mod):
    Res = []
    for Net in Mod.nets:
        Dir,_ = Mod.nets[Net]
        if 'input' in Dir:
            Res.append((Net,'input'))
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == 'flipflop':
            Conns = Obj.conns
            for Pin in Conns:
                if Pin.startswith('q'):
                    Sig = Conns[Pin]
                    Res.append((Sig,('flipflop',Inst)))
    return Res
            

def isOutput(Net,Mod):
    Dir,_ = Mod.nets[Net]
    return 'output' in Dir
GLVS = ''' mux2 and2 or2 inv select_bus shiftleft'''.split()
FLOPS = ''' flipflop mflipflop mpflipflop'''.split()

def isInputPin(Type,Pin):
    if Type in GLVS:
        if Pin[0] in 'abcdef': return True
        if Pin == 'sel': return True
        if Pin.startswith('no'): return True 
        if Pin.startswith('yes'): return True 
        return False

    logs.log_warning("UNKN %s" % Type)
    return False
    
