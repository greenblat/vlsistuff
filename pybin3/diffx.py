#! /usr/bin/env python3
import os,sys,string

def main():
    Fa = sys.argv[1]
    Fb = sys.argv[2]

    os.system('grep -v "  sign_version = 64" %s | grep -v FROMFILE > /tmp/diffx1' % (Fa))
    os.system('grep -v "  sign_version = 64" %s | grep -v FROMFILE > /tmp/diffx2' % (Fb))
    os.system('diff -qbBw /tmp/diffx1 /tmp/diffx2')






if __name__ == '__main__': main()
