
import os,sys
import veri
import logs


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
IDLE = 0

class ahbliteMaster(logs.driverClass):
    def __init__(self,Path,Monitors,Translations={},Name='noName'):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Path = Path
        self.queue=[]
        self.seq=[]
        self.Name=Name
        self.waiting=0
        self.translations=Translations

    def translate(self,Addr):
        if Addr[0] in '0123456789':
            return eval(Addr)
        if Addr in self.translations:
            return self.translations[Addr][0]
        print('cannot determine "%s" address'%Addr)
        return 0

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

        elif wrds[0]=='write':
            self.write(wrds[1],wrds[2])
        elif wrds[0]=='read':
            self.read(wrds[1])
        elif wrds[0]=='wait':
            self.wait(eval(wrds[1]))
        else:
            logs.log_info('AHB ACTION %s failed'%Txt)

    def wait(self,Wait):
        self.queue.append(('wait',Wait))

    def read(self,Addr):
        if type(Addr) is str:
            Addr = self.translate(Addr)
        self.queue.append(('read',Addr))



    def write(self,Addr,Data):
        if type(Addr) is str:
            Addr = self.translate(Addr)
        self.queue.append(('write',Addr,Data))
        
    def tr_peek(self,Sig):
        if  Sig in self.translations:
            Sig = self.translations[Sig]
        return self.peek(Sig)

    def run(self):
        if self.waiting>0:
            self.waiting -= 1
            return
        hreadyout = self.tr_peek('hreadyout')
        if hreadyout==0: return
        if self.seq!=[]:
            List = self.seq.pop(0)
            for (Sig,Val) in List:
                if  Sig in self.translations:
                    Sig = self.translations[Sig]
                if Sig=='wait':
                    self.waiting=int(Val)
                elif Sig=='catch':
                    X = self.peek(Val)
                    print('ahb read %s'%X)
                else:
                    self.force(Sig,Val)
            return

        if self.queue!=[]:
            What = self.queue.pop(0)
            if What[0]=='wait':
                self.seq.append([('wait',What[1])])
                return
            if What[0]=='burst':
                if What[2][0]=='w': HW=1
                else: HW = 0

                Burst = burstcode(What[1])

                self.seq.append([('hburst',Burst),('haddr',What[3]),('hwdata',0),('hwrite',HW),('htrans',NONSEQ),('hsize',2),('hsel',1),('hready',1)])
                for X in range(burstlen(What[1])):
                    self.seq.append([('hburst',Burst),('haddr',What[3]+4*X),('hwdata',0),('hwrite',HW),('htrans',SEQ),('hsize',2),('hsel',1),('hready',1)])
                
                self.seq.append([('hburst',0),('haddr',0),('hwdata',0),('hwrite',0),('htrans',IDLE),('hsize',0),('hsel',0),('hready',1)])


            if What[0]=='write':
                self.seq.append([('haddr',What[1]),('hwdata',0),('hwrite',1),('htrans',2),('hsize',2),('hsel',1),('hready',1)])
                self.seq.append([('wait',1)])
                self.seq.append([('haddr',0),('hwdata',What[2]),('hwrite',0),('htrans',0),('hsize',0),('hsel',0),('hready',1)])
                self.seq.append([('wait',5)])
                return

            if What[0]=='read':
                self.seq.append([('haddr',What[1]),('hwrite',0),('htrans',2),('hsel',1),('hready',1)])
                self.seq.append([('wait',1)])
                self.seq.append([('haddr',0),('hwrite',0),('htrans',0),('catch','hrdata'),('hsel',0),('hready',1)])
                self.seq.append([('wait',5)])
                return



