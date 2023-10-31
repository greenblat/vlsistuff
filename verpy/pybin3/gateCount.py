
import sys,os
import logs

try:
    import cellLibrary as libx
except:
    print('no cellLibrary.py')
    sys.exit()

def help_main(Env):
    Mod = Env.Current
    if '-gate' in Env.params:
        GateCell = Env.params['-gate'][0]
    else:
        GateCell = findOneGateCell()
    GateArea = libx.CellLib[GateCell].params['area']

    Gates = 0
    Area  = 0
    Cells = 0
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        if Type in libx.CellLib:
            La = libx.CellLib[Type].params['area']            
            Area += La
            Gates += La/GateArea
            Cells += 1
    print('cells=%d area=%.2f gates=%d gatecell=%s' % (Cells,Area,int(Gates),GateCell))






def findOneGateCell():
    Nands = []
    for Cell in libx.CellLib:
        if 'nand2' in Cell:
            Obj = libx.CellLib[Cell]
            if 'area' in Obj.params:
                Area = Obj.params['area']
                Nands.append((Area,Cell))
    Nands.sort()
    if len(Nands) > 1:
        return Nands[1][1]
    if len(Nands) == 1:
        return Nands[0][1]
    print('didnt find nand2 gate, add -gate CellName to run')
    sys.exit()
