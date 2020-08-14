

import string,os,sys

CommandsHistory=[]
import cmd
class cmdxClass(cmd.Cmd):
    def do_quit(self,aaa):
        print('thanks and see you again')
        sys.exit()
        return True
    def do_help(self,Arg):
        print(HelpString)
        return False
    def emptyline(self):
        print('emptyline')
        return False
    def default(self,Txt):
        wrds = Txt.split()
        if len(wrds)>0:
            use_command_wrds(wrds)
            CommandsHistory.append(Txt)
        return False

import logs


def runInteractive(Enva):
    global Env
    Env = Enva
    sys.path.append('.')
    Intr = cmdxClass()
    Intr.prompt='?:'
    Intr.cmdloop('hello')

    
def use_command_wrds(wrds):
    Str = ' '.join(wrds)
    exec(Str)
