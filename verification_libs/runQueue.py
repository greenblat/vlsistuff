
import os,sys,string,types
import veri
import logs
import random
import traceback



class runQueue:
    def __init__(self,Path,Queue=''):
        self.waiting=0
        self.Path=Path
        self.waitUntilAnd=[]
        self.waitUntilOr=[]
        self.waitSig=False
        self.waitVar=False
        self.waitVal=''
        self.waitNum=0
        self.waitLimit=0
        self.clockRunDuration = 28000
        self.lastRunTime = -100
        self.Table=0
        self.Vars={}
        self.Queue=string.split(Queue,'\n')
    
    def peek(self,Sig):
        return logs.peek('%s.%s'%(self.Path,Sig))


    def run(self):
        if self.lastRunTime>0:
            self.clockRunDuration =  veri.stime() - self.lastRunTime 
        self.lastRunTime  = veri.stime()
    
    
        if self.waiting:
            self.waiting -= 1
            if (self.waiting>0) and ((self.waiting % 100)==0):
                logs.log_info('waiting ilia %d'%self.waiting)
            return
    
    
        if self.waitUntilOr!=[]:
            for (Sig,Val) in self.waitUntilOr:
                Act = self.peek(Sig)
                if Act == logs.intxx(Val):
                    self.waitUntilOr=[]
                    logs.log_info('waitUntilOr done')
                    return
            self.waitNum += 1
            if (self.waitNum % 1000)==0:
                    logs.log_info('waitUntilOr %d  %s'%(self.waitNum,self.waitUntilOr))
            return
                
        if self.waitUntilAnd!=[]:
            for (Sig,Val) in self.waitUntilAnd:
                Act = self.peek(Sig)
                if Act != logs.intxx(Val):
                    self.waitNum += 1
                    if (self.waitNum % 1000)==0:
                            logs.log_info('waitUntilAnd %d  %s'%(self.waitNum,self.waitUntilAnd))
                    return
    
            self.waitUntilAnd=[]
            logs.log_info('waitUntilAnd done')
            return
                
        if self.waitVar:
            Exp = logs.getVar(self.waitVar)
            if (Exp == self.waitVal)or(str(Exp)==str(self.waitVal)):
                self.waitVar=False
                self.waitNum = 0
                logs.log_info('waitVar %s ended exp=%s '%(self.waitVar,Exp))
            else:
                self.waitNum += 1
                if (self.waitNum % 1000)==0:
                    logs.log_info('waitVar %s failed %d times over %s '%(self.waitVar,self.waitNum,self.waitVal))
                if (self.waitNum>self.waitLimit)and(self.waitLimit>0):
                    logs.log_error('waitVar %s reached limit (%d)'%(self.waitVar,self.waitLimit))
                    self.waitVar=False
                    self.waitNum = 0
            return
    
        if self.waitSig:
            Act = self.peek(self.waitSig)
            if self.waitVal[0] in '0123456789':
                Expr = '%s == %s'%(Act,self.waitVal)
            else:
                Expr = '%s %s'%(Act,self.waitVal)
                
            Cond = eval(Expr,self.Vars)
            if Cond:
                self.waitSig=False
                self.waitNum = 0
                logs.log_info('waitUntil %s ended act=%s exp=%s '%(self.waitSig,Act,self.waitVal))
            else:
                self.waitNum += 1
                if (self.waitNum % 1000)==0:
                    logs.log_info('waitUntil %s failed %d times act=%s exp=%s %s'%(self.waitSig,self.waitNum,Act,self.waitVal,Act==self.waitVal))
                if (self.waitNum>self.waitLimit)and(self.waitLimit>0):
                    logs.log_error('waitUntil %s reached limit (%d)'%(self.waitSig,self.waitLimit))
                    self.waitSig=False
                    self.waitNum = 0
    
            return
    
    
    
        if self.Queue==[]: logs.finishing()
    
    
            
    
    
        Cmd = self.Queue.pop(0)
        wrds = string.split(Cmd)
        if wrds==[]: return
        if wrds[0][0] in ['/','#']: return
    
        logs.log_info('cmd %s'%Cmd)
    
        if wrds[0]=='waitNanoSec':
            Dly = eval(wrds[1],self.Vars)
            Many = int(Dly*1000/self.clockRunDuration)
            self.waiting = Many
            logs.log_info('waitNanoSec dly=%d many=%d dura=%d'%(Dly,Many,self.clockRunDuration))
            return
    
        if wrds[0]=='waitMicroSec':
            Dly = eval(wrds[1],self.Vars)
            Many = int(Dly*1000000/self.clockRunDuration)
            self.waiting = Many
            logs.log_info('waitMicroSec dly=%d many=%d dura=%d'%(Dly,Many,self.clockRunDuration))
            return
    
        if wrds[0]=='wait':
            self.waiting = int(wrds[1])
            return
        if wrds[0]=='comment':
            Txt = string.join(wrds[1:],' ')
            forceComment(Txt)
            return
    
        if wrds[0]=='finish':
            logs.finishing()
            return
    
        if wrds[0]=='include':
            Fname = wrds[1]
            if not os.path.exists(Fname):
                logs.log_info('include file "%s" was not found'%Fname)
                return
            lines =  open(Fname).readlines()
            self.Queue = lines + db.Queue
            return
    
    
        if wrds[0]=='compareNet':
            Act = self.peek(wrds[1])
            self.Vars['table']=db.Table
            Exp = eval(wrds[2],self.Vars)
    
            if Act==Exp:
                logs.log_correct('compareNet %s got 0x%x'%(wrds[1],Exp))
            else:
                logs.log_wrong('compareNet %s exp=0x%x act=0x%x'%(wrds[1],Exp,Act))
            return
    
        if wrds[0]=='force':
            where= wrds[1]
            if (len(where)>3)and(where[:3]=='tb.'):
                veri.force(wrds[1],str(eval(wrds[2],self.Vars)))
            else:
                veri.force('tb.%s'%wrds[1],str(eval(wrds[2],self.Vars)))
            return
        if wrds[0]=='hard_force':
            where= wrds[1]
            if (len(where)>3)and(where[:3]=='tb.'):
                veri.hard_force(wrds[1],str(eval(wrds[2],self.Vars)))
            else:
                veri.hard_force('tb.%s'%wrds[1],str(eval(wrds[2],self.Vars)))
            return
    
    
        if wrds[0]=='waitVar':
            self.waitVar = wrds[1]
            self.waitVal = wrds[2]
            self.waitNum = 0
            if len(wrds)>3:
                self.waitLimit = int(wrds[3])
            else:
                self.waitLimit=0
            return
    
        if wrds[0]=='waitUntil':
            self.waitSig = wrds[1]
            self.waitVal = wrds[2]
            self.waitNum = 0
            if len(wrds)>3:
                self.waitLimit = int(wrds[3])
            else:
                self.waitLimit=0
            return
    
        if wrds[0]=='waitUntilOr':
            self.waitUntilOr=[]
            self.waitNum = 0
            ind=1
            while ind<len(wrds):
                self.waitUntilOr.append((wrds[ind],wrds[ind+1]))
                ind += 2
            return
        if wrds[0]=='waitUntilAnd':
            self.waitUntilAnd=[]
            self.waitNum = 0
            ind=1
            while ind<len(wrds):
                self.waitUntilAnd.append((wrds[ind],wrds[ind+1]))
                ind += 2
            return
    
        logs.log_error('bad command "%s"'%Cmd)
        return

def forceComment(Txt):
    A = list(Txt)
    B = map(ord,A)
    C = map(bits8,B)
    X = '0b'+string.join(C,'')
    veri.force('tb.comment',X)


def bits8(Int):
    if type(Int)==types.IntType:
        A = bin(Int)[2:]
        while len(A)<8: A = '0'+A
        return A

    if (type(Int)==types.StringType)and(len(Int)==1):
        return bits8(ord(Int))

def getWidth(Bus):
    if '[' not in Bus:
        return Bus,1
    ww = string.split(Bus[:-1],'[')
    Name = ww[0]
    ww2 = map(int,string.split(ww[1],':'))
    Width = (ww2[0]-ww2[1])+1
    return Name,Width

        
