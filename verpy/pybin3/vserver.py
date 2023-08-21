#! /usr/bin/env python3.10

import os,sys
import traceback
import re

# New = os.path.expanduser('~/verpy')
# sys.path.append(New)
import vserverHelpString as helpString
import logs
import importlib

import pyver,executes
from glvreader import glv_readfile
import module_class
dbx = False

class EnvironmentClass:
    def __init__(self):
        self.SearchDirs=[]
        self.Modules={}
        self.Current=None
        self.DontFlattens=[]
        self.systemverilog=False
        self.VerilogExtensions=['v','glv','sv']
        self.params = {}
        self.imports = {}
        self.GateLevelRead = False
        self.Path = []
        self.Vars = {}
        self.Sons = {}
        self.Fathers = {}
        self.Top = False
        self.CommandsHistory  = []

Env = EnvironmentClass()
pyver.Env = Env
Env.read_verilog_file =  pyver.read_verilog_file
Env.rundir = '.'

import cmd
class cmdxClass(cmd.Cmd):
    def do_exit(self,aaa):
        print('thanks and see you again')
        logs.closeLogs()
        cleanUp()
        saveHistory()
        sys.exit()
    def do_quit(self,aaa):
        print('thanks and see you again')
        logs.closeLogs()
        cleanUp()
        saveHistory()
        sys.exit()
    def do_help(self,aaa):
        logs.log_info(helpString.helpString)


    def emptyline(self):
        print('top: %s path=%s' % (Env.Top,'.'.join(Env.Path)))
        return False
    def default(self,Txt):
        wrds = Txt.split()
        if len(wrds)>0:
            try:
                use_command_wrds(wrds)
            except:
                logs.log_info("Failed: %s " % Txt)
                traceback.print_last()
                traceback.print_last(None,logs.Flogs[0])
#                use_command_wrds(wrds)
            Env.CommandsHistory.append(Txt)
        return False

def saveHistory():
    if len(Env.CommandsHistory) < 3: return
    Fout = open('cmd.hist','w')
    for line in Env.CommandsHistory:
        Fout.write('%s\n' % line)
    Fout.close()



def main():
    Params = logs.parse_args()
    Env.params = Params
    print(Params)
    Files = Params['fnames']
    for Fname in Files:
        pyver.load_verilog_file(Fname,'.',Env)
        logs.record_directory(Fname,Env.SearchDirs)
    if '-import' in Params:
        for Fname in Params['-import']:
            use_command_wrds(['import',Fname])
    if '-source' in Params:
        for Fname in Params['-source']:
            use_command_wrds(['source',Fname])
    if '-include' in Params:
        for Fname in Params['-include']:
            use_command_wrds(['source',Fname])
    if '-do' in Params:
        for Fname in Params['-do']:
            wrds  = Fname.split()
            use_command_wrds(wrds)
            

    execute_terminal_commands()

def execute_terminal_commands():
    Intr = cmdxClass()
    Intr.prompt='?:'
    Intr.cmdloop('hello')


def use_command_wrds(wrds):
    if wrds[0] == 'import':
        my_importing(wrds[1],Env)
        return
    if wrds[0] in ['source','include']:
        if len(wrds) == 1:
            use_command_wrds(['insts'])
            return
        Lines = readLines(wrds[1])
        for Line in Lines:
            X = Line.split()
            if X!= []:
                use_command_wrds(X)
        return

    if wrds[0] == 'glv':
        if wrds[1] in ['1','yes','True']:
            Env.GateLevelRead = True
        else:
            Env.GateLevelRead = False
        logs.log_info('set glv to %s' %Env.GateLevelRead) 
        return

    if wrds[0] == 'top':
        if len(wrds) == 1:
            logs.log_info('top is %s' % Env.Top)
            return
        Module = wrds[1]
        if Module in Env.Modules:
            Env.Current = Env.Modules[Module]
            Env.Top = Module
            Env.Path = [Module]
        else:
            logs.log_info("%s not loaded" % Module)
        return


    if wrds[0] == 'set':
        Var = wrds[1]
        Expr = wrds[2]
        Env.Vars[Var] = Expr

    if wrds[0] == 'hist':
        for Line in Env.CommandsHistory:
            print(Line)
        return

    if wrds[0] == 'current':
        if len(wrds) == 1:
            logs.log_info('current %s ' % Env.Current.Module)
            return
        Module = wrds[1]
        if Module not in Env.Modules:
            executes.try_and_load_module(Module,Env)
        if Module in Env.Modules:
            Env.Current = Env.Modules[Module]
            Env.Path = [Module]
        else:
            logs.log_info('failed to load %s' % Module)
        return

    if wrds[0] == 'load':
        if os.path.exists('db0.pickle'):
            os.system('/bin/rm db0.pickle')
        if len(wrds) == 1:
            use_command_wrds(['loaded'])
            return
        if os.path.exists(wrds[1]):
            pyver.load_verilog_file(wrds[1],'.',Env)
            logs.record_directory(wrds[1],Env.SearchDirs)
        else:
            executes.try_and_load_module(wrds[1],Env)
       
        if not Env.Current:
            return

        if Env.Path == []:
            Env.Path = [Env.Current.Module]
        if not Env.Top: 
            Env.Top = Env.Current.Module
        return


    if wrds[0] == 'dirs':
        if len(wrds) == 1:
            logs.log_info('search: %s' % str(Env.SearchDirs))
        else:
            for wrd in wrds[1:]:
                Env.SearchDirs.append(wrd)
        return
    if wrds[0] == 'load_mvlg':
        os.system('mvlg.py %s %s' % (wrds[1],'/tmp/aaa.aaa'))
        Lines = readLines('/tmp/aaa.aaa')
        for Fname in Lines:
            Fname = Fname[:-1]
            pyver.load_verilog_file(Fname,'.',Env)
        return            
    if wrds[0] == 'load_deep':
        if len(wrds) == 3:
            executes.try_and_load_module(wrds[1],Env)
            Deep = eval(wrds[2])
        elif len(wrds) == 2:
            if not Env.Current: return
            Deep = eval(wrds[1])
        loadDeep(Env.Current,Env,Deep)
        return
    if wrds[0] == 'pwd':
        logs.log_info('pwd: %s' % '.'.join(Env.Path))
        return

    if wrds[0] == 'tree_up':
        if len(wrds) == 1: return
        Net = wrds[1]
        Mod = Env.Current
        if len(wrds) >= 3:
            Now = wrds[2]
            if Now not in Env.Modules:
                executes.try_and_load_module(Now,Env)
            if Now in Env.Modules:
                Mod = Env.Modules[Now]
            else:
                logs.log_info('failed to load %s' % Now)
        Ok = True
        while Ok:
            if Mod.is_external(Net): 
                LLL = use_command_wrds(['up',Net,Mod.Module])
                if not LLL:
                    Ok = False
                else:
                    Mod = LLL[0][0]
                    Net = LLL[0][1]
            else:
                Ok = False
        logs.log_info('top wire %s %s' % (Mod.Module,Net))
        tree_down(Net,Mod,Env,[],0)
        return
        
    if wrds[0] == 'tree_down':
        if len(wrds) == 1: return
        Net = wrds[1]
        Mod = Env.Current
        if len(wrds) >= 3:
            Now = wrds[2]
            if Now not in Env.Modules:
                executes.try_and_load_module(Now,Env)
            Mod = Env.Modules[Now]
        tree_down(Net,Mod,Env,[],0)
        return



    if wrds[0] == 'up':
        if len(wrds) == 1: return
        Net = wrds[1]
        Mod = Env.Current
        if len(wrds) >= 3:
            Now = wrds[2]
            if Now not in Env.Modules:
                executes.try_and_load_module(Now,Env)
            Mod = Env.Modules[Now]

        if not Mod.is_external(Net): 
            logs.log_info('is not external sig %s in %s' % (Net,Mod.Module))
            return False

        use_command_wrds(['father',Mod.Module])
        if Mod.Module not in Env.Fathers:
            logs.log_info('didnt fine  upper caller of %s' % (Mod.Module))
            return False
        Who = Env.Fathers[Mod.Module][0]
        Fmod = Env.Modules[Who]
        Found = False
        LLL = []
        for Inst in Fmod.insts:
            Obj = Fmod.insts[Inst]
#            print("INST %s type %s mod %s" % (Inst,Obj.Type,Mod.Module))
            if Obj.Type == Mod.Module:
                for Pin in Obj.conns:
                    if Pin == Net:
                        Sig = debus(Obj.conns[Pin])
                        logs.log_info('in %s, inst %s / %s, pin %s connects to %s' % (Fmod.Module,Inst,Obj.Type,Pin,Sig))    
                        LLL.append([Fmod,Sig])
                        Found = True
        if not Found:
            logs.log_info('didnt find any conns')
            return False
        return LLL
                        





#     if wrds[0] == 'conn':
#         if len(wrds) == 1: return
#         Net = wrds[1]
#         if len(wrds) == 2:
#             Mod = Env.Current
#         else:
#             Now = wrds[2]
#             if Now not in Env.Modules:
#                 executes.try_and_load_module(Now,Env)
#             Mod = Env.Modules[Now]
#         if Net not in Mod.nets:
#             
#             Who = Env.Fathers[Mod.Module][0]
# 



    if wrds[0] == 'conn':
        if len(wrds) == 1: return
        Net = wrds[1]
        if len(wrds) == 2:
            Mod = Env.Current
        else:
            Now = wrds[2]
            if Now not in Env.Modules:
                executes.try_and_load_module(Now,Env)
            Mod = Env.Modules[Now]
        if Net not in Mod.nets:
            logs.log_info('didnt find net %s in %s' % (Net,Mod.Module))
            return
        Mod.prepareBusNetTable()    
        if Net not in Mod.netTable:
            logs.log_info('no connections for %s in %s' % (Net,Mod.Module))
            return
        List = Mod.netTable[Net]
        for A,B,C in List:
            logs.log_info('   (%s)  %20s %20s %20s' % (direction(C,B,Env),A,B,C))
        return
    if wrds[0] == 'nets':
        Ins,Outs,Inouts,Wires = [],[],[],[]
        if len(wrds) > 1:
            Now = wrds[1]
            if Now != '.':
                if Now not in Env.Modules:
                    executes.try_and_load_module(Now,Env)
                if Now not in Env.Modules:
                    logs.log_error('%s cannot be loaded' % Now)
                    return
                Mod = Env.Modules[Now]
            else:
                Mod = Env.Current
        else:
            Mod = Env.Current

        if len(wrds) > 2:
            Pattern = wrds[2]
        else:
            Pattern = '*'



        Mod.prepareBusNetTable()    
        Wi,Wo,Wio,Wwire = 0,0,0,0
        for Net in Mod.nets:
            print("XXXXXXX",Pattern,Net)
            if (Pattern == '*') or re.match(Pattern,Net):
                Dir,Wid = Mod.nets[Net]
                Wids = module_class.pr_wid(Wid)
                Sig = '%s%s' % (Net,Wids)
                if 'input' in Dir:  
                    Ins.append(Sig)
                    Wi = max(len(Sig),Wi)
                elif 'output' in Dir: 
                    Outs.append(Sig)
                    Wo = max(len(Sig),Wo)
                elif 'inout' in Dir: 
                    Inouts.append(Sig)
                    Wio = max(len(Sig),Wio)
                elif Pattern != '*':
                    Wires.append(Sig)
                    Wwire = max(len(Sig),Wwire)

        Ins.sort()
        Outs.sort()
        Inouts.sort()
        Wires.sort()
        Len = max(len(Ins),max(len(Outs),len(Inouts))) 
        logs.log_info('Nets of %s Is Os IOs' % Mod.Module)
        for ii in range(Len):
            if (ii<len(Ins)):
                Ix = Ins[ii]
                Ilen = len(Mod.netTable[debus(Ix)])
            else:
                Ix = ' '
                Ilen = ''

            if (ii<len(Outs)):
                Ox = Outs[ii]
                Olen = len(Mod.netTable[debus(Ox)])
            else:
                Ox = ' '
                Olen = ''

            if (ii<len(Inouts)):
                IOx = Inouts[ii]
                IOlen = len(Mod.netTable[debus(IOx)])
            else:
                IOx = ' '
                IOlen = ''

            Head = ' %%%ds %2s   %%%ds %2s   %%%ds  %2s' % (Wi,Ilen,Wo,Olen,Wio,IOlen)
            logs.log_info(Head % (Ix,Ox,IOx))
        for Wire in Wires:
            logs.log_info('    wire %s' % Wire)

        return

    if wrds[0] == 'father':
        if len(wrds) == 1:
            Now = Env.Current.Module
        else:
            Now = wrds[1]
        if Now not in Env.Modules:
            executes.try_and_load_module(Now,Env)
        buildSonsFathers(Env)
        if Now in Env.Fathers:
            logs.log_info('father of %s is %s' % (Now,Env.Fathers[Now]))
            return

        doTheDeepSearch(Now,Env)
        if Now in Env.Fathers:
            logs.log_info('father of %s is %s' % (Now,Env.Fathers[Now]))
            return
        else:
            logs.log_info("no father yet of %s" % Now)
        return

    if wrds[0] == 'find':
        Now = wrds[1]
        logs.log_info('top is %s' % Env.Top)
        if Now not in Env.Modules:
            executes.try_and_load_module(Now,Env)
        if Now not in Env.Modules:                
            logs.log_error('%s not found' % Now)
            return
        buildSonsFathers(Env)
        Path,soFar = findPathTo(Now,Env)
        print("XXXX",Path,soFar)
        if not Path:
            if soFar != []: 
                doTheDeepSearch(soFar[0],Env)
            else:
                doTheDeepSearch(Now,Env)
            Path,soFar = findPathTo(Now,Env)
        if Path:
            logs.log_info('FIND %s' % ('.'.join(Path)))
        else:
            logs.log_info('didnt find %s'  % Now)
        return



    if wrds[0] == 'cd':
        where = wrds[1] 
        if where == '..':
            if len(Env.Path) <2:
                use_command_wrds(['father',Env.Current.Module])
                if Env.Current.Module in Env.Fathers:
                    Who = Env.Fathers[Env.Current.Module][0]
                    Env.Current = Env.Modules[Who] 
                    Env.Path = [Who]
                    
                return

            Env.Path.pop(-1)
            Now = Env.Path[-1]
            if Now not in Env.Modules:
                executes.try_and_load_module(Now,Env)
            if Now in Env.Modules:                
                Env.Current = Env.Modules[Now] 
            return
        ww = where.split('.')
        for Inst in ww:
            Now = findInst(Inst,Env.Current)
            if Now:
                if Now not in Env.Modules:
                    executes.try_and_load_module(Now,Env)
                if Now in Env.Modules:
                    Env.Path.append(Now)
                    Env.Current = Env.Modules[Now] 
        return
    if wrds[0] == 'ls':
        if len(wrds) == 1:
            if Env.SearchDirs != []:
                Dir = Env.SearchDirs[-1]
            else:
                Dir = '.'
        else:
            Dir = wrds[1]
        List = os.listdir(Dir)
        for Fname in List:
            if Fname.endswith('.v'):
                logs.log_info('     %32s' % Fname)
        return

    if wrds[0] == 'insts':
        print("INST",wrds)
        if len(wrds)>1:
            Now = wrds[1]
            if Now not in Env.Modules:
                executes.try_and_load_module(Now,Env)
                if Now in Env.Modules:
                    Env.Current = Env.Modules[Now]
                    print("XXXXX",Env.Current.Module,Now)
        if not Env.Current: return
        Insts = {}
        Many = {}
        for Inst in Env.Current.insts:
            Type = Env.Current.insts[Inst].Type
            if Type not in Many:
                Many[Type] = 1
                Insts[Type] = Inst
            else:
                Many[Type] += 1
        logs.log_info('LS of %s' % (Env.Current.Module)) 
        for Type in Many:
            logs.log_info(' (%3s) %32s   %32s' % (Many[Type],Type,Insts[Type]))
        return            


    if wrds[0] == 'loaded':
        Keys = list(Env.Modules.keys())
        Keys.sort()
        for Mod in Keys:
            logs.log_info('     %s' % Mod)
        return 

    if wrds[0] == 'os':
        X = ' '.join(wrds[1:])
        os.system(X)
        return
    if wrds[0] in Env.imports:
        Str = '%s.%s()' % (wrds[0],wrds[1])
        exec(Str,Env.imports)
        return

    if wrds[0] in ['open']:
        if len(wrds) == 1:
            Now = Env.Top
        else:
            Now = wrds[1]
        Fname = findModuleFname(Now,Env)
        if Fname:
            os.system('open -a Textedit %s' % Fname)
        return

    if wrds[0] in ['vi']:
        if len(wrds) == 1:
            Now = Env.Top
        else:
            Now = wrds[1]
        Fname = findModuleFname(Now,Env)
        if Fname:
            os.system('vi %s' % Fname)
        return
    
    for Cmd in Commands:
        if Cmd.startswith(wrds[0]):
            wrds[0] = Cmd
            use_command_wrds(wrds)
            return


    logs.log_error('%s not recognized' % ' '.join(wrds))

def findModuleFname(Now,Env):
    for Dir in Env.SearchDirs:
        if os.path.exists('%s/%s.v' % (Dir,Now)):
            return '%s/%s.v' % (Dir,Now)
    return False

def debus(Sig):
    Sig = module_class.pr_expr(Sig)
    if '[' in Sig: return Sig[:Sig.index('[')]
    if type(Sig) is str: return Sig
        


def findInst(Inst,Mod):
    if Inst in Mod.insts:
        Type = Mod.insts[Inst].Type
        return Type
    for Who in Mod.insts:
        Type = Mod.insts[Who].Type
        if Type == Inst: return Type

    logs.log_info('didnt find "%s" in %s' % (Inst,Mod.Module))
    return False
        
def my_importing(Fname,Env,Original=True):
    sys.path += ['.']
    Orig = Fname
    if (len(Fname)>2)and(Fname[-3:]=='.py'):
        Fname = Fname[:-3]
    if ('/' in Fname):
        wrds2 = Fname.split('/')
        Fname = wrds2[-1]
        Path = '/'.join(wrds2[:-1])
        Path = os.path.abspath(Path)
        sys.path += [Path]

    That = importlib.import_module(Fname)
    That.Env = Env
    Env.imports[Fname] = That

def direction(Pin,Type,Env):
    if Pin == 'output': return 'ou'
    if Pin == 'input': return 'in'
    if Pin == 'inout': return 'io'
    if Type not in Env.Modules:
        executes.try_and_load_module(Type,Env)
    if Type not in Env.Modules: return '??'
    Mod = Env.Modules[Type]
    return dirNet(Pin,Mod)


def dirNet(Net,Mod):
    Net = debus(Net)
    if Net in Mod.nets:
        Dir,_ = Mod.nets[Net]
        if 'input' in Dir: return 'in'
        if 'output' in Dir: return 'ou'
        if 'inout' in Dir: return 'io'
    return '??'



def loadDeep(Mod,Env,Deep):
    if (Deep == 0): return
    Needs = []
    for Inst in Mod.insts:
        Type = Mod.insts[Inst].Type
        if Type not in Env.Modules:
            if Type not in Needs:
                Needs.append(Type)
    for Need in Needs:
        executes.try_and_load_module(Need,Env)

    for Need in Needs:
        if Need in Env.Modules:
            loadDeep(Env.Modules[Need],Env,Deep-1)

def buildSonsFathers(Env):
    for Module in Env.Modules:
        if Module not in Env.Sons:
            Env.Sons[Module] = []
            for Inst in Env.Modules[Module].insts:
                Obj = Env.Modules[Module].insts[Inst]
                if Obj.Type not in Env.Sons[Module]:
                    Env.Sons[Module].append(Obj.Type)
                    
                if Obj.Type not in Env.Fathers:
                    Env.Fathers[Obj.Type] = [Module]
                elif Module not in Env.Fathers[Obj.Type]:
                    Env.Fathers[Obj.Type].append(Module)

def doTheDeepSearchRound(Now,Env):
    for Dir in Env.SearchDirs:
        os.system('fgrep -l "%s "  %s/* > /tmp/deepsearch' % (Now,Dir))
        Lines = readLines('/tmp/deepsearch')
        for line in Lines:
            Cell = logs.fnameCell(line[:-1])
            if Cell not in Env.Modules:
                pyver.load_verilog_file(line[:-1],'.',Env)
    buildSonsFathers(Env)


def doTheDeepSearch(Now,Env):
    for Dir in Env.SearchDirs:
        os.system('fgrep -l "%s "  %s/* > /tmp/deepsearch' % (Now,Dir))
        Lines = readLines('/tmp/deepsearch')
        for line in Lines:
            Cell = logs.fnameCell(line[:-1])
            if Cell not in Env.Modules:
                pyver.load_verilog_file(line[:-1],'.',Env)
    buildSonsFathers(Env)
    if type(Now) is list: Now = Now[0]
    if Now in Env.Fathers:
        Up = Env.Fathers[Now][0]
        if Up not in Env.Fathers:
            print("DO FATHERS %s" % Up)
            doTheDeepSearch(Up,Env)
            
        
def readLines(Fname):
    if not os.path.exists(Fname):
        logs.log_error('failed to open file %s' % Fname)
        return []
    File = open(Fname)
    Lines = File.readlines()
    File.close()
    return Lines

def findPathTo(Now,Env,Path=[]):
    if type(Now) is list:
        Now = Now[0]
    if Now in Env.Fathers:
        Up = Env.Fathers[Now]
        if Up[0] == Env.Top: return Path,Path
        return  findPathTo(Up,Env,[Up[0]] + Path)
    return False,Path

def tree_down(Net,Mod,Env,Dones = [],Lvl=0):
    logs.log_info('  %s    %s %20s %s' % (dirNet(Net,Mod),Lvl*'  ',Net,Mod.Module))
#     logs.log_info("TREE DOWN %s %s %s %s" % (dirNet(Net,Mod),Net,Mod.Module,Dones))
    Mod.prepareBusNetTable()
    if Net not in Mod.netTable:
        logs.log_error('tree_down net %s is not in %s' % (Net,Mod.Module))
        return
    List = Mod.netTable[Net]
    for Inst,Type,Pin in List:
        if Type not in Dones:
            Dones.append(Type)
            if Pin not in ['input','output']:
                if Type not in Env.Modules:
                    executes.try_and_load_module(Type,Env)
                if Type in Env.Modules:
                    tree_down(Pin,Env.Modules[Type],Env,Dones,Lvl+1)
    
        




Commands = '''
import source include glv top set load dirs load_mvlg load_deep pwd conn
nets father find cd insts ls loaded os vi open
hist up current
'''.split()


def cleanUp():
    os.system('/bin/rm xyz_*')
    os.system('/bin/rm lex.out')
    os.system('/bin/rm db0.pickle')
    os.system('/bin/rm yacc.log')
    os.system('/bin/rm database.dump')

if __name__ == '__main__': main()
