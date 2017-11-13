
import sys
Errors = 0   
Corrects = 0   
Wrongs = 0   
Warnings = 0   
print_debug_messages=0
MAXWRONGS = 20

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



def get_cycles():
    return peek('tb.cycles')


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
def log_err(Text,Tb):
    global Errors,printed_already,Flog
    if (not Flog):
        Flog=open('pymon.log','w')
    if (Text in printed_already):
        return
    printed_already[Text]=1
    print '@%d: %d: ERROR: %s'%(get_cycles(),Errors,Text)
    Flog.write('@%d: %d ERROR: %s\n'%(get_cycles(),Errors,Text))
    Errors +=1  
    if Tb:
        veri.force('tb.errors',str(Errors))


def log_correct(Text):
    global Corrects,Flog
    if (not Flog):
        Flog=open('pymon.log','w')
    Corrects += 1
    veri.force('tb.corrects',str(Corrects))
    print '@%d: %d vs %d CORRECT: %s'%(get_cycles(),Corrects,Wrongs,Text)
    Flog.write('@%d: %d vs %d CORRECT: %s\n'%(get_cycles(),Corrects,Wrongs,Text))

    
def log_wrong(Text):
    global Wrongs,Flog
    Wrongs += 1
    veri.force('tb.wrongs',str(Wrongs))
    if (not Flog):
        Flog=open('pymon.log','w')
    print '@%d: %d vs %d: WRONG: %s'%(get_cycles(),Wrongs,Corrects,Text)
    Flog.write('@%d: %d vs %d: WRONG: %s\n'%(get_cycles(),Wrongs,Corrects,Text))
    if Wrongs >= MAXWRONGS:
        log_info('max wrongs reached (%d). bailing out.'%(Wrongs))
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
        Flog=open('pymon.log','w')
    print '%d: warning: %s'%(Warnings,Text)
    Flog.write('%d: warning: %s\n'%(Warnings,Text))
    printed_already[Text]=1
    Warnings +=1  

def log_info(Text):
    global Flog
    if (not Flog):
        Flog=open('pymon.log','w')
    print '@%d: info: %s'%(get_cycles(),Text)
    Flog.write('@%d: info: %s\n'%(get_cycles(),Text))


def log_info2(Text):
    global Flog2
    if (not Flog2):
        Flog2=open('2pymon.log','w')
    Flog2.write('@%d:     %s\n'%(get_cycles(),Text))

def log_info3(Text):
    global Flog3
    if (not Flog3):
        Flog3=open('3pymon.log','w')
    Flog3.write('@%d:     %s\n'%(get_cycles(),Text))

def log_info4(Text):
    global Flog4
    if (not Flog4):
        Flog4=open('4pymon.log','w')
    Flog4.write('@%d:     %s\n'%(get_cycles(),Text))



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
    if 'x' in Val: return -1
    if 'z' in Val: return -1
    if 'q' in Val: return -1
    return int(Val,2)
def peek(Sig):
    return intx(veri.peek(Sig))

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



   

