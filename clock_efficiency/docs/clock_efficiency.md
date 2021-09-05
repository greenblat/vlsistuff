

# Clock Efficiency flow

## What is Clock Efficiency
Each flop in an ASIC chip has a clock input. Usually this clock is a leaf of a clock tree (or one of the trees).
On edge (+ or -), this flop samples the data input "D" and transfers the new value to output "Q". If "D" causes a change in the "Q" it is a useful clock cycle. If clock pulses, but "Q" doesn't change it is wasted cycle. If "D" changes and clock doesn't pulse it is a dropped change.

<img src="clocktree.svg" alt="clocktree" style="zoom:50%;" />

Efficiency is defined the ratio between "useful" clocks and total number of clocks reaching the flop.
Most new designs have elaborate clock gating. If the clock tree is disabled early or in many branches, we save power.
Clock-tree power consumption is relatively significant, and to save battery, It is desirable to increase the ratio.
The way to do it, is rewrite RTL, so more flops will have enables.

Also considering  the  number of "D" changes, when there is no clock. It means we waste energy toggling the "D" without using it.

## The game : saving power.
For washing machine chips, this is not a big deal, as the red light in front of the machine consumes more power than all electronics. But for batterie powered devices or energy harvested from environment this could be a big deal.


## How
There are several ways to get info on wasted clock cycles,  It can be done on gate-level, where for every flop, we assign python monitor (generated by script).
This monitor catches the edge of the clock, peeks at "D" and compares to "Q". (Clock going up in simulation, precedes the change of Q). Note that to save power, CLK can be actually a gated clock. So environment counts the number of clock edges against difference of "D" and "Q".  Ideally these two counts should be equal. In practice 50% is ok, because 100% is not conveying any new information. In practice, we can try to rewrite RTL to increase the ratio.

<img src="efficiency0.svg" alt="efficiency0" style="zoom:60%;" />

For rtl, script described below creates class that monitors one module (or deep into one module), gathers the counts and reports in the end. The script collects all "always" blocks with Clocks qualified with "pos or neg edges" and all left side variables of "Qflop <= ".  We also count the number of times "D" toggles and there is no clock. 

The result is written into Python class that counts these scenarios.
The whole flow is supported by Python-Driven-Verification.

Third option, is to use same python class as before, but run it on VCD file from simulation using vcd_python3 executable.


## Preparation

pyver.py rtl/my_module.v -do clock_efficiency_rtl 
(pyver.py and clock_efficiency_rtl.py are in gitHub repository vlsistuff/verpy/pybin)
this should create a file my_module_efficience.py

Detailed scripts "run" is in vlsistuff/clock_efficiency/examples/


## Simulation  (requires pythnon-driven-verification from the same git)
xrun/vcs/iverilog -f **YourFileList** .......

at the end of the test, report is printed out  into  pymon.log0

## how it really looks

RTL code:

![rtl0](rtl0.png)

 Using pyver.py system with clock_efficiency.py driver, Will create the following code:   

![effpy0](effpy0.png)

Not shown is the class definitions and other counters. Also some optimization can reduce the complexity of this expression.

Running any simulation with this class imported and constructed, will yield report something like :

![repo0](repo0.png)

another example of log file, with DROPPED enabled. Notice, negative dropped values, it happens when the new data coming from  literal values.

![dropped](dropped.png)

Width of the flop registers is important here, because it multplies the effect. The so first line is very good, while others are not and need to be examined for opprtunity to improve power consumption. The sum of "used" and "wasted" counters is the number the clock of these flops was toggled.

With this new info, we can scan the RTL and try to improve ratios of the worst offenders.

### work in progress

The question is how efficient is this flow to improve power consumption. I am doing few trials and results are updated in **vlsistuff/clock_efficiency**    . This doc is in **vlsistuff/docs**


