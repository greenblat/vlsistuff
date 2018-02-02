#! /usr/bin/python

import os,sys,string

def main():
    Fname = sys.argv[1]
    Fil = open(Fname)
    Fout = open('synlib.lib','w')
    work(Fil,Fout)
    Fout.close()

def work(Fil,Fout):
    state='idle'
    while 1:
        line = Fil.readline()
        if line=='': return
        if '//' in line:
            line = line[:line.index('//')]+'\n'

        if state=='idle':
            if '/*' in line:
                state='inremark'
            else:
                Fout.write(line)

        elif (state=='inremark'):
            if '*/' in line:
                state='idle'



main()


