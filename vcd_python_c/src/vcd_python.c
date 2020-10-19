



#include <stdlib.h>
#include "stdio.h"
#include "strings.h"
#include "ctype.h"
#include "qq64.h"

#include <Python.h>

#define Idle 0
#define Wait_end 1
#define Scope 2
#define Var 3
#define Upscope 4
#define Dumpvars 5
#define Values 6
#define Enddef 7
#define Timescale 8

#define maxsig 5000000
#define longestVal  200000
#define SENSITIVES 100

char EXAMPLE[] = "\
import string\n\
import veri\n\
\n\
New = os.path.expanduser('~/pybin')\n\
sys.path.append(New)\n\
import logs\n\
Monitors=[]\n\
\n\
BASE = 'ml_dma_tb.ifast_dma_top.iaxi_cpu_dma.axi_dma_128'\n\
CLK = BASE + '.clk'\n\
BASE2 = BASE + '.dma_operator'\n\
\n\
def peekbin(Sig,Base=BASE):\n\
    X = veri.peek('%s.%s'%(Base,Sig))\n\
    return X\n\
\n\
def peek(Sig,Base=BASE):\n\
    return logs.intx(peekbin(Sig,Base))\n\
\n\
\n\
def peek_float(Sig,Base=BASE): \n\
    A = logs.intx(peekbin(Sig,Base)) \n\
    return logs.binary2float(A) \n\
def peek_signed(Sig,Base=BASE): \n\
    return logs.intxsigned(peekbin(Sig,Base)) \n\
\n\
\n\
def valid(Sig,Base=BASE):\n\
    X = peekbin(Sig,Base)\n\
    return X=='1'\n\
\n\
\n\
\n\
\n\
def conclusions():\n\
     # print here end of run things \n\
     print 'signing off'\n\
     return \n\
cycles = 0\n\
def negedge():\n\
    global cycles\n\
    if veri.stime()>4.60717e+08:\n\
        logs.log_info('finishing on last time')\n\
        veri.finish()\n\
        sys.exit()\n\
    logs.Cycles = cycles\n\
    for Mon in Monitors: Mon.run()\n\
    cycles += 1\n\
\n\
veri.sensitive(CLK,'0',\"negedge()\")\n\
\n\
class monitorAxiClass:\n\
    def __init__(self,Path,Monitors):\n\
        self.Path = Path\n\
        self.RID = {}\n\
        self.Add = ''\n\
        self.Qin = []\n\
        self.Q1 = []\n\
        self.Raddr= -1\n\
        self.Rsize= -1\n\
        Monitors.append(self)\n\
\n\
    def peek(self,Sig):\n\
        return logs.peek('%s%s.%s'%(self.Path,self.Add,Sig))\n\
    def valid(self,Sig):\n\
        return self.peek(Sig)==1\n\
\n\
    def run(self):\n\
        self.joiner()\n\
        self.entrance()\n\
#        self.reads()\n\
\n\
\n\
    def entrance(self):\n\
        if self.valid('arvalid')and self.valid('arready'):\n\
            arid = self.peek('arid')\n\
            addr = self.peek('araddr')\n\
            arsize = self.peek('arsize')\n\
            arburst = self.peek('arburst')\n\
            if arid not in self.RID:\n\
                self.RID[arid] = []\n\
            self.RID[arid].append((addr,arsize))\n\
//            logs.log_info('addarid arid=%d addr=%x size=%x len=%d'%(arid,addr,arsize,len(self.RID[arid])))\n\
\n\
        if self.valid('rvalid')and self.valid('rready'):\n\
            rdata = self.peek('rdata')\n\
            rid = self.peek('rid')\n\
            rlast = self.valid('rlast')\n\
            if rid not in self.RID:\n\
                logs.log_error('rid %s not in RID %s'%(rid,self.RID.keys()))\n\
                return\n\
            if self.Raddr<0:\n\
                self.Raddr,self.Rsize = self.RID[rid].pop(0)\n\
                logs.log_info('start raddr=%x rsize=%x last=%d rid=%d len=%d'%(self.Raddr,self.Rsize,rlast,rid,len(self.RID[rid])))\n\
            Off = self.Raddr & 0xf\n\
            rdata0 = rdata>>(8*Off)\n\
            Mask = maskit(self.Rsize)\n\
            rdata1 = Mask & rdata0\n\
            self.Qin.append((rdata1,self.Rsize,self.Raddr))\n\
            logs.log_info('qin rdata=%x addr=%x size=%x mask=%x Off=%x'%(rdata1,self.Raddr,self.Rsize,Mask,Off))\n\
            self.Raddr += (1<<self.Rsize)\n\
            if rlast:\n\
                self.Raddr = -1\n\
\n\
    def joiner(self):\n\
        if self.valid('local_wr') and not self.valid('joiner_full'):\n\
            wstrb = self.peek('local_wstrb')\n\
            if wstrb == 0xffff:\n\
                wdata = self.peek('local_wr_data')\n\
                Rdata,Rsize,Addr = self.Qin.pop(0)\n\
                logs.log_info('joiner %x  %x %x'%(Addr,Rdata,wdata))\n\
                self.Q1.append((wdata,Rdata,Addr))\n\
            else:\n\
                wdata = self.peek('local_wr_data')\n\
                Rdata,Rsize,Addr = self.Qin.pop(0)\n\
                self.Q1.append((wdata,Rdata,Addr))\n\
                logs.log_info('joiner wstrb=%x %x  %x %x'%(wstrb,Addr,Rdata,wdata))\n\
\n\
\n\
    def reads(self):\n\
        if self.valid('local_rd'):\n\
            data = self.peek('local_rd_data_wire')\n\
            wdata,rdata,addr = self.Q1.pop(0)\n\
            logs.log_info('local_rd %x %x %x %x'%(addr,rdata,wdata,data))\n\
\n\
monitorAxiClass(BASE,Monitors)\n\
\n\
def maskit(Size):\n\
    if Size==0: return 0xff\n\
    if Size==1: return 0xffff\n\
    if Size==2: return 0xffffffff\n\
    if Size==3: return 0xffffffffffffffff\n\
    if Size==4: return 0xffffffffffffffffffffffffffffffff\n\
\n\
";

char helpstring[] = "\
import os,sys,string\n\
import veri\n\
\n\
New = os.path.expanduser('~/pybin')\n\
sys.path.append(New)\n\
import logs\n\
\n\
LASTTIME = 4.60717e+08\n\
\n\
BASE = 'tb.dut.dma'\n\
CLK = BASE + '.clk'\n\
BASE2 = BASE + '.dma_operator'\n\
\n\
def peekbin(Sig,Base=BASE):\n\
    X = veri.peek('%s.%s'%(Base,Sig))\n\
    return X\n\
\n\
def peek(Sig,Base=BASE):\n\
    return logs.intx(peekbin(Sig,Base))\n\
\n\
\n\
def valid(Sig,Base=BASE):\n\
    X = peekbin(Sig,Base)\n\
    return X=='1'\n\
\n\
\n\
\n\
def negedge():\n\
    if veri.stime()>LASTTIME:\n\
        veri.finish()\n\
        sys.exit()\n\
    work()\n\
\n\
veri.sensitive(CLK,'0','negedge()')\n\
\n\
def work():\n\
    if valid('validin') and valid('takenin'):\n\
        data = peek('datain')\n\
        logs.log_info('data valid = %x'%data)\n\
";


char vcdHEADER0[] = "\
$timescale\n\
 1ps\n\
$end\n\
$scope module vcdpython $end\n\
";

char vcdHEADER1[] = "\
$upscope $end\n\
$enddefinitions $end\n\
#0\n\
";



FILE *inf;
FILE *Frecords;
FILE *vcdF0 = NULL;
FILE *vcdF1 = NULL;
int vcdCode = 1;
int intcode();
void do_help() { 
    printf("activation:  vcd_python <vcd_file> <python file> \nPROTOTYPE of python file:\n %s\n",helpstring); 
    printf("\n\n\nBIGGER EXAMPLE:\n %s\n",EXAMPLE); 
    exit(0); }
void check_x(int i) { return; }
void do_dumpvars(char *s) { return; }

char *int2bin(int AA,int Wid,char *tmp);
void useTriggers();
void armTriggers();
void conclusions();
void record();
void shouldbe();
void readfile();
void pushtok();
void search_time();
void popscope();
void pushscope();
void do_value();
void do_scope();
void do_var();
void do_upscope();
void do_enddefinitions();
void start_python();
void drive_value();

double start_time=0.0;
double end_time=0.0;
int state=Idle;
double run_time=0.0;
int linenum;
int LASTCHANGE=0;
int search=0;

int maxusedsig;
int debug;

// activate by time steps.
float startTime = -1;
float deltaTime = -1;
float nextTriggerTime = -1.0;
char functionTime[1000];


int psig=1;
typedef struct SIG {
    long name;
    int code;
    long path;
    long fpath;
    int wide;
    char *allocated;
    char value[9];
    char traceable;
    int toggles;
} change_sig;

 change_sig sigs[maxsig];




char scriptStart[] = "\n\
import string,os,sys\n\
import traceback \n\
sys.path=sys.path+['./']\n\
import veri\n\
print 'python starting'\n\
\n\
def conclusions():\n\
    print 'no conclusions() defined. add def conclusions(): to python code to print info at the end of the run'\n\
    print 'cheers, ilia     greenblat@mac.com' \n\
if os.path.exists(INITFILE):\n\
    try:\n\
        print 'verilog.py (%s) found'%INITFILE\n\
#        if '.py' in INITFILE: INITFILE = INITFILE[:-3] \n\
        execfile(INITFILE)  \n\
#        from verilog import *\n\
        print 'verilog.py found and loaded'\n\
    except:\n\
        traceback.print_exc() \n\
        print 'verilog.py exists, but crashed. failed to read verilog.py'\n\
        veri.finish() \n\
        sys.exit() \n\
else:\n\
    print 'verilog.py does not exist'\n\
    sys.exit() \n\
\n\
";







char Valex[longestVal];

int armed[SENSITIVES];


char option[200],fname1[1000],fname2[1000];
int main(argc, argv)
    int             argc;
    char           *argv[];

{
    int argvx;
    char            line[5000];
    char             longline[5000];
    char           *j;
    int i,m,k;
    int             maxhash = 3000, stringlength = 8, maxchars = 12000000, maxtabs = 3, maxstrings = 3000;

    alpha_init();
    Valex[0]=0;
    fname1[0]=0;
    fname2[0]=0;
/* update hash table maxsize, if wanted */
    for (i=0;i<maxsig;i++) { sigs[i].code=-1; sigs[i].allocated=0; sigs[i].traceable=0; sigs[i].toggles=0;} 
    for (i=0;i<SENSITIVES;i++) armed[i]=0;
    if (argc <= 1) do_help();
    if (argc > 1) {
        for (k = 2; k <= argc; k++) {
            strcpy(option, *++argv);
            if (strcmp(option,"-debug")==0) {
                debug=1;
            } else if (strcmp(option,"-help")==0) {
              do_help();
            } else if (strcmp(option,"-start")==0) {
                    strcpy(option, *++argv);
                  start_time=atof(option);
                  k++;
            } else if (strcmp(option,"-end")==0) {
                    strcpy(option, *++argv);
                  end_time=atoi(option);
                  k++;
            } else if (fname1[0]==0) strcpy(fname1,option); 
            else if (fname2[0]==0) strcpy(fname2,option);
        }
    }
    if (fname2[0]==0) strcpy(fname2,"verilog.py");
    for (i=0;i<maxsig;i++) {
        sigs[i].allocated = 0;
    }
        

    readfile(fname1);
    conclusions();
    exit(0);
}


void conclusions() {
    PyRun_SimpleString("conclusions()");

}




void readfile(fname) char *fname; {
    char *j;
    char line[longestVal];
    int i;
    int guard=0;
    char s1[longestVal];
    char s2[longestVal];
    char s3[10000];
    char s4[10000];
    char s5[10000];
    char s6[10000];
    char s7[10000];
    inf = fopen(fname, "r");
    Frecords = fopen("recorded.nets","w");
    if (inf==NULL) {
        printf("error: cannot open input file %s\n",fname);
        exit(2);
    }
    j = (char *) 1;
    while ((j != NULL)&&((end_time<=0)||(run_time<=end_time))&&(inf!=NULL)) {
        j = fgets(line, longestVal, inf);
        linenum++;
        guard++;

        if (j==0) {
            conclusions();
            exit(0);
        }

        if (guard>999999) { guard=0;printf("%d lines %g %d maxusedsig=%d\n",linenum,run_time,0,maxusedsig);}
        if (j == NULL) {
            exit(0);
        }
        i=sscanf(line,"%s %s %s %s %s %s %s",s1,s2,s3,s4,s5,s6,s7);
        int Len = strlen(line);
        if (Len>(longestVal-1000)) {
            printf("wow! vcd line is way too long (%d) we support up to %d\n\n",Len,longestVal-1000);
            exit(1);
        }
//        printf("line %d len=%d  i=%d %d %d\n",linenum,strlen(line),i,strlen(s1),strlen(s2));
        switch (i) {
        case 7:
            pushtok(s1,1);
            pushtok(s2,2);
            pushtok(s3,3);
            pushtok(s4,4);
            pushtok(s5,5);
            pushtok(s6,6);
            pushtok(s7,7);
            break;
        case 6:
            pushtok(s1,1);
            pushtok(s2,2);
            pushtok(s3,3);
            pushtok(s4,4);
            pushtok(s5,5);
            pushtok(s6,6);
            break;
        case 5:
            pushtok(s1,1);
            pushtok(s2,2);
            pushtok(s3,3);
            pushtok(s4,4);
            pushtok(s5,5);
            break;
        case 4:
            pushtok(s1,1);
            pushtok(s2,2);
            pushtok(s3,3);
            pushtok(s4,4);
            break;
        case 3:
            pushtok(s1,1);
            pushtok(s2,2);
            pushtok(s3,3);
            break;
        case 2:
            pushtok(s1,1);
            pushtok(s2,2);
            break;
        case 1:
            pushtok(s1,1);
            break;
        }
    }
    printf("readfile end\n");
}
int instate;
float lastTraceTime = 0.0;
void pushtok(char *s,int ind) {
    int pr;
    long n;
    if ((ind==1)&&(s[0]=='#')) {
        run_time=atof(&(s[1]));
        LASTCHANGE++;
        if ((run_time>=0)&&(run_time<start_time)&&(search)) search_time(start_time);
//        useTriggers();
//        printf("next=%f run=%f cond=%d\n",nextTriggerTime,run_time,((nextTriggerTime>=0)&&(run_time>=nextTriggerTime)));
//        if (vcdF0) { fprintf(vcdF1,"%s\n",s);}
        if ((nextTriggerTime>=0)&&(run_time>=nextTriggerTime)) {
            nextTriggerTime += deltaTime; 
            PyRun_SimpleString(functionTime);
         }
        state=Values;
        return;
    }
    instate++;
//    printf("dbg state=%d str=%s\n",state,s);
    switch (state) {
    case Idle:
        n = qqai(s);
        instate=0;
        if (n==qqai("$scope")) state=Scope;
        else if (n==qqai("$var")) state=Var;
        else if (n==qqai("$upscope")) state=Upscope;
        else if (n==qqai("$enddefinitions")) state=Enddef;
        else if (n==qqai("$timescale")) state = Timescale;
        else if (n==qqai("$comment")) state = Timescale;
        else if (n==qqai("$date")) state = Timescale;
        else if (n==qqai("$version")) state = Timescale;
        else if (n==qqai("$dumpvars")) { 
            state=Dumpvars;
            search=1;
        } else if (s[0]=='#') {
            state=Values;
            run_time=atof(&(s[1]));
        } else { 
            printf("idle token state=%d line=%d %s\n",state,linenum,s);
        }
        check_x(1);
        break;
    case Timescale: if (strcmp(s,"$end")==0) state= Idle; break;
    case Values: do_value(s);check_x(2);break;
    case Scope: n=qqai(s);do_scope(n);check_x(3);break;            
    case Var: n=qqai(s);do_var(n);check_x(4);break;            
    case Upscope: n=qqai(s);do_upscope(n);check_x(5);break;            
    case Enddef: do_enddefinitions(s);check_x(6);break;            
    case Dumpvars: do_dumpvars(s);check_x(7);break;            
    }
}

void do_scope(long n) {
    if (n==qqai("$end")) state=Idle;
    else if (instate==2)  {
        pushscope(n);
    }    
}

void do_upscope(long n){
    if (instate==1) popscope();
    if (n==qqai("$end")) state=Idle;
}
void do_enddefinitions(char *s) {
    if (strcmp("$end",s)==0) { 
        state=Idle;
        printf("maxusedsig %d/%d\n",maxusedsig,maxsig);
        start_python();
    }    
}



long code,bus;
char temp[1000];
char temp2[1000];
int widthx;

void do_var(long n) {
    switch (instate) {
        case 1:
            if (
                  (n==qqai("parameter"))
                ||(n==qqai("wire"))
                ||(n==qqai("wand"))
                ||(n==qqai("tri"))
                ||(n==qqai("tri0"))
                ||(n==qqai("tri1"))
                ||(n==qqai("reg"))
                ||(n==qqai("trireg"))
                ||(n==qqai("supply1"))
                ||(n==qqai("supply0"))
                ||(n==qqai("real"))
                ||(n==qqai("integer"))
                ||(n==qqai("time"))
                ||(n==qqai("event"))
            ) break;
            shouldbe("wire",n); break;
        case 2:
            widthx = atoi(qqia(n));
            break;
        case 3:
            code=n; break;
        case 4:
            bus=n; break;
        case 5:
            if (n==qqai("$end")) { state=Idle;record(code,bus,widthx);}
            else {
                if (n==qqai("[-1]")) {
                    record(code,bus,widthx);
                } else {
                    strcpy(temp,qqia(n));
                    if (temp[0]=='[') {
                        int j;
                        for (j=1;(temp[j]&&(temp[j]!=':'));j++);
                        if (temp[j-1]==']') {
                            sprintf(temp,"%s%s",qqia(bus),qqia(n));
                            record(code,qqai(temp),widthx);
                        } else if (temp[j]==':') {
                            strcpy(temp2,&(temp[1]));
                            temp2[j-1]=0;
                            strcpy(temp2,&(temp[j+1]));
                            temp2[strlen(temp2)-1]=0;
                            record(code,bus,widthx);
                        }
                    }
                }
            } break;
        case 6:
            state=Idle;
            break;
    }
}


int pscope=0;
long scopes[100];
int pgood=0;

void pushscope(long n) {
    scopes[pscope++]=n;
}
void popscope() {
    pscope--;
}
long getscope(temp)
char *temp;
{
    int i;
    temp[0]=0;
    for (i=0;i<pscope;i++) {
        strcat(temp,qqia(scopes[i]));
        strcat(temp,".");
    }    
    temp[strlen(temp)-1]=0;
    return qqai(temp);
}

void search_time(start_time) int start_time;
{
    char *j;
    char line[1000];
    int nexti,sig,i;
    j = (char *) 1;
    while (j != NULL) {
        j = fgets(line, 4999, inf);
        linenum++;
//        if (!(linenum&0x3fff)) printf("%d lines t= %g %s %d\n",linenum,run_time,line,(int)j);
        if (line[0]=='$') {
        } else if (line[0]=='#') {
            run_time=atof(&(line[1]));
            if (run_time>=start_time) {
                state=Values;
                return;
            }
//            useTriggers();
            printf("next=%f run=%f cond=%d\n",nextTriggerTime,run_time,((nextTriggerTime>=0)&&(run_time>=nextTriggerTime)));
            if ((nextTriggerTime>=0)&&(run_time>=nextTriggerTime)) {
                nextTriggerTime += deltaTime; 
                PyRun_SimpleString(functionTime);
             }

        } else {
            do_value(line);
        }
    }
}






char codeintstr[30];
void codeint(int Ind) {
    int pp; 
    int pos = 1;
    int xx = (Ind % 94);
    Ind = Ind / 94; 
    codeintstr[0] = xx + '!';
    codeintstr[1] = 0;
    while (Ind!=0) {
        xx = (Ind % 94)-1;
        Ind = Ind / 94; 
        codeintstr[pos] = xx + '!';
        pos++;
    }   
    codeintstr[pos] = 0;
}

int intcode(char *st) {
    int cur,i,res=0,machpil=1,more;
    for (i=0;(st[i]!=0)&&(st[i]!='\n');i++) {
        cur = (st[i]-' '); 
        if ((cur>=0)&&(cur<=94)) {
            more = cur*machpil;
            res += more;
            machpil *= 94; 
        }   
    }   
    return res-1;
}






long sensitives[SENSITIVES];
char sensitive_value[SENSITIVES];
long sensitive_command[SENSITIVES];
int psensitive=0;


#define BIG 1000000
char bigbig[BIG];
int unsigned bigptr=0;

char *allocateString__(int Len) {
    char *Ptr;
    int ii;
    Ptr = &(bigbig[bigptr]);
    for (ii=0;ii<(Len-1); ii++) bigbig[bigptr+ii]='x';
    bigbig[bigptr+ii]=0;
    bigptr += Len;
    if (bigptr>=BIG) { printf("overflow\n"); }
    else { printf("len=%d ptr=%d\n",Len,bigptr); }
    return Ptr;
}

char *allocateString(int Len) {
    char *Ptr;
    Ptr = malloc(Len+2);
    return Ptr;
}
void drive_value(char *Val,char *Code) {
    char Bus[1000];
    int P = intcode(Code);
    if (P<0) {
        printf("bad ERROR code=%s got us negative\n",Code);
        return;
    }
    if (P>=maxsig) {
        printf("bad ERROR code=%s got us too big\n",Code);
        return;
    }
    int Width = sigs[P].wide; 
    if (strlen(Val)>Width) {
        printf("FATAL internal error. net=%s code=%s (P=%d)has different width declared=%d actual=%ld in linenum %d\n",qqia(sigs[P].fpath),Code,P,Width,strlen(Val),linenum);
        return;
    }
    if (Width<=8) {
        strcpy(sigs[P].value,Val);
    } else {
        strcpy(sigs[P].allocated,Val);
    }
    if (sigs[P].traceable) {
        if (lastTraceTime<run_time) {
            fprintf(vcdF1,"#%ld\n",(long) run_time);
            lastTraceTime = run_time;
        }
        if (Val[0]=='b')
            fprintf(vcdF1,"%s %s\n",Val,Code);
        else
            fprintf(vcdF1,"%s%s\n",Val,Code);
    }
    sigs[P].toggles += 1;
    armTriggers(P,Val);
    useTriggers();
}

void armTriggers(int P,char *Val) {
    for (int ii=0;ii<psensitive;ii++) {
        int AA = (sensitives[ii]==P);
        int BB = (sensitive_value[ii]==Val[0]);
        int Cond = AA && BB;
        if (Cond) {
            armed[ii]=1;
        }
    }
}

void useTriggers() {
    for (int ii=0;ii<psensitive;ii++) {
        if (armed[ii]) {
            PyRun_SimpleString(qqia(sensitive_command[ii]));
            armed[ii]=0;
        }
    }
}





void do_value(char *strx) {
    char temp[10];
    if (Valex[0]==0) {
        if ((strx[0]=='0')||(strx[0]=='1')||(strx[0]=='x')||(strx[0]=='z')) { 
            temp[0]=strx[0];
            temp[1]=0;
            drive_value(temp,&(strx[1]));
        } else if (strx[0]=='b') { 
            strcpy(Valex,&(strx[1]));
        }
    } else {
        drive_value(Valex,strx);
        Valex[0]=0;
    }
}


void record(long code,long bus,int width) {
    char temp[1000];
    char fullname[1000];
    int ind,i,pcode;
    psig = intcode(qqia(code));
    if (psig>=maxsig) {
        printf("sigs code is larger then array, recompile (%s,%s,%d)\n",qqia(bus),qqia(code),psig);
        exit(1);
    }
    if (psig>maxusedsig)
        maxusedsig = psig;
    sprintf(fullname,"%s.%s",qqia(getscope(temp)),qqia(bus));
//    printf("fullname %s code=%s  %d\n",fullname,qqia(code),psig);
    long FullName = qqai(fullname);
    if (sigs[psig].code== -1) {
        sigs[psig].name=bus;
        sigs[psig].code=code;
        sigs[psig].path=scopes[pscope-1];
        sigs[psig].fpath=FullName;
        sigs[psig].wide=width;
        if (width>8)
            sigs[psig].allocated = allocateString(width+1);
        else
            strcpy(sigs[psig].value,"x");
    }
    qqsa(FullName,psig);
    fprintf(Frecords,"record psig=%d sig=%s code=%s full=%s\n",psig,qqia(bus),qqia(code),fullname);
}

void shouldbe(char *st,long n) {
    if (n!=qqai(st)) {
        fprintf(stderr,"line %d syntax error expected %s got %s\n",linenum,st,qqia(n));
    }
}

int get_handle(char *pathstring) {
    return 0;
}

static PyObject*
veri_stime(PyObject *self,PyObject *args) {
    if (!PyArg_ParseTuple(args, ""))
        return NULL;
    return Py_BuildValue("l", (long) run_time);
}



static PyObject*
veri_exists(PyObject *self,PyObject *args) {
    char *pathstring;
    long handle;
    if (!PyArg_ParseTuple(args, "s",&pathstring))
        return NULL;
    handle = get_handle(pathstring);
    if (!handle) {
        return Py_BuildValue("s", "0");
    }
    return Py_BuildValue("s", "1");
}

static PyObject*
veri_sensitive(PyObject *self,PyObject *args) {
    char *pathstring,*val,*function;
    char Str[10000];
    long handle;
    Str[0]='x';
    Str[1]=0;
    if (!PyArg_ParseTuple(args, "sss",&pathstring,&val,&function))
        return NULL;

    if ((pathstring[0]<='9')&&(pathstring[0]>='0')) {
        startTime = atoi(pathstring);
        nextTriggerTime = atof(pathstring);
        deltaTime = atof(val);
        strcpy(functionTime,function);
        printf("install time based triggers start=%f delta=%f\n",nextTriggerTime,deltaTime);
        return Py_BuildValue("s", Str);
    }

    long Psig =  qqas(qqai(pathstring));
    printf("install ptr=%d psig=%lu sensitive %s %s %s\n",psensitive,Psig,pathstring,val,function);
    sensitives[psensitive] =Psig; 
    sensitive_command[psensitive] = qqai(function);
    sensitive_value[psensitive] = val[0];
    psensitive++;

    if (Psig==0) {
        printf("\npython: cannot find sig %s for sensitive\n",pathstring);
        return Py_BuildValue("s", "q");
    }
    return Py_BuildValue("s", Str);
}


int trace_widths[1000];

static PyObject*
veri_trace(PyObject *self,PyObject *args) {
    char *pathstring;
    char *wstr;
    if (!PyArg_ParseTuple(args, "ss",&pathstring,&wstr))
        return NULL;

    if (!vcdF0) {
        vcdF0  = fopen("more0.vcd","w");
        fprintf(vcdF0,"%s\n",vcdHEADER0);
        vcdF1  = fopen("more1.vcd","w");
        fprintf(vcdF1,"%s\n",vcdHEADER1);
        fprintf(vcdF1,"#%ld\n",(long) run_time);
    }

    long pp = qqai(pathstring);
    long was = qqas(pp);
    if (was) {
        sigs[was].traceable = 1;
        codeint(was);
        printf("traceable now %s   %ld     |%s|   name=%s full=%s \n",pathstring,was,codeintstr,qqia(sigs[was].name),qqia(sigs[was].fpath));
        if (sigs[was].wide>1)
            fprintf(vcdF0,"$var reg %d %s %s [%d:0] $end\n",sigs[was].wide,codeintstr,pathstring,sigs[was].wide-1);
        else
            fprintf(vcdF0,"$var reg %d %s %s $end\n",sigs[was].wide,codeintstr,pathstring);
        return Py_BuildValue("s", 0);
    }
    qqsa(pp,vcdCode);
    codeint(vcdCode);
    trace_widths[vcdCode]=atoi(wstr);
    if (trace_widths[vcdCode]>1)
        fprintf(vcdF0,"$var reg %s %s %s [%d:0] $end\n",wstr,codeintstr,pathstring,trace_widths[vcdCode]-1);
    else
        fprintf(vcdF0,"$var reg %s %s %s $end\n",wstr,codeintstr,pathstring);
    vcdCode += 1;
    return Py_BuildValue("i", 0);
}

static PyObject*
veri_force(PyObject *self,PyObject *args) {
    char *pathstring;
    char *vstr;
    if (!PyArg_ParseTuple(args, "ss",&pathstring,&vstr))
        return NULL;
    if (!vcdF0) {
        vcdF0  = fopen("more0.vcd","w");
        fprintf(vcdF0,"%s\n",vcdHEADER0);
        vcdF1  = fopen("more1.vcd","w");
        fprintf(vcdF1,"%s\n",vcdHEADER1);
        fprintf(vcdF1,"#%ld\n",(long) run_time);
    }
    printf("dbg force %s\n",pathstring);
    long pp = qqai(pathstring);
    int this;
    printf("dbg2 force %s %lx\n",pathstring,pp);
    if (!qqas(pp)) {
        qqsa(pp,vcdCode);
        codeint(vcdCode);
        fprintf(vcdF0,"$var reg 1 %s %s $end\n",codeintstr,pathstring);
        this = vcdCode;
        vcdCode += 1;
    }  else {
        this = qqas(pp);
        codeint(this);
    }
    printf("dbg3 force %s %lx\n",pathstring,pp);
    int XX = atoi(vstr);
    char tmp[100];
    int Wid = trace_widths[this];
    int2bin(XX,Wid,tmp);
    if (lastTraceTime<run_time) {
        fprintf(vcdF1,"#%ld\n",(long) run_time);
        lastTraceTime = run_time;
    }
    printf("dbg4 force %s %lx\n",pathstring,pp);
    if (Wid>1) 
        fprintf(vcdF1,"b%s %s\n",tmp,codeintstr);
    else
        fprintf(vcdF1,"%c%s\n",tmp[0],codeintstr);

    return Py_BuildValue("i", 0);
}

static PyObject*
veri_peek(PyObject *self,PyObject *args) {
    char pvalue[10000];
    char pvalue2[10000];
    char *pathstring;
    if (!PyArg_ParseTuple(args, "s",&pathstring))
        return NULL;
    long Psig =  qqas(qqai(pathstring));


    if (!Psig) {
        printf("\npython: cannot find sig %s for peek\n",pathstring);
        return Py_BuildValue("s", "q");
    }


    if (sigs[Psig].wide<=8) {
        strcpy(pvalue,sigs[Psig].value);
    } else if (!sigs[Psig].allocated) {
        strcpy(pvalue,"x");
    } else {
        strcpy(pvalue,sigs[Psig].allocated);
    }
    int Len  = strlen(pvalue);
    if (Len<sigs[Psig].wide) {
        int ii;
        int diff = sigs[Psig].wide-Len;
        for (ii=0;ii<diff;ii++) pvalue2[ii]='0';
        pvalue2[ii]=0;
        strcat(pvalue2,pvalue);
        return Py_BuildValue("s", pvalue2);
    } else 
        return Py_BuildValue("s", pvalue);
}




static PyObject*
veri_listing(PyObject *self,PyObject *args) {
    char *pathstring,*vstr,*filename;
    FILE *File;
    if (!PyArg_ParseTuple(args, "sss",&pathstring,&vstr,&filename))
        return NULL;

    File = fopen(filename,"w");
    int depth = atoi(vstr);
    fclose(File);
    return Py_BuildValue("i", 1);
}


static PyObject*
veri_finish(PyObject *self,PyObject *args) {
    if (!PyArg_ParseTuple(args, ""))
        return NULL;
    printf("finish called from python\n");
    exit(0);
    return Py_BuildValue("i", 1);
}

static PyObject*
veri_toggles(PyObject *self,PyObject *args) {
    if (!PyArg_ParseTuple(args, ""))
        return NULL;
    int ii;
    for (ii=0; ii<maxsig; ii++) {
        if (sigs[ii].toggles>0)
            printf("%d = %8d    %s\n",ii,sigs[ii].toggles,qqia(sigs[ii].fpath));
    }
    return Py_BuildValue("i", 1);
}



static PyMethodDef VeriMethods[] = {
    {"exists", veri_exists, METH_VARARGS, "Return the number of arguments received by the process."},
    {"peek", veri_peek, METH_VARARGS, "Return the number of arguments received by the process."},
    {"force", veri_force, METH_VARARGS, "tracing of new signals."},
    {"trace", veri_trace, METH_VARARGS, "tracing of new signals."},
    {"stime", veri_stime, METH_VARARGS, "Return the number of arguments received by the process."},
    {"listing", veri_listing, METH_VARARGS, "Return the number of arguments received by the process."},
    {"sensitive", veri_sensitive, METH_VARARGS,"add to watch list"},
    {"finish", veri_finish, METH_VARARGS, "Return the number of arguments received by the process."},
    {"toggles", veri_toggles, METH_VARARGS, "Return the number of arguments received by the process."},
    {NULL, NULL, 0, NULL}
};

PyObject *globals;
PyObject *locals;
void start_python() {
    Py_Initialize();
    Py_InitModule("veri", VeriMethods);
    char temp[10000];
    sprintf(temp,"INITFILE = '%s'\n%s",fname2,scriptStart);
    PyRun_SimpleString(temp);
//    PyRun_SimpleString(scriptStart);
    globals = PyDict_New();
    if (!globals) exit(2);
    PyDict_SetItemString(globals, "__builtins__", PyEval_GetBuiltins());
    locals = Py_BuildValue("{}");
}

char *int2bin(int AA,int Wid,char *tmp) {
    int i;
    for (i=0;i<Wid;i++) {
        if (AA & (1<<i)) {
            tmp[Wid-1-i]='1';  
        } else {   
            tmp[Wid-1-i]='0';  
        }
    }   
    tmp[Wid]=0;
    return tmp;
}



