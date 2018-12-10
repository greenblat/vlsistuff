'''
    apb = apbDriver.apbDriver('tb.cpu',Monitors,'apb')
    apb.translations['setupreg']=0x100
    apb.write(Addr,Data)
    apb.read(Addr)
    apb.wait(100)


'''

import os,sys,string,types
import veri
import logs


class apbDriver:
    bus_locked=False
    def __init__(self,Path,Monitors,Name='optiona'):
        self.Path = Path
        self.Name = Name

        self.queue0=[]
        self.seq0=[]
        self.waiting0=0
        self.wait_until0 = False

        self.queue1=[]
        self.seq1=[]
        self.waiting1=0
        self.wait_until1 = False

        self.translations={}
        self.renames={}
        self.markers={}
        self.finishes=False
        Monitors.append(self)

    def translate(self,Addr):
        if Addr in self.translations:
            return self.translations[Addr][0]
        logs.log_error('apb %s cannot determine "%s" address'%(self.Name,Addr))
        return 0

    def marker(self,Which):
        self.queue0.append(('marker',Which))

    def read(self,Addr,expData='none'):
        if type(Addr)==types.StringType:
            Addr = self.translate(Addr)
        self.queue1.append(('read',Addr,expData))
        self.queue1.append(('wait',10))



    def write(self,Addr,Data):
        if type(Addr)==types.StringType:
            Addr = self.translate(Addr)
        self.queue0.append(('write',Addr,Data))
    def wait(self,Data):
        self.queue0.append(('wait',Data))
        self.queue1.append(('wait',Data))
    def waitUntil(self,Data,Timeout):
        self.queue0.append(('until',Data,Timeout))
        
    def finish(self,Data=10):
        self.queue0.append(('wait',Data))
        self.queue0.append(('finish',0))
    def rename(self,Sig):
        if Sig in self.renames: 
            return self.renames[Sig]
        return Sig
    def force(self,Sig,Val):
#        logs.log_info('forcing %s %s <- %s'%(self.Name,Sig,Val))
        veri.force('%s.%s'%(self.Path,Sig),str(Val))

    def installUntil(self,Val,Which):
        Expr,Timeout = Val
        Vars = extractVars(Expr)
        Trans = []
        for ind,Var in enumerate(Vars):
            Trans.append((len(Var),'__var%dxxx'%ind,Var))
        Trans.sort()
        Trans.reverse()
            
        for _,Rep,Var in Trans:
            Expr = string.replace(Expr,Var,Rep)

        if Which==0:
            self.wait_until0 = (Expr,Trans,Timeout)
        else:
            self.wait_until1 = (Expr,Trans,Timeout)

    def evaluateUntil(self,Which):
        if Which==0:
            Expr,Trans,Timeout = self.wait_until0
        else:
            Expr,Trans,Timeout = self.wait_until1
        Dir={}
        for _,Rep,Var in Trans:
            X = logs.peek(Var)
            Dir[Rep]=X
        Res = eval(Expr,Dir)
        return Res
            
        
    def run(self):
        self.run0()
        self.run1()

    def run0(self):
        if self.waiting0>0:
            self.waiting0 -= 1
            return
        if self.wait_until0:
            if self.evaluateUntil(0):
                self.wait_until0=False
            else:
                Expr,Trans,Timeout = self.wait_until0
                if (Timeout==1)and(Timeout!=0):
                    logs.log_error('timeout of wait until "%s" "%s"  happened.'%(Expr,Trans))
                    self.wait_until0=False
                else:
                    self.wait_until0 = Expr,Trans,Timeout-1
                
                return
        if self.seq0!=[]:
            List = self.seq0[0]
            if List[0][0]=='lock':
                if (apbDriver.bus_locked) and (apbDriver.bus_locked!=self):  return
        
        if self.seq0!=[]:
            List = self.seq0.pop(0)
#            logs.log_info('apb popping %s'%str(List))
            for (Sig,Val) in List:
                if Sig=='lock':
                    if Val==1: apbDriver.bus_locked=self
                    elif Val==0: apbDriver.bus_locked=False
                elif Sig=='marker':
                    logs.log_info('marker from APB %s'%self.Name)
                    if Val[0] in self.markers:
                        self.markers[Val[0]](Val[1:])
                    else:
                        logs.log_error('marker %s from APB %s is not defined'%(Val,self.Name))
                elif Sig=='finish':
                    logs.log_info('finishing from APB %s'%self.Name)
                    if self.finishes: self.finishes()
                    veri.finish()
                    sys.exit()
                elif Sig=='wait':
                    self.waiting0=int(Val)
                elif Sig=='catch':
                    Who,Exp = Val
                    X = logs.peek('%s.%s'%(self.Path,self.rename(Who)))
                    if type(Exp)==types.FunctionType:
                        Exp(X)
                    else: 
                        logs.log_info('apb %s read act=%x exp=%s who=%s'%(self.Name,X,Exp,self.rename(Who)))
                elif Sig=='until':
                    self.installUntil(Val,0)
                else:
                    self.force(self.rename(Sig),Val)
            return
        if veri.peek('%s.%s'%(self.Path,self.rename('pready')))=='0':
            self.waiting0 = 10
            return
        if self.queue0!=[]:
            What = self.queue0.pop(0)
            if What[0]=='write':
                self.seq0.append([('lock',1),('psel',1),('paddr',What[1]),('pwdata',What[2]),('pwrite',1)])
                self.seq0.append([('penable',1)])
                self.seq0.append([('psel',0),('paddr',0),('pwdata',0),('pwrite',0),('penable',0)])
                self.seq0.append([('lock',0),('wait',5)])

            elif What[0]=='read':
                self.seq0.append([('lock','1'),('psel',1),('paddr',What[1]),('pwrite',0)])
                self.seq0.append([('penable',1)])
                self.seq0.append([('catch',('prdata',What[2])),('psel',0),('paddr',0),('pwrite',0),('penable',0)])
                self.seq0.append([('lock','0'),('wait',5)])
            elif What[0]=='wait':
                self.seq0.append([('wait',What[1])])
            elif What[0]=='finish':
                self.seq0.append([('finish',0)])
            elif What[0]=='marker':
                self.seq0.append([('marker',What[1])])
            elif What[0]=='until':
                self.seq0.append([('until',(What[1],What[2]))])
            else:
                logs.log_error('apb %s: unrecognized ilia command %s'%(self.Name,str(What)))



    def run1(self):
        if self.waiting1>0:
            self.waiting1 -= 1
            return
        if self.wait_until1:
            if self.evaluateUntil(1):
                self.wait_until1=False
            else:
                Expr,Trans,Timeout = self.wait_until1
                if (Timeout==1)and(Timeout!=0):
                    logs.log_error('timeout of wait until "%s" "%s"  happened.'%(Expr,Trans))
                    self.wait_until1=False
                else:
                    self.wait_until1 = Expr,Trans,Timeout-1
                
                return
        if self.seq1!=[]:
            List = self.seq1[0]
            if List[0][0]=='lock':
                if (apbDriver.bus_locked) and (apbDriver.bus_locked!=self):  return
        
        if self.seq1!=[]:
            List = self.seq1.pop(0)
#            logs.log_info('apb popping %s'%str(List))
            for (Sig,Val) in List:
                if Sig=='lock':
                    if Val==1: apbDriver.bus_locked=self
                    elif Val==0: apbDriver.bus_locked=False
                elif Sig=='marker':
                    logs.log_info('marker from APB %s'%self.Name)
                    if Val[0] in self.markers:
                        self.markers[Val[0]](Val[1:])
                    else:
                        logs.log_error('marker %s from APB %s is not defined'%(Val,self.Name))
                elif Sig=='finish':
                    logs.log_info('finishing from APB %s'%self.Name)
                    if self.finishes: self.finishes()
                    veri.finish()
                    sys.exit()
                elif Sig=='wait':
                    self.waiting1=int(Val)
                elif Sig=='catch':
                    Who,Exp = Val
                    X = logs.peek('%s.%s'%(self.Path,self.rename(Who)))
                    if type(Exp)==types.FunctionType:
                        Exp(X)
                    else: 
                        logs.log_info('apb %s read act=%x (%s) exp=%s who=%s'%(self.Name,X,chr(X & 0xff),Exp,self.rename(Who)))
                elif Sig=='until':
                    self.installUntil(Val,0)
                else:
                    self.force(self.rename(Sig),Val)
            return
        if veri.peek('%s.%s'%(self.Path,self.rename('pready')))=='0':
            self.waiting1 = 10
            return
        if self.queue1!=[]:
            What = self.queue1.pop(0)
            if What[0]=='write':
                self.seq1.append([('lock',1),('psel',1),('paddr',What[1]),('pwdata',What[2]),('pwrite',1)])
                self.seq1.append([('penable',1)])
                self.seq1.append([('psel',0),('paddr',0),('pwdata',0),('pwrite',0),('penable',0)])
                self.seq1.append([('lock',0),('wait',5)])

            elif What[0]=='read':
                self.seq1.append([('lock','1'),('psel',1),('paddr',What[1]),('pwrite',0)])
                self.seq1.append([('penable',1)])
                self.seq1.append([('catch',('prdata',What[2])),('psel',0),('paddr',0),('pwrite',0),('penable',0)])
                self.seq1.append([('lock','0'),('wait',5)])
            elif What[0]=='wait':
                self.seq1.append([('wait',What[1])])
            elif What[0]=='finish':
                self.seq1.append([('finish',0)])
            elif What[0]=='marker':
                self.seq1.append([('marker',What[1])])
            elif What[0]=='until':
                self.seq1.append([('until',(What[1],What[2]))])
            else:
                logs.log_error('apb %s: unrecognized ilia command %s'%(self.Name,str(What)))



def extractVars(Txt):
    for Chr in '+()-<>=!':
        Txt = string.replace(Txt,Chr,' ')
    Wrds = string.split(Txt)
    Res=[]
    for Wrd in Wrds:
        if Wrd not in ['or','and','not']:
            if Wrd[0] not in '0123456789':
                Res.append(Wrd)
    return Res
