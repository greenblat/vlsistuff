
'''
i2c master 
accepts bit commands:  start/stop/ack/waitack/data/
and complex commands:   write7addr read7addr write10addr read10addr
'''


import logs
import veri
import sys,string,os
TB = 'tb'
class i2cMasterClass(logs.driverClass):
    def __init__(self,Path,Monitors,Freq=1,Renames={}):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Queue = []
        self.bitqueue = []
        self.Renames = Renames
        self.force('sda',1)
        self.force('scl',1)
        self.Freq =Freq
        self.RX = []
        self.Check = False
        
    def force(self,Sig,Val):
        if Sig in self.Renames: Sig = self.Renames[Sig]
        logs.driverClass.force(self,Sig,Val)

    def peek(self,Sig):
        if Sig in self.Renames: Sig = self.Renames[Sig]
        return logs.driverClass.peek(self,Sig)

    def action(self,Txt):
        wrds = Txt.split()
        Cmd = wrds[0]
        if Cmd =='read7addr':
            if len(wrds)==2:
                self.read7addr(wrds[1])
            else:
                self.read7addr(wrds[1],wrds[2])
        elif Cmd =='write7addr':
            self.write7addr(wrds[1],wrds[2])
        elif Cmd =='wait':
            self.wait(wrds[1])
        elif Cmd =='waitNotBusy':
            return
        else:
            logs.log_error('action not recogninzed "%s"'%Cmd)



    def idle(self):
        if self.bitqueue!=[]: return False
        if self.waiting>0: return False
        return True

    def start(self):
        self.bitqueue.append((1,1,1))
        self.bitqueue.append((1,0,1))
        self.bitqueue.append((0,0,1))

    def stop(self):
        self.bitqueue.append((0,0,1))
        self.bitqueue.append((1,0,1))
        self.bitqueue.append((1,1,1))
        logs.log_info('RX %s'%str(self.RX))
        self.RX = []

    def data(self,Data):
        if type(Data) is list:
            for Char in Data:
                self.data(Char)
            return
        self.bitqueue.append((0,Data,0.5))
        self.bitqueue.append((1,Data,1))
        self.bitqueue.append((0,Data,0.5))

    def ack(self):
        self.data(0)

    def waitack(self):
        self.bitqueue.append((0,1,0.5))
        self.bitqueue.append((1,'L',1))
        self.bitqueue.append((1,'L',0.5))

    def wait(self,Many):
        self.bitqueue.append(('wait',Many,0))

    def write7addr(self,Addr,Data,Bytes=2):
        self.send7bitaddr(Addr,0)
        self.writeBytes(Data,Bytes)

    def write10addr(self,Addr,Data,Bytes=2):
        self.send10bitaddr(Addr,0)
        self.writeBytes(Data,Bytes)

    def read7addr(self,Addr,Bytes=2):
        self.send7bitaddr(Addr,1)
        self.readBytes(Bytes)

    def write10addr(self,Addr,Bytes=2):
        self.send10bitaddr(Addr,1)
        self.readBytes(Bytes)

    def writeBytes(self,Data,Bytes):
        Dbin = logs.binx(Data,Bytes*8)
#        Dbin = reverseBin(Dbin)
        
        for Byte in range(Bytes-1):
            for II in range(8): self.data(Dbin[Byte*8+II])
            self.ack()
        for II in range(8): self.data(Dbin[(Bytes-1)*8+II])
        self.data(1)
        self.stop()
        self.wait(4)
        

    def readBytes(self,Bytes):
        
        for Byte in range(Bytes):
            for II in range(8): self.data('Q')
            self.data(1)
        self.stop()
        self.wait(4)
        



    def send7bitaddr(self,Addr,Rd):
        Abin = logs.binx(Addr,7)
#        Abin = reverseBin(Abin)
        self.start()
        for II in range(7): self.data(Abin[II])
        self.data(Rd)
        self.waitack()

    def send10bitaddr(self,Addr,Rd):
        Abin = logs.binx(Addr,10)
        Abin = reverseBin(Abin)
        self.start()
        self.data(['1','1','1','0',Abin[0],Abin[1]])
        self.data(Rd)
        for II in range(2,10): self.data(Abin[II])
        self.waitack()



    def check(self,What):
        self.Check = True
        self.checkWhat = What


    def run(self):
        veri.force(TB+'.marker',str(self.waiting))
        if self.waiting>0:
            self.waiting -= 1
            return
        if self.Check:
            Sda = self.peek('sda')
            if Sda == self.checkWhat:
                self.Check = False

                
        if self.bitqueue==[]: return
        What = self.bitqueue.pop(0)
        if What[0] == 'finish':
            veri.finish()
            sys.exit()

        if What[0]=='wait': 
            self.waiting = What[1]
            return

        if What[0] in [0,1]:
            self.waiting = int(self.Freq * What[2])
            self.force('scl',What[0])
            if What[1] in [0,1,'0','1']:
                self.force('sda',What[1])
            if What[1] == 'L' :
                self.force('sda',1)
                self.check(0)
            if What[1] == 'H' :
                self.force('sda',1)
                self.check(1,max(1,int(self.Freq/2)))
            if What[1] == 'Q' :
                self.force('sda',1)
                if What[0]==1:
                    self.RX.append(self.peek('sda'))
            return

        logs.log_error('WHAT I2C got "%s"'%str(What))



def reverseBin(Txt):
    List = list(Txt)
    List.reverse()
    Str = ''.join(List)
    return Str

