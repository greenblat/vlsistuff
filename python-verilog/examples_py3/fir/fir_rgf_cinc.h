
// auto generated C headers file of fir_rgf regfile
#ifndef __FIR_RGF_H
    #define __FIR_RGF_H

    #include <inttypes.h>

    typedef struct {
    rw uint32_t  ENABLE                   ;          // ad=0x0 w=1 acc=rw      "enable"
    rw uint32_t  SCALEFACTOR              ;          // ad=0x4 w=4 acc=rw      "scale back factor of sum before output"
    ro uint32_t       gap0x28[8];          // gap
    ro uint32_t  GOODS                    ;          // ad=0x28 w=32 acc=ro      "number of no saturations"
    ro uint32_t  BADS                     ;          // ad=0x2c w=32 acc=ro      "number of saturations"
} fir_rgf_RegDef;


#endif
