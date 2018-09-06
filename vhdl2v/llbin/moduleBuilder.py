
import os,sys,string,types
NewName = os.path.expanduser('~')
sys.path.append('%s/pybin3'%NewName)

import module_class
import logs
import pacifierVerilog
import matches

MODULES={}
Current = False

def info(Str):
    logs.log_info(Str)


def addModule(Name):
    global Current
    Name = string.lower(Name)
    if Name not in MODULES:
        MODULES[Name] = module_class.module_class(Name)
    Current = MODULES[Name]

def addModuleParam(Name,Val):
    Current.parameters[string.lower(Name)]=Val

def addWire(Name,Dir,From=0,To=0):
    Dir = verilogDir[Dir]
    Name = string.lower(Name)

    if (type(From)==types.ListType)and(len(From)==1):
        From=From[0]

    Vars = matches.matches(From,('array', ('range', '?', '?'), ('std_logic_vector', ('?', '?'))))
    if Vars:
        Wid = ('double', (Vars[2], Vars[3]), (Vars[0], Vars[1]))
        Current.nets[Name] = (Dir,Wid)
        return
        

    if From==0:
        Current.nets[Name] = (Dir,0)
        return

    if type(From)==types.TupleType:
        From,To = From
        Current.nets[Name] = (Dir,(From,To))
        return
        
    if From=='std_logic':
        Current.nets[Name] = (Dir,0)
        return
        
    if type(From)==types.ListType:
        if From[1]=='std_logic_vector':
            From = From[2]
            
        if From[0]==':':
            Current.nets[Name] = (Dir,(From[1],From[2]))
            return
    if From=='integer':
        From,To = 31,0


    try:
        X = From+To
    except:
        logs.log_error('addWire got from=%s to=%s'%(From,To))
        Current.nets[Name] = (Dir,(777,777))
        return
        

    if (From+To)==0:
        Current.nets[Name] = (Dir,0)
    else:
        Current.nets[Name] = (Dir,(From,To))



DEPTH = 0
def addSeq(What):
    GROW.append((DEPTH,What))
    
def pushIt():
    global DEPTH
    DEPTH += 1
def popIt():
    global DEPTH
    DEPTH -= 1


def addSoftAssign(Dst,Src):
    if Src[0] == '"':
        Src = Src[1:-1]
        Src = ['bin',len(Src),Src]
    addSeq(('<=',Dst,Src))

def addHardAssign(Dst,Src):
    if Src[0] == '"':
        Src = Src[1:-1]
        Src = ['bin',len(Src),Src]
    Src = reworkExpr(Src)
    Dst = reworkExpr(Dst)
    Current.add_hard_assign(Dst,Src)

def addInstance(Inst,Type):
    Current.add_inst(Type,Inst)
def add_instance_param(Inst,Param,Val):
    Current.add_inst_param(Inst,Param,Val)
def add_conn(Inst,Pin,Sig):
    Current.add_conn(Inst,Pin,Sig)


def addAlways(Always):
    A0 = Always[0]
    A1 = Always[1]
    A2 = reworkExpr(A1)
    Current.alwayses.append([A0,A2,Always[2]])



def dumpVerilog(Fname='modulevhd'):
    Fout = open('%s.v'%Fname,'w')
    for Mod in MODULES:
        pacifierVerilog.pacifier(MODULES[Mod])
        MODULES[Mod].dump()
        MODULES[Mod].dump_verilog(Fout)
    Fout.close()

GROW  = []
def getSequence():
    global GROW,DEPTH
    RES = rework_process(GROW[:])
    GROW=[]
    DEPTH = 0
    return RES

def rework_process(List):
    CACHE = {}
    Level = 0
#    for (Lvl,Stmnt) in List:
#        info('lvl %s %s'%(Lvl,Stmnt))
    for (Lvl,Stmnt) in List:
        if Lvl not in CACHE: CACHE[Lvl]=[]
        if Lvl==Level:
            CACHE[Lvl].append(Stmnt)
#            info('go lvl=%s level=%s stmtn=%s %s'%(Lvl,Level,Stmnt,CACHE))
        elif (Lvl>Level):
            CACHE[Lvl].append(Stmnt)
#            info('down lvl=%s level=%s stmtn=%s %s'%(Lvl,Level,Stmnt,CACHE))
            Level = Lvl
        elif (Lvl<Level):
            Was = ['list']+CACHE.pop(Level)
#            info('up was=%s'%str(Was))
            Level = Lvl
            Bef = list(CACHE[Lvl][-1])
#            info('up bef=%s'%str(Bef))
            Aft = Bef.append(Was)
#            info('up aft=%s'%str(Bef))
            CACHE[Lvl][-1] = Bef
#            info('up lvl=%s level=%s stmtn=%s %s'%(Lvl,Level,Stmnt,CACHE))
    info('CACHE0 %s'%str(CACHE))        
    while Level!=0:
        Was = CACHE.pop(Level)
        Level -= 1
        Bef = CACHE[Level][-1]
        CACHE[Level][-1] = [Bef,Was]
    info('CACHE1 %s'%str(CACHE))        
    Final = CACHE[0]
    info('CACHE2 %s'%str(Final))        
    return ['list']+list(Final)

verilogDir = {'IN':'input','OUT':'output','INOUT':'inout','BUFFER':'output','wire':'wire'
    ,'input':'input','output':'output','wire':'wire'
    ,'reg':'reg'
}
KNOWNOPS = string.split('& && | || ! ~ - + != question > < >= <= * / ')
def reworkExpr(Expr):
    if type(Expr) in [types.StringType,types.IntType]: return Expr
    if (type(Expr)==types.ListType)and(len(Expr)==1):
        return reworkExpr(Expr[0])
    if (type(Expr)==types.TupleType)and(len(Expr)==1):
        return reworkExpr(Expr[0])
    if Expr[0] in KNOWNOPS:
        Res = [Expr[0]]
        for Item in Expr[1:]:
            Fixed = reworkExpr(Item)
            Res.append(Fixed)
        return Res
    if Expr[0] == 'concat':
        AA = reworkExpr(Expr[1])
        BB = reworkExpr(Expr[2])
        if listtuple(AA)and(AA[0]=='curly'):
            return ['curly']+AA[1:]+[BB]
        return ['curly',AA,BB]
    if Expr[0] == 'subbus':
        return Expr
    if Expr[0] == ':=':
        A0 = reworkExpr(Expr[1])
        A1 = reworkExpr(Expr[2])
        return ('<=',A0,A1)
    if Expr[0] == 'assign':
        A0 = reworkExpr(Expr[1])
        A1 = reworkExpr(Expr[2])
        return ('<=',A0,A1)
    if Expr[0] == 'subbit':
        if (type(Expr[2])==types.ListType)and(Expr[2][0]=='funccall'):
            if (Expr[2][1]=='RANGE'):
                Who  = Expr[2][2]
                if Who in Current.nets:
                    _,Wid = Current.nets[Who]
                    if type(Wid)==types.TupleType:
                        return ['subbus',Expr[1],Wid[0],Wid[1]]
            if (Expr[2][1]=='high'):
                Who  = Expr[2][2]
                if Who in Current.nets:
                    _,Wid = Current.nets[Who]
                    if type(Wid)==types.TupleType:
                        return ['subbit',Expr[1],Wid[0]]
            if (Expr[2][1]=='Event'):
                Who  = Expr[2][2]
                return ['functioncall','edge',[Who]]

        return Expr
    if Expr[0] == 'funccall':
        if Expr[1]=='Event':
            return ['functioncall','edge',[Expr[2]]]

    if (type(Expr)==types.ListType):
        Res = []
        for Item in Expr:
            Item2 = reworkExpr(Item)
            Res.append(Item2)
        return Res
    if (type(Expr)==types.TupleType):
        if Expr[0]=='if':
            Cond = reworkExpr(Expr[1])
            Yes = reworkExpr(Expr[2])
            return ['if',Cond,Yes]

        if Expr[0]=='ifelse':
            After = reworkIf(Expr)
            return After

        if Expr[0]=='case':
            Cond = Expr[1]
            Res = []
            Expr2 = Expr[2]
            if Expr2[0]=='list':
                Expr2 = Expr2[1:]
            for Item in Expr2:
                if len(Item)==1: Item = Item[0]
                if Item[0]=='list':
                    Item = Item[1:]
                if  Item[0]=='case':
                    if len(Item)==3:
                        if listtuple(Item[1]) and (len(Item[1])==1): Item[1]=Item[1][0]
                        if Item[1]=='others': Item[1]='default'
                        Case = reworkCaseCond(Item[1])
                        Res.append([Case,reworkExpr(Item[2])])
                    elif len(Item)==2:
                        if Item[1]=='default':
                            Res.append(['default',[]])
                        else:
                            logs.log_error('default item in case "%s"'%(Item))
                    else:
                        logs.log_error('item in case "%s"'%(Item))
                elif  Item[0]=='others':
                    Res.append(['default',reworkExpr(Item[1])])
                else:
                    logs.log_error('case rework got %s %s'%(Item,str(Expr)))
            return ['case',Cond,Res]

    logs.log_error('reworkExpr %d %s %s'%(len(Expr),type(Expr),str(Expr)))
    return Expr



def reworkIf(IF):
    if len(IF)==5:
        Else = IF[4][0][1]
#        info('IFFF5 %s\n   %s\n   %s\n   %s\n   %s\n\n\n'%(IF[0],IF[1],IF[2],IF[3],Else))
        Cond = reworkExpr(IF[1])
        Yes = reworkExpr(IF[2])
        No = reworkExpr(putElse(IF[3],Else))
        After = ['ifelse',Cond,Yes,No]
        return After

    if len(IF)==4:
#        info('IFFF4 %s %s %s %s'%(IF[0],IF[1],IF[2],IF[3]))
        Else = IF[3][0][0]
        if Else=='else':
            Else = IF[3][0][1:]
            Cond = reworkExpr(IF[1])
            Yes = reworkExpr(IF[2])
            No = reworkExpr(Else)
            IF = ['ifelse',Cond,Yes,No]
        if Else=='ifelse':
            Else = IF[3][0]
            Else = ['if',Else[1],Else[2]]
            Cond = reworkExpr(IF[1])
            Yes = reworkExpr(IF[2])
            No = reworkExpr(Else)
            IF = ['ifelse',Cond,Yes,No]
        return IF

    logs.log_error('reworkIf got %d %s'%(len(IF),IF))
    return IF

def putElse(No,Else):
    if len(No)==1: No=No[0]
    if len(No)==4:
        Last = No[3]
        X = putElse(Last,Else)
        return [No[0],No[1],No[2],X]
    
    if len(No)==3:
        return [No[0],No[1],No[2],Else]

    logs.log_error('putElse %d %s'%(len(No),No))
    return No


def was_reworkIf(IF):
    if len(IF)==3: return IF
    info('len=%d IF=%s'%(len(IF),IF))
    if len(IF)==5:
        IFF = ['ifelse',IF[1],IF[2]]
        AA = flattenIFELSE(IF[3])
        BB = IF[4]
        ALL = AA+[BB]
        info('ALL %s'%(str(ALL)))
        Ok=True
        while (len(ALL)>1)and Ok:
            Last= ALL[-1]
            Bef = ALL[-2]
            if (Last[0]=='else')and(Bef[0]=='elsif'):
                New = ['ifelse',Bef[1],Bef[2],Last[1]]
                info('new %s'%str(New))
                ALL.pop(-1)
                ALL.pop(-1)
                ALL.append(New)
                info('newll %s'%str(ALL))
            elif (Last[0]=='ifelse')and(Bef[0]=='elsif'):
                New = ['ifelse',Bef[1],Bef[2],Last]
                info('new %s'%str(New))
                ALL.pop(-1)
                ALL.pop(-1)
                ALL.append(New)
                info('newll %s'%str(ALL))
            else:
                info('bad last0=%s bef0=%s ALL=%s last=%s bef=%s'%(Last[0],Bef[0],str(ALL),Last,Bef))
                Ok=False
            
        info('new ALL %s'%str(ALL))
        IFF.append(ALL)
        return IFF


    if len(IF)==4:
        IFF = ['ifelse',IF[1],IF[2]]
        AA = flattenIFELSE(IF[3])
        ALL = AA
        if ALL[0]=='elsif':
            ALL[0]='if'
            return ALL
        if ALL[0]=='else':
            return ALL[1]
        info('ALL4 %s'%(str(ALL)))
        Ok=True
        while (len(ALL)>1)and Ok:
            Last= ALL[-1]
            Bef = ALL[-2]
            if (Last[0]=='else')and(Bef[0]=='elsif'):
                New = ['ifelse',Bef[1],Bef[2],Last[1]]
                info('new %s'%str(New))
                ALL.pop(-1)
                ALL.pop(-1)
                ALL.append(New)
                info('newll %s'%str(ALL))
            elif (Last[0]=='ifelse')and(Bef[0]=='elsif'):
                New = ['ifelse',Bef[1],Bef[2],Last]
                info('new %s'%str(New))
                ALL.pop(-1)
                ALL.pop(-1)
                ALL.append(New)
                info('newll %s'%str(ALL))
            elif (Last[0]=='elsif')and(Bef[0]=='elsif'):
                NewLast = ['if',Last[1],Last[2]]
                New = ['ifelse',Bef[1],Bef[2],NewLast]
                info('new %s'%str(New))
                ALL.pop(-1)
                ALL.pop(-1)
                ALL.append(New)
            else:
                info('bad4 %s %s %s %s %s'%(Last[0],Bef[0],str(ALL),Last,Bef))
                Ok=False
            
        info('new ALL4 %s'%str(ALL))
        IFF.append(ALL)
        return IFF


    logs.log_error('reworkIf got strange %d "%s"'%(len(IF),IF))
    return IF

def flattenIFELSE(LL):
    if LL[0]=='elsif': return [LL]
    if LL[0]=='else': return LL
    if (len(LL)==2)and(LL[0][0]=='elsif'):
        Seq = LL[1]
        if len(Seq)==2:
            Fseq = flattenIFELSE(Seq)
            return [LL[0]]+Fseq
        elif Seq[0]=='elsif':
            return LL
    logs.log_error('flattenIFELSE got "%s"'%(LL))
    return LL
        
def listtuple(AA):
    return  type(AA) in [types.ListType, types.TupleType]

def reworkCaseCond(Item):
    if listtuple(Item):
        if Item[0]=='|':
            res = []
            for QQ in Item[1:]:
                RR = reworkCaseCond(QQ)
                for XX in RR:
                    res.append(XX)
            return res
    return [Item]


