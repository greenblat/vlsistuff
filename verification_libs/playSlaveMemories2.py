import os,sys,string
import veri
import logs    
import random

SLAVE_RAM_SIZE = 0
DELAY = 0
VERSION = 'verification_libs/playSlaveMemories2.py 16may2018'


def invent0(Addr):
    Now = (Addr >> 24) & 0xff 
    return Now

SEQ = 0
def invent1(Addr):
    global SEQ
    SEQ += 1
    if SEQ==0: SEQ=1
    return SEQ

byByte = True
byAddr = False

class memoryClass:
    def __init__(self,Size,Which,Monitors):
        self.Size = Size # 0-byte, 1-16bits, 2-32bits, 3-64, 4-128
        self.DDD = 16
        self.Path = 'tb'
        self.Ram={}
        self.local_rd = 0
        self.delay_wr=0
        self.Which=Which
        Monitors.append(self)
        logs.log_info('memoryClass class taken from %s'%VERSION)

    def finish(self):
        return
    def force(self,Sig,Val):
        veri.force('%s.%s%s'%(self.Path,Sig,self.Which),str(Val))
    def peek(self,Sig):
        return logs.peek('%s.%s%s'%(self.Path,Sig,self.Which))

    def report(self):
        Addr = self.Ram.keys()
        Addr.sort()
        First = (Addr[0] & 0xfffffff0)
        Ofile = open('ram.report','w')
        logs.log_info('reporting ram from %x to %x'%(First,Addr[-1]))
        for aa in range(First,Addr[-1]+1):
            if (aa & 0xf)==0:
                Ofile.write('\n   ram %08x : '%aa)
            if (aa & 0xf)==8:
                Ofile.write('  ')
            if aa in self.Ram:
                Ofile.write('%02x '%self.Ram[aa])
            else:
                Ofile.write('%2s '%'.')
        Ofile.write('\n\n\n')
        Ofile.close()


    def init(self,Addr0,Bytes,Start=0):
        for ii in range(Addr0,Addr0+Bytes):
            self.Ram[ii]= 0xff & (Start+ii-Addr0)
            
    def run(self):
        if self.local_rd:
            self.local_rd=0
            self.force('s_local_rd_data',self.rdata)
            self.force('s_local_rd_data_ok',1)
        else:
            self.force('s_local_rd_data_ok',0)

        if (self.delay_wr>0):
            self.force('s_local_wr_ok','0')
            self.delay_wr -= 1
        elif self.peek('s_local_wr')==1:
            self.writing()
            self.force('s_local_wr_ok','1')
            self.delay_wr = DELAY
        else: 
            self.force('s_local_wr_ok','0')
        if self.peek('s_local_rd')==1:
            self.reading()

    def writing(self):
        addr  = self.peek('s_local_wr_addr')
        wdata = self.peek('s_local_wr_data')
        wstrb = self.peek('s_local_wstrb')
        bytes = 1<<self.Size
        for ii in range(bytes+1):
            if (wstrb & (1<<ii))!=0:
                data = 0xff & (wdata>>(ii*8))
                self.Ram[addr+ii] = data
                logs.log_info('slaveRam write %x <- %02x'%(addr+ii,data))

    def reading(self):
        addr  = self.peek('s_local_rd_addr')
        bytes = 1<<self.Size
        mask0 = bytes-1
        addr  = addr & ~mask0
        Res=0
        for ii in range(bytes+1):
            if (addr+ii) in self.Ram:
                Byte = self.Ram[addr+ii]
            elif (byAddr):
                Byte = invent0(addr+ii)
                self.Ram[addr+ii] = Byte
            elif (byByte):
                Byte = invent1(addr+ii)
                self.Ram[addr+ii] = Byte
            else:
                Byte = random.randint(0,255)
                self.Ram[addr+ii] = Byte
            Res |= (Byte<<(ii*8))
        self.rdata = Res
        self.force('s_local_rd_addr_ok','1')
        self.local_rd = 1

