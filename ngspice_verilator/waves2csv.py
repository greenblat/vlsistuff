#! /usr/bin/env python3
import os,sys,string

def main():
    Fname = sys.argv[1]
    File = open(Fname)
    Fout = open('out.csv','w')

    while 1:
        line = File.readline()
        if line=='': return
        try:
            wrds = list(map(float,line.split()))
            for ind,x in enumerate(wrds):
                wrds[ind] = x*1.0e6
            wrds = list(map(str,wrds))
        except:
            wrds = line.split()

        Fout.write('%s\n'%','.join(wrds))
    Fout.close()

if __name__ == '__main__': main()
