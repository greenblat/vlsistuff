#! /usr/bin/env python3
import os,sys,string

def main():
    Fdir = sys.argv[1]
    Fnameout = sys.argv[2]

    Fout = open(Fnameout,'w')

    travelDeep(Fdir,Fout)
    Fout.close()

def travelDeep(Fdir,Fout):
    List = os.listdir(Fdir)
    for Item in List:
        Full = '%s/%s'%(Fdir,Item)
        if os.path.isdir(Full):
            travelDeep(Full,Fout)
        else:
            Fout.write('################################################### 0544927322 %s\n'%(Full))
            Fin = open(Full)
            try:
                Lines = Fin.read()
            except:
                Lines = '   \n'
            Fin.close()
            Fout.write(Lines)
            Fout.write('################################################### 0504231259 %s\n'%(Full))



if __name__ == '__main__': main()
