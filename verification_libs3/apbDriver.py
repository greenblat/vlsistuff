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
    def __init__(self,Path,Monitors,Name='optional'):
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
        self.prefix = ''
        self.markers={}
        self.finishes=False
        self.hexMode = False
        self.Backs = []
        if Monitors != -1:
            Monitors.append(self)
        self.Caller = False
        logs.log_info('apbDriver  ver 27.apr.2021')
        self.noList = []
        if not self.exists('pstrb'):
            self.noList.append('pstrb')

    def exists(self,Sig):
        Full = '%s.%s'%(self.Path,Sig)
        X = veri.exists(Full)
        return Full == '1'


    def setName(self,Name):
        self.queue0.append(('name',Name))
    def load_renames_file(self,Fname):
        '''define wd_load_value 0x0'''
        File = open(Fname)
        while 1:
            line = File.readline()
            if line=='': return
            wrds = line.split()
            if (len(wrds)==3) and (wrds[0]=='define'):
                Name = wrds[1]
                Addr = eval(wrds[2])
                self.renames[Name]=Addr



    def busy(self):
        if self.queue1!=[]: return True
        if self.queue0!=[]: return True
        if self.seq0!=[]: return True
        if self.seq1!=[]: return True
        return False

    def translate(self,Addr):
        if ('[' in Addr):
            Bus,Ind = Addr.split('[')
            Ind = eval(Ind[:-1])
            Base = self.translate(Bus)
            return Base + 4*Ind

        Addr = self.rename(Addr)
        if type(Addr) is int: return Addr
        if Addr in self.translations:
            return self.translations[Addr][0]
        try:
            Add = eval(Addr,self.renames)
            return Add
        except:
            logs.log_error('apb %s cannot determine "%s" address'%(self.Name,Addr))
            return 0

    def marker(self,Which):
        self.queue0.append(('marker',Which))

    def prdata(self):
        Who,Act,Addr = self.Backs.pop(0)
        return Act

    def action(self,Cmd):
        wrds = Cmd.split()
        if wrds[0]=='read':
            if len(wrds)==2:
                self.read(wrds[1])
            else:
                self.read(wrds[1],self.eval(wrds[2]))
        elif wrds[0]=='write':
            self.write(wrds[1],wrds[2])
        elif wrds[0]=='prdata':
            Who,Act,Addr = self.Backs.pop(0)
            Deg = wrds[1]
            if self.Caller:
                self.Caller.Translates[Deg]=Act
                print('XXXXX',Deg,Act)

        elif wrds[0]=='wait':
            self.wait(wrds[1])
        else:
            logs.log_error('action not recogninzed "%s"'%Cmd)

    def read1(self,Addr,expData='none'):
        if type(Addr) is str:
            Addr = self.translate(Addr)
        self.queue1.append(('read',Addr,expData))

    def read(self,Addr,expData='none'):
        if type(Addr) is str:
            Addr = self.translate(Addr)
        self.queue0.append(('read',Addr,expData))

    def forcenet(self,Net,Val):
        self.queue0.append(('force',Net,Val))

    def eval(self,Data):
        if self.Caller:
            return eval(Data,self.renames,self.Caller.Translates)
        return eval(Data,self.renames)

    def write(self,Addr,Data):
        if type(Addr) is str:
#            logs.log_info('translate address in=%s out=%x'%(Addr,self.translate(Addr)))
            Addr = self.translate(Addr)
        if type(Data) is float:
            Data = logs.float2binary(Data)
#        logs.log_info('apb write  address=%x  data=%x'%(Addr,Data))
        if type(Data) is str:
            Data = self.eval(Data)
        self.queue0.append(('write',Addr,Data))

    def write1(self,Addr,Data):
        if type(Addr) is str:
            Addr = self.translate(Addr)
        if type(Data) is float:
            Data = logs.float2binary(Data)
        if type(Data) is str:
            Data = eval(Data,self.renames)
        self.queue1.append(('write',Addr,Data))


    def wait1(self,Data):
        self.queue1.append(('wait',Data))

    def wait(self,Data):
        self.queue0.append(('wait',Data))
    def waitUntil(self,Data,Timeout):
        self.queue0.append(('until',Data,Timeout))
    def waitNotBusy(self,Data,Timeout):
        self.queue0.append(('notbusy',0))
#        logs.log_info('enable waiting for not busy')

        
    def finish(self,Data=10):
        self.queue0.append(('wait',Data))
        self.queue0.append(('finish',0))
    def rename(self,Sig):
        if Sig[0] in '0123456789':
            return Sig
        if self.prefix!='':
            Sig = '%s%s'%(self.prefix,Sig)
        if Sig in self.renames: 
            return self.rename(self.renames[Sig])
        return Sig
    def peek(self,Sig):
        if Sig in self.noList:
            return 0
        if Sig in self.translations:
            Sig = self.translations[Sig]
        if self.Path=='':
            Full = self.rename(Sig)
        else:
            Full = '%s.%s'%(self.Path,self.rename(Sig))
        return logs.peek(Full)
    def force(self,Sig,Val):
        if Sig in self.noList:
            return 
#        logs.log_info('forcing %s %s <- %x'%(self.Name,Sig,Val))
        if Sig in self.translations:
            Sig = self.translations[Sig]
        if self.hexMode: Val = hex(Val)
        if self.Path=='':
            veri.force(Sig,str(Val))
        else:
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
            Expr = Expr.replace(Var,Rep)

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
        self.doQueue0()

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
            AA0 = self.seq0[0][0]
            if (len(AA0)==3)and(AA0[0]=='conditional'):
                Who = AA0[1]
                What = AA0[2]
                Val = self.peek(Who)
                if What!=Val:return
            if AA0=='notbusy':
#                logs.log_info('seq0 %s %s'%(AA0,self.busy()))
                if self.busy(): return 
                self.seq0.pop(0)
                return

            List = self.seq0[0]
#            if self.peek('pready')==0:
#                return
            if (len(List[0])==3): List.pop(0)
#            logs.log_info('DBG0 %s'%str(List))
            for (Sig,Val) in List:
                if Sig=='lock':
                    if Val==1: apbDriver.bus_locked=self
                    elif Val==0: apbDriver.bus_locked=False
                elif Sig=='name':
                    self.Name = Val
                elif Sig=='marker':
                    logs.log_info('marker from APB %s'%self.Name)
                    if Val[0] in self.markers:
                        self.markers[Val[0]](Val[1:])
                    else:
                        logs.log_error('marker %s from APB %s is not defined'%(Val,self.Name))
                elif Sig=='finish':
                    logs.log_info('finishing from APB %s'%self.Name,2)
                    logs.log_ending('scores',2)
                    if self.finishes: self.finishes()
                    veri.finish()
                    sys.exit()
                elif Sig=='wait':
                    self.waiting0=int(Val)
                elif Sig=='catch':
                    Who,Exp,Addr = Val
                    print('EXP',Who,Addr,Exp)
                    Act = self.peek(self.rename(Who))
                    if type(Exp) is types.FunctionType:
                        Exp(Act)
                    elif type(Exp) is int:
                        logs.log_ensure((Exp==Act),'apb addr=%x %s read act=%x exp=%s (0x%x) (0d%d)  who=%s'%(Addr,self.Name,Act,Exp,Exp,Exp,self.rename(Who)),2)
                    else: 
                        logs.log_info('apb addr=%x %s read act=%x who=%s'%(Addr,self.Name,Act,self.rename(Who)))
                        self.Backs.append((Who,Act,Addr))
                elif Sig=='until':
                    self.installUntil(Val,0)
                else:
                    self.force(self.rename(Sig),Val)
            if self.peek('pready')==1:
                self.seq0.pop(0)
            return
        if self.peek('pready')==0:
            self.waiting0 = 10
            return
    def doQueue0(self):
        while self.queue0!=[]:
            What = self.queue0.pop(0)
            if What[0]=='write':
#                logs.log_info('write apb queue0 seq0 %s %s %s'%(What[0],hex(What[1]),hex(What[2])))
                self.seq0.append([('penable',0),('lock',1),('psel',1),('pstrb',0xf),('paddr',What[1]),('pwdata',What[2]),('pwrite',1)])
                self.seq0.append([('penable',1)])
                if (self.queue0==[])or(self.queue0[0][0] not in ['write','read']):
                    self.seq0.append([('conditional','pready',1),('psel',0),('pstrb',0),('paddr',0),('pwdata',0),('pwrite',0),('penable',0),('lock',0)])
#                self.seq0.append([('lock',0)])

            elif What[0]=='read':
                self.seq0.append([('lock','1'),('psel',1),('paddr',What[1]),('pwrite',0)])
                self.seq0.append([('penable',1)])
                self.seq0.append([('conditional','pready',1),('catch',('prdata',What[2],What[1])),('psel',0),('paddr',0),('pwrite',0),('penable',0)])
                self.seq0.append([('lock','0'),('wait',5)])
            elif What[0]=='wait':
                self.seq0.append([('wait',What[1])])
            elif What[0]=='finish':
                self.seq0.append([('finish',0)])
            elif What[0]=='marker':
                self.seq0.append([('marker',What[1])])
            elif What[0]=='name':
                self.seq0.append([('name',What[1])])
            elif What[0]=='until':
                self.seq0.append([('until',(What[1],What[2]))])
            elif What[0]=='force':
                self.seq0.append([(What[1],What[2])])
            elif What[0]=='notbusy':
                self.seq0.append(('notbusy',0))
            else:
                logs.log_error('apb %s: unrecognized ilia command %s'%(self.Name,str(What)))



    def run1(self):
#        if (len(self.queue1),len(self.seq1)) != (0,0):
#            logs.log_info('run1 wait1=%d until1=%s queue1=%d seq1=%d'%(self.waiting1,self.wait_until1,len(self.queue1),len(self.seq1)))
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
            AA0 = self.seq1[0][0]
            if (len(AA0)==3)and(AA0[0]=='conditional'):
                Who = AA0[1]
                What = AA0[2]
                Val = self.peek(Who)
                if Val!=What:return
            List = self.seq1.pop(0)
            if (len(List[0])==3):  List.pop(0)
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
                    Who,Exp,Addr = Val
                    X = self.peek(self.rename(Who))
                    logs.log_info('catch %s %s'%(Who,Exp))
                    if type(Exp) is function:
                        Exp(X)
                    elif type(Exp)== int:
                        logs.log_ensure((Exp==Act),'apb addr=%x %s read act=%x exp=%s (0x%x) (0d%d)  who=%s'%(Addr,self.Name,Act,Exp,Exp,Exp,self.rename(Who)),2)
                    else: 
                        Exp0 = eval(Exp,self.renames)
                        logs.log_info('apb %s read act=%x exp=%s (%x) (0d%d)   who=%s'%(self.Name,X,Exp,Exp0,Exp0,self.rename(Who)))
                        self.Backs.append((Who,Act,Addr))

                elif Sig=='until':
                    self.installUntil(Val,0)
                else:
                    self.force(self.rename(Sig),Val)
            return
        if self.peek(self.rename('pready'))=='0':
            self.waiting1 = 10
            return
        if self.queue1!=[]:
            What = self.queue1.pop(0)
            if What[0]=='write':
                self.seq1.append([('lock',1),('psel',1),('paddr',What[1]),('pwdata',What[2]),('pwrite',1)])
                self.seq1.append([('penable',1)])
                self.seq1.append([('conditional','pready',1),('psel',0),('paddr',0),('pwdata',0),('pwrite',0),('penable',0)])
                self.seq1.append([('lock',0)])

            elif What[0]=='read':
                self.seq1.append([('lock','1'),('psel',1),('paddr',What[1]),('pwrite',0)])
                self.seq1.append([('penable',1)])
                self.seq1.append([('conditional','pready',1),('catch',('prdata',What[2],What[1])),('psel',0),('paddr',0),('pwrite',0),('penable',0)])
                self.seq1.append([('lock','0')])
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
        Txt = Txt.replace(Chr,' ')
    Wrds = Txt.split()
    Res=[]
    for Wrd in Wrds:
        if Wrd not in ['or','and','not']:
            if Wrd[0] not in '0123456789':
                Res.append(Wrd)
    return Res
