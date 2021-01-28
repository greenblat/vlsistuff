#! /usr/bin/env python3
import os,sys,string
sys.path.append('/Users/ilia/verification_libs3')
import logs

def main():
    Fname = sys.argv[1]
    Path = os.path.abspath(sys.argv[0])
    Path = Path.split('/')
    Path = '/'.join(Path[:-1])
    os.system('%s/pylexer.py %s'%(Path,Fname))
    readLexFile('lex.out')
    logs.setVar('state','idle')
    scanLexLines()
    Module = logs.getVar('module')
    Fout = open('%s.regfile'%Module,'w')
    Fout.write('// translated from rdl file %s\n'%Fname)
    Fout.write('chip %s bus=apb wid=32 addrwid=16 empty=0xdeadbeef reset=async\n'%Module)
    for Reg,Obj in DB:
        if Obj.build():
            if Obj.Repeat==1:
                Obj.report(Fout,'')
            else:
                for XX in range(Obj.Repeat):
                    Obj.report(Fout,'_%s'%XX)
    Fout.write('end\n')
    Fout.close()

LINES = []
def readLexFile(Fname):
    File = open(Fname)
    while 1:
        line = File.readline()
        if line=='': return
        wrds = line.split()
        A = ' '.join(wrds[:-3])
        B = wrds[-3]
        C = wrds[-2]
        D = wrds[-1]
        LINES.append((A,B,C,D))

def scanLexLines():
    ind = 0
    while ind < len(LINES):
        next = stateMach(ind,LINES[ind])
        ind = next

def stateMach(ind,Line):
    state = logs.getVar('state')
    if (state=='idle'):
        if (Line[0]=='addrmap')and(LINES[ind+1][1]=='token')and(LINES[ind+2][1]=='{'):
            logs.setVar('module',LINES[ind+1][0])
            logs.setVar('state','work0')
            return ind+3
        return ind+1
    elif (state=='work0'):
        if Line[0]=='name':
            return skipTo(ind,';')
        elif Line[0] == 'reg':
            next,REGLIST = getReg(ind)
            treatReg(REGLIST)
            return next
        elif Line[0] == '}':
            finalize()
            return len(LINES)
        elif Line[0] == 'eol':
            return ind+1
        else:
            print('error0',Line)
            return ind+1
    else:
        print('error1',state,Line)
        return ind+1



def skipTo(ind,Who):
    while True:
        Line = LINES[ind]
        if Line[0]== Who:
            return ind+1
        ind += 1

def getReg(ind):
    ind += 1
    Start = ind
    Depth = 0
    while True:
        Line = LINES[ind]
        if Line[0]=='{': Depth += 1
        elif Line[0]=='}': Depth -= 1
        elif (Line[0]==';')and(Depth==0):
            LL = LINES[Start:ind]
            REG = []
            for X in LL:
                if X[0]!='eol':
                    REG.append(X)
            return ind+1,REG
            
        ind += 1 
DB = []
def treatReg(REGLIST):
    Name = REGLIST[0][0]
    if REGLIST[-2][0] == '}':
        Name2 = REGLIST[-1][0]
        REG2 = REGLIST[2:-2]
        Repeat =1
    elif REGLIST[-5][0] == '}':
        Name2 = REGLIST[-4][0]
        Repeat = eval(REGLIST[-2][0])
        REG2 = REGLIST[2:-5]
    Fields = treatFields(REG2[:])
    Desc = logs.getVar('description')
    logs.setVar('description',False)
    Obj = regClass(Name,Name2,Repeat)
    if Desc:
        Obj.description = Desc
    DB.append((Name,Obj))
    
    for FF in Fields:
        Fh = headers(FF)
        if Fh!=[]:
            Fname,Access,Wid,Reset,Desc = parseField(Fh)
            Obj.fields.append((Fname,Access,Wid,Reset,Desc))

def combineRsts(Rst,Str):
    ww = Str.split("'b")
    if len(ww)==2:
        Wid = eval(ww[0])
        Val = int(ww[1],2)
        Rst = (Rst<<Wid)|Val
        return Rst
    else:
        print('reset value not dealt with "%s"'%(Str))
        return Rst


fieldsKeeper = {}

class regClass:
    def __init__(self,Name,Name2,Repeat):
        self.Name = Name
        self.Name2 = Name2
        self.Repeat = int(Repeat)
        self.Reset = 'none'
        self.fields = []
        self.Wid = 0
        self.Access='none'
        self.Reset='none'
        self.description=False


    def build(self):
        if self.fields==[]: 
            print('Ilia STRANGE %s'%self.Name)
            return False
        Last =  self.fields[-1]
        if Last[0].startswith('reserved')and(Last[1]=='ro'):
            self.fields.pop(-1)
        Rsts = 0
        for Fi in self.fields:
            self.Wid += Fi[2]
            Rsts = combineRsts(Rsts,Fi[3])
#            Rsts.append(Fi[3])
            if Fi[1] == 'rw': self.Access='rw'
            elif Fi[1] == 'rw_pulse': self.Access='rw_pulse'
            elif (Fi[1]=='ro'):
                if self.Access=='ro': 
                    pass
                elif self.Access=='none': 
                    self.Access='ro'
                elif Fi[0].startswith('reserved'):
                    pass
                else:
                    print('Ilia access error %s'%(self.Name))
            else: 
                print('Ilia access error %s'%(self.Name))
        if len(self.fields)==1: self.fields=[]
        self.Reset = Rsts
        return True


    def report(self,Fout,Who):
        if self.Name.startswith('reserved'): return
        Desc = ' ' 
        if self.description:
            Desc = 'description="%s"'%self.description
            Desc = Desc.replace('""','"')
            Desc = Desc.replace(' ','.')

        Fout.write('reg %s%s access=%s wid=%d reset=%s %s\n'%(self.Name,Who,self.Access,self.Wid,hex(self.Reset),Desc))
        for Fi in self.fields:
            Fname = Fi[0]
            if Fi[4]:
                Desc = 'description="%s"'%(Fi[4])
                Desc = Desc.replace('""','"')
                Desc = Desc.replace(' ','.')
            else:
                Desc = ' '
            Rst = combineRsts(0,Fi[3])
            if Rst==0:
                Rst = ''
            else:
                Rst = 'reset=0x%x'%Rst
            Access=Fi[1]
            if Fname.startswith('reserved'):
                Access='gap'
            
            Fout.write('field %s access=%s wid=%d %s %s\n'%(Fname,Access,Fi[2],Rst,Desc))
            if (Fname in fieldsKeeper)and(Access!='gap'):
                print('ERROR! double field name %s  in reg %s'%(Fname,self.Name))
            else:
                fieldsKeeper[Fname] = True



def parseField(List):
    Access='none'
    if appears('sw = rw',List): Access='rw'
    if appears('sw = w',List): Access='rw_pulse'
    if appears('sw = r',List): Access='ro'
    if appears('name =',List):
        Ind = List.index('name')+2
        Desc = List[Ind]
    else:
        Desc=False
    Ex = List.index('}')
    Name = List[Ex+1]
    Wid = eval(List[Ex+3])
    Reset = 'none'
    if List[Ex+5]=='=':
        Reset = List[Ex+6]

    if Access=='none':
        print('ACCESS',List)
    return Name,Access,Wid,Reset,Desc

def appears(Str,List):
    WW = Str.split()
    if WW[0] not in List: return False
    St = List.index(WW[0])
    while St < (len(List)-len(WW)):
        Ok = True
        for ii,X in enumerate(WW):
            if X != List[St+ii]: Ok=False
        if Ok: return True
        St += 1
    return False

def headers(FF):
    Fh = []
    for X in FF:
        Fh.append(X[0])
    return Fh

def treatFields(REG):
    if REG==[]: return []
    if REG[0][0]=='field':
        ind,Field = getField(REG)
        REG1 = REG[ind:]
        More = treatFields(REG1)
        if More==[]: return [Field]
        return [Field]+More
    elif REG[0][0]=='name':
        logs.setVar('description',REG[2][0])
        More = treatFields(REG[4:])
        return More
    else:
        print('WTF %s'%REG[0])
    return []


def getField(REG):
    ind =0
    Depth = 0
    while True:
        Line = REG[ind]
        if Line[0]=='{': Depth += 1
        elif Line[0]=='}': Depth -= 1
        elif (Line[0]==';')and(Depth==0):
            LL = REG[:ind]
            Field = []
            for X in LL:
                if X[0]!='eol':
                    Field.append(X)
            return ind+1,Field
        ind += 1 


def finalize():
    print('final')

if __name__ == '__main__': main()
