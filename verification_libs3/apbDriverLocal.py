

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
        self.uart = False
        self.Expected = {}
        self.Active = False

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
            self.Expected[self.eval(Addr)] = eval(Data)
        elif wrds[0] == 'read':
            Addr = wrds[1]
            Back = -1
            if len(wrds)>2: Back = wrds[1]
            self.Queue.append(('read',Addr,Back))
        elif wrds[0] == 'ram':
            Addr = self.eval(wrds[1])
            Addr += 0x1000
            Data = wrds[2]
            self.Queue.append(('write',hex(Addr),Data))
        else:
            logs.log_error('lib3 apbDriverLocal valid actions: (%s) skip fixstuff sbc crc ackdelim crcdelim dlc eof ' % Txt)


    def run(self):
        if self.reading>=0:
            if self.peek('xvalid') == 1:
                Rdata = self.peek('xrdata')
                logs.log_info("APBM %s %x %x" % (self.Prefix,self.reading,Rdata))
                self.Backs.append(('read',Rdata,self.reading))

                if (Rdata>=0) and (self.reading in self.Expected):
                    Exp = self.Expected[self.reading]
                    logs.log_ensure(Rdata == Exp,"Read Back from APB exp=0x%x act=0x%x addr=0x%x" % (Exp,Rdata,self.reading))
                self.reading = -1

        if self.Active:
            self.Active = False
            self.force('xread',0)
            self.force('xwrite',0)
            return
#        if self.peek('xidle') == 0: 
#            self.force('xread',0)
#            self.force('xwrite',0)
#            return

        if self.Queue == []: return
        Head =  self.Queue.pop(0)
        if Head[0] == 'write':
            if self.uart: self.uart(self.Nick,Head)
            logs.log_info("APBAA %s %s ad=%s da=%s" % (self.Nick,Head[0],Head[1],Head[2]))
            self.force('xwrite',1)
            self.force('xaddr',Head[1])
            self.force('xwdata',Head[2])
            self.Active = True
        elif Head[0] == 'read':
            if self.uart: self.uart(self.Nick,Head)
            logs.log_info("APBAA %s %s ad=%s" % (self.Nick,Head[0],Head[1]))
            self.force('xread',1)
            self.force('xaddr',Head[1])
            self.reading = self.eval(Head[1])
            self.Active = True



    def busy(self,Why=False):
        return False

