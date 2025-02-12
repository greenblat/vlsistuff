#! /usr/bin/env python3
import os,sys,string

def main():
    Fname1 = sys.argv[1]
    File = open(Fname1)
    Lines1 = File.readlines()
    File.close()

    Fname2 = sys.argv[2]
    File = open(Fname2)
    Lines2 = File.readlines()
    File.close()

    DB = {}
    for line in Lines1:
        wrds = line.split()
        Key = ' '.join(wrds[:-1])
        Num = eval(wrds[-1])
        DB[Key] = Num

    for line in Lines2:
        wrds = line.split()
        Key = ' '.join(wrds[:-1])
        Num = eval(wrds[-1])
        if Key in DB:
            DB[Key] += Num
        else:
            DB[Key] = Num
    Fout = open(sys.argv[3],'w')
    for Key in DB:
        Fout.write('%s %s\n' % (Key,DB[Key]))

    Fout.close()


if __name__ == '__main__': main()
