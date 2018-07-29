
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
            Regs +='    %s%s = 0;\n'%(Sig,wids(DirHL[1]))
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
            Fout.write('    %s.%s(%s%s)\n'%(Pref,Sig,Sig,wids(DirHL[1])))
            Pref=','
    Fout.write(');\n')
    if not Simple:
        Fout.write('endmodule\n')
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
    

   
def dump_empty_module(Mod):
    Name = Mod.Module
    Fout = open('%s.empty'%(Name),'w')
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
            Fout.write('    %s%s [%s:%s] %s\n'%(Pref,Dir,pr_expr(HL[0]),pr_expr(HL[1]),In))
        Pref = ',' 
    for Out,Dir,HL in Outs:
        if 'reg' not in Dir:
            Dir = '%s reg'%(Dir)
        if HL==0:
            Fout.write('    %s%s %s %s\n'%(Pref,Dir,'  ',Out))
        else:
            Fout.write('    %s%s [%s:%s] %s\n'%(Pref,Dir,HL[0],HL[1],Out))
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

    def force(self,Sig,Val):
        veri.force('%s.%s'%(self.Path,Sig),str(Val))

    def peek(self,Sig):
        return logs.peek('%s.%s'%(self.Path,Sig))

    def valid(self,Sig):
        return self.peek(Sig)==1

    def run(self):
        if self.valid('validin')and self.valid('takenin'):
            return


driverMonitor('tb',Monitors)



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


def wids(HL):
    if HL==0:
        return ''
    H=HL[0]
    L=HL[1]
    if (H==-1):
        return ''
    else:
        return '[%s:%s]'%(pr_expr(H),pr_expr(L))

def widsx(HL):
    if HL==0:
        return '1'
    H=HL[0]
    L=HL[1]
    if (H==-1):
        return '1'
    else:
        return '%s'%(pr_expr(int(H)-int(L)+1))
    


