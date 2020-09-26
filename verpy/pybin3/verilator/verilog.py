

import veri
import string,os,sys
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs3'%NewName)

import logs

Monitors = []

def initial(initfile):
    print('initial %s'%initfile)
    veri.force("rst_n",'0')
    if initfile!='':
        Queue.append('include %s'%initfile)
        executeCommands()
    execute_terminal_commands()

def posedge():
    return

def negedge():
    for Mon in Monitors: Mon.run()
    if veri.stime()>5:
        veri.force("rst_n",'1')
    if veri.stime()>1000000:
        veri.finish()
        sys.exit()



HelpString = '''
    !!!argument to executable - is assumed to be "include" file of initial commands.!!!
    run <num>  : run this number of steps
    CR : run 1
    .  : run 1
    till running <SafeCount> : run till cpu running  (or Safe decrements to zero)
    till break <SafeCount>   : run till debug is active (or Safe decrements to zero)
    history    : print commands you typed
    include <fname>  : source fname as lines of typed commands
    source  <fname>  : source fname as lines of typed commands (synonim to include)
    force Sig Val    : force IO signals : val is integer (0xAA - also ok)
    peek Sig         : current value of Sig
    help             : print this help
    status           : print vital state vars: regs,pc,stack...
    shell <csh coomand> : run command in linux shell, like vi emacs ls ...
    quit (or control-D) : exits back to shell
'''








imported = []
CommandsHistory=[]
import cmd
class cmdxClass(cmd.Cmd):
    def do_quit(self,aaa):
        print('thanks and see you again')
        veri.finish()
        sys.exit()
        return True
    def do_help(self,Arg):
        print(HelpString)
        return False
    def do_history(self,Arg):
        for LL in CommandsHistory:
            logs.log_info('   %s'%LL)
        return False
    def emptyline(self):
        Queue.append('.')
        executeCommands()
        Intr.prompt='@%d ?:'%veri.stime()
        CommandsHistory.append('.')
        return False
    def do_source(self,Txt):
        Queue.append('include %s'%Txt)
        executeCommands()
        Intr.prompt='@%d ?:'%veri.stime()
        CommandsHistory.append('include %s'%Txt)
    def do_include(self,Txt):
        Queue.append('include %s'%Txt)
        executeCommands()
        Intr.prompt='@%d ?:'%veri.stime()
        CommandsHistory.append('include %s'%Txt)
    def do_status(self,Txt):
        Queue.append('status')
        executeCommands()
        Intr.prompt='@%d ?:'%veri.stime()
        CommandsHistory.append('status %s'%Txt)
    def do_assert(self,Txt):
        Queue.append('assert %s'%Txt)
        executeCommands()
        Intr.prompt='@%d ?:'%veri.stime()
        CommandsHistory.append('assert %s'%Txt)

    def do_till(self,Txt):
        Queue.append('till %s'%Txt)
        executeCommands()
        Intr.prompt='@%d ?:'%veri.stime()
        CommandsHistory.append('till %s'%Txt)
    def do_run(self,Txt):
        Queue.append('run %s'%Txt)
        executeCommands()
        Intr.prompt='@%d ?:'%veri.stime()
        CommandsHistory.append('run %s'%Txt)
    def do_force(self,Txt):
        Queue.append('force %s'%Txt)
        executeCommands()
        Intr.prompt='@%d ?:'%veri.stime()
        CommandsHistory.append('force %s'%Txt)
    def do_ram_force(self,Txt):
        Queue.append('ram_force %s'%Txt)
        executeCommands()
        Intr.prompt='@%d ?:'%veri.stime()
        CommandsHistory.append('ram_force %s'%Txt)
    def do_ram_peek(self,Txt):
        Queue.append('ram_peek %s'%Txt)
        executeCommands()
        Intr.prompt='@%d ?:'%veri.stime()
        CommandsHistory.append('ram_peek %s'%Txt)
    def do_dma_ram(self,Txt):
        Queue.append('dma_ram %s'%Txt)
        executeCommands()
        Intr.prompt='@%d ?:'%veri.stime()
        CommandsHistory.append('dma_ram  %s'%Txt)
    def do_import(self,Txt):
        wrds = Txt.split()
        if (len(wrds)==3)and(wrds[1]=='as'):
            Str = 'import %s as %s; global %s '%(wrds[0],wrds[2],wrds[2])
            exec(Str)
            imported.append(wrds[2])
        elif (len(wrds)==1):
            exec('import %s ; global %s '%(wrds[0],wrds[0]))
            imported.append(wrds[0])
        else:
            logs.log_info('import of "%s" failed'%Txt)
    def do_shell(self,Txt):
        os.system(Txt)

    def default(self,Txt):
        if Txt=='EOF':
            sys.exit()
        wrds = Txt.split()
        if len(wrds)>0:
            Queue.append(Txt)
            executeCommands()
            Intr.prompt='@%d ?:'%veri.stime()
            CommandsHistory.append(Txt)
        return False



Intr = cmdxClass()

def execute_terminal_commands():
    Intr.prompt='?:'
    Intr.cmdloop('hello')

Queue = []



def runcycle():
    run_tick();

def run_tick():
    veri.runcycle()


def executeCommands():
    global interactiveWait,Queue
    while Queue!=[]:
        Cmd = Queue.pop(0)
        if '#' in Cmd: Cmd = Cmd[:Cmd.index('#')]
        wrds=Cmd.split()
        if len(wrds)==0:
            pass
        elif (wrds[0]=='.'):
            runcycle()
        elif (len(wrds)==2)and(wrds[0]=='run'):
            for ii in range(int(wrds[1])): runcycle()
        elif (wrds[0]=='pause'):
            logs.log_info('pause on %s'%str(wrds))
            return
        elif (wrds[0]=='assert'):
            logs.log_info('assert on %s'%str(wrds))
            return
            
                
        elif (wrds[0]=='till'):
            if len(wrds)==1:
                logs.log_error('till needs param running|break and optional max run count')
            else:
                What = wrds[1]
                if len(wrds)>2:
                    Safe = int(wrds[2])
                else:
                    Safe = 1000
            if What[0]=='r':
                while (Safe>0)and(not weAreRunning()):
                    runcycle()
                    Safe -= 1
                
            elif What[0]=='b':
                while (Safe>0)and(not weAreInBreak()):
                    runcycle()
                    Safe -= 1
            else:
                logs.log_error('till command accepts "running" "break" parameters, not "%s"'%(What))

        elif (wrds[0]=='force'):
            for ii in range(1,len(wrds)-1,2):
                Val = wrds[ii+1]
                try:
                    X = eval(Val)
                except:
                    X = 0
                    logs.log_error('forcing %s to "%s" failed.'%(wrds[ii],Val))
                Vals = '%x'%X
                veri.force(wrds[ii],Vals)
                if (wrds[ii]=='triggers')and(wrds[ii+1]!='0'):
                    if apb.queue0!=[]:
                        logs.log_warning('triggers toggled while APB queue is not empty. check that all program is loaded by now (len=%d)'%(len(apb.queue0)))
        elif (wrds[0]=='peek'):
            for ii in range(1,len(wrds)):
                Val = veri.peek(wrds[ii])
                Str= '%s=0x%x'%(wrds[ii],int(Val,16))
                logs.log_info('%s'%Str)
        elif (wrds[0]=='width'):
            for ii in range(1,len(wrds)):
                Val = veri.width(wrds[ii])
                Str= '%s=%d'%(wrds[ii],int(Val))
                logs.log_info('%s'%Str)
        elif (wrds[0]=='include'):
            try:
                File = open(wrds[1])
                print('file %s opened '%wrds[1])
                lines = File.readlines()
                Queue = lines + Queue
                executeCommands()
            except:
#                traceback.print_last()
#                traceback.print_stack()
                logs.log_error('failed to include "%s" file'%(wrds[1]))
        elif (wrds[0]=='define'):
            Locals[wrds[1]]=eval(wrds[2],Locals)
        elif (wrds[0]=='cpuf'):
            Addr = eval(wrds[1],Locals)
            Data = eval(wrds[2],Locals)
            veri.cpu_ram_f(str(Addr),str(Data))
        elif (wrds[0]=='cpup'):
            Addr = eval(wrds[1],Locals)
            Data = veri.cpu_ram_p(str(Addr))
            print('cpudata %s'%Data)
        elif wrds[0] in ['loadCpu','load_cpu']: 
            if len(wrds)>1: 
                loadCpu(wrds[1])
            else:
                logs.log_error('give application filename to loadCpu')
        elif wrds[0] in ['quit','exit']: 
            veri.finish()
            sys.exit()
        elif wrds[0] in ['axi_peek']: 
            if len(wrds)==2:
                Many = 16
                Addr = eval(wrds[1],Locals)
            elif len(wrds)==3:
                Many = eval(wrds[2],Locals)
                Addr = eval(wrds[1],Locals)
            else:
                logs.log_error('axi_peek <Start> <Count>')
                Addr=0
                Many=0
            guard = 0
            Str = '%06x : '%Addr
            for Run in range(Addr,Addr+Many):
                if guard==16:
                    logs.log_info(Str)
                    Str = '%06x : '%Run
                    guard=0

                if Run in slave.Ram:
                    Val = hex(slave.Ram[Run] & 0xff)[2:]
                    if Val[-1]=='L': Val = Val[:-1]
                    if len(Val)<2: Val = ' '+Val

                else:
                    Val = ' _'
                Str += ' '+Val
                guard += 1
            logs.log_info(Str)
        elif wrds[0] in ['axi_force']: 
            if len(wrds)<2:
                logs.log_error('axi_force <Start> HexValues ....')
            else:                
                Addr = eval(wrds[1],Locals)
                for wrd in wrds[2:]:
                    if (len(wrd)>=2)and(wrd[:2]=='0x'):
                        wrd = wrd[2:]
                    while len(wrd)>0:
                        try:
                            Byte = int(wrd[-2:],16)
                        except:
                            logs.log_error('axi_force found "%s" non-hexable'%(wrd[-2:]))
                            Byte=0
                        wrd = wrd[:-2]
                        slave.Ram[Addr]=Byte
                        Addr += 1
        elif wrds[0] in ['axi_flood']: 
            if len(wrds)==4:
                Val = eval(wrds[3],Locals)
            else:
                Val = 0
            if len(wrds)<3:
                logs.log_error('axi_flood <Start> <End> [flood Val]')
            else:
                Start = eval(wrds[1],Locals)
                End = eval(wrds[2],Locals)
                for II in range(Start,End+1):
                    slave.Ram[II]=Val & 0xff



        elif wrds[0] in ['dma_ram']: 
            Low = eval(wrds[1],Locals)
            High = eval(wrds[2],Locals)
            for Addr in range(Low,High+1):
                Val = veri.dma_ram(str(Addr))
                if Val==(72*'0'):
                    res = '@%x: 0 '%(Addr)
                else:
                    res = '%d @%x: %s '%(len(Val),Addr,Val)
                logs.log_info('%s'%res)
        elif wrds[0] in ['ram_peek']: 
            Low = eval(wrds[1],Locals)
            High = eval(wrds[2],Locals)
            res = '@%x: '%(Low*2)
            many = 0
            for Addr in range(Low,High+1):
                Val = veri.cpu_ram_p(str(Addr))
                res += ' %s'%Val
                many += 1
                if many==8:
                    logs.log_info('%s'%res)
                    res = '@%x: '%(2*(Addr+1))
                    many = 0
            if many>0:
                logs.log_info('%s'%res)
        elif '.' in wrds[0]: 
            www = wrds[0].split('.')
            if www[0] in imported:
                exec(' '.join(wrds),locals(),globals())
            else: 
                print('failed to do \"%s\"'%Cmd)

        else:
            try:
                exec(' '.join(wrds),locals(),globals())
                print('exec %s'%str(wrds))
            except:
                print('failed to do \"%s\"'%Cmd)



