
import os,sys,string,types
import logs
import module_class

def help_main(Env):
    Mod = Env.Current
    if not os.path.exists('src'): os.mkdir('src')
    makeSpice(Mod)
    createTb(Mod)

    
    Fval = open('src/values.h','w')
    forcesAndPeeks(Mod,Fval)
    widths(Mod,Fval)
    Fval.close()
    renaming()
    makeCpp(Mod)


def makeSpice(Mod):
    Fout = open('src/%s.cir'%Mod.Module,'w')
    Fout.write('* wrapper of %s\n'%(Mod.Module))
    Fout.write('.model d_%s d_python (path="path" module="%s")\n'%(Mod.Module,Mod.Module))
    Outs = []
    Ins = []
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if 'output' in Dir:
            List = explode(Net,Wid)
            Outs.extend(List)
        elif 'input' in Dir:
            List = explode(Net,Wid)
            Ins.extend(List)
    print('INS',Ins)            
    print('OUS',Outs)            
    Both = Ins+Outs
    Both.sort()
    Ins.sort()
    Outs.sort()
    print('Both',Both)            
    print('INS',Ins)            
    print('OUS',Outs)            

    Fout.write('.subckt %s %s \n'%(Mod.Module,' '.join(Both)))
    
    for ind,Out in enumerate(Outs):
        Fout.write('aout%d [d_%s] [%s] dtoa\n'%(ind,Out,Out))
    for ind,In in enumerate(Ins):
        Fout.write('ain%d [%s] [d_%s] atod\n'%(ind,In,In))


    Fout.write('a_%s \n+  [d_%s]\n+ [d_%s]\n+ d_%s\n'%(Mod.Module,' d_'.join(Ins),' d_'.join(Outs),Mod.Module))
    Fout.write('.ends\n')
    Fout.write('\n\n\n* instance\n')
    Fout.write('*x%s\n'%Mod.Module)
    for X in Both:
        Fout.write('*+ %s\n'%X)
    Fout.write('*%s\n\n'%(Mod.Module))


def explode(Net,Wid):   
    if Wid in [0,'0']: return [Net]
    if type(Wid) is tuple:
        Hi = int(Wid[0])
        Lo = int(Wid[1])
        Res = []
        for ind in range(Lo,Hi+1):
            Res.append('%s_%d_'%(Net,ind))
        return Res
    logs.log_error('explode of bus %s %s failed'%(Net,Wid))
    return [Net]


def renaming():
    File = open('src/encodingx.py','w')
    File.write('#encoding of nets for verilator\n')
    for Key in RENAMES:
        File.write('%s = %d\n'%(Key,RENAMES[Key]))
    File.write('INDEXES = {}\n')
    for Key in RENAMES:
        File.write('INDEXES["%s"] = %d\n'%(Key,RENAMES[Key]))
    File.close()


def createTb(Mod):
    Fout = open('src/wrap_%s.v'%Mod.Module,'w')
    Fout.write('module wrap_%s (input incrdbg\n'%Mod.Module)
    Inst = '%s dut(\n'%(Mod.Module)
    Pref = ' '
    Assigns = []
    for Net in MUSTS:
        Mod.nets[Net] = ('output reg',(31,0))
        
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        Dir = Dir.replace('reg','')
        Dir = Dir.replace(' ','')
        if 'input' in Dir:
            Fout.write('  ,%s %s %s\n'%(module_class.pr_dir(Dir),module_class.pr_wid(Wid),module_class.pr_expr(Net)))
            Inst += '    %s.%s(%s)\n'%(Pref,Net,Net)
        elif Net in MUSTS:
            Fout.write('  ,%s %s %s\n'%(module_class.pr_dir('output reg'),module_class.pr_wid(Wid),module_class.pr_expr(Net)))
        else:
            Fout.write('  ,%s %s %s\n'%(module_class.pr_dir('output'),module_class.pr_wid(Wid),module_class.pr_expr(Net)))
            if 'output' not in Dir:
                Assigns.append('assign %s = dut.%s;\n'%(Net,Net))
                Mod.nets[Net] = 'output',Wid
            elif  Net not in MUSTS:
                Inst += '    %s.%s(%s)\n'%(Pref,Net,Net)
        Pref = ','
    Fout.write(');\n')
    Fout.write('%s);\n'%Inst)
    for Assign in Assigns:
        Fout.write(Assign)
    Fout.write(HELPERS1)
    Fout.close()


MUSTS = 'cycles errors wrongs panics corrects marker0 marker1 marker2'.split()


HELPERS1 = '''
reg dbg;
always @(posedge clk) if (incrdbg) begin
    cycles <= cycles + 1;
    errors <= errors + cycles;
    wrongs <= wrongs + errors;
    panics <= panics + wrongs;
    corrects <= corrects + panics;
    marker0 <= marker0 + marker0;
    marker1 <= marker1 + marker1;
    marker2 <= marker2 + marker2;
    dbg <= |(cycles^errors^wrongs^panics^corrects^marker0^marker1^marker2);
end
endmodule
'''

RENAMES = {}
def forcesAndPeeks(Mod,Fval):
    Fval.write(STR0)
    Index = 0
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if ('input' in Dir)or('output' in Dir):
            Wid1 = Wid
            Wid = getWid(Net,Wid,Mod)
            if Wid<=64:
                Str = STR1.replace('NET',Net)
                Str = Str.replace('IND',str(Index))
                Fval.write(Str)
                RENAMES[Net] = Index
                Index += 1
            else:
                logs.log_info('signal %s is not driven'%Net)


    Fval.write(STR2)
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if ('input' in Dir)or('output' in Dir):
            Wid = getWid(Net,Wid,Mod)
            Str = STR3.replace('NET',Net)
            Str = Str.replace('IND',str(RENAMES[Net]))
            if Wid<=64:
                Str = Str.replace('WID',str(Wid))
                Fval.write(Str)
    Fval.write(STR4)

def makeCpp(Mod):
    Path = logs.getVar('PATH')
    Fin  = open('%s/verilator/wrapper.cpp'%Path)
    Fout = open('src/wrapper.cpp','w')
    lines = Fin.readlines()
    Fin.close()
    for line in lines:
        line = line.replace('TOP',Mod.Module)
        Fout.write(line)
    Fout.close()
    Fin  = open('%s/verilator/verilog.py'%Path)
    Fout = open('src/verilog.py','w')
    lines = Fin.readlines()
    Fin.close()
    for line in lines:
        line = line.replace('TOP',Mod.Module)
        Fout.write(line)
    Fout.close()
    Fout = open('src/comp','w')
    Fout.write(COMP.replace('TOP',Mod.Module))
    Fout.close()
    os.system('chmod +x src/comp')
    

COMP = '''#! /bin/csh -f

set INC = /Library/Frameworks/Python.framework/Versions/3.9/include/python3.9/
set LIB = /Library/Frameworks/Python.framework/Versions/3.9/lib

/bin/rm -R obj_dir


verilator -Wall \\
    -Wno-lint \\
    --top-module wrap_TOP \\
    -trace \\
    -cc  --exe src/wrapper.cpp \\
    src/wrap_TOP.v \\
\\
    -LDFLAGS  "-O3 -I$INC  -lpython3.9 -L$LIB" \\
    -CFLAGS   "-O3 -I$INC  -lpython3.9 -L$LIB" \\
    -f all.files \

cd obj_dir
make -f Vwrap_TOP.mk
# make -j -C obj_dir -f Vtb.mk Vtb


g++  wrapper.o verilated.o verilated_vcd_c.o Vwrap_TOP__ALL.a \
    -fPIC -O3 -I/Library/Frameworks/Python.framework/Versions/3.9/include/python3.9/  \
    -lpython3.9 -L/Library/Frameworks/Python.framework/Versions/3.9/lib  \
    -o wrap_TOP.so -lm -lstdc++ --shared





'''




def widths(Mod,Fval):
    Fval.write(STR5)
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if ('input' in Dir)or('output' in Dir):
            Wid1 = Wid
            Wid = getWid(Net,Wid,Mod)
            Ind = RENAMES[Net]
            if Wid==0: Wid=1
            Fval.write('        case %d: return %d; // %s\n'%(Ind,Wid,Net))
    Fval.write('        default: return -1;\n') 
    Fval.write('    }\n}\n') 



STR3 ='    case IND : {top->NET = val;return 0;} // NET\n'
STR4 = '''
        default : {
            printf("error! net=%d is not defined for force\\n",path);
            return -1L;
        }
    }
}
'''

STR5 = '''extern "C" int getWid(int path) {
    switch (path) {
'''

def getWid(Net,Wid,Mod):
    if Wid in ['0',0]: return 0
    if Wid in ['1',1]: return 1
    if type(Wid) is int: return Wid
    if type(Wid) is tuple:
        if len(Wid)==2:
            Hi = getWid(Net,Wid[0],Mod)
            Lo = getWid(Net,Wid[1],Mod)
            return Hi-Lo+1
        if (len(Wid)==3)and(Wid[0]=='packed'):
            AA = getWid(Net,Wid[1],Mod)
            BB = getWid(Net,Wid[2],Mod)
            return AA*BB
    if type(Wid) is list:
        if len(Wid)==3:
            AA = getWid(Net,Wid[1],Mod)
            BB = getWid(Net,Wid[2],Mod)
            Str = '%s %s %s'%(AA,Wid[0],BB)
            return getWid(Net,Str,Mod)
        return 1
    if type(Wid) is str:
        return eval(Wid,Mod.parameters)

    logs.log_error('wid of "%s" failed "%s"'%(Net,Wid)) 
    return 1





STR0 = '''
extern "C" long getValue(int path) {
    switch (path) {
'''
STR1 ='        case IND : return (long) top->NET; // NET\n'

STR2 = '''
        default : {
            printf("error! net=%d is not defined for peek\\n",path);
            return -1L;
        }
    }
}


extern "C" int setValue(int path,long val) {
    switch (path) {
'''

