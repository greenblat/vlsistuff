

def dumpMod(Mod,Fname):
    Ftmp = open('%s.v' % Fname,'w')
    Mod.dump_verilog(Ftmp)
    Ftmp.close()

def createNewRtl(Mod):
    dumpMod(Mod,'xxx0')
    runNewRtl(Mod)
    dumpMod(Mod,'xxx1')

def runNewRtl(Mod):
    Insts = list(Mod.insts.keys())
    for Inst in Insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        if 'delay' in Obj.params:
            Dly = Obj.params['delay']
            Dly = [(Dly,Dly)]
        else:
            Dly = ''
        if Type.startswith('nand'):
            O,Ins  = typicalConns(Obj.conns,'&')
            Mod.hard_assigns.append((O,('~',Ins),'',Dly))
            Mod.insts.pop(Inst)
        elif Type.startswith('and'):
            O,Ins  = typicalConns(Obj.conns,'&')
            Mod.hard_assigns.append((O,Ins,'',Dly))
            Mod.insts.pop(Inst)
        elif Type.startswith('nor'):
            O,Ins  = typicalConns(Obj.conns,'|')
            Mod.hard_assigns.append((O,('~',Ins,'',Dly)))
            Mod.insts.pop(Inst)
        elif Type.startswith('or'):
            O,Ins  = typicalConns(Obj.conns,'|')
            Mod.hard_assigns.append((O,Ins,'',Dly))
            Mod.insts.pop(Inst)
        elif Type.startswith('xor'):
            O,Ins  = typicalConns(Obj.conns,'^')
            Mod.hard_assigns.append((O,Ins,'',Dly))
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
            Mod.insts.pop(Inst)
        elif Type == 'flop':
            ensureExists(Obj,Inst,'ck d q')
            Ck = Obj.conns['ck']
            D = Obj.conns['d']
            Q = Obj.conns['q']
        elif Type == 'dffr':
            ensureExists(Obj,Inst,'ck d q rn')
            Ck = Obj.conns['ck']
            D = Obj.conns['d']
            Q = Obj.conns['q']
            RN = Obj.conns['rn']
        elif Type == 'dffs':
            ensureExists(Obj,Inst,'ck d q sn')
            Ck = Obj.conns['ck']
            D = Obj.conns['d']
            Q = Obj.conns['q']
            SN = Obj.conns['sn']
        elif Type == 'mux2':
            ensureExists(Obj,Inst,'i0 i1 s o')
            i0 = Obj.conns['i0']
            i1 = Obj.conns['i1']
            s = Obj.conns['s']
            o = Obj.conns['o']
            Mod.hard_assigns.append((O,('question',s,i1,i0),'',Dly))
            Mod.insts.pop(Inst)
        elif list(Obj.conns.keys()) != []:
            pass
        else:
           print('warning! %s ignored for rtl verilog %s %s' % (Type,Inst,Obj.conns)) 



def ensureExists(Obj,Inst,Pins):
    Pins = Pins.split()
    for Pin in Pins:
        if Pin not in Obj.conns:
            Obj.conns[Pin] = '0' 
            logs.log_info('ensurePinExists %s / %s  is missing %s pin connection' % (Inst,Obj.Type,Pin))


def typicalConns(Conns,Op):
    Ins = ['','','','','','','','','','']
    O = ''
    for Pin in Conns.keys():
        if Pin[0] == 'o':
            O = Conns[Pin]
        elif Pin[0] == 'i':
            Ind = int(Pin[1:])
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




