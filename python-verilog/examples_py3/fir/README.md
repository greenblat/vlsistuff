
# Example of FIR. 
8 bit fir example with 8 coefficients.

## Activation
script **comp** runs the compilation and the test.
in iverilog (icarus simulator)

## Synopsys/Cadence/Questa simulators
 You need to edit the script and compile
 the connection ( in vlsistuff/python-verilog/vpi3 are example scripts).
and in vlsistuff/python-verilog/ are examples of activation in various simulators.


## Design
Simple 8x8 fir.
Packaged in top with register file.
the testbench is driven by sequence file test0.seq
    
it activates APB writes to program the coeffs and other variables. All sitting in register file.
then it enables the fir and last enables the uvm mockup.

## Software
if it is Your first visit, read the pdfs in python-verilog directory to get understanding of it all.


Good Luck
Ilia
