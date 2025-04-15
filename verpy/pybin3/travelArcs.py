#! /usr/bin/env python3
import os,sys
import importlib
sys.path.append('/Users/iliagreenblat/verification_libs3')
import logs
Modules = {}
Instances = {}
MISSINGS = {}
CLOCKED = {}
def main():
    logs.setVar('longest',0)
    Fname = sys.argv[1]
    Way = Fname.split('/')
    Path = '/'.join(Way[:-1])
    sys.path.append(Path)
    Top = Way[-1][:-3]
    Topo = importlib.import_module(Top)
    Modules[Top] = Topo.hld
#    print("DIRDIR",Top,dir(Topo.hld))
    loadDeep([Top],[Top])
    logs.log_info("LOADED %s" % list(Modules.keys()))
    createMissings()
    Instances[Top] = Top
    instancesDeep([Top],[Top])
    createConnTables()
    scanDeep(Top,[Top])
    PATHS.sort()
    PATHS.reverse()
    Frep = open('%s.longarcs.report' % Top,'w')
    for (Len,Path) in PATHS:
        Frep.write(Path + '\n')
    Frep.close()

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
        self.DRIVEN = {}



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
            Hld.CLOCKED = {}
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
    for Term in Hld.STARTS:
        if Term in Hld.CLOCKED:
            Clk = Hld.CLOCKED[Term]
            CLOCKED['.'.join(Path+[Term])] = Clk

        travelFW(Term,Mod,Path,[ Path+[Term+ str(Hld.STARTS[Term])]])
    if len(Path)==1:
        for Term in Hld.INPUTS:
            travelFW(Term,Mod,Path,[ Path+[Term]])
        
    for Inst,Type in Hld.SONS:
        if Type in Modules:
            scanDeep(Type,Path+[Inst])
PATHS = []
def printPath(Kind,Mod,Path):
    Lng = logs.getVar('longest')
    if len(Path) > Lng:
        logs.setVar('longest',len(Path))
    Start = '.'.join(Path[0])
    End   = '.'.join(Path[-1])
    if Start == End: return
    StartClk = 'N'
    EndClk = 'N'
    if Start in CLOCKED: StartClk = CLOCKED[Start]
    if End in CLOCKED: EndClk = CLOCKED[End]
    Pr = '%s %s %d / %d :   (%s)  %s ->  (%s) %s \n' % (Kind,Mod,len(Path),Lng,StartClk,'.'.join(Path[0]),EndClk,'.'.join(Path[-1]))
    for PP in Path:
        X = '.'.join(PP)
        Add = ''
        if len(PP)==2:
            Sig = PP[1]
            Where = PP[0]
            if Where in Modules:
                if Sig in Modules[Where].DRIVEN:
                    Add = Modules[Where].DRIVEN[Sig]

        if len(PP)>=3:
            Sig = PP[-1]
            Where = PP[-3]
            if Where in Modules:
                print("Where ",Where,Sig, Sig in Modules[Where].DRIVEN)
                if Sig in Modules[Where].DRIVEN:
                    Add = Modules[Where].DRIVEN[Sig]
#            print("XXXX",Sig,Where, Sig in Modules[Where].DRIVEN)
        Pr += '    %s   %s\n' % (X,Add)
    logs.log_info(Pr)
    PATHS.append( (len(Path),Pr))

def ppPath(Path):
    return '.'.join(Path)


DONES = {}

def travelFW(Net,Mod,instPath,netPath):
    Src = ppPath(netPath[0])
    Len = len(netPath)
    Here = ppPath(instPath + [Net])
    if ((Here,Src) in DONES)and(DONES[(Here,Src)]>=Len):
        return
    if Net == 'finishing':
        logs.log_info('TTT here=%s  %s %s %s %s' % (Here,Src,Mod,Len,Net),4)

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
                    if Pin in Sth.INPUTS:
                        dinstPath =  instPath + [Inst] 
                        Key = '.'.join(dinstPath)
                        Type = Instances[Key]
                        travelFW(Pin,Type,dinstPath,netPath + [ dinstPath + [Pin]])
            
        

    if Net not in  Modules[Mod].ARCSFW:
        if (Net in Hld.OUTPUTS) and (len(instPath)>1):
            upInst = instPath[:-1] 
            Type = Instances['.'.join(upInst)]
            Father = Modules[Type]
            upNetPath = netPath+[instPath + [Net]]
            upHld = Modules[Type]
            Keyx = (instPath[-1],Net)
            if Net in Hld.TERMS:
                pass
            if Keyx in upHld.instPinTable:
                upSig = upHld.instPinTable[Keyx]
                if upSig == 'rst_nn':
                    print('RST_NN',upSig,Type,instPath[:-1],upNetPath)
                travelFW(upSig,Type,instPath[:-1],upNetPath)
        elif Net in Hld.TERMS:
            printPath('PATHT',Mod,netPath+[instPath+[Net]])
        else:
            printPath('PATH1',Mod,netPath+[instPath+[Net]])
        return


    Arcs = Hld.ARCSFW[Net]
    for End in Arcs:
        if End in Hld.TERMS:
            printPath('PATH2',Mod,netPath+[instPath+[End+str(Hld.DRIVEN[End])]]+[instPath+[End+str(Hld.TERMS[End])]])
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
                    Topo = importlib.import_module(Son)
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
