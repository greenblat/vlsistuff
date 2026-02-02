#! /usr/bin/env python3
import os,sys,string
import signVerilogModule

def main():
    if len(sys.argv)>1:
        work(sys.argv[1])
    else:
        work('rtl')

def work(Dir):
    Cellar = os.path.expanduser('~/cellar')
    if not os.path.exists(Cellar):
        os.mkdir(Cellar)
    if not os.path.exists(Dir):
        print("No directory %s" % Dir)
        return
    if os.path.isdir(Dir):
        List = os.listdir(Dir)
        for Fname in List:
            if Fname.endswith('.v'):
                File = '%s/%s'% (Dir,Fname)
                checkFile(File)
    else:
        checkFile(Dir)

#            When = signVerilogModule.work('%s/%s'% (Dir,Fname))
#            if When:
#                os.system('/bin/cp %s/%s ~/cellar/%s_%s ' % (Dir,Fname,When,Fname))

def checkFile(Fname):
    When = signVerilogModule.work(Fname)
    ww = Fname.split('/')
    Cell = ww[-1]
    if When:
        os.system('/bin/cp %s ~/cellar/%s_%s ' % (Fname,When,Cell))


if __name__ == '__main__': main()
