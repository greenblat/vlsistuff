#! /usr/bin/python

import os,sys,string

START = 'synthesis_off'
STOP = 'synthesis_on'
def main():
    Fname = sys.argv[1]
    File = open(Fname)
    lines = File.readlines()
    Fout = open('cleaned.vhd','w')
    state='idle'
    for line in lines:
        wrds = string.split(line)
        if wrds==[]:
            pass
        elif state=='idle':
            Fout.write(line)
            if '--' in wrds[0]:
                if START in line:
                    state= 'off'
        elif (state=='off'):
            if '--' in wrds[0]:
                if STOP in line:
                    state= 'idle'
                Fout.write(line)
            else:
                Fout.write('--   '+line)
            
main()

