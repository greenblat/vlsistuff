#! /usr/bin/env python3

import os,sys,string
from support1 import *
import logs
#from vlexer import run_lexer
from executes import execute_line

from glvreader import glv_readfile
dbx = False
class EnvironmentClass:
    def __init__(self):
        self.SearchDirs=[]
        self.Modules={}
        self.Current=None
        self.DontFlattens=[]
        self.systemverilog=False
        self.VerilogExtensions=['v','glv']

Env = EnvironmentClass()
def main():
    setupMain(Env)
    do_something(Env.params)


def setupMain(Env):
    params =  logs.parse_args()
    Env.systemverilog = '-sv' in params
    Env.params=params
    if (len(params.keys())==1):
        if (params['fnames']==[]):
            print_help()
            logs.log_info('nothing given to do. exiting.')
            return
    Fnames = params['fnames']
    logs.log_info('fnames: %s'%(str(Fnames)))
    if ('-rundir' in params):
        Env.rundir=params['-rundir'][0]
        if not os.path.exists(Env.rundir):
            os.mkdir(Env.rundir)
    else:
        Env.rundir='.'

    if ('-y' in params):
        Env.SearchDirs.extend(params['-y'])
    if ('-ext' in params):
        Env.VerilogExtensions.extend(params['-ext'])
    Env.GateLevelRead=('-glv' in params)

    Env.read_verilog_file=read_verilog_file
    Env.read_gate_level_verilog_file=read_gate_level_verilog_file
    Env.params=params
    for Fname in Fnames:
        if Env.GateLevelRead:
            Env.read_gate_level_verilog_file(Fname,Env.rundir)
        else:
            Env.read_verilog_file(Fname,Env.rundir,Env)
        logs.record_directory(Fname,Env.SearchDirs)

#    Env.Current = Env.Modules

def run_lexer(Fname,FnameOut):
    if Env.systemverilog:
        print('using system verilog parsing')
        os.system('systemverilog_lexer %s %s'%(Fname,FnameOut))
    else:
        os.system('%s/verilog_lexer %s %s -no_eol'%(Env.params['execpath'],Fname,FnameOut))



def read_verilog_file(Fname,RunDir,Env):
    global dbx
    run_lexer(Fname,'%s/lex.out'%RunDir)
    if Env.systemverilog:
        from vyaccer3 import run_yacc
        import db1 as dbx
    else:
        from vyaccer2 import run_yacc
        import db0 as dbx
    print('reading %s file'%Fname)
    run_yacc(False,'%s/lex.out'%RunDir,RunDir,Fname)
    Locals = dbx.load_parsed(RunDir)
    print('locals %s'%(Locals.keys()))
    for Mod in Locals:
        Locals[Mod].cleanZeroNets()
    for Mod in Locals:
        if not Env.Current: Env.Current=Locals[Mod]
        Env.Modules[Mod]=Locals[Mod]


def read_gate_level_verilog_file(Fname,RunDir):
    logs.log_info('gatelevel readfile %s'%Fname)
    run_lexer(Fname,'%s/lex.out'%RunDir)
    File = open('%s/lex.out'%RunDir)
    Locals = glv_readfile(File)
    for Mod in Locals:
        Locals[Mod].cleanZeroNets()
    for Mod in Locals:
        Env.Modules[Mod]=Locals[Mod]




def do_something(params):
    lines=[]
    print(Env.Current)
    if '-dofile' in params:
        for Scenario in params['-dofile']:
            Fin = open(Scenario,'r')
            lines += Fin.readlines()
            Fin.close()
    if ('-do' in params):
        for line in params['-do']:
            lines += [line]
    if ('-top' in params):
        for line in params['-top']:
            lines += ['top %s'%(line)]
    if ('-import' in params):
        for line in params['-import']:
            lines += ['import %s'%(line)]
    if ('-help_main' in params):
            lines += ['help_main']
    if (len(lines)>0):
        for line in lines:
            logs.log_info('do line: %s'%line)
            execute_line(line,Env)
    else:
        print(Env.Current)
        if ('-o' in params):
            Foutname = params['-o'][0]
        else:
            Foutname = 'dumpver.v'
        if dbx:
            logs.log_err('no  "-do scenario_filename" given,so i proceed to dump verilog')
            dbx.dump_all_verilog(Foutname)

    logs.log_ending('exiting')

def print_help():
    logs.log_info(HelpString)
HelpString = '''
    invocation: pyver.py <verilogfilename>  -import something.py
'''
if __name__ == '__main__':
    main()

