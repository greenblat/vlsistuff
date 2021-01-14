
# example of design with several clocks

there is axi slow clock, used to drive in jobs.
there is fast sys_clk used for calculation,
the output is valid on very slow  apb.

this design doesnt make sese n design sence, but demonstrates multi clock verificatio.

the accelerator accepts bursts of data, computes sqrt for each data , sums it and puts it on apb.



