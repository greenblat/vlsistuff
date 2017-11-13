/*
 * |-----------------------------------------------------------------------|
 * |                                                                       |
 * |   Copyright Cadence Design Systems, Inc. 1985, 1988.                  |
 * |     All Rights Reserved.       Licensed Software.                     |
 * |                                                                       |
 * |                                                                       |
 * | THIS IS UNPUBLISHED PROPRIETARY SOURCE CODE OF CADENCE DESIGN SYSTEMS |
 * | The copyright notice above does not evidence any actual or intended   |
 * | publication of such source code.                                      |
 * |                                                                       |
 * |-----------------------------------------------------------------------|
 */

/*
 * |-------------------------------------------------------------|
 * |                                                             |
 * | PROPRIETARY INFORMATION, PROPERTY OF CADENCE DESIGN SYSTEMS |
 * |                                                             |
 * |-------------------------------------------------------------|
 */

/*************************** File vpi_user_cds.h **************************/
/***** This file is to be included in files which call VPI routines *******/
/************* and require access to non-IEEE compliant aspects ***********/

#ifndef VPI_USER_CDS_H
#define VPI_USER_CDS_H

#ifdef  __cplusplus
extern "C" {
#endif

/*---------------------------------------------------------------------------*/
/*--------------------------- Portability Help ------------------------------*/
/*---------------------------------------------------------------------------*/
/* Sized variables */
#ifndef PLI_TYPES
#define PLI_TYPES
typedef int             PLI_INT32;
typedef unsigned int    PLI_UINT32;
typedef short           PLI_INT16;
typedef unsigned short  PLI_UINT16;
typedef char            PLI_BYTE8;
typedef unsigned char   PLI_UBYTE8;
#endif

/* Use to export a symbol */
#if WIN32
#ifndef PLI_DLLISPEC
#define PLI_DLLISPEC __declspec(dllimport)
#define VPI_USER_CDS_DEFINED_DLLISPEC 1
#endif
#else
#ifndef PLI_DLLISPEC
#define PLI_DLLISPEC
#endif
#endif

/* Use to import a symbol */
#if WIN32
#ifndef PLI_DLLESPEC
#define PLI_DLLESPEC __declspec(dllexport)
#define VPI_USER_CDS_DEFINED_DLLESPEC 1
#endif
#else
#ifndef PLI_DLLESPEC
#define PLI_DLLESPEC
#endif
#endif

/* Use to mark a function as external */
#ifndef PLI_EXTERN
#define PLI_EXTERN
#endif

/* Use to mark a variable as external */
#ifndef PLI_VEXTERN
#define PLI_VEXTERN extern
#endif

#ifndef PLI_PROTOTYPES
#define PLI_PROTOTYPES
#define PROTO_PARAMS(params) params
/* object is defined imported by the application */
#define XXTERN PLI_EXTERN PLI_DLLISPEC
/* object is exported by the application */
#define EETERN PLI_EXTERN PLI_DLLESPEC
#endif


/*---------------------------------------------------------------------------*/
/*------------------------------ Array sizes --------------------------------*/
/*---------------------------------------------------------------------------*/

#ifndef MAX_SYSTFS
#define MAX_SYSTFS 1024
#endif
#define VPI_MAXARRAY 1024 /*
                           * This is the default size of the arrays located
                           * in the vpi_user.c file.  The need for this is
                           * due to a dynamic linking issue on the Solaris
                           * platform.  The linker/compilier stores size
                           * infomation about arrays in the generated .o,
                           * .so and exe files.  When the default executable
                           * is linked against the libvpi and libpli dynamic
                           * libraries the size of the arrays in the default
                           * libraries must be larger then the arrays in the 
                           * libraries being used.
                           */


/****************************** OBJECT TYPES ******************************/

#define vpiAttribute_OLD   500   /* Attribute */
#define vpiCallback_OLD    501   /* Registered callback */
#define vpiDelayTerm_OLD   504   /* Delay terminal which is a load or driver. */
#define vpiDelayDevice_OLD 505   /* Delay object within a net. */
#define vpiDb              509   /* Handle to a database (SHM, VCD) */
#define vpiOptDriver       510   /* Handle to an optimized driver */
#define vpiOptLoad         511   /* Handle to an optimized load */
#define vpiGateArray_OLD   512   /* gate instance array */
#define vpiInstanceArray_OLD   513   /* vpiInstance arrays */
#define vpiModuleArray_OLD 514   /* module instance array */
#define vpiPrimitiveArray_OLD  515   /* vpiprimitiveArray type */
#define vpiSwitchArray_OLD 516   /* switch instance array */
#define vpiUdpArray_OLD    517   /* UDP instance array */
#define vpiGenScopeArray   518   /* array of generates */
#define vpiGenScope        519   /* generate scope */
#define vpiGenVar          520   /* generate variable */

/******************************** METHODS *********************************/
/************* methods used to traverse 1 to 1 relationships **************/
#define vpiPorts_OLD       502   /* Module port */
#define vpiTaskFunc_OLD    503   /* HDL task or function */
#define vpiInTerm_OLD      506   /* To get to a delay device's drivers. */
#define vpiOutTerm_OLD     507   /* To get to a delay device's loads. */
#define vpiSimNet_OLD      508   /* To get to a simulated net. */

/************ methods used to traverse 1 to many relationships ************/



/******************************* PROPERTIES *******************************/
/************************ generic object properties ***********************/
#define vpiDecompile_OLD   500   /* decompile the object */
#define vpiSigned_OLD      510   /* Object is typed as being signed */

/************************** function properties ***************************/
#define vpiFuncType_OLD    501   /* HDL function type */
#define vpiRegFunc_OLD        1   /* default funct declaration */
#define vpiIntFunc_OLD        2   /* function returns an int */
#define vpiRealFunc_OLD       3   /* function returns a real */
#define vpiTimeFunc_OLD       4   /* function returns a time */

/********************** text manipulation properties **********************/
#define vpiEndLineNo       502   /* Line number where the join, end, or endmodule is located */

/************************ port and net properties *************************/
#define vpiFullNetType     503   /* Get the resolved net type */

/*************************** module properties ****************************/
#define vpiTimeFormatPrec  504   /* Precision specified with $timeformat */
#define vpiTimeFormatUnit  505   /* Unit specified with $timeformat */
#define vpiDesignProtected 516   /* module is protected or contains a protected 
                                    construct; this is different from vpiProtected,
                                    which checks only if the module is protected, not 
                                    that does it contain some protected construct.*/

/************************* delay term properties **************************/
#define vpiDelayType_OLD   506   /* The type of object that cause the delay term to exist. */
#define   vpiModPathDelay_OLD      1
#define   vpiInterModPathDelay_OLD 2
#define   vpiMIPDelay_OLD          3

/************************* attribute properties ***************************/
#define vpiDefAttribute_OLD 515  /* Attribute is on module definition */
/* The following is not covered by other Const Types */
#define vpiTimeConst           7   /* Type Time for Attributes */

/************************* expression properties **************************/
/* These can be returned by vpiOpType */
#define vpiArithLShiftOp_OLD   500
#define vpiArithRShiftOp_OLD   501

/*********************** system taskfunc properties ***********************/
/* This can be returned by vpiSysFuncType */
/* alias to vpiSizedSignedFunc in vpi_user.h */
#define vpiSysFuncSignedSized  5

/************************** data base properties **************************/
#define vpiDbType          507   /* The type of database */
#define   vpiSHM               1
#define   vpiVCD               2
#define   vpiSST2              3

/************** FLAGS for vpi_db_open and vpiSST2 databases ***************/
#define dbEvent                0x02  /* Dump all events on an object to the database */
#define dbCompress             0x04  /* Turn on database compression */
#define dbPrimitives           0x08  /* Record primitives. */
#define dbDrivers              0x10  /* Record drivers. */

/************************** access properties *****************************/
#define vpiWriteAccess     508  /* The object has write access */
#define vpiReadAccess      509  /* The object has read access */
#define vpiConnectivityAccess 512 /* The object has connectivity access */

/********************* interoperability properties ************************/
#define vpiLanguage        511
#define   vpiVerilog           1  /* Is a Verilog object */
#define   vpiVHDL              2  /* Is a VHDL object */
#define   vpiSystemC           3  /* Is a SystemC object */

#define vpiFullVHDLName    513  /* Full name using VHDL terminology */
#define vpiFullLSName      514  /* Full name relative to each scope's language domain. */

/********************* save/restart properties ************************/
#define vpiSaveRestartID_OLD       515 /* Get a unique ID for save/restart data */
#define vpiSaveRestartLocation_OLD 516 /* Name of save/restart data file */

/************************** I/O related defines ***************************/
/* ATTENTION!!!  These were eliminated from the IEEE 1364-2000 specification. */
#define VPI_MCD_STDERR  0x00000002
#define VPI_MCD_LOG     0x00000004


/************************** STRUCTURE DEFINITIONS *************************/

/**************************** CALLBACK REASONS ****************************/
#define cbPLIError_OLD     500  /* for when a PLI type error/warning occures */
#define cbDisable_OLD      501  /* for when a block containing a system task is disabled. */
#define cbAssign_OLD       502  /* for when an assign statement occures */
#define cbDeassign_OLD     503  /* for when an deassign statment occures */
#define cbDbOpen           504  /* for when a database is opened */
#define cbDbClose          505  /* for when a database is closed */
#define cbNonBlockingSynch 506  /* call routine when the non blocking occures */
#define cbStmtNB           507  /* call when the non blocking stmt matures. */
#define cbStmtContFinish   508  /* call when the assignment delay or event control matures */
#define cbAtEndOfSimTime   509  /* to be treated like cbReadWrite,happens when no other events that modify values exist */
#define cbNBASynch         510  /* occurs before any non-blocking assignments, and after all other assignments */
				

/*
   Types of probes, these types are only of use if the obj is a
   module, HDL task or function otherwise the type and depth entry is
   ignored. 
*/
#define dbProbeObj       0x00
#define dbProbePorts     0x01
#define dbProbeInputs    0x02
#define dbProbeOutputs   0x04
#define dbProbeAll       0x08
#define dbProbeAllNoMem  0x10
#define dbProbeToCell    0x20  /* Stop dumping objects below cell instances */
#define dbProbeNoPorts   0x40  /* dump all but the ports */
#define dbProbePrimitives 0x80  /* dump only primitives */

/*
 * Type of access to perform on object and database
 */
#define dbProbe          1
#define dbDelete         2
#define dbProbeOn        3
#define dbProbeOff       4
#define dbFlush          5

/************************* FUNCTION DECLARATIONS **************************/

#ifndef ACC_USER_H
typedef PLI_INT32   *handle;
#endif

XXTERN vpiHandle acc_to_vpi PROTO_PARAMS((handle object));
XXTERN handle    vpi_to_acc PROTO_PARAMS((vpiHandle object));
XXTERN vpiHandle vpi_db_open PROTO_PARAMS((PLI_INT32 dbType, PLI_BYTE8 *dbPath, PLI_INT32 flag));
XXTERN PLI_INT32 vpi_db_close PROTO_PARAMS((vpiHandle id));
XXTERN PLI_INT32 vpi_db_access PROTO_PARAMS((PLI_INT32 dbAccessType, vpiHandle db, vpiHandle obj, PLI_INT32 probeType, PLI_INT32 depth));

XXTERN void *    vpi_get_sc_handle PROTO_PARAMS((vpiHandle object));


/**************************** GLOBAL VARIABLES ****************************/

#undef PLI_XXTERN
#undef PLI_EETERN

#ifdef VPI_USER_CDS_DEFINED_DLLISPEC
#undef VPI_USER_CDS_DEFINED_DLLISPEC
#undef PLI_DLLISPEC
#endif
#ifdef VPI_USER_CDS_DEFINED_DLLESPEC
#undef VPI_USER_CDS_DEFINED_DLLESPEC
#undef PLI_DLLESPEC
#endif

#ifdef PLI_PROTOTYPES
#undef PLI_PROTOTYPES
#undef PROTO_PARAMS
#undef XXTERN
#undef EETERN
#endif

#ifdef  __cplusplus
}
#endif

#endif
