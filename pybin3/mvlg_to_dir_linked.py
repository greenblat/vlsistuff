#! /usr/bin/python3


import os,sys,string
defines={}
def main():
    global defines
    Mvlgname = sys.argv[1]
    Odir = sys.argv[2]
    os.system('mvlg.py %s files.files'%(Mvlgname))
    File1 = open('files.files','r')
    lines = File1.readlines()
    File1.close()
    if not os.path.exists(Odir):
        os.system('mkdir %s'%(Odir))
    for line in lines:
        if (len(line)>0):
            if (line[0]=='+'):
                print('plus_line ',line),
                if '+define+' in line:
                    line = line.replace('+define+','')
                    line = line.replace('=',' ')
                    wrds = line.split()
                    if (len(wrds)==1):
                        wrds=wrds+['1']
                    defines[wrds[0]]=wrds[1] 
            else:
                ww = line.split()
                if (ww[0]=='-v'):
                    os.system('ln -s %s %s/'%(ww[1],Odir))
                elif ((ww[0])[0]!='-'):
                    os.system('ln -s %s %s/'%(ww[0],Odir))
    print('creating mvlg_defines_file')
    Ofile = open('%s/mvlg_defines.v'%(Odir),'w')
    for Key in defines:
        Val = defines[Key]
        Ofile.write('`define %s %s\n'%(Key,Val))
    Ofile.close()
main()


