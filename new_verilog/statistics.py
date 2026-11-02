#! /usr/bin/env python3

import os,sys
import importlib
DB = {}
Calls = {}
Called = {}
Totals = {}
def main():
    Fname = sys.argv[1]
    if '/' in Fname:
        wrds = Fname.split('/')
        Path = '/'.join(wrds[:-1])
        sys.path.append(Path)
        Fname = wrds[-1]
    if Fname.endswith('.py'):
        Fname = Fname[:-3]
    That = importlib.import_module(Fname)
    RawModules = That.modules
    maketables(RawModules)

def maketables(RawModules):
    if len(sys.argv)>2: 
        Fname = sys.argv[2]
    else:
        Fname = 'out.table'
    Fout = open(Fname,'w')
    for Module in RawModules:
        Insts = RawModules[Module]['instances']
        Nice = niceName(Module)
        Calls[Nice] = {}
        for Inst in Insts:
            Type = Insts[Inst]['module']
            Nice2 = niceName(Type)
            add_call(Nice,Nice2)
    for Mod in Calls:
        for Son in Calls[Mod]:
            Num = Calls[Mod][Son]
            Fout.write('%s %s %d\n' % (Mod,Son,Num))

    Fout.close()

def add_call(Mod,Son):
    if Son in Calls[Mod]:
        Calls[Mod][Son] += 1
    else:
        Calls[Mod][Son] = 1


def work(RawModules):
    for Module in RawModules:
        Insts = RawModules[Module]['instances']
        Nice = niceName(Module)
        Calls[Nice] = []
        DB[Nice] = {}
        Now = DB[Nice]
        Now['cells'] = 0
        for Inst in Insts:
            Type = Insts[Inst]['module']
            Nice2 = niceName(Type)
            if Nice2 not in Called: Called[Nice2] = []

            if Type in RawModules:
                if Nice2 not in Calls[Nice]: Calls[Nice].append(Nice2)
                if Nice not in Called[Nice2] : Called[Nice2].append(Nice)
                if Nice2 not in Now:
                    Now[Nice2] = 1
                else:
                    Now[Nice2] += 1
            else:
                Now['cells'] += 1

    for Module in DB:
        Tot = compute(Module,DB,Totals)
        Totals[Module] = Tot
    Fout = open('out.csv','w')
    Fout.write("cell,local,deep\n")
    for Module in DB:
        if Module != 'cells':
            print(Module,DB[Module]['cells'],Totals[Module])
            Fout.write("%s,%d,%d\n" % (Module,DB[Module]['cells'],Totals[Module]))
    Fout.close()

    for MM in Calls: 
        if MM not in Called:
            Top = MM
    print("TOP",Top)
    Fout = open('hier.csv','w')
    Fout.write("cell,local,deep,son,local,deep\n")
    hier(Top,'',Fout)
    Fout.close()

def hier(Top,Pref,Fout):
    List = Calls[Top]
    Fout.write('%s,%d,%d,%s%s\n' % (Top,DB[Top]['cells'],Totals[Top],Pref,Top))
    Pref = Pref + ','
    for Son in List:
        hier(Son,Pref,Fout)



def compute(Module,DB,Totals):
    Cells = DB[Module]
    if Module in Totals: return Totals[Module]
    Tot = 0
    for Cell in Cells:
        if Cell == 'cells':
            X = Cells[Cell]
        else:
            X = compute(Cell,DB,Totals)
        Tot += X
    Totals[Module] = Tot        
    return Tot
        
def niceName(Module):
    if 'paramod' in Module:
        xx = Module.split('\\')
        xx = xx[1:]
        Module = '_'.join(xx)
        Module = Module.replace("=s32'",'|')
        while '|0' in Module:
            Module = Module.replace("|0",'|')
    return Module



main()




