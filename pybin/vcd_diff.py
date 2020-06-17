#! /usr/bin/python 
"""
  take two vcd files, find diffs on start/period basis.

"""


import os,sys,string
import logs


class vcd_holder:
    def __init__(self,Fname):
        self.File = open(Fname,'r')
        self.Codes={}
        self.Sigs={}
        self.Values={}
        self.Times={}
        self.SimTime=0
        self.FileClosed=False
        self.Scale=1
        self.read_header()

    def read_header(self):
        ok=1
        self.inLineNum=0
        self.path=[]
        while (ok):
            line = self.File.readline()
            self.inLineNum= self.inLineNum+1
            if (len(line)==0):
                self.FileClosed=True
                return
            wrds=string.split(line)  
            if (len(wrds)>0)and(wrds[0]=='$scope'):
                self.path = self.path + [wrds[2]]
            elif (len(wrds)>0)and(wrds[0]=='$upscope'):
                self.path =self. path[:-1]
            elif (len(wrds)>0)and(wrds[0]=='$var'):
                self.init_var(wrds)
            elif (len(wrds)>0)and(wrds[0]=='$enddefinitions'):
                return

    def init_var(self,wrds):
        Code=wrds[3]
        Bus = wrds[4] 
        if ((wrds[5])[0]=='['):
            Bus = Bus + wrds[5] 
        PathBus = string.join(self.path+[Bus],'.')
        if Code in self.Sigs: return
        self.Codes[PathBus]=Code
        self.Sigs[Code]=PathBus
        self.Values[Code]='x'
        self.Times[Code]= -1


    def advance_till(self,Time):
        while (not self.FileClosed):
            line = self.File.readline()
            self.inLineNum += 1
            if (len(line)==0):
                self.FileClosed=True
                return
            line=line[:-1]
            if (len(line)>1)and(line[0]=='#'):
                numa = line[1:]
                This = 1.0*int(numa)/self.Scale
                self.SimTime=This
                if (This>=Time):
                    return
            elif (len(line)>1)and(line[0]!='$'):
                if (line[0] == 'b'):
                    wrds = string.split(line)
                    Val = (wrds[0])[1:]
                    Code = wrds[1]
                    self.use_value(Val,Code)    
                elif (line[0] == 'r'):
                    wrds = string.split(line)
                    Val = (wrds[0])[1:]
                    Code = wrds[1]
                    self.use_value(Val,Code)    
                else:
                    Val = line[0]
                    Code = line[1:]
                    self.use_value(Val,Code)    
    
    def use_value(self,Val,Code):
        self.Values[Code]=Val
        self.Times[Code]=self.SimTime

def main():
    global Cycle,Vcd1,Vcd2
    if ('-setup' in sys.argv):
        parse_args(sys.argv[1:])
    else:
        Fname1 = sys.argv[1]
        Fname2 = sys.argv[2]
        Vcd1 = vcd_holder(Fname1)
        Vcd2 = vcd_holder(Fname2)
        if (len(sys.argv)>3):
            parse_args(sys.argv[3:])


    if (len(CheckList)==0):
        print 'building checklist'
        build_checklist(Vcd1,Vcd2)




    Time1=Start1
    Time2=Start2
    Cycle=0
    print 'starting diffing on %d signals'%(len(CheckList))
    while (not Vcd1.FileClosed and not Vcd2.FileClosed):
        Cycle+=1
        if ((Cycle%1000)==0):
            print 'cycle ',Cycle
        Vcd1.advance_till(Time1)
        Vcd2.advance_till(Time2)
        compare_values(CheckList,Vcd1,Vcd2,Cycle,Time1,Time2)
        Time1 += Period1
        Time2 += Period2
        if (Cycles>0)and(Cycle>=Cycles):
            return

    LL=[]
    for Key in CHANGES:
        LL.append((CHANGES[Key],Key))
    LL.sort()
    LL.reverse()
    for (Num,Key) in LL:
       logs.log_info('%12d   %s'%(Num,Key))




def build_checklist(Vcd1,Vcd2):
    global CheckList
    Sigs1 = set(Vcd1.Codes.keys())
    Sigs2 = set(Vcd2.Codes.keys())
    CheckList = Sigs1.intersection(Sigs2)
    Fout = open('checklist.mutual','w')
    for Sig in CheckList:
        Code1 = Vcd1.Codes[Sig]
        Code2 = Vcd2.Codes[Sig]
        Fout.write('%s    %s  %s\n'%(Sig,Code1,Code2))
    Fout.close()


LASTS = {}
CHANGES = {}

def compare_values(CheckList,Vcd1,Vcd2,Time,Time1,Time2):
    Dones = 0
    Diffs = []
    for Sig in CheckList:
        Code1 = Vcd1.Codes[Sig]
        V1 = Vcd1.Values[Code1]
        T1 = Vcd1.Times[Code1]
        Code2 = Vcd2.Codes[Sig]
        V2 = Vcd2.Values[Code2]
        T2 = Vcd2.Times[Code2]
        if (V1!=V2):
            Diffs += [(T1,V1,T2,V2,Sig)]
            Dones +=1
    Diffs.sort()
    TT = 0
    for (T1,V1,T2,V2,Sig) in Diffs:
        note_diff('diff',Sig,V1,T1,V2,T2,Time)
        TT = max(TT,max(T1,T2))

    logs.log_info('   <> %d   @%d (%d  %d) %d'%(Time,Dones,Time1/1000,Time2/1000,int(TT/1000)))
    
def note_diff(Which,Sig,V1,T1,V2,T2,Time):
    Indx = compIndex(Sig)
    if Sig not in LASTS:
        LASTS[Sig] = (V1,V2)
        CHANGES[Sig] = 1
        logs.log_info('iii%d cycle=%d   sig=%-50s  v1=%s v2=%s ft1=%.3f   ft2=%.3f '%(Indx,Cycle,Sig,V1,V2,T1,T2))
    else:
        W1,W2 = LASTS[Sig]
        CHANGES[Sig] += 1
        if (W1!=V1)or(W2!=V2):
            logs.log_info('iii%d cycle=%d   sig=%-50s  v1=%s v2=%s ft1=%.3f   ft2=%.3f '%(Indx,Cycle,Sig,V1,V2,T1,T2))
            LASTS[Sig] = (V1,V2)

def compIndex(Sig):
   return Sig.count('.')




def parse_args(List):
    global Start1,Period1,CheckList,NoCheckList
    global Start2,Period2
    global Cycles
    Start1=0
    Start2=0
    Period1=1
    Period2=1
    Cycles=-1
    CheckList=[]
    NoCheckList=[]
    if ('-setup' in List):
        X = List.index('-setup')
        Fname = (List[X+1])
        Fil = open(Fname)
        readin_setup(Fil)
    if ('-start' in List):
        X = List.index('-start')
        Start1 = int(List[X+1])
        Start2 = int(List[X+1])
    if ('-period' in List):
        X = List.index('-period')
        Period1 = int(List[X+1])
        Period2 = int(List[X+1])
    if ('-scale' in List):
        X = List.index('-scale')
        Vcd1.Scale = int(List[X+1])
        Vcd2.Scale = int(List[X+1])
    if ('-cycles' in List):
        X = List.index('-cycles')
        Cycles = int(List[X+1])
    if ('-check' in List):
        X = List.index('-check')
        Fname = (List[X+1])
        Fil = open(Fname)
        readin_checklist(Fil)
    if ('-nocheck' in List):
        X = List.index('-nocheck')
        Fname = (List[X+1])
        Fil = open(Fname)
        readin_nochecklist(Fil)

        

def readin_nochecklist(Fil):
    global CheckList,NoCheckList
    while 1:
        line= Fil.readline()
        if (len(line)==0):
            return
        wrds = string.split(line)
        if (len(wrds)>0):
            NoCheckList += [wrds[0]]
        
    for Sig in NoCheckList:
        if Sig in CheckList:
            Ind = CheckList.index(Sig)
            CheckList.pop(Ind)



def readin_checklist(Fil):
    global CheckList
    while 1:
        line= Fil.readline()
        if (len(line)==0):
            return
        wrds = string.split(line)
        if (len(wrds)>0):
            CheckList += [wrds[0]]
        
    for Sig in CheckList:
        if Sig in NoCheckList:
            Ind = CheckList.index(Sig)
            CheckList.pop(Ind)
        
def readin_setup(Fil):
    global Start1,Start2,Period1,Period2
    global Cycles
    global Vcd1,Vcd2
    while 1:
        line= Fil.readline()
        if (len(line)==0):
            return
        if (line[0]!='#'):
            wrds = string.split(line)
            if (len(wrds)>=2):
                Key = wrds[0]
                Val = intx(wrds[1])
                print 'reading setup %s'%(string.join(wrds,' '))
                if (Key == 'start1'):
                    Start1 = Val
                elif (Key == 'start2'):
                    Start2 = Val
                elif (Key == 'period1'):
                    Period1 = Val
                elif (Key == 'period2'):
                    Period2 = Val
                elif (Key == 'scale1'):
                    Vcd1.Scale = Val
                elif (Key == 'scale2'):
                    Vcd2.Scale = Val
                elif (Key == 'scale'):
                    Vcd1.Scale = Val
                    Vcd2.Scale = Val
                elif (Key == 'cycles'):
                    Cycles = Val
                elif (Key == 'check'):
                    Fil = open(wrds[1])
                    readin_checklist(Fil)
                elif (Key == 'nocheck'):
                    Fil = open(wrds[1])
                    readin_nochecklist(Fil)
                elif (Key == 'vcd1'):
                    Vcd1 = vcd_holder(wrds[1])
                elif (Key == 'vcd2'):
                    Vcd2 = vcd_holder(wrds[1])
                else:
                    print 'bad keyword line',line


def intx(In):
    for Ch in In:
        if (Ch not in '0123456789'):
            return 0
    return int(In)



main()





