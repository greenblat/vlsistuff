#! /usr/bin/python
import os,sys,string

Db = []
Labels = {}
Ranges = {}
Assigns = {}
def main():
    Fname = sys.argv[1]
    Main = sys.argv[2]
    File = open(Fname)

    W1 = string.split(Fname,'/')
    W2 = string.split(W1[-1],'.')
    Cell = W2[0]

    lines = File.readlines()
    for line in lines:
        Obj = linesClass(line)
        Db.append(Obj)

    for ind,Obj in enumerate(Db):
        if Obj.Kind=='label': 
            Lbl = Obj.wrds[-1]
            Labels[Lbl]  = ind
    Fregs = string.split('F1 F2 F3 F4 F5 F6 F7')
    Xregs = string.split('X1 X2 X3 X4 X5 X6 X7')
    travel(Labels[Main],Fregs,Xregs)

    useAssigns(Cell)
#    reports()



def useAssigns(Cell):
    for Obj in Db:
        wrds1 = []
        Obj.wrds1 = Obj.wrds[:]
        for ind,wrd in enumerate(Obj.wrds1):
            if wrd in Assigns:
                Obj.wrds1[ind] = Assigns[wrd]
                
    Fout = open('%s.app'%Cell,'w')
    for Obj in Db:
        Line = string.join(Obj.wrds1,' ')
        Fout.write('    %s ;\n'%Line)
    Fout.close()


def reports():
    for Ind,Obj in enumerate(Db):
        print('db',Ind,Obj.Kind,Obj.wrds,Obj.Dest,Obj.Srcs)
    Keys = Ranges.keys()
    Keys.sort()
    for Key in Keys:
        print(Key,Ranges[Key])

    for Key in Assigns:
        print('assigns',Key,Assigns[Key])


def travel(Ind,Fregs,Xregs):
    if Ind >= len(Db): 
        print('ERROR! overflow len=%d'%(Ind))
        return
    Obj = Db[Ind]
    if Obj.Kind=='sleep': 
        return

    if Obj.Kind=='var': 
        print('ERROR! %s %s'%(Obj.Kind,Obj.wrds))
        travel(Ind+1)
        retur
    
    if Obj.Kind == 'goto':
        Down = Labels[Obj.wrds[-1]]
        travel(Dow,Fregs,Xregs)
        return

    if Obj.Kind == 'if':
        Down = Labels[Obj.wrds[-1]]
        for Src in Obj.Srcs:
            Ranges[Src].append(Ind)
            Reg = Assigns[Src]
            if 'FV' in Src:
                if (Reg not in Fregs):
                    Fregs.append(Reg)
            elif 'XV' in Src:
                if (Reg not in Xregs):
                    Xregs.append(Reg)
        Xregs1 = Xregs[:]
        Fregs1 = Fregs[:]
        travel(Down,Fregs,Xregs)
        travel(Ind+1,Fregs1,Xregs1)
        return

    if Obj.Kind == 'label':
        travel(Ind+1,Fregs,Xregs)
        return

    if Obj.Kind == 'op':
        if Obj.Dest!='':
            if Obj.Dest not in Ranges:
                Ranges[Obj.Dest] = [Ind]
            if 'FV' in Obj.Dest:
                Assigns[Obj.Dest] = Fregs.pop(0)
            elif 'XV' in Obj.Dest:
                Assigns[Obj.Dest] = Xregs.pop(0)

        if Obj.Srcs!=[]:
            for Src in Obj.Srcs:
                Ranges[Src].append(Ind)
                Reg = Assigns[Src]
                if 'FV' in Src:
                    if (Reg not in Fregs):
                        Fregs.append(Reg)
                elif 'XV' in Src:
                    if (Reg not in Xregs):
                        Xregs.append(Reg)
        
        travel(Ind+1,Fregs,Xregs)
        return

    print('noKind',Obj.Kind,Obj.wrds)

class linesClass:
    def __init__(self,Line):
        self.Line = Line
        self.Srcs = []
        self.Dest = ''
        self.Kind = False
        wrds = string.split(Line)
        self.wrds = wrds
        if len(wrds)==0:
            pass
        elif wrds[0] in ['float','int']: 
            self.Kind = 'var'
        elif wrds[0] in ['label']: 
            self.Kind = 'label'
        elif wrds[0] in ['goto']: 
            self.Kind = 'goto'
        elif wrds[0] in ['if']: 
            self.gather(wrds)
            self.Kind = 'if'
        elif wrds[0] in ['sleep()']: 
            self.Kind = 'sleep'
        else:
            self.Kind = 'op'
            self.gather(wrds)
#            print('use ',self.Kind,self.Dest,self.Srcs,Line)

    def gather(self,wrds):
        if isXreg(wrds[0]):
            self.Dest = wrds[0]
        elif isFreg(wrds[0]):
            self.Dest = wrds[0]
        for Wrd in wrds[1:]:
            if isXreg(Wrd): 
                self.Srcs.append(Wrd)
            elif isFreg(Wrd): 
                self.Srcs.append(Wrd)



def isXreg(Txt):
    if Txt[0]!='X': return False
    if len(Txt)<3: return False
    if Txt[1]!='V': return False
    for Chr in Txt[2:]:
        if Chr not in '0123456789': return False
    return True

def isFreg(Txt):
    if Txt[0]!='F': return False
    if len(Txt)<3: return False
    if Txt[1]!='V': return False
    for Chr in Txt[2:]:
        if Chr not in '0123456789': return False
    return True





if __name__ == '__main__': main()


