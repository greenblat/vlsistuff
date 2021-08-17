#! /usr/bin/python3
import os,sys


DB = []
def main():
    Fname = sys.argv[1]
    File = open(Fname)
    readFile(File)
    DB.sort()
    DB.reverse()
    for Count,Module in DB:
        print('%10d   %s' % (Count,Module))

def readFile(File):
    Count = 0
    while 1:
        line = File.readline()
        if line=='': return
        wrds = line.split()
        if len(wrds)>0:
            if wrds[0] == 'module':
                Module = wrds[1]
                Count = 0
            elif 'endmodule' in wrds:
                if Count>1:
                    DB.append((Count,Module))
            elif 'DFF' in wrds[0]:
                Count += 1

if __name__ == '__main__': main()

