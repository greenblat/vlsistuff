
import os,sys
sys.path.append('/Users/iliagreenblat/vlsistuff/verification_libs3')
import logs 
import module_class
import new_flattens
import importlib
import copy
from codes import Codes
try:
    import torch
except:
    torch = False

Moses = ['nmos','pmos','dgvnfet','dgvpfet','nfet','pfet','dgxnfet','dgxpfet','dgnfet','dgpfet']
def isMos(Type):
    return Type in Moses
def isNmos(Type):
    return ('nmos' in Type) or ('nfet' in Type)
def isPmos(Type):
    return ('pmos' in Type) or ('pfet' in Type)
def compatibleMos(Mos0,Mos1):
    A = Mos0.replace('n','p')
    B = Mos1.replace('n','p')
    return A==B 
def otherSide(Mod,Inst,One):
    Obj = Mod.insts[Inst]
    Sh = module_class.hashit(Obj.conns['i'])
    Dh = module_class.hashit(Obj.conns['o'])
    if One == Sh: return Dh 
    if One == Dh: return Sh 
    logs.log_error('otherSide %s %s %s %s' % (Mod.Module,Inst,One,Obj.conns))
    return One


def parallels2(Mod,Kinds):
    Db = {}
    for Kind in Kinds:
        Db[Kind] = {}
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        LL = []
        if Obj.Type in Kinds:
            Str0,Other0 = '%s %s' % (hsh(Obj.conns['g']),hsh(Obj.conns['i'])),hsh(Obj.conns['o'])
            Str1,Other1 = '%s %s' % (hsh(Obj.conns['g']),hsh(Obj.conns['o'])),hsh(Obj.conns['i'])
            if Str0 not in Db[Obj.Type]: Db[Obj.Type][Str0] = []
            if Str1 not in Db[Obj.Type]: Db[Obj.Type][Str1] = []
            Db[Obj.Type][Str0].append((Inst,Other0))
            Db[Obj.Type][Str1].append((Inst,Other1))
    Renames = []
    for Kind in Kinds:
        Profiles = Db[Kind]
        for Prof in Profiles:
            List = Profiles[Prof]
            if len(List)==1:
                pass
            elif len(List)==2:
                Inst0,Other0 = List[0]
                Inst1,Other1 = List[1]
                Mod.insts.pop(Inst1)
                Renames.append((Other1,Other0))
                print("AAAA insts=",Inst0,Inst1," others=",Other0,Other1,' prof ',Prof)
            elif len(List)==3:
                Inst0,Other0 = List[0]
                Inst1,Other1 = List[1]
                Inst2,Other2 = List[2]
                Mod.insts.pop(Inst1)
                Mod.insts.pop(Inst2)
                Renames.append((Other1,Other0))
                Renames.append((Other2,Other0))
                print("AAAA3",Inst0,Inst1,Inst2,Other0,Other1,Other2)
            else:
                Inst0,Other0 = List[0]
                for Instx,Otherx in List[1:]:
                    Mod.insts.pop(Instx)
                    Renames.append((Otherx,Other0))
                logs.log_warning("Parallels2 WIDE got %d in semi parallel of %s" % (len(List),Mod.Module))
    Dones = 0
    for Inst in Mod.insts:                
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Was = Obj.conns[Pin]
            for From,To in Renames:
                if Was == From:
                    Obj.conns[Pin] = To
                    Dones += 1
    if Dones>0:
        logs.log_info('parallels2 deeper %s ' % Dones)
        parallels2(Mod,Kinds)



def parallels(Mod,Kinds):
    Db = {}
    for Kind in Kinds:
        Db[Kind] = {}
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        LL = []
        if Obj.Type in Kinds:
            for Pin in Obj.conns:
                LL.append((Pin,Obj.conns[Pin]))
            LL.sort()
            Str = ''
            for (_,Net) in LL:
                Str += ' %s' % Net
            if Str not in Db[Obj.Type]: Db[Obj.Type][Str] = []
            Db[Obj.Type][Str].append(Inst)
    Dones = 0
    for Kind in Kinds:
        Profiles = Db[Kind]
        for Prof in Profiles:
            List = Profiles[Prof]
            if len(List)>1:
                for Inst in List[1:]:
                    Mod.insts.pop(Inst)
                    Dones += 1
    logs.log_info('parallels in %s removed %d mos' % (Mod.Module,Dones))




def help_main(Env):
    Mod = Env.Current
    Env.DontFlattens.extend(Moses)
    flattenDeep(Mod,Env)
    logs.log_info('total0 components is %s in %s' % ( len(Mod.insts.keys()),Mod.Module))
    parallels(Mod,Moses)
    retypeAllMos(Mod)
    parallels2(Mod,['nmos','pmos'])
    logs.log_info('total1 components is %s in %s' % ( len(Mod.insts.keys()),Mod.Module))
    Mod.buildNetTable()
    if torch:
        restoreModel('model.pt')
    clusterFind(Mod)
    

### class TranslationModel(torch.nn.Module):
###     def __init__(self, input_size, output_size,numLines):
###         if not Base: return
###         super(TranslationModel, self).__init__()
### 
###         # Define the layers of the neural network
###         self.linear1 = torch.nn.Linear(input_size, numLines)
###         self.activation = torch.nn.ReLU()
###         self.linear2 = torch.nn.Linear(numLines, output_size)
### 
###     def forward(self, x): 
###         # Pass the input through the first linear layer and the activation function
###         x = self.linear1(x)
###         x = self.activation(x)
### 
###         # Pass the output of the first linear layer through the second linear layer
###         x = self.linear2(x)
### 
###         return x
### 


def restoreModel(Filename):

    global model,optimizer

    model = TranslationModel(MaxA, MaxB,Len)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    training_results = torch.load("model.pt")
    model.state_dict = training_results['model_state_dict']
    optimizer.state_dict = training_results['optimizer_state_dict']





def clusterFind(Mod):
    for Net in Mod.netTable:
        List = Mod.netTable[Net]
        if meetNP(List):
            Cluster = travelCluster([Net],Mod,[],[])
            Cmode = makeModule(Cluster[2],Cluster[3],Mod)
            Cline = makeLine(Cmode)
            print('cline',Cline)

def clusterFind2(Mod):
    Mod.buildNetTable()
    Clusters = []
    for Net in Mod.netTable:
        List = Mod.netTable[Net]
        if meetNP(List):
            Cluster = travelCluster([Net],Mod,[],[])
            Cmode = makeModule(Cluster[2],Cluster[3],Mod)
            Cline = cline0(Cmode)
            Clusters.append((Cline,Cluster[2]))
    return Clusters



def cline0(Mod):
    Line0 = createNetlistLine(Mod)
    Line0.sort()
    return Line0

def makeLine(Mod):
    Line0 = createNetlistLine(Mod)
    Line0.sort()
    print('cline0',Line0)
    Line1,Nets = numerizeLine(Line0)
    return Line1


def createNetlistLine(Mod):
    NN = []
#    for Net in Mod.nets:
#        if Mod.nets[Net][0] == 'input':
#            NN.append(('input',Net))
#        elif 'output' in Mod.nets[Net][0]:
#            NN.append(('output',Net))
    for Inst in Mod.insts:
        Rec = instRecord(Mod.insts[Inst])
        NN.append(Rec)
    return NN

from module_class import hashit
def instRecord(Obj):
    LL = [Obj.Type]
    Pins = list(Obj.conns.keys())
    Pins.sort()
    for Pin in Pins:
        Sig = hashit(Obj.conns[Pin])
        if (Obj.Type in ['nmos','pmos']) and (Pin in ['i','o']):
            LL.append('<%s' % (Sig))
        else:
            LL.append('%s=%s' % (Pin,Sig))
    return LL


Index = 2
def codifyNet(Net,Nets):
    global Index
    if Net in Nets:
        return Nets[Net]
    Nets[Net] = Index
    Index += 1
    return Nets[Net]


def numerizeLine(Line):
    Out = []
    Nets = {'vcc':1,'gnd':-1}
    for Item in Line:
        Kind = Codes[Item[0]]
        Out.append(Kind)
        for Net in Item[1:]:
            Code = codifyNet(Net,Nets)
            Out.append(Code)
        Out.append(0)
    return Out,Nets









def makeModule(Insts,Internals,Mod):
    X = logs.incrVar('cluster')
    Name = 'cluster%d' % X
    Clust = module_class.module_class(Name)
    for Inst in Insts:
        Obj = copy.deepcopy(Mod.insts[Inst])
        Clust.insts[Inst] = Obj
    for Inst in Insts:
        Obj = Clust.insts[Inst]
        for Pin in Obj.conns:
            Sig = hsh(Obj.conns[Pin])
            Clust.nets[Sig] = 'wire',1
            Obj.conns[Pin] = Sig
    return Clust

def isInput(Sig,Mod):
    if type(Sig) is str:
        return (Sig in Mod.nets) and ('input' in Mod.nets[Sig])
    if type(Sig) is list:
        return isInput(Sig[1],Mod)

    logs.log_error(' %s failed isInput test in %s' % (Sig,Mod.Module))
    return False



def meetNP(List):
    Nok,Pok = False,False
    for Inst,Type,Pin in List:
        if (Pin in ['i','o']) and isNmos(Type): Nok = True
        if (Pin in ['i','o']) and isPmos(Type): Pok = True
    return Nok and Pok

def travelCluster(Nets,Mod,SofarInsts,SofarNets):
    News = []
    Down = []
    if Nets == []: return [],Mod,SofarInsts,SofarNets
    for Net in Nets:
        List = Mod.netTable[Net]
        for Inst,Type,Pin in List:
            if (Inst in Mod.insts) and (Pin in ['i','o']) and isMos(Type) and (Inst not in News) and (Inst not in SofarInsts): 
                News.append(Inst)
                Other = otherSide(Mod,Inst,Net)
                Bulk = Mod.insts[Inst].conns['bulk']
                if (Other!= Bulk) and (Other not in Nets): Down.append(Other)
            
    return travelCluster(Down,Mod,SofarInsts+News,SofarNets+Down)




def retypeAllMos(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        if Type in Translates:
            Map = Translates[Type]
            Obj.Type = Map['type']
            for Pin in list(Obj.conns.keys()):
                Npin = Map[Pin]
                Sig = Obj.conns[Pin]
                Obj.conns.pop(Pin)
                Obj.conns[Npin] = Sig 
        elif (Type in ['nmos','pmos']):
            pass
        elif (Type in Moses):
            logs.log_error("Type %s has no translate, %s" % (Type,list(Obj.conns)))
        if 'bulk' not in Obj.conns:
            if Obj.Type == 'nmos': Obj.conns['bulk'] = 'gnd'
            if Obj.Type == 'pmos': Obj.conns['bulk'] = 'vcc'



Translates = {}
Translates['nfet'] = {'type':'nmos','s':'i','d':'o','gate':'g','bulk':'bulk'}
Translates['pfet'] = {'type':'pmos','s':'i','d':'o','gate':'g','bulk':'bulk'}
Translates['dgxnfet'] = {'type':'nmos','s':'i','d':'o','gate':'g','bulk':'bulk'}
Translates['dgxpfet'] = {'type':'pmos','s':'i','d':'o','gate':'g','bulk':'bulk'}
Translates['dgvnfet'] = {'type':'nmos','s':'i','d':'o','gate':'g','bulk':'bulk'}
Translates['dgvpfet'] = {'type':'pmos','s':'i','d':'o','gate':'g','bulk':'bulk'}
Translates['dgnfet'] = {'type':'nmos','s':'i','d':'o','gate':'g','bulk':'bulk'}
Translates['dgpfet'] = {'type':'pmos','s':'i','d':'o','gate':'g','bulk':'bulk'}

def hsh(Net):
    return module_class.hashit(Net)



def flattenDeep(Mod,Env):
    new_flattens.flatten_deep(Mod,'*',Env,Env.try_and_load_module)

