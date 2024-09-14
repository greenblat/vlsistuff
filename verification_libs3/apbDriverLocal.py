

import logs
import random


class apbDriverLocal(logs.driverClass):
    def __init__(self,Path,Monitors,Prefix,Nickname):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Queue = []
        self.reading = -1
        self.Prefix = Prefix
        self.Nick = Nickname
        self.Backs = []

    def onFinish(self):
        return

    def read(self,Addr):
        self.Queue.append(('read',Addr,-1))
    def write(self,Addr,Data):
        self.Queue.append(('write',Addr,Data))
    def action(self,Txt,Origs=[]):
        wrds = Txt.split()
        if wrds==[]:
            pass
        elif wrds[0] == 'write':
            Addr = wrds[1]
            Data = wrds[2]
            self.Queue.append(('write',Addr,Data))
        elif wrds[0] == 'read':
            Addr = wrds[1]
            Back = -1
            if len(wrds)>2: Back = wrds[1]
            self.Queue.append(('read',Addr,Back))
        else:
            logs.log_error('valid actions: skip fixstuff sbc crc ackdelim crcdelim dlc eof ')


    def run(self):
        if self.reading>=0:
            if self.peek('xvalid') == 1:
                logs.log_info("APBM %s %x %x" % (self.Prefix,self.reading,self.peek('xrdata')))
                self.Backs.append(('read',self.peek('xrdata'),self.reading))
                self.reading = -1

        if self.peek('xidle') == 0: 
            self.force('xread',0)
            self.force('xwrite',0)
            return

        if self.Queue == []: return
        Head =  self.Queue.pop(0)
        if Head[0] == 'write':
            self.force('xwrite',1)
            self.force('xaddr',Head[1])
            self.force('xwdata',Head[2])
        elif Head[0] == 'read':
            self.force('xread',1)
            self.force('xaddr',Head[1])
            self.reading = self.eval(Head[1])



    def busy(self,Why=False):
        return False

