#! /usr/bin/env python3
import os,sys,string
# `define MLCPU_REGMAP_LDSTPROG_ADDR               `UVM_REG_ADDR_WIDTH'h0000

def main():
    Fname = sys.argv[1]
    X = os.popen('/Users/iliagreenblat/clients/magic/Rocky/rocky -sv %s' % Fname)
    lines = X.readlines()
    ww = lines[0].split('/')
    Sname = ww[-1][:-1]
    Fil = open(Sname)
    Lines = Fil.readlines()
    Fil.close()
    LL = []
    for line in Lines:
        if ('`define' in line) and ('_ADDR' in line):
            ww = line.split()
            if len(ww) == 3:
                Reg = ww[1].replace('_ADDR','')
                if 'h' in ww[2]:
                    Ind = ww[2].index('h')
                    Addr = ww[2][Ind+1:]
                    LL.append([Reg,Addr])
    Ok = True
    while Ok:
        Ok = check(LL)
        if Ok:
            for ind,[A,B] in enumerate(LL):
                LL[ind] = [A[1:],B]
    Fout = open('regs.seq','w')                
    for A,B in LL:
        aa = A.lower()
        if aa.endswith('_0'):
            Fout.write('define %s 0x%s\n' % (aa[:-2],B))
        Fout.write('define %s 0x%s\n' % (aa,B))
    Fout.close()



def check(LL):
    Let = LL[0][0][0]
    for [A,B] in LL:
        if A[0] != Let: return False

    return True



if __name__ == '__main__': main()
