
import logs
def dumpMod(Mod,Fname):
    Ftmp = open('%s.v' % Fname,'w')
    Mod.dump_verilog(Ftmp)
    Ftmp.close()

def createNewRtl(Mod):
#    dumpMod(Mod,'xxx0')
    runNewRtl(Mod)
    runInstances(Mod)
#    dumpMod(Mod,'xxx1')

def runInstances(Mod):
    Insts = list(Mod.insts.keys())
    for Inst in Insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        Params = Obj.params
        if 'type' in Params:
            Obj.Type = Params['type']
            Obj.params.pop('type')

def runNewRtl(Mod):
    Insts = list(Mod.insts.keys())
    Alwayses0 = {}
    Alwayses1 = {}
    Alwayses2 = {}
    for Inst in Insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        if 'delay' in Obj.params:
            Dly = Obj.params['delay']
            Dly = [(Dly,Dly)]
        else:
            Dly = ''

        if Type.startswith('nandi'):
            O,Ins  = typicalConns(Obj.conns,'&',True)
            Mod.hard_assigns.append((O,('~',Ins),'',Dly))
            Mod.insts.pop(Inst)
        elif Type.startswith('andi'):
            O,Ins  = typicalConns(Obj.conns,'&',True)
            Mod.hard_assigns.append((O,Ins,'',Dly))
            Mod.insts.pop(Inst)
        elif Type.startswith('nand'):
            O,Ins  = typicalConns(Obj.conns,'&')
            Mod.hard_assigns.append((O,('~',Ins),'',Dly))
            Mod.insts.pop(Inst)
        elif Type.startswith('and'):
            O,Ins  = typicalConns(Obj.conns,'&')
            Mod.hard_assigns.append((O,Ins,'',Dly))
            Mod.insts.pop(Inst)
        elif Type.startswith('nor'):
            O,Ins  = typicalConns(Obj.conns,'|')
            Mod.hard_assigns.append((O,('~',Ins),'',Dly))
            Mod.insts.pop(Inst)
        elif Type.startswith('or'):
            O,Ins  = typicalConns(Obj.conns,'|')
            Mod.hard_assigns.append((O,Ins,'',Dly))
            Mod.insts.pop(Inst)
        elif Type.startswith('xor'):
            O,Ins  = typicalConns(Obj.conns,'^')
            Mod.hard_assigns.append((O,Ins,'',Dly))
            Mod.insts.pop(Inst)
        elif Type.startswith('less'):
            O,Ins  = typicalConns(Obj.conns,'^')
            Mod.hard_assigns.append((O,('<',Ins[1],Ins[2]),'',Dly))
            Mod.insts.pop(Inst)
        elif Type.startswith('more'):
            O,Ins  = typicalConns(Obj.conns,'^')
            Mod.hard_assigns.append((O,('>',Ins[1],Ins[2]),'',Dly))
            Mod.insts.pop(Inst)
        elif Type.startswith('xnor'):
            O,Ins  = typicalConns(Obj.conns,'^')
            Mod.hard_assigns.append((O,('~',Ins),'',Dly))
            Mod.insts.pop(Inst)
        elif Type.startswith('inv'):
            O,Ins  = typicalConns(Obj.conns,'&')
            Mod.hard_assigns.append((O,('~',Ins),'',Dly))
            Mod.insts.pop(Inst)
        elif Type.startswith('buf'):
            O,Ins  = typicalConns(Obj.conns,'&')
            Mod.hard_assigns.append((O,Ins,'',Dly))
            equalizeWidth(Mod,O,Ins[0])
            Mod.insts.pop(Inst)
        elif Type == 'mux2':
            ensureExists(Obj,Inst,'i0 i1 s o')
            i0 = Obj.conns['i0']
            i1 = Obj.conns['i1']
            s = Obj.conns['s']
            O = Obj.conns['o']
            Mod.hard_assigns.append((O,('question',s,i1,i0),'',Dly))
            Mod.insts.pop(Inst)
        elif Type == 'mux4':
            ensureExists(Obj,Inst,'i0 i1 i2 i3 s0 s1 o')
            i0 = Obj.conns['i0']
            i1 = Obj.conns['i1']
            i2 = Obj.conns['i2']
            i3 = Obj.conns['i3']
            s0 = Obj.conns['s0']
            s1 = Obj.conns['s1']
            O = Obj.conns['o']
            Mod.hard_assigns.append((O,('question',s1,('question',s0,i3,i2),('question',s0,i1,i0)),'',Dly))
            Mod.insts.pop(Inst)

        elif Type == 'flop':
            ensureExists(Obj,Inst,'ck d q')
            Ck = Obj.conns['ck']
            D = Obj.conns['d']
            Q = Obj.conns['q']
            Mod.add_net(Q,'reg',0)
            if Ck not in Alwayses0: Alwayses0[Ck] = []
            Alwayses0[Ck].append((Q,D)) 
            equalizeWidth(Mod,Q,D)
            Mod.insts.pop(Inst)

        elif Type == 'dffr':
            ensureExists(Obj,Inst,'ck d q rn')
            Ck = Obj.conns['ck']
            D = Obj.conns['d']
            Q = Obj.conns['q']
            RN = Obj.conns['rn']
            Mod.add_net(Q,'reg',0)
            if 'qn' in Obj.conns:
                QN = Obj.conns['qn']
                if (QN != ''):
                    Mod.add_net(QN,'wire',0)
                    Mod.hard_assigns.append((QN,['~',Q],'',''))
                
            if (Ck,RN) not in Alwayses1: Alwayses1[(Ck,RN)] = []
            Alwayses1[(Ck,RN)].append((Q,D,0)) 
            equalizeWidth(Mod,Q,D)

            if ('qn' in Obj.conns)and(QN != ''):
                equalizeWidth(Mod,QN,D)
            Mod.insts.pop(Inst)
        elif Type == 'dffs':
            ensureExists(Obj,Inst,'ck d q sn')
            Ck = Obj.conns['ck']
            D = Obj.conns['d']
            Q = Obj.conns['q']
            SN = Obj.conns['sn']
            Mod.add_net(Q,'reg',0)
            if (Ck,SN) not in Alwayses1: Alwayses1[(Ck,SN)] = []
            Alwayses1[(Ck,SN)].append((Q,D,1)) 
            if 'qn' in Obj.conns:
                QN = Obj.conns['qn']
                if (QN != ''):
                    Mod.add_net(QN,'wire',0)
                    Mod.hard_assigns.append((QN,['~',Q],'',''))
            equalizeWidth(Mod,Q,D)
            if ('qn' in Obj.conns) and (QN != ''):
                equalizeWidth(Mod,QN,D)
            Mod.insts.pop(Inst)
        elif list(Obj.conns.keys()) != []:
            pass
        else:
           logs.log_warning('%s ignored for rtl verilog %s %s' % (Type,Inst,Obj.conns)) 
    for Ck in Alwayses0:
        List = Alwayses0[Ck]
        List2 = ['list']
        for Q,D in List:
            List2.append(('<=',Q,D))
        Mod.alwayses.append((('edge','posedge',Ck),List2,'always'))
    for Ck,RN in Alwayses1:
        List = Alwayses1[(Ck,RN)]
        List2 = ['list']
        for Q,D,_ in List:
            List2.append(('<=',Q,D))
        ListRst = ['list']
        for Q,_,Df in List:
            ListRst.append(('<=',Q,Df))
        Mod.alwayses.append((('list',('edge','posedge',Ck),('edge','negedge',RN)),['ifelse',('!',RN),ListRst,List2],'always'))

def equalizeWidth(Mod,NetA,NetB):
    if (type(NetA) is str) and (type(NetB) is str):
        return

    if (type(NetA) is list) and (type(NetB) is str):
        if NetA[0] == 'subbus':
            Wid = eval(NetA[2])-eval(NetA[3])+1
            Mod.add_sig(NetB,'wire',(Wid-1,0))
            return
        if NetA[0] == 'subbit':
            return
    if (type(NetA) is str) and (type(NetB) is list):
        equalizeWidth(Mod,NetB,NetA)
        return

    if (type(NetA) is list) and (type(NetB) is list):
        if (NetA[0] == 'subbus') and (NetB[0] == 'subbus'):
            return

    logs.log_error('failed equalizeWidth %s %s' % (NetA,NetB))

def ensureExists(Obj,Inst,Pins):
    Pins = Pins.split()
    for Pin in Pins:
        if Pin not in Obj.conns:
            Obj.conns[Pin] = '0' 
            logs.log_info('ensurePinExists %s / %s  is missing %s pin connection' % (Inst,Obj.Type,Pin))


def typicalConns(Conns,Op,I1inv = False):
    Ins = ['','','','','','','','','','']
    O = ''
    for Pin in Conns.keys():
        if Pin[0] == 'o':
            O = Conns[Pin]
        elif Pin[0] == 'i':
            Ind = int(Pin[1:])
            if I1inv and (Ind == 1):
                Ins[Ind]  = ('~',Conns[Pin])
            else:
                Ins[Ind]  = Conns[Pin]
    Ins2 = [Op]
    for In in Ins:
        if In == 'vcc':
            Ins2.append('1')
        elif In == 'gnd':
            Ins2.append('0')
        elif In != '': 
            Ins2.append(In)
    if len(Ins2) == 2:
        Ins2 = Ins2[1:]
    return O,Ins2




