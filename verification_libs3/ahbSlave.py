
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

class ahbSlave(logs.driverClass):
    def __init__(self,Path,Monitors,Translations={},Name='noName'):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Path = Path
        self.Name=Name
        self.RAM = {}
        self.waiting=0
        self.translations=Translations
        self.hrdata = 0
        self.haddr = 0

    def translate(self,Addr):
        if Addr[0] in '0123456789':
            return eval(Addr)
        if Addr in self.translations:
            return self.translations[Addr][0]
        logs.log_error('cannot determine "%s" address'%Addr)
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

        elif wrds[0]=='size':
            self.HSIZE = eval(wrds[1])
        elif wrds[0]=='prot':
            self.HPROT = eval(wrds[1])
        elif wrds[0]=='write':
            self.write(wrds[1],wrds[2])
        elif wrds[0]=='read':
            self.read(wrds[1])
        elif wrds[0]=='wait':
            self.wait(eval(wrds[1]))
        else:
            logs.log_info('AHB ACTION %s failed'%Txt)




    def tr_peek(self,Sig):
        if  Sig in self.translations:
            Sig = self.translations[Sig]
        return self.peek(Sig)
    def tr_force(self,Sig,Val):
        if  Sig in self.translations:
            Sig = self.translations[Sig]
        return self.force(Sig,Val)

    def run(self):
        if self.waiting>0:
            self.waiting -= 1
            return
        if self.hrdata>=0:
            self.tr_force('hrdata',self.hrdata)
            logs.log_info('AHB slave %s :got read addr=%x data=%x'%(self.Name,self.haddr,self.hrdata))
            self.hrdata = -1
        self.tr_force('hready',1)
#        logs.log_info('>>>> hsel %d htrans %d hwrite %d haddr %x hwdata %x'%(self.tr_peek('hsel'),self.tr_peek('htrans'),self.tr_peek('hwrite'),self.tr_peek('haddr'),self.tr_peek('hwdata')))
        if (self.tr_peek('hsel')==1)and (self.tr_peek('htrans') in [SEQ,NONSEQ]):
            haddr  = self.tr_peek('haddr')
            hwrite  = self.tr_peek('hwrite')
            if (hwrite) :
                self.RAM[haddr] = self.tr_peek('hwdata')
                self.tr_force('hresp',0)
                self.haddr = haddr
                logs.log_info('AHB slave %s :got written addr=%x data=%x'%(self.Name,self.haddr,self.RAM[haddr] ))
                
            elif haddr in self.RAM:
                self.hrdata = self.RAM[haddr]
            else:
                self.hrdata = random.randint(0,0xffffffff)
                self.RAM[haddr] = self.hrdata







