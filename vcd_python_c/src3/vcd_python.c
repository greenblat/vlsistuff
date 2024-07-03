



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

#define maxsig 7000000
#define longestVal  200000
#define SENSITIVES 100

char EXAMPLE[] = "\
import string\n\
import veri\n\
\n\
New = os.path.expanduser('~/verification_libs3')\n\
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
     print('signing off')\n\
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
veri.sensitive(CLK,'0',\"negedge()\",'0')\n\
veri.sensitive(\"always\",'0',\"ontimechange()\",'0')\n\
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
import os,sys\n\
import veri\n\
\n\
New = os.path.expanduser('~/vlsistuff/verification_libs3')\n\
sys.path.append(New)\n\
import logs\n\
\n\
def conclusions():\n\
    logs.closeLogs()\n\
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
# -> when CLK path goes down (or 1 for up) :: veri.sensitive(CLK,'0','negedge()')\n\
# -> start time. period  :: veri.sensitive('100,'10','negedge()')\n\
# -> on every time change :: veri.sensitive('always','0','negedge()')\n\
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



FILE *Inf;
FILE *Frecords;
FILE *vcdF0 = NULL;
FILE *vcdF1 = NULL;
int vcdCode = 1;
int intcode(char *c);
int diffs (char *A, char *B);
void do_help() { 
    printf("activation:  vcd_python <vcd_file> <python file> \nPROTOTYPE of python file:\n %s\n",helpstring); 
    printf("   -toggles  -start <TIME> -end <TIME>\n");
    printf("\n\n\nBIGGER EXAMPLE:\n %s\n",EXAMPLE); 
    exit(0); }
void check_x(int i) { return; }

char *int2bin(int AA,int Wid,char *tmp);
void useTriggers();
void armTriggers(int P,char *Val);
void conclusions();
void record(long code,long bus,int width, long Kind);
void shouldbe(char *st,long n);
void readfile(char *fname);
void pushtok(char *s,int ind);

void popscope();
void pushscope(long n);
void do_value(char *strx,int forReal);
void do_scope(long n);
void do_var(long n);
void do_upscope(long n);
void do_enddefinitions( char *s);
void start_python();
void drive_value(char *Val,char *Code,int forReal);

double start_time=0.0;
double end_time=0.0;
int state=Idle;
void do_dumpvars(char *s) { state=Values; return; }
double run_time=0.0;
int linenum;
int LASTCHANGE=0;
int search=0;

long Changes = 0;
int maxusedsig;
int debug;

// activate by time steps.
float startTime = -1;
float deltaTime = -1;
float nextTriggerTime = -1.0;
float nextOffsetTime = -1.0;
char functionTime[1000];
char functionOffset[1000];
int AlwaysMode = 0;


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
    int toggles2;
    int changed;
    long wasZ;
} change_sig;

 change_sig sigs[maxsig];




char scriptStart[] = "\n\
import string,os,sys\n\
import traceback \n\
sys.path=sys.path+['./']\n\
print(dir())\n\
import veri\n\
print('python starting')\n\
\n\
def conclusions():\n\
    print('no conclusions() defined. add def conclusions(): to python code to print info at the end of the run')\n\
    print('cheers, ilia     greenblat@mac.com') \n\
if os.path.exists(INITFILE):\n\
    try:\n\
        print('verilog.py (%s) found'%INITFILE)\n\
#        if '.py' in INITFILE: INITFILE = INITFILE[:-3] \n\
        exec(open(INITFILE).read())  \n\
#        from verilog import *\n\
        print('verilog.py found and loaded')\n\
    except:\n\
        traceback.print_exc() \n\
        print('verilog.py exists, but crashed. failed to read verilog.py')\n\
        veri.finish() \n\
        sys.exit() \n\
else:\n\
    print('verilog.py does not exist')\n\
    if (not toggles): sys.exit() \n\
\n\
";







char Valex[longestVal];

int armed[SENSITIVES];
int sensitive_offset[SENSITIVES];
long sensitives[SENSITIVES];
char sensitive_value[SENSITIVES];
long sensitive_command[SENSITIVES];
int psensitive=0;


char option[200],fname1[1000],fname2[1000];
int toggles = 0;
int main( int argc, char *argv[]) {
    int argvx;
//    char            line[5000];
//    char             longline[5000];
    char           *j;
    int i,m,k;
    int             maxhash = 3000, stringlength = 8, maxchars = 12000000, maxtabs = 3, maxstrings = 3000;

    alpha_init();
    Valex[0]=0;
    fname1[0]=0;
    fname2[0]=0;
/* update hash table maxsize, if wanted */
    for (i=0;i<maxsig;i++) { sigs[i].code=-1; sigs[i].changed=0;sigs[i].allocated=0; sigs[i].traceable=0; sigs[i].toggles=0; sigs[i].toggles2=0; sigs[i].wasZ = 0;} 
    for (i=0;i<SENSITIVES;i++) armed[i]=0;
    for (i=0;i<SENSITIVES;i++)  sensitive_offset[i]= -1;
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
                  end_time=atof(option);
                  k++;
            } else if (strcmp(option,"-toggles")==0) {
                toggles = 1;
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


void simpleToggles();
int python_started = 0;
void conclusions() {
    if (!python_started) {
        printf("it appears that Your vcd file has no data\n");
        return;
    }
    PyRun_SimpleString("conclusions()");
    if (toggles) {
        printf("dumping toggles\n");
        simpleToggles();
    }

}

void simpleToggles() {
    int tot = 0;
    int tot2 = 0;
    int ii;
    FILE *flog;
    flog = fopen("toggles.rpt","w");
    fprintf(flog,"bus toggles, bit toggles, net\n");
    printf("bus toggles, bit toggles, net\n");
    for (ii=0; ii<=maxusedsig; ii++) {
        if (sigs[ii].toggles>0) {
            printf("%d %s\n",sigs[ii].toggles,qqia(sigs[ii].fpath));
            fprintf(flog,"%d %d %s\n",sigs[ii].toggles2,sigs[ii].toggles,qqia(sigs[ii].fpath));
            tot += sigs[ii].toggles;
            tot2 += sigs[ii].toggles2;
        }
    }
    printf("total %d bit toggles and %d bus toggles2\n",tot,tot2);
    for (ii=0; ii<=maxusedsig; ii++) {
        if (sigs[ii].wasZ>0) {
            printf("%s  was Z\n",qqia(sigs[ii].fpath));
            fprintf(flog,"%s  was Z\n",qqia(sigs[ii].fpath));
        }
    }
    fclose(flog);
}

char s1[longestVal];
char s2[longestVal];
char s3[longestVal];
char s4[longestVal];
char s5[longestVal];
char s6[longestVal];
char s7[longestVal];

void readfile(char *fname) {
    char *j;
    char line[longestVal];
    int i;
    int guard=0;
    Inf = fopen(fname, "r");
    Frecords = fopen("recorded.nets","w");
    if (Inf==NULL) {
        printf("error: cannot open input file %s\n",fname);
        exit(2);
    }
    j = (char *) 1;
    double last_time = 0.0;
    while ((j != NULL)&&((end_time<=0.0)||(run_time<=end_time))&&(Inf!=NULL)) {
        j = fgets(line, longestVal, Inf);
        linenum++;
        guard++;

        if (j==0) {
            conclusions();
            exit(0);
        }

        if (guard>999999) { guard=0;printf("%d lines time=%g %d maxusedsigs=%d\n",linenum,run_time,0,maxusedsig);}
        if (j == NULL) {
            printf("end of file simtime=%g\n",run_time);
            exit(0);
        }

        if ((run_time-last_time)>1000000000.0) {
            last_time = run_time;
            printf("TIME %d lines time=%g %d maxusedsigs=%d\n",linenum,run_time,0,maxusedsig);
        }


        i=sscanf(line,"%s %s %s %s %s %s %s",s1,s2,s3,s4,s5,s6,s7);
        int Len = strlen(line);
//        printf("len %d i=%d\n",Len,i);
        if (Len>(longestVal-1000)) {
            printf("wow! vcd line is way too long (%d) we support up to %d\n\n",Len,longestVal-1000);
            exit(1);
        }
//        printf("line %d len=%d  i=%d %d %d %s %s\n",linenum,strlen(line),i,strlen(s1),strlen(s2),s1,s2);
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
    printf("readfile end run_time=%g end_time=%g  start_time=%g\n",run_time,end_time,start_time);
}
int instate;
float lastTraceTime = 0.0;
void pushtok(char *s,int ind) {
    int pr;
    long n;
    int forReal;
    if (s[0]==0) return;
    if ((ind==1)&&(s[0]=='#')) {
        run_time=atof(&(s[1]));
        LASTCHANGE++;
        if (AlwaysMode) {
            PyRun_SimpleString(functionTime);
            state=Values;
            return;
        }
        if ((nextTriggerTime>=0)&&(run_time>=nextTriggerTime)) {
            nextTriggerTime += deltaTime; 
            PyRun_SimpleString(functionTime);
         }
        if ((nextOffsetTime>=0)&&(run_time>=nextOffsetTime)) {
            PyRun_SimpleString(functionOffset);
            nextOffsetTime = -1;
         }
        state=Values;
        return;
    }
    instate++;
//    printf("dbg state=%d str=%s\n",state,s);
    forReal = ((run_time>=0)&&(run_time>=start_time));
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
        else if (n==qqai("$dumpports")) { 
            state=Dumpvars;
            search=1;
        } else if (n==qqai("$dumpall")) { 
            state=Dumpvars;
        } else if (n==qqai("$dumpvars")) { 
            state=Dumpvars;
            //search=1;
        } else if (s[0]=='#') {
            state=Values;
            run_time=atof(&(s[1]));
            search=1;
        } else { 
            printf("idle token state=%d line=%d %s\n",state,linenum,s);
        }
        check_x(1);
        break;
    case Timescale: if (strcmp(s,"$end")==0) state= Idle; break;
    case Values: do_value(s,forReal);check_x(2);break;
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

long Kind = 0;

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
                ||(n==qqai("port"))
            ) Kind = n; break;
            shouldbe("wire",n); break;
        case 2:
            widthx = atoi(qqia(n));
            break;
        case 3:
            code=n; break;
        case 4:
            bus=n; break;
        case 5:
            if (n==qqai("$end")) { state=Idle;record(code,bus,widthx,Kind);}
            else {
                if (n==qqai("[-1]")) {
                    record(code,bus,widthx,Kind);
                } else {
                    strcpy(temp,qqia(n));
                    if (temp[0]=='[') {
                        int j;
                        for (j=1;(temp[j]&&(temp[j]!=':'));j++);
                        if (temp[j-1]==']') {
                            sprintf(temp,"%s%s",qqia(bus),qqia(n));
                            record(code,qqai(temp),widthx,Kind);
                        } else if (temp[j]==':') {
                            strcpy(temp2,&(temp[1]));
                            temp2[j-1]=0;
                            strcpy(temp2,&(temp[j+1]));
                            temp2[strlen(temp2)-1]=0;
                            record(code,bus,widthx,Kind);
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
long getscope(char *temp) {
    int i;
    temp[0]=0;
    for (i=0;i<pscope;i++) {
        strcat(temp,qqia(scopes[i]));
        strcat(temp,".");
    }    
    temp[strlen(temp)-1]=0;
    return qqai(temp);
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
void drive_value(char *Val,char *Code,int forReal) {
    int P = intcode(Code);
    if (P<0) {
        printf("bad ERROR line=%d code='%s' got us negative P=%d val=%s\n",linenum,Code,P,Val);
        return;
    }
    if (P>=maxsig) {
        printf("bad ERROR line=%d code=%s P=%d > maxsig %d got us too big, val=%s\n",linenum,Code,P,maxsig,Val);
        return;
    }


    if (Val[0] == 'r') {
        Val[9]=0;
        strcpy(sigs[P].value,&(Val[1]));
        return;
    }
    int Diffs;
    int Width = sigs[P].wide; 
    if (sigs[P].code == -1) {
        printf("FATAL internal error. code=%s (P=%d) (intcode=%d) is not a declared net linenum %d\n",Code,P,sigs[P].code,linenum);
        return;
    } else if (strlen(Val)>Width) {
        printf("FATAL internal error. net=%s code=%s (P=%d)has different width declared=%d actual=%ld in linenum %d\n",qqia(sigs[P].fpath),Code,P,Width,strlen(Val),linenum);
        return;
    }
//    printf("DRIVE wid=%d %s %s %s   %ld\n",sigs[P].wide,Code,qqia(sigs[P].name),Val,(long) run_time);
    if (Width<=8) {
        Diffs = diffs(sigs[P].value,Val);
        strcpy(sigs[P].value,Val);
    } else {
        Diffs = diffs(sigs[P].allocated,Val);
        strcpy(sigs[P].allocated,Val);
    }
    if (Val[0] == 'z') { sigs[P].wasZ = run_time; }
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
    sigs[P].toggles += Diffs;
    if (Diffs!=0) { 
        sigs[P].toggles2 ++;
        sigs[P].changed = 1;
    }
    if (forReal) {
        armTriggers(P,Val);
        useTriggers();
    }
}

void armTriggers(int P,char *Val) {
    for (int ii=0;ii<psensitive;ii++) {
        int AA = (sensitives[ii]==P);
        int BB = (sensitive_value[ii]==Val[0]);
        int Cond = AA && BB;
        if (Cond) {
            if (sensitive_offset[ii]>0) {
                nextOffsetTime = sensitive_offset[ii] + run_time;
            } else {
                armed[ii]=1;
            }
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





void do_value(char *strx,int forReal) {
    char temp[10];
    Changes++;
    if (Valex[0]==0) {
        if ((strx[0]=='0')||(strx[0]=='1')||(strx[0]=='x')||(strx[0]=='z')) { 
            temp[0]=strx[0];
            temp[1]=0;
            drive_value(temp,&(strx[1]),forReal);
        } else if (strx[0]=='p') { 
            drive_value(&(strx[1]),s4,forReal);
            s1[0]=0;
            s2[0]=0;
            s3[0]=0;
            s4[0]=0;
        } else if (strx[0]=='b') { 
            strcpy(Valex,&(strx[1]));
        } else if (strx[0]=='r') { 
            strcpy(Valex,strx);
        }
    } else {
        drive_value(Valex,strx,forReal);
        Valex[0]=0;
    }
}

long zerox = -1;

void record(long code,long bus,int width, long Kind) {
    char temp[1000];
    char fullname[1000];
    int ind,i,pcode;
    psig = intcode(qqia(code));
    if (psig>=maxsig) {
        printf("sigs code is larger then array, recompile (%s,%s,%d)\n",qqia(bus),qqia(code),psig);
        return;
    }
    if (psig>maxusedsig)
        maxusedsig = psig;
    sprintf(fullname,"%s.%s",qqia(getscope(temp)),qqia(bus));
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
    if (psig==0) zerox = FullName;
    fprintf(Frecords,"record psig=%d sig=%s code=%s kind=%s full=%s\n",psig,qqia(bus),qqia(code),qqia(Kind),fullname);
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
veri_changes(PyObject *self,PyObject *args) {
    if (!PyArg_ParseTuple(args, ""))
        return NULL;
    return Py_BuildValue("l", (long) Changes);
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
    char *pathstring,*val,*function,*offset;
    char Str[10000];
    long handle;
    Str[0]='x';
    Str[1]=0;
    int hasOffset = -1;
    printf(">>>>>>>>>>>>>>>>>>>>>>>>>>\n");
//    if (PyArg_ParseTuple(args, "sss",&pathstring,&val,&function))
//        hasOffset = 1;
    if (PyArg_ParseTuple(args, "ssss",&pathstring,&val,&function,&offset))
        hasOffset = 2;
    if (hasOffset<0) return NULL;

    if (strcmp(pathstring,"always")==0) {
        strcpy(functionTime,function);
        AlwaysMode = 1;
        return Py_BuildValue("s", "always");
    }

    if ((pathstring[0]<='9')&&(pathstring[0]>='0')) {
        startTime = atoi(pathstring);
        nextTriggerTime = atof(pathstring);
        deltaTime = atof(val);
        strcpy(functionTime,function);
        printf("install time based ||%s|| triggers start=%f delta=%f\n",Str,nextTriggerTime,deltaTime);
        return Py_BuildValue("s", Str);
    }

    long Psig =  qqas(qqai(pathstring));
    printf("install ||%s|| ptr=%d psig=%lu sensitive %s %s %s\n",Str,psensitive,Psig,pathstring,val,function);
    sensitives[psensitive] =Psig; 
    sensitive_command[psensitive] = qqai(function);
    sensitive_value[psensitive] = val[0];
    if (hasOffset) {
        sensitive_offset[psensitive] = atof(offset);
    }
    psensitive++;

    if (Psig==99999999) {
        printf("\npython: cannot find sig %s for sensitive\n",pathstring);
        printf("%lx  %lx   %s\n",zerox,qqai(pathstring),pathstring);
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
    long pp = qqai(pathstring);
    int this;
    if (qqas(pp) == 99999999) {
        qqsa(pp,vcdCode);
        codeint(vcdCode);
        fprintf(vcdF0,"$var reg 1 %s %s $end\n",codeintstr,pathstring);
        this = vcdCode;
        vcdCode += 1;
    }  else {
        this = qqas(pp);
        codeint(this);
    }
    int XX = atoi(vstr);
    char tmp[100];
    if (this>=1000) return Py_BuildValue("i", 0);
    int Wid = trace_widths[this];
    int2bin(XX,Wid,tmp);
    if (lastTraceTime<run_time) {
        fprintf(vcdF1,"#%ld\n",(long) run_time);
        lastTraceTime = run_time;
    }
    if (Wid>1) 
        fprintf(vcdF1,"b%s %s\n",tmp,codeintstr);
    else
        fprintf(vcdF1,"%c%s\n",tmp[0],codeintstr);

    return Py_BuildValue("i", 0);
}

static PyObject*
veri_peek(PyObject *self,PyObject *args) {
    char pvalue[100000];
    char pvalue2[100000];
    char *pathstring;
    if (!PyArg_ParseTuple(args, "s",&pathstring))
        return NULL;
    long Psig =  qqas(qqai(pathstring));

    if (Psig == 99999999) {
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
    char *notestring;
    if (!PyArg_ParseTuple(args, "s", &notestring))
        return NULL;
    int ii,jj=0;
    char tmp[1000];
    sprintf(tmp,"%s = []",notestring);
    PyRun_SimpleString(tmp);
    int tot = 0;
    for (ii=0; ii<=maxusedsig; ii++) {
        if (sigs[ii].toggles>0) {
//             sprintf(tmp,"%s.append((%d,'%s'))",notestring,sigs[ii].toggles,qqia(sigs[ii].fpath));
            sprintf(tmp,"addit((%d,%d,'%s'))",sigs[ii].toggles,sigs[ii].toggles2,qqia(sigs[ii].fpath));
            PyRun_SimpleString(tmp);
//            printf("TMP %s\n",tmp);
            tot += sigs[ii].toggles;
            sigs[ii].toggles = 0;
        }
    }
    return Py_BuildValue("i", tot);
}


static PyObject*
veri_changed(PyObject *self,PyObject *args) {
    char *notestring;
    if (!PyArg_ParseTuple(args, "s", &notestring))
        return NULL;
    int ii,jj=0;
    char tmp[1000];
    sprintf(tmp,"%s = []",notestring);
    PyRun_SimpleString(tmp);
    int tot = 0;
    for (ii=0; ii<=maxusedsig; ii++) {
        if (sigs[ii].changed) {
            sprintf(tmp,"%s.append(('%s'))",notestring,qqia(sigs[ii].fpath));
            PyRun_SimpleString(tmp);
            sigs[ii].changed = 0;
            tot ++;
        }
    }
    return Py_BuildValue("i", tot);
}



static PyMethodDef VeriMethods[] = {
    {"exists", veri_exists, METH_VARARGS, "Return the number of arguments received by the process."},
    {"peek", veri_peek, METH_VARARGS, "Return the number of arguments received by the process."},
    {"force", veri_force, METH_VARARGS, "tracing of new signals."},
    {"trace", veri_trace, METH_VARARGS, "tracing of new signals."},
    {"stime", veri_stime, METH_VARARGS, "Return the number of arguments received by the process."},
    {"changes", veri_changes, METH_VARARGS, "Return the number of arguments received by the process."},
    {"listing", veri_listing, METH_VARARGS, "Return the number of arguments received by the process."},
    {"sensitive", veri_sensitive, METH_VARARGS,"add to watch list"},
    {"finish", veri_finish, METH_VARARGS, "Return the number of arguments received by the process."},
    {"toggles", veri_toggles, METH_VARARGS, "Return the number of arguments received by the process."},
    {"changed", veri_changed, METH_VARARGS, "Return the number of arguments received by the process."},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef veri_module_definition =
{
    PyModuleDef_HEAD_INIT,
    "veri", /* name of module */
    "",          /* module documentation, may be NULL */
    -1,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    VeriMethods,
    NULL,
    NULL,
    NULL,
    NULL,
};

PyMODINIT_FUNC PyInit_veri(void)
{

    return PyModule_Create(&veri_module_definition);
}







PyObject *globals;
PyObject *locals;
void start_python() {
    char temp[10000];
    PyImport_AppendInittab("veri", PyInit_veri);
    Py_Initialize();
    if (toggles) 
        sprintf(temp,"toggles = True\nINITFILE = '%s'\n%s",fname2,scriptStart);
    else
        sprintf(temp,"toggles = False\nINITFILE = '%s'\n%s",fname2,scriptStart);
    PyRun_SimpleString(temp);
    globals = PyDict_New();
    if (!globals) exit(2);
    PyDict_SetItemString(globals, "__builtins__", PyEval_GetBuiltins());
    locals = Py_BuildValue("{}");
    python_started = 1;
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

int diffs (char *A, char *B) {
    int Diff = 0;
    int ind;
    for (ind=0;A[ind]!=0;ind++) {
        if (A[ind]!=B[ind]) Diff++;
    }
    return Diff;
}


