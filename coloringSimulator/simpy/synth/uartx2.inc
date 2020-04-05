
read_verilog -sv uartx2.all
hierarchy -check -top  uartx2
check;
proc; opt; fsm; opt; memory; opt
check;

techmap; opt
dfflibmap -liberty /Users/ilia/clients/yosys_libs/basic2.lib
abc -liberty  /Users/ilia/clients/yosys_libs/basic2.lib

clean
write_verilog -noattr  uartx2.glv


flatten;
check;
opt;
check;
clean;
write_verilog uartx2.flat
