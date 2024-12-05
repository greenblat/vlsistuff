#! /usr/bin/env python3

import os,sys

def main():
    Dirs = sys.argv[1:]
    for Dir in Dirs:
        List = os.listdir(Dir)
        for Fname in List:
            if Fname.endswith('.v') or Fname.endswith('.rdl') or Fname.endswith('.vvv'):
                print(">>>>>>> %s/%s" % (Dir,Fname))
                os.system('cat %s/%s' % (Dir,Fname))


main()



