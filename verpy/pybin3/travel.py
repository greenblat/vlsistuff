#! /usr/bin/env python3.9
import os,sys,string


import importlib
sys.path.append('/Users/ilia/verification_libs3')
import logs
HLDS = {}
LOGS = []
def main():
    loadup()
    buildHierarchy()
    for Mod in HLDS:
        Hld = HLDS[Mod]
        for Reg in Hld.TERMS:
            travel(Hld,Reg,[(Hld.Name,Reg)])

    LOGS.sort()
    LOGS.reverse()
    for _,Path in LOGS:
        logs.log_info(Path)



def travel(Hld,Net,Sofar):
#    logs.log_info('%s %s    %s'%(Hld.Name,Net,Sofar))
    if len(Sofar)>1:
        Head = Sofar[0] 
        if Head in Sofar[1:]:
            report('LOOP',Hld.Name,Net,Sofar)
            return

    if (Net in Hld.TERMS)and(len(Sofar)>1):
        report('TOTERM',Hld.Name,Net,Sofar)
        return

    if Net in  Hld.ARCSFW:
        Fws = Hld.ARCSFW[Net]
        print('FWS',Net,Fws)
        for Fw in Fws:
            travel(Hld,Fw,[('fw',Hld.Name,Fw)]+Sofar)
    if Net in Hld.OUTPUTS:
        if Hld.Name in CALLED:
            Fathers = CALLED[Hld.Name]
            for (Father,Son) in Fathers:
                Up = HLDS[Father]
                for (S0,P0,Sig) in Up.CONNS:
                    if (S0 == Son)and(P0==Net):
                        travel(Up,Sig,[('up',Father,Sig)]+Sofar)
        else: 
            report('TOOUT',Hld.Name,Net,Sofar)
#            logs.log_info('TOOUT %s.%s  %s\n\n\n'%(Hld.Name,Net,Sofar))


    for Inst,Pin,Sig in Hld.CONNS:
        if Sig==Net:
            for Inst2,Type in Hld.SONS:
                if Inst2==Inst:
                    if Type not in HLDS:
                        logs.log_warning('%s is not read'%Type)
                    else:
                        Son = HLDS[Type]
                        if Pin in Son.INPUTS:
                            travel(Son,Pin,[('down',Son.Name,Pin,Hld.Name,Sig)]+Sofar)


CALLED = {}
def buildHierarchy():
    for Mod in  HLDS:
        Hld = HLDS[Mod]
        for (Inst,Type) in Hld.SONS:
            if Type not in CALLED: 
                CALLED[Type] = []
            CALLED[Type].append((Mod,Inst))
            


def loadup():
    List = os.listdir('arcs')
    sys.path.append('arcs')
    for Fname in List:
        if '.py' in Fname:
            X = importlib.import_module(Fname[:-3])
            Name = X.hld.Name
            HLDS[Name] = X.hld

def report(Dir,Mod,Net,Path):
    LL = list(map(str,Path))
    Str = '\n    '.join(LL)
    Res = '%s len=%d     %s.%s <- %s  \n    %s\n\n\n'%(Dir,len(Path),Mod,Net,Path[-1],Str)
    LOGS.append((len(Path),Res))


if __name__ == '__main__': main()
