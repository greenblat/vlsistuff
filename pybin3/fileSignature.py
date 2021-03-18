#! /usr/bin/env python3
import os,sys


def compSignature(Fname):
    File = open(Fname,'rb')
    Chars = File.read()
    File.close()
    K0 = len(Chars)
    K1 = 0
    K1 = sum(Chars)
    for Chr in Chars:
        K1 += Chr
    return '%10s %11s'%(K0,K1)




def main():
    Fname = sys.argv[1]
    if os.path.isdir(Fname):
        List = os.listdir(Fname)
        for Item in List:
            Full = '%s/%s'%(Fname,Item)
            if os.path.isdir(Full):
                pass
            else:
                Sign = compSignature('%s/%s'%(Fname,Item))
                print(Sign,'  ',Item)
        return

    File = open(Fname)
    Sign = compSignature(Fname)
    print(Sign,'  ',Fname)

    while 1:
        line = File.readline()
        if line=='': return
        wrds = line.split()
        if len(wrds)==0:
            pass
        else:
            work()

if __name__ == '__main__': main()
