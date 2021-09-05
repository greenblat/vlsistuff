
'''
explore and print path from point to point , 
traversing hierarchies.

state: delicate but works.
missing, need to do: generate

'''


import logs
from executes import try_and_load_module
from module_class import support_set

FORWARD = {}
BACKWARD = {}
def help_main(Env):
    Mod = Env.Current
    bringAll(Mod,Env)

    buildTable(Mod,'',Env)
    createOutputs(Mod)
    createStartsAndEnds(Mod)
    for St in STARTS:
        travelDeep(St,[St])
    reports()

STARTS = {}
ENDS = {}
OUTPUTS = {}
INPUTS = {}

def createOutputs(Mod):
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if 'output' in Dir:
            OUTPUTS[Net] = True
        if 'input' in Dir:
            INPUTS[Net] = True

def createStartsAndEnds(Mod):
    for Sig in FORWARD:
        if Sig not in BACKWARD:
            STARTS[Sig] = True

    for Sig in BACKWARD:
        if Sig not in FORWARD:
            ENDS[Sig] = True







def travelDeep(St,Sofar):
    List =  FORWARD[St]
    for Mid in List:
        if Mid in OUTPUTS:
            reportPath(Sofar+[Mid],'OUTPUT')

        if (Mid in ENDS) and (Mid not in OUTPUTS):
            reportPath(Sofar+[Mid],'ENDS  ')

        if (Mid not in FORWARD):
            if (Mid not in ENDS):
                reportPath(Sofar+[Mid],'STUCK ')
        else:            
            travelDeep(Mid,Sofar+[Mid])


def reportPath(Path,Why):
    logs.log_info('PATH %s   %s -> %s (%d)' % (Why,Path[0],Path[-1],len(Path)),3)

    if (Path[0] in INPUTS) and (Path[-1] in OUTPUTS):
        logs.log_info('PATH %s   %s -> %s (%d)' % (Why,Path[0],Path[-1],len(Path)),5)
        for ind,Sig in enumerate(Path):
            logs.log_info('    %3d  %s' % (ind,Sig),5)
            
            




def reports():
    for Key in FORWARD:
        logs.log_info('FORWARD %s %s' % (Key,FORWARD[Key]),2)
    for Key in BACKWARD:
        logs.log_info('BACKWARD %s %s' % (Key,BACKWARD[Key]),2)


def buildTable(Mod,Path,Env):
    for Dst,Src,_,_ in Mod.hard_assigns:
        Dsts = support_set(Dst,False)
        Srcs = support_set(Src,False)
        for S in Srcs:
            for D in Dsts:
                recordTable(Path+'.'+S,Path+'.'+D)
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        Son = Env.Modules[Type]
        for Pin in Obj.conns:
            Nets = support_set(Obj.conns[Pin],False)
            Dir,_ = Son.nets[Pin]
            if 'output' in Dir:
                for Net in Nets:
                    recordTable(Path+'.'+Inst+'.'+Pin,Path+'.'+Net)
            elif 'input' in Dir:
                for Net in Nets:
                    recordTable(Path+'.'+Net,Path+'.'+Inst+'.'+Pin)
            else:
                logs.log_error('strange dir %s of %s in %s' % (Dir,Pin,Type))
                
    for When,Body,_  in Mod.alwayses:
        if combiAlways(When):
            scanBody(Body,[],Path)

    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        Son = Env.Modules[Type]
        buildTable(Son,Path+'.'+Inst,Env)
    



def combiAlways(When):
    if When == '*': return True
    if When[0] == 'edge': return False
    if When[0] == 'list':
        return combiAlways(When[1])
    logs.log_error('combiAlways failed on "%s"' % str(When))
    return False

def scanBody(Body,Conds,Path):
    if (type(Body) is tuple) or (type(Body) is list):
        if Body[0] in ['=','<=']:
            Dsts = support_set(Body[1],False)
            Srcs = support_set(Body[2],False)
            for S in Srcs+Conds:
                for D in Dsts:
                    recordTable(Path+'.'+S,Path+'.'+D)
            return 
        if Body[0] == 'list':
            for Item in Body[1:]:
                scanBody(Item,Conds,Path)
            return
        if Body[0] == 'ifelse':
            More = support_set(Body[1],False)
            scanBody(Body[2],Conds+More,Path)
            scanBody(Body[3],Conds+More,Path)
            return
        if Body[0] == 'if':
            More = support_set(Body[1],False)
            scanBody(Body[2],Conds+More,Path)
            return
        if Body[0] == 'case':
            More = support_set(Body[1],False)
            for Label,Item in Body[2]:
                scanBody(Item,Conds+More,Path)
            return
                


    logs.log_error('scanBody failed on %s' % str(Body[0]))            
    return        
        



        
def recordTable(S,D):
    if S[0] == '.': S = S[1:]
    if D[0] == '.': D = D[1:]
    if S in FORWARD:
        if D not in FORWARD[S]:
            FORWARD[S].append(D)
    else:
        FORWARD[S] = [D]
    if D in BACKWARD:
        if S not in BACKWARD[D]:
            BACKWARD[D].append(S)
    else:
        BACKWARD[D] = [S]

def bringAll(Mod,Env):
    for Inst in Mod.insts:
        Type = Mod.insts[Inst].Type
        try_and_load_module(Type,Env)
        if Type in Env.Modules:
            Son = Env.Modules[Type]
            bringAll(Son,Env)
