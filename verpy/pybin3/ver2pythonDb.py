'''
takes verilog soft gatelevel synthesis results and creates python class ready to be used in ML travels

'''

import logs
import inspect
import json
import yaml

HEADER = '''
class MODClass:
    def __init__(self):
        self.Name = "MOD"
'''

class moduleClass:
    def __init__(self,Name):
        self.Name = Name
        self.netdirs = {}
        self.netwids = {}
        self.wires = {}
        self.insts = {}
        self.bufs = []
        self.libtypes0 = {}
        self.libtypes1 = {}
        self.types0 = {}
        self.types1 = {}

def help_main(Env):
    if type(Env.Current) is None:
        logs.log_error('ver2pythonDb got non type')
        return
    Mod = Env.Current
    exploadConns(Mod)
    removeParams(Mod)
    dumpV(Mod,'builds/%s.build' % Mod.Module)
    Build = createBuild(Mod)
    dumpPython(Build,Mod)
    dumpYaml(Build,Mod)
    dumpJson(Build,Mod)

def removeParams(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Obj.params = {}
def dumpJson(Build,Mod):
    Fout = open('%s.json' % Mod.Module,'w')
    json.dump(Build.__dict__,Fout,indent=4)
    Fout.close()
    return

#     Fout.write('\ntypes0 =')
#     json.dump(Build.types0,Fout,indent=4)
#     Fout.write('\ntypes1 =')
#     json.dump(Build.types1,Fout,indent=4)
#     Fout.write('\nnetwids =')
#     json.dump(Build.netwids,Fout,indent=4)
#     Fout.write('\nnetdirs =')
#     json.dump(Build.netdirs,Fout,indent=4)
#     Fout.write('\ninsts = ')
#     json.dump(Build.insts,Fout,indent=4)
#     Fout.close()

def dumpYaml(Build,Mod):
    Fout = open('%s.yaml' % Mod.Module,'w')
    yaml.dump(Build,Fout)
    Fout.close()

def dumpPython(Build,Mod):
    Fout = open('%s.py' % Mod.Module,'w')
    Fout.write(HEADER.replace('MOD',Mod.Module))

    Fout.write('        self.types0 = {\n')
    Pref = ' '
    for Inst in Build.types0:
        Type =  Build.types0[Inst]
        Fout.write('           %s"%s":"%s"\n' % (Pref,Inst,Type))
        Pref = ','
    Fout.write('        }\n')

    Fout.write('        self.types1 = {\n')
    Pref = ' '
    for Type in Build.types1:
        List =  Build.types1[Type]
        Fout.write('           %s"%s" : %s\n' % (Pref,Type,repr(List)))
        Pref = ','
    Fout.write('        }\n')

    Fout.write('        self.libtypes0 = {\n')
    Pref = ' '
    for Inst in Build.libtypes0:
        Type =  Build.libtypes0[Inst]
        Fout.write('           %s"%s":"%s"\n' % (Pref,Inst,Type))
        Pref = ','
    Fout.write('        }\n')

    Fout.write('        self.libtypes1 = {\n')
    Pref = ' '
    for Type in Build.libtypes1:
        List =  Build.libtypes1[Type]
        Fout.write('           %s"%s" : %s\n' % (Pref,Type,repr(List)))
        Pref = ','
    Fout.write('        }\n')



    Fout.write('        self.netwids = {\n')
    Pref = ' '
    for Net in Build.netwids:
        Wid =  Build.netwids[Net]
        Fout.write('           %s"%s" : %s\n' % (Pref,Net,Wid))
        Pref = ','
    Fout.write('        }\n')

    Fout.write('        self.netdirs = {\n')
    Pref = ' '
    for Net in Build.netdirs:
        Dir =  Build.netdirs[Net]
        Fout.write('           %s"%s" : "%s"\n' % (Pref,Net,Dir))
        Pref = ','
    Fout.write('        }\n')

    Fout.write('        self.wires = {\n')
    Pref = ' '
    for Net in Build.wires:
        Wid =  Build.wires[Net]
        Fout.write('           %s"%s" : "%s"\n' % (Pref,Net,Wid))
        Pref = ','
    Fout.write('        }\n')


    Fout.write('        self.conns = {\n')
    Pref = ' '
    for Inst in Build.insts:
        Conns =  Build.insts[Inst]
        Exp = explodeConns(Conns)
        Fout.write('           %s"%s" : %s\n' % (Pref,Inst,repr(Conns)))
        Pref = ','
    Fout.write('        }\n')

    Fout.close()


#    source_code = inspect.getsource(Build)
#    Fout.write(source_code)

def explodeConns(Conns):
    Res = {}
    for Pin in Conns:
        Sig = Conns[Pin]
        if type(Sig) is str: 
            if ',' in Sig:
                print('>>>>> %s' % (Sig))
            elif ':' in Sig:
                print('>>>>> %s' % (Sig))
            else:
                Res[Pin] = Sig
        elif type(Sig) is int:
            Res[Pin] = Sig
        elif type(Sig) is list: 
            if Sig[0] == 'curly':
                print('>>>>> %s' % (Sig))
    return Res                

def createBuild(Mod):
    Build = moduleClass(Mod.Module)
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        Width = getWid(Wid)
        if isSynWire(Net):
            Build.wires[Net] = Width
        else:
            Build.netdirs[Net] = Dir
            Build.netwids[Net] = Width
        
    for Inst in Mod.insts:
        Type = Mod.insts[Inst].Type
        if libType(Type):
            Build.libtypes0[Inst] = Type
            if Type  not in Build.libtypes1: Build.libtypes1[Type] = []
            Build.libtypes1[Type].append(Inst)
            Build.insts[Inst] = {}
            for Pin in Mod.insts[Inst].conns:
                Sig = Mod.insts[Inst].conns[Pin]
                if type(Sig) is str:
                    Build.insts[Inst][Pin] = Sig
                elif type(Sig) is int:
                    Build.insts[Inst][Pin] = Sig
                elif Sig[0] in ['subbit']:
                    Build.insts[Inst][Pin] = Mod.pr_expr(Sig)
                elif Sig[0] in ['subbus']:
                    print(">>>>>>SUBBUS",Pin,Sig)
                elif Sig[0] in ['curly']:
                    print(">>>>>>CURLY",Pin,Sig)
        else:
            Build.types0[Inst] = Type
            if Type  not in Build.types1: Build.types1[Type] = []
            Build.types1[Type].append(Inst)
            Build.insts[Inst] = {}
            for Pin in Mod.insts[Inst].conns:
                Sig = Mod.insts[Inst].conns[Pin]
                Sig1 = Mod.pr_expr(Sig)
                Build.insts[Inst][Pin] = Sig1

#        Build.insts[Inst] = Mod.insts[Inst].conns
    return Build


def getWid(Wid):
    if Wid == 0: return 1
    if type(Wid) is int: return Wid
    if type(Wid) is list:
        if len(Wid) == 2:
            if (type(Wid[0]) is int) and (type(Wid[1]) is int):
                return Wid[0]-Wid[1]+1
            try:
                Hi = int(Wid[0])
                Lo = int(Wid[1])
                return Hi-Lo
            except:
                return ('+',Wid[0],1)
    if type(Wid) is tuple:
        if len(Wid) == 2:
            if (type(Wid[0]) is int) and (type(Wid[1]) is int):
                return Wid[0]-Wid[1]+1
            try:
                Hi = int(Wid[0])
                Lo = int(Wid[1])
                return Hi-Lo
            except:
                return ('+',Wid[0],1)


    logs.log_error('getWid got "%s"' % (str(Wid)))

    return 1

def isSynWire(Net):
    if type(Net) is not str: return False
    return  (Net[0] == '_')
        
def libType(Type):
    return (Type == 'BUF') or Type.startswith('scs130ms_') or Type.endswith('20P96CPD')

def explodeBus(Sig,Mod):
    if Sig in [0,1,'0','1']:
        return [int(Sig)]
    if (type(Sig) is str) and (Sig in Mod.nets):
        _,Wid = Mod.nets[Sig]
        if (type(Wid) is tuple) and (len(Wid) ==2):
            Hi = int(Wid[0])
            Lo = int(Wid[1])
            return explodeBus(['subbus',normalize(Sig),Hi,Lo],Mod)
        elif (Wid == 0):
            pass
        else:
            logs.log_error("explodeBus got %s  %s" % (Sig,Wid))  
           
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
        Sigx = '%s[%s]' % (normalize(Sig[1]),Sig[2])
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
            Res.append('%s[%s]' % (normalize(Sig[1]),Ind))
        return Res
    elif (type(Sig) is list) and (Sig[0] == 'curly'):
        Res = []
        for Item in Sig[1:]:
            Part = explodeBus(Item,Mod)
            Res.extend(Part)
        return Res
    elif (type(Sig) is list) and (Sig[0] == 'hex'):
        if Sig[2][0] == 'x':
            if str(Sig[1]) == '1': return 'gnd'
            if type(Sig[2]) is str:
                Res = []
                for ii in range(len(Sig[2])):
                    Res.append('gnd')
                return Res
            logs.log_error("XXXXXXXXXX %s %s" % (Sig[2],Sig))
    elif (type(Sig) is list) and (Sig[0] == 'bin'):
        if Sig[1] in ['1',1]:
            if str(Sig[2]) == '1': return ['vcc']
            if str(Sig[2]) == '0': return ['gnd']
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
                Adds.append((Mod.pr_expr(D),Mod.pr_expr(S),X,Y))
        else:
            Mod.hard_assigns.pop(Ind)
            Ind -= 1
            for ind,D in enumerate(Dseq):
                if len(Sseq)>ind:
                    S = Sseq[ind]
                else:
                    S = 0
                if D != '0':
                    Adds.append((Mod.pr_expr(D),Mod.pr_expr(S),X,Y))
        Ind +=1
    Mod.hard_assigns.extend(Adds)


def explodeBusses(Mod):
    for Net in list(Mod.nets.keys()):
        Dir,Wid = Mod.nets[Net]
        if (type(Wid) is tuple) or (type(Wid) is list):
            Hi,Lo = Wid
            Hi = Mod.compute_int(Hi)
            Lo = Mod.compute_int(Lo)
            for II in range(int(Lo),int(Hi)+1):
                New = '%s[%s]' % (Net,II)
#                New = normalize(New)
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

def explodeConnections(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Pins = list(Obj.conns.keys())
        for Pin in Pins:
            Sig = Obj.conns[Pin] 
            Seq = explodeBus(Sig,Mod)
            
            if len(Seq)>1:
                Obj.conns.pop(Pin)
                Seq.reverse()
                for ind in range(len(Seq)):
                    Pinx = '%s[%s]' % (Pin,ind)
                    Obj.conns[Pinx] = Seq[ind]



def exploadConns(Mod):
    dumpV(Mod,'a00.v')
    dealAssigns(Mod)
    explodeConnections(Mod)
    dumpV(Mod,'a01.v')
    explodeBusses(Mod)
    dumpV(Mod,'a02.v')
    makeBuffers(Mod)
    dumpV(Mod,'a03.v')
    makeReplacements(Mod)
    dumpV(Mod,'a04.v')
    removeZeroNets(Mod)
    dumpV(Mod,'a04.v')

def dumpV(Mod,Fname):
    if not Mod: 
        logs.log_error('NO Mod for %s' % Fname)
        return
    File = open(Fname,'w')
    Mod.dump_verilog(File)
    File.close()

def makeBuffers(Mod):
    for ind,(Dst,Src,_,_) in enumerate(Mod.hard_assigns):
        Mod.add_inst_conns('BUF','',[('A',Mod.pr_expr(Src)),('X',Mod.pr_expr(Dst))])
    Mod.hard_assigns = []

def makeReplacements(Mod):
    REPLACE = {} 
    REMOVE = []

    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == 'BUF':
            In = Mod.pr_expr(Obj.conns['A'])
            Out = Mod.pr_expr(Obj.conns['X'])
            if In.startswith('outx_'):
                REMOVE.append(Inst)
                REPLACE[In] = Out
    for Inst in REMOVE:
        Mod.insts.pop(Inst)
    useReplace(REPLACE,Mod)


#    for ind,(Dst,Src,_,_) in enumerate(Mod.hard_assigns):
#        if Src == 'outx_'+Dst:
#            Mod.hard_assigns.pop(ind)
#            REPLACE[Src] = Dst
#        else:
#            Mod.add_inst_conns('BUF','',[('A',Src),('X',Dst)])



def useReplace(REPLACE,Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            Sig = Mod.pr_expr(Sig)
            if Sig in REPLACE:
                Obj.conns[Pin] = REPLACE[Sig]
                if Sig in Mod.nets: Mod.nets.pop(Sig)
                logs.log_info("REPLACE %s %s pin=%s sig=%s rep=%s" % (Inst,Obj.Type,Pin,Sig,REPLACE[Sig]))
            else:
                Obj.conns[Pin] = Sig

def removeZeroNets(Mod):
    Many = {}
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            if Sig not in Many: Many[Sig] = 0
            Many[Sig] += 1
    Nets = list(Mod.nets.keys()) 
    RM = []
    for Net in Nets:
        if Net not in Many:
            Mod.nets.pop(Net)
        elif Net.startswith('outx_') and (Many[Net] == 1):
#            Mod.nets.pop(Net)
            RM.append(Net)

    Insts = list(Mod.insts.keys())
    for Inst in Insts:
        Obj = Mod.insts[Inst]
        if libType(Obj.Type):
            Goes = False
            GoesNet = False
            for Pin in Obj.conns:
                Sig = Obj.conns[Pin]
                if Sig in RM:
                    Goes = True
                    GoesNet = Sig
            if Goes: 
                Mod.insts.pop(Inst)
                Mod.nets.pop(GoesNet)
