#! /usr/bin/env python3
import os,sys,string
def main():
    Fname = 'deep.list'
    if len(sys.argv)>1:
        Fname = sys.argv[1]
    File = open(Fname)
    readFile(File)

    Fout = open('xmon.py','w')
    print('%d regs'%len(LONG))
    Fout.write(HEADER)
    Fout.write('LONG = [\n  "%s"'%LONG[0])
    for Reg in LONG:
        Fout.write('    ,"%s"\n'%(Reg))
    Fout.write(']\n')
    Fout.close()

HEADER = '''
import veri
import logs
VALS = {}
def run():
    for Reg in LONG:
        Val = veri.peek(Reg)
        if Reg not in VALS: 
            VALS[Reg] = Val
        else:
            Was = VALS[Reg]
            VALS[Reg] = Val
            if forWorse(Was,Val):
                logs.log_error('for worse %s %s -> %s'%(Reg,Was,Val))

def forWorse(Bef,Aft):
    return ('x' in Aft) and not ('x' in Bef)

'''

def readFile(File):
    while 1:
        line = File.readline()
        if line=='': return
        wrds = line.split()
        if wrds==[]:
            pass
        elif wrds[0] == "module:" :
            Path = wrds[2]
        elif wrds[0] == "reg:" :
            Reg = wrds[1]
            if '.' in Path:
                record(Path,Reg)
LONG = []
def record(Path,Reg):
    Net = '%s.%s'%(Path,Reg)
    LONG.append(Net)

if __name__ == '__main__': main()
