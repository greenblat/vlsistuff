#! /usr/bin/env python3

import os,sys
def main():
    Pool0 = os.listdir('tmppy')
    for Fname in Pool0:
        Full = 'tmppy/%s' % Fname
        if Full.endswith('.py'):
            Dest = 'tables/%s.table' % Fname[:-3]
            if not os.path.exists(Dest):
                print(">>> %s" % Fname)
                os.system('statistics.py %s %s' % (Full,Dest))

main()





