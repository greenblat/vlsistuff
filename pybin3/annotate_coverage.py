#! /usr/bin/env python3

import os,sys

def main():
    Mvlg = sys.argv[1]
    File = open(Mvlg)
    Lines = File.readlines()
    for line in Lines:
        ww = line.split()
        if len(ww)>0:
            Rtl = ww[0]
            os.system('pyver.py %s -do annotate_linecov -do clean -cover coverage.report' % Rtl)
            w0 = Rtl.split('/')
            w1 = w0[-1].split('.')
            Module = w1[0]
            if os.path.exists('%s.txt' % Module):
                os.system('/bin/mv %s.txt annotated' % Module)
    os.system('pyver.py -do clean')

main()



