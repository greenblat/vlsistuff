#! /usr/bin/env python3.9

import sys
import logs
import shutil

import regfile
LIST = []
def main():
    Fname = sys.argv[1]
    Cell, Dir, Ext = logs.fnameCell(Fname)
    Regfiles = sys.argv[2:]
    if Dir == '':
        Dir = '.'
    File = open(Fname)
    readFile(File)

    if Ext == '':
        run(Cell, Regfiles,Dir)
    else:
        run(Cell, Regfiles,Dir)


def run(Fname, Regfiles,Dirx='.'):
    Present = {}
    for regFile in Regfiles:
        Cell, Dir, Ext = logs.fnameCell(regFile)
        Present[Cell] = regFile,Dir,Ext
    Mdfile = open('%s.md' % Fname,'w') 
    Csvfile = open('%s.csv' % Fname,'w') 
    for Rgf,Instance,Base in LIST: 
        if Rgf not in Present:
            logs.log_error('needed rgf %s is not in given list %s' % (Rgf,list(Present.keys())))
        else:
            regFile,Dir, Ext = Present[Rgf]
            if Dir == '':
                Dir = '.'
            if Ext == '':
                Rname = Rgf
            else:
                Rname = '%s.%s' % (Rgf, Ext)
            regfile.run(Rname, Dir,Base)
            Name = regfile.Db['module']
#            if Name != Instance:
#                shutil.copyfile('%s.md' % Name, '%s.md' % Instance)
            Mdfile.write('# %s   %s\n\n' % (Rgf, Instance))
            Csvfile.write(',,,,\n,,,,\n,file,%s,%s,,,,\n\n' % (Rgf, Instance))
            concatFile('%s.md' % Name,Mdfile)
            concatFile('%s.csv' % Name,Csvfile)
    
#            logs.log_info('%s %x %s' % (Rgf,regfile.Db['lastAddr'],list(regfile.Db.keys())))
    Mdfile.close()        
    Csvfile.close()        

def concatFile(From,To):
    File = open(From)
    Str = File.read()
    File.close()
    To.write(Str)


def readFile(File):
    lines = File.readlines()
    File.close()

    for Lnum,line in enumerate(lines):
        wrds = line.split()
        if wrds == []:
            pass
        elif wrds[0][0] in '#/':
            pass 
        elif wrds[0] == 'rgf':
            Params = regfile.getParams(Lnum,wrds[1:])
            Kind = Params['names'][0]
            if 'instance' in Params:
                Instance = Params['instance']
            else:
                Instance = Kind
            Base = Params['base']
            LIST.append((Kind,Instance,Base))

if __name__ == '__main__': main()
