
import sys,string,os,types
Errors = 0   
print_debug_messages=0

import time
import traceback
printed_already={}

Flog = False
Flog2 = False

Server=False
srvString=''

MODULE = ['none']
def currentModule():
    return MODULE[0]

def setCurrentModule(Module):
    MODULE[0]=Module

def please_print_debugs():
    global print_debug_messages
    print_debug_messages=1

def log_time(Why):
    log_info('info: %s                                 time=%s'%(Why,time.ctime()))

def log_fatal(Text):
    print 'FATAL error!! %s'%(Text)
    log_ending('from fatal')
    sys.exit()

def log_error(Text,Trace=False):
    log_err(Text,Trace)
def log_err(Text,Trace=False):
    global Errors,printed_already,Flog,srvString
    if (not Flog):
        Flog=open('pymon.file','w')
    if (Text in printed_already):
        return
    printed_already[Text]=1
    Str = '%d: ERROR!! in %s: %s\n'%(Errors,MODULE[0],Text)
    print Str,
    if Server: srvString += Str
    Flog.write(Str)
    Errors +=1  
    if (Trace):
        traceback.print_stack(None,None,Flog)

Warnings = 0   
def log_warning(Text):
    global Warnings,printed_already,Flog,srvString
    if (Text in printed_already):
        return
    if (not Flog):
        Flog=open('pymon.file','w')
    Str = '%d: warning in %s: %s\n'%(Warnings,MODULE[0],Text)
    print Str,
    if Server: srvString += Str
    Flog.write(Str)
    printed_already[Text]=1
    Warnings +=1  
def log_print(Text):
    log_info(Text,True)
def log_screen(Text):
    log_info(Text,True)

def log_info(Text,Print=True):
    global Flog,srvString
    if (not Flog):
        Flog=open('pymon.file','w')
    Str = 'info: %s\n'%(Text)
    if Print:            
        print Str,
    if Server: srvString += Str
    Flog.write(Str)


def log_info2(Text,Print=False):
    global Flog2,srvString
    if (not Flog2):
        Flog2=open('2.pymon.file','w')
    Str = 'info: %s\n'%(Text)
    if Print:            
        print Str,
    if Server: srvString += Str
    Flog2.write(Str)

def log_dbg(Text):
    if (print_debug_messages):
        print 'dbg: ',Text

def log_ending(Who):
    log_time('%s.py has %d errors and %d warnings logged\n\n'%(Who,Errors,Warnings))
    if (Flog):
        Flog.close()
    return Errors



params={}
def get_param(Param,Default):
    print '>>>>',Param,params
    if Param in params:
        print '>>>>>',params[Param]
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


def record_directory(Fname,SearchDirs):
    wrds = string.split(Fname,'/')
    wrds = wrds[:-1]
    Dir = string.join(wrds,'/')
    if (len(Dir)==0):
        Dir = '.'
    if (Dir not in SearchDirs):
        SearchDirs.append(Dir)

def check_directory_exists(Fname):
    if '/' not in Fname:
        return
    wrds = string.split(Fname,'/')
    wrds = wrds[:-1]
    res=wrds.pop(0)
    while 1:
        if not os.path.exists(res):
            os.mkdir(res)
        if wrds==[]:
            return
        res = res +'/'+wrds.pop(0)

def startsWith(Long,Short):
    if type(Long)!=types.StringType: return False
    if Short not in Long: return False
    return  Long.index(Short)==0 

VVars={}
def getVar(Var):
    if Var in VVars: return VVars[Var]
    VVars[Var]=0
    return 0

def setVar(Var,Value):
    VVars[Var]=Value

def incrVar(Var):
    Now = 1+getVar(Var)
    setVar(Var,Now)
    return Now




def gatherBraces(Lex,St='(',En=')'):
    Stack=[]
    Temp=[]
    ind=0
    while ind<len(Lex):
        Tok = Lex[ind]
        if type(Tok) in [types.ListType]:
            Tk = gatherBraces(Tok,St,En)
            Lex[ind]=Tk
            ind += 1
        elif Tok[0]==St:
            Stack.append(ind)
            Temp.append(Tok)
            ind +=1 
        elif Tok[0]==En:
            if Stack==[]:
                print 'woi',ind,Tok
                return Lex 
            Start = Stack.pop(-1)
            TT = Temp.pop(-1)
            Part = Lex[Start+1:ind]
            Lex = Lex[:Start]+[Part]+Lex[ind+1:]
        else:
            ind += 1
    return Lex 

def pStack(Txt=''):
    if Txt!='': log_error(Txt)
    traceback.print_stack(None,None,Flog)
    Flog.write('\n\n\n')

def endsWith(Long,Short):
    if type(Long)!=types.StringType: return False
    if Short not in Long: return False
    return  Long.index(Short)==(len(Long)-len(Short))


def startsWith(Long,Short):
    if type(Long)!=types.StringType: return False
    if Short not in Long: return False
    return  Long.index(Short)==0

def extract_base_name(Fname):
    AA = string.split(Fname,'/')
    BB = AA[-1]
    CC = string.split(BB,'.')
    return CC[0]



