#! /usr/bin/env python3
import os,sys,string

def main():
    Fname = sys.argv[1]
    ww = Fname.split('/')
    Top = ww[-1]
    if len(ww)==1:
        Path = '.'
    else:
        Path = '/'.join(ww[:-1])

    List = [Fname,'vlib.v']
    runRounds(List,Path)

def runRounds(List,Path):
    Miss = runList(List,Path)
    print(Miss)
    Down = Miss+List
    Down = set(Down)
    Down = list(Down)
    if len(Down)>len(List):
        runRounds(Down,Path)
    




def runList(List,Path):
    Mvlg = open('tmp.mvlg','w')
    for Fname in List:
        Mvlg.write('%s\n'%(Fname))
    Mvlg.close()
    os.system('mvlg.py tmp.mvlg tmp.files')
    os.system('iverilog -f tmp.files >& tmp.log')
    Flog = open('tmp.log','r')
    lines = Flog.readlines()
    Flog.close()
    Missings = missings(lines,Path)
    return Missings



def missings(lines,Path):
    Mis = []
    for line in lines:
        wrds = line.split()
        if (len(wrds)==4)and(wrds[1]=='referenced'):
            Cell = wrds[0]
            Mis.append('%s/%s.v'%(Path,Cell))
    return Mis

if __name__ == '__main__': main()

