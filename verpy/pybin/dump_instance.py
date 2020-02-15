
import os,sys,string
import types
import logs
import traceback

from scan_rtl import  scan_statements,is_edged_timing,get_sensitivity_list,compute1
from extract_expr_nets import extract_sigs
from rtl_width import  get_width
from module_class import module_class,instance_class,pr_expr
from executes import try_and_load_module
from cleanParameters import cleanParameters
import logs

def help_main(Env):
    Mod = Env.Current
    if '-clean' in Env.params:
        cleanParameters(Mod)
    dump_instance(Mod,'-simple' in Env.params)
    dump_empty_module(Mod)
    if '-tb' in Env.params:
        prepare_tb(Mod)

def prepare_tb(Mod):
    Name = Mod.Module
    print 'prepare tb %s'%Name
    STR = string.replace(PREPARE_STRING,'MOD',Name)
    os.system(STR)
    Fcomp = open('comp','w')
    Fcomp.write(' #! /bin/csh -f\n')
    Fcomp.write(' \n\n')
    Fcomp.write('iverilog -o tb.vvp tb.v \\\n')
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
    /bin/mv MOD.inst.py verilog.py

    /bin/rm lex.out
    /bin/rm db0.pickle
    /bin/rm yacc.log
    /bin/rm database.dump

'''



def dump_instance(Mod,Simple=False):
    Name = Mod.Module
    Fout = open('%s.inst'%(Name),'w')
    if not Simple:
        Fout.write('module tb;\n')
        Fout.write('reg [31:0] cycles;   initial cycles=0;\n')
        Fout.write('reg [31:0] errors;   initial errors=0;\n')
        Fout.write('reg [31:0] wrongs;   initial wrongs=0;\n')
        Fout.write('reg [31:0] panics;   initial panics=0;\n')
        Fout.write('reg [31:0] corrects; initial corrects=0;\n')
        Fout.write('reg [31:0] marker;   initial marker=0;\n')

    for Param in Mod.parameters:
        Val = Mod.parameters[Param]
        Fout.write('parameter %s = %s;\n'%(Param,pr_expr(Val)))

    Regs=''
    Sigs = Mod.nets.keys()
    Sigs.sort()
    for Sig in Sigs:
        DirHL = Mod.nets[Sig]
        Dir1 = DirHL[0]
        if Simple:
            Fout.write('wire %s %s;\n'%(wids(DirHL[1]),Sig))
        elif ('input' in Dir1):
            Fout.write('reg %s %s;\n'%(wids(DirHL[1]),Sig))
            Regs +='    %s = 0;\n'%(Sig)
        elif ('output' in Dir1):
            Fout.write('wire %s %s;\n'%(wids(DirHL[1]),Sig))
        elif ('inout' in Dir1):
            Fout.write('inout_driver drv_%s(.io(%s),.dflt(1\'b0));\n'%(Sig,Sig))
    if not Simple:
        Fout.write(String1)
        Fout.write(Regs)
        Fout.write('    #100;\n    rst_n=1;\nend\n')
    Fout.write('%s dut (\n'%(Name))
    Pref=' '
    for Sig in Sigs:
        DirHL = Mod.nets[Sig]
        Dir1 = string.split(DirHL[0])[0]
        if (Dir1=='output')or(Dir1=='inout')or(Dir1=='input'):
            Wids = wids(DirHL[1])
            if '][' in Wids: Wids=''
            Fout.write('    %s.%s(%s%s)\n'%(Pref,Sig,Sig,Wids))
            Pref=','
    Fout.write(');\n')
    if not Simple:
        Fout.write(PLUSARG)
        Fout.write('endmodule\n')
        Fout.write(INOUT_DRIVER))
    Fout.close()
    Fout = open('%s.inst.py'%(Name),'w')
    Fout.write(String2)
    Fout.write('def cucu():\n')
    for Sig in Sigs:
        DirHL = Mod.nets[Sig]
        Dir1 = string.split(DirHL[0])[0]
        if (Dir1=='input')and(Sig not in ['clk','rst_n']):
            Fout.write("    veri.force('tb.%s','0')\n"%(Sig))

    for Sig in Sigs:
        DirHL = Mod.nets[Sig]
        Dir1 = string.split(DirHL[0])[0]
        if (Dir1=='output'):
            Fout.write("    %s = logs.peek('tb.%s')\n"%(Sig,Sig))
    Fout.close()
    
PLUSARG = '''
reg [1023:0] testname;
initial begin
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
        Fout.write('module %s #(\n  %s)\n(\n'%(Name,string.join(Prms,' ,')))
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
"""    
String2 = """

import os,sys,string,random
import veri
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs'%NewName)
import logs
Monitors=[]
cycles=0


class driverMonitor:
    def __init__(self,Path,Monitors):
        Monitors.append(self)
        self.Path = Path
        self.state='idle'

    def force(self,Sig,Val):
        veri.force('%s.%s'%(self.Path,Sig),str(Val))

    def peek(self,Sig):
        return logs.peek('%s.%s'%(self.Path,Sig))
    def peeksigned(self,Sig):
        return logs.peeksigned('%s.%s'%(self.Path,Sig))

    def valid(self,Sig):
        return self.peek(Sig)==1

    def run(self):
        if self.state=='idle':
            self.state='work0'
        elif self.state=='work0':
            self.state='work1'
        elif self.state=='work1':
            self.state='idle'


        if self.valid('validin')and self.valid('takenin'):
            return


# driverMonitor('tb',Monitors)



def negedge():
    global cycles
    cycles += 1
    veri.force('tb.cycles',str(cycles))
    if (cycles>1000):
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
    if type(Wid)not in [types.TupleType,types.ListType]:
        return False
    if (len(Wid)==3)and(Wid[0] in ['packed','double']):
        return True
    if len(Wid)!=2:
        logs.log_err('bad width definition, ilia!  %s '%(str(Wid)))
        traceback.print_stack(None,None,logs.Flog)
        return False
    return False



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
    if type(Wid)==types.IntType:
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
    


