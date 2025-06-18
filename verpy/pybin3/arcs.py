
import os
import logs
from module_class import hashit
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
DRIVEN = {}
CONNS = []
TERMS = {}
STARTS = {}
CLOCKED = {}
INPUTS = []
OUTPUTS = []
SONS = []
COSTS = []
from pprint import pprint
import pprint
from module_class import support_set
def help_main(Env):
    global ARCSBK ,ARCSFW ,CONNS ,TERMS ,INPUTS ,OUTPUTS ,SONS, COSTS, DRIVEN


    for Module in Env.Modules:
        ARCSBK = {}
        ARCSFW = {}
        CONNS = []
        TERMS = {}
        INPUTS = []
        OUTPUTS = []
        SONS = []
        COSTS = {}
        DRIVEN = {}
        buildOne(Env.Modules[Module])


def buildOne(Mod):
    builds(Mod)
    if not os.path.exists('arcs'):
        os.mkdir('arcs')
    out = open('arcs/%s.py'%Mod.Module,'w')
    out.write(STRING.replace('NAME',Mod.Module))
    out.write('hld.ARCSFW = %s\n'%pprint.pformat(ARCSFW))
    out.write('hld.CONNS = %s\n'%pprint.pformat(CONNS))
    out.write('hld.TERMS = %s\n'%pprint.pformat(TERMS))
    out.write('hld.CLOCKED = %s\n'%pprint.pformat(CLOCKED))
    out.write('hld.INPUTS = %s\n'%pprint.pformat(INPUTS))
    out.write('hld.OUTPUTS = %s\n'%pprint.pformat(OUTPUTS))
    out.write('hld.SONS = %s\n'%pprint.pformat(SONS))
    out.write('hld.COSTS = %s\n'%pprint.pformat(COSTS))
    out.write('hld.STARTS = %s\n'%pprint.pformat(STARTS))
    out.write('hld.DRIVEN = %s\n'%pprint.pformat(DRIVEN))
    out.write('hld.ARCSBK = %s\n'%pprint.pformat(ARCSBK))
    out.close()

def getCosts(Src,Deep):
    SetS = support_set(Src,False)
    if type(Src) is str:
        if Src in SetS:
            return [(Src,0)]
    elif type(Src) is int:
        return []
    elif type(Src) is list:
        if Src == []: return []
        if len(Src) == 1:
            return getCosts(Src[0],Deep+1)
        if Src[0] in ['hex','bin','dig']:
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
                return getCosts(Src[1],Deep+1)
            else:
                Costs =  getCosts(Src[1],Deep+1)
                return mergeCosts(Costs,Costs,2)
        elif Src[0] in ['*']:
            Csts0 = getCosts(Src[1],Deep+1)
            Csts1 = getCosts(Src[2],Deep+1)
            return mergeCosts(Csts0,Csts1,4)
        elif Src[0] in ['+','-']:
            Csts0 = getCosts(Src[1],Deep+1)
            if len(Src)==3:
                Csts1 = getCosts(Src[2],Deep+1)
                return mergeCosts(Csts0,Csts1,2)
            return mergeCosts(Csts0,[],2)
        elif Src[0] in ['!','~']:
            Csts0 = getCosts(Src[1],Deep+1)
            return mergeCosts(Csts0,[],1)

        elif Src[0] in ['&','&&','|','||','^','>','<','>=','<=','==','!=']:
            Csts0 = getCosts(Src[1],Deep+1)
            if len(Src) == 3:
                Csts1 = getCosts(Src[2],Deep+1)
                Cost =  mergeCosts(Csts0,Csts1,1)
                return Cost
            if len(Src) == 2:
                Csts0 =  getCosts(Src[1],Deep+1)
                Cost =  mergeCosts(Csts0,[],1)
                return Cost


        elif Src[0] in ['question']:
            Csts0 = getCosts(Src[1],Deep+1)
            Csts1 = getCosts(Src[2],Deep+1)
            Csts2 = getCosts(Src[3],Deep+1)
            Csts3 =  mergeCosts(Csts1,Csts2,1)
            Cost =  mergeCosts(Csts0,Csts3,1)
            print("QUESTION",Cost,Src)
            return Cost
        elif Src[0] in ['curly']:
            Csts = []
            for Item in Src[1:]:
                Cost = getCosts(Item,Deep+1)
                Csts = mergeCosts(Csts,Cost,0)
            return Csts                
                
    if type(Src) is list:
        Csts = []
        for Sig in Src:
            Cost = getCosts(Sig,Deep+1)
            Csts = mergeCosts(Csts,Cost,0)
        return Csts


    logs.log_error('failed deep=%s cost %s' % (str(Deep),Src))
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
#    print('COSTIT dst=%s src=%s' % (Dst,Src))
    Costs =  getCosts(Src,0)
    SetD = support_set(Dst,False)
    for D in SetD:
        for (S,Cost) in Costs:
            COSTS[(D,S)] = Cost


def adds(Dst,Src,Nons,Where):
    SetS = support_set(Src,False)
    if Dst[0] == 'subbit':
        SetD = support_set(Dst[1],False)
    else:
        SetD = support_set(Dst,False)
#    print("ADDS dst=",Dst,' src=',Src,' setS',SetS,'setD',SetD)
    SetS = cleanNons(SetS,Nons+SetD)
    Cost = costIt(Dst,Src)
    for Out in SetD:
        if Out not in ARCSBK:
            ARCSBK[Out] = []
        for In in SetS:
            if In not in ARCSBK[Out]: 
                ARCSBK[Out].append(In)
#                print("ADDS0",Where,'out=',Out,'in=',In)

    for In in SetS:
        if In not in ARCSFW:
            ARCSFW[In] = []
        for Out in SetD:
            if Out not in ARCSFW[In]: 
                ARCSFW[In].append(Out)
#                print("ADDS1",Where,'out=',Out,'in=',In)

def cleanNons(Lst,Nons):
    for Non in Nons:
        if Non in Lst:
            Lst.remove(Non)
    return Lst


GATELEVEL = {}
GATELEVEL['EFX_ADD'] = [('CI','I0','I1'),('CO','O')]
GATELEVEL['EFX_LUT4'] = [('I0','I1','I2','I3'),('O')]
GATELEVEL['EFX_MULT'] = [('A', 'B', 'CEA', 'CEB','RSTA', 'RSTB'), ('CEO', 'O', 'RSTO'),('CLK')]
GATELEVEL['EFX_FF'] = [('CE', 'D'), ('Q'),('CLK','SR')]
GATELEVEL['EFX_GBUFCE'] = [('CE', 'I'), ('O')]
GATELEVEL['EFX_RAM_5K'] = [('RADDR', 'RE', 'WADDR','WE','WDATA','WCLKE'),('RDATA'),('RCLK','WCLK')]


GATELEVEL['bufx'] = [('a'),('x')]
GATELEVEL['inv'] = [('a'),('x')]
GATELEVEL['xor2'] = [('a','b'),('x')]
GATELEVEL['or2'] = [('a','b'),('x')]
GATELEVEL['or3'] = [('a','b','c'),('x')]
GATELEVEL['or4'] = [('a','b','c','d'),('x')]
GATELEVEL['or5'] = [('a','b','c','d','e'),('x')]
GATELEVEL['or6'] = [('a','b','c','d','e','f'),('x')]
GATELEVEL['or7'] = [('a','b','c','d','e','f','g'),('x')]
GATELEVEL['or8'] = [('a','b','c','d','e','f','g','h'),('x')]
GATELEVEL['and2'] = [('a','b'),('x')]
GATELEVEL['and3'] = [('a','b','c'),('x')]
GATELEVEL['and4'] = [('a','b','c','d'),('x')]

COMPLEX = {}
COMPLEX['adder'] = [('a','b'),('x')]
COMPLEX['right'] = [('a','b'),('x')]
COMPLEX['shiftright'] = [('a','b'),('x')]
COMPLEX['shiftleft'] = [('a','b'),('x')]
COMPLEX['adder_lit'] = [('a','b'),('x')]
COMPLEX['multiplier'] = [('a','b'),('x')]
COMPLEX['subtractor'] = [('a','b'),('x')]
COMPLEX['subtractor_lit'] = [('a','b'),('x')]
COMPLEX['mux2'] = [('a','b','sel'),('x')]
COMPLEX['select'] = [('a','b','sel'),('x')]
COMPLEX['select_bus'] = [('a','b','sel'),('x')]
COMPLEX['select_bus_lit'] = [('a','sel'),('x')]
COMPLEX['comparator'] = [('a','b'),('x')]
COMPLEX['comparator_lit'] = [('a'),('x')]
COMPLEX['flipflop'] = [('d','en'),('q'),('clk','rst_n')]



if os.path.exists('gatelevel.py'):
    print('importing gatelevel')
    from gatelevel import GATELEVEL


def builds(Mod):
    Params = []
    for Param in Mod.parameters:
        Params.append(Param)
    for Param in Mod.localparams:
        Params.append(Param)


    for Dst,Src,_,_ in Mod.hard_assigns:
        adds(Dst,Src,['vcc','gnd']+Params,'hard_assign')
                
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        if Obj.Type in GATELEVEL:
            GL = GATELEVEL[Obj.Type]
            if len(GL) == 2:
                Outs,Inps = whatConnected(Obj,GL[1]),whatConnected(Obj,GL[0])
                adds(Outs,Inps,['vcc','gnd'],'instance_glv')
                driven(Outs,Inst,Obj.Type)
            elif len(GL) == 3:
                Outs,Inps = whatConnected(Obj,GL[1]),whatConnected(Obj,GL[0])
                for D in Inps: 
                    if D not in TERMS: 
                        TERMS[D] = (Obj.Type,Inst)
                        CLOCKED[D] = GL[2][0]
        elif Obj.Type in COMPLEX:
            Arcs = getComplexArcs(Obj)
            if Obj.Type == 'flipflop':
                print("FFF",Mod.Module,Inst,Obj.Type,len(Arcs))
            for Fr,To in Arcs:
                if (Fr in Obj.conns) and (To in Obj.conns):
#                    if Obj.Type == 'flipflop':print("XXXX",Inst,Obj.Type,Fr,To)
                    Frnet = Obj.conns[Fr]
                    Tonet = Obj.conns[To]
                    adds(Tonet,Frnet,[],'inst_complex')    
                    driven([Tonet],Obj.Name,Obj.Type)
            Ds,Qs,Clk = getFlipFlop(Obj)
            for D in Ds: 
                if D not in TERMS: 
                    TERMS[D] = (Obj.Type,Inst)
                    CLOCKED[D] = Clk
            for Q in Qs: 
                if Q not in STARTS: 
                    STARTS[Q] = (Obj.Type,Inst)
                    CLOCKED[Q] = Clk
        else:
            SONS.append((Inst,Obj.Type))
            for Pin in Obj.conns:
                Sig = Obj.conns[Pin]
                SetS = support_set(Sig,False)
                for Src in SetS:
                    CONNS.append((Inst,Pin,Src))
    for Timing,Alw,_ in Mod.alwayses:
        Clk = getClockFromEdge(Timing)
        travelAlw(Alw,[],Params,Mod,Clk)

    for Net in Mod.nets:
        Dir,_ = Mod.nets[Net]
        if 'output' in Dir: OUTPUTS.append(Net)
        if 'input' in Dir: INPUTS.append(Net)


def getFlipFlop(Obj):
    if Obj.Type != 'flipflop': return [],[],''
    Clk = Obj.conns['clk']
    Wid = Obj.params['WID']
    Ds = []
    Qs = []
    if Wid == 1:
        print("GETFLIPFLIP %s %s" % (Obj.Name,Obj.conns))
        Ds.append(Obj.conns['d'])
        Qs.append(Obj.conns['q'])
        return Ds,Qs,Clk

    for ii in range(Wid):
        Dpin = 'd_%d_' % ii 
        Qpin = 'a_%d_' % ii 
        if Dpin in Obj.conns: Ds.append(Obj.conns[Dpin])
        if Qpin in Obj.conns: Qs.append(Obj.conns[Qpin])
    return Ds,Qs,Clk

def getComplexArcs(Obj):
    Type = Obj.Type
    Params = makeInts(Obj.params)

    Res = []
    if Type == 'mux2':
        Wid = Params['WID']
        for ii in range(Wid):
            Res.append( ('yes_%d_'%ii,'x_%d_'%ii) )
            Res.append( ('no_%d_'%ii,'x_%d_'%ii) )
            Res.append( ('sel','x_%d_'%ii) )
        return Res            

    if Type == 'comparator_lit':
        Wid = Params['WID']
        for ii in range(Wid):
            Res.append( ('a_%d_'%ii,'x') )
        return Res            
    if Type == 'comparator':
        Wida = Params['WIDA']
        Widb = Params['WIDB']
        for ii in range(Wida):
            Res.append( ('a_%d_'%ii,'x') )
        for ii in range(Widb):
            Res.append( ('b_%d_'%ii,'x') )
        return Res            
    if Type == 'multiplier':
        Wid = Params['WID']
        for ii in range(Wid):
            for jj in range(Wid):
                Res.append( ('a_%d_'%jj,'x_%d_'%ii) )
                Res.append( ('b_%d_'%jj,'x_%d_'%ii) )
        return Res            
    if Type == 'adder':
        Wid = Params['WID']
        for ii in range(Wid):
            for jj in range(ii,Wid):
                Res.append( ('a_%d_'%jj,'x_%d_'%ii) )
                Res.append( ('b_%d_'%jj,'x_%d_'%ii) )
        return Res            
    if Type == 'adder_lit':
        Wid = Params['WID']
        for ii in range(Wid):
            for jj in range(ii,Wid):
                Res.append( ('a_%d_'%jj,'x_%d_'%ii) )
        return Res            

    if Type == 'subtractor':
        Wid = Params['WID']
        for ii in range(Wid):
            for jj in range(ii,Wid):
                Res.append( ('a_%d_'%jj,'x_%d_'%ii) )
                Res.append( ('b_%d_'%jj,'x_%d_'%ii) )
        return Res            
    if Type == 'subtractor_lit':
        Wid = Params['WID']
        for ii in range(Wid):
            for jj in range(ii,Wid):
                Res.append( ('a_%d_'%jj,'x_%d_'%ii) )
        return Res            

    if Type == 'select_bus':
        Wid = Params['WID']
        Depth = Params['DEPTH']
        Bits = len(bin(Depth))-2
        for ii in range(Wid):
            for jj in range(Depth):
                kk = jj*Wid + ii
                Res.append( ('a_%d_'%kk,'x_%d_'%ii) )
            for bb in range(Bits):
                Res.append( ('b_%d_'%bb,'x_%d_'%ii) )
        return Res            
                    
    if Type == 'shiftleft':
        Wid = Params['WID']
        Bits = len(bin(Wid))-2
        for ii in range(Wid):
            for jj in range(ii,Wid):
                Res.append( ('a_%d_'%jj,'x_%d_'%ii) )
            for bb in range(Bits):
                Res.append( ('b_%d_'%bb,'x_%d_'%ii) )
        return Res            
                    
    if Type == 'shiftright':
        Wid = Params['WID']
        Bits = len(bin(Wid))-2
        for ii in range(Wid):
            for jj in range(Wid-1,ii-1,-1):
                Res.append( ('a_%d_'%jj,'x_%d_'%ii) )
            for bb in range(Bits):
                Res.append( ('b_%d_'%bb,'x_%d_'%ii) )
        return Res            
                    


    if Type == 'flipflop':
#        Wid = Params['WID']
#        for ii in range(Wid):
#            Res.append( ('clk','q_%d_'%ii) )
        return Res

    print(Type,Params,list(Obj.conns.keys()))
    return []

def getClockFromEdge(Timing):
    if type(Timing) is list:
        if Timing[0] == 'list':
            if (Timing[1][0] == 'edge') and (Timing[1][1] == 'posedge'):
                return Timing[1][2]
        elif (Timing[0] == 'edge')and (Timing[0][1] == 'posedge'):
                return Timing[0][2]
    return False

def whatConnected(Obj,Pins):
    Res = []
    for Pin in Pins:
        if Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            if Sig[0] not in ['0','1','vcc','gnd']:
                Res.append(Sig)
    return Res

def driven(Outs,Inst,Type):
    for Out in Outs:
        DRIVEN[hashit(Out)] = (Inst,Type)



def travelAlw(Alw,Cond,Params,Mod,Clk):
    if type(Alw) is list:
        if Alw[0]=='list':
            for AA in Alw[1:]:
                travelAlw(AA,Cond,Params,Mod,Clk)
            return
        if Alw[0]=='for':
            travelAlw(Alw[4],Cond,Params,Mod,Clk)
            return
        if Alw[0]=='ifelse':
            More = support_set(Alw[1],False)
            print("IFELSE",Alw[2],Alw[3],Cond+More,Params)
            travelAlw(Alw[2],Cond+More,Params,Mod,Clk)
            travelAlw(Alw[3],Cond+More,Params,Mod,Clk)
            return

        if Alw[0]=='if':
            More = support_set(Alw[1],False)
            print("IF",Alw[2],Cond+More,Params)
            travelAlw(Alw[2],Cond+More,Params,Mod,Clk)
            return

        if Alw[0]=='wait': return
        if Alw[0]=='#': return

        if Alw[0]=='case':
            More = support_set(Alw[1],False)
            for Case in Alw[2]:
               More2 = support_set(Case[0],False) 
               travelAlw(Case[1],Cond+More+More2,Params,Mod,Clk)
            return

        if Alw[0]=='<=':
            Str = '<= %s %s' % (Alw[1],Alw[2])
            adds(Alw[1],Alw[2],Params,Str)
            adds(Alw[1],Cond,Params,'<=cond')
            SetD = support_set(Alw[1],False)
            for D in SetD: 
                if D not in TERMS: 
                    TERMS[D] = Alw[2]
                    CLOCKED[D] = Clk
            return

        if Alw[0]=='=':
            adds(Alw[1],Alw[2],Params,'=')
            adds(Alw[1],Cond,Params,'=cond')
            return

        if Alw[0]=='functioncall':
            return
        if Alw[0]=='empty_begin_end':
            return

    logs.log_error('ARCS %s: alw %s' % (Mod.Module,Alw))

def makeInts(Params):
    for Key in Params:
        Val = Params[Key]
        if type(Val) is str:
            try:
                Valx = eval(Val)
                Params[Key] = Valx
            except:
                pass
    return Params

