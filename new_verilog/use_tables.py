#! /usr/bin/env python3

import os,sys

Totals = {}
Calls = {}
Finals = {}

def main():
    Top = sys.argv[1]
    build(Top)
    print(Totals[Top])
    LL = []
    for Mod in Totals:
        if Totals[Mod]>3:
            LL.append((Totals[Mod],Mod))
    LL.sort()
    LL.reverse()
    for Tot,Mod in LL:
        print('    %s %s' % (Tot,Mod))

def build(Top):
    if Top in Totals: return Totals[Top]

    readTable(Top)
    if Top not in Finals:
        List = Calls[Top]
        Tot = 0
        for (Son,Many) in List:
            if Son in Finals: 
                Tot += Many
            else:
                Add = build(Son)
                Tot += Add*Many
        Totals[Top] = Tot
        return Tot                
    return 1


def readTable(Top):
    if Top in Finals: return
    if Top in Calls: return

    Fname = 'tables/%s.table' % Top
    if os.path.exists(Fname):
        Fin = open(Fname)
        lines = Fin.readlines()
        Fin.close()
        for line in lines:
            wrds = line.split()
            if len(wrds) == 3:
                addCall(wrds[0],wrds[1],wrds[2])
            else:
                print('error! %s %s' % (Top,wrds))
    else:
        Finals[Top] = True

def addCall(Module,Son,Times):
    Times = eval(Times)
    if Module not in Calls: Calls[Module] = []
    Calls[Module].append((Son,Times))


main()



