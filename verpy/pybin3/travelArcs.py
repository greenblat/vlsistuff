#! /usr/bin/env python3
import os,sys
import importlib
sys.path.append('/Users/iliagreenblat/verification_libs3')
import logs
Modules = {}
Instances = {}
MISSINGS = {}
def main():
    logs.setVar('longest',0)
    Fname = sys.argv[1]
    Way = Fname.split('/')
    Path = '/'.join(Way[:-1])
    sys.path.append(Path)
    Top = Way[-1][:-3]
    Topo = importlib.import_module(Top)
    Modules[Top] = Topo.hld
    loadDeep([Top],[Top])
    createMissings()
    Instances[Top] = Top
    instancesDeep([Top],[Top])
    createConnTables()
    scanDeep(Top,[Top])


class holderClass:
    def __init__(self,Name):
        self.Name = Name
        self.ARCSBK = {}
        self.ARCSFW = {}
        self.CONNS = []
        self.TERMS = []
        self.INPUTS = []
        self.OUTPUTS = []
        self.SONS = []



def createMissings():
    for Mod in MISSINGS:
        Father = MISSINGS[Mod]
        Hld = holderClass(Mod)
        Fth = Modules[Father]
        Inst1 = False
        for Inst0,Type0 in Fth.SONS:
            if Type0 == Mod:
                Inst1 = Inst0
        if not Inst1:
            logs.log_error('createMissings failed on %s %s' % (Mod,Father))
        else:
            Modules[Mod] = Hld
            Hld.TERMS.append('dummy')
            Hld.ARCSFW['dummy'] = []
            for Inst,Pin,Sig in Fth.CONNS:
                if (Inst == Inst1):
                    if Sig in Fth.OUTPUTS:
                        Hld.OUTPUTS.append(Pin)
                        Hld.ARCSFW['dummy'].append(Pin)
                    elif Sig in Fth.INPUTS:
                        Hld.INPUTS.append(Pin)
                    elif Sig in Fth.TERMS:
                        Hld.INPUTS.append(Pin)
                    elif Sig in Fth.ARCSBK:
                        Hld.INPUTS.append(Pin)
                    elif Sig in Fth.ARCSFW:
                        Hld.OUTPUTS.append(Pin)
                        Hld.ARCSFW['dummy'].append(Pin)
                    else:
                        Hld.OUTPUTS.append(Pin)
                        Hld.ARCSFW['dummy'].append(Pin)
            logs.log_info('INVENTED MISSIGS %s outs=%s ins=%s ' % (Mod,Hld.OUTPUTS,Hld.INPUTS))            
            


def instancesDeep(Mods,Path):
    for  Mod in Mods:
        if Mod in Modules:
            Hld = Modules[Mod]
            for Inst,Type in Hld.SONS:
                Instances['.'.join(Path + [Inst])] = Type
                instancesDeep([Type],Path + [Inst])






def scanDeep(Mod,Path):
    Hld = Modules[Mod]
    for Term in Hld.TERMS:
        travelFW(Term,Mod,Path,[ Path+[Term]])
    if len(Path)==1:
        for Term in Hld.INPUTS:
            travelFW(Term,Mod,Path,[ Path+[Term]])
        
    for Inst,Type in Hld.SONS:
        if Type in Modules:
            scanDeep(Type,Path+[Inst])

def printPath(Kind,Mod,Path):
    Lng = logs.getVar('longest')
    if len(Path) > Lng:
        logs.setVar('longest',len(Path))
    Pr = '%s %s %d / %d :    %s -> %s \n' % (Kind,Mod,len(Path),Lng,'.'.join(Path[0]),'.'.join(Path[-1]))
    for PP in Path:
        X = '.'.join(PP)
        Pr += '    %s\n' % X
    logs.log_info(Pr)

def ppPath(Path):
    return '.'.join(Path)


DONES = {}

def travelFW(Net,Mod,instPath,netPath):
    Src = ppPath(netPath[0])
    Len = len(netPath)
    Here = ppPath(instPath + [Net])
    if ((Here,Src) in DONES)and(DONES[(Here,Src)]>=Len):
        return
#    logs.log_info('TTT here=%s  %s %s %s %s' % (Here,Src,Mod,Len,Net),4)

    DONES[(Here,Src)] = Len
    if Mod not in Modules:
        printPath('PATH0',Mod,netPath+[instPath+[Net]])
        return

    Hld = Modules[Mod]
    for Inst,Pin,Sig in Hld.CONNS:
        if (Sig == Net):
            for Instx,Typex in Hld.SONS:
                if Instx == Inst:
                    Sth = Modules[Typex]
                    print("X23",Instx,Typex,Pin,Pin in Sth.INPUTS)
                    if Pin in Sth.INPUTS:
                        dinstPath =  instPath + [Inst] 
                        Key = '.'.join(dinstPath)
                        Type = Instances[Key]
                        travelFW(Pin,Type,dinstPath,netPath + [ dinstPath + [Pin]])
            
        

    if Net not in  Modules[Mod].ARCSFW:
        printPath('PATH1',Mod,netPath+[instPath+[Net]])
        return


    Arcs = Hld.ARCSFW[Net]
    for End in Arcs:
        if End in Hld.TERMS:
            printPath('PATH2',Mod,netPath+[instPath+[End]])
        if (End in Hld.OUTPUTS) and (len(instPath)==1):
            printPath('PATH3',Mod,netPath+[instPath+[End]])
        elif (End in Hld.OUTPUTS) and (len(instPath)>1):
            upInst = instPath[:-1] 
            Type = Instances['.'.join(upInst)]
            Father = Modules[Type]
            upNetPath = netPath+[instPath + [End]]
            upHld = Modules[Type]
            Keyx = (instPath[-1],End)
            if End in Hld.TERMS:
                pass
            elif Keyx in upHld.instPinTable:
                upSig = upHld.instPinTable[Keyx]
                if upSig == 'rst_nn':
                    print('RST_NN',upSig,Type,instPath[:-1],upNetPath)
                travelFW(upSig,Type,instPath[:-1],upNetPath)
        if End in Hld.netTable:
            for (Inst,Pin) in Hld.netTable[End]:
                dinstPath =  instPath + [Inst] 
                Key = '.'.join(dinstPath)
                Type = Instances[Key]
                travelFW(Pin,Type,dinstPath,netPath + [ dinstPath + [Pin]])

        if (End not in Modules[Mod].TERMS) and (End in Modules[Mod].ARCSFW):
            travelFW(End,Mod,instPath,netPath+ [ instPath + [End]])

def loadDeep(Works,Sofar):
    Deeper = []
    for Mod in Works:
        Sons = Modules[Mod].SONS
        for _,Son in Sons:
            if Son not in Sofar:
                Sofar.append(Son)
                try:
                    Topo = importlib.import_module(Son)
                    Modules[Son] = Topo.hld
                    Deeper.append(Son)
                except:
                    logs.log_warning('missing %s' % Son)
                    MISSINGS[Son] = Mod
                
    if Deeper!=[]: loadDeep(Deeper,Sofar)

def createConnTables():
    for Mod in Modules:
        Hld = Modules[Mod]
        Hld.netTable = {}
        Hld.instPinTable = {}
        for Inst,Pin,Sig in Hld.CONNS:
            if Sig not in Hld.netTable: Hld.netTable[Sig] = []
            Hld.netTable[Sig].append((Inst,Pin))
            Hld.instPinTable[(Inst,Pin)] = Sig

if __name__ == '__main__': main()
