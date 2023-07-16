#! /usr/bin/env python3
import os,sys,string

def main():
    Dir1 = sys.argv[1]
    Dir2 = sys.argv[2]
    Cmd = 'diff -qbBw %s %s' % (Dir1,Dir2) 
    X = os.popen(Cmd)
    Res = X.readlines()
    X.close()
    onlies = 0
    diffies = 0
    LL = []
    Onlies = []
    for line in Res:
        if 'differ' in line:
            wrds = line.split()
            if len(wrds) >= 4:
                F1 = wrds[1]
                F2 = wrds[-2]
                LL.append((F1,F2))
                print('diff -bBw %s %s' % (F1,F2))
                diffies += 1
        elif ('Only' in line):
            onlies += 1
            Onlies.append(line)
    for (F1,F2) in LL:
        print('/bin/cp %s %s' % (F1,F2))
    print('\n\n\n')
    for line in Onlies:
        print(line[:-1])
    print('onlies %d diffies %d tots %d ' % (onlies,diffies,len(Res)))
                

if __name__ == '__main__': main()
