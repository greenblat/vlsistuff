#! /usr/bin/env python3
import os,sys,string
HELPER = '''
apbMuxBuilder.py    5          0x300000        0x2000          [module name] 
                    ^             ^              ^               ^
                    !             !              !               !
                  number     first address    addr increment   optional
                  of ports

will create a module that muxes (combinatorically!!) 5 APB slaves into one slave.
the psel0 will be fired when paddr above or equal first address parameter.
guess the rest.

pclk and presetn are outside scope of the generated module.

'''
def main():
    if (len(sys.argv)<4)or('-h' in sys.argv)or ('--h' in sys.argv):
        print(HELPER)
        return
    Portsnum = eval(sys.argv[1])
    Startaddr = eval(sys.argv[2])
    Incraddr  = eval(sys.argv[3])
    if len(sys.argv)>4:
        Module = sys.argv[4]
    else:
        Module = 'apbmux%d'%Portsnum
    File = open('%s.v'%Module,'w')
    File.write(HEADER.replace('MODULE',Module))
    for II in range(Portsnum):
        File.write(PORT.replace('NN',str(II)))

    File.write(');\n')
    for II in range(Portsnum):
        File.write('assign pwrite%d = pwrite; '%II)
        File.write('assign penable%d = penable; '%II)
        File.write('assign pstrb%d = pstrb; '%II)
        File.write('assign pwdata%d = pwdata;\n'%II)

    Run = Startaddr
    for II in range(Portsnum):
        File.write("assign psel%d  = psel && (paddr>=32'h%x) && (paddr<32'h%x);\n"%(II,Run,Run+Incraddr))
        File.write("reg psel%d_d1; always @(pclk) psel%d_d1  <= psel%d;\n"%(II,II,II))
        File.write("assign paddr%d  = paddr-32'h%x;\n"%(II,Run))
        Run += Incraddr;
    File.write('assign pready = \n')
    for II in range(Portsnum):
        File.write('    psel%d_d1 ? pready%d :\n'%(II,II))
    File.write("    1'b1;\n")
    
    File.write('assign pslverr = \n')
    for II in range(Portsnum):
        File.write('    psel%d_d1 ? pslverr%d :\n'%(II,II))
    File.write("    1'b0;\n")

    File.write('assign prdata = \n')
    for II in range(Portsnum):
        File.write('    psel%d_d1 ? prdata%d :\n'%(II,II))
    File.write("    0;\n")

    File.write('endmodule\n')
    File.write(INSTANCE.replace('MODULE',Module))
    for II in range(Portsnum):
        File.write(CONNS.replace('NN',str(II)))
    File.write('); */\n\n')
    File.close()

HEADER = '''
module  MODULE #(parameter DWID=32,parameter AWID=32) (
    input pclk, input presetn
    ,input psel, input pwrite, input penable, input [3:0] pstrb 
    ,output pslverr, output pready
    ,input [AWID-1:0] paddr, input [DWID-1:0] pwdata, output [DWID-1:0] prdata
'''

PORT = '''

    ,output pselNN, output pwriteNN, output [3:0] pstrbNN
    ,input pslverrNN, input preadyNN
    ,output [AWID-1:0] paddrNN, output [DWID-1:0] pwdataNN, input [DWID-1:0] prdataNN
'''

INSTANCE = '''
/* instance template

MODULE MODULE (.pclk(pclk),.prestn(presetn),.psel(psel),.pwrite(pwrite),.penable(penable)
    ,.pwdata(pwdata),.paddr(paddr),.pstrb(pstrb)
    ,.pready(pready),.pslverr(pslverr),.prdata(prdata)
'''

CONNS = '''
    ,.pselNN(pselNN) .penableNN(penableNN).pwriteNN(pwriteNN) .pstrbNN(pstrbNN) .pslverrNN(pslverrNN)
    ,.preadyNN(preadyNN) .paddrNN(paddrNN) .pwdataNN(pwdataNN) .prdataNN(prdataNN)
'''
if __name__ == '__main__': main()
