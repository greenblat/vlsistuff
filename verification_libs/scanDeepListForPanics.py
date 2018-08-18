#! /usr/bin/python

import os,sys,string

Path = os.path.expanduser('~/verification_libs')
sys.path.append(Path)

import logs


def main():
    if len(sys.argv)==1:
        Fname = 'deep.list'
    else:
        Fname = sys.argv[1]
    work(Fname)

def work(Fname):
    if not os.path.exists(Fname):
        print 'cannot open "%s" file, if parameter not given, i look for "deep.list" file.'%Fname
        return
    
    File = open(Fname)
    work2(File)
    File.close()

def work2(File):
    Fout = open('panics.py','w')
    Fout.write(HEADER)
    while 1:
        line = File.readline()
        if line=='':
            Fout.write(FOOTER)
            Fout.close()
            return
        wrds = string.split(line)
        if len(wrds)==0:
            pass
        elif (wrds[0]=='son:'):
            pass
        elif (wrds[0]=='reg:'):
            pass
        elif (wrds[0]=='module:'):
            Path = wrds[2]
        elif (wrds[0]=='net:'):
            Net = wrds[1]
            ww = string.split(Net,'.')
            Panic = ww[-1]
            if logs.startsWith(Panic,'panic'):
                Fout.write('    panics += monitorPanic("%s.%s")\n'%(Path,Panic))
        elif (wrds[0]=='arr:'):
            pass
        else:
            print 'ilia? what is "%s"'%(string.join(wrds,' '))

HEADER='''
import logs
import veri
def monitorPanic(Net):
    Val = logs.peek(Net)
    if Val!=0:
        logs.log_error('monitorPanic activated on %s'%Net)
        return 1
    return 0


def monitorPanics():
    panics=0
'''
FOOTER='''
    veri.force('tb.panics',str(panics))
'''

if __name__ == '__main__':
    main()
