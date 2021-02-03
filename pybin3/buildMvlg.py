#! /usr/bin/env python3
'''
give path to top level module

'''

import os,sys,string

def main():
    Fpath = sys.argv[1]
    Tip = sys.argv[2]
    Db = {}
    scanTheDir(Fpath,Db)
    Len = len(list(Db.keys()))
    print('found %d verilog files for %s'%(Len,Tip))
    for Key in Db:
        print("|%s|%s|"%(Key,Db[Key]))
    if Tip in Db:
        Tfile = Db[Tip]
        runRounds([Tfile],Db)
    else:
        print('no %s'%Tip)

def scanTheDir(Dir,Db):
    List = os.listdir(Dir)
    for Fname in List:
        if Fname.endswith('.v')or Fname.endswith('.sv')or Fname.endswith('.vh'):
            Cell = Fname.split('.')[0]
            Db[Cell] = '%s/%s'%(Dir,Fname)
        elif os.path.isdir('%s/%s'%(Dir,Fname)):
            scanTheDir('%s/%s'%(Dir,Fname),Db)



def runRounds(List,Db):
    print('enter %d'%(len(List)))
    Miss = runList(List,Db)
    print(len(Miss))
    Down = Miss+List
    Down = set(Down)
    Down = list(Down)
    if len(Down)>len(List):
        runRounds(Down,Db)
    else:
        print('final len %s'%len(Down))
        for Mis in Miss:
            print(' missing %s'%Mis)




def runList(List,Db):
    Mvlg = open('tmp.mvlg','w')
    for Fname in List:
        Mvlg.write('%s\n'%(Fname))
    Mvlg.close()
    os.system('mvlg.py tmp.mvlg tmp.files')
    os.system('iverilog -f tmp.files -I rtl  >& tmp.log')
    Flog = open('tmp.log','r')
    lines = Flog.readlines()
    Flog.close()
    Missings = missings(lines,Db)
    return Missings



def missings(lines,Db):
    Mis = []
    for line in lines:
        wrds = line.split()
        if (len(wrds)==4)and(wrds[1]=='referenced'):
            Cell = wrds[0]
            if Cell in Db:
                Path = Db[Cell]
                Mis.append('%s'%(Path))
    return Mis

if __name__ == '__main__': main()

