
import string
import logs
import veri
#import pdb
#import pudb
import random

class axiLiteSlaveClass:
    def __init__(self,Path,Monitors,Prefix='',Suffix=''):
        self.Path = Path
        Monitors.append(self)
        self.arqueue=[]
        self.awqueue=[]
        self.rqueue=[]
        self.awlen = -1
        self.wid = -1
        self.bqueue=[]
        self.waitread=0
        self.bwaiting=0
        self.bytex=0x30
        self.Prefix = Prefix
        self.Suffix = Suffix
        self.Translates = {}
        self.Ram = {}
        self.wready = 0
        self.bvalid_armed = False
        self.WAITREAD = 4

    def peek(self,Sig):
        if self.Prefix!='': Sig = '%s%s'%(self.Prefix,Sig)
        if self.Suffix!='': Sig = '%s%s'%(Sig,self.Suffix)
        if Sig in self.Translates: Sig = self.Translates[Sig]
        return logs.peek('%s.%s'%(self.Path,Sig))

    def force(self,Sig,Val):
        if self.Prefix!='': Sig = '%s%s'%(self.Prefix,Sig)
        if self.Suffix!='': Sig = '%s%s'%(Sig,self.Suffix)
        if Sig in self.Translates: Sig = self.Translates[Sig]
        veri.force('%s.%s'%(self.Path,Sig),str(Val))

    def run(self):
#        pudb.set_trace()
        self.reading()
        self.writing()
        self.sendrqueue()

    def sendrqueue(self):
        if self.waitread>0:
            self.waitread -= 1
            self.idleread()
            return
        if self.peek('rready')==0: 
            self.idleread()
            return
        if self.rqueue==[]: 
            self.idleread()
            return
        if self.rqueue[0]=='pop':
            self.rqueue.pop(0)
            self.arqueue.pop(0)
            self.idleread()
            return
        rdata = self.rqueue.pop(0)
        if rdata=='wait':
            self.waitread=5
            self.idleread()
            return

        self.force('rvalid',1)
        self.force('rresp',0)
        self.force('rdata','0x'+rdata)


    def idleread(self):
        self.force('rvalid',0)
        self.force('rdata',0)

    def reading(self):
        if len(self.arqueue)>4:
            self.force('arready',0)
        elif self.peek('arvalid')==1:
            self.force('arready',1)
            araddr=self.peek('araddr')
            self.arqueue.append((araddr))
            self.rqueue.append(('wait',self.WAITREAD,0))
            self.readQueue(araddr,1)
            self.rqueue.append('pop')
                
                
    def readQueue(self,ii,addr):
        Addr = addr
        Addr1 = Addr & Mask 
        if Addr1!=Addr:
            logs.log_warning('axiSlave %s%s read address is not aligned addrin=%08x'%(self.Prefix,self.Suffix,Addr))
        rdata = ''
        takenram = 0
        for ii in range(16):
            Add = Addr1 + ii
            if Add in self.Ram:
                AA = '%02x'%(self.Ram[Add])
                takenram += 1
#                logs.log_info('axiSlave %s%s addr in ram %x '%(self.Prefix,self.Suffix,Add))
            else:
#                AA = '%02x'%(0xff)
                AA = '%02x'%(self.bytex)
                self.bytex += 1
#                logs.log_info('axiSlave %s%s addr not in ram %x '%(self.Prefix,self.Suffix,Add))
            rdata = AA + rdata
        self.rqueue.append(rdata)
        logs.log_info('axiSlave %s%s taken from ram %d bytes  rdata=%s addr=%08x'%(self.Prefix,self.Suffix,takenram,rdata,Addr))



    def writing(self):
        if self.bwaiting>0:
            self.bwaiting -= 1
            self.force('bvalid',0)
        elif self.bqueue!=[]:
            if self.peek('bready')==0: 
                self.force('bvalid',0)
            else:
                bid,bresp = self.bqueue.pop(0)
                if bid=='wait':
                    self.bwaiting=int(bresp)
                    self.force('bvalid',0)
                else:
                    self.force('bresp',bresp)
                    self.force('bvalid',1)
        else:
            self.force('bvalid',0)

        if len(self.awqueue)>4:
            self.force('awready',0)
        elif self.peek('awvalid')==1:
            self.force('awready',1)
            awaddr=self.peek('awaddr')
            self.awqueue.append(awaddr)
            self.awaddr = awaddr

        if self.wready>0:
            self.wready -= 1
            self.force('wready',0)
        else:
            self.wready = 5
            self.force('wready',1)
            
        if (self.peek('wvalid')==1)and((self.wready==5)):
            logs.log_info('axiSlave %s%s <<<<< wready=%d '%(self.Prefix,self.Suffix,self.wready))
            veri.force('tb.marker','0x77')
            wstrb = self.peek('wstrb')
            wdata = self.peek('wdata')
            logs.log_info('axiSlave %s%s write wstrb=%x awaddr=%x wdata=%x'%(self.Prefix,self.Suffix,wstrb,self.awaddr,wdata))

            for ii in range(16):
                if ((wstrb>>ii)&1)==1:
                    Byte = (wdata>>(ii*8))& 0xff
                    self.Ram[self.awaddr+ii]=Byte
#                    logs.log_info('axiSlave %s%s write to  ram %x '%(self.Prefix,self.Suffix,self.awaddr+ii))

            if (not self.bvalid_armed):
                self.bqueue.append(('wait',random.randint(50,100)))
                self.bqueue.append((self.wid,0))
                self.bvalid_armed = True
                return
        if (self.bvalid_armed):               
                self.bvalid_armed = False



