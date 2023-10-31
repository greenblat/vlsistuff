
import os


import logs
from module_class import pr_expr

def help_main(Env):
    Mod = Env.Current
#    Fout = open('yyy.v','w')
#    Mod.dump_verilog(Fout)
#    Fout.close()
#
    dealAssigns(Mod)
#    Fout = open('xxx.v','w')
#    Mod.dump_verilog(Fout)
#    Fout.close()
#    return
    explodeBusses(Mod)
    normalizeConns(Mod)
    normalizeInsts(Mod)
    for Net in list(Mod.nets.keys()):
        Dir,Wid = Mod.nets[Net]
        Netn = normalize(Net)
        Mod.nets[Netn] = Dir,(63,0)
        if Netn != Net:
            Mod.nets.pop(Net)
    addDebugNets(Mod)
    if os.path.exists('interconnects.py'):
        from interconnects import INTERCONNECTS
        DBOX = 0
        SDF = 0
        for Sinst,Spin,Dinst,Dpin,Dly0,Dly1 in INTERCONNECTS:
            if (Dly0>0)or(Dly1>0)and (Dpin != 'output'):
                Mod.add_inst('dbox','dbox_%d' % DBOX)
                if Spin == 'input':
                    Mod.add_conn('dbox_%d' % DBOX,'inx',Sinst)
                else:
                    Sig = Mod.insts[Sinst].conns[Spin]
                    Mod.add_conn('dbox_%d' % DBOX,'inx',Sig)

                Sig = Mod.insts[Dinst].conns[Dpin]
                Sig_aft = 'sdf_'+str(SDF)+'_'+Sig
                SDF += 1
                Mod.add_conn('dbox_%d' % DBOX,'outx',Sig_aft)
                Mod.insts[Dinst].conns[Dpin] = Sig_aft
                Mod.nets[Sig_aft] = ['wire',(63,0)]

                Mod.insts['dbox_%d' % DBOX].add_param('dly0',Dly0)
                Mod.insts['dbox_%d' % DBOX].add_param('dly1',Dly1)

                DBOX += 1

    Fout = open('%s.sdfv' % Mod.Module,"w")
    Mod.dump_verilog(Fout)
    Fout.close()

def addDebugNets(Mod):
    for Net in list(Mod.nets.keys()):
        Dir,Wid = Mod.nets[Net]
        if Wid == (63,0):
            New = 'dbg_%s' % Net
            Mod.nets[New] = 'wire',0
            Mod.hard_assigns.append((New,['subbit',Net,0],False,False))

def explodeBus(Sig,Mod):
    if Sig in [0,1,'0','1']:
        return [int(Sig)]
    if (type(Sig) is str) and (Sig in Mod.nets):
        _,Wid = Mod.nets[Sig]
        if (type(Wid) is tuple) and (len(Wid) ==2):
            Hi = int(Wid[0])
            Lo = int(Wid[1])
            return explodeBus(['subbus',normalize(Sig),Hi,Lo],Mod)
    elif (type(Sig) is str) and (Sig[0] in '123456789'):
        if "'" in Sig:
            ww = Sig.split("'")
            Wid = int(ww[0])
            Val0 = ww[1][1:]
            if 'x' in Val0: Val = 0
            elif ww[1][0] == 'h': Val = int(ww[1][1:],16)
            elif ww[1][0] == 'd': Val = int(ww[1][1:],10)
            elif ww[1][0] == 'b': Val = int(ww[1][1:],2)
            Seq = list(logs.binx(Val,Wid))
            return Seq
        return [Sig]
    elif (type(Sig) is list) and (Sig[0] == 'subbit'):
        Sigx = '%s_%s_' % (normalize(Sig[1]),Sig[2])
        return [Sigx] 
    elif (type(Sig) is list) and (Sig[0] == 'subbus'):
        if len(Sig)==3:
            Hi = int(Sig[2][0])
            Lo = int(Sig[2][1])
        else:
            Hi = int(Sig[2])
            Lo = int(Sig[3])
        Res = []
        for Ind in range(Hi,Lo-1,-1):
            Res.append('%s_%s_' % (normalize(Sig[1]),Ind))
        return Res
    elif (type(Sig) is list) and (Sig[0] == 'curly'):
        Res = []
        for Item in Sig[1:]:
            Part = explodeBus(Item,Mod)
            Res.extend(Part)
        return Res
    if (type(Sig) is str):
        Sig1 = normalize(Sig)
        return [Sig1]
    else:
        logs.log_error('explodeBus got "%s" in %s ' % (Sig,Mod.Module))
        return [Sig]
    

def dealAssigns(Mod):
    Ind = 0
    Limit = len(Mod.hard_assigns)
    Adds = []
    while Ind < len(Mod.hard_assigns):
        Dst,Src,X,Y = Mod.hard_assigns[Ind]
        Dseq = explodeBus(Dst,Mod)
        Sseq = explodeBus(Src,Mod)
        if '0' in Dseq:
            print("OOOOOOOOOOOO",Dst)
        elif (len(Dseq) == 1) and (len(Sseq) == 1):
            if Dseq[0] != Sseq[0]:
                Mod.hard_assigns[Ind] = Dseq[0],Sseq[0],X,Y
        elif (len(Dseq)  == len(Sseq)):
            Mod.hard_assigns.pop(Ind)
            Ind -= 1
            for ind,D in enumerate(Dseq):
                S = Sseq[ind]
                Adds.append((D,S,X,Y))
        else:
            Mod.hard_assigns.pop(Ind)
            Ind -= 1
            for ind,D in enumerate(Dseq):
                if len(Sseq)>ind:
                    S = Sseq[ind]
                else:
                    S = 0
                if D != '0':
                    Adds.append((D,S,X,Y))
        Ind +=1
    for iiii,XX in enumerate(Adds):
        print(iiii,XX)
    Mod.hard_assigns.extend(Adds)


def normalizeInsts(Mod):
    for Inst in list(Mod.insts.keys()):
        Obj = Mod.insts[Inst]
        Inst0 = normalize(Inst)
        if Inst0 != Inst:
            Mod.insts[Inst0] = Obj
            Obj.Name = Inst0
            Mod.insts.pop(Inst)
        


def normalizeConns(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            Sigs = Mod.pr_expr(Sig)
            Sign = normalize(Sigs)
            Obj.conns[Pin] = Sign
            if (Sign not in Mod.nets)and(Sign[0] not in '0123456789'):
                Mod.nets[Sign] = 'wire',0



def explodeBusses(Mod):
    for Net in list(Mod.nets.keys()):
        Dir,Wid = Mod.nets[Net]
        if type(Wid) is tuple:
            Hi,Lo = Wid
            for II in range(int(Lo),int(Hi)+1):
                New = '%s[%s]' % (Net,II)
                New = normalize(New)
                Mod.nets[New] = Dir,0
            Mod.nets.pop(Net) 
    
def normalize(Str):
    if type(Str) is list:
        Str = pr_expr(Str)
        return normalize(Str)

    Str = Str.replace(' ','')
    for Chr in "[]().":
        Str = Str.replace(Chr,'_')

    if Str[0] == '\\':
        Str = Str[1:]
    if Str[0] == '1':
        return "64'h"+Str[-1]
    return Str



