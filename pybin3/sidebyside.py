#! /usr/bin/env python3
import os,sys,string

def main():
    Fname1 = sys.argv[1]
    Fname2 = sys.argv[2]
    File = open(Fname1)
    Lines1 = File.readlines()
    File.close()
    File = open(Fname2)
    Lines2 = File.readlines()
    File.close()
    Max = 0
    for line in Lines1:
        Max = max(Max,len(line))

    nums = max(len(Lines1),len(Lines2)) 
    Lout = Fname1
    Lout += ' '*(5+Max-len(Lout))
    Lout += Fname2
    print(Lout)
    print('_'*(10+len(Lout)))


    for Ind in range(nums):
        Lout = '%03d: ' % (Ind+1)
        if Ind < len(Lines1): Lout += Lines1[Ind][:-1]
        Lout += ' '*(5+Max-len(Lout))

        if Ind < len(Lines2): Lout += Lines2[Ind][:-1]
        print(Lout)


if __name__ == '__main__': main()
