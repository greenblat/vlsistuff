
import string
import logs
import veri


class spiMaster:
    def __init__(self,Path,Monitors):
        Monitors.append(self)
        self.Queue = []
        self.Path = Path
        self.iq = []
        self.waiting=0

    def peek(self,Sig):
        Sig = self.rename(Sig)
        return logs.peek('%s.%s'%(self.Path,Sig))
    def bpeek(self,Sig):
        Sig = self.rename(Sig)
        return veri.peek('%s.%s'%(self.Path,Sig))
    def force(self,Sig,Val):
        Sig = self.rename(Sig)
        veri.force('%s.%s'%(self.Path,Sig),str(Val))
    def rename(self,Sig):
        return Sig


    def send(self,Str):
        LL = string.split(Str)
        for Item in LL:
            if Item[0] in '123456789':
                Byte = eval(Item)
                self.sendByte(Byte)
            elif Item == '||':
                self.Queue.append('||')
            elif Item == '0':
                Byte = 0
                self.sendByte(Byte)
            elif Item[0]=='0':
                if Item[:2]=='0x':
                    Byte = eval(Item)
                    self.sendByte(Byte)
                elif Item[:2]=='0b':
                    L1 = list(Item[2:])
#                    L1.reverse()
                    self.Queue.extend(L1)
            else:
                Byte = ord(Item[0])
                self.sendByte(Byte)

    def sendByte(self,Byte):
        print('sendByte',hex(Byte))
        Bin = logs.binx(Byte,8)
        L1 = list(Bin)
#        L1.reverse()
        self.Queue.extend(L1)

    def run(self):
        if self.waiting>0:
            self.waiting -= 1
            return
        if self.iq!=[]:
            clk,din,csn = self.iq.pop(0)
            if clk=='wait':
                self.waiting = din
                return
            self.force('spi_ss',csn)
            self.force('spi_mosi',din)
            self.force('spi_clk',clk)
            return

        if self.Queue==[]: 
            return
        while self.Queue!=[]:
            Bit = self.Queue.pop(0)
            if Bit=='||':
                self.iq.append((1,0,0))
                self.iq.append((1,0,0))
                self.iq.append((1,0,0))
                self.iq.append((1,0,1))
                self.iq.append((1,0,1))
                self.iq.append((1,0,1))
                self.iq.append(('wait',10,0))
            else:
                self.iq.append((0,Bit,0))
                self.iq.append((0,Bit,0))
                self.iq.append((0,Bit,0))
                self.iq.append((1,Bit,0))
                self.iq.append((1,Bit,0))
                self.iq.append((1,Bit,0))
        self.iq.append((1,0,0))
        self.iq.append((1,0,0))
        self.iq.append((1,0,0))
        self.iq.append((0,0,0))
        self.iq.append((0,0,0))
        self.iq.append((0,0,0))
        self.iq.append((0,0,1))
        self.iq.append(('wait',10,0))
            

