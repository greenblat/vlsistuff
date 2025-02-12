#! /usr/bin/env python3
import os,sys,string

def main():
    Load = cpuLoad()
    print('load %d' % int(Load))

END = 'PID    COMMAND          %CPU TIME'.split()

def cpuCopies(List):
    os.system('top -l 2 > /tmp/cpu.log')
    File = open('/tmp/cpu.log')
    Lines = File.readlines()
    File.close()
    Lines.reverse()
    Tot = 0
    for line in Lines:
        wrds = line.split()
        if compatible(wrds,END): return Tot 
        if type(List) is list:
            if (len(wrds)>2) and (wrds[1] in List):
                Tot += 1
        else:
            if (len(wrds)>2) and (wrds[1] == List):
                Tot += 1
    return Tot

def cpuLoad():
    os.system('top -l 2 > /tmp/cpu.log')
    File = open('/tmp/cpu.log')
    Lines = File.readlines()
    File.close()
    Lines.reverse()
    Tot = 0
    for line in Lines:
        wrds = line.split()
        if compatible(wrds,END): return Tot 
        Val = findNumber(wrds)
        try:
            Load = eval(Val)
        except:
            Load = 100
            print('BADBABDBABABD',wrds)
        Tot += Load
        
    return Tot

def findNumber(wrds):
    for Ind in [2,3,4,5]:
        if len(wrds)>Ind:
            Wrd = wrds[Ind]
            if (':' not in Wrd) and (Wrd[0] in '012345678'): return Wrd
    return 0

def compatible(List0,List1):
    if List0 == []: return False
    if len(List1)>len(List0): return False
    X = List0[:len(List1)]
    return X == List1

if __name__ == '__main__': main()
