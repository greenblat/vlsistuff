
import os
STRING = '''
class holder:
    def __init__(self):
        self.Name = "NAME"

hld = holder()
'''


ARCSBK = {}
ARCSFW = {}
CONNS = []
TERMS = []
INPUTS = []
OUTPUTS = []
SONS = []
from pprint import pprint
import pprint
from module_class import support_set
def help_main(Env):
    for Module in Env.Modules:
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
    out.close()

def adds(Dst,Src,Nons):
    SetS = support_set(Src,False)
    SetD = support_set(Dst,False)
    SetS = cleanNons(SetS,Nons+SetD)
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
            Dst = support_set(Alw[1],False)
            Src = support_set(Alw[2],False)
            adds(Dst,Src,Params)
            for D in Dst: 
                if D not in TERMS: TERMS.append(D)
            return

        if Alw[0]=='=':
            Dst = support_set(Alw[1],False)
            Src = support_set(Alw[2],False)
            adds(Dst,Src,Params)
            return


    print('ERROR alw',Alw)



