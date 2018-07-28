
import sys,types,string
Errors = 0   
Corrects = 0   
Wrongs = 0   
Warnings = 0   
print_debug_messages=0
MAXWRONGS = 2000
MAXERRORS = 2000
PYMONLOG = 'pymon.log'

import time
printed_already={}

Flog = False
Flog2 = False
Flog3 = False
Flog4 = False

try:
    import veri
except:
    import fakeVeri as veri

finishCycles = 0

def get_cycles():
    Now =  peek('tb.cycles')
    if (finishCycles>0)and(finishCycles<=Now):
        veri.finish()

    return Now


def please_print_debugs():
    global print_debug_messages
    print_debug_messages=1

def log_time(Why):
    log_info('info: %s                                 time=%s'%(Why,time.ctime()))

def log_fatal(Text):
    print 'FATAL error!! %s'%(Text)
    log_ending('from fatal')
    sys.exit()

def log_error(Text,Tb=True):
    log_err(Text,Tb)
def log_err(Text,Tb=True):
    global Errors,printed_already,Flog
    if (not Flog):
        Flog=open(PYMONLOG,'w')
    Errors +=1  
    Flog.write('@%d: %d ERROR: %s\n'%(get_cycles(),Errors,Text))
    if Tb:
        veri.force('tb.errors',str(Errors))


    if (Errors>MAXERRORS):
        log_info('max errors reached (%d). bailing out. (MAXERRORS==%d)'%(Errors,MAXERRORS))
        veri.finish()
        sys.exit()   # in icarus, sometimes finish doesnt catch

    if (Text in printed_already):
        return
    printed_already[Text]=1
    print '@%d: %d: ERROR: %s'%(get_cycles(),Errors,Text)

def log_correct(Text,Print=True):
    global Corrects,Flog
    if (not Flog):
        Flog=open(PYMONLOG,'w')
    Corrects += 1
    veri.force('tb.corrects',str(Corrects))
    if Print:
        print '@%d: %d vs %d (err=%d) CORRECT: %s'%(get_cycles(),Corrects,Wrongs,Errors,Text)
    Flog.write('@%d: %d vs %d (err=%d) CORRECT: %s\n'%(get_cycles(),Corrects,Wrongs,Errors,Text))

def log_ensure(Cond,Text):
    if Cond:
        log_correct(Text)
    else:
        log_wrong(Text)
    
def log_wrong(Text):
    global Wrongs,Flog
    Wrongs += 1
    veri.force('tb.wrongs',str(Wrongs))
    if (not Flog):
        Flog=open(PYMONLOG,'w')
    print '@%d: %d vs %d (err=%d): WRONG: %s'%(get_cycles(),Wrongs,Corrects,Errors,Text)
    Flog.write('@%d: %d vs %d (err=%d): WRONG: %s\n'%(get_cycles(),Wrongs,Corrects,Errors,Text))
    if Wrongs >= MAXWRONGS:
        log_info('max wrongs reached (%d). bailing out. (MAXWRONGS==%d)'%(Wrongs,MAXWRONGS))
        veri.finish()
        sys.exit()   # in icarus, sometimes finish doesnt catch

def finish(Text='.'):
    print '@%d: wrongs=%d vs corrects=%d errors=%d warnings=%d: FINISHING on %s'%(get_cycles(),Wrongs,Corrects,Errors,Warnings,Text)
    Flog.write('@%d: wrongs=%d vs corrects=%d errors=%d warnings=%d: FINISHING on %s'%(get_cycles(),Wrongs,Corrects,Errors,Warnings,Text))
    veri.finish()
    


def log_warning(Text):
    global Warnings,printed_already,Flog
    if (Text in printed_already):
        return
    if (not Flog):
        Flog=open(PYMONLOG,'w')
    print '%d: warning: %s'%(Warnings,Text)
    Flog.write('%d: warning: %s\n'%(Warnings,Text))
    printed_already[Text]=1
    Warnings +=1  

def log_info(Text):
    global Flog
    if (not Flog):
        Flog=open(PYMONLOG,'w')
    print '@%d: info: %s'%(get_cycles(),Text)
    Flog.write('@%d: info: %s\n'%(get_cycles(),Text))


def log_info2(Text):
    global Flog2
    if (not Flog2):
        Flog2=open(PYMONLOG+'2','w')
    Flog2.write('@%d:     %s\n'%(get_cycles(),Text))

def log_info3(Text):
    global Flog3
    if (not Flog3):
        Flog3=open(PYMONLOG+'3','w')
    Flog3.write('@%d:     %s\n'%(get_cycles(),Text))

def log_info4(Text):
    global Flog4
    if (not Flog4):
        Flog4=open(PYMONLOG+'4','w')
    Flog4.write('@%d:     %s\n'%(get_cycles(),Text))



def log_dbg(Text):
    if (print_debug_messages):
        print 'dbg: ',Text

def log_ending(Who):
    log_time('%s.py has %d errors, %d wrongs,  %d corrects and %d warnings logged\n\n'%(Who,Errors,Wrongs,Corrects, Warnings))
    if (Flog):
        Flog.close()
    return Errors



params={}
def get_param(Param,Default):
    if Param in params:
        return params[Param][0]
    return Default
def parse_args():
    global params
    fnames=[]
    state='idle'
    for X in sys.argv[1:]:
        if (state=='idle'):
            if (X[0]=='-'):
                state='param'
                Param = X 
            else:
                fnames += [X]
        elif (state=='param'):
            if (X[0]=='-'):
                params[Param]='yes'
                state='param'
                Param = X 
            else:
                state='idle'    
                if (Param in params):
                    params[Param] += [X] 
                else:
                    params[Param]=[X]
    if (state=='param'):
        params[Param]='yes'
    params['fnames']=fnames 
    return params


def startsWith(Long,Short):
    if type(Long)!=types.StringType: return False
    if Short not in Long: return False
    return  Long.index(Short)==0 

def intx(Val):
    if type(Val)==types.IntType: return Val
    if type(Val)==types.LongType: return Val
    if type(Val)==types.FloatType: return Val
    if Val=='-999': return -1
    if 'x' in Val: return -1
    if 'z' in Val: return -1
    if 'q' in Val: return -1
    return int(Val,2)

def peek(Sig):
    V  = intx(veri.peek(Sig))
    return V

def peeksigned(Sig):
    Str = veri.peek(Sig)
    X = intx(Str)
    if 'x' in Str: return 9999
    if 'z' in Str: return 9999
    if Str[0]=='0': return X
    if len(Str)==1: return X
    Base = 1<<len(Str)
    Res = X-Base
    return Res

def make_str(Int):
    Y = bin(Int)
    return Y

def bin8(Int):  
    X = bin(Int)[2:]
    while len(X)<8:
        X = '0'+X
    return X

def asciiForce(Sig,Str):
    res = '0b'
    for Chr in Str:
        Ord = ord(Chr)
        Bin = bin8(Ord)
        res += Bin
    veri.force(Sig,res)



   
    
def float2int(Float):
    if Float== -1: return -1
    if ((Float & 0x7fffffff)==0): return 0

    Bin = bin(Float)[2:]
    if len(Bin)<32:
        Bin = (32-len(Bin))*'0'+Bin
       
    Sign = int(Bin[0],2)
    Exp0  = int(Bin[1:9],2)
    Exp  = Exp0-127
    Mant = int('1'+Bin[9:],2)
    Shift  = Exp-23
    if Shift>0:
        Int = Mant<<Shift
    else:
        Int = Mant>>(-Shift)
    if Sign:
        Int = -Int
    return Int 



def binary2float(Float):
    if Float<0: return 0
    if Float==0: return 0
    Bin = bin(Float)[2:]
    if len(Bin)<32:
        Bin = (32-len(Bin))*'0'+Bin
    Sign = int(Bin[0],2)
    Exp0  = int(Bin[1:9],2)
    Exp  = Exp0-127
    Mant = 1.0*int('1'+Bin[9:],2)
    Shift  = Exp-23



    if Shift>0:
        Int = Mant* (1<<Shift)
    else:
        Int = Mant/(1<< -Shift)
    if Sign:
        Int = -Int
    return Int 



def float2binary(X):
    XX = int(X * (1<<24))
    XXX = int2float2(XX)
    Exp0 = (XXX & 0x7f800000)>>23
    if Exp0<24:
        return 0
    Exp1 = Exp0 - 24
    YYY = (XXX & 0x807fffff)| (Exp1<<23)
    return YYY 


def int2float2(Int):
    if Int==0:
        return 0
    sign0 = int(Int<0)
    Abs = int(abs(Int))
    Bin = bin(Abs)[2:]
    Len = len(Bin)
    Mant = Bin[1:]
    if len(Mant)>23:
        Mant = Mant[:23]
    elif len(Mant)<23:
        Mant = Mant+'0'*(23-len(Mant))

    Exp0 = Len-1
    Exp = 0x7f+Exp0
    bexp = '00000000'+bin(Exp)[2:]
    Bexp = bexp[-8:]

    Big = '0b'+str(sign0)+Bexp+Mant
    return int(Big,2)




def panicFinish(Reason,ContinueFor=20):
    global finishCycles
    finishCycles = get_cycles()+ContinueFor
    log_error('finishCycle activated because of "%s"'%(Reason))


      
def finishing(Txt='"not given"'):
    log_info('finishing on %s'%Txt)
    veri.finish()

Vars = {}
def incr(Who,By=1):
    if Who not in Vars:
        Vars[Who]=0
    Vars[Who] += By
    return Vars[Who]

def vars(varName,Value,Clear=False):
    if Clear and (varName in Vars):
        Vars.pop(varName)
        
    if startsWith(varName,'list'):
        if varName not in Vars:
            Vars[varName]=[Value]
        else:
            Vars[varName].append(Value)
    else:
        Vars[varName]=Value
    


def gatherPanicNets(deepListFname):
    File = open(deepListFname)
    List=[]
    while True:
        line  = File.readline()
        if line=='': return List
        wrds = string.split(line)
        if len(wrds)>0:
            if wrds[0]=='module:':
                Path = wrds[2]
            elif wrds[0]=='net:':
                Net = wrds[1]                
                if '.' in Net:
                    www = string.split(Net,'.')
                    Last = www[-1]
                    if startsWith(Last,'panic'):
                        List.append(Net)
                else:
                    if startsWith(Net,'panic'):
                        List.append('%s.%s'%(Path,Net))
                        

def getValues(Path,Str,Hex=True,Signed=False):
    wrds = string.split(string.replace(Str,',',' ')) 
    res = ''
    resi = []
    resd = {}
    for wrd in wrds:
        if Signed:
            Val = peeksigned('%s.%s'%(Path,wrd))
        else:
            Val = peek('%s.%s'%(Path,wrd))
        resi.append(Val)
        resd[wrd]=Val
        if Hex=='float':
            res += ' %s=%f'%(wrd,binary2float(Val))
            resd[wrd]=binary2float(Val)
        elif Hex:
            res += ' %s=%x'%(wrd,Val)
        else:
            res += ' %s=%d'%(wrd,Val)
    return res,resi,resd
    

def parseVars(Str):
    wrds = string.split(Str)
    Res={}
    for wrd in wrds:
        if '=' in wrd:
            ww = string.split(wrd,'=')
            if len(ww)==2:
                Res[ww[0]]=ww[1]
    return Res

def countOnes(Val):
    Bin = bin(Val)[2:]
    cnt=0
    for X in Bin:
        if X=='1': cnt += 1
    return cnt


def closeEnough(AA,BB,Epsilon=0.0001):
    if AA==BB: return True

    AA0 = abs(AA)*Epsilon


    Diff = abs(AA-BB)
    if Diff<Epsilon: return True
    if (abs(BB)<Epsilon)and(abs(AA)<Epsilon): return True
    if (abs(BB)<Epsilon)and(abs(AA)>Epsilon): return False
    if (abs(BB)>Epsilon)and(abs(AA)<Epsilon): return False

    Diff = abs(abs(AA/BB)-1.0)
    if Diff<Epsilon: return True

    return False


def fixedp(Int,Shift):
    X = 1<<Shift
    Res = 1.0 * Int /X
    return Res

def bin2str(Bin):
    res =''
    while len(Bin)>=8:
        Chr1 = Bin[-8:]
        Bin  = Bin[:-8]
        if 'x' in Chr1:
            return res
        Int = int(Chr1,2)
        if Int==0: return res
        Chr = chr(Int)
        res = Chr + res
    return res

print '>>>verification_logs loaded'

