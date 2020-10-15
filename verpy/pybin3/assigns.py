
import logs
import module_class


def help_main(Env):
    Mod = Env.Current
    buildTranslation(Mod)
    logs.log_info('translation has %d members'%(len(TRANSLATIONS.keys())))
    Insts =  list(Mod.insts.keys())
#    gatherAssigns(Mod)
    for Inst in Insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        logs.log_info('inst %s %s'%(Inst,Type))
        Del = dealType(Type,Inst,Obj,Mod)
        if Del:
            Mod.insts.pop(Inst)



    Fout = open('%s.rtl0'%Mod.Module,'w')
    Mod.dump_verilog(Fout)
    Fout.close()
    gatherAlwayses(Mod)
    Fout = open('%s.rtl1'%Mod.Module,'w')
    Mod.dump_verilog(Fout)
    Fout.close()
    gatherExpressions(Mod)
    Fout = open('%s.rtl2'%Mod.Module,'w')
    Mod.dump_verilog(Fout)
    Fout.close()


def gatherExpressions(Mod):
    Dsts = {}
    Srcs = {}
    Invs = {}
    x2s = []
    for In in SOURCES:
        Srcs[In] = 1
    for Dst,Src,_,_ in Mod.hard_assigns:
        if type(Dst) is str:
            Dsts[Dst] = Src
            if (Src[0] == '!')and(len(Src)==2)and(type(Src[1]) is str):
                Invs[Dst] = Src[1]
        Sup = module_class.support_set(Src)
        for In in Sup:
            if (type(In) is str):
                if In not in Srcs: 
                    Srcs[In] = 1
                else: Srcs[In] += 1
                
    for Net in Dsts:
        if (Net in Srcs)and(Srcs[Net]==1)and(Net in Mod.nets):
            Dir,Wid = Mod.nets[Net]
            if Dir=='wire':
                x2s.append(Net)
    Deletes = []        
    Addeds = []
    for Inv in Invs.keys():
        Src = Invs[Inv]
        if Src in x2s:
            logs.log_info('x2s driven inverter  %s <= %s = %s'%(Inv,Src,Dsts[Src]))
            Expr = Dsts[Src]
            if Expr[0] in ('~', '!'):
                Addeds.append((Inv,Expr[1]))
                Deletes.append(Inv)
                Deletes.append(Src)
    Ind = 0
    while Ind<len(Mod.hard_assigns):
        Dst,Src,_,_ = Mod.hard_assigns[Ind]
        if Dst in Deletes:
            Mod.hard_assigns.pop(Ind)
        else:
            Ind += 1
        
    for (Dst,Src) in  Addeds:
        Mod.hard_assigns.append((Dst,Src,'',''))
            
    Uses = {}
    for Inv in Invs.keys():
        if Inv in x2s:
            Uses[Inv] = Invs[Inv]
            
    Ind = 0
    while Ind < len(Mod.hard_assigns):
        (Dst,Src,_,_)  = Mod.hard_assigns[Ind]
        Src1,Done = replaces(Src,Uses)
        if Done:
            Mod.hard_assigns[Ind] = (Dst,Src1,'','')
            logs.log_info('fixed hard_assign %s %s   <- %s'%(Dst,Src1,Src))
            Ind += 1
        elif  (type(Dst) is str) and(Dst in Uses)and(Dst not in SOURCES):
            Mod.hard_assigns.pop(Ind)
            if Dst in Mod.nets: Mod.nets.pop(Dst)
        else:
            Ind += 1

def replaces(Src,Uses):
    if (type(Src) is str) and (Src in Uses): return ('!',Uses[Src]),True
    if type(Src) is str: return Src,False

    LL = list(str(Src))
    Done = False
    for Ind,In in enumerate(LL):
        Inx,What = replaces(In,Uses)
        if What:
            LL[Ind]=Inx
            Done = True
    return LL,Done        


ALWAYS = {}
SOURCES = []
def gatherAlwayses(Mod):
    for Cond,Body,Kind in Mod.alwayses:
        if Cond not in ALWAYS: ALWAYS[Cond]=[]
        ALWAYS[Cond].append(Body)
        
    Mod.alwayses = []
    for Cond in ALWAYS:
        logs.log_info('ALWAYS %d %s'%(len(ALWAYS[Cond]),Cond))
        List = ALWAYS[Cond]
        RList = ['list']
        BList = ['list']
        if (Cond[0]=='list'):
            for Item in List:
                RR = Item[2]
                BB = Item[3]
                RList.append(RR)
                BList.append(BB)
                if (BB[0]=='<='):
                    LL = BB[2]
                    if (type(LL) is list): LL = tuple(LL)
                    if LL not in SOURCES: SOURCES.append(LL)
                MM = module_class.support_set(Item[1])
                for M1 in MM:
                    if (M1 not in SOURCES): SOURCES.append(M1)
            Mod.alwayses.append( ( Cond, ('ifelse',Item[1],RList,BList),'always'))
        elif (Cond[0]=='edge'):
            for Item in List:
                BB = Item
                BList.append(BB)
                if (BB[0]=='<='):
                    LL = BB[2]
                    if (type(LL) is list): LL = tuple(LL)
                    if LL not in SOURCES: SOURCES.append(LL)
                MM = module_class.support_set(Item[1])
                for M1 in MM:
                    if (M1 not in SOURCES): SOURCES.append(M1)
            Mod.alwayses.append( ( Cond, BList,'always'))
            
        else:
            logs.log_error('condition list is "%s"'%str(List))

ONES = []
TWOS = []

def gatherAssigns(Mod):
    netTable = Mod.prepareNetTable()
    logs.log_info('netTable %d'%len(netTable.keys()))
    for Net in netTable:
        if Net in Mod.nets:
            Dir,Wid = Mod.nets[Net]
            logs.log_info('NNNN %s %s %s'%(Net,Dir,Wid))
            if (Dir == 'wire')and(Wid==0):
                if len(netTable[Net])==2:
                    logs.log_info('two %s %s'%(Net,netTable[Net]))
                    TWOS.append(Net)
                elif len(netTable[Net])==1:
                    logs.log_info('one %s %s'%(Net,netTable[Net][0]))
                    ONES.append(Net)




def buildTranslation(Mod):
    Insts = Mod.insts.keys()
    for Inst in Insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == 'BUFX2':
            A = Obj.conns['A']
            Y = Obj.conns['Y']
            registerBuf(A,Y)
            Mod.insts.pop(Inst)
#    logs.log_info('ORIGINS %s'%(ORIGINS.keys()))
#    logs.log_info('BUFS %s'%(str(BUFS)))
#    logs.log_info('DRIVES %s'%(str(DRIVES)))
    for Out in BUFS:
        In = findIn(Out)
        TRANSLATIONS[Out] = In

def buildTranslationInv(Mod):
    Insts = Mod.insts.keys()
    for Inst in Insts:
        Obj = Mod.insts[Inst]
        if Obj.Type == 'INVX1':
            A = Obj.conns['A']
            Y = Obj.conns['Y']
            registerInv(A,Y)
            Mod.insts.pop(Inst)
#    logs.log_info('ORIGINS %s'%(ORIGINS.keys()))
#    logs.log_info('BUFS %s'%(str(BUFS)))
#    logs.log_info('DRIVES %s'%(str(DRIVES)))
    for Out in INVS:
        In = findIn(Out)
        TRANSLATIONS[Out] = In


def findIn(Net):
    if Net in ORIGINS: return Net
    Src = BUFS[Net]
    return findIn(Src)

def findInv(Net,Depth):
    if Net not in INVS: return Net,Depth
    Src = INVS[Net]
    return findInv(Src,Depth+1)




def trans(Txt):
    if (type(Txt) is str):
        if Txt in TRANSLATIONS: return TRANSLATIONS[Txt]
    return Txt

BUFS = {}
ORIGINS = {}
DRIVES = {}
TRANSLATIONS = {}

def registerBuf(A,Y):
    BUFS[Y] = A
    if A not in BUFS:
        ORIGINS[A] = True
    if Y in ORIGINS:
        ORIGINS.pop(Y)
    if A not in DRIVES:
        DRIVES[A] = [Y]
    else:
        DRIVES[A].append(Y)


def registerInv(A,Y):
    INVS[Y] = A




def dealType(Type,Inst,Obj,Mod):
    if Type in KNOWNS:
        What = KNOWNS[Type]
        if What[0]=='mul':
            logs.log_info('dealType %s %s %s'%(Type,Inst,What[1:]))
            for Dst,Op,Src in What[1:]:
                dealSingle(Dst,Op,Src,Obj,Mod)
            return True
        elif What[0]=='func':
            return What[1](Obj,Mod)
        else:
            Dst,Op,Src = KNOWNS[Type]
            dealSingle(Dst,Op,Src,Obj,Mod)
            return True
    else:
        logs.log_info('leaving %s as is'%(Type))
        return False


def dealSingle(Dst,Op,Src,Obj,Mod):
    Ins = []
    Pref = ''
    if Op!='': 
        if (Op[0]=='~')and(len(Op)>1):
            Ins.append(Op[1:])
            Pref = '~'
        else:
            Ins.append(Op)
            Pref = ''
    for In in Src:
        Inx = trans(Obj.conns[In])
        Ins.append(Inx)
    if Pref!='':
        Ins = (Pref,Ins)
    logs.log_info('dealSingle dst=%s %s  %s  ins %s'%(Dst,Obj.conns[Dst],Obj.Type,Ins))
    Mod.hard_assigns.append((Obj.conns[Dst],Ins,'',''))
    return True
        



KNOWNS = {}
KNOWNS['BUFX2'] = ('Y','',['A']) 
KNOWNS['INVX1'] = ('Y','!',['A']) 
KNOWNS['XOR2X1'] = ('Y','^',['A','B']) 
KNOWNS['XOR3X1'] = ('Y','^',['A','B','C']) 
KNOWNS['ADDHX1'] = ['mul',('CO','&',('A','B')),('S','^',('A','B'))] 

KNOWNS['BUF'] = ('Y','',['A']) 
KNOWNS['INV'] = ('Y','!',['A']) 
KNOWNS['XOR2'] = ('Y','^',['A','B']) 
KNOWNS['XOR3'] = ('Y','^',['A','B','C']) 
KNOWNS['XNOR2'] = ('Y','~^',('A','B'))
KNOWNS['XNOR3'] = ('Y','~^',('A','B','C'))

KNOWNS['AND2'] = ('Y','&',('A','B'))
KNOWNS['AND3'] = ('Y','&',('A','B','C'))
KNOWNS['NAND2'] = ('Y','~&',('A','B'))
KNOWNS['NAND3'] = ('Y','~&',('A','B','C'))
KNOWNS['NOR2'] = ('Y','~|',('A','B'))
KNOWNS['NOR3'] = ('Y','~|',('A','B','C'))
KNOWNS['OR2'] = ('Y','|',('A','B'))
KNOWNS['OR3'] = ('Y','|',('A','B','C'))




KNOWNS['AND2X1'] = ('Y','&',('A','B'))
KNOWNS['AND3X1'] = ('Y','&',('A','B','C'))
KNOWNS['AND4X1'] = ('Y','&',('A','B','C','D'))
KNOWNS['NAND2X1'] = ('Y','~&',('A','B'))
KNOWNS['NAND3X1'] = ('Y','~&',('A','B','C'))
KNOWNS['NAND4X1'] = ('Y','~&',('A','B','C','D'))
KNOWNS['NOR2X1'] = ('Y','~|',('A','B'))
KNOWNS['NOR3X1'] = ('Y','~|',('A','B','C'))
KNOWNS['NOR4X1'] = ('Y','~|',('A','B','C','D'))
KNOWNS['XNOR2X1'] = ('Y','~^',('A','B'))
KNOWNS['XNOR3XL'] = ('Y','~^',('A','B','C'))


def mx2x1(Obj,Mod):
    A = trans(Obj.conns['A'])
    B = trans(Obj.conns['B'])
    S0 = trans(Obj.conns['S0'])
    Y = Obj.conns['Y']
    Mod.hard_assigns.append((Y,('?',S0,B,A),'',''))
    return True


def mx3x1(Obj,Mod):
    A = trans(Obj.conns['A'])
    B = trans(Obj.conns['B'])
    C = trans(Obj.conns['C'])
    S0 = trans(Obj.conns['S0'])
    S1 = trans(Obj.conns['S1'])
    Y = Obj.conns['Y']
    Mod.hard_assigns.append((Y,('?',S1,C,('?',S0,B,A)),'',''))
    return True

def mx4x1(Obj,Mod):
    A = trans(Obj.conns['A'])
    B = trans(Obj.conns['B'])
    C = trans(Obj.conns['C'])
    D = trans(Obj.conns['D'])
    S0 = trans(Obj.conns['S0'])
    S1 = trans(Obj.conns['S1'])
    Y = Obj.conns['Y']
    Mod.hard_assigns.append((Y,('?',S1,('?',S0,D,C),('?',S0,B,A)),'',''))
    return True

def getQ(Pin,Obj,Mod,MakeReg=True):
    if Pin not in Obj.conns: return ''
    Q = Obj.conns[Pin]
    logs.log_info('getQ %s=%s  %s %s'%(Pin,Q,Obj.Name,Obj.Type))
    if MakeReg:
        if type(Q) is str:
            if Q not in Mod.nets:
                Mod.nets[Q] = 'reg',0
            elif 'output' in Mod.nets[Q]:
                Mod.nets[Q] = 'output reg',0
            else:
                Mod.nets[Q] = 'reg',0
        elif (Q[0] == 'subbit'):
            Bus = Q[1]
            Ind = eval(Q[2])
            if Bus not in Mod.nets:
                Mod.nets[Bus] = 'reg',(Ind,0)
            elif 'output' in Mod.nets[Bus]:
                _,Wid = Mod.nets[Bus]
                Wid = max(Wid[0],Ind),0
                Mod.nets[Bus] = 'output reg',Wid
            else:
                _,Wid = Mod.nets[Bus]
                Wid = max(Wid[0],Ind),0
                Mod.nets[Bus] = 'reg',Wid
    return Q

def getQandQN(Obj,Mod):
    Q = getQ('Q',Obj,Mod,True)
    QN = getQ('QN',Obj,Mod,Q=='')
    return Q,QN

def dffrx1(Obj,Mod):
    D = trans(Obj.conns['D'])
    CK = trans(Obj.conns['CK'])
    RN = trans(Obj.conns['RN'])
    Cond = ('list', ('edge', 'posedge', CK), ('edge', 'negedge', RN))
    Q,QN = getQandQN(Obj,Mod)

    if (Q=='')and(QN==''):
        logs.log_warning('no Q, QN in dffrx1 %s'%Obj.Name)
        logs.log_info('%s %s' %('Q' in Obj.conns,'QN' in Obj.conns))
        return False

    if (QN==''):
        Mod.alwayses.append((Cond,('ifelse',('!',RN),('<=',Q,0),('<=',Q,D)),'always'))
    elif (Q==''):
        Mod.alwayses.append((Cond,('ifelse',('!',RN),('<=',QN,1),('<=',QN,('!',D))),'always'))
    else:
        Mod.alwayses.append((Cond,('ifelse',('!',RN),('<=',Q,0),('<=',Q,D)),'always'))
        Mod.hard_assigns.append((QN,('!',Q),'',''))
    return True



def dffsx1(Obj,Mod):
    D = trans(Obj.conns['D'])
    CK = trans(Obj.conns['CK'])
    SN = trans(Obj.conns['SN'])
    Q,QN = getQandQN(Obj,Mod)

    Cond = ('list', ('edge', 'posedge', CK), ('edge', 'negedge', SN))
    if (Q=='')and(QN==''):
        logs.log_warning('no Q, QN in dffsx1 %s'%Obj.Name)
        return True

    if (QN==''):
        Mod.alwayses.append((Cond,('ifelse',('!',SN),('<=',Q,1),('<=',Q,D)),'always'))
    elif (Q==''):
        Mod.alwayses.append((Cond,('ifelse',('!',SN),('<=',QN,0),('<=',QN,('!',D))),'always'))
    else:
        Mod.alwayses.append((Cond,('ifelse',('!',SN),('<=',Q,1),('<=',Q,D)),'always'))
        Mod.hard_assigns.append((QN,('!',Q),'',''))
    return True


def dffx1(Obj,Mod):
    D = trans(Obj.conns['D'])
    CK = trans(Obj.conns['CK'])
    Q,QN = getQandQN(Obj,Mod)

    Cond = ('edge', 'posedge', CK)
    if (Q=='')and(QN==''):
        logs.log_warning('no Q, QN in dffx1 %s'%Obj.Name)
        return True

    if (QN==''):
        Mod.alwayses.append((Cond,('<=',Q,D),'always'))
    elif (Q==''):
        Mod.alwayses.append((Cond,('<=',QN,('!',D)),'always'))
    else:
        Mod.alwayses.append((Cond,('<=',Q,D),'always'))
        Mod.hard_assigns.append((QN,('!',Q),'',''))
    return True

def addfx1(Obj,Mod):
    A = trans(Obj.conns['A'])
    B = trans(Obj.conns['B'])
    CI = trans(Obj.conns['CI'])
    if 'CO' in Obj.conns:
        CO = trans(Obj.conns['CO'])
        COfunc = ('|',('&',A,B),('&',A,CI),('&',CI,B))
        Mod.hard_assigns.append((CO,COfunc,'',''))
    if 'S' in Obj.conns:
        S = trans(Obj.conns['S'])
        Sfunc = ('^',A,B,CI)
        Mod.hard_assigns.append((S,Sfunc,'',''))
    return True

KNOWNS['MX2X1'] = ('func',mx2x1)
KNOWNS['MX3X1'] = ('func',mx3x1)
KNOWNS['MX4X1'] = ('func',mx4x1)
KNOWNS['DFFX1'] = ('func',dffx1)
KNOWNS['DFFRX1'] = ('func',dffrx1)
KNOWNS['DFFSX1'] = ('func',dffsx1)
KNOWNS['ADDFX1'] = ('func',addfx1)



