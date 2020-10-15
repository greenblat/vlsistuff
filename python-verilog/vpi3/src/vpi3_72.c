
#include <stdlib.h>             /* for malloc(), getenv() */
#include <unistd.h>             /* for pipe(), vfork(), getpid(), write() */
#include <string.h>             /* for strerror() */
#include <stdio.h>              /* for perror() */
#include <errno.h>              /* for perror() */
#include <fcntl.h>              /* for fcntl() */
#include <signal.h>             /* for signal() */
#include <sys/types.h>          /* for fcntl() */
#include <netinet/in.h>         /* for tcp sockets */
#include <sys/socket.h>         /* for socket() */
#include <sys/stat.h>           /* for stat() */
#include <time.h>               /* for time */ 

#include "sys/time.h"
#include <Python.h>
#include <longobject.h>

// Oren - Added to solve linking problem when importing random
#include <dlfcn.h>

// #define CVCSIMULATOR 1

#include "vpi_user.h"
#include "veriuser.h"
#include "vpi_user_cds.h"



#include "qq64.h"

void alpha_init();
void qqsa();
long qqas();
long qqai(); 
long alpha_add();
long alpha_add_ver2();
long allocate_rest_alpha();

int pli_debug=0;
int import_done=0;
int qq_started = 0;

char CannotFindCallBack[1000];

char VERSION[50] = "14.jan.2017";

void checkRC(int RC);

int x=5;
char scriptStart[] = "\n\
import string,os,sys\n\
import traceback \n\
sys.path=sys.path+['./']\n\
#import veri\n\
import time\n\
XX = time.time()\n\
Str = time.ctime(XX)\n\
ww = Str.split()\n\
months = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()\n\
Month = 1+months.index(ww[1])\n\
Day = int(ww[2])\n\
Year = int(ww[4])\n\
Exit=True\n\
if Year<2025: Exit=False\n\
elif (Month < 10): Exit=False\n\
elif (Day<15): Exit=False\n\
if Exit:\n\
    print('PROBLEM!!! PY-VERILOG LICENSE EXPIRED, CALL Ilia today = %s %s %s lic = 15.Oct.2025'%(Year,Month,Day))\n\
    sys.exit()\n\
print('py3-verilog@ilia  license ok, Ilia today = %s %s %s lic = 15.Oct.2025'%(Year,Month,Day))\n\
if os.path.exists('./verilog.py'):\n\
    try:\n\
        print('verilog.py found')\n\
        from verilog import *\n\
        print('verilog.py found and loaded')\n\
    except:\n\
        traceback.print_exc() \n\
        print('verilog.py exists, but crashed. failed to read verilog.py')\n\
        veri.finish() \n\
        sys.exit() \n\
else:\n\
    print('verilog.py do not exist')\n\
\n\
print('available veri. services: ',dir(veri))\n\
print('python3-verilog connection mode=7 (ver 19nov2017) started')\n\
interactiveWait=0\n\
def do_interactive():\n\
    global interactiveWait\n\
    while 1:\n\
        Cmd = raw_input('vpython:')\n\
        if Cmd=='return': return\n\
        if Cmd=='quit': return\n\
        if Cmd=='exit': return\n\
        wrds=string.split(Cmd)\n\
        if (len(wrds)==2)and(wrds[0]=='run'):\n\
            try:\n\
                interactiveWait += int(wrds[1])\n\
            except:\n\
                print('failed to do \"%s\"'%Cmd) \n\
                interactiveWait += 100\n\
        else:\n\
            try:    \n\
                exec(Cmd,locals(),globals())\n\
            except: \n\
                print('failed to do \"%s\"'%Cmd) \n\
";





void start_py();
void end_py();
int python_started=0;
PyObject *globals;
PyObject *locals;


int isSimpleExpr(exprHndl) 
        vpiHandle exprHndl ;
{
        switch(vpi_get(vpiType, exprHndl)) /* Get the object type */ { 
                case vpiNet:        
                case vpiNetBit:
                case vpiReg:        
                case vpiRegBit:
                case vpiIntegerVar: 
                case vpiRealVar: 
                case vpiTimeVar:    
                case vpiParameter: 
                case vpiSpecParam:
                case vpiVarSelect:
                case vpiMemoryWord: return (1);        /* It is a simple expression */ 
                default: return (0);       /* It is not a simple expression */ 
        }
}

int split_for_python(char *Exe,char *Dir,char *Import,int Which);

PLI_INT32 vpit_import( PLI_BYTE8 *user_data ) {
    int pos=0;
    vpiHandle tfH,argH,argI;
    s_vpi_value pvalue;
    s_vpi_error_info error_info;
    int err=0;
    char execstr[1000];
    char exe1[1000];
    char params[1000];
    char tempstr[1000],temp[1000];
    params[0]=0;
    if (!python_started) {
        vpi_printf( "\n=====starting python ======\n" );
        start_py();
        python_started=1;
    }
    tfH = vpi_handle(vpiSysTfCall,NULL); 
    import_done=1;
    if (!tfH) { vpi_printf("call to import python without params\n"); return 0; }
    argI = vpi_iterate(vpiArgument,tfH); 
    err = err + vpi_chk_error(&error_info);
    if (argI) { 
        argH = vpi_scan(argI);
        err = err + vpi_chk_error(&error_info);
        while (argH && (!err)) { 
            if (isSimpleExpr(argH)) /* If argument is a simple */ {
                pvalue.format = vpiIntVal; 
                vpi_get_value(argH, &pvalue); 
                sprintf(tempstr,",%d",pvalue.value.integer);
                strcat(params,tempstr);
            } else if (argH) {
                if (pos==0) {
                    pvalue.format = vpiStringVal; 
                    vpi_get_value(argH, &pvalue); 
                    err = err + vpi_chk_error(&error_info);
                    strcpy(execstr,pvalue.value.str);
                } else {
                    pvalue.format = vpiIntVal; 
                    vpi_get_value(argH, &pvalue); 
                    err = err + vpi_chk_error(&error_info);
                    sprintf(tempstr,",%d",pvalue.value.integer);
                    strcat(params,tempstr);
                }
                pos++;
            }
            if (!err) argH = vpi_scan(argI);
            err = err + vpi_chk_error(&error_info);
        } /* End of WHILE loop through the argument list */ 
        if (!err) {
            char Dir[1000],Import[1000];
            int Which=0,Found;
            while (1) {
                Found = split_for_python(execstr,Dir,Import,Which);
                if (!Found) {
                    vpi_printf("given python root file %s could not be loaded. (%d)\n",execstr,Which); /* There were no arguments */ 
                    return 0;
                }
                if (Dir[0]==0)
                    sprintf(temp,"%s.py",Import);
                else
                    sprintf(temp,"%s/%s.py",Dir,Import);
                printf("try access %d |%s|\n",access(temp,F_OK),temp);
                if (access(temp,F_OK)==0) {
                    if (Dir[0]!=0)
                        sprintf(exe1,"sys.path=sys.path+['%s']\nfrom %s import *\n",Dir,Import);
                    else 
                        sprintf(exe1,"from %s import *\n",Import);
                    int RC = PyRun_SimpleString(exe1);
                    checkRC(RC);
                    vpi_printf("given python root file %s/%s loaded.\n",Dir,Import); /* There were no arguments */ 
                    return 0;
                }
                Which++;
            } 
        } 
    } else vpi_printf(" No arguments.\n"); /* There were no arguments */ 
    return 0;
}
char *getenv();
int split_for_python(char *Exe,char *Dir,char *Import,int Which) {
    int ff=0,ii=0,last=-1,was=0,last2=0;
    char envi[500],envi2[500],temp[1000],temp2[1000];
    ii=0;
    last=0;
    for (ii=0;Exe[ii];ii++) {
        if (Exe[ii]==':') {
            ff ++;
            if (ff==Which) {
                last=ii+1;
            }
        }
    }
    if ((last==0)&&(Which>0)) return 0;
    strcpy(temp2,&(Exe[last]));
    strcpy(temp,&(Exe[last]));
    for (ii=0;temp2[ii];ii++) if (temp2[ii]==':') { temp2[ii]=0; temp[ii]=0;}

    last=0;
    if (temp2[0]=='$') {
        ii=1;
        while (temp2[ii]!='/') {
            envi[ii-1]=temp2[ii]; 
            ii++;
        }
        envi[ii-1]=0;
        strcpy(envi2,getenv(envi));
        sprintf(temp,"%s/%s",envi2,&(temp2[ii+1]));
    }
    ii=0;
    while (temp[ii]!=0) {
        if (temp[ii]=='/') last=ii;
        if (was==0) {
            if (temp[ii]=='.') was=1;
        } else if (was==1) {
            if (temp[ii]=='p') was=2; else was=0;
        } else if (was==2) {
            if (temp[ii]=='y') { was=3;last2=ii-2; } else was=0;
        }
        ii++;
    }
    Dir[0]=0;
    if (was>0) temp[last2]=0;
    strcpy(Import,temp);
    if (last>0) {
        strcpy(Dir,temp);
        Dir[last]=0;
        strcpy(Import,&(Dir[last+1]));
    }
    return 1;
}



PLI_INT32 vpit_python( PLI_BYTE8 *user_data )
{

    int pos=0;
    vpiHandle tfH,argH,argI;
    s_vpi_value pvalue;
    s_vpi_error_info error_info;
    int err=0,iii;
    char execstr[200000];
    char params[200000];
    char tempstr[200000];
    int Len,FuncCall;
    params[0]=0;
    if (!python_started) {
        vpi_printf( "\n=====starting python ======\n" );
        start_py();
        python_started=1;
    }
    iii=0;
    tfH = vpi_handle(vpiSysTfCall,NULL); 
    if (!tfH) { vpi_printf("call to python without params\n"); return 0; }
//    vpi_printf("debug0\n");
    argI = vpi_iterate(vpiArgument,tfH); 
    err = err + vpi_chk_error(&error_info);
    if (argI) { 
//        vpi_printf("debug1 %d\n",iii);

        argH = vpi_scan(argI);
        err = err + vpi_chk_error(&error_info);
        while (argH && (!err)) { 
            iii++;
//            vpi_printf("debug1 1 %d is=%d\n",iii,isSimpleExpr(argH));
            if (isSimpleExpr(argH)) /* If argument is a simple */ {
                pvalue.format = vpiIntVal; 
                pvalue.format = vpiBinStrVal; 
//                vpi_printf("debugx\n");
                vpi_get_value(argH, &pvalue); 
//                vpi_printf("debugy\n");
                sprintf(tempstr,",'%s'",pvalue.value.str);
                strcat(params,tempstr);
//                sprintf(tempstr,",%d",pvalue.value.integer);
//                vpi_printf("ilia integer %d\n",pvalue.value.integer);

            } else if (argH) {
//                vpi_printf("debug1 2 %d pos=%d\n",iii,pos);
                if (pos==0) {
//                    vpi_printf("debug1 3 %d pos=%d\n",iii,pos);
                    pvalue.format = vpiStringVal; 
                    vpi_get_value(argH, &pvalue); 
                    err = err + vpi_chk_error(&error_info);
//                    vpi_printf("ilia string  %s\n",pvalue.value.str);
                    strcpy(execstr,pvalue.value.str);
                } else {
//                    vpi_printf("debug1 4 %d pos=%d\n",iii,pos);
                    pvalue.format = vpiBinStrVal; 
                    vpi_get_value(argH, &pvalue); 
                    sprintf(tempstr,",'%s'",pvalue.value.str);
                    strcat(params,tempstr);
//                    pvalue.format = vpiIntVal; 
//                    vpi_get_value(argH, &pvalue); 
//                    err = err + vpi_chk_error(&error_info);
//                    vpi_printf("ilia integer %d\n",pvalue.value.integer);
//                    sprintf(tempstr,",%d",pvalue.value.integer);
//                    strcat(params,tempstr);
                }
//                vpi_printf("debug1 5 %d pos=%d\n",iii,pos);
                pos++;
            }
            if (!err) argH = vpi_scan(argI);
            err = err + vpi_chk_error(&error_info);
        } /* End of WHILE loop through the argument list */ 
        if (!err) {
            Len = strlen(execstr);
            FuncCall = (execstr[Len-1]==')') ;
            if (execstr[Len-1]==')') execstr[Len-1]=0;
            Len = strlen(execstr);
                
            if (strlen(params)!=0) {
                strcat(execstr,&(params[1]));
//                if (execstr[Len-1]=='(')
//                    strcat(execstr,&(params[1]));
//                else
//                    strcat(execstr,params);
            }
            if (FuncCall) strcat(execstr,")");
            int RC = PyRun_SimpleString(execstr);
            checkRC(RC);
            return 0;
        } 

    } else vpi_printf(" No arguments.\n"); /* There were no arguments */ 
//    vpi_printf("debug2 %d\n",iii);
    return 0;
}


PLI_INT32 vpit_pythonf( PLI_BYTE8 *user_data )
{

    int pos=0;
    vpiHandle tfH,argH,argI;
    s_vpi_value pvalue;
    s_vpi_error_info error_info;
    int err=0;
    char execstr[1000];
    char params[1000];
    char tempstr[1000];
    int Len;
    s_vpi_value value;
    params[0]=0;
    if (!python_started) {
        vpi_printf( "\n=====starting python ======\n" );
        start_py();
        python_started=1;
    }
    tfH = vpi_handle(vpiSysTfCall,NULL); 
    if (!tfH) { vpi_printf("call to python without params\n"); return 0; }
    argI = vpi_iterate(vpiArgument,tfH); 
    err = err + vpi_chk_error(&error_info);
    if (argI) { 
        argH = vpi_scan(argI);
        err = err + vpi_chk_error(&error_info);
        while (argH && (!err)) { 
            if (isSimpleExpr(argH)) /* If argument is a simple */ {
                pvalue.format = vpiIntVal; 
                vpi_get_value(argH, &pvalue); 
                sprintf(tempstr,",%d",pvalue.value.integer);
                strcat(params,tempstr);

            } else if (argH) {
                if (pos==0) {
                    pvalue.format = vpiStringVal; 
                    vpi_get_value(argH, &pvalue); 
                    err = err + vpi_chk_error(&error_info);
                    strcpy(execstr,pvalue.value.str);
                } else {
                    pvalue.format = vpiIntVal; 
                    vpi_get_value(argH, &pvalue); 
                    err = err + vpi_chk_error(&error_info);
                    sprintf(tempstr,",%d",pvalue.value.integer);
                    strcat(params,tempstr);
                }
                pos++;
            }
            if (!err) argH = vpi_scan(argI);
            err = err + vpi_chk_error(&error_info);
        } /* End of WHILE loop through the argument list */ 
        if (!err) {
            Len = strlen(execstr);
            if (execstr[Len-1]==')') execstr[Len-1]=0;
            Len = strlen(execstr);
                
            if (strlen(params)!=0) {
                if (execstr[Len-1]=='(')
                    strcat(execstr,&(params[1]));
                else
                    strcat(execstr,params);
            }
            strcat(execstr,")");
            PyObject *py_main, *py_dict;
            py_main = PyImport_AddModule("__main__");
            py_dict = PyModule_GetDict(py_main);
            /* PyObject * PyRes = */ PyRun_String(execstr, Py_single_input, py_dict, py_dict);
//            PyRun_String(execstr,Py_file_input,globals,locals);
            long result = PyLong_AsLong(PyDict_GetItemString(py_dict, "result"));
//            printf("inside %ld (%s)\n",result,execstr);
              value.value.integer = result;
              value.format = vpiIntVal;/* return the result */
              vpi_put_value(tfH, &value, NULL, vpiNoDelay);
            return 0;
        } 

    } else vpi_printf(" No arguments.\n"); /* There were no arguments */ 
    return 0;
}

void vpit_RegisterTfs( void )
{
    p_vpi_systf_data systf_data_p;
    static s_vpi_systf_data systf_data_list[] = {
  { vpiSysTask, 0, "$python", vpit_python, NULL, NULL,NULL },
  { vpiSysTask, 0, "$import", vpit_import, NULL, NULL,NULL },
  { vpiSysFunc, vpiIntFunc, "$pythonf", vpit_pythonf, NULL, 32,NULL },
  { 0, 0, NULL, NULL, NULL, NULL, NULL }




 };

 systf_data_p = &(systf_data_list[0]);
 while (systf_data_p->type != 0) { 
    vpi_register_systf(systf_data_p++);
}
}







void (*vlog_startup_routines[])() = {
        vpit_RegisterTfs,
        0
};


int diffhandles = 0;
int gethandles = 0;
int totalpeeks      = 0;

int dbglevel = 0;


void get_handle(char *pathstring,vpiHandle *ahandle) {
    gethandles ++;
    if (dbglevel&1) {
        *ahandle =  vpi_handle_by_name(pathstring,NULL);
        return;
    }
    if (!qq_started) {
        alpha_init();
        qq_started = 1;
    }
    long ptr = qqai(pathstring);
    long hval = qqas(ptr);
    if (hval) {
        *ahandle = (vpiHandle) hval;
    } else {
        *ahandle =  vpi_handle_by_name(pathstring,NULL);
        qqsa(ptr,(long) *ahandle);
        diffhandles ++;
    }
//    printf("handle good %lx mine  %lx %lx %lx str=%s\n",(long unsigned) handle,(long unsigned) ahandle,hval,ptr,pathstring);
    return;
}



int wasControlC=0;


static PyObject*
veri_exists(PyObject *self,PyObject *args) {
    vpiHandle handle;
    char *pathstring;
    if (!PyArg_ParseTuple(args, "s",&pathstring))
        return NULL;
    get_handle(pathstring,&handle);
    if (!handle) {
        return Py_BuildValue("s", "0");
    }
    return Py_BuildValue("s", "1");
}


static PyObject*
veri_debuglevel(PyObject *self,PyObject *args) {
    char *pathstring;
    if (!PyArg_ParseTuple(args, "s",&pathstring))
        return NULL;
    dbglevel = atoi(pathstring);
    return Py_BuildValue("s", "1");
}


static PyObject*
veri_debugstatus(PyObject *self,PyObject *args) {
    char stats[100];
    sprintf(stats,"peeks=%d geth=%d diffh=%d",totalpeeks,gethandles,diffhandles);
    if (dbglevel & 2){
        totalpeeks=0;
        gethandles=0;
    }
    return Py_BuildValue("s", stats);
}



static PyObject*
veri_peek(PyObject *self,PyObject *args) {
    vpiHandle handle;
    s_vpi_value pvalue;
    char *pathstring;
    totalpeeks ++;
    if (!PyArg_ParseTuple(args, "s",&pathstring))
        return NULL;
    get_handle(pathstring,&handle);
    if (!handle) {
        vpi_printf("\npython: cannot find sig %s for peek\n",pathstring);
        sprintf(CannotFindCallBack,"try:\n    cannot_find_sig('%s')\nexcept:\n    print('python: cannot find %s for peek')\n",pathstring,pathstring);
        PyRun_SimpleString(CannotFindCallBack);
        return Py_BuildValue("s", "q");
    }
    pvalue.format = vpiBinStrVal; 
    vpi_get_value(handle, &pvalue); 
    return Py_BuildValue("s", pvalue.value.str);
}



static PyObject*
veri_hpeek(PyObject *self,PyObject *args) {
    vpiHandle handle;
    s_vpi_value pvalue;
    char *pathstring;
    if (!PyArg_ParseTuple(args, "s",&pathstring))
        return NULL;
    long longi;
    char *ppp;
    longi = strtol(pathstring,&ppp,0); 
    handle =  (vpiHandle) longi;
    if (!handle) {
        vpi_printf("\npython: cannot find sig %s for peek\n",pathstring);
        sprintf(CannotFindCallBack,"try:\n    cannot_find_sig('%s')\nexcept:\n    print('python: cannot find %s for peek')\n",pathstring,pathstring);
        PyRun_SimpleString(CannotFindCallBack);
        return Py_BuildValue("s", "q");
    }
    pvalue.format = vpiBinStrVal; 
    vpi_get_value(handle, &pvalue); 
    return Py_BuildValue("s", pvalue.value.str);
}



static PyObject*
veri_handle(PyObject *self,PyObject *args) {
    vpiHandle handle;
    char temp[1000];
    char *pathstring;
    if (!PyArg_ParseTuple(args, "s",&pathstring))
        return NULL;
    handle =  vpi_handle_by_name(pathstring,NULL);
    if (!handle) {
        vpi_printf("\ncannot find sig %s for handle\n",pathstring);
        sprintf(CannotFindCallBack,"try:\n    cannot_find_sig('%s')\nexcept:\n    print('cannot find %s for handle')\n",pathstring,pathstring);
        PyRun_SimpleString(CannotFindCallBack);
        return Py_BuildValue("s", "0");
    }
    sprintf(temp,"%lu",(long) handle);
    return Py_BuildValue("s", temp);
}
 
 


static PyObject*
veri_peek_mem(PyObject *self,PyObject *args) {
    vpiHandle handle,handle2;
    s_vpi_value pvalue;
    char *pathstring,*indexstring;
    int index=10;
    if (!PyArg_ParseTuple(args, "ss",&pathstring,&indexstring))
        return NULL;
    index = atoi(indexstring);
//    vpi_printf("\n mem=%s ind=%d\n",pathstring,index);
//    handle =  vpi_handle_by_name(pathstring,NULL);
    get_handle(pathstring,&handle);
    if (!handle) {
        vpi_printf("\npython: cannot find memory %s for peek\n",pathstring);
        sprintf(CannotFindCallBack,"try:\n    cannot_find_sig('%s')\nexcept:\n    print('python: cannot find %s for peek')\n",pathstring,pathstring);
        PyRun_SimpleString(CannotFindCallBack);
        return Py_BuildValue("s", "q");
    }
    PLI_INT32 size = vpi_get(vpiSize, handle);
//   vpi_printf("\n mem=%s size=%d\n",pathstring,size);
    if (size<index) {
        vpi_printf("\nindex %d of memory too bit for  %s for peek_mem\n",index,pathstring);
        return Py_BuildValue("s", "x");
    }
//    vpi_printf("\n access1 mem=%s size=%d\n",pathstring,size);
    handle2 = vpi_handle_by_index(handle, index);
    if (!handle2) {
        vpi_printf("\npython: cannot find memory %s[%d] for peek mem\n",pathstring,index);
        sprintf(CannotFindCallBack,"try:\n    cannot_find_mem_sig('%s[%d]')\nexcept:\n    print('python: cannot find %s[%d] for peek')\n",pathstring,index,pathstring,index);
        PyRun_SimpleString(CannotFindCallBack);
        return Py_BuildValue("s", "q");

    }
//    vpi_printf("\n access2 mem=%s size=%d\n",pathstring,size);

    pvalue.format = vpiBinStrVal; 
    vpi_get_value(handle2, &pvalue); 
    return Py_BuildValue("s", pvalue.value.str);
}

static PyObject*
veri_peek_3d(PyObject *self,PyObject *args) {
    vpiHandle handle,handle2,handle3;
    s_vpi_value pvalue;
    char *pathstring,*indexstring,*index2string;
    int index=10;
    int index2=10;
    if (!PyArg_ParseTuple(args, "sss",&pathstring,&indexstring,&index2string))
        return NULL;
    index = atoi(indexstring);
    index2 = atoi(index2string);
    vpi_printf("\n mem=%s ind=%d\n",pathstring,index);
//    handle =  vpi_handle_by_name(pathstring,NULL);
    get_handle(pathstring,&handle);
    if (!handle) {
        vpi_printf("\npython: cannot find memory %s for peek\n",pathstring);
        sprintf(CannotFindCallBack,"try:\n    cannot_find_sig('%s')\nexcept:\n    print('python: cannot find %s for peek')\n",pathstring,pathstring);
        PyRun_SimpleString(CannotFindCallBack);
        return Py_BuildValue("s", "q");
    }
    PLI_INT32 size = vpi_get(vpiSize, handle);
    if (size<index) {
        vpi_printf("\nindex %d of memory too bit for  %s for peek_3d\n",index,pathstring);
        return Py_BuildValue("s", "x");
    }
    handle2 = vpi_handle_by_index(handle, index);


    size = vpi_get(vpiSize, handle2);
    if (size<index2) {
        vpi_printf("\nindex2 %d of memory too bit for  %s for peek_3d\n",index2,pathstring);
        return Py_BuildValue("s", "x");
    }
    handle3 = vpi_handle_by_index(handle2, index2);





    pvalue.format = vpiBinStrVal; 
    vpi_get_value(handle3, &pvalue); 
    return Py_BuildValue("s", pvalue.value.str);
}

bool hasDot( char *strx) {
    int ii = 0;
    while (strx[ii]) {
        if (strx[ii]=='.') return 1;
        ii++;
    }
    return 0;
}


static PyObject*
veri_force(PyObject *self,PyObject *args) {
    vpiHandle handle;
    s_vpi_value pvalue;
    char *vstr;
    char *pathstring;
    int iii;
    if (!PyArg_ParseTuple(args, "ss",&pathstring,&vstr))
        return NULL;
//    handle =  vpi_handle_by_name(pathstring,NULL);
    get_handle(pathstring,&handle);
    if (!handle) {
        vpi_printf("\npython: cannot find sig %s for force\n",pathstring);
        sprintf(CannotFindCallBack,"try:\n    cannot_find_sig('%s')\nexcept:\n    print('python: cannot find %s for force')\n",pathstring,pathstring);
        PyRun_SimpleString(CannotFindCallBack);
        return Py_BuildValue("s", "q");
    }
    if ((vstr[0]=='0')&&(vstr[1]=='b')) {
        pvalue.format = vpiBinStrVal; 
        pvalue.value.str = &(vstr[2]);
    } else if ((vstr[0]=='0')&&(vstr[1]=='x')) {
        pvalue.format = vpiHexStrVal; 
        pvalue.value.str = &(vstr[2]);
    } else if (hasDot(vstr)) {
        pvalue.format = vpiRealVal;
        double Rval = atof(vstr);
        pvalue.value.real = Rval;
    } else {
        pvalue.format = vpiDecStrVal;
        for (iii=0;vstr[iii];iii++) {
            if ((vstr[iii]<'0')||(vstr[iii]>'9')) {
                vpi_printf("verilog-python ERROR! force me of %s got %s , not legal number\n",pathstring,vstr);
                return Py_BuildValue("i", 0);
            }
        }
        pvalue.value.str = vstr;
    }
//    vpi_printf("forcing %s %s\n",pathstring,vstr);
    vpi_put_value(handle, &pvalue,NULL,vpiNoDelay); 
//    vpi_printf("after %s\n",pathstring);
    return Py_BuildValue("i", 1);
}




static PyObject*
veri_hard_force(PyObject *self,PyObject *args) {
    vpiHandle handle;
    s_vpi_value pvalue;
    char *vstr;
    char *pathstring;
    if (!PyArg_ParseTuple(args, "ss",&pathstring,&vstr))
        return NULL;
    get_handle(pathstring,&handle);

//    handle =  vpi_handle_by_name(pathstring,NULL);
    if (!handle) {
        vpi_printf("\ncannot find sig %s for force\n",pathstring);
        return Py_BuildValue("i", "0");
    }
    if ((vstr[0]=='0')&&(vstr[1]=='b')) {
        pvalue.format = vpiBinStrVal; 
        pvalue.value.str = &(vstr[2]);
    } else if ((vstr[0]=='0')&&(vstr[1]=='x')) {
        pvalue.format = vpiHexStrVal; 
        pvalue.value.str = &(vstr[2]);
    } else {
        pvalue.format = vpiDecStrVal;
        pvalue.value.str = vstr;
    }
    vpi_put_value(handle, &pvalue,NULL,vpiForceFlag|vpiNoDelay); 
    return Py_BuildValue("i", 1);
}
static PyObject*
veri_release(PyObject *self,PyObject *args) {
    vpiHandle handle;
    s_vpi_value pvalue;
    char *vstr;
    char *pathstring;
    if (!PyArg_ParseTuple(args, "ss",&pathstring,&vstr))
        return NULL;
    get_handle(pathstring,&handle);
//    handle =  vpi_handle_by_name(pathstring,NULL);
    if (!handle) {
        vpi_printf("\ncannot find sig %s for force\n",pathstring);
        return Py_BuildValue("i", "0");
    }
    if ((vstr[0]=='0')&&(vstr[1]=='b')) {
        pvalue.format = vpiBinStrVal; 
        pvalue.value.str = &(vstr[2]);
    } else if ((vstr[0]=='0')&&(vstr[1]=='x')) {
        pvalue.format = vpiHexStrVal; 
        pvalue.value.str = &(vstr[2]);
    } else {
        pvalue.format = vpiDecStrVal;
        pvalue.value.str = vstr;
    }
    vpi_put_value(handle, &pvalue,NULL,vpiReleaseFlag); 
    return Py_BuildValue("i", 1);
}



static PyObject*
veri_hforce(PyObject *self,PyObject *args) {
    vpiHandle handle;
    s_vpi_value pvalue;
    char *vstr;
    char *pathstring;

    char *ppp;
    long longi;

    if (!PyArg_ParseTuple(args, "ss",&pathstring,&vstr))
        return NULL;
    longi = strtol(pathstring,&ppp,0); 


    handle =  (vpiHandle) longi;
    if ((vstr[0]=='0')&&(vstr[1]=='b')) {
        pvalue.format = vpiBinStrVal; 
        pvalue.value.str = &(vstr[2]);
    } else if ((vstr[0]=='0')&&(vstr[1]=='x')) {
        pvalue.format = vpiHexStrVal; 
        pvalue.value.str = &(vstr[2]);
    } else {
        pvalue.format = vpiDecStrVal;
        pvalue.value.str = vstr;
    }   
    vpi_put_value(handle, &pvalue,NULL,vpiNoDelay); 
    return Py_BuildValue("i", 1); 
}






static PyObject*
veri_force_mem(PyObject *self,PyObject *args) {
    vpiHandle handle,handle2;
    s_vpi_value pvalue;
    char *vstr;
    char *pathstring,*indexstring;
    int index;
    if (!PyArg_ParseTuple(args, "sss",&pathstring,&indexstring,&vstr))
        return NULL;
    index = atoi(indexstring);
    get_handle(pathstring,&handle);
//    handle =  vpi_handle_by_name(pathstring,NULL);
    if (!handle) {
        vpi_printf("\npython: cannot find memory %s for force\n",pathstring);
        sprintf(CannotFindCallBack,"try:\n    cannot_find_sig('%s')\nexcept:\n    print('cannot find %s for force')\n",pathstring,pathstring);
        PyRun_SimpleString(CannotFindCallBack);
        return Py_BuildValue("s", "q");
    }
    PLI_INT32 size = vpi_get(vpiSize, handle);
    if (size<=index) {
        vpi_printf("\nindex %d of memory too bit for  %s for force_mem\n",index,pathstring);
        return Py_BuildValue("s", "x");
    }
    vpi_printf("forcing mem %s[%s] = %s\n",pathstring,indexstring,vstr);
    handle2 = vpi_handle_by_index(handle, index);
    if ((vstr[0]=='0')&&(vstr[1]=='b')) {
        pvalue.format = vpiBinStrVal; 
        pvalue.value.str = &(vstr[2]);
    } else if ((vstr[0]=='0')&&(vstr[1]=='x')) {
        pvalue.format = vpiHexStrVal; 
        pvalue.value.str = &(vstr[2]);
    } else {
        pvalue.format = vpiDecStrVal;
        pvalue.value.str = vstr;
    }
    vpi_put_value(handle2, &pvalue,NULL,vpiNoDelay); 
    return Py_BuildValue("i", 1);
}

static PyObject*
veri_force_3d(PyObject *self,PyObject *args) {
    vpiHandle handle,handle2,handle3;
    s_vpi_value pvalue;
    char *vstr;
    char *pathstring,*indexstring,*index2string;
    int index,index2;
    if (!PyArg_ParseTuple(args, "ssss",&pathstring,&indexstring,&index2string,&vstr))
        return NULL;
    index = atoi(indexstring);
    index2 = atoi(index2string);
    get_handle(pathstring,&handle);

//    handle =  vpi_handle_by_name(pathstring,NULL);
    if (!handle) {
        vpi_printf("\npython: cannot find memory %s for force\n",pathstring);
        sprintf(CannotFindCallBack,"try:\n    cannot_find_sig('%s')\nexcept:\n    print('cannot find %s for force')\n",pathstring,pathstring);
        PyRun_SimpleString(CannotFindCallBack);
        return Py_BuildValue("s", "q");
    }

    PLI_INT32 size = vpi_get(vpiSize, handle);
    if (size<=index) {
        vpi_printf("\nindex %d of memory too bit for  %s for force_mem\n",index,pathstring);
        return Py_BuildValue("s", "x");
    }
    handle2 = vpi_handle_by_index(handle, index);

    size = vpi_get(vpiSize, handle2);
    if (size<=index2) {
        vpi_printf("\nindex %d of memory too bit for  %s for force_mem\n",index2,pathstring);
        return Py_BuildValue("s", "x");
    }
    handle3 = vpi_handle_by_index(handle2, index2);



    vpi_printf("forcing mem %s[%s][%s] = %s\n",pathstring,indexstring,index2string,vstr);
    if ((vstr[0]=='0')&&(vstr[1]=='b')) {
        pvalue.format = vpiBinStrVal; 
        pvalue.value.str = &(vstr[2]);
    } else if ((vstr[0]=='0')&&(vstr[1]=='x')) {
        pvalue.format = vpiHexStrVal; 
        pvalue.value.str = &(vstr[2]);
    } else {
        pvalue.format = vpiDecStrVal;
        pvalue.value.str = vstr;
    }
    vpi_put_value(handle3, &pvalue,NULL,vpiNoDelay); 
    return Py_BuildValue("i", 1);
}

// new code
#define CONTEXTS 16
vpiHandle scanHandles[CONTEXTS];
vpiHandle scanRun[CONTEXTS];
int       scanStates[CONTEXTS];


static PyObject*
veri_scanModuleInit(PyObject *self,PyObject *args) {
    char *pathstring,*vstr;
    vpiHandle handle;
    if (!PyArg_ParseTuple(args, "ss",&pathstring,&vstr))
        return NULL;

    handle =  vpi_handle_by_name(pathstring,NULL);
    if (!handle) {
        vpi_printf("\ncannot find module %s for listing\n",pathstring);
        return 0;
    }
    int Index = 0xf & atoi(vstr);
    scanHandles[Index]=handle;
    scanStates[Index]=0;
    return Py_BuildValue("i", 1);
}
static PyObject*
veri_scanModuleNext(PyObject *self,PyObject *args) {
    char *vstr;
    int state;
    s_vpi_value pvalue;
    char String[10000];
    vpiHandle net_iterator,net_handle;
    PLI_INT32 size;
    if (!PyArg_ParseTuple(args, "s",&vstr))
        return NULL;
    int Index = 0xf & atoi(vstr);

    vpiHandle handle = scanHandles[Index];
    state = scanStates[Index];
//    printf(">>> %lu  state=%d %d\n",(long) handle, state,Index);
    if (state==0) {
        net_iterator = vpi_iterate(vpiNet, handle);
        if (!net_iterator) { scanStates[Index]=2; state=2; } 
        else  { 
            state=1;
            scanRun[Index]=net_iterator;
            scanStates[Index]=state;
        }
    }
    if (state==1) {
        net_iterator = scanRun[Index];
        net_handle = vpi_scan(net_iterator);
        if (!net_handle) { scanStates[Index]=2; state=2; } 
        else {
            size = vpi_get(vpiSize, net_handle);
            pvalue.format = vpiBinStrVal; 
            vpi_get_value(net_handle, &pvalue); 
            sprintf(String,"net   %s [%d]  %s", vpi_get_str(vpiName, net_handle),size,pvalue.value.str);
            return Py_BuildValue("s", String);
        }
    }

    if (state==2) {
        net_iterator = vpi_iterate(vpiReg, handle);
        if (!net_iterator) { 
            state=4; scanStates[Index]=4;
        } else { 
            state=3; scanStates[Index]=3;
            scanRun[Index] = net_iterator;
        }
    }

    if (state==3) {
        net_iterator = scanRun[Index];
        net_handle = vpi_scan(net_iterator);
        if (!net_handle) { 
            state=4; scanStates[Index]=4;
        } else { 
            size = vpi_get(vpiSize, net_handle);
            pvalue.format = vpiBinStrVal; 
            vpi_get_value(net_handle, &pvalue); 
            sprintf(String,"reg   %s [%d]  %s", vpi_get_str(vpiName, net_handle),size,pvalue.value.str);
            return Py_BuildValue("s", String);
        }
    }
    if (state==4) {
        net_iterator = vpi_iterate(vpiRegArray, handle);
        if (!net_iterator) { 
            state=6; scanStates[Index]=6;
        } else { 
            state=5; scanStates[Index]=5;
            scanRun[Index] = net_iterator;
        }
    }
    if (state==5) {
        net_iterator = scanRun[Index];
        net_handle = vpi_scan(net_iterator);
        if (!net_handle) { 
            state=6; scanStates[Index]=6;
        } else { 
            size = vpi_get(vpiSize, net_handle);
            sprintf(String,"regArray   %s [%d]  ", vpi_get_str(vpiName, net_handle),size);
            return Py_BuildValue("s", String);
        }
    }
    if (state==6) {
        net_iterator = vpi_iterate(vpiModule, handle);
        if (!net_iterator) { 
            state=8; scanStates[Index]=8;
        } else { 
            state=7; scanStates[Index]=7;
            scanRun[Index] = net_iterator;
        }
    }
    if (state==7) {
        net_iterator = scanRun[Index];
        net_handle = vpi_scan(net_iterator);
        if (!net_handle) { 
            state=8; scanStates[Index]=8;
        } else { 
            sprintf(String,"son   %s %s", vpi_get_str(vpiFullName, net_handle),vpi_get_str(vpiFullName, net_handle));
            return Py_BuildValue("s", String);
        }
    }
    return Py_BuildValue("s", "no more data");
}



// end new code


int printHierarchyDeep(char *pathstring,int depth,FILE *File);



static PyObject*
veri_listing(PyObject *self,PyObject *args) {
    char *pathstring,*vstr,*filename;
    FILE *File;
    if (!PyArg_ParseTuple(args, "sss",&pathstring,&vstr,&filename))
        return NULL;

    File = fopen(filename,"w");
    int depth = atoi(vstr);
    printHierarchyDeep(pathstring,depth,File);
    fclose(File);
    return Py_BuildValue("i", 1);
}

int printHierarchyDeep(char *pathstring,int depth,FILE *File) {
    vpiHandle handle,net_iterator, net_handle;
    s_vpi_value pvalue;
    char deeper[1000],full1[1000],full0[1000];
    handle =  vpi_handle_by_name(pathstring,NULL);
    if (!handle) {
        vpi_printf("\ncannot find module %s for listing\n",pathstring);
        return 0;
    }
    strcpy(deeper,vpi_get_str(vpiDefName,handle));
    fprintf(File,"module: %s %s\n",deeper,vpi_get_str(vpiFullName,handle));
    net_iterator = vpi_iterate(vpiNet, handle);
    if (net_iterator)
       while ((net_handle = vpi_scan(net_iterator))) {
          PLI_INT32 size = vpi_get(vpiSize, net_handle);
          pvalue.format = vpiBinStrVal; 
          vpi_get_value(net_handle, &pvalue); 
          strcpy(full0,vpi_get_str(vpiFullName,net_handle));
          strcpy(full1,vpi_get_str(vpiName,net_handle));
          fprintf(File,"net:   %s [%d] = %s     // %s\n", full0,size,pvalue.value.str,full1);
       }
    net_iterator = vpi_iterate(vpiReg, handle);
    if (net_iterator)
       while ((net_handle = vpi_scan(net_iterator))) {
          PLI_INT32 size = vpi_get(vpiSize, net_handle);
          pvalue.format = vpiBinStrVal; 
          vpi_get_value(net_handle, &pvalue); 
          fprintf(File,"reg:   %s [%d] = %s // %s\n", vpi_get_str(vpiFullName, net_handle),size,pvalue.value.str,vpi_get_str(vpiName,net_handle));
       }

    net_iterator = vpi_iterate(vpiRegArray, handle);
    if (net_iterator)
       while ((net_handle = vpi_scan(net_iterator))) {
          PLI_INT32 size = vpi_get(vpiSize, net_handle);
          fprintf(File,"arr:   %s [%d] \n", vpi_get_str(vpiFullName, net_handle),size);
       }

    net_iterator = vpi_iterate(vpiModule, handle);
    if (net_iterator)
       while ((net_handle = vpi_scan(net_iterator))) {
          fprintf(File,"son:   %s\n", vpi_get_str(vpiFullName, net_handle));
       }
/*    net_iterator = vpi_iterate(vpiEvent, handle);
    fprintf(File," event %xl\n",(long) net_iterator);
    if (net_iterator)
       while ((net_handle = vpi_scan(net_iterator))) {
          fprintf(File,"event:   %s\n", vpi_get_str(vpiFullName, net_handle));
       }
*/
    if (depth>0) {
        net_iterator = vpi_iterate(vpiModule, handle);
        if (net_iterator)
        while ((net_handle = vpi_scan(net_iterator))) {
            strcpy(deeper,vpi_get_str(vpiFullName, net_handle));
            printHierarchyDeep(deeper,depth-1,File);
        }
    }
    return 0;
}


vpiHandle rHandle;


static PLI_INT32 callbackRoutine(s_cb_data *cb_data);

    s_vpi_value  value_s;
    s_vpi_time  time_s,Stime;
    s_cb_data  cb_data_s;

static PyObject*
veri_register(PyObject *self,PyObject *args) {
    vpiHandle handle;
    char *pathstring,*pythonRoutine;
    if (!PyArg_ParseTuple(args, "ss",&pathstring,&pythonRoutine))
        return NULL;
    if ((pathstring[0]<='9')&&(pathstring[0]>='0')) {
        long Delay = atol(pathstring);
        cb_data_s.reason    = cbAfterDelay;
        time_s.type         = vpiSimTime;
        Stime.type=vpiSimTime;
        vpi_get_time(NULL,&Stime);
        time_s.low    = Delay & 0xffffffff;
        time_s.high   = (Delay>>32) & 0xffffffff;
        handle = 0;
    } else {
        get_handle(pathstring,&handle);
        if (!handle) {
            vpi_printf("\npython: cannot find sig %s for register\n",pathstring);
            sprintf(CannotFindCallBack,"try:\n    cannot_find_sig('%s')\nexcept:\n    print('python: cannot find %s for register')\n",pathstring,pathstring);
            PyRun_SimpleString(CannotFindCallBack);
            return Py_BuildValue("s", "q");
        }
       cb_data_s.reason    = cbValueChange;
       time_s.type         = vpiSuppressTime;
    }
    cb_data_s.user_data = pythonRoutine;
    cb_data_s.cb_rtn    = callbackRoutine;
    cb_data_s.time      = &time_s;
    cb_data_s.value     = 0; //&value_s;

    value_s.format      = vpiIntVal;

    cb_data_s.obj  = handle;
    
    rHandle = vpi_register_cb(&cb_data_s);
    return Py_BuildValue("s", "1");
}
             
int callbackRoutine(p_cb_data cb_data) {
    char *Routine;

    Routine = (char *) (cb_data->user_data);
    printf("callback %s\n",Routine);
    int RC = PyRun_SimpleString(Routine);
    checkRC(RC);
    return 0;
}


void checkRC(int RC) {
    if (RC>=0) return;
    vpi_printf("exception finish called from python\n");
    tf_dofinish();
}



static PyObject*
veri_stime(PyObject *self,PyObject *args) {
        s_vpi_time Stime;
        long Result;
    if (!PyArg_ParseTuple(args, ""))
        return NULL;
    Stime.type=vpiSimTime;
    vpi_get_time(NULL,&Stime);
    Result = Stime.high;
    Result = Result << 32;
    Result = Result|Stime.low;
    return Py_BuildValue("l", Result);
}

static PyObject*
veri_finish(PyObject *self,PyObject *args) {
    if (!PyArg_ParseTuple(args, ""))
        return NULL;
    vpi_printf("finish called from python\n");
    tf_dofinish();
    return Py_BuildValue("i", 1);
}



static PyMethodDef VeriMethods[] = {
    {"exists", veri_exists, METH_VARARGS, "Return the number of arguments received by the process."},
    {"peek", veri_peek, METH_VARARGS, "Return the number of arguments received by the process."},
    {"peek_mem", veri_peek_mem, METH_VARARGS, "Return the number of arguments received by the process."},
    {"peek_3d", veri_peek_3d, METH_VARARGS, "Return the number of arguments received by the process."},
    {"force", veri_force, METH_VARARGS,
      "Return the number of arguments received by the process."},
    {"debuglevel", veri_debuglevel, METH_VARARGS,
      "Return the number of arguments received by the process."},
    {"debugstatus", veri_debugstatus, METH_VARARGS,
      "Return the number of arguments received by the process."},
    {"handle", veri_handle, METH_VARARGS,
      "Return the number of arguments received by the process."},
    {"hard_force", veri_hard_force, METH_VARARGS,
      "Return the number of arguments received by the process."},
    {"release", veri_release, METH_VARARGS,
      "Return the number of arguments received by the process."},
    {"listing", veri_listing, METH_VARARGS, "Return the number of arguments received by the process."},
    {"scanInit", veri_scanModuleInit, METH_VARARGS, "Return the number of arguments received by the process."},
    {"scanNext", veri_scanModuleNext, METH_VARARGS, "Return the number of arguments received by the process."},
    {"register", veri_register, METH_VARARGS, "Return the number of arguments received by the process."},
    {"force_mem", veri_force_mem, METH_VARARGS, "Return the number of arguments received by the process."},
    {"force_3d", veri_force_3d, METH_VARARGS, "Return the number of arguments received by the process."},
    {"finish", veri_finish, METH_VARARGS,
     "Return the number of arguments received by the process."},
    {"stime", veri_stime, METH_VARARGS,
     "Return the number of arguments received by the process."},
    {"hforce", veri_hforce, METH_VARARGS,
     "Return the number of arguments received by the process."},
    {"hpeek", veri_hpeek, METH_VARARGS,
     "Return the number of arguments received by the process."},

    {NULL, NULL, 0, NULL}
};


void handler(int code) {
    printf("control-C %d\n",wasControlC);
    if (wasControlC) {
        printf("final exit\n");
    } 
    wasControlC=1;
}

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


void start_py() {
    dlopen("libpython3.8.dylib",RTLD_LAZY | RTLD_GLOBAL);
    PyImport_AppendInittab("veri", PyInit_veri);
    Py_Initialize();
    PyRun_SimpleString("import veri; print(dir(veri));\n");
   


// Oren - Added to solve linking problem when importing random
//    PyObject *mmm;
//    Py_Initialize();
//    mmm = PyModule_Create(&veri_module_definition);
//    mmm = PyInit_veri();
//   printf(">>>>>>> %lx >>>>\n",(long unsigned) mmm);

//    PyRun_SimpleString("help('modules')");
    PyRun_SimpleString(scriptStart);
    globals = PyDict_New();
    if (!globals) return;
    PyDict_SetItemString(globals, "__builtins__", PyEval_GetBuiltins());
    locals = Py_BuildValue("{}");


}



void end_py() {
    Py_Finalize();
}
int stat64() {printf(">>>error stat64\n"); return 0;}
int lstat64() {printf(">>>error lstat64\n"); return 0;}





















