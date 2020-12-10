

#include <iostream>    
#include <strings.h>    
#include "Vwrap_cntrl.h"
#include "verilated.h"
#include "verilated_vcd_c.h"


vluint64_t cycles = 0;       // Current simulation time
Vwrap_cntrl* top = new Vwrap_cntrl;
VerilatedVcdC* tfp = new VerilatedVcdC;
int VcdOn = 1;


#include "values.h"

extern "C" int runCycle(int many) {
    int ii;
    for (ii=0;ii<many;ii++) {
        top->clk = 0;
        top->eval();
        if (VcdOn) tfp->dump(cycles*10);
        cycles ++;
    
        top->clk = 1;
        top->eval();
        if (VcdOn) tfp->dump(cycles*10);
        cycles ++;
        top->cycles = cycles/2;
    }
    return 0;
}

extern "C" void  init0() {
    int argc = 0;
    char** argv;
    Verilated::commandArgs(argc, argv);
    Verilated::traceEverOn(true);
    if (VcdOn) {
        top->trace(tfp, 99);
        tfp->open("waves.vcd");
        printf("waves opened\n");
    }
}


int initialize(int argc, char** argv, char** env) {
    Verilated::commandArgs(argc, argv);
    Verilated::traceEverOn(true);
    if (VcdOn) {
        top->trace(tfp, 99);
        tfp->open("waves.vcd");
    }
    return 1;
}


extern "C" void  wrapup() {
    if (VcdOn) {
        tfp->close();
    }
    top->final();
    delete top;
    exit(0);
}


