#! /usr/bin/env python3
import os,sys,string


FNAMES =  'db0.pickle xxx yacc.log a.out dumpver.v *.pyc *.log0 *.logseq log.yosys *yosys.log recorded.nets dump.vcd pymon.* tb.vvp deep.list'.split()


def main():
    count = 0
    Frm = open('removes','w')
    os.system('find . >  /tmp/clean.list')
    File = open('/tmp/clean.list')
    lines = File.readlines()
    File.close()
    for Fname in FNAMES:
        for line in lines:
            Last = line.split('/')[-1].strip()
            if Last == Fname:
                Frm.write('/bin/rm -f %s' % line)
                count += 1
            elif (Fname[0] == '*') and (Last.endswith(Fname[1:])):
                Frm.write('/bin/rm -f %s' % line)
                count += 1
            elif (Fname[-1] == '*') and (Fname[:-1] in Last):
                Frm.write('/bin/rm -f %s' % line)
                count += 1
    Frm.close()
    print('found %d files to remove' % count)
if __name__ == '__main__': main()
