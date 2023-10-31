

PLACES = {}
PLACED = {}
import logs
import random

import hints

logs.setVar('inputY',0)
logs.setVar('outputX',100)
logs.setVar('topY',100)
logs.setVar('topX',100)

def help_main(Env):
    Mod = Env.Current
    placement0(Mod)
    generateZdraw(Mod)

def generateZdraw(Mod):
    Fout = open('%s.zdraw' % (Mod.Module),'w')
    Fout.write('schematic %s\n' % (Mod.Module))
    for (Type,Name) in PLACES:
        Orient = orientation(Type)
        X,Y = PLACES[(Type,Name)]
        Fout.write('inst %s %s  xy=%s,%a rot=%s\n' % (Type,Name,X,Y,Orient))

    Mod.buildNetTable()
    for Net in Mod.netTable:
        List = Mod.netTable[Net]
        if List[0][2] in ['input','output','inout']:
            St0 = Net
        else:
            St0 = '%s.%s' % (List[0][0],List[0][2])
        for Inst,_,Pin in List[1:]:
            Fout.write('wire %s %s %s.%s\n' % (Net,St0,Inst,Pin))

    Fout.write('end\n')

def placement0(Mod):
    for Net in Mod.nets:
        Dir,_ = Mod.nets[Net]
        if 'input' in Dir:
            place0Net('input',Net)
        elif 'output' in Dir:
            place0Net('output',Net)
        elif 'inout' in Dir:
            place0Net('inout',Net)

    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        zType = zdrawType(Obj.Type)
        place0Inst(zType,Inst)

def place0Inst(Type,Inst):
    X,Y = findFreeXY() 
    PLACES[(Type,Inst)] = (X,Y)
    PLACED[(X,Y)] = (Type,Inst)

def findFreeXY():
    Round = 0
    while Round<100:
        X = logs.getVar('topX')
        X = random.randint(10,X)
        Y = logs.getVar('topY')
        Y = random.randint(10,Y)
        if (X,Y) not in PLACED:
            return X,Y
        Round += 1




def place0Net(Dir,Net):
    if Dir == 'input':
        Y = logs.getVar('inputY')
        PLACES[(Dir,Net)] = (0,Y)
        logs.setVar('inputY',Y+10)

    if Dir == 'output':
        Y = logs.getVar('outputY')
        PLACES[(Dir,Net)] = logs.getVar('outputX'),Y
        logs.setVar('outputY',Y+10)

    if Dir == 'inout':
        X = logs.getVar('topX')//2
        Y = logs.getVar('topY')
        PLACES[(Dir,Net)] = (X,Y)

def zdrawType(Type):
    if Type in hints.ZTYPES: return hints.ZTYPES[Type]
    return Type

def orientation(Type):
    if Type in hints.ZORIENT: return hints.ZORIENT[Type]
    return 'r0'

