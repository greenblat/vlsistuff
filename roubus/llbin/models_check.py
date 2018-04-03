#! /usr/bin/python

import os,sys,string

def main():
    List = os.listdir('models')
    Fout = open('chk.list','w')
    for Fname in List:
        if '.v'==Fname[-2:]:
            Fout.write('models/%s\n'%(Fname))
    Fout.close()
    os.system('iverilog -f chk.list')
    os.system('/bin/rm a.out')


main()


        
