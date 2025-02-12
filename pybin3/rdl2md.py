#! /usr/bin/env python3

import os,sys,string

def main():
    Fname = sys.argv[1]
    File = open(Fname)
    Fseq = open('rdl.seq','w')
    Fout = open('rdl.md','w')
    Fout.write(HEADER)

    Lines = File.readlines()
    File.close()
    for line in Lines:
        wrds = line.split()
        if (len(wrds) == 4) and (wrds[0] == '//'):
            if wrds[1] == 'Register':
                Reg = wrds[3]
            if wrds[1] == 'Address':
                Addr = eval(wrds[3])
                addReg(Reg,Addr,Fout,Fseq)
    Fout.close()
    Fseq.close()



def addReg(Reg,Addr,Fout,Fseq):
    Fout.write('| %s | %s |\n' % (Reg,hex(Addr)))
    Fseq.write('define %s  %s\n' % (Reg,hex(Addr)))

HEADER = '''
| reg | addr |
| --- | ---- |
'''




if __name__ == '__main__': main()


'''

      // Register : soft_reset
      // Address  : 0x0
'''
