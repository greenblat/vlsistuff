#! /usr/bin/env python3
import os,sys,string


FNAMES = 'log.yosys *yosys.log recorded.nets dump.vcd pymon.* tb.vvp deep.list'.split()


def main():
    count = 0
    Frm = open('removes','w')
    for Fname in FNAMES:
        os.system('find . -name "%s" > /tmp/clean.list' % Fname)
        File = open('/tmp/clean.list')
        lines = File.readlines()
        File.close()
        for line in lines:
            Frm.write('/bin/rm -f %s' % line)
            count += 1
    Frm.close()
    print('found %d files to remove' % count)
if __name__ == '__main__': main()
