
def funcify(Func,Trans={}):
    Func1= Func.replace('"','')
    for Char in '^()+*!&|':
        Func1 = Func1.replace(Char,' %s '%Char)
    Func2 = Func1.strip()
    wrds = Func2.split()


    guard = 100
    while ')' in wrds:
        guard -= 1
        if (guard<=0):
            print('ilia too much guard wrds=%s'%(str(wrds)))
            sys.exit()
        ind1 = wrds.index(')')
        ind0 = ind1-1
        while wrds[ind0]!='(':
            ind0 -= 1
        part = wrds[ind0+1:ind1]
        part = overwork(part)
        bef = wrds[:ind0]
        aft = wrds[ind1+1:]
        wrds = bef + [part] + aft

    res = []
    for wrd in wrds:
        if (wrd[-1]=="'")and(len(wrd)>1):
            res.append('!')
            res.append(wrd[:-1])
        else:
            res.append(wrd)
    wrds = res[:]
    wrds = replace_ticks(wrds)


    wrds = overwork(wrds)
    wrds = gather_nots(wrds)
    wrds = flat_list(wrds)
    res=[]
    for wrd in wrds:
        if wrd in Trans:
            res.append('d_%s'%wrd)
        else:
            res.append(wrd)
            
    Str = ' '.join(res)
    return Str

def gather_nots(wrds):
    if type(wrds) is str: return wrds
    res=[]
    Skip=False
    for ind,wrd in enumerate(wrds):
        if Skip:
            Skip=False
        elif wrd=='!':
            part = gather_nots(wrds[ind+1])
            res.append(['!',part])
            Skip=True
        elif type(wrd) is list:
            part = gather_nots(wrd)
            res.append(part)
        else:
            res.append(wrd)
            Skip=False
    if (type(res) is list)and(len(res)==1):
        return res[0]
    return res

def replace_ticks(wrds):
    res = []
    for wrd in wrds:
        if type(wrd) is list:
            wrd2 = replace_ticks(wrd)
            res.append(wrd2)
        elif (wrd[-1]=="'")and(len(wrd)>1):
            New = [ '!',wrd[:-1]]
            res.append(New)
        elif (wrd=="'"):
            Last = res.pop(-1)
            New = [ '!',Last]
            res.append(New)
        else:
            res.append(wrd)
    return res[:]

def flat_list(wrds):
    if type(wrds) is str:
        return [wrds]
    ind = 0
    res = []
    while wrds!=[]:
        pp = wrds.pop(0)
        if type(pp) is list:
            wrds = ['(']+pp+[')']+wrds
        else:
            res.append(pp)
    return res


def overwork(part):
    ind=1
    while ind<len(part):
        Var = part[ind]
        if Var == '+':
            part[ind]='||'
        elif Var == '&':
            part[ind]='&&'
        elif Var == '|':
            part[ind]='||'
        elif Var == '*':
            part[ind]='&&'
            
        if (ind>0) and (is_var(Var) or (Var=='!')):
            Prev = part[ind-1]
            if not is_oper(Prev):
                part = part[:ind]+['&&']+part[ind:]
        ind +=1        
    return part
            
        
Letters = 'qwertyuiopasdfghjklzxcvbnm'
Letters += 'QWERTYUIOPASDFGHJKLZXCVBNM'
Opers = '+*||&&^!'    

def  is_var(Var):
    if (type(Var) is str)and(Var[0] in Letters):
        return True
    if (type(Var) is list):
        return True
    return False
        
def is_oper(Var):
    if (type(Var) is str)and(Var[0] in Opers):
        return True
    return False

def edged(Func):
    for Char in '()':
        Func = Func.replace(Char,'')
    wrds = Func.split()
    if len(wrds)==1:
        return 'posedge %s'%wrds[0]
    if (len(wrds)==2)and(wrds[0]=='!'):
        return 'negedge %s'%wrds[1]
    Wire = invent_wire_name()
    Wires.append('wire %s = %s;\n'%(Wire,Func))
    return 'posedge %s'%Wire



def match_table(VV,LL,Cell):
    res = [] 
    ind=0
    ptr=0
    while ind<len(VV):
        Var = VV[ind]
        Sym = LL[ind]
        if Sym=='H':
            res.append(Var)
        elif Sym=='L':
            res.append('!%s'%Var)
        elif Sym=='-':
            pass 
        elif Sym=='N':
            pass 
        else:
            print('error!! cell=%s match table vv=%s ll=%s ind=%s sym=%s'%(Cell,VV,LL,ind,Sym))

        ind+=1
    X = '&&'.join(res)    
    if LL[-1]=='H':
        Y = '1'
    elif LL[-1]=='L':
        Y = '0'
    elif LL[-1]=='N':
        Y = VV[-1]
        Y = False
    elif LL[-1]=='-':
        Y = VV[-1]
        Y = False
        Y = False
    elif LL[-1]=='X':
        Y="1'bx"
    else:
        print('error! cell=%s LL=%s last one is not in set. vv=%s'%(Cell,LL,VV))
        Y = "1'bx"
    return X,Y



def pythonizeFunc(Func):
    ww = Func.split()
    ww1 = bracketize(ww)
    while (len(ww1)==1)and(type(ww1) is list):
        ww1=ww1[0]
    FF = pythonize2(ww1)
    return FF

def pythonize2(ww):
    if type(ww) is str:
        return 'getPinVal(self,[%s])'%(ww)

    if len(ww)==3:
        A = pythonize2(ww[0])
        B = pythonize2(ww[2])
        Func = '%s(%s,%s)'%(py_op(ww[1]),A,B)
        return Func
    if len(ww)==1:
        return 'self.pinMsg["%s"]'%(ww[0])
    if len(ww)==2:
        A = pythonize2(ww[1])
        return '%s(%s)'%(py_op(ww[0]),A)

    if (len(ww)>4)and(ww[1]==ww[3]):
        x1 = pythonize2(ww[:3])
        ind = 3
        while ind<len(ww):
            x1 = '%s(%s,%s)'%(py_op(ww[ind]),x1,pythonize2(ww[ind+1]))
            ind += 2
        return x1

    print('error! %s'%str(ww))
    return 'err'


def py_op(Op):
    if Op=='^': return 'msg_xor'
    if Op=='!': return 'msg_not'
    if Op=='|': return 'msg_or'
    if Op=='||': return 'msg_or'
    if Op=='&': return 'msg_and'
    if Op=='&&': return 'msg_and'
    print( 'pyop error! %s'%(Op))
    return 'xxx'



def bracketize(List):
    queue=[]
    curr=[]
    for X in List:
        if X=='(':
            queue.append(curr[:])
            curr=[]
        elif X==')':
            Last = queue.pop(-1)
            Last.append(curr)
            curr = Last[:]
        else:
            curr.append(X)
    return curr



def clean_it(Txt):
    if (Txt[0]=='(')and(Txt[-1]==')'):
        Txt = Txt[1:-1]
    while Txt[0]==' ':
        Txt = Txt[1:]
    while Txt[-1]==' ':
        Txt = Txt[:-1]
    return Txt 
 



def match_table(VV,LL,Cell):
    res = []
    ind=0
    ptr=0
    while ind<len(VV):
        Var = VV[ind]
        Sym = LL[ind]
        if Sym=='H':
            res.append(Var)
        elif Sym=='L':
            res.append('!%s'%Var)
        elif Sym=='-':
            pass
        elif Sym=='N':
            pass
        else:
            print('error!! cell=%s match table vv=%s ll=%s ind=%s sym=%s'%(Cell,VV,LL,ind,Sym))

        ind+=1
    X = '&&'.join(res)    
    if LL[-1]=='H':
        Y = '1'
    elif LL[-1]=='L':
        Y = '0'
    elif LL[-1]=='N':
        Y = VV[-1]
        Y = False
    elif LL[-1]=='-':
        Y = VV[-1]
        Y = False
        Y = False
    elif LL[-1]=='X':
        Y="1'bx"
    else:
        print('error! cell=%s LL=%s last one is not in set. vv=%s'%(Cell,LL,VV))
        Y = "1'bx"
    return X,Y
