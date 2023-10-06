
# -lower in sys.argv will make all external connections to lower case. Pins/Ports are unaffected.

import os,sys,string
import logs
import traceback

from scan_rtl import  scan_statements,is_edged_timing,get_sensitivity_list,compute1
from extract_expr_nets import extract_sigs
from rtl_width import  get_width
from module_class import module_class,instance_class,pr_expr
from executes import try_and_load_module
from cleanParameters import cleanParameters
import logs

def help_main(Env,Color=False,Volt=False):
    Mod = Env.Current
    if '-clean' in Env.params:
        cleanParameters(Mod)

    dump_instance(Env,Mod,'-simple' in Env.params,'-lower' in Env.params,Color,Volt)
    print("VOLT %s %s" % (Volt,Env.params))
    dump_empty_module(Mod)
    if '-tb' in Env.params:
        prepare_tb(Mod)

FWID = 63
def makeIt64Bits(Mod):
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if ('input' in Dir) or ('output' in Dir):
            if Wid == 0:
                Mod.nets[Net] = Dir,(FWID,0)    
            elif type(Wid) is tuple:
                if type(Wid[0]) is int:
                    Wid2 = ('packed',Wid,(FWID,0))
                    Mod.nets[Net] = Dir,Wid2   



def prepare_tb(Mod):
    Name = Mod.Module
    print('prepare tb %s'%Name)
    STR = PREPARE_STRING.replace('MOD',Name)
    os.system(STR)
    if not os.path.exists('verilog.py'):
        os.system('/bin/mv %s.inst.py verilog.py'%Name)
        
    Fcomp = open('comp','w')
    Fcomp.write(' #! /bin/csh -f\n')
    Fcomp.write(' \n\n')
    Fcomp.write('iverilog  -Wtimescale  -o tb.vvp -g2012 -I ../rtl tb.v \\\n')
    Fcomp.write('    ../rtl/%s.v  \\\n\n\n\n'%Name)
    Fcomp.close()
    os.system('chmod +x comp')

INOUT_DRIVER = '''

module inout_driver ( inout io , input dflt );

reg val; initial val=0;
reg drive; initial drive=0;
assign io = drive ? val : 1'bz;
assign (pull1,pull0) io = dflt;

endmodule
'''

PREPARE_STRING = '''
    /bin/rm pymon.file
    /bin/rm *.empty
    /bin/mv MOD.inst tb.v
    /bin/rm lex.out
    /bin/rm db0.pickle
    /bin/rm yacc.log
    /bin/rm database.dump
    /bin/rm xyz*

'''



def dump_instance(Env,Mod,Simple=False,allPinsLowerCase = False,Color = False,Volt = False):
    Name = Mod.Module
    Fout = open('%s.inst'%(Name),'w')
    if not Simple:
        Fout.write('`timescale 1ns/1ps\n')
        Fout.write('module tb;\n')
        Fout.write('integer    cycles;   initial cycles=0;\n')
        Fout.write('integer    errors;   initial errors=0;\n')
        Fout.write('integer    wrongs;   initial wrongs=0;\n')
        Fout.write('integer    panics;   initial panics=0;\n')
        Fout.write('integer    corrects; initial corrects=0;\n')
        Fout.write('integer    seqptr; initial seqptr=0;\n')
        Fout.write('reg [31:0] marker;   initial marker=0;\n')
        Fout.write('reg [31:0] marker0;   initial marker0=0;\n')
        Fout.write('reg [31:0] marker1;   initial marker1=0;\n')
        Fout.write('reg [31:0] marker2;   initial marker2=0;\n')
        Fout.write('reg [31:0] marker3;   initial marker3=0;\n')
        Fout.write('reg [31:0] Index;   initial Index=0;\n')
        Fout.write('reg [31:0] ID;   initial ID=0;\n')

    for Param in Mod.parameters:
        Val = Mod.parameters[Param]
        Fout.write('parameter %s = %s;\n'%(Param,pr_expr(Val)))

    Regs=''
    Sigs = list(Mod.nets.keys())
    Sigs.sort()
    if Volt or Color:
        if '-voltages' in Env.params:
            Fname = Env.params['-voltages']
            os.system('ln -sf %s voltages.py' % Fname[0])
        try:
            from voltages import DRVS
            logs.log_info("voltages.py imported")
        except:
            logs.log_info("No voltages directions, reading file voltage.py failed")
            DRVS = {}
    for Sig in Sigs:
        DirHL = Mod.nets[Sig]
        Dir1 = DirHL[0]
        Wid = DirHL[1]
        if allPinsLowerCase: Sig = Sig.lower()
        if Simple:
            Fout.write('wire %s %s;\n'%(wids(DirHL[1]),Sig))
        elif ('input' in Dir1):
            if Volt:
                if isVolt(DRVS,Sig):
                    Kind,Voltx = DRVS[Sig]
                    Fout.write('reg %s %s = %s;\n'%(wids(Wid),Sig,Voltx))
                else:
                    print("XXXXXX",Sig,Wid)
                    Fout.write('reg %s %s;\n'%(wids(Wid),Sig))
            elif Color:
                if isVolt(DRVS,Sig):
                    Fout.write('reg %s [15:0] %s;\n'%(widscolor(DirHL[1]),Sig))
                    Fout.write('reg %s en_%s;\n'%(widscolor(DirHL[1]),Sig))
                    Fout.write('wire %s drv_%s;\n'%(wids(Wid),Sig))
                else:
                    Fout.write('reg %s %s;\n'%(widscolor(DirHL[1]),Sig))
                    Fout.write('wire %s drv_%s;\n'%(wids(Wid),Sig))
            else:
                Fout.write('reg %s %s;\n'%(wids(DirHL[1]),Sig))
            if not Volt or not isVolt(DRVS,Sig):
                Regs +='    %s = 0;\n'%(Sig)
        elif ('output' in Dir1):
            if Volt:
                Fout.write('wire %s %s;\n'%(wids(Wid),Sig))
            elif Color:
                if isVolt(DRVS,Sig):
                    Fout.write('wire %s [15:0] %s;\n'%(widscolor(DirHL[1]),Sig))
                    Fout.write('wire %s  %s_en;\n'%(widscolor(DirHL[1]),Sig))
                    Fout.write('wire %s drv_%s;\n'%(wids(Wid),Sig))
                else:
                    Fout.write('wire %s %s;\n'%(widscolor(DirHL[1]),Sig))
                    Fout.write('wire %s drv_%s;\n'%(wids(Wid),Sig))
            else:
                Fout.write('wire %s %s;\n'%(wids(DirHL[1]),Sig))
        elif ('inout' in Dir1):
            Fout.write('wire %s %s; reg %s tb_%s = 0; assign (pull1,pull0) %s = tb_%s;\n'%(wids(DirHL[1]),Sig,wids(DirHL[1]),Sig,Sig,Sig))

    if Color:
        for Sig in Sigs:
            DirHL = Mod.nets[Sig]
            Dir1 = DirHL[0]
            if allPinsLowerCase: Sig = Sig.lower()
            Wid = DirHL[1]
            if ('input' in Dir1):
#                Fout.write('wire %s drv_%s;\n'%(wids(Wid),Sig))
                if (type(Wid) is tuple) and (Wid[0] == 'packed'): 
                    Bus = int(Wid[1][0]) - int(Wid[1][1]) + 1
                    if Sig in DRVS:
                        Kind,Volt = DRVS[Sig]
                        for Ind in range(int(Wid[1][1]),int(Wid[1][0])+1):
                            if isVolt(DRVS,Sig):
                                Fout.write("initial begin %s[%s] = %s; en_%s[%s] = %s; end\n" % (Sig,Ind,Volt,Sig,Ind,int(Volt>400)))
                                Fout.write('%s #(%s) drvx_%s_%s (.drv(drv_%s[%s]),.voltin(%s[%s]),.inx(en_%s[%s]) );\n'%(Kind,Volt,Sig,Ind,Sig,Ind,Sig,Ind,Sig,Ind))
                            else:
                                Fout.write('%s #(%s) drvx_%s_%s (.drv(drv_%s[%s]),.inx(%s[%s]) );\n'%(Kind,Volt,Sig,Ind,Sig,Ind,Sig,Ind))

                    else:
                        Fout.write('input_bus_driver #(%s,800) drvx_%s ( .drv(drv_%s),.inx(%s) );\n'%(Bus,Sig,Sig,Sig))
                elif Sig in DRVS:
                    Kind,Volt = DRVS[Sig]
                    if isVolt(DRVS,Sig):
                        Fout.write('initial begin %s = %s; en_%s = %s; end\n' % (Sig,Volt,Sig,int(Volt>400)))
                        Fout.write('%s #(%s) drvx_%s (.drv(drv_%s),.voltin(%s),.inx(en_%s) );\n'%(Kind,Volt,Sig,Sig,Sig,Sig))
                    else:
                        Fout.write('%s #(%s) drvx_%s (.drv(drv_%s),.inx(%s) );\n'%(Kind,Volt,Sig,Sig,Sig))
                else:                
                    Fout.write('input_driver #(800) drvi_%s (.drv(drv_%s),.inx(%s));\n'%(Sig,Sig,Sig))
            elif ('output' in Dir1):
                if (type(Wid) is tuple)and (Wid[0] == 'packed'): 
                    Bus = int(Wid[1][0]) - int(Wid[1][1]) + 1
                    if isVolt(DRVS,Sig):
                        Fout.write('output_volt_bus_monitor #(%s) drvx_%s (.drv(drv_%s),.outx(%s_en),.voltout(%s) );\n'%(Bus,Sig,Sig,Sig,Sig))
                    else:
                        Fout.write('output_bus_monitor #(%s) drvx_%s (.drv(drv_%s),.outx(%s) );\n'%(Bus,Sig,Sig,Sig))
                elif isVolt(DRVS,Sig):
                    Fout.write('output_volt_monitor mon_%s (.drv(drv_%s),.outx(en_%s),.voltout(%s));\n'%(Sig,Sig,Sig,Sig))
                else:
                    Fout.write('output_monitor mon_%s (.drv(drv_%s),.outx(%s));\n'%(Sig,Sig,Sig))



    if 'clk' not in Sigs:
        Fout.write('reg clk;\n')
    if 'rst_n' not in Sigs:
        Fout.write('reg rst_n;\n')
    if not Simple:
        Fout.write(String1)
        Fout.write(Regs)
        Fout.write('    #100;\n    rst_n=1;\nend\n')
    Fout.write('%s dut (\n'%(Name))
    Pref=' '
    for Sig in Sigs:
        DirHL = Mod.nets[Sig]
        Dir1 = DirHL[0].split()[0]
        if (Dir1=='output')or(Dir1=='inout')or(Dir1=='input'):
            Wids = wids(DirHL[1])
            if '][' in Wids: Wids=''
            Ext = Sig
            if allPinsLowerCase: Ext = Sig.lower()
            if Color:
                Fout.write('    %s.%s(drv_%s%s)\n'%(Pref,Sig,Ext,Wids))
            else:
                Fout.write('    %s.%s(%s%s)\n'%(Pref,Sig,Ext,Wids))
            Pref=','
    Fout.write(');\n')
    if not Simple:
        Fout.write(PLUSARG)
        Fout.write('endmodule\n')
        Fout.write(INOUT_DRIVER)
    Fout.close()
    Fout = open('verilog.py','w')
    Fout.write(String2)
    Fout.write('def cucu():  # list of all interface signals, just to help You find the names\n')
    for Sig in Sigs:
        DirHL = Mod.nets[Sig]
        Dir1 = DirHL[0].split()[0]
        if (Dir1=='input')and(Sig not in ['clk','rst_n']):
            if allPinsLowerCase: Sig = Sig.lower()
            Fout.write("    veri.force('tb.%s','0')\n"%(Sig))

    for Sig in Sigs:
        DirHL = Mod.nets[Sig]
        Dir1 = DirHL[0].split()[0]
        if (Dir1=='output'):
            if allPinsLowerCase: Sig = Sig.lower()
            Fout.write("    %s = logs.peek('tb.%s')\n"%(Sig,Sig))
    Fout.close()
    
def isVolt(DRVS,Sig):
    if Sig not in DRVS: return False
    Kind,Volt = DRVS[Sig]
    return  'volt' in Kind




PLUSARG = '''
reg [1023:0] testname;
initial begin
    if ($value$plusargs("LOG=%s",testname)) begin 
        $python("pymonname()",testname);
    end 


    if ($value$plusargs("SEQ=%s",testname)) begin 
         $display(" Running SEQ= %s.",testname); 
    end else begin
        testname = 0;
        $display(" default test");
    end 
    #10;
    if (testname!=0) $python("sequence()",testname);
end 
'''


   
def dump_empty_module(Mod):
    Name = Mod.Module
    Fout = open('%s.empty'%(Name),'w')
    Prms = []
    for Prm in Mod.parameters:
        This = 'parameter %s = %s\n'%(Prm,pr_expr(Mod.parameters[Prm]))
        Prms.append(This)
    if Prms!=[]:
        Fout.write('module %s #(\n  %s)\n(\n'%(Name,' ,'.join(Prms)))
    else:
        Fout.write('module %s (\n'%Name)
    Ins=[]
    Outs=[]
    Sigs = Mod.nets.keys()
    for Sig in Sigs:
        DirHL = Mod.nets[Sig]
        Dir1 = DirHL[0]
        if ('input' in Dir1):
            Ins.append((Sig,DirHL[0],DirHL[1]))
        elif ('output' in Dir1):
            Outs.append((Sig,DirHL[0],DirHL[1]))

    Ins.sort()
    Outs.sort()

    Pref = ' ' 
    for In,Dir,HL in Ins:
        if HL==0:
            Fout.write('    %s%s %s %s\n'%(Pref,Dir,'  ',In))
        else:
            Fout.write('    %s%s %s %s\n'%(Pref,Dir,wids(HL),In))
        Pref = ',' 
    for Out,Dir,HL in Outs:
        if 'reg' not in Dir:
            Dir = '%s reg'%(Dir)
        if HL==0:
            Fout.write('    %s%s %s %s\n'%(Pref,Dir,'  ',Out))
        else:
            Fout.write('    %s%s %s %s\n'%(Pref,Dir,wids(HL),Out))
        Pref = ',' 
    Fout.write(');\n')
    Fout.write('initial begin\n')
    for Out,Dir,HL in Outs:
        Fout.write('    %s = 0;\n'%Out)
    Fout.write('end\n')
    Fout.write('endmodule\n')
    Fout.close()




String1 = """
always begin
    clk=0;
    #10;
    clk=1;
    #3;
    $python("negedge()");
    #7;
end
initial begin
    $dumpvars(0,tb);
    rst_n = 0;
"""    
String2 = """

import os,sys,random
import veri



NewName = os.path.expanduser('~')
if os.path.exists('%s/vlsistuff' % NewName):
    sys.path.append('%s/vlsistuff/verification_libs3'%NewName)
elif 'VLSISTUFF' in os.environ:
    sys.path.append('%s/verification_libs3'%os.environ['VLSISTUFF'])
else:
    print("please set VLSISTUFF to where You cloned vlsistuff repository. like:  /home/cucu/softs/vlsistuff")
    sys.exit()

import logs
Monitors=[]
cycles=0
GIVEUP_TIMEOUT = 1000    # how many cycles to run before retirment. 

import sequenceClass
seq = sequenceClass.sequenceClass('tb',Monitors,'',[])


def pymonname(Name):
    logs.pymonname(Name)



def sequence(TestName):
    Seq = logs.bin2string(TestName)
    seq.readfile(Seq)
    logs.setVar('sequence',Seq)
    Dir = os.path.dirname(Seq)
    logs.setVar('testsdir',Dir)
    logs.log_info('SEQUENCE %d'%len(seq.Sequence))


def cannot_find_sig(Sig):
    logs.log_error('cannot find "%s" signal in the design'%Sig)




class driverMonitor(logs.driverClass):
    def __init__(self,Path,Monitors):
        logs.driverClass.__init__(self,Path,Monitors)
#        Monitors.append(self)
#        self.Path = Path
#        self.state='idle'
#        self.waiting  = 0
#
#    def force(self,Sig,Val):
#        veri.force('%s.%s'%(self.Path,Sig),str(Val))
#
#    def peek(self,Sig):
#        return logs.peek('%s.%s'%(self.Path,Sig))
#    def peeksigned(self,Sig):
#        return logs.peeksigned('%s.%s'%(self.Path,Sig))
#
#    def valid(self,Sig):
#        return self.peek(Sig)==1
#
    def run(self):
        if self.waiting>0:
            self.waiting -= 1
        elif self.state=='idle':
            self.state='work0'
        elif self.state=='work0':
            self.state='work1'
        elif self.state=='work1':
            self.state='idle'


        if self.valid('validin')and self.valid('takenin'):
            return

# example of driver class usage
# driverMonitor('tb',Monitors)



def negedge():
    global cycles
    cycles += 1
    veri.force('tb.cycles',str(cycles))
    if (cycles>GIVEUP_TIMEOUT):
        logs.log_info('finishing on default guard of %d'%GIVEUP_TIMEOUT)
        veri.finish()
    rst_n = veri.peek('tb.rst_n')
    if (rst_n!='1'):
        return

    if (cycles==30):
        veri.listing('tb','100','deep.list')
    if (cycles>30):
        for Mon in Monitors: Mon.run()

"""
def is_double_def(Wid):
    if not isinstance(Wid,(tuple,list)):
        return False
    if (len(Wid)==3)and(Wid[0] in ['packed','double']):
        return True
    if len(Wid)!=2:
        logs.log_err('bad width definition, ilia!  %s '%(str(Wid)))
        traceback.print_stack(None,None,logs.Flog)
        return False
    return False


def widscolor(Wid):
    X = wids(Wid)
    if '][' in X:
        Ind = X.index('][')
        X = X[:Ind+1]
    elif '[' in X:
        Ind = X.index('[')
        X =  ''
        
        
    return X

def wids(Wid):
    if is_double_def(Wid):
        if (Wid[0]=='packed'):
                return '%s%s'%(pr_wid(Wid[1]),pr_wid(Wid[2]))

    if Wid==0:
        return ''
    H=Wid[0]
    L=Wid[1]
    if (H==-1):
        return ''
    else:
        return '[%s:%s]'%(pr_expr(H),pr_expr(L))

def pr_wid(Wid):
    if Wid==None:
        logs.log_err('wid is none error')
        traceback.print_stack(None,None,logs.Flog)
        return 'wid is none error!!'
    if Wid==0:
        return ''
    if type(Wid) is int:
        return '[%s:0]'%(pr_expr(Wid))
    if (len(Wid)==3)and(Wid[0]=='double'):
        return '%s%s'%(pr_wid(Wid[1]),pr_wid(Wid[2]))
     
    if (len(Wid)==3)and(Wid[0]=='packed'):
        return pr_wid(Wid[1])+pr_wid(Wid[2])
    if len(Wid)==3:
        logs.log_err('pr_wid %s'%(str(Wid)))
        traceback.print_stack(None,None,logs.Flog)
        return str(Wid)
    return '[%s:%s]'%(pr_expr(Wid[0]),pr_expr(Wid[1]))





def widsx(HL):
    if HL==0:
        return '1'
    H=HL[0]
    L=HL[1]
    if (H==-1):
        return '1'
    else:
        return '%s'%(pr_expr(int(H)-int(L)+1))
    


