#! /usr/bin/env python3.10
import os,sys,string
sys.path.append('/Users/iliagreenblat/verification_libs3')
import pandas as pd

import logs


def main():
    Fname = sys.argv[1]
    df = pd.read_excel(Fname)
    Cell = logs.fnameCell(Fname)
    Csv = df.to_csv()
    Fout = open('%s.csv' % Cell,'w')
    Fout.write(Csv)
    Fout.close()

if __name__ == '__main__': main()
