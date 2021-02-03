#! /usr/bin/env python3
import os,sys,string

def main():
    Fname = sys.argv[1]
    Fin = open(Fname)
    state = 'idle'
    while True:
        line = Fin.readline()
        if line=='': return
        state = work(line,state)


def work(line,state):
    global Fmid
    if state=='idle':
        if '0544927322' in line:
            wrds = line.split()
            if (len(wrds)==3)and(wrds[0][:5] == '#####'):
                Fname = wrds[2]
                Fmid = openFile(Fname)
                return 'work'
    elif state=='work':
        if '0504231259' in line:
            wrds = line.split()
            if (len(wrds)==3)and(wrds[0][:5] == '#####'):
                Fmid.close()
                return 'idle'
        else:
            Fmid.write(line)
            return 'work'

    return state


def openFile(Path):
    mkdirPath(Path)
    return open(Path,'w')

def mkdirPath(Path):
    if '/' not in Path: return
    WW = Path.split('/')
    WW.pop(-1)
    print(WW,Path)
    for ii in range(1,len(WW)+1):
        Sub = '/'.join(WW[:ii])
        Abs = os.path.abspath(Sub)
        print(Abs,Sub,ii,len(WW)+1)
        if not os.path.exists(Abs):
            os.mkdir(Sub)


if __name__ == '__main__': main()
