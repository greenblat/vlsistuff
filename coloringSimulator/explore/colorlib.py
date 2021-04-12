


import veri
import logs
import sys
print(sys.path)
import ctypes

import random

CODES = [0]
def newNet(Father,Pin,Inst):
    Net = netClass(Father,Pin,Inst)
    Net.Code = len(CODES)
    Id = id(Net)
    print(Pin,Inst,ctypes.cast(Id, ctypes.py_object).value)
    CODES.append(Net)
    return Net.Code




class netClass:
    def __init__(self,Father,Pin,Inst):
        self.Id = id(self)
        logs.log_info('%s %s %x'%(Pin,Inst,self.Id))
        self.Father = Father
        self.Pin = Pin
        self.Inst = Inst
        self.Value = 0
        self.Color = ''
        self.Clock = '' 
        self.Cycle = 0 
        self.refClock = '' 
        self.Depth = 0
        self.Support = []
    



class instanceClass:
    def __init__(self,Kind,Path):
        self.Kind = Kind
        self.Path = Path
        self.Base = db.baseme(self)
        self.Pins = {}
        veri.force('%s.base'%(Path),str(self.Base))

        if Kind == 'color':
            self.Color = logs.bin2str(veri.peek('%s.color'%(Path)))
            self.Clock = logs.bin2str(veri.peek('%s.clock'%(Path)))
            self.refClock = logs.bin2str(veri.peek('%s.refclock'%(Path)))

            if self.Clock != '':
                self.Cycle = 0
            self.Pins['in0'] = newNet(self,'in0',self.Base)
            self.Pins['out0'] = newNet(self,'out0',self.Base)

        elif Kind == 'blob':
            self.Func = logs.bin2str(veri.peek('%s.func'%(Path)))
            self.Func = self.Func.replace('||','|')
            self.Func = self.Func.replace('&&','&')
            self.Func = self.Func.replace('!','~')
            self.Vars = getVars(self.Func)
            for Var in self.Vars:
                self.Pins[Var] = newNet(self,Var,self.Base)
            self.Pins['out0'] = newNet(self,'out0',self.Base)
            self.Vals = {}
        elif Kind == 'flop':
            self.Pins['clk'] =  newNet(self,'clk',self.Base)
            self.Pins['dd']  =  newNet(self,'dd',self.Base)
            self.Pins['qq']  =  newNet(self,'qq',self.Base)
        else:
            logs.log_error('kind is %s'%self.Kind)

    def peek(self,Pin):
        return logs.peek('%s.%s'%(self.Path,Pin))
    def force(self,Pin,Val,Obj):
        Path = '%s.%s'%(self.Path,Pin)
        Cval = codeval(Val)
        if (Cval<0)or(Cval>3):
            logs.log_error('forcing failed %s <- %s'%(Path,Val))
            return
        Id = Obj.Code
        Tog = (Id<<2) +codeval(Val)
        veri.force('%s.%s'%(self.Path,Pin),hex(Tog))
        print('FORCING',self.Path,Pin,Val,hex(Tog))


    def run(self,Pin,Val):
        if self.Kind == 'color':
            self.runColor(Val)
        elif self.Kind == 'flop':
            self.runFlop(Pin,Val)
        elif self.Kind == 'blob':
            self.runBlob(Pin,Val)
        else:
            logs.log_error('run kind is %s'%self.Kind)

    def runFlop(self,Pin,Val):
        if Pin == 0:   # clock
            Clk  = self.getNet('clk')
            Clk.Value = value(Val)
            if Clk.Value == '1':
                QQ = self.getNet('qq')
                DD = self.getNet('dd')
                QQ.refClock = Clk.Clock
                QQ.Cycle = Clk.Cycle
                Dval = DD.Value
                QQ.Value = Dval
                self.force('qq',Dval,QQ)
        else:
            DD = self.getNet('dd')
            DD.Value = value(Val)
            Obj = self.getObj(Val)
            if Obj:
                DD.Color = Obj.Color
                DD.refClock = Obj.refClock
                DD.Cycle = Obj.Cycle
            

    def runBlob(self,Pin,Val):
        Pin = 'in%s'%Pin
        self.Vals[Pin] = value(Val)
        Obj = self.getObj(Val)
        OutV = computeFunc(self.Func,self.Vals)
        Out = self.getNet('out0')
        Out.Depth = 1
        Out.Value = OutV
        if Obj != 0:
            Out.Color = Obj.Color
            Out.refClock = Obj.refClock
            Out.Cycle = Obj.Cycle
            Out.Depth = Obj.Depth + 1
        self.force('out0',OutV,Out)


    def runColor(self,Val):
        Val = value(self.peek('in0'))
        In  = self.getNet('in0')
        In.Value = Val
        Out  = self.getNet('out0')
        Out.Color = self.Color
        Out.Value = Val
        if self.Clock != '' :
            Out.Clock = self.Clock
            Out.Cycle = self.Cycle
            self.Cycle += 1
        if self.refClock != '':
            Out.refClock = self.refClock
            Out.Cycle = self.Cycle

        self.force('out0',Val,Out)

    def getNet(self,Pin):
        Code = self.Pins[Pin]
#        print(ctypes.cast(id(Code), ctypes.py_object).value)
        if Code>=len(CODES):
            logs.log_error('code %d (%d) is illegal for pin %s path %s'%(Code,len(CODES),Pin,self.Path))
            return 0
        return CODES[Code]

    def getObj(self,Bus):
#       if (Bus & 0xfffffffffffffffc) == 0: return 0
#        Obj =  ctypes.cast(id(Bus), ctypes.py_object).value
        Code = Bus>>2
        if (Code>len(CODES)): return 0
        return CODES[Code]

def codeval(Val):
    if Val == 'z': return 0
    if Val == 'x': return 1
    if Val == '0': return 2
    if Val == '1': return 3
    if Val ==  0 : return 2
    if Val ==  1 : return 3
def value(Val):
    if Val<0: return 'x'
    X = Val & 3
    if X==0: return 'z'
    if X==1: return 'x'
    if X==2: return 0
    if X==3: return 1
    return 'x'

def getVars(Func):
    for Chr in '~*%+-()&^%|?:':
        Func = Func.replace(Chr,' ')
    Vars = Func.split()
    Vars = set(Vars)
    Vars = list(Vars)
    Vars.sort()
    return Vars

def computeFunc(Func,Vals):
    try:
        return 1 & eval(Func,Vals)
    except:
        return 'x'


def newCode():
    return logs.incrVar('newCode')+1


class dbClass:
    def __init__(self):
        self.BASE = 0
        self.Sons = {}
        self.Metas = {}

    def baseme(self,Son):
        self.BASE += 1
        self.Sons[self.BASE] = Son
        return self.BASE
        
    def addson(self,Kind,Path):
        Son = instanceClass(Kind,Path)
        self.baseme(Son)




import os,sys,string,random
import veri
import logs

db = dbClass()
def flopinit(AA):
    db.addson('flop',logs.bin2str(AA))
def floprun(Base,Pin,Val):
    db.Sons[Base].run(Pin,Val)

def colorinit(AA):
    db.addson('color',logs.bin2str(AA))
def colorrun(Base,Val):
    db.Sons[Base].run(0,Val)

def blobinit(AA):
    db.addson('blob',logs.bin2str(AA))
def blobrun(Base,Pin,Val):
    db.Sons[Base].run(Pin,Val)


