
import os
import logs
STRING = '''
class holder:
    def __init__(self):
        self.Name = "NAME"


    def travelFW(self,Net,Deep=0,Sofar=[]):
        if Net in self.ARCSFW:
            Tos = self.ARCSFW[Net]
            print('FW',Net,Deep,Tos)
            Sofar.append(Net)
            for To in Tos:
                if To not in Sofar:
                    self.travelFW(To,Deep+1,Sofar)
    
    
    def travelBK(self,Net,Deep=0,Sofar=[]):
        if Net in self.ARCSBK:
            Tos = self.ARCSBK[Net]
            print('BK',Net,Deep,Tos)
            Sofar.append(Net)
            for To in Tos:
                if To not in Sofar:
                    self.travelBK(To,Deep+1,Sofar)

hld = holder()

'''


ARCSBK = {}
ARCSFW = {}
CONNS = []
TERMS = []
INPUTS = []
OUTPUTS = []
SONS = []
COSTS = []
from pprint import pprint
import pprint
from module_class import support_set
def help_main(Env):
    global ARCSBK ,ARCSFW ,CONNS ,TERMS ,INPUTS ,OUTPUTS ,SONS, COSTS

    for Module in Env.Modules:
        ARCSBK = {}
        ARCSFW = {}
        CONNS = []
        TERMS = []
        INPUTS = []
        OUTPUTS = []
        SONS = []
        COSTS = {}
        buildOne(Env.Modules[Module])


def buildOne(Mod):
    builds(Mod)
    if not os.path.exists('arcs'):
        os.mkdir('arcs')
    out = open('arcs/%s.py'%Mod.Module,'w')
    out.write(STRING.replace('NAME',Mod.Module))
    out.write('hld.ARCSBK = %s\n'%pprint.pformat(ARCSBK))
    out.write('hld.ARCSFW = %s\n'%pprint.pformat(ARCSFW))
    out.write('hld.CONNS = %s\n'%pprint.pformat(CONNS))
    out.write('hld.TERMS = %s\n'%pprint.pformat(TERMS))
    out.write('hld.INPUTS = %s\n'%pprint.pformat(INPUTS))
    out.write('hld.OUTPUTS = %s\n'%pprint.pformat(OUTPUTS))
    out.write('hld.SONS = %s\n'%pprint.pformat(SONS))
    out.write('hld.COSTS = %s\n'%pprint.pformat(COSTS))
    out.close()

def getCosts(Src):
    SetS = support_set(Src,False)
    if type(Src) is str:
        if Src in SetS:
            return [(Src,0)]
    elif type(Src) is int:
        return []
    elif type(Src) is list:
        if Src == []: return []
        if len(Src) == 1:
            return getCosts(Src[0])
        if Src[0] in ['hex','bin','dec']:
            return []
        elif Src[0] in ['subbus']:
            return [(Src[1],0)]
        elif Src[0] in ['subbit']:
            if type(Src[2]) is int:
                return [(Src[1],0)]
            else:
                return [(Src[1],2)]
        elif Src[0] in ['>>','<<']:
            if type(Src[2]) is int:
                return getCosts(Src[1])
            else:
                Costs =  getCosts(Src[1])
                return mergeCosts(Costs,Costs,2)
        elif Src[0] in ['*']:
            Csts0 = getCosts(Src[1])
            Csts1 = getCosts(Src[2])
            return mergeCosts(Csts0,Csts1,4)
        elif Src[0] in ['+','-']:
            Csts0 = getCosts(Src[1])
            if len(Src)==3:
                Csts1 = getCosts(Src[2])
                return mergeCosts(Csts0,Csts1,2)
            return mergeCosts(Csts0,[],2)
        elif Src[0] in ['!','~']:
            Csts0 = getCosts(Src[1])
            return mergeCosts(Csts0,[],1)

        elif Src[0] in ['&','&&','|','||','^','>','<','>=','<=','==','!=']:
            Csts0 = getCosts(Src[1])
            Csts1 = getCosts(Src[2])
            Cost =  mergeCosts(Csts0,Csts1,1)
            print("CCCCC",Src,Csts0,Csts1,Cost)
            return Cost
        elif Src[0] in ['question']:
            Csts0 = getCosts(Src[1])
            Csts1 = getCosts(Src[2])
            Csts2 = getCosts(Src[3])
            Csts3 =  mergeCosts(Csts1,Csts2,1)
            Cost =  mergeCosts(Csts0,Csts3,1)
            print("QUESTION",Cost,Src)
            return Cost
        elif Src[0] in ['curly']:
            Csts = []
            for Item in Src[1:]:
                Cost = getCosts(Item)
                Csts = mergeCosts(Csts,Cost,0)
            return Csts                
                
    logs.log_error('failed cost %s' % str(Src))
    return []
    
def mergeCosts(Cost0,Cost1,Add):
    Tog = {}
    for Sig,Cost in Cost0:
        Tog[Sig] = Cost
    for Sig,Cost in Cost1:
        if Sig in Tog:
            Tog[Sig] = Tog[Sig] + Cost
        else:
            Tog[Sig] = Cost
    Res = []
    for Sig in Tog:
        Res.append((Sig,Tog[Sig]+Add))
    return Res
    

def costIt(Dst,Src):
    Costs =  getCosts(Src)
    SetD = support_set(Dst,False)
    for D in SetD:
        for (S,Cost) in Costs:
            COSTS[(D,S)] = Cost


def adds(Dst,Src,Nons):
    SetS = support_set(Src,False)
    SetD = support_set(Dst,False)
    SetS = cleanNons(SetS,Nons+SetD)
    Cost = costIt(Dst,Src)
    for Out in SetD:
        if Out not in ARCSBK:
            ARCSBK[Out] = []
        for In in SetS:
            if In not in ARCSBK[Out]: ARCSBK[Out].append(In)

    for In in SetS:
        if In not in ARCSFW:
            ARCSFW[In] = []
        for Out in SetD:
            if Out not in ARCSFW[In]: ARCSFW[In].append(Out)

def cleanNons(Lst,Nons):
    for Non in Nons:
        if Non in Lst:
            Lst.remove(Non)
    return Lst



def builds(Mod):
    Params = []
    for Param in Mod.parameters:
        Params.append(Param)
    for Param in Mod.localparams:
        Params.append(Param)


    for Dst,Src,_,_ in Mod.hard_assigns:
        adds(Dst,Src,Params)
                
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        SONS.append((Inst,Obj.Type))
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            SetS = support_set(Sig,False)
            for Src in SetS:
                CONNS.append((Inst,Pin,Src))
    for _,Alw,_ in Mod.alwayses:
        travelAlw(Alw,[],Params)

    for Net in Mod.nets:
        Dir,_ = Mod.nets[Net]
        if 'output' in Dir: OUTPUTS.append(Net)
        if 'input' in Dir: INPUTS.append(Net)


def travelAlw(Alw,Cond,Params):
    if type(Alw) is list:
        if Alw[0]=='list':
            for AA in Alw[1:]:
                travelAlw(AA,Cond,Params)
            return
        if Alw[0]=='for':
            travelAlw(Alw[4],Cond,Params)
            return
        if Alw[0]=='ifelse':
            More = support_set(Alw[1],False)
            travelAlw(Alw[2],Cond+More,Params)
            travelAlw(Alw[3],Cond+More,Params)
            return

        if Alw[0]=='if':
            More = support_set(Alw[1],False)
            travelAlw(Alw[2],Cond+More,Params)
            return

        if Alw[0]=='wait': return
        if Alw[0]=='#': return

        if Alw[0]=='case':
            More = support_set(Alw[1],False)
            for Case in Alw[2]:
               More2 = support_set(Case[0],False) 
               travelAlw(Case[1],Cond+More+More2,Params)
            return

        if Alw[0]=='<=':
            adds(Alw[1],Alw[2],Params)
            SetD = support_set(Alw[1],False)
            for D in SetD: 
                if D not in TERMS: TERMS.append(D)
            return

        if Alw[0]=='=':
            adds(Alw[1],Alw[2],Params)
            return


    print('ERROR alw',Alw)



