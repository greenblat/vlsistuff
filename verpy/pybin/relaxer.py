#! /usr/bin/python
import os,sys,string

def main():
    Fname = sys.argv[1]
    File = open(Fname)
    Fout = open('out.file','w')
    Fv = open('out.v','w')

    while 1:
        line = File.readline()
        if line=='': return
        wrds = string.split(line)
        if len(wrds)==0:
            pass
        elif (len(wrds)>=4)and(wrds[-3]=='token'):
            if wrds[0][0]=='\\':
                Txt = wrds[0][1:]
                for Chr in '[]\\./':
                    Txt = Txt.replace(Chr,'_')
                wrds[0] = Txt
                line = string.join(wrds,' ')+'\n'
            Fout.write(line)
            Fv.write(wrds[0]+'\n')

        else:
            Fout.write(line)
            Fv.write(wrds[0]+'\n')


if __name__ == '__main__': main()
