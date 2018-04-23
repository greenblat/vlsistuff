



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

#define maxsig 500000

FILE *inf;
FILE *Frecords;
int intcode();
void do_help() { exit(0); }
void check_x(int i) { return; }
void do_dumpvars(char *s) { return; }

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

double start_time=0.0;
double end_time=0.0;
int state=Idle;
double run_time=0.0;
int linenum;
int LASTCHANGE=0;
int search=0;

int maxusedsig;
int debug;



int psig=1;
typedef struct SIG {
    long name;
    long value;
    int code;
    long path;
    long fpath;
} change_sig;

 change_sig sigs[maxsig];




char scriptStart[] = "\n\
import string,os,sys\n\
import traceback \n\
sys.path=sys.path+['./']\n\
import veri\n\
print 'python starting'\n\
\n\
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







char Valex[16000];




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
    for (i=0;i<maxsig;i++) { sigs[i].code=-1;} 
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
    long xxx = qqai("x");
    for (i=0;i<maxsig;i++) {
        sigs[i].value = xxx;
    }
        

    readfile(fname1);
    exit(0);
}






void readfile(fname) char *fname; {
    char *j;
    char line[1000];
    int i;
    int guard=0;
    char s1[10000];
    char s2[10000];
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
        j = fgets(line, 4999, inf);
        linenum++;
        guard++;
        if (guard>999999) { guard=0;printf("%d lines %g %d max=%d\n",linenum,run_time,0,maxusedsig);}
        if (j == NULL) {
            return;
        }
        i=sscanf(line,"%s %s %s %s %s %s %s",s1,s2,s3,s4,s5,s6,s7);
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
}
int instate;
void pushtok(char *s,int ind) {
    int pr;
    long n;
    if ((ind==1)&&(s[0]=='#')) {
        run_time=atof(&(s[1]));
        LASTCHANGE++;
        if ((run_time>=0)&&(run_time<start_time)&&(search)) search_time(start_time);
        state=Values;
        return;
    }
    instate++;
//    printf("state=%d str=%s\n",state,s);
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
        else if (n==qqai("$dumpvars")) { 
            state=Dumpvars;
            search=1;
        } else if (s[0]=='#') {
            state=Values;
            do_value(s);
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
                ||(n==qqai("event"))
            ) break;
            shouldbe("wire",n); break;
        case 2:
            break;
        case 3:
            code=n; break;
        case 4:
            bus=n; break;
        case 5:
            if (n==qqai("$end")) { state=Idle;record(code,bus);}
            else {
                if (n==qqai("[-1]")) {
                    record(code,bus);
                } else {
                    strcpy(temp,qqia(n));
                    if (temp[0]=='[') {
                        int j;
                        for (j=1;(temp[j]&&(temp[j]!=':'));j++);
                        if (temp[j-1]==']') {
                            sprintf(temp,"%s%s",qqia(bus),qqia(n));
                            record(code,qqai(temp));
                        } else if (temp[j]==':') {
                            strcpy(temp2,&(temp[1]));
                            temp2[j-1]=0;
                            strcpy(temp2,&(temp[j+1]));
                            temp2[strlen(temp2)-1]=0;
                            record(code,bus);
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
        } else {
            sig = intcode(&(line[1]));
            if ((sig>0)&&(sig<=maxsig))
                sigs[sig].value=line[0];
        }
    }
}


int intcode(char *st) {
    int cur,i,res=0,machpil=1,more;
    for (i=0;(st[i]!=0)&&(st[i]!='\n');i++) {
        cur = (1+st[i]-'!');
        if ((cur>=0)&&(cur<=94)) {
            more = cur*machpil;
            res += more;
            machpil *= 94;
        }
    }
    return res;
}

long sensitives[100];
char sensitive_value[100];
long sensitive_command[100];
int psensetive=0;

void drive_value(char *Val,char *Code) {
    int P = intcode(Code);
    char Bus[1000];
    strcpy(Bus,qqia(sigs[P].name));
    sigs[P].value = qqai(Val);
//    printf("code=%d sig=%s val=%s time=%f\n",P,qqia(sigs[P].fpath),Val,run_time);
    for (int ii=0;ii<psensetive;ii++) {
//        printf("sense ii=%d P=%u S=%lu       %c %c\n",ii,P,sensitives[ii],sensitive_value[ii],Val[0]);
        if ((sensitives[ii]==P)&&(sensitive_value[ii]==Val[0])) {
            PyRun_SimpleString(qqia(sensitive_command[ii]));
            return;
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


void record(long code,long bus) {
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
    long FullName = qqai(fullname);
    if (sigs[psig].code== -1) {
        sigs[psig].name=bus;
        sigs[psig].code=code;
        sigs[psig].path=scopes[pscope-1];
        sigs[psig].fpath=FullName;
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
    Str[1]='0';
    if (!PyArg_ParseTuple(args, "sss",&pathstring,&val,&function))
        return NULL;

    long Psig =  qqas(qqai(pathstring));
    printf("install ptr=%d psig=%lu sensitive %s %s %s\n",psensetive,Psig,pathstring,val,function);
    sensitives[psensetive] =Psig; 
    sensitive_command[psensetive] = qqai(function);
    sensitive_value[psensetive] = val[0];
    psensetive++;

    if (Psig==0) {
        printf("\npython: cannot find sig %s for peek\n",pathstring);
        return Py_BuildValue("s", "q");
    }
    return Py_BuildValue("s", Str);
}


static PyObject*
veri_peek(PyObject *self,PyObject *args) {
    char pvalue[10000];
    char *pathstring;
    if (!PyArg_ParseTuple(args, "s",&pathstring))
        return NULL;
    long Psig =  qqas(qqai(pathstring));


    if (!Psig) {
        printf("\npython: cannot find sig %s for peek\n",pathstring);
        return Py_BuildValue("s", "q");
    }
    strcpy(pvalue,qqia(sigs[Psig].value));
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




static PyMethodDef VeriMethods[] = {
    {"exists", veri_exists, METH_VARARGS, "Return the number of arguments received by the process."},
    {"peek", veri_peek, METH_VARARGS, "Return the number of arguments received by the process."},
    {"stime", veri_stime, METH_VARARGS, "Return the number of arguments received by the process."},
    {"listing", veri_listing, METH_VARARGS, "Return the number of arguments received by the process."},
    {"sensitive", veri_sensitive, METH_VARARGS,"add to watch list"},
    {"finish", veri_finish, METH_VARARGS,
     "Return the number of arguments received by the process."},
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


