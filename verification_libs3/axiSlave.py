
import string
import logs
import veri
#import pdb
#import pudb
import random


class axiSlaveClass:
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
        (rlast,rid,rdata) = self.rqueue.pop(0)
        if rlast=='wait':
            self.waitread=rid
            logs.log_info('axiSlave waitread %s'%rid)
            self.idleread()
            return

        self.force('rvalid',1)
        self.force('rlast',rlast)
        self.force('rid',rid)
        self.force('rresp',0)
        self.force('rdata','0x'+rdata)


    def idleread(self):
        self.force('rvalid',0)
        self.force('rlast',0)
        self.force('rdata',0)

    def reading(self):
        if len(self.arqueue)>4:
            self.force('arready',0)
        elif self.peek('arvalid')==1:
            self.force('arready',1)
            arid=self.peek('arid')
            arburst=self.peek('arburst')
            araddr=self.peek('araddr')
            arlen=self.peek('arlen')
            arburst=self.peek('arburst')
            arsize=self.peek('arsize')
            self.arqueue.append((arburst,araddr,arlen,arburst,arsize))
            self.rqueue.append(('wait',self.WAITREAD,0))
            for ii in range(arlen):
                self.readQueue(ii,arburst,arsize,araddr,arid,0)
            self.readQueue(arlen,arburst,arsize,araddr,arid,1)
            self.rqueue.append('pop')
                
                
    def readQueue(self,ii,burst,arsize,addr,rid,rlast):
        Incr = 1<<arsize
        Mask = ~((1<<arsize)-1)
        if burst==0:
            Addr = addr
        else:
            Addr = ii*Incr + addr
        Addr1 = Addr & Mask 
        if Addr1!=Addr:
            logs.log_warning('axiSlave read address is not aligned size=%d addrin=%08x'%(arsize,Addr))
        rdata = ''
        takenram = 0
        for ii in range(16):
            Add = Addr1 + ii
            if Add in self.Ram:
                AA = '%02x'%(self.Ram[Add])
                takenram += 1
#                logs.log_info('axiSlave addr in ram %x '%(Add))
            else:
#                AA = '%02x'%(0xff)
                AA = '%02x'%(self.bytex)
                self.bytex += 1
#                logs.log_info('axiSlave addr not in ram %x '%(Add))
            rdata = AA + rdata
        self.rqueue.append((rlast,rid,rdata))
        logs.log_info('axiSlave taken from ram %d bytes  rdata=%s addr=%08x'%(takenram,rdata,Addr))



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
                    self.force('bid',bid)
                    self.force('bresp',bresp)
                    self.force('bvalid',1)
        else:
            self.force('bvalid',0)

        if len(self.awqueue)>4:
            self.force('awready',0)
        elif self.peek('awvalid')==1:
            self.force('awready',1)
            awburst=self.peek('awburst')
            awid=self.peek('awid')
            awaddr=self.peek('awaddr')
            awlen=self.peek('awlen')
            awburst=self.peek('awburst')
            awsize=self.peek('awsize')
            self.awqueue.append((awburst,awaddr,awlen,awid,awsize))
            logs.log_info('axiSlave >>>awvalid %x %x %x %x %x'%(awburst,awaddr,awlen,awid,awsize))

        if self.wready>0:
            self.wready -= 1
            self.force('wready',0)
        else:
            self.wready = 5
            self.force('wready',1)
            
        if (self.peek('wvalid')==1)and((self.wready==5)):
            logs.log_info('axiSlave <<<<< wready=%d awlen=%d '%(self.wready,self.awlen))
            veri.force('tb.marker','0x77')
            if self.awlen<0:
                if len(self.awqueue)==0:
                    logs.log_error('axiSlave awqueue empty and wvalid is on')
                else:
                    self.awburst,self.awaddr,self.awlen,self.wid,self.awsize = self.awqueue.pop(0)
            wstrb = self.peek('wstrb')
            wlast = self.peek('wlast')
            wdata = self.peek('wdata')
            logs.log_info('axiSlave write wstrb=%x wid=%x wlast=%d wlen=%d awaddr=%x burst=%d wdata=%x'%(wstrb,self.wid,wlast,self.awlen,self.awaddr,self.awburst,wdata))

            for ii in range(16):
                if ((wstrb>>ii)&1)==1:
                    Byte = (wdata>>(ii*8))& 0xff
                    self.Ram[self.awaddr+ii]=Byte
#                    logs.log_info('axiSlave write to  ram %x '%(self.awaddr+ii))
            self.awaddr += 1<<self.awsize
            if self.awlen==0:
                self.awlen = -1
                if wlast!=1:
                    logs.log_error('axislave %s: %s   no last'%(self.Path,self.Prefix))
            else:
                self.awlen -= 1

            if (wlast==1)and(not self.bvalid_armed):
                self.bqueue.append(('wait',random.randint(50,100)))
                self.bqueue.append((self.wid,0))
                self.bvalid_armed = True
        if (self.bvalid_armed):               
            wlast = self.peek('wlast')
            if (wlast==0): 
                self.bvalid_armed = False



