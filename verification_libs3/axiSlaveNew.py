import logs
import veri
import random

class axiSlaveClass:
    def __init__(self,Path,Monitors,prefix='',suffix='',Name='axiSlave'): 
        self.Path = Path
        self.Name = Name
        self.prefix = prefix
        self.suffix = suffix
        self.Translates = {}
        Monitors.append(self)

        self.Ram = {}
        self.arqueue=[]
        self.awqueue=[]
        self.wqueue=[]
        self.rqueue=[]
        self.awlen = -1
        self.wid = -1
        self.abqueue = []
        self.bqueue = []

        self.keepW = 0
        self.keepAw = 0
        self.keepAr = 0
        self.delayAw = 100
        self.delayAr = 100
        self.delayW = 100
        self.waitread = 0
        self.bwaiting = 0

        R = self.peekbin('rdata')
        self.busWidth = len(R)//8
        self.read_data_generator = None
        self.verbose = False
        self.bytex = 1
        self.errorReadFromUnknown = False

    def peekbin(self,Sig):
        Orig = Sig
        if self.prefix!='': Sig = '%s%s'%(self.prefix,Sig)
        if self.suffix!='': Sig = '%s%s'%(Sig,self.suffix)
        if Sig in self.Translates:
            Sig = self.Translates[Sig]
        return veri.peek('%s.%s'%(self.Path,Sig))
    def peek(self,Sig):
        Orig = Sig
        if self.prefix!='': Sig = '%s%s'%(self.prefix,Sig)
        if self.suffix!='': Sig = '%s%s'%(Sig,self.suffix)
        if Sig in self.Translates:
            Sig = self.Translates[Sig]
        return logs.peek('%s.%s'%(self.Path,Sig))

    def force(self,Sig,Val):
        if self.prefix!='': Sig = '%s%s'%(self.prefix,Sig)
        if self.suffix!='': Sig = '%s%s'%(Sig,self.suffix)
        if Sig in self.Translates: Sig = self.Translates[Sig]
        veri.force('%s.%s'%(self.Path,Sig),str(Val))

    def action(self,Txt,Orig):
        logs.log_info("no action %s" % Txt)
        return


    def onFinish(self):
        if self.busy(): self.busyWhy();

    def busy(self):
        if self.arqueue!=[]: return True
        if self.awqueue!=[]: return True
        if self.wqueue!=[]: return True
        if self.rqueue!=[]: return True
        if self.bqueue!=[]: return True
        if self.abqueue!=[]: return True
        return False


    def keepValids(self):
        logs.force('tb.marker0',self.keepAw+5)
        logs.force('tb.marker1',self.keepW+5)
        if self.keepAw!= 0:
            self.keepAw -= 1 
            if self.keepAw == 0:
                self.force('awready',1)
        else:
            if self.peek('awvalid') == 1:
                self.keepAw = self.delayAw 
            if self.delayAw == 0:
                self.force('awready',1)
            else:
                self.force('awready',0)
                
        if self.keepAr!= 0:
            self.keepAr -= 1 
            if self.keepAr == 0:
                self.force('arready',1)
        else:
            if self.peek('arvalid') == 1:
                self.keepAr = self.delayAr 
            if self.delayAr == 0:
                self.force('arready',1)
            else:
                self.force('arready',0)

        
        if self.keepW!= 0:
            self.keepW -= 1 
            if self.keepW == 0:
                self.force('wready',1)
        else:
            if self.peek('wvalid') == 1:
                self.keepW = self.delayW 

            if self.delayW == 0:
                self.force('wready',1)
            else:
                self.force('wready',0)

    def run(self):
        self.keepValids()
        self.reading()
        self.writing()
        self.runbqueue()
        self.sendrqueue()

    def reading(self):
        if self.peek('arvalid')==1:
            arid=self.peek('arid')
            arburst=self.peek('arburst')
            araddr=self.peek('araddr')
            arlen=self.peek('arlen')
            arsize=self.peek('arsize')
            if self.peek('arready') == 1:
                self.arqueue.append((arburst,araddr,arlen,arsize))

                self.rqueue.append(('wait',10,0,0))
                for ii in range(arlen):
                    self.readQueue(arlen,ii,arburst,arsize,araddr,arid,0)
                self.readQueue(arlen,arlen,arburst,arsize,araddr,arid,1)
                self.rqueue.append('pop')


    def readQueue(self,arlen,ii,burst,arsize,addr,rid,rlast):
        Incr = 1<<arsize
        Mask = ~((1<<arsize)-1)
        Mask2 = ((1<<arsize)-1)
        if burst==0:
            Addr = addr
        elif burst==1:
            Addr = ii*Incr + addr
        elif burst==2:
            Len = (arlen+1) * (1<<arsize)
            Maskw = ~(Len-1)
            Maskw2 = (Len-1)
            Base = addr & Maskw
            Addr = ii*Incr + addr
            Pos = Addr &  Maskw2
            Addr =  Base + Pos
        else:
            logs.log_error('BURST %s' % burst)
            Addr = addr

        Addr1 = Addr & Mask 
        if Addr1!=Addr:
            logs.log_warning('axiSlave read address is not aligned size=%d addrin=%08x'%(arsize,Addr))
        if self.read_data_generator is None:
            rdata = ''
            takenram = 0
            for jj in range(Incr):
                Add = Addr1 + jj
                if Add in self.Ram:
                    AA = '%02x'%(self.Ram[Add])
                    takenram += 1
                else:
                    AA = '%02x'%(self.bytex)
                    if self.errorReadFromUnknown:
                        logs.log_error("READING FROM UN INIT RAM address=%x" % Add)
                    self.bytex = (self.bytex+1) & 0xff
                rdata = AA + rdata
                logs.log_info(
                'axiSlave taken from ram %d bytes  rdata=%s addr=%08x rid=%x burst=%d arlen=%d' % (takenram, rdata, Addr, rid,burst,arlen),verbose=self.verbose)
        else:
            rdata = self.read_data_generator(Addr1)
            rdata = hex(rdata)[2:]
            logs.log_info(f'[{self.Name}]: reading data from read data generator function rdata = 0x{rdata}, ',verbose=self.verbose)
        self.rqueue.append((rlast,rid,rdata,Addr))

    def idleread(self):
        self.force('rvalid',0)
        self.force('rlast',0)
        self.force('rdata',0)



    def sendrqueue(self):
        if self.waitread>0:
            self.waitread -= 1
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
        if self.peek('rready')==0: 
            (rlast,rid,rdata,Addr) = self.rqueue[0]
            if rlast=='wait':
                self.waitread=1
                self.idleread()
            else:
                self.force('rvalid',1)
                self.force('rlast',rlast)
                self.force('rid',rid)
                self.force('rresp',self.rresp(Addr))
                self.force('rdata','0x'+rdata)
                logs.log_info('RDATA %s addr=%s rid=%d rlast=%d' % (rdata,Addr,rid,rlast),verbose=self.verbose)
            return
        (rlast,rid,rdata,Addr) = self.rqueue.pop(0)
        logs.log_info("RAXI len=%d rlast=%s rid=%s addr=%x" % (len(self.rqueue),rlast,rid,Addr),verbose=self.verbose)
        if rlast=='wait':
            self.waitread=1
            self.idleread()
            return
        self.force('rvalid',1)
        self.force('rlast',rlast)
        self.force('rid',rid)
        self.force('rresp',0)
        self.force('rdata','0x'+rdata)

    def runbqueue(self):
        if self.peek('awvalid') and self.peek('awready'):
            self.abqueue.append((self.peek('awid'),0))
        if self.peek('wvalid') and self.peek('wready') and self.peek('wlast'):
            AB = self.abqueue.pop()
            self.bqueue.append(AB)
            self.bwaiting = 10
        if self.bwaiting>0:
            self.bwaiting -= 1
            self.force('bvalid',0)
        elif self.bqueue!=[]:
            bid,bresp = self.bqueue[0]
            self.bqueue.pop(0)
            if type(bid) is not int: bid = bid[0]
            self.force('bid',bid)
            self.force('bvalid',1)
        elif self.peek('bready')==1:
            self.force('bvalid',0)

    def writing(self):
        if (self.peek('awvalid')==1)and(self.peek('awready')==1):
            awburst=self.peek('awburst')
            awid=self.peek('awid')
            awaddr=self.peek('awaddr')
            awlen=self.peek('awlen')
            awburst=self.peek('awburst')
            awsize=self.peek('awsize')
            self.awqueue.append((awburst,awaddr,awlen,awid,awsize))

        if (self.peek('wvalid')==1)and(self.peek('wready')==1):
            wstrb=self.peek('wstrb')
            wdata=self.peek('wdata')
            wlast=self.peek('wlast')
            self.wqueue.append((wdata,wlast,wstrb))



        if len(self.wqueue) == 0: return
        if (self.awlen<0) and (len(self.awqueue) == 0): return

        if self.awlen<0:
            self.awburst,self.awaddr,self.awlen,self.wid,self.awsize = self.awqueue.pop(0)


        (wdata,wlast,wstrb) = self.wqueue.pop(0)
        if (wlast==1):
            if self.awqueue!=[]: self.awqueue.pop(0)
            self.awlen = -1
        for ii in range(self.busWidth):
            if ((wstrb>>ii)&1)==1:
                Byte = (wdata>>(ii*8))& 0xff
                self.Ram[self.awaddr+ii]=Byte
        self.awaddr += 1<<self.awsize
        self.awlen -= 1






