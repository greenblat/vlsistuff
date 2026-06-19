
// auto generated C headers file of dut_rf regfile
#ifndef __DUT_RF_H
    #define __DUT_RF_H

    #include <inttypes.h>

    typedef struct {
    ro uint32_t  VERSION                  ;          // ad=0x0 w=32 acc=ro      "version date"
    rw uint32_t  REG0[3]                  ;          // ad=0x4 w=96 acc=rw      "first wide register"
    ro uint32_t  STATUS                   ;          // ad=0x10 w=32 acc=ro      "value of counter"
    rw uint32_t  COUNTER_START            ;          // ad=0x14 w=32 acc=rw_pulse      "start the counter"
    rw uint32_t  INTERRUPTS               ;          // ad=0x18 w=32 acc=w1c      "interrupts keeper"
    rw uint32_t  SET_INTERRUPT            ;          // ad=0x1c w=5 acc=rw_pulse      "sat named interrupt"
} dut_rf_RegDef;


#endif
