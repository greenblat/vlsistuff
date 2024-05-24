


def help_main(Env):
    if  '-list' in Env.params:
        Dir = Env.params['-list']
        workList(Dir)
        return
    singleCell(Env)        

    
def manyCells(Env):
    Fout = open('primitives.py','w')
    Fout.write('import snl\n')
    for Cell in Env.Modules:
        Mod = Env.Modules[Cell]
        workCell(Mod,Fout)

def singleCell(Env):
    Mod = Env.Current
    Fout = open('%s.py' % Mod.Module,'w')
    workCell(Mod,Fout)
    Fout.close()

def workCell(Mod,Fout):
    Cell = Mod.Module
    Inps,Outs = [],[]
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if 'input' in Dir:
            Inps.append(Net)
        elif 'output' in Dir:
            Outs.append(Net)
    if (Inps==[])and(Outs==[]):
        Fout.write('# empty %s\n' % Cell)
    else:
        Fout.write('def %s (lib):\n' % Cell)
        Fout.write('    cell = snl.SNLDesign.createPrimitive(lib, "%s")\n' % Cell)
        for In in Inps:
            Fout.write('    %s = snl.SNLScalarTerm.create(cell, snl.SNLTerm.Direction.Input, "%s")\n' % (In,In))
        for Out in Outs:
            Fout.write('    %s = snl.SNLScalarTerm.create(cell, snl.SNLTerm.Direction.Output, "%s")\n' % (Out,Out))
        if (Inps==[])or(Outs==[]):
            pass
        else:
            Fout.write('    cell.addCombinatorialArcs([%s], [%s])\n' % (', '.join(Inps),', '.join(Outs)))

def workList(Dir):
    Fout = open('second_part','w')
    Fout.write('\n#\n')
    Fout.write('def constructPrimitives(lib):\n')
    List = os.listdir(Dir)
    for Fname in List:
        LL = Fname.split()
        Fout.write('    %s(lib)\n' % LL[0])
    Fout.write('\n\n\n')
    Fout.close()
