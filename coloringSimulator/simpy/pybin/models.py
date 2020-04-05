
import logs3 as logs

def extract(Obj):
    A,Clr = Obj.vals('a')
    Out,_ = Obj.vals('o')
    Index = 1+int(Obj.Params['index'])
    New = ((32*'0')+A)[-Index]
    if New!=Out:
        return [('o',New,Clr)],[]
    return [],[]
    

def insert(Obj):
    A,Clr = Obj.vals('a')
    Out = Obj.vals('o')[0]
    Index = 1+int(Obj.Params['index'])
    LL = list(Out)
    if len(LL)<Index:
        More = '0'*(Index-len(LL))
        LL = list(More)+LL
        
    LL[-Index] = A
    New = ''.join(LL)
    if New!=Out:
#        print('INSERT',New,Obj.Conns['a'])
        return [('o',New,Clr)],[]
    return [],[]

    
def and2(Obj):
    A,Colsa = Obj.vals('a')
    B,Colsb = Obj.vals('b')

    Bsig = Obj.Conns['b']

    if (A=='1')and(B=='1'):
        Out = '1'
        Colo = mergeColors(Colsa,Colsb)
    elif (A=='0'):
        Out = '0'
        Colo = Colsa
    elif (B=='0'):
        Out = '0'
        Colo = Colsb
    elif (A=='1'):
        Out = 'x'
        Colo = Colsb
    elif (B=='1'):
        Out = 'x'
        Colo = Colsa
    else: # both unknown
        Out = 'x'
        Colo = mergeColors(Colsa,Colsb)

    if Out!=Obj.vals('o'):
        Colo = Obj.addVdd(Colo)
        return [('o',Out,Colo)],[]
    return [],[]

def and3(Obj):
    A,Colsa = Obj.vals('a')
    B,Colsb = Obj.vals('b')
    C,Colsc = Obj.vals('c')

    if (A=='1')and(B=='1')and(C=='1'):
        Out = '1'
        Colo = mergeColors(Colsa,Colsb)
        Colo = mergeColors(Colo,Colsc)
    elif (A=='0'):
        Out = '0'
        Colo = Colsa
    elif (B=='0'):
        Out = '0'
        Colo = Colsb
    elif (C=='0'):
        Out = '0'
        Colo = Colsc
    elif (A=='1'):
        Out = 'x'
        Colo = Colsb
    elif (B=='1'):
        Out = 'x'
        Colo = Colsc
    elif (C=='1'):
        Out = 'x'
        Colo = Colsa
    else: # both unknown
        Out = 'x'
        Colo = mergeColors(Colsa,Colsb)
        Colo = mergeColors(Colo,Colsc)

    if Out!=Obj.vals('o'):
        Colo = Obj.addVdd(Colo)
        return [('o',Out,Colo)],[]
    return [],[]

def or2(Obj):
    A,Colsa = Obj.vals('a')
    B,Colsb = Obj.vals('b')
    if (A=='1')and(B=='1'):
        Out = '1'
        Colo = mergeColors(Colsa,Colsb)
    elif (A=='1'):
        Out = '1'
        Colo = Colsa
    elif (B=='1'):
        Out = '1'
        Colo = Colsb
    elif (A=='0')and(B=='0'):
        Out = '0'
        Colo = mergeColors(Colsa,Colsb)
        Colo = Obj.addVdd(Colo)
    elif (A in ['x','z']):
        Out = 'x'
        Colo = Colsa
    else:
        Out = 'x'
        Colo = Colsb
    if Out!=Obj.vals('o'):
        return [('o',Out,Colo)],[]
    return [],[]

def or3(Obj):
    A,Colsa = Obj.vals('a')
    B,Colsb = Obj.vals('b')
    C,Colsc = Obj.vals('c')
    if (A=='1')and(B=='1')and(C==1):
        Out = '1'
        Colo = mergeColors(Colsa,Colsb)
        Colo = mergeColors(Colo,Colsc)
    elif (A=='1'):
        Out = '1'
        Colo = Colsa
    elif (B=='1'):
        Out = '1'
        Colo = Colsb
    elif (C=='1'):
        Out = '1'
        Colo = Colsc
    elif (A=='0')and(B=='0')and(C=='0'):
        Out = '0'
        Colo = mergeColors(Colsa,Colsb)
        Colo = mergeColors(Colo,Colsc)
    elif (A in ['x','z']):
        Out = 'x'
        Colo = Colsa
    elif (B in ['x','z']):
        Out = 'x'
        Colo = Colsb
    else:
        Out = 'x'
        Colo = Colsc
    if Out!=Obj.vals('o'):
        Colo = Obj.addVdd(Colo)
        return [('o',Out,Colo)],[]
    return [],[]





def nand2(Obj):
    OO,[] = and2(Obj)
    if OO==[]: return [],[]
    return inverseOut(OO,Obj)

def nand3(Obj):
    OO,[] = and3(Obj)
    if OO==[]: return [],[]
    return inverseOut(OO,Obj)


def nor2(Obj):
    OO,[] = or2(Obj)
    if OO==[]: return [],[]
    return inverseOut(OO,Obj)

def nor3(Obj):
    OO,[] = or3(Obj)
    if OO==[]: return [],[]
    return inverseOut(OO,Obj)

def xnor2(Obj):
    OO,[] = xor2(Obj)
    if OO==[]: return [],[]
    return inverseOut(OO,Obj)

def xnor3(Obj):
    OO,[] = xor3(Obj)
    if OO==[]: return [],[]
    return inverseOut(OO,Obj)


def inverseOut(OO,Obj):
    Pin,Out,Colo = OO[0]
    if Out=='1':
        return [('o','0',Colo)],[]
    elif Out=='0':
        return [('o','1',Colo)],[]
    return [('o','x',Colo)],[]

def xor2(Obj):
    A,Colsa = Obj.vals('a')
    B,Colsb = Obj.vals('b')
    if (A=='x')or(A=='z'):
        Out ='x'
        Colo = Colsa
    elif (B=='x')or(B=='z'):
        Out ='x'
        Colo = Colsb
    elif (A!=B):
        Out = '1'
        Colo = mergeColors(Colsa,Colsb)
    else:
        Out = '0'
        Colo = mergeColors(Colsa,Colsb)
    if Out!=Obj.vals('o'):
        Colo = Obj.addVdd(Colo)
        return [('o',Out,Colo)],[]
    return [],[]

def xor3(Obj):
    A,Colsa = Obj.vals('a')
    B,Colsb = Obj.vals('b')
    C,Colsc = Obj.vals('c')
    if (A=='x')or(A=='z'):
        Out ='x'
        Colo = Colsa
    elif (B=='x')or(B=='z'):
        Out ='x'
        Colo = Colsb
    elif (C=='x')or(C=='z'):
        Out ='x'
        Colo = Colsc
    else:
        X=sum(map(int,[A,B,C]))
        X = X & 1
        Out = str(X)
        Colo = mergeColors(Colsa,Colsb)
        Colo = mergeColors(Colo,Colsc)

    if Out!=Obj.vals('o'):
        Colo = Obj.addVdd(Colo)
        return [('o',Out,Colo)],[]
    return [],[]


def inv(Obj):
    A,Colsa = Obj.vals('a')
    if (A=='1'):
        Out = '0'
    elif (A=='0'):
        Out = '1'
    else:
        Out = 'x'
    if Out!=Obj.vals('o'):
        Colsa = Obj.addVdd(Colsa)
        return [('o',Out,Colsa)],[]
    return [],[]

def buf(Obj):
    A,Colsa = Obj.vals('a')
    if A!=Obj.vals('o'):
        Colsa = Obj.addVdd(Colsa)
        return [('o',A,Colsa)],[]
    return [],[]


def dff(Obj):
    Edge,ColsClk = Obj.posedge('clk')
    if Edge:
        D,Colsd = Obj.vals('d')
        Q,_ = Obj.vals('q')
        if D!=Q:
            _,ColsClk = Obj.vals('clk')
            Colq = mergeColors(ColsClk,Colsd)
            Colq = Obj.addVdd(Colq)
            return [],[('q',D,Colq)]
    return [],[]

def dffr(Obj):
    Rb,Colsr = Obj.vals('rb')
    if Rb=='0':
        if '0'!=Obj.vals('q'):
            return [('q','0',Colsr)],[]
        return [],[]
    Edge,ColsClk = Obj.posedge('clk')
    if Edge:
        D,Colsd = Obj.vals('d')
        Q,_ = Obj.vals('q')
        if D!=Q:
            Colq = mergeColors(ColsClk,Colsd)
            Colq = Obj.addVdd(Colq)
            return [],[('q',D,Colq)]
    return [],[]


def python_func(Obj):
    if not Obj.Func:
        Func = Obj.Params['func']
        Func0 = eval('Obj.db.Script.%s'%Func)
        Obj.Func = Func0
    return Obj.Func(Obj)            

def ram(Obj):
    Clk = Obj.Conns['clk']
    Edge,ColClk = Obj.db.Nets[Clk].posedge()
    Res = [],[]
    if Edge:
        if 'QQ' in Obj.Context:
            Res =  [('q',Obj.Context.pop('QQ'),ColClk)],[]

        cs,Colscs = Obj.vals('cs')
        if cs=='1':
            add,Colsa = Obj.vals('a')
            A = logs.intx(add)
            we,Colswe = Obj.vals('we')
            if we=='1':
                din,Colsd = Obj.vals('d')
                D = logs.intx(din)
                Obj.Context[A]=D
                logs.log_info('ram cswr ad=%d data=%d '%(A,D))
            elif we=='0':
                if A in Obj.Context:
                    QQ = bin(Obj.Context[A])[2:]
                else:
                    QQ = 'x'
                logs.log_info('ram csrd ad=%d data=%s %s'%(A,QQ,Obj.Context))
                Obj.Context['QQ']=QQ 

    return Res
    

def mux2(Obj):
    sel,ColsSel = Obj.vals('sel')
    a,Colsa = Obj.vals('a')
    b,Colsb = Obj.vals('b')
    if sel=='1':
        Out,Colo0 = a,Colsa
    elif sel=='0':
        Out,Colo0 = b,Colsb
    elif (a==b):
        Out,Colo0 = a,Colsa
    else:
        Out,Colo0 = 'x',ColsSel

    if Out != Obj.vals('o')[0]:
        Colo = mergeColors(Colo0,ColsSel)
        Colo = Obj.addVdd(Colo)
        return [('o',Out,Colo)],[]

    return [],[]

Models = {}
Models['insert']=insert
Models['extract']=extract
Models['ram']=ram
Models['mux2']=mux2
Models['and2']=and2
Models['python']=python_func
Models['or2']=or2
Models['nand2']=nand2
Models['nor2']=nor2
Models['xnor2']=xnor2
Models['xor2']=xor2
Models['inv']=inv
Models['buf']=buf
Models['dff']=dff
Models['dffr']=dffr
Models['or3']=or3
Models['and3']=and3
Models['nor3']=nor3
Models['nand3']=nand3
Models['xor3']=xor3
Models['xnor3']=xnor3

def findOutDir(Type,Pin): 
    if Pin[0] in ['o','q','z']: return 'output'
    if Pin[0] in ['a','b','c','i','s','w']: return 'input'
    logs.log_error('findOutDir %s %s'%(Type,Pin))
    return 'input'

def makeList(Item):
    if type(Item) is list: return Item
    return [Item]

def llist(Color):
    if not Color: return []
    return list(Color.keys())

def mergeColors(Color0,Color1):
    Merge={}
    if not Color0: return Color1
    if not Color1: return Color0
    Keys = llist(Color0)+llist(Color1)
    Bag = set(Keys)
    for Key in Bag:
        if (Key in Color0)and(Key in Color1):
            Clks = makeList(Color0[Key])+makeList(Color1[Key])
            Clks.sort()
            if Key=='clk':
                Found={}
                for Clk,Cycle in Clks:
                    if Clk not in Found:
                        Found[Clk]=Cycle
                    else:
                        Found[Clk] = max(Cycle,Found[Clk])
                LL = []
                for Clk in Found:
                    LL.append((Clk,Found[Clk]))
                Merge['clk']=LL                    
            elif Key=='color':
                Clrs = list(set(Clks))
                Merge['color']=Clrs                    
            else:
                Clrs = list(set(Clks))
                Merge['Key']=Clrs                    
                
        elif (Key in Color0):
            Merge[Key]=Color0[Key]
        elif (Key in Color1):
            Merge[Key]=Color1[Key]
    return Merge

def simple(Val):
    return (type(Val) is int)or(type(Val) is str)

