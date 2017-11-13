#! /usr/bin/python

import math,os,sys,string


'''
make sinus table verilog module
'''

LINES = 2048
WID   = 16
ADDR = 11

def main():
    Fout = open('rtl/sintab.v','w')
    Fout.write('module sintab(input [%d:0] addr,output reg [%d:0] out);\n'%(ADDR-1,WID-1))
    Fout.write('always @* begin\n')
    Fout.write('    case (addr)\n')
    for II in range(LINES):
        Angle = II*(2 * math.pi)/LINES
        Fout.write('        %d : out = %d;\n'%(II,int(math.sin(Angle)*0x7fff)))
    Fout.write('    endcase\n')
    Fout.write('end\n')
    Fout.write('endmodule\n')
    
main()
