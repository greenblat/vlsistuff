

#include "rtl/rgf/dut_rf.h"

void startCounter(int From) {
    __ext_store(ADDR_COUNTER_START,From);
}

void main() {
    int vers;
    __ext_store(ADDR_INTERRUPTS,0xfff);
    vers = __ext_load(ADDR_VERSION);
    __ext_store(ADDR_REG0+4,vers);
    __nop(5);
    startCounter(0x500);
    __sleep(10);
    __nop(6);
    __stop();
    __ext_store(ADDR_INTERRUPTS,0xfff);
    __nop(7);
    __finish_good();
}


