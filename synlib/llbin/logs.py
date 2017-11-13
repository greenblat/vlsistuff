
import sys
Errors = 0   
print_debug_messages=0

import time,string
printed_already={}

Flog = False

def please_print_debugs():
    global print_debug_messages
    print_debug_messages=1

def log_time(Why):
    log_info('info: %s                                 time=%s'%(Why,time.ctime()))

def log_fatal(Text):
    print 'FATAL error!! %s'%(Text)
    log_ending('from fatal')
    sys.exit()

def log_error(Text):
    log_err(Text)
def log_err(Text):
    global Errors,printed_already,Flog
    if (not Flog):
        Flog=open('build_gdspl_run.log','w')
    if (Text in printed_already):
        return
    printed_already[Text]=1
    print '%d: error!! %s'%(Errors,Text)
    Flog.write('%d: error!!: %s\n'%(Errors,Text))
    Errors +=1  

Warnings = 0   
def log_warning(Text):
    global Warnings,printed_already,Flog
    if (Text in printed_already):
        return
    if (not Flog):
        Flog=open('build_gdspl_run.log','w')
    print '%d: warning: %s'%(Warnings,Text)
    Flog.write('%d: warning: %s\n'%(Warnings,Text))
    printed_already[Text]=1
    Warnings +=1  
def log_info(Text):
    global Flog
    if (not Flog):
        Flog=open('build_gdspl_run.log','w')
    print 'info: ',Text
    Flog.write('info: %s\n'%(Text))
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
    return parse_words_args(sys.argv[1:])

def parse_words_args(List):
    global params
    fnames=[]
    state='idle'
    for X in List:
        if (state=='idle'):
            if (X[0]=='-'):
                state='param'
                Param = X 
            elif (X[0]=='+'):
                if X[-1]=='+':
                    X = X[:-1]
                ww = string.split(X[1:],'+')
                if len(ww)==2:
                    params[ww[0]]=[ww[1]]
                elif len(ww)==1:
                    params[ww[0]]=['yes']
                else:
                    log_error('plus arg illegal format: %s'%X)
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


