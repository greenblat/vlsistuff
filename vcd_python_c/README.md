- This version of vcd_python is written in C. So it is much faster than pure python.
** This version uses python3 !!! **

# vcd_python3
- to compile, just run (and first -  modify to match Your system) "compile3_on_my_mac" or linux.

- should use src3 for python3
- this should produce vcd_python executable right here.
- You need decent python 3.7 (or 8,9,10,11,12 or 13)  on Your system.
- especially library. Most problems come from the location of these libraries and setup of $LD_LIBRARY_PATH or similar $DYLD.....

Once past these problems,  
try demo - script called "run".


to activate vcd_python: (as shown in "run") :

vcd_python3 <VCDFILE> <PYTHONFILE>   [-start Time] [-end Time]

(the invokation line is used to create "invokation" varible in python, so it is possible to add parameters for python )

(mind You, some options were not debugged yet).


1. import veri    # this connects python to C.
2. veri.peek(Net)   is used to peek on values in VCD.
3.  use: veri.sensitive('tb.clk','0',"negedge()","0")
    last parameter is delay in timepoints of the vcd from negedge of clk
4.  use: veri.sensitive('always','0',"negedge()","0")
    "always" means negedge is called on every new timepoint.



try it and the see the speed.


addition:   veri.trace and veri.force
the intention is to enable to write out vcd file of chosen signals.

first use veri.trace(Sig,Width)   to mark signals for tracing.
Sig maybe either existing net in the design or new net.
New net requires width specified (as string).
existing nets dont look at width parameter (but it still must be be there (put zero))


Exisiting nets will be dumped to vcd file if they are traced. Simply by copying them from the VCD file.
Invented nets need veri.force(Sig,Val) command to change their value in the created vcd file.


# vcd_python32

- uses src3/vcd_python2.c
- no veri.trace, only veri.force
- creates identical copy of input vcd file (traces all signals)
- veri.force is new:  new "module" called trace will be added to VCD.
- veri.force :  this trace module has 24 integers. Integers 0 to 19 are free, 20 is errors, 21 is wrongs, 22 is corrects.
- veri.force example:     veri.force('5','0x223')
   veri.force can accept first parameter string of a number from 0 to 22


[for short overview](docs/Vcd_python3.md)

