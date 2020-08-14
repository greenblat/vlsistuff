

#include <iostream>    
#include <strings.h>    
#include "VTOP.h"
#include "verilated.h"
#include "verilated_vcd_c.h"

#include <Python.h>

vluint64_t cycles = 0;       // Current simulation time
VTOP* top = new VTOP;
VerilatedVcdC* tfp = new VerilatedVcdC;

void initials(char *initfile) {
    char work[1000];
    sprintf(work,"initial('%s')",initfile);
    int RC = PyRun_SimpleString(work);
}

void negedge() {
    int RC = PyRun_SimpleString("negedge()");
}
void posedge() {
    int RC = PyRun_SimpleString("posedge()");
}


#include "values.h"

static PyObject*
veri_peek(PyObject *self,PyObject *args) {
    char *pathstring;
    if (!PyArg_ParseTuple(args, "s",&pathstring))
        return NULL;
    char Val[1000];
    strcpy(Val,getValue(pathstring));
    return Py_BuildValue("s", Val);
}
static PyObject*
veri_width(PyObject *self,PyObject *args) {
    char *pathstring;
    if (!PyArg_ParseTuple(args, "s",&pathstring))
        return NULL;
    char Val[1000];
    strcpy(Val,getWid(pathstring));
    return Py_BuildValue("s", Val);
}

char longbits[10000];
static PyObject* veri_force(PyObject *self,PyObject *args) {
    char *vstr;
    char *pathstring;
    if (!PyArg_ParseTuple(args, "ss",&pathstring,&vstr)) return NULL;

    int Wid = strtol(getWid(pathstring),NULL,10);
    if (Wid<=64) {
        setValue(pathstring,vstr);
        return Py_BuildValue("i", 1);
    }
    int ii,jj;
    for (ii=0;ii<=((Wid+3)/4);ii++) {
        longbits[ii]='0';
    }
    longbits[ii]=0;
    jj=strlen(vstr)-1;
    ii--;


    while ((ii>=0)&&(jj>=0)&&(
                  ((vstr[jj]>='a')&&((vstr[jj]<='f')))
                ||((vstr[jj]>='0')&&(vstr[jj]<='9'))
          )) {
        longbits[ii]=vstr[jj];
        ii--;
        jj--;
    }
    setValue(pathstring,longbits);
    return Py_BuildValue("i", 1);
}

static PyObject* veri_stime(PyObject *self,PyObject *args) {
    return Py_BuildValue("l", cycles);
}

static PyObject* veri_finish(PyObject *self,PyObject *args) {
    if (!PyArg_ParseTuple(args, "")) return NULL;
    printf("finish called from python\n");
    tfp->close();
    top->final();
//    Py_Finalize();
    return Py_BuildValue("i", 1);
}

static PyObject* veri_runcycle(PyObject *self,PyObject *args) {
    if (!PyArg_ParseTuple(args, "")) return NULL;
    top->clk = 0;
    negedge();
    top->eval();
    tfp->dump(cycles*10);
    cycles++;

    top->clk = 1;
    posedge();
    top->eval();
    tfp->dump(cycles*10);
    cycles++;
    return Py_BuildValue("i", 1);
}





static PyMethodDef VeriMethods[] = {
    {"peek", veri_peek, METH_VARARGS, "Return the number of arguments received by the process."},
    {"width", veri_width, METH_VARARGS, "Return the number of arguments received by the process."},
    {"force", veri_force, METH_VARARGS, "Return the number of arguments received by the process."},
    {"finish", veri_finish, METH_VARARGS, "Return the number of arguments received by the process."},
    {"runcycle", veri_runcycle, METH_VARARGS, "Return the number of arguments received by the process."},
    {"stime", veri_stime, METH_VARARGS, "Return the number of arguments received by the process."},
    {NULL, NULL, 0, NULL}
};


PyObject *globals;
PyObject *locals;

char scriptStart[] = "\n\
import string,os,sys\n\
import traceback \n\
sys.path=sys.path+['./']\n\
import veri\n\
import time\n\
XX = time.time()\n\
Str = time.ctime(XX)\n\
ww = string.split(Str)\n\
months = string.split('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec')\n\
Month = 1+months.index(ww[1])\n\
Day = int(ww[2])\n\
Year = int(ww[4])\n\
if os.path.exists('./verilog.py'):\n\
    try:\n\
        print 'verilog.py found'\n\
        from verilog import *\n\
        print 'verilog.py found and loaded'\n\
    except:\n\
        traceback.print_exc() \n\
        print 'verilog.py exists, but crashed. failed to read verilog.py'\n\
        veri.finish() \n\
        sys.exit() \n\
else:\n\
    print 'verilog.py do not exist'\n\
\n\
print 'available veri. services: ',dir(veri)\n\
print 'python-verilog connection mode=4 (ver 09sep2015) started'\n\
";


void start_py() {
    printf("<><><><<>\n");
    Py_Initialize();
    Py_InitModule("veri", VeriMethods);
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


char initfile[1000];

int main(int argc, char** argv, char** env) {
    Verilated::commandArgs(argc, argv);
    Verilated::traceEverOn(true);
    int pos=0;
    initfile[0]=0;
    for (int kk=2;kk<=argc;kk++) {
        char option[100];
        strcpy(option, *++argv);
        if (strcmp(option,"-i")==0) {
            strcpy(initfile, *++argv);
            kk++;
        }
    }


    start_py();
    top->trace(tfp, 99);
    tfp->open("waves.vcd");
    initials(initfile);
//    while (!Verilated::gotFinish()) {
// 
//         top->clk = 0;
//         negedge();
//         top->eval();
//         tfp->dump(cycles);
//         cycles++;
// 
//         top->clk = 1;
//         posedge();
//         top->eval();
//         tfp->dump(cycles);
//         cycles++;
//     }
    printf("closing shop\n");
    tfp->close();
    top->final();
    delete top;
    exit(0);
}


