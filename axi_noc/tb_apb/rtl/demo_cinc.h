
// auto generated C headers file of demo regfile
#ifndef __RF_INTERFACE_RGF_H
    #define __RF_INTERFACE_RGF_H

    #include <inttypes.h>

    typedef struct {
    rw uint32_t  KEY0[4]                  ;          // ad=0x0 w=128 acc=rw      "key for 64 bit encryptions"
    rw uint32_t  KEY1[4]                  ;          // ad=0x10 w=128 acc=rw      "key for 64 bit encryptions"
} demo_RegDef;
#endif
