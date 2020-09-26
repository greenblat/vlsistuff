#! /usr/bin/env python3

import os,sys,string

def main():
    Infile = sys.argv[1]
    Outfile = sys.argv[2]
    os.system('mvlg.py  %s  tmp.tmp'%Infile)
    lines = open('tmp.tmp').readlines()
    Fout = open(Outfile,'w')
    Finc = open('runme.file','w')
    Finc.write('~iliag/pybin/macro_verilog_pp.py %s \\\n'%(Outfile))
    for line in lines:
        wrds = line.split()
        if '+incdir+' in line:
            line = line.replace('+incdir+','')
            line = line.replace('+','')
            wrds = line.split()
            Finc.write('   -y  %s ///n'%(wrds[0]))
            Fname = False
        elif len(wrds)==1:
            Fname = wrds[0]
        elif (len(wrds)==2)and(wrds[0]=='-v'):
            Fname = wrds[1]
        else:
            Fname = False
        if Fname:
            copyFile(Fname,Fout)
            

Bads = ['\r',chr(0x92),chr(0x9),chr(0x85),chr(0x96),chr(0xb7)]
def copyFile(Fname,Fout):
    if not os.path.exists(Fname):
        Fout.write('// %s doesnt  exist\n'%(Fname))
        return
    Fin = open(Fname)
    while 1:
        line = Fin.readline()
        res = ''
        for ch in line:
            if ch not in Bads:
                res += ch
            else:
                res += ' '
                
        if line=='':
            Fout.write('\n\n\n')
            Fin.close()
            return
        Fout.write(res)


main()





