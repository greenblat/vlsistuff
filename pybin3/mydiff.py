#! /usr/bin/env python3
import os,sys,string

def main():
    Afname = sys.argv[1]
    Bfname = sys.argv[2]
    Adir = getDir(Afname)
    Bdir = getDir(Bfname)
    if Adir and not os.path.exists('/tmp/%s' % Adir): os.mkdir('/tmp/%s' % Adir)
    if Bdir and not os.path.exists('/tmp/%s' % Bdir): os.mkdir('/tmp/%s' % Bdir)
    os.system('grep -v FROM %s | grep -v sign_version > /tmp/%s' % (Afname,Afname))
    os.system('grep -v FROM %s | grep -v sign_version > /tmp/%s' % (Bfname,Bfname))
    Os = os.popen('diff -bBw /tmp/%s /tmp/%s' % (Afname,Bfname))
    Lines = Os.readlines()
    for line in Lines:
        print(line[:-1])

def getDir(Fname):
    if '/' in Fname:
        return Fname[:Fname.index('/')]
    return False


if __name__ == '__main__': main()
