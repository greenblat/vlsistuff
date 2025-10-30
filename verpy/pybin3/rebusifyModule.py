

from synthesis0 import BRICKS
import logs

def help_main(Env):
    Mod = Env.Current

    busifyNets(Mod)


    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type in BRICKS:
            workOnObj(Mod,Obj)
        else:
            workOnObj(Mod,Obj)
    Insts = list(Mod.insts.keys()) 
    for Inst in Insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == 'mflipflop':
            Ports = Obj.params['PORTS']
            if Ports>1:
                redoFlop(Mod,Obj)
            else:
                Obj.conns['en'] = Obj.conns.pop('en0')
                Obj.conns['d'] = Obj.conns.pop('d0')



    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            if (type(Sig) is list) and (Sig[0] == 'curly'):
                Sig0 = gatherGnds(Sig)
                Obj.conns[Pin] = Sig0

    Fout = open('%s.busv' % Mod.Module,'w')
    Mod.dump_verilog(Fout)
    Fout.close()

def gatherGnds(Sig):
    if ('gnd' not in Sig) and ('vcc' not in Sig): return Sig
    Sig0 = Sig[:]
    Num = 0
    St = -1
    Wid = 0
    for ind,X in enumerate(Sig0):
        if (X in ['vcc','gnd']) and (St<0): St = ind
        if X == 'vcc':
            Num = 2*Num+1
            Wid += 1
        elif X == 'gnd':
            Num = 2*Num
            Wid += 1
        elif (St>0) and (ind>St):
            Bef = Sig0[:St]
            Aft = Sig0[ind:]
            Const = "%d'h%x" % (Wid,Num)
#            if Wid == 1:
#                if Num == 0: Const = 'gnd'
#                if Num == 1: Const = 'vcc'
            Res = Bef + [Const  ] + Aft
            if len(Res) == 2: return Const
            return gatherGnds(Res)
    if St>0:
        Bef = Sig0[:St]
        Aft = Sig0[ind+1:]
        Const = "%d'h%x" % (Wid,Num)
        Res = Bef + [Const  ] + Aft
        if len(Res) == 2: return Const
        return Res
        
    return Sig



def redoFlop(Mod,Obj):
    Pairs = []
    Rms = []
    Ens = []
    for II in range(Obj.params['PORTS']):
        En = Obj.conns['en%s' % II]
        Di = Obj.conns['d%s' % II]
        Pairs.append((En,Di))
        Rms.append('en%s' % II)
        Rms.append('d%s' % II)
        Pp = chr( ord('a') + II)
        Ens.append( (Pp,En))
    Out = Mod.add_sig('','wire',1)
    Or = Mod.add_inst_conns('or%s' % len(Ens),'',Ens)
    Or.conns['x'] = Out
    Obj.conns['en'] = Out
    Pins = list(Obj.conns.keys())
    for Rm in Rms: Obj.conns.pop(Rm)
    Wid = Obj.params['WID']
    while len(Pairs)>1:
        (En0,Di0) = Pairs.pop(0)
        (En1,Di1) = Pairs.pop(0)
        Out = Mod.add_sig('','wire',Wid)
        Mux2 = Mod.add_inst_conns('mux2','',[('x',Out),('sel',En0),('yes',Di0),('no',Di1)])
        Mux2.params['WID'] = Wid
        Mux2.params['YWID'] = Wid
        Mux2.params['NWID'] = Wid

        Enx = Mod.add_sig('','wire',1)
        Orx = Mod.add_inst_conns('or2','',[('a',En0),('b',En1),('x',Enx)])
        Pairs.append((Enx,Out))
    
    Obj.conns['d'] = Out

    
    



def workOnObj(Mod,Obj):
    Pins = {}
    for Pin in Obj.conns:
        Sig = Obj.conns[Pin]
        if not Sig:
            pass
        elif bussed(Sig):
            Bus,Ind = bussed(Sig)
            Sig = ['subbit',Bus,Ind]
            Obj.conns[Pin] = Sig
        if bussed(Pin) and Sig:
            Bus,Ind = bussed(Pin)
            if Bus not in Pins: Pins[Bus] = []
            Pins[Bus].append( (Ind,Sig) )
    for Bus in Pins:
        Pins[Bus].sort()
        Pins[Bus].reverse()
        LL = ['curly']
        for _,Sig in Pins[Bus]:
            LL.append(Sig)
        Obj.conns[Bus] = LL
    Opins = list(Obj.conns.keys())
    for Pin in Opins:
        if bussed(Pin):
            Bus,Ind = bussed(Pin)
            if Bus in Obj.conns:
                Obj.conns.pop(Pin)
        


def busifyNets(Mod):
    Busses = {}
    Dirs = {}
    for Net in Mod.nets:
        if bussed(Net):
            Bus,Ind = bussed(Net)
            Dir,_ = Mod.nets[Net]
            Dirs[Bus] = Dir
            if Bus not in Busses: Busses[Bus] = []
            if Ind not in Busses[Bus]:
                Busses[Bus].append(Ind)
    for Bus in Busses:
        LL = Busses[Bus]
        LL.sort()
        Low = LL[0]
        High = LL[-1]
        Mod.nets[Bus] = Dirs[Bus],(High,Low)

    Nets = list(Mod.nets.keys())
    for Net in Nets:
        if bussed(Net):
            Bus,Ind = bussed(Net)
            if Bus in Dirs: 
                Mod.nets.pop(Net)

        


            
def bussed(Net):
    ww = Net.split('_')
    if (len(ww)>=3) and (ww[-1] == ''):
        Bus = '_'.join(ww[:-2])
        Ind = eval(ww[-2])
        return Bus,Ind
    return False


AA = ['curly','aa','gnd']
print(AA,gatherGnds(AA))

AA = ['curly','gnd','aa','gnd']
print(AA,gatherGnds(AA))


