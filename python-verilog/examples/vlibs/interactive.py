

import os,sys,string,random
import veri
import logs


import thread
import cmd
import traceback


external_commands = False


HELP = 'interacrtive commands: quit file history os clear force peek listing source time'
logs.log_info('interactive on: %s'%HELP)
CommandsHistory=[]
Interactive = True
class cmdxClass(cmd.Cmd):
    def do_quit(self,aaa):
        print 'thanks and see you again'
        veri.finish()
        sys.exit()
        return True
    def do_help(self,Arg):
        print 'x ',HELP
        return False
    def emptyline(self):
        return False
    def default(self,Txt):
        wrds = string.split(Txt)
        if len(wrds)>0:
            try:
                use_command_wrds(self,wrds)
                CommandsHistory.append(Txt)
            except:
                print 'words %s crashed.'%Txt
                traceback.print_last()
        return False

def use_command_wrds(self,wrds):
    if wrds==[]: return
    if (wrds[0] in ['quit','exit']):
        veri.finish()
    elif wrds[0] in ['slow','sleep']:
        if len(wrds)==1:
            veri.force('tb.run_slowly','1')
        elif wrds[1] in ['True','1']:
            veri.force('tb.run_slowly','1')
        elif wrds[1] in ['False','0']:
            veri.force('tb.run_slowly','0')
        else:
            print 'command "slow" or "sleep" accept one parameter: True or False or 1 or 0"'
    elif wrds[0]=='os':
        Cmd = string.join(wrds[1:],' ')
        os.system(Cmd)
    elif wrds[0]=='time':
        print 'time',veri.stime()
    elif wrds[0]=='eval':
        Cmd = string.join(wrds[1:],' ')
        print eval(Cmd)
    elif wrds[0]=='exec':
        Cmd = string.join(wrds[1:],' ')
        exec(Cmd)
    elif wrds[0] in ['file','source']:
        try:
            Fin = open(wrds[1])
        except:
            print 'failed to open %s'%wrds[1]
            return
        lines = Fin.readlines()
        Fin.close()
        for line in lines:
            wrds0 = string.split(line)
            print '>>',wrds0
            use_command_wrds(self,wrds0)
    elif (wrds[0]=='history'):
        for ind,X in enumerate(CommandsHistory):
            print ind,X
    elif (wrds[0]=='reset'):
        veri.force('tb.rst_n',wrds[1])
    elif (wrds[0]=='listing'):
        veri.listing('tb','100','deep.list')
    elif (wrds[0]=='force'):
        veri.force(wrds[1],wrds[2])
    elif (wrds[0]=='peek'):
        Val = veri.peek(wrds[1])
        logs.log_info('peeking %s  0x%x    %s'%(wrds[1],logs.intx(Val),Val))
    elif (external_commands):
        external_commands(wrds)
    else:
        print 'y ',HELP



def execute_terminal_commands():
    Intr = cmdxClass()
    Intr.prompt='?:'
    Intr.cmdloop('hello')




Thr = thread.start_new_thread(execute_terminal_commands,())

