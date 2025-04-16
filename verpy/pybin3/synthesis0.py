import string
import sys
import logs


import optimize0


PaternEdge0 = ['list', ['edge', 'posedge', 'Clk' ], ['edge', 'negedge', 'Rst' ]]
PaternEdge1 = ['edge', 'posedge', 'Clk' ]
PaternEdge2 = ['*' ]

Patterns = [PaternEdge0,PaternEdge1,PaternEdge2]

def match(What,Pattern,Vars):
    if What == Pattern: return True,Vars
    if (len(Pattern) == 1)and (What == Pattern[0]):
        return True,Vars
    if (type(What) is str) and (type(Pattern) is str) and (Pattern[0] in string.ascii_uppercase):
        Vars[Pattern] = What
        return True,Vars
    if (type(What) is str):
        return False
    if type(What) is list:
        if What[0] != Pattern[0]: 
            return False
        for ind,Item in enumerate(What[1:]):
            Comp = Pattern[1:][ind]
            if not match(Item,Comp,Vars): 
                return False
    return True,Vars        


def useParams(Mod):
    Argv = sys.argv
    for ind,Arg in enumerate(Argv):
        if Arg == '-define':
            defines = Argv[ind+1]
            ww = defines.split()
            Rename = []
            for wrd in ww:
                if '=' in wrd:
                    ww2 = wrd.split('=')
                    Param = ww2[0]
                    Val = eval(ww2[1])
                    if Param in Mod.parameters:
                        Mod.parameters[Param] = Val
                        Rename.append((Param,Val))
                    else:
                        logs.log_error('param %s val %s not in module %s' % (Param,Val,Mod.Module))
            Rename.sort()
            if Rename != []:
                NewName = Mod.Module
                for Prm,Val in Rename:
                    NewName += '_'+str(Val)
                    Mod.Module = NewName
def help_main(Env):
    Mod = Env.Current
    Mod.MUX2S = {}
    useParams(Mod)
    replaceFunctions(Mod)
    instances(Mod)
    for Dst,Src,_,_ in Mod.hard_assigns:
        Wid = Mod.sig_width(Dst)
        Src0 = synth0(Src,Mod,Wid)
        print("HARD",Dst,Src,Src0)
        merge(Dst,Src0,Mod)
    Mod.hard_assigns = []
    dumpver(Mod,'%s.bef0' % Mod.Module)
    always(Mod)
    dumpver(Mod,'%s.bef1' % Mod.Module)
    clearBufs(Mod)
    removeParams(Mod)
    dumpver(Mod,'%s.bef2' % Mod.Module)
    optimize0.optimize0(Mod)
    dumpver(Mod,'%s.bef3' % Mod.Module)
    optimize0.makeByBits(Mod)
    optimize0.optimize0(Mod)
    optimize0.zeroDriveRound(Mod,[],'A')
    Ones = optimize0.bufx_round(Mod,'A')
    dumpver(Mod,'%s.bef4' % Mod.Module)
    optimize0.bufx_round(Mod,'B')
    optimize0.zeroDriveRound(Mod,Ones,'B')
    dumpver(Mod,'%s.bef5' % Mod.Module)
    optimize0.zeroDriveRound(Mod,[],'C')
    dumpver(Mod,'%s.bef6' % Mod.Module)
    Done = 1
    Rnd = 0
    while Done > 0 :
        Done = optimize0.similarGatesRound(Mod,'D'+ str(Rnd))
        Rnd += 1
    optimize0.zeroDriveRound(Mod,Ones,'E')
    dumpver(Mod,'glv/%s.v' % Mod.Module)

def dumpver(Mod,Fname):
    File = open(Fname,'w')
    Mod.dump_verilog(File)
    File.close()




def removeParams(Mod):
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if type(Wid) is tuple:
            if len(Wid) == 2:
                Hi = Mod.compute_int(Wid[0])
                Lo = Mod.compute_int(Wid[1])
                Mod.nets[Net] = Dir,(Hi,Lo)
            elif Wid[0] == 'packed':
                Hi = Mod.compute_int(Wid[1][0])
                Lo = Mod.compute_int(Wid[1][1])
                H = max(Hi,Lo)
                L = min(Hi,Lo)
                Hi1 = Mod.compute_int(Wid[2][0])
                Lo1 = Mod.compute_int(Wid[2][1])
                Mod.nets[Net] = Dir,('packed',(H,L),(Hi1,Lo1))

    Mod.parameters = {}
    Mod.localparams = {}

def chunkWidth(Bus,Mod):
    Dir,Wid = Mod.nets[Bus]
    if type(Wid) is tuple:
        if len(Wid) == 2:
            Hi = Mod.compute_int(Wid[0])
            Lo = Mod.compute_int(Wid[1])
            return Hi-Lo+1
        elif Wid[0] == 'packed':
            Hi = Mod.compute_int(Wid[1][0])
            Lo = Mod.compute_int(Wid[1][1])
            Hi1 = Mod.compute_int(Wid[2][0])
            Lo1 = Mod.compute_int(Wid[2][1])
            H = max(Hi,Lo)
            L = min(Hi,Lo)
            return H-L+1
    return 1


def lineWidth(Bus,Mod):
    Dir,Wid = Mod.nets[Bus]
    if type(Wid) is tuple:
        if len(Wid) == 2:
            return 1
        elif Wid[0] == 'packed':
            Hi1 = Mod.compute_int(Wid[2][0])
            Lo1 = Mod.compute_int(Wid[2][1])
            return Hi1-Lo1+1
    return 1


EJECTS = {}
def always(Mod):
    global EJECTS
    for Alw in Mod.alwayses:
        EJECTS = {}
        Edge = Alw[0]
        Body = Alw[1]
        if (len(Body) == 2) and (Body[0] == 'list'): Body = Body[1]
        for ind,Pat in enumerate(Patterns):
            Vars = match(Edge,Pat,{})
            if Vars:
                Vars = Vars[1]
                if ind==0:
                    if Body[0] == 'ifelse':
                        scanDeep(Body[3],[],(0,Vars['Clk'],Vars['Rst']),Mod)   
                    else:
                        logs.log_error("always bad %s" % str(Body[2]))
                elif ind==1:
                    scanDeep(Body,[],(1,Vars['Clk']),Mod)   
                elif ind==2:
                    scanDeep(Body,[],(2),Mod)   
                dealEjects(Mod)
                    
    Mod.alwayses = []

def predealEjects(Mod):
    Keys = list(EJECTS.keys())
    Partials = []
    Fulls = []
    for Key in Keys:
        if '[' in Key:
           Bus = Key[:Key.index('[')] 
           if Bus not in Partials: Partials.append(Bus)
        else:
            if Key not in Fulls: Fulls.append(Key)
    for Bus in Partials:
        if Bus in Fulls:  Fulls.remove(Bus)
    return Partials,Fulls


def dealEjects(Mod):
    Partials,Fulls = predealEjects(Mod)        
    ejectFulls(Mod,Fulls)
    ejectPartials(Mod,Partials)

def ejectFulls(Mod,Fulls):
    for Dst in Fulls:
        List = EJECTS[Dst]
        Wid0 = Mod.sig_width(Dst)
        if len(List) > 1:
            Dats = []
            Cnd = ['||']
            for  Src,Cond,TT in List:
                Cnd.append(Cond)
                Dats.append( (Cond,Src))
            Dats.reverse()
            XX = ['bus']
            for ii in range(Wid0):
                XX.append('gnd')
            Dat = ['question',Dats[0][0],Dats[0][1],XX]
            for Cond,Src in Dats[1:]:
                Dat = ['question',Cond,Src,Dat]
            TT = List[0][2]
        else:
            Cnd = List[0][1]
            Dat = List[0][0]
            TT = List[0][2]


        Src0 = synth0(Dat,Mod,Wid0)
        if Cnd == []: 
            Cond0 = 'vcc'
            Mod.add_sig('vcc','input',0)
        else:
            Cond0 = synth0(Cnd,Mod,Wid0)
        if TT == 2:
            Rst = 'vcc'
        elif TT[0] == 0:
            Rst = TT[2]
        else:
            Rst = 'vcc'
            Mod.add_sig('vcc','input',0)
#        Src1 = Mod.pr_expr(Src0)
        if (TT == 2) or (TT[0] in [0,1,2]):
            if Dst in DSTLISTS:
                Dst = DSTLISTS[Dst]
                if Dst[0] == 'subbit':
                    Bus = Dst[1]
                    Ind = Dst[2]
                    _,Wid = Mod.nets[Bus]
                    if (type(Wid) is tuple) and (Wid[0] == 'packed'):
                        W1_0 = Mod.compute_int(Wid[1][0])-Mod.compute_int(Wid[1][1])+1
                        W1_1 = Mod.compute_int(Wid[1][1])-Mod.compute_int(Wid[1][0])+1
                        W1 = max(W1_0,W1_1)
                        W2_0 = Mod.compute_int(Wid[2][0])-Mod.compute_int(Wid[2][1])+1
                        W2_1 = Mod.compute_int(Wid[2][1])-Mod.compute_int(Wid[2][0])+1
                        W2 = max(W2_0,W2_1)
                        for II in range(W1):
                            Wr = ['&&',Cond0,['==',Ind,II]]
                            Wrx = synth0(Wr,Mod,Wid0)
                            Dst = ['subbit',Bus,II]
                            Dstx = synth0(Dst,Mod,Wid0)
                            Src1 = splitBits(Src0,Mod,Wid0)
                            print("DSTX",Dst,Dstx)
                            if Dstx[0] != 'bus': Dstx = ['bus']+Dstx
                            print("SRC1",Src1)
                            Obj = Mod.add_inst_conns('flipflop','%s_%s_%s_reg' % (Bus,Ind,II),[('clk',TT[1]),('rst_n',Rst),('d',Src1),('en',Wrx),('q',Dstx)])
                            Obj.params['WID'] = W2
                    elif (type(Wid) is tuple):
                        W1 = Mod.compute_int(Wid[0])-Mod.compute_int(Wid[1])+1
                        for II in range(W1):
                            Wr = ['&&',Cond0,['==',Ind,II]]
                            Wrx = synth0(Wr,Mod,Wid0)
                            Dst = ['subbit',Bus,II]
                            Dstx = synth0(Dst,Mod,Wid0)
                            Obj = Mod.add_inst_conns('flipflop','%s_%s_reg' % (Bus,II),[('clk',TT[1]),('rst_n',Rst),('d',Src0),('en',Wrx),('q',Dstx)])
                            Obj.params['WID'] = 1
                    else:
                        logs.log_error("untreated yet Dst=%s for flop" % Mod.pr_expr(Dst))

            elif (TT==2):
                merge(Dst,Src0,Mod)
            else:
                Obj = Mod.add_inst_conns('flipflop','%s_reg_1' % Dst,[('clk',TT[1]),('rst_n',Rst),('d',Src0),('en',Cond0),('q',Dst)])
                Wid0 = Mod.sig_width(Dst)
                Obj.params['WID'] = Wid0
        elif TT[0] in [2]:
            print("222222",Src0,Cond0,Dst)


def ejectPartials(Mod,Partials):
    for Bus in Partials:
        Wid = chunkWidth(Bus,Mod)
        Wid0 = lineWidth(Bus,Mod)
        for II in range(Wid):
            Dats = []
            Cnd = ['||']
            for Dst in EJECTS:
                List = EJECTS[Dst]
                Code = compatible(II,Bus,Dst)
                logs.log_info("COMPATIBLE ii=%s dst=%s list=%s code=%s" % (II,Dst,List,Code))
                if Code:
                    And = 0
                    if Code != 1:
                        And = ['==',Code,II]
                    for  Src,Cond,TT in List:
                        if Wid0 == 1:
                            Bits0 = synth0(Src,Mod,1)
                            Sbits = splitBits(Bits0,Mod,Wid)  
                            if Bits0 == 0:
                                Line = 'gnd'
                            elif Bits0 == 1:
                                Line = 'vcc'
                            elif (type(Bits0) is list) and (Bits0[0] == 'bus'):
                                if len(Bits0) == 2:
                                    Line = Bits0[1]
                                else:
                                    Line = Bits0[II+1]
                            else:
                                if len(Sbits) == 2:
                                    Line = Sbits[1]
                                else:
                                    Line = Sbits[-1]
                            logs.log_info("NOEXTRACTBIT bus=%s wid=%s wid0=%s src=%s ii=%s line=%s" % (Bus,Wid,Wid0,Src,II,Line))
                        else:
                            Line = extractBit(Src,II,Wid0,Mod)
                            logs.log_info("EXTRACTBIT bus=%s wid=%s wid0=%s src=%s ii=%s line=%s" % (Bus,Wid,Wid0,Src,II,Line))

                        if And:
                            Cnd.append( ['&&',And,Cond] )
                            Dats.append( (['&&',And,Cond],Line))
                        else:
                            Cnd.append(Cond)
                            Dats.append( (Cond,Line))
                    Dats.reverse()
                    logs.log_info("DATS %s wid0=%s ii=%s dats=%s cnd=%s" % (Bus,Wid0,II,Dats,Cnd))
                    if (len(Dats)>1):
                        XX = ['bus']
                        for ii in range(Wid0): XX.append('gnd')
                        Dat = ['question',Dats[0][0],Dats[0][1],XX]
                        for Cond,Src in Dats[1:]:
                            Dat = ['question',Cond,Src,Dat]
                        TT = List[0][2]
                    else:
                       Dat = Dats[0][1]
            logs.log_info("BEFORE CODE ii=%s bus=%s dat=%s cnd=%s wid0=%s" %(II,Bus,Dat,Cnd,Wid0))
            Src0 = synth0(Dat,Mod,Wid0)
            if (type(Src0) is list)and (len(Src0) == 1): Src0 = Src0[0]
            logs.log_info("AFTER CODE0 ii=%s bus=%s src0=%s" % (II,Bus,Src0))
            if Cnd == []:
                Cond0 = 'vcc'
                Mod.add_sig('vcc','input',0)
            else:
                Cond0 = synth0(Cnd,Mod,Wid0)
            if TT == 2:
                Rst = 'vcc'
            elif TT[0] == 0:
                Rst = TT[2]
            else:
                Rst = 'vcc'
                Mod.add_sig('vcc','input',0)
            Obj = Mod.add_inst_conns('flipflop','%s_reg_%s' % (Bus,II),[('clk',TT[1]),('rst_n',Rst),('d',Src0),('en',Cond0),('q',['subbit',Bus,II])])
            Obj.params['WID'] = Wid0
            print("CODE FLOP",Bus,II,Src0,Cond0);

def extractBit(Src,II,Wid,Mod):
    if type(Src) is str:
        if Src in Mod.nets:
            _,Wid1 = Mod.nets[Src]
            if type(Wid) is tuple:
                if Wid[0] == 'packed':
                    return extractBit(['subbus',Src,(Wid[1][0],Wid[1][1]) ], II,Wid,Mod)
                else:
                    return extractBit(['subbus',Src,(Wid[0],Wid[1])],II,Wid,Mod)
            return Src
    if type(Src) is int:
        X = (Src>>II) & 1
        return X
    if type(Src) is list:
        if Src[0] == 'bin':
            if len(Src[2])<=II: return 0
            return Src[2][II]
        if Src[0] == 'subbus':
            Hi = Src[2][0]
            Lo = Src[2][1]
            if (Wid == 1):
                Ind = Lo + II
                return ['subbit',Src[1],Ind]
            else:
                Hi2 = Lo + Wid -1
                return ['subbus',Src[1],(Hi2,Lo)]
        if Src[0] == 'bus':
            XX = Src[:]
            XX.reverse()
            return XX[II]
    
    Cond0 = synth0(Src,Mod,Wid)
    return extractBit(Cond0,II,Wid,Mod)
    



def compatible(Ind,Bus,Dst):
    if Bus == Dst: return 1
    if '[' in Dst:
        B0 = Dst[:Dst.index('[')]
        if B0 != Bus: return False
        I0 = Dst[Dst.index('[')+1:-1]
        if I0[0] in '0123456789': 
            I1 = eval(I0)
            if I1 != Ind: return False
            return 1
        return I0

    if Bus != Dst: return False
    logs.log_error("COMPATIBLE %s %s %s" % (Ind,Bus,Dst))
    return False

def scanDeep(Body,Sofar,Kind,Mod):
    if type(Body) is list:
        if Body[0] == '<=':
            eject(Body[1],Body[2],Sofar,Kind,Mod)
        elif Body[0] == '=':
            eject(Body[1],Body[2],Sofar,Kind,Mod)
        elif Body[0] == 'list':
            for Item in Body[1:]:
                scanDeep(Item,Sofar,Kind,Mod)
        elif Body[0] == 'ifelse':
            Cond = Body[1]
            if Sofar == []:
                DeepY = [Cond]
                DeepN = [['!',Cond]]
            else:
                DeepY = ['&&',Cond,Sofar]
                DeepN = ['&&',['!',Cond],Sofar]
            scanDeep(Body[2],DeepY,Kind,Mod)
            scanDeep(Body[3],DeepN,Kind,Mod)
        elif Body[0] == 'if':
            Cond = Body[1]
            if Sofar == []:
                DeepY = [Cond]
            else:
                DeepY = ['&&',Cond,Sofar]
            scanDeep(Body[2],DeepY,Kind,Mod)
        else:
            logs.log_error('scanDeep failed on %s' % str(Body))

    else:
        logs.log_error('scanDeep failed on %s' % str(Body))
DSTLISTS = {}        
def eject(Dst,Src,Cond,Kind,Mod):
    if type(Dst) is list:
        X = Mod.pr_expr(Dst)
        if X not in DSTLISTS:
            DSTLISTS[X] = Dst
        Dst = X
    if Dst in EJECTS:
        EJECTS[Dst].append((Src,Cond,Kind))
    else:
        EJECTS[Dst] = [(Src,Cond,Kind)]

def clearBufs(Mod):
    Renames,Bufs = getRenames(Mod)
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if 'reg' in Dir:
            Dir = Dir.replace('reg','wire')
            if 'output' in Dir: Dir = 'output'
            Mod.nets[Net] = Dir,Wid
        if Net in ['vcc']:
            Mod.nets[Net] = 'wire',1
            Mod.hard_assigns.append( (Net,1,'',''))
        if Net in ['gnd']:
            Mod.nets[Net] = 'wire',1
            Mod.hard_assigns.append( (Net,0,'',''))
    Insts = list(Mod.insts.keys())
    for Inst in Insts:
        if Inst in Mod.insts:
            Obj = Mod.insts[Inst]
            if Obj.Type != 'bufx':
                for Pin in Obj.conns:
                    Sig = Obj.conns[Pin]
                    if (type(Sig) is str) and (Sig in Renames):
                        Obj.conns[Pin] = Renames[Sig]
                        if Sig in Bufs:
                            Rem = Bufs[Sig]
                            if Rem in Mod.insts:
                                Mod.insts.pop(Rem)


def getRenames(Mod):
    Renames = {}
    Bufs = {}
    for Buf in Mod.insts:
        Obj = Mod.insts[Buf]
        if Obj.Type == 'bufx':
            Out = Obj.conns['x']
            In = Obj.conns['a']
            if (In not in ['vcc','gnd']) and (type(Out) is str) and (not (Out.startswith('net_'))) and (type(In) is str) and In.startswith('net_'):
                Renames[In] = Out
                Bufs[In] = Buf
    print("RENAMES",Renames)
    print("BUFS",Bufs)
    return Renames,Bufs



def merge(Dst,Src,Mod):
    Wid = Mod.sig_width(Dst)
    Sbits = splitBits(Src,Mod,Wid)
    Dbits = splitBits(Dst,Mod,Wid)
    if Sbits[0] == 'bus': Sbits.pop(0)
    if Dbits[0] == 'bus': Dbits.pop(0)
    print("MERGE",Dst,len(Sbits),len(Dbits))
    while (Sbits!=[]) and (Dbits!=[]):
        SB = Sbits.pop(-1) 
        DB = Dbits.pop(-1) 
        addInst1('bufx',DB,SB,Mod)
    while Dbits!=[]:
        DB = Dbits.pop(-1) 
        addInst1('bufx',DB,'gnd',Mod)
    print("MERGE2",Dst,len(Sbits),len(Dbits))
        

KNOWNS = {}
def splitBits(Expr,Mod,Mwid=64 ):
    if type(Expr) is int:
        Res = []
        for ii in range(Mwid):
            X = (Expr>>ii) & 1
            if (X==1):
                Res.append('vcc')
                Mod.add_sig('vcc','input',0)
            else:
                Res.append('gnd')
                Mod.add_sig('gnd','input',0)
        Res.reverse()    
        Res = ['bus']+Res
        return Res

    if type(Expr) is str:
        if Expr in Mod.parameters:
            Val = splitBits(Mod.parameters[Expr],Mod)
            return Val
        if Expr in Mod.localparams:
            Val = splitBits(Mod.localparams[Expr],Mod)
            return Val
            
        if Expr in Mod.nets:
            _,Wid = Mod.nets[Expr]
            if Wid in [0,1,'0','1']:
                return [Expr]
            if type(Wid) is int:
                logs.log_error("SPLIT %s" % str(Expr))
                return [Expr]
            Hi,Lo = Wid
            Hi = Mod.compute_int(Hi)
            Lo = Mod.compute_int(Lo)
            Run = Lo
            Res = ['bus']
            while Lo <= Hi:
                Sig = '%s[%s]' % (Expr,Hi)
                Res.append(Sig)
                Hi -= 1
            return Res
    if type(Expr) is list:
        if len(Expr) == 1:
            return splitBits(Expr[0],Mod,Mwid)
        if Expr[0] == 'bus':
            return Expr
            Res = ['bus']
            for X in Expr[1:]:
                RR = splitBits(X,Mod)
                Res.extend(RR)
            return  Res
        if Expr[0] == 'subbus':
            return synth0(Expr,Mod,Mwid)

        if Expr[0] == 'subbit':
            Bus = Expr[1]
            Ind = Expr[2]
            if (type(Ind) is int) and singleIndexBus(Bus,Mod):
                return ['%s[%d]' % (Bus,Ind)]
            elif singleIndexBus(Bus,Mod):
                BB = synth0(Expr[2],Mod,Mwid)
                Key = '%s,%s' % (Expr[1],BB)
                if Key in KNOWNS: return KNOWNS[Key]
                Out = Mod.add_sig('','wire',1)
                Obj = Mod.add_inst_conns('select','',[('a',Expr[1]),('b',BB),('x',Out)])
                L1 = Mod.sig_width(Bus)
                Obj.params['WID'] = L1
                KNOWNS[Key] = Out
                return [Out]
            else:
                _,Wid = Mod.nets[Bus]
                if (type(Wid) is tuple):
                    if Wid[0] == 'packed':
                        W1_0 = Mod.compute_int(Wid[1][0])-Mod.compute_int(Wid[1][1])+1
                        W1_1 = Mod.compute_int(Wid[1][1])-Mod.compute_int(Wid[1][0])+1
                        W1 = max(W1_0,W1_1)
                        W2_0 = Mod.compute_int(Wid[2][0])-Mod.compute_int(Wid[2][1])+1
                        W2_1 = Mod.compute_int(Wid[2][1])-Mod.compute_int(Wid[2][0])+1
                        W2 = max(W2_0,W2_1)
                        BB = synth0(Expr[2],Mod)
                        Key = '%s,%s' % (Expr[1],BB)
                        if Key in KNOWNS: 
                            return KNOWNS[Key][:]
                        Out = Mod.add_sig('','wire',W2)
                        if type(BB) is int:
                            Obj = Mod.add_inst_conns('select_bus_lit','',[('a',Expr[1]),('x',Out)])
                            Obj.params['LIT'] = BB
                        else:
                            Obj = Mod.add_inst_conns('select_bus','',[('a',Expr[1]),('b',BB),('x',Out)])
                        Obj.params['WID'] = W2
                        Obj.params['DEPTH'] = W1
                        Res = splitBits(Out,Mod)
                        KNOWNS[Key] = Res
                        return Res
    if type(Expr) is str: return [Expr]

    logs.log_error("EXPR SPLIT %s" % str(Expr))
    breakIt()
    return [Expr]
def breakIt():
    print("BREAK %d %d %d" % 'no')

def singleIndexBus(Bus,Mod):
    if Bus not in Mod.nets: return False
    _,Wid = Mod.nets[Bus]
    if type(Wid) is int: return True
    if type(Wid) is tuple:
        if len(Wid) == 2: return True

    return False



COMPARES = ['==','!=','<','<=','>','=>','>=']
def synth0(Src,Mod,Mwid=64,Depth=0):
    logs.log_info('SYNTH0 %s src=%s' % (Depth,Src))
    Res = synth0__(Src,Mod,Mwid,Depth)
    if (type(Res) is str) and (Res in Mod.nets):
        logs.log_info('SYNTH1 %s res=%s net=%s src=%s' % (Depth,Res,Mod.nets[Res],Src))
    else:
        logs.log_info('SYNTH1 %s %s %s' % (Depth,Src,Res))
    return Res

def synth0__(Src,Mod,Mwid=64,Depth=0):
    if type(Src) is str: 
        if '.' in Src: return 0
        return Src
    if type(Src) is int: return Src & ((1<<Mwid)-1)
    if type(Src) is list:
        if len(Src) == 0:
            return 'gnd'
        if len(Src) == 1:
            return synth0(Src[0],Mod,Mwid,Depth+1)
        if Src[0] == 'bus': return Src                
        if Src[0] == '&&':
            LL = []
            for X in Src[1:]:
                A = synth0(X,Mod,Mwid,Depth+1)
                if A!='vcc':
                    LL.append(A)
            Len = len(LL)
            Out = makeWide(LL,'and',Mod)
            return Out
        if Src[0] == '||':
            LL = []
            for X in Src[1:]:
                A = synth0(X,Mod,Mwid,Depth+1)
                if A!='gnd':
                    LL.append(A)
            Len = len(LL)
            Out = makeWide(LL,'or',Mod)
            return Out

        if Src[0] == '^':
            A = synth0(Src[1],Mod,Mwid,Depth+1)
            B = synth0(Src[2],Mod,Mwid,Depth+1)
            Out = addInst2('xor2','',A,B,Mod)
            return Out
            

        if (Src[0] == '|') and (len(Src) ==2):
            A = synth0(Src[1],Mod,Mwid,Depth+1)
            AA = splitBits(A,Mod)
            Len = len(AA)
            Out = makeWide(AA,'or',Mod)
            Mod.add_sig(Out,'wire',1)
            return Out


        if (Src[0] == '&') and (len(Src) ==2):
            A = synth0(Src[1],Mod,Mwid,Depth+1)
            AA = splitBits(A,Mod)
            Len = len(AA)
            Out = makeWide(AA,'and',Mod)
            Mod.add_sig(Out,'wire',1)
            return Out


        if Src[0] == '&':
            A = synth0(Src[1],Mod,Mwid,Depth+1)
            B = synth0(Src[2],Mod,Mwid,Depth+1)
            AA = splitBits(A,Mod)
            BB = splitBits(B,Mod)
            if AA[0] == 'bus': AA = AA[1:]
            if BB[0] == 'bus': BB = BB[1:]
            AA.reverse()
            BB.reverse()
            Len = min(len(AA),len(BB))
            Out = Mod.add_sig('','wire',Len)
            for ind in range(Len):
                A0 = AA[ind] 
                B0 = BB[ind] 
                addInst2('and2',('subbit',Out,ind),A0,B0,Mod)
            return Out

        if Src[0] == '|':
            A = synth0(Src[1],Mod,Mwid,Depth+1)
            B = synth0(Src[2],Mod,Mwid,Depth+1)
            AA = splitBits(A,Mod)
            BB = splitBits(B,Mod)
            if AA[0] == 'bus': AA = AA[1:]
            if BB[0] == 'bus': BB = BB[1:]
            AA.reverse()
            BB.reverse()
            Len = min(len(AA),len(BB))
            Out = Mod.add_sig('','wire',Len)
            for ind in range(Len):
                A0 = AA[ind] 
                B0 = BB[ind] 
                OO = ('subbit',Out,ind)
                if A0 == 'gnd': addInst1('bufx',OO,B0,Mod)
                elif (A0 == 'vcc') or (B0 == 'vcc'): addInst1('bufx',OO,'vcc',Mod)
                elif B0 == 'gnd': addInst1('bufx',OO,A0,Mod)
                else: addInst2('or2',OO,A0,B0,Mod)
            return Out
            
        if Src[0] == 'dig':
            Wid = eval(Src[1])
            Val = int(Src[2],10)
            Res = []
            for ii in range(Wid):
                if ((Val>>ii)&1) == 1:
                    Res.append('vcc')
                else:
                    Res.append('gnd')
            Res.reverse()
            return ['bus']+Res

        if Src[0] == 'hex':
            Wid = eval(Src[1])
            Val = int(Src[2],16)
            Res = []
            for ii in range(Wid):
                if ((Val>>ii)&1) == 1:
                    Res.append('vcc')
                else:
                    Res.append('gnd')
            Res.reverse()
            return ['bus']+Res




        if Src[0] == '!':
            A = synth0(Src[1],Mod,Mwid,Depth+1)
            Out = addInst1('inv','',A,Mod)
            return Out

        if Src[0] == 'question':
            Yes0 = synth0(Src[2],Mod,Mwid,Depth+1)
            Yes = splitBits(Yes0,Mod,Mwid)
            if Yes[0] == 'bus': Yes = Yes[1:]
            No = synth0(Src[3],Mod,Mwid,Depth+1)
            No = splitBits(No,Mod,Mwid)
            if No[0] == 'bus': No = No[1:]
            Res = ['bus']
            Len = max(len(Yes),len(No))
            Last = 0
            for ind in range(Len):
                NN = getBit(No,ind)
                YY = getBit(Yes,ind)
                if (NN != 'gnd') or (YY != 'gnd'):
                    Last = ind
            No = No[:Last+1]
            Yes = Yes[:Last+1]
            Out = Mod.add_sig('','wire',Last+1)
            if len(Yes)>1: Yes = ['curly']+Yes
            if len(No)>1: No = ['curly']+No
            logs.log_info('QUEST OUT=%s yes=%s src2=%s yes0=%s mwid=%d' % (Out,Yes,Src[2],Yes0,Mwid))
            if (Yes==No):
                return Yes
            elif (Yes==['vcc']) and (No == ['gnd']):
                Cond = synth0(Src[1],Mod,Mwid,Depth+1)
                return Cond
            else:
                Cond = synth0(Src[1],Mod,Mwid,Depth+1)
                Key = str([('sel',Cond),('yes',Yes),('no',No)])
                if Key in Mod.MUX2S:
                    return Mod.MUX2S[Key]
                Obj = Mod.add_inst_conns('mux2','',[('sel',Cond),('yes',Yes),('no',No),('x',Out)])
                Obj.params['WID'] = Last+1
                Mod.MUX2S[Key] = Out
                return Out

        if Src[0] in ['>>']:
            AA = synth0(Src[1],Mod,Mwid,Depth+1)
            L1 = Mod.sig_width(AA)
            BB = synth0(Src[2],Mod,Mwid,Depth+1)
            Out = Mod.add_sig('','wire',1)
            Obj = Mod.add_inst_conns('shiftright','',[('a',AA),('b',BB),('x',Out)])
            Obj.params['WID'] = L1
            return Out

        if Src[0] in ['<<']:
            AA = synth0(Src[1],Mod,Depth+1)
            L1 = Mod.sig_width(AA)
            BB = synth0(Src[2],Mod,Depth+1)
            Out = Mod.add_sig('','wire',L1)
            Obj = Mod.add_inst_conns('shiftleft','',[('a',AA),('b',BB),('x',Out)])
            Obj.params['WID'] = L1
            return Out

        if Src[0] in ['*']:
            AA = synth0(Src[1],Mod,Mwid,Depth+1)
            L1 = Mod.sig_width(AA)
            BB = synth0(Src[2],Mod,Mwid,Depth+1)
            L2 = Mod.sig_width(BB)
            Out = Mod.add_sig('','wire',(L1+L2))
            Obj = Mod.add_inst_conns('multiplier','',[('a',AA),('b',BB),('x',Out)])
            Obj.params['WID'] = L1+L2
            return Out

        if Src[0] in COMPARES:
            Out = Mod.add_sig('','wire',1)

            B0 = Mod.compute_int(Src[2],False)
            if type(B0) is int:
                AA = synth0(Src[1],Mod,Mwid,Depth+1)
                Obj = Mod.add_inst_conns('comparator_lit','',[('a',AA),('x',Out)])
                L1 = expr_width(Src[1],Mod)
                Obj.params['WID'] = L1
                Obj.params['LIT'] = B0
                Kind = COMPARES.index(Src[0])
                Obj.params['KIND'] = Kind
                return Out


            AA = synth0(Src[1],Mod,Mwid,Depth+1)
            BB = synth0(Src[2],Mod,Mwid,Depth+1)
            Obj = Mod.add_inst_conns('comparator','',[('a',AA),('b',BB),('x',Out)])
            L1 = Mod.sig_width(AA)
            L2 = Mod.sig_width(BB)
            Obj.params['WIDA'] = L1
            Obj.params['WIDB'] = L2
            Kind = COMPARES.index(Src[0])
            Obj.params['KIND'] = Kind
            return Out
            
        if Src[0] in ['~']:
            AA = synth0(Src[1],Mod,Mwid,Depth+1)
            Bits = splitBits(AA,Mod)
            L1 = Mod.sig_width(AA)
            Out = Mod.add_sig('','wire',L1)
            Res = ['bus']
            for Sig in Bits:
                if Sig != 'bus':
                    Mid = addInst1('inv','',Sig,Mod)
                    Res.append(Mid)
            return Res

        if (Src[0] == '-') and (len(Src) ==2):
            AA = synth0(0,Mod,Mwid,Depth+1)
            BB = synth0(Src[1],Mod,Mwid,Depth+1)
            L2 = Mod.sig_width(BB)
            Out = Mod.add_sig('','wire',L2)
            Obj = Mod.add_inst_conns('subtractor','',[('a',AA),('b',BB),('x',Out)])
            Obj.params['WID'] = L2
            return Out
        if Src[0] in ['+','-']:
            A0 = Mod.compute_int(Src[1],False)
            B0 = Mod.compute_int(Src[2],False)
            if (type(A0) is int) and (type(B0) is int): 
                if Src[0] == '-': return (A0-B0)
                if Src[0] == '+': return (A0+B0)

            if (type(B0) is int): 
                AA = synth0(Src[1],Mod,Mwid,Depth+1)
                L1 = Mod.sig_width(AA)
                Out = Mod.add_sig('','wire',1+L1)
                if Src[0] == '+': Type = 'adder_lit'
                if Src[0] == '-': Type = 'subtractor_lit'
                Obj = Mod.add_inst_conns(Type,'',[('a',AA),('x',Out)])
                Obj.params['WID'] = L1+1
                Obj.params['LIT'] = B0
                return Out


            AA = synth0(Src[1],Mod,Mwid,Depth+1)
            BB = synth0(Src[2],Mod,Mwid,Depth+1)
            L1 = Mod.sig_width(AA)
            L2 = Mod.sig_width(BB)
            Out = Mod.add_sig('','wire',1+max(L1,L2))

            if Src[0] == '+': Type = 'adder'
            if Src[0] == '-': Type = 'subtractor'
            Obj = Mod.add_inst_conns(Type,'',[('a',AA),('b',BB),('x',Out)])
            Obj.params['WID'] = max(L1,L2)
            return Out

        if Src[0] == 'repeat':
            Many = Mod.compute_int(Src[1])
            Rep = synth0(Src[2],Mod,Mwid,Depth+1)
            Sbits = splitBits(Rep,Mod)
            Res = ['bus']
            while Sbits!= []:
                Pop = Sbits.pop(0)
                if Pop[0] == 'bus': Pop = Pop[1:]
                Res.extend(Sbits)
            return Res
        
        if Src[0] == 'bin':
            Wid = Mod.compute_int(Src[1])
            Z = '0'*Wid + Src[2]
            Res = []
            Pos = -1
            for x in range(Wid):
                if Z[Pos] == '1': 
                    Res = ['vcc']+Res
                    Mod.add_sig('vcc','input',0)
                else: 
                    Res = ['gnd'] + Res
                    Mod.add_sig('gnd','input',0)
                Pos -= 1
            Res = ['bus'] + Res
            return Res                

        if Src[0] == 'subbit':
            return splitBits(Src,Mod)
        if Src[0] == 'subbus':
            Net = Src[1]
            Hi = Mod.compute_int(Src[2][0])
            Lo = Mod.compute_int(Src[2][1])
            Res = ['bus']
            while Hi>=Lo:
                Res.append('%s[%d]' % (Net,Hi))
                Hi -= 1
            return Res


        if Src[0] == 'curly':
            if Src[1] == 'repeat':
                return synth0(Src[1:],Mod,Mwid,Depth+1)
            Res = ['bus']
            for Item in Src[1:]:
                AA = synth0(Item,Mod,Mwid,Depth+1)
                AA = splitBits(AA,Mod)
                if AA[0] == 'bus': AA =  AA[1:]
                Res.extend(AA)
            return Res

    logs.log_error("SYNTH0 %s %s " % (type(Src),Src))
    return Src

def getBit(List,ind):
    if len(List)>ind: return List[ind]
    return 'gnd'
    


def makeWide(List,Type,Mod):
    Runlist = List[:]
    if Runlist[0] == 'bus': Runlist  = Runlist[1:]
    while len(Runlist)>1:
        if len(Runlist)>=8:
            X = addInstX(Type,Runlist[:8],Mod)
            if len(Runlist) == 8: return X
            Runlist = Runlist[8:]+[X]
        elif len(Runlist)>=7:
            X = addInstX(Type,Runlist[:7],Mod)
            if len(Runlist) == 7: return X
            Runlist = Runlist[7:]+[X]
        elif len(Runlist)>=6:
            X = addInstX(Type,Runlist[:6],Mod)
            if len(Runlist) == 6: return X
            Runlist = Runlist[6:]+[X]
        elif len(Runlist)>=5:
            X = addInstX(Type,Runlist[:5],Mod)
            if len(Runlist) == 5: return X
            Runlist = Runlist[5:]+[X]
        elif len(Runlist)>=4:
            X = addInstX(Type,Runlist[:4],Mod)
            if len(Runlist) == 4: return X
            Runlist = Runlist[4:]+[X]
        elif len(Runlist)>=3:
            X = addInstX(Type,Runlist[:3],Mod)
            if len(Runlist) == 3: return X
            Runlist = Runlist[3:]+[X]
        else:
            X = addInst2(Type+'2','',Runlist[0],Runlist[1],Mod)
            if len(Runlist) == 2: return X
            Runlist = Runlist[2:]+[X]
    return Runlist[0]

def addInstX(Type,List,Mod):
    Type = Type + str(len(List))
    Out = Mod.add_sig('','wire',1)
    Pins = 'a b c d e f g h'. split()
    Pins = Pins[:len(List)]
    LL = [('x',Out)]
    for ind,Pin in enumerate(Pins):
        LL.append( (Pin,List[ind]))
    Mod.add_inst_conns(Type,'',LL)
    return Out

def addInst2(Type,Out,A,B,Mod):
    if Out == '':
        Out = Mod.add_sig('','wire',1)
    Mod.add_inst_conns(Type,'',[('a',A),('b',B),('x',Out)])
    return Out

def addInst1(Type,D,S,Mod):
    Out = Mod.add_sig(D,'wire',1)
    if (type(Out) is list) and (Out[0] == 'subbus') and (Out[2] == Out[3]):
        Out = ['subbit',Out[1],Out[2]]
    Mod.add_inst_conns(Type,'',[('a',S),('x',Out)])
    return Out

def replaceFunctions(Mod):
    for ind,(Dst,Src,A,B) in enumerate(Mod.hard_assigns):
        Src1 = replaceFunction(Src,Mod)
        if Src1 != Src:
            Mod.hard_assigns[ind] = (Dst,Src1,A,B)
    Mod.functions = {}            
def replaceFunction(Src,Mod):
    if type(Src) is list:
        if Src[0] == 'functioncall':
            Func = Src[1]
            Def = Mod.functions[Func]
            Wid = Def[0]
            Out = Mod.add_sig('','wire',Wid)
            Obj = Mod.add_inst_conns(Func,'',[(Func+'_out',Out)])
            Inps = Src[2]
            for Net,Wid,Dir in Def[1]:
                if Dir == 'input':
                    Obj.add_conn(Net,Inps.pop(0))
            return Out
    return Src

def instances(Mod):
    Insts = list(Mod.insts.keys())
    for Inst in Insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            if needsSynth(Sig):
                Res = synth0(Sig,Mod)
                Obj.conns[Pin] = Res
        Keys = list(Obj.params.keys())
        Keys.sort()
        if Keys!=[]:
            Type = Obj.Type
            for Key in Keys:
                Val = Obj.params[Key]
                Val = Mod.compute_int(Val)
                Type += '_' + str(Val)
            Obj.Type = Type
        Obj.params = {}

Ops = '| || & && ^ ~ - + * >> << >= => <= =< < >'
def needsSynth(Sig):
    if type(Sig) is str: return False
    if type(Sig) is int: return False
    if type(Sig) is list:
        if Sig[0] in ['curly','hex','dig','bin','subbus','subbit']: return True
        if Sig[0] in Ops: return True
    return False

def expr_width(Expr,Mod):
    if type(Expr) is str:
        if Expr in Mod.nets:
            return Mod.sig_width(Expr)
        else:
            logs.log_error('expr_width %s' % str(Expr))
            return 1
    if type(Expr) is int: return 32

    if type(Expr) is list:
        if Expr[0] in ['hex','dig','bin']: return Expr[1]
        if Expr[0] == 'bus': return len(Expr)-1
        if Expr[0] == 'subbus': 
            Hi = Expr[2][0]
            Lo = Expr[2][1]
            return  Hi-Lo+1
        if Expr[0] in ['&&','||']: return 1
        if Expr[0] in ['&','|']: 
            Wa = expr_width(Expr[1],Mod)
            if type(Wa) is str: Wa = eval(Wa)
            Wb = expr_width(Expr[2],Mod)
            if type(Wb) is str: Wb = eval(Wb)
            if type(Expr[1]) is int: return Wb
            if type(Expr[2]) is int: return Wa
            return max(Wa,Wb)

    logs.log_error('expr_width %s' % str(Expr))
    return 1



