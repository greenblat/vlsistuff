#! /usr/bin/env python3
'''
    turn md from generated regfile into sequence for testing it
    ['', '0x3c', 'cpu_test_caches_controls', ' ', ' ', 'rw', '14', ' ', '"test modes of icache and dcache rams"', '\n']
'''
import os,sys,string
import random


HEADER = '''

print READING WRITING of GLOBAL_RGF

include addressMap.seq
include ../hdl/global_rgf_inc.seq

define BASEADDR GLOBAL_RGF

wait 1000
waitUntil (dut.hresetn==1)
wait 100

'''

FOOTER = '''

wait 100
ahb waitNotBusy 5000
wait 100
finish

'''



def main():
    Fname = sys.argv[1]
    File = open(Fname)
    lines = File.readlines()
    File.close()
    
    Cell = cellName(Fname)
    Fout = open('%s_test.seq'%Cell,'w')
    Fout.write(HEADER)
    READS = []
    for line in lines:
        wrds = line.split('|')
        if len(wrds)<7:
            pass
        elif (wrds[1]!='')and(wrds[1][0]=='0'):
            Addr = wrds[1]
            Reg = wrds[2]
            Access = wrds[5]
            Wid = eval(wrds[6])
            Val = random.randint(0x80000000,0xffffffff)
            Masked = Val & ((1<<Wid)-1)
            if Access in ['rw','rw_pulse']:
                Fout.write('print writing _%s wid=%s\n'%(Reg,Wid))
                Fout.write('ahb write BASEADDR+%s %s\n'%(Addr,hex(Val)))
                READS.append((Addr,Masked,Reg,Wid))

    for (Addr,Masked,Reg,Wid) in READS:
        Fout.write('print reading _%s wid=%s\n'%(Reg,Wid))
        Fout.write('ahb read BASEADDR+%s %s\n'%(Addr,hex(Masked)))
    Fout.write(FOOTER)
    Fout.close()


def cellName(Fname):
    X = Fname.split('/')
    X0 = X[-1]
    X = X0.split('.')
    return X[0]

if __name__ == '__main__': main()

