import string
import os,sys
import logs
def stam():
    return 0
logs.get_cycles = stam


import optimize0
import pprint


PaternEdge0 = ['list', ['edge', 'posedge', 'Clk' ], ['edge', 'negedge', 'Rst' ]]
PaternEdge1 = ['edge', 'posedge', 'Clk' ]
PaternEdge2 = ['*' ]

Patterns = [PaternEdge0,PaternEdge1,PaternEdge2]

DbgDumps =  '-dbg'  in sys.argv

BRICKS = '''
    select select_bus adder  adder_lit  and2  bufx  comparator  comparator_lit
    mpflipflop mflipflop flipflop  inv  mux2
    xor2 xor8
    or2  or3  or4  or5 or6 or7 or8
    shiftright_lit shiftleft_lit shiftleft  shiftright  subtractor  subtractor_lit multiplier multiplier_lit
'''.split()



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
    if not Mod: 
        logs.log_error('no current in Env')
        return
    Mod.MUX2S = {}
#    if '-redo' not in sys.argv:
#        if os.path.exists('pys/%s.py' % Mod.Module):
#            return
    
    buildSons(Mod,Env)
    useParams(Mod)
    computeParams(Mod,4)
    preprocess(Mod)
    dumpver(Mod,'%s.befns' % Mod.Module)
    always(Mod)
    dumpver(Mod,'%s.befz' % Mod.Module)
    replaceFunctions(Mod)
    dumpver(Mod,'%s.befy' % Mod.Module)
    instances(Mod)
    dumpver(Mod,'%s.befx' % Mod.Module)
    for Dst,Src,_,_ in Mod.hard_assigns:
        Wid = Mod.exprWidth(Dst)
        Src0 = synth0(Src,Mod,Wid)
        merge(Dst,Src0,Mod)
    dumpver(Mod,'%s.befw' % Mod.Module)
    Mod.hard_assigns = []
    dumpver(Mod,'%s.bef0' % Mod.Module)
    always(Mod)
#    dumpver(Mod,'%s.bef1' % Mod.Module)
    clearBufs(Mod)
    removeParams(Mod)
    dumpver(Mod,'%s.bef2' % Mod.Module)
    optimize0.optimize0(Mod)
    dumpver(Mod,'%s.bef3' % Mod.Module)
    optimize0.makeByBits(Mod)
    optimize0.optimize0(Mod)
    optimize0.zeroDriveRound(Mod,[],'A')
    Ones = optimize0.bufx_round(Mod,'A')
#    dumpver(Mod,'%s.bef4' % Mod.Module)
    optimize0.bufx_round(Mod,'B')
    optimize0.zeroDriveRound(Mod,Ones,'B')
#    dumpver(Mod,'%s.bef5' % Mod.Module)
    optimize0.zeroDriveRound(Mod,[],'C')
#    dumpver(Mod,'%s.bef6' % Mod.Module)
    Done = 1
    Rnd = 0
    while Done > 0 :
        Done = optimize0.similarGatesRound(Mod,'D'+ str(Rnd))
        logs.log_info("similarGatesRound %s %s" % (Rnd,Done))
        Rnd += 1
    optimize0.zeroDriveRound(Mod,Ones,'E')
    checker(Mod,Env)
    if not os.path.exists('glv'): os.mkdir('glv')
    dumpver(Mod,'glv/%s.v' % Mod.Module,True)
    dump_python(Mod)
    keep_save()
    Flog = open('pymon.log0')
    Lines = Flog.read()
    if not os.path.exists('logs'): os.mkdir('logs')
    Flog = open('logs/%s.log' % (Mod.Module),'w')
    Flog.write(Lines)
    Flog.close()

def dump_python(Mod):
    if not os.path.exists('pys'): os.mkdir('pys')
    Fout = open("pys/%s.py" % Mod.Module,'w')
    Fout.write('INSTS = {}\n')
    Fout.write("NETS = ")
    pprint.pprint(Mod.nets,Fout)
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst] 
        Conns = pprint.pformat(Obj.conns)
        Params = pprint.pformat(Obj.params)
        Fout.write('INSTS["%s"] = ("%s",%s,%s)\n' % (Inst,Obj.Type,Params,Conns))

    Fout.close()

    

def dumpver(Mod,Fname,Overide=False):
    if not Overide and not DbgDumps: return
    File = open(Fname,'w')
    Mod.dump_verilog(File)
    File.close()

def computeParams(Mod,Deep):
    Done = True
    for Prm in Mod.parameters:
        Val = Mod.parameters[Prm]
        if type(Val) is not int:
            Val2 = Mod.compute_int(Val)
            Mod.parameters[Prm] = Val2
            Done = False
    for Prm in Mod.localparams:
        Val = Mod.localparams[Prm]
        if type(Val) is not int:
            Val2 = Mod.compute_int(Val)
            Mod.localparams[Prm] = Val2
            Done = False
    if (not Done) and (Deep>0):
        computeParams(Mod,Deep-1)


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
ASYNCS = {}
def always(Mod):
    global EJECTS,ASYNCS
    for Alw in Mod.alwayses:
        EJECTS = {}
        ASYNCS = {}
        Edge = Alw[0]
        Body = Alw[1]
        if (len(Body) == 2) and (Body[0] == 'list'): Body = Body[1]
        for ind,Pat in enumerate(Patterns):
            Vars = match(Edge,Pat,{})
            if Vars:
                Vars = Vars[1]
                if ind==0:
                    if Body[0] == 'ifelse':
                        scanDeep(Body[2],Body[1],(0,Vars['Clk'],Vars['Rst']),Mod,True)   
                        scanDeep(Body[3],[],(0,Vars['Clk'],Vars['Rst']),Mod)   
                    else:
                        logs.log_error("always bad %s" % str(Body[2]))
                elif ind==1:
                    scanDeep(Body,[],(1,Vars['Clk']),Mod)   
                elif ind==2:
                    scanDeep(Body,[],(2),Mod)   
                dealEjects(Mod,Edge)
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
#    logs.log_info('PARTIALS %s' % str(Partials))
    return Partials,Fulls

def printEJECTS(Pat):
    logs.log_info("DSTLIST: %s" % str(DSTLISTS))
    for Key in EJECTS:
        List = EJECTS[Key]
        logs.log_info('EJECT %s %s' % (Pat,Key))
        for Item in List:
            logs.log_info('      %s' % str(Item))

def dealEjects(Mod,Pat):
    printEJECTS(Pat)
    Partials,Fulls = predealEjects(Mod)        
    ejectFulls2(Mod,Fulls,Pat)
    ejectPartials2(Mod,Partials)

# ILIA
def ejectFulls2(Mod,Fulls,Pat):
    for Dst in Fulls:
        List = EJECTS[Dst]
        Wid0 = Mod.exprWidth(Dst)
        TT = List[0][2]
        logs.log_info("FULL pat=%s dst=%s len=%s wid=%s tt=%s list=%s" % (Pat,Dst,len(List),Wid0,TT,List))
        if (len(List) == 1)and (Pat == '*'):
            Port = List[0]
            Src0 = synth0(Port[0],Mod,Wid0)
            Cond = synth0(Port[1],Mod,1)
            Src1 = synth0(['&&',Cond,Src0],Mod,1)
            Obj = Mod.add_inst_conns('bufx','%s_buf' % Dst,[('a',Src1),('x',Dst)])

            
        elif (len(List) == 1):
            Obj = Mod.add_inst_conns('flipflop','%s_reg' % Dst,[('clk',TT[1]),('q',Dst)])
            Obj.params['WID'] = Wid0
            if Dst in ASYNCS:
                AS = ASYNCS[Dst][0]
                Default = AS[0]
                if type(Default) is not int:
                    Default = eval(Default,Mod.parameters,Mod.localparams)
                Obj.params['ASYNC'] = Default
                if (len(AS[1]) == 2) and (AS[1][0] in ('~','!')):
                    Obj.conns['rst_n'] = AS[1][1]
                else:
                    Obj.conns['rst'] = synth0(AS[1],Mod,1)
            else:
                Obj.conns['rst_n'] = 'vcc'
            Port = List[0]
            Src0 = synth0(Port[0],Mod,Wid0)
            if Port[1] == []: 
                Cond = 'vcc'
            else:
                Cond = synth0(Port[1],Mod,1)
            Obj.conns['en'] = Cond
            Obj.conns['d'] = Src0

        elif (Pat == '*'):
            logs.log_info("LEN>1 %d dst=%s list= " % (len(List),Dst))
            for Item in List:
                logs.log_info("       LEN>1 %d item=%s " % (len(List),Item))
        else:
            Obj = Mod.add_inst_conns('mflipflop','%s_reg' % Dst,[('clk',TT[1]),('q',Dst)])
            Obj.params['WID'] = Wid0
            Obj.params['PORTS'] = len(List)
            if Dst in ASYNCS:
                AS = ASYNCS[Dst][0]
                Default = AS[0]
                if type(Default) is not int:
                    Default = eval(Default,Mod.parameters,Mod.localparams)
                Obj.params['ASYNC'] = Default
                if (len(AS[1]) == 2) and (AS[1][0] in ('~','!')):
                    Obj.conns['rst_n'] = AS[1][1]
                else:
                    Obj.conns['rst_n'] = synth0(AS[1],Mod,1)
            else:
                Obj.conns['rst_n'] = "vcc"
            for ind,Port in enumerate(List):
                Src0 = synth0(Port[0],Mod,Wid0)
                if Port[1] == []: 
                    Cond = 'vcc'
                else:
                    Cond = synth0(Port[1],Mod,1)
                Obj.conns['en%d'% ind] = Cond
                Obj.conns['d%d'% ind] = Src0


#    sys.exit()


def ejectFulls(Mod,Fulls):
    for Dst in Fulls:
        List = EJECTS[Dst]
        Wid0 = Mod.exprWidth(Dst)
        logs.log_info("FULL %s len=%s wid=%s list=%s" % (Dst,len(List),Wid0,List))
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
        logs.log_info("FULL2 %s len=%s wid=%s list=%s" % (Dst,len(List),Wid0,List))
        if (TT == 2) or (TT[0] in [0,1,2]):
            logs.log_info("FULL3 TT=%s %s len=%s wid=%s list=%s  dsts=%s " % (TT,Dst,len(List),Wid0,List,Dst in DSTLISTS))
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
                            if Dstx[0] != 'bus': Dstx = ['bus']+Dstx
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
            logs.log_error("222222 %s %s %s" %(Src0,Cond0,Dst))

# ILIA

def ejectPartials2(Mod,Partials):
    for Bus in Partials:
        Wid = Mod.exprWidth(Bus)
        _,WW = Mod.nets[Bus]
        Wid1 = -1
        if (type(WW) is tuple) and (WW[0] == 'packed'):
            H1,L1 = WW[1]
            H2,L2 = WW[2]
            H1 = Mod.pr_expr(H1)
            L1 = Mod.pr_expr(L1)
            H2 = Mod.pr_expr(H2)
            L2 = Mod.pr_expr(L2)
            if type(H1) is str:
                H1 = eval(H1,Mod.parameters,Mod.localparams)
            if type(L1) is str:
                L1 = eval(L1,Mod.parameters,Mod.localparams)
            if type(H2) is str:
                H2 = eval(H2,Mod.parameters,Mod.localparams)
            if type(L2) is str:
                L2 = eval(L2,Mod.parameters,Mod.localparams)
            Wid1 = H1-L1+1
            Wid2 = H2-L2+1

        Ports = []
        for Dst in EJECTS:
            if included(Dst,Bus):
                List = EJECTS[Dst]
                Ports.append((Dst,List))
        TT = Ports[0][1][0][2]
        Obj = Mod.add_inst_conns('mpflipflop','%s_reg' % Bus,[('clk',TT[1]),('q',Bus)])
        Obj.params['PORTS'] = len(Ports)
        Obj.params['WIDO'] = Wid
        if Wid1>0:
            Obj.params['DEPTH'] = Wid1
            Obj.params['LINE'] = Wid2
        if Bus in ASYNCS:
            AS = ASYNCS[Bus][0]
            Default = AS[0]
            if type(Default) is not int:
                Default = eval(Default,Mod.parameters,Mod.localparams)
            Obj.params['ASYNC'] = Default
            if (len(AS[1]) == 2) and (AS[1][0] in ('~','!')):
                Obj.conns['rst_n'] = AS[1][1]
            else:
                Obj.conns['rst'] = synth0(AS[1],Mod,1)

        for ind,(Dst,Port) in enumerate(Ports):
            PP = Port[0]
            Src0 = synth0(PP[0],Mod,Wid)
            if PP[1] == []:
                Cond = 'vcc'
            else:
                Cond = synth0(PP[1],Mod,1)
            if len(Ports) == 1:                
                Obj.conns['en'] = Cond
                Obj.conns['d'] = Src0
                Wid0 = Mod.exprWidth(Dst)
                Obj.params['WIDI'] = Wid0
            else:
                Obj.conns['en%d'% ind] = Cond
                Obj.conns['d%d'% ind] = Src0
                Wid0 = Mod.exprWidth(Dst)
                Obj.params['wid%d'% ind] = Wid0
                Ind0,Ind1 = indexify(Dst,Mod)
                if Ind0 == Ind1:
                    if type(Ind0) is int:
                        Obj.params['pos%d'% ind] = Ind0
                    else:
                        Obj.conns['pos%d'% ind] = Ind0
                elif Ind0>=0:
                    Obj.params['lo%d'% ind] = Ind0
                    Obj.params['hi%d'% ind] = Ind1
                
                


def busify_x(Sig):
    if (type(Sig) is str)and('[' in Sig)and(Sig[-1]==']')and(Sig[0]!='\\'):
        ind = Sig.index('[')
        Net = Sig[:ind]
        Inds = Sig[ind+1:-1]
        if ':' in Inds:
            ww = Inds.split(':')
            return ['subbus',Net,ww[0],ww[1]]
        return ['subbit',Net,Inds]
    return Sig


def indexify(Dst,Mod):
    Sig = busify_x(Dst)
    if Sig[0] == 'subbit':
        try:
            Ind0 = eval(Sig[2],Mod.parameters,Mod.localparams)
        except:
            Ind0 = Sig[2]
        Ind1 = Ind0
        return Ind0,Ind1
    if Sig[0] == 'subbus':
        Ind0 = eval(Sig[2])
        Ind1 = eval(Sig[3])
        return Ind0,Ind1
    return -1,-3


def included(Dst,Bus):
    if Dst == Bus: return True
    if not Dst.startswith(Bus): return False
    if '[' in Dst:
        Base = Dst[:Dst.index('[')]
        return Base == Bus
    return False

def aaa():
        for Dst in EJECTS:
            List = EJECTS[Dst]
        TT = List[0][2]
        Obj = Mod.add_inst_conns('mflipflop','%s_reg' % Dst,[('clk',TT[1]),('q',Dst)])
        Obj.params['WID'] = Wid
        Obj.params['PORTS'] = len(List)

        if (3<4):
            if Dst in ASYNCS:
                AS = ASYNCS[Dst][0]
                Default = AS[0]
                Obj.params['ASYNC'] = Default
                if (len(AS[1]) == 2) and (AS[1][0] in ('~','!')):
                    Obj.conns['rst_n'] = AS[1][1]
                else:
                    Obj.conns['rst'] = synth0(AS[1],Mod,1)
            else:
                Obj.conns['rst_n'] = 'vcc'

        if Dst in ASYNCS:
            AS = ASYNCS[Dst][0]
            Default = AS[0]
            Obj.params['ASYNC'] = Default
            if (len(AS[1]) == 2) and (AS[1][0] in ('~','!')):
                Obj.conns['rst_n'] = AS[1][1]
            else:
                Obj.conns['rst'] = synth0(AS[1],Mod,1)
        for ind,Port in enumerate(List):
            Src0 = synth0(Port[0],Mod,Wid0)

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
                logs.log_info("COMPATIBLE ii=%s dst=%s list=%s code=%s bus=%s wid=%s wid0=%s " % (II,Dst,List,Code,Bus,Wid,Wid0))
                if Code:
                    And = 0
                    if type(Code) is not int:
                        And = ['==',Code,II]
                    for  Ind,(Src,Cond,TT) in enumerate(List):
                        logs.log_info('COMP2 which=%d ii=%s dst=%s src=%s cond=%s tt=%s' % (Ind,II,Dst,Src,Cond,TT))
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

                        logs.log_info('CND dst=%s code=%s and=%s cond=%s' % (Dst,Code,And,Cond))
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
            if Dats != []:
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

def int2bus(Wid,Int):
    res = []
    for ii in range(Wid):
        if (Int>>ii) & 1:
            res.append('vcc')
        else:
            res.append('gnd')
    res.reverse()
    return ['bus']+res

        

def extractBit(Src,II,Wid,Mod):
    if type(Src) is str:
        if Src in Mod.nets:
            _,Wid1 = Mod.nets[Src]
            if type(Wid1) is tuple:
                if Wid1[0] == 'packed':
                    return extractBit(['subbus',Src,(Wid1[1][0],Wid1[1][1]) ], II,Wid,Mod)
                else:
                    return extractBit(['subbus',Src,(Wid1[0],Wid1[1])],II,Wid,Mod)
            return Src
    if type(Src) is int:
        return int2bus(Wid,Src) 
    if type(Src) is list:
        if Src[0] == 'bin':
            Val = int(Src[1],2)
            return int2bus(Wid,Val)
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
            if (Wid == 1):
                XX = Src[:]
                XX.reverse()
                return XX[II]
            else:
                return Src
    
    Cond0 = synth0(Src,Mod,Wid)
    return extractBit(Cond0,II,Wid,Mod)
    



def compatible(Ind,Bus,Dst):
    if Bus == Dst: return 1
    if '[' in Dst:
        B0 = Dst[:Dst.index('[')]
        if B0 != Bus: return False
        I0 = Dst[Dst.index('[')+1:-1]
        if ':' in I0:
            ww = I0.split(':')
            Hi = eval(ww[0])
            Lo = eval(ww[1])
            if (Ind>=Lo) and (Ind<=Hi):
                return '%s[%s]' % (Bus,Ind)
            return False
        if I0[0] in '0123456789': 
            I1 = eval(I0)
            if I1 != Ind: return False
            return 1
        return I0

    if Bus != Dst: return False
    logs.log_error("COMPATIBLE %s %s %s" % (Ind,Bus,Dst))
    return False

def scanDeep(Body,Sofar,Kind,Mod,Async=False):
    if Body[0] == 'for': return 0
    if type(Body) is list:
        if Body[0] == '<=':
            eject(Body[1],Body[2],Sofar,Kind,Mod,Async)
        elif Body[0] == '=':
            eject(Body[1],Body[2],Sofar,Kind,Mod,Async)
        elif Body[0] == 'list':
            for Item in Body[1:]:
                scanDeep(Item,Sofar,Kind,Mod,Async)
        elif Body[0] == 'ifelse':
            Cond = Body[1]
            if Sofar == []:
                DeepY = [Cond]
                DeepN = [['!',Cond]]
            else:
                DeepY = ['&&',Cond,Sofar]
                DeepN = ['&&',['!',Cond],Sofar]
            scanDeep(Body[2],DeepY,Kind,Mod,Async)
            scanDeep(Body[3],DeepN,Kind,Mod,Async)
        elif Body[0] == 'if':
            Cond = Body[1]
            if Sofar == []:
                DeepY = [Cond]
            else:
                DeepY = ['&&',Cond,Sofar]
            scanDeep(Body[2],DeepY,Kind,Mod,Async)
        else:
            logs.log_error('scanDeep failed on async=%s  body=%s' % (Async,Body))

    else:
        logs.log_error('scanDeep failed on %s' % (str(Body),Async))

DSTLISTS = {}        
def eject(Dst,Src,Cond,Kind,Mod,Async):
    if type(Dst) is list:
        Dst0 = Mod.pr_expr(Dst)
    else:
        Dst0 = Dst
    if Dst0 not in DSTLISTS:
        DSTLISTS[Dst0] = Dst
    if Async:
        if type(Src) is str:
            Src = eval(Src,Mod.parameters,Mod.localparams)
        elif type(Src) is int:
            Src = Src
        elif type(Src) is list:
            if Src[0] in ['bin','hex','dig']:
                Val = getLitVal(Src)
                Src = str(Val)
            else:  
                Srcx = Mod.pr_expr(Src)
                Src = eval(Srcx,Mod.parameters,Mod.localparams)
        if Dst0 in ASYNCS:
            ASYNCS[Dst0].append((Src,Cond,Kind))
        else:
            ASYNCS[Dst0] = [(Src,Cond,Kind)]
        return
    if Dst0 in EJECTS:
        EJECTS[Dst0].append((Src,Cond,Kind))
    else:
        EJECTS[Dst0] = [(Src,Cond,Kind)]

def getLitVal(Src):
    Wid = int(Src[1])
    Act = Src[2]
    if Src[0] == 'hex':
        Val = int(Act,16)
    elif Src[0] == 'bin':
        Val = int(Act,2)
    elif Src[0] == 'dig':
        Val = int(Act,10)
    return Val


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
    return Renames,Bufs



def merge(Dst,Src,Mod):
    Wid = Mod.sig_width(Dst)
    Sbits = splitBits(Src,Mod,Wid)
    Dbits = splitBits(Dst,Mod,Wid)
    if Sbits[0] == 'bus': Sbits.pop(0)
    if Dbits[0] == 'bus': Dbits.pop(0)
    while (Sbits!=[]) and (Dbits!=[]):
        SB = Sbits.pop(-1) 
        DB = Dbits.pop(-1) 
        addInst1('bufx',DB,SB,Mod)
    while Dbits!=[]:
        DB = Dbits.pop(-1) 
        addInst1('bufx',DB,'gnd',Mod)
        

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
            if len(Wid) == 2:
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
            elif (len(Wid) == 3) and (Wid[0] == 'packed'):
                Hi0,Lo0 = Wid[1]
                Hi0 = Mod.compute_int(Hi0)
                Lo0 = Mod.compute_int(Lo0)
                Hi1,Lo1 = Wid[2]
                Hi1 = Mod.compute_int(Hi1)
                Lo1 = Mod.compute_int(Lo1)
                Res = ['bus']
                while Lo0 <= Hi0:
                    II = Hi1
                    while II >= Lo1:
                        Sig = '%s[%s][%s]' % (Expr,Hi0,II)
                        Res.append(Sig)
                        II -= 1
                    Hi0 -= 1
                return Res

            else:
                logs.log_error("SPLIT WID  %s %s" % (Wid,str(Expr)))
                return [Expr]

    if type(Expr) is list:
        if len(Expr) == 0:
            return ['vdd']
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

        if Expr[0] == 'curly':
            Res = []
            for Ex in Expr[1:]:
                More = splitBits(Ex,Mod)
                Res.extend(More)
            return Res                


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
                logs.log_info('SUBBITX %s %s out=%s l1=%s' % (Bus,Key,Out,L1))
                KNOWNS[Key] = Out
                return [Out]
            else:
                _,Wid = Mod.nets[Bus]
                if (type(Wid) is tuple):
                    if Wid[0] == 'packed':
                        W1_0 = Mod.compute_int(Wid[1][0],False)-Mod.compute_int(Wid[1][1],False)+1
                        W1_1 = Mod.compute_int(Wid[1][1],False)-Mod.compute_int(Wid[1][0],False)+1
                        W1 = max(W1_0,W1_1)
                        W2_0 = Mod.compute_int(Wid[2][0],False)-Mod.compute_int(Wid[2][1],False)+1
                        W2_1 = Mod.compute_int(Wid[2][1],False)-Mod.compute_int(Wid[2][0],False)+1
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
                        KNOWNS[Key] = Res[:]
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
#    logs.log_info('HARD SYNTH0 %s mwid=%d src=%s' % (Depth,Mwid,Src))
    Res = synth0__(Src,Mod,Mwid,Depth)
    if (type(Res) is list) and (len(Res) == 1): Res = Res[0]
    return Res

def synth0__(Src,Mod,Mwid=64,Depth=0):
    if type(Src) is str: 
        if '.' in Src: return 0
        A0 = Mod.compute_int(Src,False)
        if type(A0) is int:
            return synth0(['dig',str(Mwid),str(A0)],Mod,Mwid,Depth)
        return Src
    if type(Src) is int: 
        XX =  Src & ((1<<Mwid)-1)
        XY = splitBits(XX,Mod,Mwid)
        return XY
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
                A0 = makeNotEqZero(A,Mod)
                if A0!='vcc':
                    LL.append(A0)
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
            if Len==0: return 'vcc'
            Out = makeWide(LL,'or',Mod)
            return Out

        if Src[0] == '^':
            if len(Src) == 3:
                Out = makeWideGate('xor2',Mod,Mwid,Src[1],Src[2],Depth)
                return Out
            elif len(Src) == 2:
                A = synth0(Src[1],Mod,Mwid,Depth+1)
                AA = splitBits(A,Mod)
                Len = len(AA)
                Out = makeWide(AA,'xor',Mod)
                return Out
                

        if (Src[0] == '|') and (len(Src) ==2):
            A = synth0(Src[1],Mod,Mwid,Depth+1)
            AA = splitBits(A,Mod)
            Len = len(AA)
            Out = makeWide(AA,'or',Mod)
            Mod.add_sig(Out,'wire',1)
            return Out

        if Src[0] == '~&':
            LL = synth0(Src[1],Mod,Mwid,Depth+1)
            Out = makeWide(LL,'nand',Mod)
            return Out


        if (Src[0] == '&') and (len(Src) ==2):
            A = synth0(Src[1],Mod,Mwid,Depth+1)
            AA = splitBits(A,Mod)
            Len = len(AA)
            Out = makeWide(AA,'and',Mod)
            Mod.add_sig(Out,'wire',1)
            return Out


        if Src[0] == '&':
            Out = makeWideGate('and2',Mod,Mwid,Src[1],Src[2],Depth)
            return Out

        if Src[0] == '|':
            Out = makeWideGate('or2',Mod,Mwid,Src[1],Src[2],Depth)
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
            AA = synth0(Src[1],Mod,Mwid,Depth+1)
            Out = addInst1('inv','',AA,Mod)
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
#            logs.log_info('QUEST mwid=%d OUT=%s yes=%s src2=%s src3=%s  yes0=%s no=%s' % (Mwid,Out,Yes,Src[2],Src[3],Yes0,No))
            if (Yes==No):
                if Yes == ['gnd']:
                    Res = ['bus']
                    for ii in range(Mwid):
                        Res.append('gnd')
                    return Res
                logs.log_info('YESNO %s' %(str(Yes)))
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
                Obj.params['YWID'] = len(Yes)
                if Yes[0] == 'curly': Obj.params['YWID']  -= 1
                Obj.params['NWID'] = len(No)
                if No[0] == 'curly': Obj.params['NWID']  -= 1
                Mod.MUX2S[Key] = Out
                return Out

        if Src[0] in ['>>']:
            AA = synth0(Src[1],Mod,Mwid,Depth+1)
            L1 = Mod.exprWidth(AA)
            Src2 = Mod.compute_int(Src[2],False)
            if type(Src2) is int:
                Out = Mod.add_sig('','wire',Mwid)
                Obj = Mod.add_inst_conns('shiftright_lit','',[('a',AA),('x',Out)])
                Obj.params['WID'] = Mwid
                Obj.params['shift'] = Src2
                return Out


            BB = synth0(Src[2],Mod,Mwid,Depth+1)
            Out = Mod.add_sig('','wire',Mwid)
            Obj = Mod.add_inst_conns('shiftright','',[('a',AA),('b',BB),('x',Out)])
            Obj.params['WID'] = Mwid
            return Out

        if Src[0] in ['<<']:
            AA = synth0(Src[1],Mod,Mwid,Depth+1)
            L1 = Mod.exprWidth(AA)
            Out = Mod.add_sig('','wire',Mwid)
            Src2 = Mod.compute_int(Src[2],False)
            if type(Src2) is int:
                Obj = Mod.add_inst_conns('shiftleft_lit','',[('a',AA),('x',Out)])
                Obj.params['WID'] = Mwid
                Obj.params['shift'] = Src2
                return Out

            BB = synth0(Src[2],Mod,Mwid,Depth+1)
            Obj = Mod.add_inst_conns('shiftleft','',[('a',AA),('b',BB),('x',Out)])
            Obj.params['WID'] = Mwid
            return Out

        if Src[0] in ['*']:
            AA = synth0(Src[1],Mod,Mwid,Depth+1)
            L1 = Mod.exprWidth(AA)
            Src2 = Mod.compute_int(Src[2],False)
            if type(Src2) is int:
                L2 = Mod.exprWidth(Src2)
                Out = Mod.add_sig('','wire',(L1+L2))
                Obj = Mod.add_inst_conns('multiplier_lit','',[('a',AA),('x',Out)])
                Obj.params['WID'] = L1+L2
                Obj.params['LIT'] =  Src2
                return Out


            BB = synth0(Src[2],Mod,Mwid,Depth+1)
            L2 = Mod.exprWidth(BB)
            Out = Mod.add_sig('','wire',(L1+L2))
            Obj = Mod.add_inst_conns('multiplier','',[('a',AA),('b',BB),('x',Out)])
            Obj.params['WID'] = L1+L2
            return Out
        if Src[0] in ['/']:
            AA = synth0(Src[1],Mod,Mwid,Depth+1)
            L1 = Mod.exprWidth(AA)
            BB = synth0(Src[2],Mod,Mwid,Depth+1)
            L2 = Mod.exprWidth(BB)
            Out = Mod.add_sig('','wire',L1)
            Obj = Mod.add_inst_conns('divider','',[('a',AA),('b',BB),('x',Out)])
            Obj.params['WID'] = L1
            return Out
        if Src[0] in ['%']:
            AA = synth0(Src[1],Mod,Mwid,Depth+1)
            L1 = Mod.exprWidth(AA)
            BB = synth0(Src[2],Mod,Mwid,Depth+1)
            L2 = Mod.exprWidth(BB)
            Out = Mod.add_sig('','wire',L1)
            Obj = Mod.add_inst_conns('remainder','',[('a',AA),('b',BB),('x',Out)])
            Obj.params['WID'] = L1
            return Out

        if Src[0] in COMPARES:
            Out = Mod.add_sig('','wire',1)

            A0 = Mod.compute_int(Src[1],False)
            B0 = Mod.compute_int(Src[2],False)
            if (type(B0) is int) and (type(A0) is int):
                if (A0 == B0) and (Src[0] in ['==','>=','=<','<=']): return 'vcc'
                if (A0 != B0) and (Src[0] in ['!=','>','<']): return 'vcc'
                return 'gnd'
            if type(B0) is int:
                AA = synth0(Src[1],Mod,Mwid,Depth+1)
                if (type(AA) is list) and (len(AA) == 1): AA = AA[0]
                Obj = Mod.add_inst_conns('comparator_lit','',[('a',AA),('x',Out)])
#                L1 = Mod.exprWidth(Src[1])
                L1 = Mod.exprWidth(AA)
#                logs.log_info('COMPARES l=%d aa=%s B0=%s src1=%s' % (L1,AA,B0,Src[1]))
                Obj.params['WID'] = L1
                Obj.params['LIT'] = B0
                Kind = COMPARES.index(Src[0])
                Obj.params['KIND'] = Kind
                return Out


            AA = synth0(Src[1],Mod,Mwid,Depth+1)
            BB = synth0(Src[2],Mod,Mwid,Depth+1)
            if (type(AA) is list) and (len(AA) == 1): AA = AA[0]
            if (type(BB) is list) and (len(BB) == 1): BB = BB[0]
            Obj = Mod.add_inst_conns('comparator','',[('a',AA),('b',BB),('x',Out)])
            L1 = Mod.exprWidth(AA)
            L2 = Mod.exprWidth(BB)
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
            if len(Res) == 2: return Res[1]
            return Res

        if (Src[0] == '-') and (len(Src) ==2):
            AA = synth0(0,Mod,Mwid,Depth+1)
            BB = synth0(Src[1],Mod,Mwid,Depth+1)
            L2 = Mod.exprWidth(BB)
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
                L1 = Mod.exprWidth(AA)
                Out = Mod.add_sig('','wire',1+L1)
                if Src[0] == '+': Type = 'adder_lit'
                if Src[0] == '-': Type = 'subtractor_lit'
                Obj = Mod.add_inst_conns(Type,'',[('a',AA),('x',Out)])
                Obj.params['WID'] = L1+1
                Obj.params['LIT'] = B0
                return Out

            if (type(A0) is int): 
                BB = synth0(Src[2],Mod,Mwid,Depth+1)
                L1 = Mod.exprWidth(BB)
                Out = Mod.add_sig('','wire',1+L1)
                if Src[0] == '+': Type = 'adder_lit'
                if Src[0] == '-': Type = 'subtractor_lit'
                Obj = Mod.add_inst_conns(Type,'',[('a',BB),('x',Out)])
                Obj.params['WID'] = L1+1
                Obj.params['LIT'] = A0
                return Out





            AA = synth0(Src[1],Mod,Mwid,Depth+1)
            BB = synth0(Src[2],Mod,Mwid,Depth+1)
            L1 = Mod.exprWidth(AA)
            L2 = Mod.exprWidth(BB)
            Out = Mod.add_sig('','wire',1+max(L1,L2))

            if Src[0] == '+': Type = 'adder'
            if Src[0] == '-': Type = 'subtractor'
            Obj = Mod.add_inst_conns(Type,'',[('a',AA),('b',BB),('x',Out)])
            Obj.params['WID'] = max(L1,L2)
            return Out

        if Src[0] == 'repeat':
            Many = Mod.compute_int(Src[1])
            Rep = synth0(Src[2],Mod,Mwid,Depth+1)
            if Rep[0] == 'bus': Rep.pop(0)
            Res = ['bus']
            for X in range(Many):
                Res.extend(Rep)
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
#            Bus = Src[1]
#            Ind = Src[2]
#            Wid = chunkWidth(Bus,Mod)
#            Wid0 = lineWidth(Bus,Mod)
#
#            if Wid0 == 1:
#                if (type(Ind) is int) and singleIndexBus(Bus,Mod):
#                    return ['%s[%d]' % (Bus,Ind)]
#                elif singleIndexBus(Bus,Mod):
#                    BB = synth0(Expr[2],Mod,Mwid)
#                

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



def makeWideGate(Gate,Mod,Mwid,Src1,Src2,Depth):
    A = synth0(Src1,Mod,Mwid,Depth+1)
    B = synth0(Src2,Mod,Mwid,Depth+1)
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
        else: 
            addInst2(Gate,OO,A0,B0,Mod)
    return Out



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
    if (type(A) is list)and(len(A) == 1): A = A[0]
    if (type(B) is list)and(len(B) == 1): B = B[0]
    if type(A) is list:
        print("addInst2A",Type,Out,A,B)
        breakIt();
    if type(B) is list:
        print("addInst2B",Type,Out,A,B)
        breakIt();
    Mod.add_inst_conns(Type,'',[('a',A),('b',B),('x',Out)])
#    Mod.add_inst_conns(Type,'',[('a',A),('b',B),('x',Out)])
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
            if Func == '$clog2':
                Val = Src[2][0]
                Val = Mod.compute_int(Val)
                return Val
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
        if Obj.Type not in BRICKS:
            for Pin in Obj.conns:
                Sig = Obj.conns[Pin]
                if needsSynth(Sig):
                    Res = synth0(Sig,Mod)
                    Bits = splitBits(Res,Mod)
                    logs.log_info("INSTANCE %s %s %s %s " % (Obj.Type,Sig,Res,Bits))
                    Obj.conns[Pin] = Bits
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

Ops = '! ~ | || & && ^ ~ - + * >> << >= => <= =< < >'
def needsSynth(Sig):
    if type(Sig) is str: return False
    if type(Sig) is int: return False
    if type(Sig) is list:
        if Sig[0] in ['question','curly','hex','dig','bin','subbus','subbit']: return True
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

def makeNotEqZero(AA,Mod):
    if AA == 'vcc': return 'vcc'
    if AA == 'gnd': return 'gnd'
    if type(AA) is int:
        if AA==0: return 'gnd'
        return 'vcc'
    if type(AA) is str:
        if AA in Mod.nets:
            _,Wid = Mod.nets[AA]
            if Wid in [0,1,'0','1']: return AA
            if type(Wid) is tuple:
                Expr = ['!=',AA,0]
                return synth0(Expr,Mod,1)
        elif '[' in AA:
            Bus = AA[:AA.index('[')]
            if Bus in Mod.nets:
                return AA
        else:                
            logs.log_error('STR and not a NET "%s"' % (AA))
            return AA

    if type(AA) is list:
        if len(AA) == 1: return makeNotEqZero(AA[0],Mod)
        if AA[0] == 'subbit': return AA
        if AA[0] == 'subbus':
            Expr = ['!=',AA,0]
            return synth0(Expr,Mod,1)
        if AA[0] == 'bus':
            if 'vcc' in AA: return 'vcc'
            return 'gnd'
            
    logs.log_error('makeNotEqZero got "%s"' % str(AA))
    return AA
        
STDPARAMS = {}
STDPARAMS[('syncfifo','0')] = 'WID'
STDPARAMS[('syncfifo','1')] = 'DEPTH'
STDPARAMS[('syncfifo_v2','0')] = 'WID'
STDPARAMS[('syncfifo_v2','1')] = 'DEPTH'
Parametrized = []
def buildSons(Mod,Env):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        Params = {}
        for Prm in Obj.params:
            Prmx = str(Prm)
            if Prmx[0] in '0123456789':
                Key = (Type,Prmx)
                if Key in STDPARAMS:
                    Name = STDPARAMS[Key]
                    Params[Name] = Obj.params[Prm]
                else:
                    logs.log_error('BUILDSONS key=%s not given' % str(Key))
                    Params[Prm] = Obj.params[Prmx] 
            else:
                Params[Prm] = Obj.params[Prmx] 
        Obj.params = Params

        Params = list(Obj.params.keys())
        Params.sort()

        LLL = ''
        if Params != []:
            for Prm in Params:
                Val = Obj.params[Prm]
                if type(Val) is not int:
                    Val2 = Mod.compute_int(Val)
                    Val = Val2
                Type += '_%s' % Val
                LLL += ' %s=%s'% (Prm,Val)
            Parametrized.append((Obj.Type,Type,LLL))
        else:
#            keep_system('pyver.py ../rtl/%s.v -do synthesis0 -do clean' % (Type))
            keep_system('prep.py ../rtl/%s.v ' % (Type))
    for Type,FullType,LLL in Parametrized:
        if not os.path.exists('glv/%s.v' % FullType):
            logs.log_info('GENERATE %s from %s  %s' % (FullType,Type,LLL))
#            keep_system('pyver.py ../rtl/%s.v -do synthesis0 -do clean -define "%s"' % (Type,LLL))
            keep_system('prep.py ../rtl/%s.v %s ' % (Type,LLL))
KEEPS = []
def keep_system(Txt):
    KEEPS.append(Txt+'\n')
    
def keep_save():
    if not os.path.exists('todo.keeps'):
        Lines = []
    else:
        Fout = open('todo.keeps')
        Lines = Fout.readlines()
        Fout.close()
    for line in KEEPS:
        if line not in Lines:
            Lines.append(line)

    Fout = open('todo.keeps','w')
    for line in Lines:
        Fout.write('%s' % line)
    Fout.close()




GLVS = '''
    nand8 xor2 xor8 and2 or2 or3 or4 or5 or6 or7 or8 and3 and4 and5 and6 and7 and8 bufx inv
    mux2 mflipflop mpflipflop flipflop shiftleft shiftright comparator_lit comparator
    adder subtractor multiplier divider remainder
    adder adder_lit subtractor subtractor_lit
    shiftright_lit shiftleft_lit
    select select_bus
'''.split()

def checker(Mod,Env):
    Mod.buildNetTable()
    Oks = 0
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        if os.path.exists('glv/%s.v' % Type):
            if Type not in Env.Modules:
                Fname = 'glv/%s.v' % Type
                Env.read_gate_level_verilog_file(Fname,Env.rundir,Env)
            Son = Env.Modules[Type]
            for Pin in Obj.conns:
                if Obj.conns[Pin] and (Pin not in Son.nets):
                    logs.log_error('missing net %s of %s in inst %s' % (Pin,Type,Inst))
            for Net in Son.nets:
                Dir,_ = Son.nets[Net]
                if Dir in ['input']:
                    if Net not in Obj.conns:
                        logs.log_error('missing input %s of %s in inst %s' % (Net,Type,Inst))
            
        elif Type in 'nand8 xor2 xor8 and2 or2 or3 or4 or5 or6 or7 or8 and3 and4 and5 and6 and7 and8 bufx inv'.split():
            Oks += checkSimple(Obj,Mod)
        elif Type in 'adder subtractor multiplier divider remainder'.split():
            Oks += checkArith(Obj,Mod)
        elif Type == 'mux2':
            Oks += checkMux2(Obj,Mod)
        elif Type == 'flipflop':            
            Oks += checkFlipFlop(Obj,Mod)
        elif Type == 'mflipflop':            
            Oks += checkMFlipFlop(Obj,Mod)
        elif Type == 'mpflipflop':            
            Oks += checkMPFlipFlop(Obj,Mod)
        elif Type in 'shiftleft shiftright'.split():            
            Oks += checkShifts(Obj,Mod)
        elif Type in 'shiftleft_lit shiftright_lit'.split():            
            Oks += checkShiftsLit(Obj,Mod)
        elif Type == 'comparator_lit':            
            Oks += checkComparatorLit(Obj,Mod)
        elif Type == 'comparator':            
            Oks += checkComparator(Obj,Mod)
        elif Type == 'adder_lit':            
            Oks += checkAdderLit(Obj,Mod)
        elif Type == 'multiplier_lit':            
            Oks += checkAdderLit(Obj,Mod)
        elif Type == 'subtractor_lit':            
            Oks += checkSubtractorLit(Obj,Mod)
        elif Type == 'select_bus':            
            Oks += checkSelectBus(Obj,Mod)
        elif Type == 'select':            
            Oks += checkSelect(Obj,Mod)
        else:
            logs.log_error('ADD %s to checkers' % Type)
    logs.log_info('CORRECTS %s  ERRORS %s' % (Oks,logs.Errors))
def checkComparatorLit(Obj,Mod):
    Wid = Obj.params['WID']
    As,Xs = 0,0
    for Pin in Obj.conns:
        Sig = Obj.conns[Pin]
        if Pin[0] == 'x': Xs += 1
        elif Pin[0] == 'a': As += 1
    if (As!=Wid) or (Xs!=1):
        logs.log_error('%s ComparatorLit %s %s as=%d x=%d wid=%d' % (Mod.Module,Obj.Type,Obj.Name,As,Xs,Wid))
        return 0
    else:
        return 1

def checkComparator(Obj,Mod):
    Wida = Obj.params['WIDA']
    Widb = Obj.params['WIDB']
    As,Bs,Xs = 0,0,0
    for Pin in Obj.conns:
        Sig = Obj.conns[Pin]
        if Pin[0] == 'x': Xs += 1
        elif Pin[0] == 'a': As += 1
        elif Pin[0] == 'b': Bs += 1
    if (As!=Wida) or (Bs!=Widb) or (Xs!=1):
        logs.log_error('Comparator %s %s as=%d bs=%d x=%d wid=%d:%d' % (Obj.Type,Obj.Name,As,Bs,Xs,Wida,Widb))
        return 0
    else:
        return 1

def diff1(A,B):
    Abs = abs(A-B)
    return Abs>1

def checkAdderLit(Obj,Mod):
    Wid = Obj.params['WID']
    As,Xs = 0,0
    for Pin in Obj.conns:
        Sig = Obj.conns[Pin]
        if Pin[0] == 'x': Xs += 1
        elif Pin[0] == 'a': As += 1
    if diff1(Xs,Wid) or diff1(As,Wid):
        logs.log_error('ARITHLIT %s %s wid=%d xs=%d a=%d ' % (Obj.Type,Obj.Name,Wid,Xs,As))
        return 0
    else:
        return 1


def checkSubtractorLit(Obj,Mod):
    Wid = Obj.params['WID']
    As,Xs = 0,0
    for Pin in Obj.conns:
        Sig = Obj.conns[Pin]
        if Pin[0] == 'x': Xs += 1
        elif Pin[0] == 'a': As += 1
    if diff1(Xs,Wid) or diff1(As,Wid):
        logs.log_error('ARITHLIT %s %s wid=%d xs=%d a=%d ' % (Obj.Type,Obj.Name,Wid,Xs,As))
        return 0
    else:
        return 1

def checkSelectBus(Obj,Mod):
    Wid = Obj.params['WID']
    Depth = Obj.params['DEPTH']

    As,Bs,Xs = 0,0,0
    for Pin in Obj.conns:
        Sig = Obj.conns[Pin]
        if Pin[0] == 'x': Xs += 1
        elif Pin[0] == 'a': As += 1
        elif Pin[0] == 'b': Bs += 1
    if (Xs != Wid) or (As != (Depth*Wid)):
        logs.log_error('SELECTBUS %s %s wid=%d*%d xs=%d a=%d b=%d ' % (Obj.Type,Obj.Name,Wid,Depth,Xs,As,Bs))
        return 0
    else:
        return 1


def checkSelect(Obj,Mod):
    Wid = Obj.params['WID']

    As,Bs,Xs = 0,0,0
    for Pin in Obj.conns:
        Sig = Obj.conns[Pin]
        if Pin[0] == 'x': Xs += 1
        elif Pin[0] == 'a': As += 1
        elif Pin[0] == 'b': Bs += 1
    if (Xs != 1) or diff1(As,Wid):
        logs.log_error('SELECT %s %s wid=%d*%d xs=%d a=%d b=%d ' % (Obj.Type,Obj.Name,Wid,Depth,Xs,As,Bs))
        return 0
    else:
        return 1




def checkArith(Obj,Mod):
    Wid = Obj.params['WID']
    As,Bs,Xs = 0,0,0
    for Pin in Obj.conns:
        Sig = Obj.conns[Pin]
        if Pin[0] == 'x': Xs += 1
        elif Pin[0] == 'a': As += 1
        elif Pin[0] == 'b': Bs += 1
    if Obj.Type == 'multiplier':
        if diff1(Xs,Wid) or diff1((As+Bs),Wid):
            logs.log_error('ARITH %s %s wid=%d xs=%d a=%d b=%d' % (Obj.Type,Obj.Name,Wid,Xs,As,Bs))
            return 0
        return 1
    elif not diff1(Xs,Wid) and not diff1(As,Wid) and (Bs<As):
        Pins = list(Obj.conns.keys())
        for Pin in Pins:
            if Pin[0] == 'a':
                Num = Pin[1:]
                Dpin = 'b%s' % Num
                if Dpin not in Obj.conns:
                    Obj.conns[Dpin] = 'gnd'
        return 1
    elif diff1(Xs,Wid) or diff1(As,Wid) or diff1(Bs,Wid):

        logs.log_error('ARITH %s %s wid=%d xs=%d a=%d b=%d' % (Obj.Type,Obj.Name,Wid,Xs,As,Bs))
        return 0
    else:
        return 1


def checkMux2(Obj,Mod):
    Wid = Obj.params['WID']
    As,Bs,Xs,Sel = 0,0,0,0
    for Pin in Obj.conns:
        Sig = Obj.conns[Pin]
        if Pin[0] == 'x': Xs += 1
        elif Pin.startswith('yes'): As += 1
        elif Pin.startswith('no'): Bs += 1
        elif Pin == 'sel':
            Sel += 1
    if diff1(Xs,Wid) or (Sel!=1):
        logs.log_error('MUX2 E0 %s %s wid=%d xs=%d yes=%d no=%d sel=%d' % (Obj.Type,Obj.Name,Wid,Xs,As,Bs,Sel))
        return 0
    elif diff1(As,Wid) and diff1(Bs,Wid) :
        logs.log_error('MUX2 E1 %s %s wid=%d xs=%d yes=%d no=%d sel=%d' % (Obj.Type,Obj.Name,Wid,Xs,As,Bs,Sel))
        return 0
    elif ((As==1) or (Bs==1) ) and (Xs>1) :
        logs.log_error('MUX2 E2 %s %s wid=%d xs=%d yes=%d no=%d sel=%d' % (Obj.Type,Obj.Name,Wid,Xs,As,Bs,Sel))
        return 0
    else:
        return 1


def checkMFlipFlop(Obj,Mod):
    return 1

def checkMPFlipFlop(Obj,Mod):
    return 1

def checkFlipFlop(Obj,Mod):
    Wid = Obj.params['WID']
    Ds,Qs,En,Clk,Rst = 0,0,0,0,0
    for Pin in Obj.conns:
        Sig = Obj.conns[Pin]
        if Pin[0] == 'q': Qs += 1
        elif Pin[0] == 'd': Ds += 1
        elif Pin == 'en': En += 1
        elif Pin == 'clk': Clk += 1
        elif Pin == 'rst_n': Rst += 1
    if (Qs==Wid) and (Ds<Wid) and (En==1) and (Clk==1) and (Rst <= 1):
        Pins = list(Obj.conns.keys())
        for Pin in Pins:
            if Pin[0] == 'q':
                Num = Pin[1:]
                Dpin = 'd%s' % Num
                if Dpin not in Obj.conns:
                    Obj.conns[Dpin] = 'gnd'
        return 1
        
    
    if diff1(Qs,Wid) or (diff1(Ds,Wid) and not (Ds>Wid)) or (En!=1) or (Clk!=1) or (Rst!=1):
        logs.log_error('FLIPFLOP %s %s wid=%d qs=%d ds=%d' % (Obj.Type,Obj.Name,Wid,Qs,Ds))
        return 0
    else:
        return 1


def checkShiftsLit(Obj,Mod):
    return 1


def checkShifts(Obj,Mod):
    Wid = Obj.params['WID']
    As,Bs,Xs = 0,0,0
    for Pin in Obj.conns:
        Sig = Obj.conns[Pin]
        if Pin[0] == 'a': As += 1
        elif Pin[0] == 'b': Bs += 1
        elif Pin[0] == 'x': Xs += 1

    if Obj.Type == 'shiftright':
        if (As>Wid) and (Xs == Wid):
            Obj.params['WID'] = As
            expandCons(Obj,'a','x','')
            return 1
    if (As != Wid) or (Xs != Wid):
        logs.log_error('SHIFTER %s %s wid=%d xs=%d as=%d bs=%d' % (Obj.Type,Obj.Name,Wid,Xs,As,Bs))
        return 0
    else:
        return 1

def expandCons(Obj,From,To,What = ''):
    Pins = list(Obj.conns.keys())
    for Pin in Pins:
        if Pin.startswith(From):
            Ind = Pin[len(From):]
            Tpin = To+Ind
            if Tpin not in Obj.conns:
                Obj.conns[Tpin] = What



def checkSimple(Obj,Mod):
    Type = Obj.Type
    Inst = Obj.Name
    Len = len(list(Obj.conns.keys()))
    Bads = 0
    if  (Len==2):
        if Type not in ['bufx','inv']:
            logs.log_error('checkSimple of %s failed on %s' % (Type,Inst,list(Obj.conns.keys())))
            Bads += 1
    for Pin in Obj.conns:
        if (Pin != 'x'):
            Sig = Obj.conns[Pin]
            List  = Mod.netTable[Sig]
            if len(List) < 2:
                logs.log_error('checkSimple input pin %s / %s  is not driven in %s / %s' % (Pin,Sig,Type,Inst))
                Bads += 1
    if Bads>0: return 0        
    return 1
    
def preprocess(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Prm in Obj.params:
            Val0 = Obj.params[Prm]
            if type(Val0) is int:
                Val = Val0
            elif type(Val0) is str:
                Val  = eval(Val0,Mod.parameters,Mod.localparams)
            elif type(Val0) is list:
                Valx = Mod.pr_expr(Val0)
                Val  = eval(Valx,Mod.parameters,Mod.localparams)
            
            Obj.params[Prm] = Val
            if "__builtins__" in Mod.parameters.keys(): Mod.parameters.pop("__builtins__")
            if "__builtins__" in Mod.localparams.keys(): Mod.localparams.pop("__builtins__")
    for Ind,(Dst,Src,A,B) in enumerate(Mod.hard_assigns):
        Dst = rework(Dst,Mod)
        Src = rework(Src,Mod)
        Mod.hard_assigns[Ind] = (Dst,Src,A,B)
    for ind,Alw in enumerate(Mod.alwayses):
        Body = Alw[1]
        if (len(Body) == 2) and (Body[0] == 'list'): Body = Body[1]
        Body2 = []
        for Item in Body:
            A1 = scanDeepRework(Item,Mod)
            Body2.append(A1)
        Mod.alwayses[ind] = [Alw[0],Body2,Alw[2]]

def scanDeepRework(Body,Mod):
    return rework(Body,Mod)
REWORKDONES = {}
def rework(Expr,Mod):
    if type(Expr) is str: return Expr
    if type(Expr) is int: return Expr
    if type(Expr) is list:
        if Expr[0] == 'subbit':
            Bus = Expr[1]
            Ind = Expr[2]
            if type(Ind) is list:
                if Ind[0] == 'subbus':
                    Wid = Mod.exprWidth(Ind)
                    New = '%s_%s_%s' % (Ind[1],Ind[2][0],Ind[2][1])
                    if New in REWORKDONES:
                        return ['subbit',Bus,New]
                    Mod.add_sig(New,'wire',Wid) 
                    Mod.hard_assigns.append((New,Ind,'',''))
                    REWORKDONES[New] = Ind
                    return ['subbit',Bus,New]
                else:
                    return Expr
            else:
                return Expr
        else:
            Res = []
            for Item in Expr:
                Rep = rework(Item,Mod)
                Res.append(Rep)
            return Res
    elif type(Expr) is tuple:
        Res = []
        for Item in Expr:
            Rep = rework(Item,Mod)
            Res.append(Rep)
        return tuple(Res)

    logs.log_error("rework %s" % str(Expr))
    return Expr


