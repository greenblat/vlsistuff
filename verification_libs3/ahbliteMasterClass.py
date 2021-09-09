
import os,sys
import veri
import logs
import random


BURSTS = 'single incr incr4 wrap4 incr8 wrap8 incr16 wrap16'.split()
def burstlen(Burst):
    if Burst=='single': return 1
    if Burst=='incr': return 5
    if Burst[-1]== '4': return 4
    if Burst[-1]== '8': return 8
    if Burst[-1]== '6': return 16
    logs.log_error('Burst %s is not a burst'%Burst)
    return 1

def burstcode(Burst):
    if Burst=='single': return 0
    if Burst=='incr': return 1
    if Burst == 'wrap4': return 2
    if Burst == 'incr4': return 3
    if Burst == 'wrap8': return 4
    if Burst == 'incr8': return 5
    if Burst == 'wrap16': return 6
    if Burst == 'incr16': return 7
    logs.log_error('Burst %s is not a burst'%Burst)
    return 1

SEQ = 3
NONSEQ = 2
BUSY = 1
IDLE = 0

class ahbliteMaster(logs.driverClass):
    def __init__(self,Path,Monitors,Translations={},Name='noName'):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Path = Path
        self.queue=[]
        self.seq=[]
        self.Name=Name
        self.waiting=0
        self.HSEL = 1
        self.translations=Translations
        self.busyOk = True
        self.HSIZE = 2
        self.HPROT = 0
        self.Enable = True
        self.RDATA = []
        self.HWD = 1

    def translate(self,Addr):
        if Addr[0] in '0123456789':
            return eval(Addr)
        if Addr in self.translations:
            return self.translations[Addr][0]
        logs.log_error('cannot determine "%s" address'%Addr)
        return 0


    def onFinish(self):
        return


    def busy(self):
        if self.queue!=[]: return True
        if self.waiting>0: return True
        if self.seq!=[]:   return True
        return False

    def action(self,Txt):
        wrds = Txt.split()
        if wrds[0] in BURSTS:
# ahb wrap4 write 0x1000
            Kind = wrds[1]
            Addr = eval(wrds[2])
            self.queue.append(('burst',wrds[0],Kind,Addr))

        elif wrds[0]=='enable':
            self.Enable = eval(wrds[1])
        elif wrds[0]=='busy':
            self.busyOk = eval(wrds[1])
        elif wrds[0]=='size':
            self.HSIZE = eval(wrds[1])
        elif wrds[0]=='prot':
            self.HPROT = eval(wrds[1])
        elif wrds[0]=='write':
            self.write(wrds[1],wrds[2])
        elif wrds[0]=='read':
            if len(wrds)>2: 
                self.read(wrds[1],wrds[2])
            else:
                self.read(wrds[1])
        elif wrds[0]=='wait':
            self.wait(eval(wrds[1]))
        elif wrds[0]=='RD':
            if len(wrds)==1:
                self.RDATA = []
                return
            Addr = eval(wrds[1])
            Exps = list(map(eval,wrds[2:]))
            while (Exps!=[])and(self.RDATA!=[]):
                Ad,Rd = self.RDATA.pop(0)
                Exp = Exps.pop(0)
                logs.log_ensure((Ad==Addr)and(Rd == Exp),' AHB RD %x exp %x act %x' % (Addr,Exp,Rd))
                Addr += 4
        else:
            logs.log_error('AHB ACTION %s failed'%Txt)

    def wait(self,Wait):
        self.queue.append(('wait',Wait))

    def read(self,Addr,Data = 'none'):
        if type(Addr) is str:
            Addr = self.translate(Addr)
        self.queue.append(('read',Addr,Data))



    def write(self,Addr,Data):
        if type(Addr) is str:
            Addr = self.translate(Addr)
        self.queue.append(('write',Addr,Data))
        
    def tr_peek(self,Sig):
        if  Sig in self.translations:
            Sig = self.translations[Sig]
        return self.peek(Sig)
    def tr_force(self,Sig,Val):
        if  Sig in self.translations:
            Sig = self.translations[Sig]
        return self.force(Sig,Val)

    def hwdata(self):
        self.HWD += 1
        Res = self.HWD + (random.randint(0x1000,0xffff)<<16)
        return  hex(Res)
        
    def run(self):
        if veri.exists('tb.lenq') == '1':
            veri.force('tb.lenqq',str(len(self.queue)))
            veri.force('tb.lenq',str(len(self.seq)))
        if not self.Enable:
            return
        if self.waiting>0:
            self.waiting -= 1
            return
        hreadyout = self.tr_peek('hreadyout')
        if self.seq==[]:
            self.tr_force('hsel',0)
            self.tr_force('htrans',0)
            self.tr_force('hburst',0)
            self.tr_force('hwrite',0)
        if self.seq!=[]:
            List = self.seq[0]
            for (Sig,Val) in List:
                if Sig=='wait':
                    self.waiting=int(Val)
                elif Sig=='catch':
                    if hreadyout==1:
                        X = self.tr_peek(Val[0])
                        if Val[2]!= 'none':
                            if type(Val[2]) == str:
                                Exp = eval(Val[2])
                            else:
                                Exp = Val[2]
                            logs.log_info('ahb %s read act=0x%x exp=%s addr=0x%x '%(self.Name,X,Exp,Val[1]))
                            logs.log_ensure(X==Exp,'ahb %s read act=0x%x exp=%x addr=0x%x '%(self.Name,X,Exp,Val[1]))
                        else:
                            self.RDATA.append((Val[1],X))
                            logs.log_info('ahb %s read 0x%x addr=0x%x'%(self.Name,X,Val[1]))
                elif Sig=='waitUntil':
                    (Net,What) = Val
                    Act = self.tr_peek(Net)
                    if (Act != What): return
                else:
                    self.tr_force(Sig,Val)
            if self.tr_peek('hresp')!=0:
                self.seq = []
                print('HRESP %s' % self.tr_peek('hresp'))
                self.tr_force('hsel',0)
                self.tr_force('htrans',0)
                self.tr_force('hburst',0)
                self.tr_force('hwrite',0)
                return
            if hreadyout==0: return
            self.seq.pop(0)

        while self.queue!=[]:
            What = self.queue.pop(0)
            if What[0]=='wait':
                self.seq.append([('wait',What[1])])
                return
            if What[0]=='burst':
                if What[2][0]=='w': HW=1
                else: HW = 0

                Burst = burstcode(What[1])

                self.seq.append([('hburst',Burst),('haddr',What[3]),('hwdata',0),('hwrite',HW),('htrans',NONSEQ),('hsize',self.HSIZE),('hsel',1)])
                Addrs = []
                if 'wrap' not in What[1]:
                    for X in range(burstlen(What[1])):
                        Addr = What[3]+4*X
                        Addrs.append(Addr)
                elif What[1] == 'wrap4':
                    Low  = What[3] & 0xfffffff0
                    High = (Low + 0x10)-4
                    for X in range(burstlen(What[1])):
                        Addr = What[3]+4*X
                        if Addr<=High:
                            Addrs.append(Addr)
                        else:
                            Addrs.append(Addr-0x10)

                elif What[1] == 'wrap8':
                    Low  = What[3] & 0xffffffe0
                    High = (Low + 0x20)-4
                    for X in range(burstlen(What[1])):
                        Addr = What[3]+4*X
                        if Addr<=High:
                            Addrs.append(Addr)
                        else:
                            Addrs.append(Addr-0x20)

                elif What[1] == 'wrap16':
                    Low  = What[3] & 0xffffffc0
                    High = (Low + 0x40) - 4
                    for X in range(burstlen(What[1])):
                        Addr = What[3]+4*X
                        if Addr<=High:
                            Addrs.append(Addr)
                        else:
                            Addrs.append(Addr-0x40)
#                        logs.log_info('WRAP16 addr=%x run=%x low=%x high=%x    %s' % (What[3],Addr,Low,High,list(map(hex,Addrs))))


#                print('ADDRS',What[0],What[1],burstlen(What[1]),Addrs)
                for X in range(burstlen(What[1])-1):
                    Addr = Addrs[X+1]
                    Eff = Addrs[X]
#                    if (self.busyOk)and(random.randint(0,100)>80):
#                        self.seq.append([('hburst',Burst),('haddr',Addr),('hwdata',0),('hwrite',HW),('htrans',BUSY),('hsize',self.HSIZE),('hsel',1)])
                    if HW==1:
                        self.seq.append([('hburst',Burst),('haddr',Addr),('hwdata',self.hwdata()),('hwrite',HW),('htrans',SEQ),('hsize',self.HSIZE),('hsel',1)])
                    else:
                        self.seq.append([('hburst',Burst),('haddr',Addr),('hwdata',0),('hwrite',HW),('htrans',SEQ),('catch',('hrdata',Eff,'none')),('hsize',self.HSIZE),('hsel',1)])
                
                Eff = Addrs[X+1]
                if HW==1:
                    HWDATA = self.hwdata()
                    self.seq.append([('hburst',0),('haddr',0),('hwdata',HWDATA),('hwrite',0),('htrans',IDLE),('hsize',0),('hsel',0)])
                else:
                    self.seq.append([('hburst',0),('haddr',0),('hwdata',0),('hwrite',0),('htrans',IDLE),('catch',('hrdata',Eff,'none')),('hsize',0),('hsel',0)])
                return


            if What[0]=='write':
                self.seq.append([('haddr',What[1]),('hwdata',0),('hwrite',1),('htrans',2),('hsize',self.HSIZE),('hsel',1)])
                self.seq.append([('haddr',0),('hwdata',What[2]),('hwrite',0),('htrans',0),('hsize',0),('hsel',0)])
                self.seq.append([('haddr',0),('hwrite',0),('htrans',0),('hsel',0)])
                self.seq.append([('waitUntil',('hreadyout',1))])
                return

            if What[0]=='read':
                
                self.seq.append([('haddr',What[1]),('hwrite',0),('htrans',2),('hsel',1),('hsize',self.HSIZE)])
                self.seq.append([('haddr',0),('hwrite',0),('htrans',0),('catch',('hrdata',What[1],What[2])),('hsel',self.HSEL)])
                self.seq.append([('waitUntil',('hreadyout',1))])
                return




