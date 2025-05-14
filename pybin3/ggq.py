#! /usr/bin/env python3
import os,sys,string

def main():
    Dir1 = sys.argv[1]
    Dir2 = sys.argv[2]
    List1 = os.listdir(Dir1)
    List2 = os.listdir(Dir2)
    All = []
    for File1 in List1:
        if File1 in List2:
            Cmd = 'diffx.py %s/%s %s/%s' % (Dir1,File1,Dir2,File1) 
            X = os.popen(Cmd)
            Res = X.readlines()
            for line in Res:
                if 'differ' in line:
                    All.append('%s/%s %s/%s differ' % (Dir1,File1,Dir2,File1))
            X.close()
    for File1 in List1:
        if File1 not in List2:
            print('only in < : %s' % File1)
    for File2 in List2:
        if File2 not in List1:
            print('only in > : %s' % File2)
    for line in All:
        wrds = line.split()
        print('diff -Bbw %s %s' % (wrds[0],wrds[1]))
    if All == []:
        print('NO DIFFS')
    return

#    Cmd = 'diff -qbBw %s %s' % (Dir1,Dir2) 
#    Cmd = 'diffx.py -qbBw %s %s' % (Dir1,Dir2) 
#    Cmd = 'mydiff.qq  %s %s' % (Dir1,Dir2) 
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
                print('diffx.py -bBw %s %s' % (F1,F2))
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
