#! /usr/bin/python

HelpString = '''
    lookforPath <dir> <path>
    dir is directory where single module file reside
    path is dotted path to instance (like chip.dma.master1.fifo0 ) 
      after synthesis, instance names tend to become long and not as module names, especially if they are duplicated.
      this module helps navgate the directory full of single module files to find the correct one.
'''
import os,sys,string

def main():
    if len(sys.argv)==1:
        print(HelpString)
        return
    Dir = sys.argv[1]
    Path  = string.split(sys.argv[2],'.')
    lookDeep(Path[0],Dir,Path[1:])



def lookDeep(Module,Dir,Path):
    print('enter module',Module,Path)
    if Path==[]: 
        print('final: %s/%s.v'%(Dir,Module))
        return

    File = open('%s/%s.v'%(Dir,Module))
    Inst = Path[0]
    Down = scanFile(File,Inst,Path[1:])
    if not Down:
        print('exit: %s/%s.v not found inst %s'%(Dir,Module,Inst))
        return
    File.close()        
    print('going down module %s is %s'%(Inst,Down))
    lookDeep(Down,Dir,Path[1:])


def scanFile(File,Inst,More):
    Line = ''
    while True:
        while ';' not in Line:
            line = File.readline()
            line = string.replace(line,'(',' ( ')
            Line += line
            if (line==''): return False
        Pos = Line.index(';')
        Bef = Line[:Pos]
        Aft = Line[Pos+1:]
        Line = Aft
        wrds = string.split(Bef)
#        print('DOWN',(wrds[1]==Inst),(wrds[0]!='module'),More,wrds)
        if (wrds[1]==Inst)and(wrds[0]!='module'):
            return wrds[0]

        if (wrds[1]==Inst)and(wrds[0]=='module')and(More==[]):
            return wrds[1]


if __name__ == '__main__': main()
