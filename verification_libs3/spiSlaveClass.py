

import logs
import veri
import sys,random,os
TB = 'tb'
class spiSlaveClass(logs.driverClass):
    def __init__(self,Path,Monitors,Freq=1,Renames={}):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Renames = Renames
        self.Bytes = []
        self.Rcv = 0
        self.rcvPos = 0
        self.was_sck = 1
    def callback(self,Txt):
        return Txt
    def force(self,Sig,Val):
        if Sig in self.Renames: Sig = self.Renames[Sig]
        logs.driverClass.force(self,Sig,Val)

    def peek(self,Sig):
        if Sig in self.Renames: Sig = self.Renames[Sig]
        return logs.driverClass.peek(self,Sig)

    def idle(self):
        return True
    def busy(self):
        return not self.idle()

    def action(self,Txt):
        wrds = Txt.split()
        Cmd = wrds[0]
        if Cmd == 'add':
            for Byte in wrds[1:]:
                self.Bytes.append(eval(Byte))

    def run(self):
        now = self.peek('spi_sck') 
        NegEdge = False
        PosEdge = False
        if (now == 1)and(self.was_sck == 0):
            PosEdge = True
        elif (now == 0)and(self.was_sck == 1):
            NegEdge = True

        self.was_sck = now

        if self.state == 'idle':
            if '0' in self.peekbin('spi_csn'):
                self.state = 'work'
                self.SCK = self.peek('spi_sck')
                self.Pos = 7
                self.force('spi_miso',(self.Bytes[0]>>self.Pos) & 1)
        elif self.state == 'work':
            if '0' not in self.peekbin('spi_csn'):
                self.state = 'idle'
                logs.log_info('DESELECTED %d %02x' % (self.rcvPos,self.Rcv))
                return
            if NegEdge:
                if self.Bytes == []:
                    self.Bytes.append(random.randint(0,225))
                self.force('spi_miso',(self.Bytes[0]>>self.Pos) & 1)
                self.Pos -= 1
                if self.Pos <0 :
                    self.Pos = 7
                    self.Bytes.pop(0)
            elif PosEdge:
                self.Rcv = self.Rcv*2 + self.peek('spi_mosi')
                self.rcvPos += 1
                if self.rcvPos == 8:
                    logs.log_info('SLAVE SPI got %02x' % self.Rcv)
                    self.rcvPos = 0
                    self.Rcv = 0
            



def reverseBin(Txt):
    List = list(Txt)
    List.reverse()
    Str = ''.join(List)
    return Str

