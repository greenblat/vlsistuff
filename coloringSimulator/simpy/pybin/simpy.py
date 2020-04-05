#! /usr/bin/env python3
import os,sys,string
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs'%NewName)

import logs3 as logs

from models import *

        
class dbClass:
    def __init__(self):
        self.Cycles = 0
        self.Wrongs = 0
        self.Corrects = 0
        self.Errors = 0
        self.Simtime = 0
        self.vcdTime = 0
        self.Insts = {}
        self.Nets = {}
        self.Queues = [[],[]]
        self.timeWheel = {}
        self.times = []
        self.Fvcd = False
        self.script = False
        self.LastTime =  -1
        self.vcdIndex = {}
        self.Clocks = {}
        self.RUN = True
        
    def keepClocks(self):
        for Clk in self.Clocks:
            Cycles,Dur1,Dur0 = self.Clocks[Clk]
            X = Cycles * (Dur1+Dur0)
            self.setNet(Clk,X,'0',{'clk':(Clk,Cycles)})
            self.setNet(Clk,X+Dur1,'1',{'clk':(Clk,Cycles)})
            self.Clocks[Clk] = Cycles+1,Dur1,Dur0 


    def addMeToNet(self,Sig,Dir,Obj,Pin):
        if Sig not in self.Nets:
            Onet = netClass(self,Sig,1)
        else:
            Onet = self.Nets[Sig]
        if Dir[0] == 'o':
            Onet.Outs.append((Obj,Pin))
        elif Dir[0] == 'i':
            Onet.Ins.append((Obj,Pin))
    
    def runOne(self):
        self.keepClocks()
        while self.Queues[0]!=[]:
            Onet = self.Queues[0].pop(0)
            for Obj,Pin in Onet.Ins:
                Obj.setPin(Pin,Onet.Value,Onet.Colors,False)

        while self.Queues[1]  != []:
            Onet = self.Queues[1].pop(0)
            Onet.setVal(Onet.Next,Onet.Colors,False)
            Drv,Pin = Onet.Outs[0]
            for Obj,Pin in Onet.Ins:
                Obj.setPin(Pin,Onet.Value,Onet.Colors,False)

        while self.Queues[0]!=[]:
            Onet = self.Queues[0].pop(0)
            for Obj,Pin in Onet.Ins:
                Obj.setPin(Pin,Onet.Value,Onet.Colors,True)
        if self.times==[]: return
        self.Simtime = self.times.pop(0)
        if (self.Simtime>=self.LastTime)and(self.LastTime>0):
            logs.log_info('lasttime reached. exiting')
            self.RUN = False
            return
        List = self.timeWheel.pop(self.Simtime)
        for Onet,Val,Colors in List:
            Onet.setVal(Val,Colors,True)

    def active(self):
        if self.times != []: return True
        if self.Queues[0] != []: return True
        if self.Queues[1] != []: return True
        return False

    def setNet(self,Net,Time,Val,Colors=False):
        if Time not in self.times:
            self.times.append(Time)
            self.times.sort()
            self.timeWheel[Time] = []
        if Net not in self.Nets:
            logs.log_error('net %s is not defined for setNet'%Net)
            return
        Onet  = self.Nets[Net]
        self.timeWheel[Time].append((Onet,Val,Colors))
            
    def run(self):
        while self.active()and self.RUN:
            self.runOne()
            
    def report(self):
        for Net in self.Nets.keys():
            Onet = self.Nets[Net]

    def setFuture(self,Sig,Val,Colors,Delay):
        Time = Delay + self.Simtime
        self.setNet(Sig,Time,Val,Colors)
        
    def vcdWrite(self,Sig,Val):
        if self.Simtime>self.vcdTime:
            self.Fvcd.write('#%d\n'%self.Simtime)
            self.vcdTime = self.Simtime
        Vcdx= self.vcdIndex[Sig]
        Wid = self.Nets[Sig].Width
        Wid = max(Wid,len(Val))
        if Wid==1:
            self.Fvcd.write('%s%s\n'%(Val,Vcdx))
        else:
            A = '0'*Wid + Val
            Val = A[-Wid:]
            self.Fvcd.write('b%s %s\n'%(Val,Vcdx))
        
    def readme(self,Fname):
        File = open(Fname)
    
        while 1:
            line = File.readline()
            if line=='': return
            if '//' in line:
                line = line[:line.index('//')]
            wrds = line.split()
            if len(wrds)==0:
                pass 
            elif wrds[0]=='include':
                self.readme(wrds[1])
            elif wrds[0]=='net':
                Net = wrds[1]
                if '|' in wrds:
                    wrds = wrds[wrds.index('|')+1:]
                    for Prm in wrds:
                        ww = Prm.split('=')
                        if (len(ww)==2)and(ww[0]=='width'):
                            Wid = int(ww[1])
                            if Net not in self.Nets:
                                netClass(self,Net,Wid)
                            else:
                                self.Nets[Net].Width=Wid
                        elif (Prm!=';'):
                            logs.log_error('bad param for net %s -- %s'%(Net,Prm))
                else:
                    logs.log_error('bad net line %s'%(wrds.join(' ')))

            elif wrds[0]=='inst':
                Type = wrds[1]
                Inst = wrds[2]
                LL = wrds[3:]
                Conns = []
                Params = {}
                Wids = []
                while (LL!=[])and(LL[0] not in ['|',';']):
                    Conn = LL.pop(0)
                    if '<' in Conn:
                        ww = Conn.split('<')
                        Bus,Wid = parseBus(ww[1])
                        Conns.append(('input',ww[0],Bus))
                        Wids.append((Bus,Wid))
                    elif '>' in Conn:
                        ww = Conn.split('>')
                        Bus,Wid = parseBus(ww[1])
                        Conns.append(('output',ww[0],Bus))
                        Wids.append((Bus,Wid))
                    else:
                        ww = Conn.split('=')
                        Bus,Wid = parseBus(ww[1])
                        Conns.append((ww[0],Bus))
                        Wids.append((Bus,Wid))
                    
                if (LL!=[])and(LL[0]=='|'):
                    LL.pop(0)
                    while (LL!=[])and(LL[0] != ';'):
                        Prm = LL.pop(0)
                        ww = Prm.split('=')
                        Params[ww[0]]=ww[1]
                instanceClass(self,Type,Inst,Conns,Params)
                for Bus,Wid in Wids:
                    self.Nets[Bus].Width=max(Wid,self.Nets[Bus].Width)
    
            elif wrds[0]=='color':
                Net = wrds[1]
                Params = parseParam(wrds[2:])
                if Net not in self.Nets:
                    netClass(self,Net,1)
                db.Nets[Net].Colors = Params
            elif wrds[0]=='force':
                Net = wrds[1]
                if Net not in self.Nets:
                    netClass(self,Net,1)

                self.setNet(Net,0,wrds[2],self.Nets[Net].Colors)
                if len(wrds)>3:
                    LL = wrds[3:]
                    while LL!=[]:
                        Time = int(LL.pop(0))
                        Val  = LL.pop(0)
                        self.setNet(Net,Time,Val,self.Nets[Net].Colors)
            elif wrds[0]=='clock':
                Clk = wrds[1]
                if Clk not in self.Nets:
                    netClass(self,Clk,1)
                self.Clocks[Clk] = (0,int(wrds[2]),int(wrds[3]))
            elif wrds[0]=='script':
                self.script = wrds[1]
            elif wrds[0]=='vcd':
                db.Fvcd = open(wrds[1],'w')
                start_vcd(db)
            elif wrds[0]=='run':
                if not db.Fvcd: 
                    db.Fvcd = open('a.vcd','w')
                if len(wrds)>1:
                    db.LastTime = int(wrds[1])
                return
            else:
                logs.log_error('unrecognized %s command'%wrds[0])

db = dbClass()


class instanceClass:
    def __init__(self,db,Type,Inst,Conns,Params=[]):
        self.Type = Type
        self.Inst = Inst
        self.Name = Inst
        self.Context = {}
        self.Conns = {}
        self.Colors = {}
        self.db = db
        self.Delay = 0
        self.Params = Params
        self.Func = False
        db.Insts[Inst] = self
        for Conn in Conns:
            if len(Conn)==3:
                Dir,Pin,Sig = Conn
                self.Conns[Pin]=Sig
                db.addMeToNet(Sig,Dir,self,Pin)
            elif len(Conn)==2:
                Pin,Sig = Conn
                self.Conns[Pin]=Sig
                Dir = findOutDir(Type,Pin)
                db.addMeToNet(Sig,Dir,self,Pin)

    def addVdd(self,Colors):
        if 'vdd' not in self.Colors:
            return Colors
        if 'vdd' not in Colors:
            VDD = self.Colors['vdd']
            Colors['vdd']=VDD
            return Colors

        VDD = Colors['vdd']
        Vddobj = self.Colors['vdd']
        if VDD!=Vddobj:
            logs.log_error('VDD collision object=%s/%s hass vdd=%s   net arrived vdd=%s'%(Obj.Name,Obj.Type,Vddobj,VDD))
        Colors['vdd']=Vddobj
        return Colors


    def vals(self,Pin):
        Sig = self.Conns[Pin]
        Colors = self.db.Nets[Sig].Colors
        if Colors==None:
            Colors = {}
        return self.db.Nets[Sig].Value,Colors

    def posedge(self,Pin):
        Sig = self.Conns[Pin]
        Edge = self.db.Nets[Sig].posedge()
        return Edge

    def setPin(self,Pin,Val,Color,noEdge):
        self.run(noEdge)

    def run(self,noEdge):
        Code = Models[self.Type]
        Nows,Nexts = Code(self)
        if noEdge: Nexts=[]
        if self.Delay==0:
            for Pin,Val,Colors in Nows:
                Sig = self.Conns[Pin]
                self.db.Nets[Sig].setVal(Val,Colors,True)
            for Pin,Val,Colors in Nexts:
                Sig = self.Conns[Pin]
                self.db.Nets[Sig].setNext(Val,Colors)
        else: 
            for Pin,Val,Colors in Nows+Nexts:
                Sig = self.Conns[Pin]
                self.db.setFuture(Sig,Val,Colors,self.Delay)
                



class netClass:
    def __init__(self,db,Net,Width):
        self.Net = Net
        self.Name = Net
        self.Width = Width
        db.Nets[Net] = self
        self.Ins = []
        self.Outs = []
        self.Prev = 0
        self.Value = 'x'
        self.Next = 0
        self.Time = -1
        self.Colors = {}
        self.db = db

    def posedge(self):
        return (self.Prev!='1')and(self.Value=='1'),self.Colors

    def setNext(self,Val,Colors):
        self.Next = Val
        self.Colors = Colors
        self.db.Queues[1].append(self)
    def setVal(self,Val,Colors=False,enQueue=True):
        Val = str(Val)
        if Val!=self.Value:
            self.Prev = self.Value
            self.Value = Val
            self.Time = self.db.Simtime
            self.Colors = Colors
            self.db.vcdWrite(self.Net,self.Value)
            if enQueue:
                self.db.Queues[0].append(self)






def main():
    Fname = sys.argv[1]
    db.readme(Fname)
    logs.log_info('insts %d nets %d'%(len(db.Nets.keys()),len(db.Insts.keys())))
    if db.script:
        AA = db.script.split('/')
        if len(AA)>1:
            Path = '/'.join(AA[:-1])
            sys.path.append(Path)
        else:
            sys.path.append('.')

        MM = AA[-1]
        MM = MM.replace('.py','')
        exec('import %s'%MM)
        exec('db.Script = %s'%MM)

    while db.RUN:
        db.run() 
    db.report()


def start_vcd(db):
    db.Fvcd.write('$scope module %s $end\n'%('top'))
    for Pos,Sig in enumerate(db.Nets.keys()):
        Onet = db.Nets[Sig]
        db.vcdIndex[Sig]=vcdcode(Pos)
        Wid = db.Nets[Sig].Width
        db.Fvcd.write('$var wire %d %s %s $end\n'%(Wid,vcdcode(Pos),Sig))
    db.Fvcd.write('$upscope $end\n')
    db.Fvcd.write('$enddefinitions $end\n')



def vcdcode(Pos):
    X = '%' 
    A = '!' 
    B = '~' 
    C = '"' 
    D = '\\'
    Dist = ord(B)-ord(A)+1
    run=Pos+1 
    res=''  
    while (run):
        X1 = int(run / Dist); 
        X2 = int(run %  Dist);
        Ch = ord(A)+X2;
        res=res+chr(Ch);
        run=X1; 
    
    return res;


def checkVal(Obj,Val):
    if type(Val) is int:
        logs.log_error('checkVal %s %s'%(Val,Obj.Name))
    else:
        logs.log_correct('checkVal %s %s'%(Val,Obj.Name))

def parseBus(Txt):
    if '[' not in Txt:
        return Txt,1
    Bus = Txt[:Txt.index('[')]
    WW = Txt[Txt.index('[')+1: -1]
    if ':':
        ww2 = list(map(int,WW.split(':')))
        Wid = ww2[0]-ww2[1]+1
        return Bus,Wid
    logs.log_error('expects bus[hi:lo]')
    return Bus,1

def parseParam(wrds):
    Params = {}
    for wrd in wrds:
        WW = wrd.split('=')
        if len(WW)==2:
            Params[WW[0]]=WW[1]
    return Params         


if __name__ == '__main__': main()

