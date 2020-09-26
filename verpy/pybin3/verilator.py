
import os,sys,string,types
import logs
import module_class

def help_main(Env):
    Mod = Env.Current
    if not os.path.exists('src'): os.mkdir('src')
    createTb(Mod)

    
    Fval = open('src/values.h','w')
    forcesAndPeeks(Mod,Fval)
    widths(Mod,Fval)
    Fval.close()
    makeCpp(Mod)

def createTb(Mod):
    Fout = open('src/tb.v','w')
    Fout.write('module tb (input incrdbg\n')
    Inst = '%s dut(\n'%(Mod.Module)
    Pref = ' '
    Assigns = []
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        Dir = Dir.replace('reg','')
        Dir = Dir.replace(' ','')
        if 'input' in Dir:
            Fout.write('  ,%s %s %s\n'%(module_class.pr_dir(Dir),module_class.pr_wid(Wid),module_class.pr_expr(Net)))
            Inst += '    %s.%s(%s)\n'%(Pref,Net,Net)
        else:
            Fout.write('  ,%s %s %s\n'%(module_class.pr_dir('output'),module_class.pr_wid(Wid),module_class.pr_expr(Net)))
            if 'output' not in Dir:
                Assigns.append('assign %s = dut.%s;\n'%(Net,Net))
            else:
                Inst += '    %s.%s(%s)\n'%(Pref,Net,Net)
        Pref = ','
    Fout.write(');\n')
    Fout.write('%s);\n'%Inst)
    for Assign in Assigns:
        Fout.write(Assign)
    Fout.write(HELPERS0)
    Fout.close()



HELPERS0 = '''
reg [31:0] cycles;   initial cycles=0;
reg [31:0] errors;   initial errors=0;
reg [31:0] wrongs;   initial wrongs=0;
reg [31:0] panics;   initial panics=0;
reg [31:0] corrects; initial corrects=0;
reg [31:0] marker;   initial marker=0;
reg [31:0] marker0;   initial marker0=0;
reg [31:0] marker1;   initial marker1=0;

reg dbg;
always @(posedge clk) if (incrdbg) begin
    cycles <= cycles + 1;
    errors <= errors + cycles;
    wrongs <= wrongs + errors;
    panics <= panics + wrongs;
    corrects <= corrects + panics;
    marker <= marker + marker;
    marker0 <= marker0 + marker0;
    marker1 <= marker1 + marker1;
    dbg <= |(cycles^errors^wrongs^panics^corrects^marker^marker0^marker1);
end
endmodule
'''


def forcesAndPeeks(Mod,Fval):
    Fval.write(STR0)
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if ('input' in Dir)or('output' in Dir):
            Wid1 = Wid
            Wid = getWid(Net,Wid,Mod)
            Fval.write('// %s %d %s\n'%(Net,Wid,Wid1))
            if Wid<=32:
                Str = STR1.replace('NET',Net)
                X = (Wid+3)/4
                Str = Str.replace('LL',str(X))
                Fval.write(Str)
            elif Wid<=64:
                Str = STR1_1.replace('NET',Net)
                X = (Wid+3)/4
                Str = Str.replace('LL',str(X))
                Fval.write(Str)
            else:
                Str = STR1_2.replace('NET',Net)
                PP = ''
                TOP = ''
                WW = Wid
                pos = 0
                while (WW>=32):
                    PP = '%08x'+PP
                    WW -= 32
                    TOP = 'top->%s[%d],'%(Net,pos)+TOP
                    pos += 1 
                X = (WW+3)/4
                if (X>0): 
                    PP = '%%0%dx'%X+PP
                    TOP = 'top->%s[%d],'%(Net,pos)+TOP
                Str = Str.replace('LLL','"'+PP+'"')
                Str = Str.replace('TOP',TOP[:-1])
                Fval.write(Str)



    Fval.write(STR2)
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if ('input' in Dir)or('output' in Dir):
            Wid = getWid(Net,Wid,Mod)
            Str = STR3.replace('NET',Net)
            if Wid<=64:
                Str = Str.replace('WID',str(Wid))
                Fval.write(Str)
            else:
                Fval.write('    if (strcmp(path,"%s")==0) {\n'%(Net))
                Many = (Wid+31)/32
                for ii in range(Many):
                    Fval.write('        copy8(val,%d); top->%s[%d] = strtol(tmp,NULL,16);\n'%(Many-ii-1,Net,Many-ii-1))
                Fval.write('        return; }\n')
    Fval.write(STR4)

def makeCpp(Mod):
    Path = logs.getVar('PATH')
    Fin  = open('%s/verilator/sim_main.cpp'%Path)
    Fout = open('src/sim_main.cpp','w')
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
    Fout.write(COMP)
    Fout.close()
    os.system('chmod +x src/comp')
    

COMP = '''#! /bin/csh -f

set INC = /Library/Frameworks/Python.framework/Versions/3.8/include/python3.8/
set LIB = /Library/Frameworks/Python.framework/Versions/3.8/lib

/bin/rm -R obj_dir


verilator -Wall \\
    -Wno-lint \\
    --top-module tb \\
    -trace \\
    -cc  --exe src/sim_main.cpp \\
    src/tb.v \\
\\
    -LDFLAGS  "-O3 -I$INC  -lpython3.8 -L$LIB" \\
    -CFLAGS   "-O3 -I$INC  -lpython3.8 -L$LIB" \\
    -f all.files \

make -j -C obj_dir -f Vtb.mk Vtb
'''




def widths(Mod,Fval):
    Fval.write(STR5)
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if ('input' in Dir)or('output' in Dir):
            Wid1 = Wid
            Wid = getWid(Net,Wid,Mod)
            Fval.write('    if (strcmp(path,"%s")==0) { strcpy(VVV,"%d"); return VVV;}\n'%(Net,Wid))
    Fval.write('    strcpy(VVV,"-1"); return VVV;\n}\n') 



STR3 ='    if (strcmp(path,"NET")==0) {top->NET = strtol(val,NULL,16);return;}\n'
STR4 = '''
    printf("error! net=%s is not defined for force\\n",path);
    return;
}
'''

STR5 = 'char *getWid(char *path) {\n'

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
char VVV[50000];
char *getValue(char *path) {
'''
STR1 ='     if (strcmp(path,"NET")==0) { sprintf(VVV,"%0LLx",top->NET); return VVV;}\n'
STR1_1 ='     if (strcmp(path,"NET")==0) { sprintf(VVV,"%0LLlx",top->NET); return VVV;}\n'
STR1_2 ='     if (strcmp(path,"NET")==0) { sprintf(VVV,LLL,TOP); return VVV;}\n'

STR2 = '''
    printf("error! net=%s is not defined for peek\\n",path);
    sprintf(VVV,"%s","-1"); return VVV;
}

char tmp[9];
void copy8_old(char *Str,int Pos) {
    int pos = Pos*8;
    for (int ii=0;ii<8;ii++) tmp[ii]=Str[pos+ii];
    tmp[8]=0;
}
void copy8(char *Str,int Pos) {
    int Len = strlen(Str)-1;
    int ii = 7;
    int fr; 
    for (ii=7;(ii>=0);ii--) {
        fr = Len-(Pos*8)-7+ii;
        if (fr>=0) tmp[ii]=Str[fr];
        else tmp[ii]='0';
    }   
    tmp[8]=0;
}





void setValue(char *path,char *val) {
'''

