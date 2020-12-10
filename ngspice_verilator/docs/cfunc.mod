






#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>
#include <string.h>
#include <dlfcn.h>

#include <Python.h>

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
print('py-verilog@ilia  license ok, Ilia today = %s %s %s lic = 15.Oct.2020'%(Year,Month,Day))\n\
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
";

int python_started = 0;
PyObject *globals;
PyObject *locals;


int outputs[128];

//   static PyObject*
//   veri_peek(PyObject *self,PyObject *args) {
//       char *pathstring;
//       int res = 0;
//       int Val;
//       if (!PyArg_ParseTuple(args, "s",&pathstring))
//           return NULL;
//       if (pathstring[0]=='i') {
//           for (int i=0;pathstring[i];i++) {   
//               char cc = pathstring[i];
//               if ((cc>='0')&&(cc<='9')) {
//                   res = 10*res + (cc-'0');
//           Val = in[res]; 
//       } else if (pathstring[0]=='o') {
//           for (int i=0;pathstring[i];i++) {   
//               char cc = pathstring[i];
//               if ((cc>='0')&&(cc<='9')) {
//                   res = 10*res + (cc-'0');
//           Val = out[res]; 
//       }
//   
//       return Py_BuildValue("s", "0");
//   }


static PyObject*
veri_force(PyObject *self,PyObject *args) {
    char *vstr;
    char *pathstring;
    if (!PyArg_ParseTuple(args, "ss",&pathstring,&vstr)) return NULL;
    int res;
    res=0;
    for (int i=0;pathstring[i];i++) {   
           char cc = pathstring[i];
           if ((cc>='0')&&(cc<='9')) {
               res = 10*res + (cc-'0');
           }
    }
    outputs[res] = vstr[0];
    printf("forcing res=%d vstr=%s\n",res,vstr);
    return Py_BuildValue("i", 1);
}



static PyObject*
veri_stime(PyObject *self,PyObject *args) {
        long Result;
    if (!PyArg_ParseTuple(args, ""))
        return NULL;
    Result = 10000;
    return Py_BuildValue("l", Result);
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
//    {"peek", veri_peek, METH_VARARGS, "Return the number of arguments received by the process."},
    {"force", veri_force, METH_VARARGS, "Return the number of arguments received by the process."},
    {"finish", veri_finish, METH_VARARGS, "Return the number of arguments received by the process."},
    {"stime", veri_stime, METH_VARARGS, "Return the number of arguments received by the process."},
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



void start_py() {
    dlopen("libpython3.9.dylib",RTLD_LAZY | RTLD_GLOBAL);
    dlopen("libpython3.9.so",RTLD_LAZY | RTLD_GLOBAL);
    PyImport_AppendInittab("veri", PyInit_veri);
    Py_Initialize();
    PyRun_SimpleString("import veri; print(dir(veri));\n");



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






void cm_d_python(ARGS)
{
    int i,          /* generic loop counter index */
        j,          /* lookup index bit value */
        k,          /* generic loop counter index */
        idx,        /* lookup index */
        ivalid,     /* check for valid input */
        isize,      /* number of input ports */
        osize,      /* number of output ports */
        dsize,      /* number of input delay params */
        rsize,      /* number of output rise delay params */
        fsize,      /* number of output fall delay params */
        lsize       /* number of input load params */
    ;
    char        *path;
    char        *module;
    double      maxdelay,  /* maximum input-to-output delay */
        testdelay;


    if (!python_started) {
        printf( "\n=====starting python ======\n" );
        start_py();
        python_started=1;
    }



    Digital_t  *in;       /* temp storage for input bits  */  
    Digital_t  *out;      /* temporary output for buffers */

    /** Retrieve size values and compute table length... **/ 
    isize = PORT_SIZE(in);
    osize = PORT_SIZE(out);

    path = PARAM(path);
    module = PARAM(module);

    if (INIT) {
        for (int kk=0;kk<osize;kk++) 
            cm_event_alloc(kk,sizeof(Digital_State_t));
        printf("init done\n");
        for (int kk=0;kk<osize;kk++) 
            OUTPUT_DELAY(out[kk]) = PARAM(rise_delay);
    } 
    char Str0[1000];
    char tmp[1000];
    sprintf(Str0,"run_spice(\"%s %s %d %d  %f %f | ",path,module,isize,osize,PARAM(rise_delay),PARAM(fall_delay));
//    printf("Str0 %s\n",Str0);
    char Val;
    for (int kk=0;kk<isize;kk++)  {
//        if (FALSE == PORT_NULL(in) ) Val = 'X';
        if ( 1 == INPUT_STATE(in[kk])) Val = '1';
        else if ( 0 == INPUT_STATE(in[kk])) Val = '0';
        else Val = 'x';
//        printf("in[%d] %c %d %d\n",kk,Val,INPUT_STATE(in[i]), PORT_NULL(in) );
        sprintf(tmp," %c",Val);
        strcat(Str0,tmp);


    }
//    printf("Str01 %s\n",Str0);
    strcat(Str0," |");
    for (int kk=0;kk<osize;kk++) {
//        out[kk] = (Digital_State_t *) cm_event_get_ptr(osize+kk,0);
        sprintf(tmp," %c",'x');
        strcat(Str0,tmp);
    }
    strcat(Str0," \") ");
//    printf("Str0 finale %s\n",Str0);
    for (int kk=0; kk<128; kk++) outputs[kk]=0;
    int RC = PyRun_SimpleString(Str0);
    for (int ii=0;ii<osize;ii++) {
        if (outputs[ii]) {
            printf("dnd  %d %c\n"
                ,ii
                ,outputs[ii]
            );
            OUTPUT_CHANGED(out[ii]) = TRUE;
            if (outputs[ii]=='0') { 
                OUTPUT_STATE(out[ii]) = ZERO;
                OUTPUT_DELAY(out[ii]) = PARAM(fall_delay);
            } else if (outputs[ii]=='1') { 
                OUTPUT_STATE(out[ii]) = ONE;
                OUTPUT_DELAY(out[ii]) = PARAM(rise_delay);
            } else { 
                OUTPUT_STATE(out[ii]) = UNKNOWN;
                OUTPUT_DELAY(out[ii]) = PARAM(rise_delay);
            }
        } else {
            OUTPUT_CHANGED(out[ii]) = FALSE;
        }
    }
}

