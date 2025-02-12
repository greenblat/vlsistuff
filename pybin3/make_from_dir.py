#! /usr/bin/env python3
# usage:  make_from_dir.py DSRC EXTSRC DDST DEXT
import os,sys,string

def main():
    Fsrc = sys.argv[1]
    Lsrc = os.listdir(Fsrc)
    Ext = sys.argv[2]
    Fdst = sys.argv[3]
    Fdstext = sys.argv[4]
    for Fname in Lsrc:
        if Fname.endswith('.'+Ext):
            Fcell = Fname.replace('.'+Ext,'')
            if (Fsrc == Fdst) and (Ext == Fdstext):
                Cmd = 'remake %s/%s.%s\n' % (Fdst,Fcell,Fdstext)
            else:
                Cmd = 'make %s/%s.%s\n' % (Fdst,Fcell,Fdstext)
            os.system(Cmd)




if __name__ == '__main__': main()
