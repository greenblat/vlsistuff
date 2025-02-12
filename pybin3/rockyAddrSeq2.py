#! /usr/bin/env python3

#       if (PADDR == 8'h0) begin
#          server_0_src_addr_decoded    = 1'b1;



import os,sys,string

def main():
    Fname = sys.argv[1]
    File = open(Fname)
    Fout = open('regs.seq','w')

    Lines = File.readlines()
    Addr = -1
    for line in Lines:
        if ("if (PADDR ==" in line)and('begin' in line):
            line = line.replace(')',' ')
            line = line.replace('else','')
            wrds = line.split()
            if len(wrds) == 5:
                Addr = wrds[3]
                if 'h' in Addr:
                    Addr2 = Addr.split('h')
                    Addr = Addr2[1]
        elif ('_decoded' in line):
            wrds = line.split()
            Reg = wrds[0]
            Reg = Reg.replace('_decoded','')
            if Addr != -1:
                print("REG",Reg,Addr)
                Fout.write('define %s 0x%s\n' % (Reg,Addr))
            Addr = -1
    Fout.close()

if __name__ == '__main__': main()
