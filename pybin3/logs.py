
import sys,types,os
import traceback
Errors = 0   
Corrects = 0   
Wrongs = 0   
Warnings = 0   
print_debug_messages=0
print_warning_messages= True
MAXWRONGS = 2000
MAXERRORS = 2000000
PYMONLOG = 'pymon.log'

WHERE = ''

print("VERPY LOGS")    
Flogs = {}


import time
printed_already={}

TB = 'tb'
try:
    import veri
except:
    import fakeVeri as veri

finishCycles = 0


noCycles=False
Cycles=0
def get_cycles():
    global noCycles
    if noCycles:
        return veri.stime()
    else:
        Now =  peek('%s.cycles'%TB)
        if Now<0: noCycles=True
    if (finishCycles>0)and(finishCycles<=Now):
        veri.finish()
        sys.exit()

    return Now

finishReason = False

MODULE = ['none']
def currentModule():
    return MODULE[0]

def setCurrentModule(Module):
    MODULE[0]=Module




def finish(Txt):
    if finishReason:
        finishReason(Txt,Errors,Wrongs,Corrects)
    else:
        log_info('finishing %s with errors=%d wrongs=%d corrects=%d'%(Txt,Errors,Wrongs,Corrects))
        veri.finish()
        sys.exit()

def please_print_debugs():
    global print_debug_messages
    print_debug_messages=1

def log_time(Why,Which=0):
    log_info('info: %s                                 time=%s'%(Why,time.ctime()),Which)

def log_fatal(Text,Which=0):
    log_ending('from fatal',Which)
    log_error('FATAL! %s'%Text,Which,False,True)
    if finishReason:
        finishReason('FATAL! %s'%Text,Errors+1,Wrongs,Corrects)
    sys.exit()


def keep_error(Text):
    NewName = os.path.expanduser('~')
    Fname = '%s/cellar/errors.keep' % NewName
    if not os.path.exists(Fname):
        Fout = open(Fname,'w')
        Fout.write('%s\n' % Text)
        Fout.close()
        return

    Fout = open(Fname,'a')
    Fout.write('%s\n' % Text)
    Fout.close()
    return


def log_error(Text,Which=0,Tb=True,Pstack=False):
    log_err(Text,Which,Tb,Pstack)
ERRS = {}
def log_errx(Kind,Text,Which=0,Tb=True,Pstack=False):
    if Kind not in ERRS:
        ERRS[Kind] = []
    ERRS[Kind].append(Text)
def report_errx(Module):
    Keys = list(ERRS.keys())
    Keys.sort()
    Keys.reverse()
    for Key in Keys:
        List = ERRS[Key]
        for Txt in List:
            log_err('___E%03d  %s    @%s' % (Key,Txt,Module))
    
def log_err(Text,Which=0,Tb=True,Pstack=False):
    global Errors,printed_already
    if (Which not in Flogs):
        Flogs[Which]=open(PYMONLOG+str(Which),'w')
    Errors +=1  
    Flogs[Which].write('@%d: %s %d ERROR: %s\n'%(get_cycles(),WHERE,Errors,Text))
    if Pstack:
        traceback.print_stack(file=Flogs[Which])
        
    if Tb:
        veri.force('%s.errors'%TB,str(Errors))

    Flogs[Which].flush()

    if (Errors>MAXERRORS):
        log_info('max errors reached (%d). bailing out. (MAXERRORS==%d)'%(Errors,MAXERRORS),Which)
        if finishReason:
            finishReason('too many errors',Errors+1,Wrongs,Corrects)
        veri.finish()
        sys.exit()   # in icarus, sometimes finish doesnt catch

    if (Text in printed_already):
        return
    printed_already[Text]=1
    print('@%d: %s %d: ERROR: %s'%(get_cycles(),WHERE,Errors,Text))

def log_correct(Text,Which=0,Print=True):
    global Corrects
    if (Which not in Flogs):
        Flogs[Which]=open(PYMONLOG+str(Which),'w')
    Corrects += 1
    veri.force('%s.corrects'%TB,str(Corrects))
    if Print:
        print('@%d: %d vs %d (err=%d) CORRECT: %s'%(get_cycles(),Corrects,Wrongs,Errors,Text))
    Flogs[Which].write('@%d: %d vs %d (err=%d) CORRECT: %s\n'%(get_cycles(),Corrects,Wrongs,Errors,Text))

def log_ensure(Cond,Text,Which=0):
    if Cond:
        log_correct(Text,Which)
    else:
        log_wrong(Text,Which)
    
def log_wrong(Text,Which=0):
    global Wrongs
    Wrongs += 1
    veri.force('%s.wrongs'%TB,str(Wrongs))
    if (Which not in Flogs):
        Flogs[Which]=open(PYMONLOG+str(Which),'w')
    print('@%d: %d vs %d (err=%d): WRONG: %s'%(get_cycles(),Wrongs,Corrects,Errors,Text))
    Flogs[Which].write('@%d: %d vs %d (err=%d): WRONG: %s\n'%(get_cycles(),Wrongs,Corrects,Errors,Text))
    if Wrongs >= MAXWRONGS:
        log_info('max wrongs reached (%d). bailing out. (MAXWRONGS==%d)'%(Wrongs,MAXWRONGS),Which)
        if finishReason:
            finishReason('too many wrongs',Errors,Wrongs+1,Corrects)
        veri.finish()
        sys.exit()   # in icarus, sometimes finish doesnt catch

def finish_now(Text='.'):
    global Flog
    if (not Flog):
        Flog=open(PYMONLOG,'w')
    Now = veri.stime()
    if (Wrongs==0)and(Errors==0)and(Warnings==0):
        Text =  '@%d: @%d: corrects=%d FINISHING on all good %s'%(get_cycles(),Now,Corrects,Text)
    else:        
        Text =  '@%d: @%d: wrongs=%d vs corrects=%d errors=%d warnings=%d: FINISHING on %s'%(get_cycles(),Now,Wrongs,Corrects,Errors,Warnings,Text)
    print(Text)
    Flog.write(Text+'\n')
    if finishReason:
        finishReason('finish now',Errors,Wrongs,Corrects)
    veri.finish()
    


def log_warning(Text,Which=0):
    global Warnings,printed_already,Flog
    if (Text in printed_already) or not print_warning_messages:
        return
    if (Which not in Flogs):
        Flogs[Which]= open(PYMONLOG+str(Which),'w')
    print('%d: warning: %s'%(Warnings,Text))
    Flogs[Which].write('%d: warning: %s\n'%(Warnings,Text))
    printed_already[Text]=1
    Warnings +=1  
    Flogs[Which].flush()

def log_write(Text,Which=0):
    if Which not in Flogs:
        Flogs[Which]=open(PYMONLOG+str(Which),'w')
#    print('%s'%(Text))
    Flogs[Which].write('%s\n'%(Text))

def log_info(Text,Which=0):
    if Which not in Flogs:
        Flogs[Which]=open(PYMONLOG+str(Which),'w')
    print('@%d: info: %s'%(get_cycles(),Text))
    Flogs[Which].write('@%d: info: %s\n'%(get_cycles(),Text))
    Flogs[Which].flush()

def closeLogs():
    for Which in Flogs:
        Flogs[Which].close()


def log_finfo(Text,File):
    File.write('@%d: info: %s\n'%(get_cycles(),Text))

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

INFOX = {}
def log_infox(Text,Where,Print=False):
    if Where not in INFOX:
        INFOX[Where]=open('pymon.logx%s'%str(Where),'w')
    INFOX[Where].write('@%d:     %s\n'%(get_cycles(),Text))
    if Print:
        print('@%d:     %s\n'%(get_cycles(),Text))


def log_debug(Text):
    log_dbg(Text)
def log_dbg(Text):
    if (print_debug_messages):
        print('dbg: ',Text)

def log_ending(Who,Which=0):
    log_time('%s.py has %d errors, %d wrongs,  %d corrects and %d warnings logged\n\n'%(Who,Errors,Wrongs,Corrects, Warnings),Which)
    return Errors



params={}
def get_param(Param,Default):
    if Param in params:
        return params[Param][0]
    return Default
def parse_args():
    fnames=[]
    state='idle'

    PYVER = sys.argv[0]
    AA = PYVER.split('/')
    AA.pop(-1)
    ExecPath = '/'.join(AA)
    params['execpath'] = ExecPath




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

def endsWith(Long,Short):
    if not(type(Long) is str): return False
    if Short not in Long: return False
    return  Long.index(Short)==(len(Long)-len(Short)) 


def startsWith(Long,Short):
    if type(Long) is str: return False
    if Short not in Long: return False
    return  Long.index(Short)==0 

def intx(Val):
    if type(Val) is int: return Val
    if type(Val) is float: return Val
    if Val=='-999': return -1
    if 'x' in Val: return -1
    if 'z' in Val: return -1
    if 'q' in Val: return -1
    if '-' in Val: return -1
    try:
        return int(Val,2)
    except:
        return int(Val)

def peek(Sig):
    V  = intx(veri.peek(Sig))
    return V
def valid(Sig):
    V  = intx(veri.peek(Sig))
    return V==1

def peekList(List,Prefix,Format='hex'):
    if type(List) is str:
        List = List.split()
    res = ''
    for Sig in List:
        Sig = '%s.%s'%(Prefix,Sig)
        if Format=='signed':
            V = peeksigned(Sig)
        else:
            V = peek(Sig)
        Wrds = Sig.split('.')
        Base = Wrds[-1]
        if Format=='hex':
            Str = ' %s=%s'%(Base,hex(V))
        elif Format=='bin':
            Str = ' %s=%s'%(Base,bin(V))
        else:
            Str = ' %s=%s'%(Base,V)
        res += Str
    return res
        


def peeksigned(Sig):
    Str = veri.peek(Sig)
    return intxsigned(Str)

def intxsigned(Str):
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

def binx(Int,Wid=8):  
    X = bin(Int)[2:]
    Pref = '0'*Wid
    Y = Pref + X
    Z = Y[-Wid:]
    return Z

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



def peek_float(Sig):
    Bin = peek(Sig)
    return binary2float(Bin)


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
    if finishReason:
        finishReason(Reason,Errors,Wrongs,Corrects)


      
def finishing(Txt='"not given"',ContinueFor=20):
    global finishCycles
    if finishCycles>0: return
    log_info('finishing %s with errors=%d wrongs=%d corrects=%d'%(Txt,Errors,Wrongs,Corrects))
    if finishReason:
        finishReason(Txt,Errors,Wrongs,Corrects)
    finishCycles = get_cycles()+ContinueFor

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
        wrds = line.split()
        if len(wrds)>0:
            if wrds[0]=='module:':
                Path = wrds[2]
            elif wrds[0]=='net:':
                Net = wrds[1]                
                if '.' in Net:
                    www = Net.split('.')
                    Last = www[-1]
                    if startsWith(Last,'panic'):
                        List.append(Net)
                else:
                    if startsWith(Net,'panic'):
                        List.append('%s.%s'%(Path,Net))
                        

def getValues(Path,Str,Hex=True,Signed=False):
    Str = Str.replace(',',' ')
    wrds = Str.split() 
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
    wrds = Str.split()
    Res={}
    for wrd in wrds:
        if '=' in wrd:
            ww = wrd.split('=')
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

def bin2string(Bin):
    return bin2str(Bin)

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

def clog2(Num):
    return len(bin(Num))-2

def bothOnes(Int):
    if Int==0: return -1,-1
    Bin = bin(Int)[2:]
    Max = len(Bin)-1
    Lbin = list(Bin)
    Lbin.reverse()
    Min = Lbin.index('1')
    return Max,Min

FINISHES = {}
def finish_deferred(Tag,Count):
    if Tag not in FINISHES:
        FINISHES[Tag]= Count
    else:
        FINISHES[Tag] += Count
    
ALIVES=[]
class aliveHolderClass:
    def __init__(self,Sig,Wait):
        self.Sig = Sig
        self.Wait = Wait
        self.Val = 'x'
        self.finishTime = 100
    def run(self):
        if self.Sig=='timeout':
            if self.Wait<=get_cycles():
                Txt = 'keepSimulationAlive decided to end this simulation, on timeout'
                log_info(Txt)
                if finishReason:
                    finishReason(Txt,Errors,Wrongs,Corrects)
                veri.finish()
            return 0,'timeout'

        Now = veri.peek(self.Sig)
        if Now != self.Val:
            self.Val = Now
            self.finishTime = get_cycles() + self.Wait
#            log_info('advance time %s to %d'%(self.Sig,self.finishTime))
        return self.finishTime,self.Sig
            



def setupKeepSimulationAlive(KEEP_ALIVE):
    Lines = KEEP_ALIVE.split('\n')
    for line in Lines:
        ww = line.split()
        if len(ww)==0:
            pass
        elif len(ww)!=2:
            log_error('lines in keep alive should have two items:  sig waittime "%s"'%line)
        else:
            Sig = ww[0]
            Wait = int(ww[1])
            ALIVES.append(aliveHolderClass(Sig,Wait))


def keepSimulationAlive():
    if ALIVES==[]: return
    When = 0
    Blame = ''
    for Obj in ALIVES:
        This,Who = Obj.run()
        if This>When: Blame=Who
        When = max(When,This)
#    log_info('max when %d cycles %d by %s'%(When,get_cycles(),Blame))
    if When==0: return        
    if When<(get_cycles()-20):
        log_info('keepSimulationAlive decided to end this simulation (%s)'%Blame)
        veri.finish()
        
def fnameCell(Fname):
    wrds = Fname.split('/')
    wrd0 = wrds[-1]
    wrds = wrd0.split('.')
    X = '.'.join(wrds[:-1])
    return X

RemovesLater=[]
def remove_later(Fname):
    RemovesLater.append(Fname)

def use_remove_laters():
    for Fname in RemovesLater:
        os.remove(Fname)

def ensure_dir(Dir):
    if not os.path.exists(Dir):
        os.system('mkdir %s'%Dir)

varValues = {}
def setVar(Var,Val):
    varValues[Var] = Val
    
def getVar(Var):
    if Var in varValues: return varValues[Var]
    return 0
def incrVar(Var):
    A = getVar(Var)
    setVar(Var,A+1)
    return A

def mkdir(Dir):
    if os.path.exists(Dir): return
    os.mkdir(Dir)

def extract_base_name(Fname):
    AA = Fname.split('/')
    BB = AA[-1]
    CC = BB.split('.')
    return CC[0]

def mustKey(Dir,Key,Msg=''):
    if isinstance(Key,(list,tuple)):
        for Ak in Key:
            mustKey(Dir,Ak,Msg)
    elif Key in Dir: return
    log_error('mustKey %s %s failed.  %s '%(Key,Msg,Dir.keys()))

def neededBits(Int):
    Bin = bin(Int)[2:]
    return len(Bin)



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



def record_directory(Fname,SearchDirs):
    wrds = Fname.split('/')
    wrds = wrds[:-1]
    Dir = '/'.join(wrds)
    if (len(Dir)==0):
        Dir = '.'
    if (Dir not in SearchDirs):
        SearchDirs.append(Dir)



class driverClass:
    def __init__(self,Path,Monitors):
        Monitors.append(self)
        self.Path = Path
        self.state='idle'
        self.waiting  = 0 
        self.edges = {}

    def force(self,Sig,Val):
        veri.force('%s.%s'%(self.Path,Sig),str(Val))

    def forceAscii(self,Sig,Txt,Len):
        Res = '0x'
        for ii in range(Len):
            Chr = '%02x'%ord(Txt[ii])
            Res += Chr
        self.force(Sig,Res)


    def peek(self,Sig):
        return peek('%s.%s'%(self.Path,Sig))
    def peeksigned(self,Sig):
        return peeksigned('%s.%s'%(self.Path,Sig))
    def peekfloat(self,Sig):
        return peek_float('%s.%s'%(self.Path,Sig))

    def valid(self,Sig):
        return self.peek(Sig)==1


    def posedge(self,Sig):
        if Sig not in self.edges:
            self.edges[Sig] = self.peek(Sig)
        if self.valid(Sig) and (self.edges[Sig]==0):
            self.edges[Sig] = 1
            return True
        self.edges[Sig] = self.peek(Sig)
        return False
    def negedge(self,Sig):
        if Sig not in self.edges:
            self.edges[Sig] = self.peek(Sig)
        if not self.valid(Sig) and (self.edges[Sig]==1):
            self.edges[Sig] = 0
            return True
        self.edges[Sig] = self.peek(Sig)
        return False


    def run(self):
        log_error('run() of driverClass is supposed to be replaced')


def check_directory_exists(Fname):
    if '/' not in Fname:
        return
    wrds = Fname.split('/')
    wrds = wrds[:-1]
    res=wrds.pop(0)
    while 1:
        if not os.path.exists(res):
            os.mkdir(res)
        if wrds==[]:
            return
        res = res +'/'+wrds.pop(0)


def splitQuotes(Txt):
    Str = ''
    state = 'idle'
    for Chr in Txt:
        if state=='idle':
            if Chr=='"':
                state='work'
                Str += Chr
            else:
                Str += Chr
        elif state=='work':
            if Chr=='"':
                state='idle'
                Str += Chr
            elif Chr==' ':
                Str += 'SPACE$SPACE'
            else:
                Str += Chr
    Wrds = Str.split()
    for ind,Wrd in enumerate(Wrds):
        X = Wrd.replace('SPACE$SPACE',' ')
        Wrds[ind] = X
    return Wrds

def pStack(Txt=''):
    if Txt!='': print(Txt)
    traceback.print_stack()



print('>>>verification_logs loaded')

