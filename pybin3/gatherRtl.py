#! /usr/bin/env python3

import os,sys
import time

def main():
    Dirs = sys.argv[1:]
    for Dir in Dirs:
        List = os.listdir(Dir)
        for Fname in List:
            if goodEnds(Fname):
                print(">>>>>>> %s/%s" % (Dir,Fname))
                time.sleep(0.1)
                os.system('cat %s/%s' % (Dir,Fname))

def goodEnds(Fname):
    Ends = '.v .sv .rdl .vvv'.split()
    for End in Ends:
        if Fname.endswith(End): return True
    return False

main()



