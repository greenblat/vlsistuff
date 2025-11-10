
import string
import logs
import veri
#import pdb
#import pudb
import random


class axiSlaveClass:
    def __init__(self,Path,Monitors,prefix='',suffix='',Name='slv no name', busWidth = 8):
        self.Path = Path
        self.Name = Name
        if self.Path != '':
            self.Path = self.Path + '.'
        if Monitors!= -1:
            Monitors.append(self)
        self.arqueue=[]
        self.awqueue=[]
        self.wqueue=[]
        self.rqueue=[]
        self.awlen = -1
        self.wid = -1
        self.bqueue0=[]
        self.bqueue=[]
        self.waitread=0
        self.bwaiting=0
        self.bytex=0x30
        self.prefix = prefix
        self.suffix = suffix
        self.Translates = {}
        self.Fixed = {}
        self.Ram = {}
        self.RAM = self.Ram
        self.wready = 0
        self.WAITREAD = 500
        self.WAITWRITE = 0
        self.busWidth = busWidth
        self.Passive = False
        self.Starvation = False
        self.Initial = True
        self.badRresp =  0
        self.Awready = 1
        self.Arready = 1
        self.Arready_int = 1
        self.force('bid',0)
        self.force('rid',0)
        self.force('rresp',0)
        self.force('bresp',0)
        self.force('bvalid',0)
        self.read_data_generator = None
        self.verbose = False
        self.errorReadFromUnknown = False
        self.waitWready = 0
        self.was_arvalid  = 0

    def onFinish(self):
        if self.busy(): self.busyWhy();


    def busy(self):
#        print('SELF BUSY',self.arqueue!=[],self.awqueue!=[],self.wqueue,self.rqueue!=[],self.bqueue!=[],self.bqueue0!=[])
        if self.arqueue!=[]: return True
        if self.awqueue!=[]: return True
        if self.wqueue!=[]: return True
        if self.rqueue!=[]: return True
        if self.bqueue!=[]: return True
        if self.bqueue0!=[]: return True

        return False
    def busyWhy(self):
        logs.log_info('%s: SLV Busy ar=%d aw=%d w=%d r=%d b=%d b0=%d ' % (self.Name,len(self.arqueue),len(self.awqueue),len(self.wqueue),len(self.rqueue),len(self.bqueue),len(self.bqueue0)),verbose=self.verbose)
        if self.wqueue!=[]:
            logs.log_info('WQUEUE %x %x %x' % self.wqueue[0],verbose=self.verbose)
        if self.awqueue!=[]:
            logs.log_info('AWQUEUE %x %x %x %x %x' % self.awqueue[0],verbose=self.verbose)

    def peek(self,Sig):
        Orig = Sig
        if Sig in self.Fixed: return self.Fixed[Sig]
        if self.prefix!='': Sig = '%s%s'%(self.prefix,Sig)
        if self.suffix!='': Sig = '%s%s'%(Sig,self.suffix)
        if Sig in self.Translates: 
            Sig = self.Translates[Sig]
        
        return logs.peek('%s%s'%(self.Path,Sig))

    def force(self,Sig,Val):
        if self.Passive: return
        if self.prefix!='': Sig = '%s%s'%(self.prefix,Sig)
        if self.suffix!='': Sig = '%s%s'%(Sig,self.suffix)
        if Sig in self.Translates: Sig = self.Translates[Sig]
        veri.force('%s%s'%(self.Path,Sig),str(Val))

    def action(self,Text,Orig=[]):
        Wrds = Text.split()
        if Wrds == []:
            pass
        elif Wrds[0] == 'test':
            logs.log_info("TEST XXXXX %s" % Wrds,verbose=self.verbose)
        elif Wrds[0] == 'verbose':
            if Wrds[1] in ['yes','1','on']:
                self.verbose = True
            elif Wrds[1] in ['no','0','off']:
                self.verbose = False
            else:
                logs.log_error('verbose recognizes:  yes 1  or no 0')
        elif Wrds[0] == 'errorReadFromUnknown':
            if Wrds[1] in ['yes','1','on']:
                self.errorReadFromUnknown = True
            elif Wrds[1] in ['no','0','off']:
                self.errorReadFromUnknown = False
            else:
                logs.log_error('verbose recognizes:  yes 1  or no 0')

        elif Wrds[0] == 'awready':
            self.Awready = eval(Wrds[1])
            self.force('awready',self.Awready)
        elif Wrds[0] == 'arready':
            self.Arready = eval(Wrds[1])
            self.force('arready',self.Arready)
        elif Wrds[0] == 'rresp':
            self.badRresp = eval(Wrds[1])
            logs.log_info('BADRESP of slave set to %x' % self.badRresp,verbose=self.verbose)
        elif Wrds[0] == 'starvation':
            if Wrds[1] == 'on':
                self.Starvation = True
            elif Wrds[1] == 'off':
                self.Starvation = False
            else:
                logs.log_error('starvation gets only on / off , not "%s"' % Wrds[1])
        elif Wrds[0] == 'passive':
            self.Passive = True
        elif Wrds[0] == 'active':
            self.Passive = False
        elif Wrds[0] == 'write':
            Addr = eval(Wrds[1])
            for Wrd in Wrds[2:]:
                Data = eval(Wrd)
                Addr = self.addWord(Addr,Data)
        elif Wrds[0] == 'ramfile':
            File = open(Wrds[1])
            lines = File.readlines()
            File.close()
            Addr = 0
            for line in lines:
                wrds = line.split()
                for wrd in wrds:
                    if wrd[0]=='@':
                        Addr = int(wrd[1:],16)
                    else:
                        Addr = self.addWord(Addr,int(wrd,16))
        elif Wrds[0] == 'ram':
            Addr = eval(Wrds[1])
            for Wrd in Wrds[2:]:
                Addr = self.addWord(Addr,eval(Wrd))
        elif Wrds[0] == 'waitread':
            self.WAITREAD = eval(Wrds[1])
        elif Wrds[0] == 'waitwrite':
            self.WAITWRITE = eval(Wrds[1])
            logs.log_info("AXI_SLAVE: WAITWRITE = %d" % self.WAITWRITE,verbose=self.verbose)
        elif Wrds[0] == 'buswidth':
            self.busWidth = eval(Wrds[1])
        elif Wrds[0] == 'flood':
            Addr0 = eval(Wrds[1])
            Addr1 = eval(Wrds[2])
            Val   = eval(Wrds[3])
            for Add in range(Addr0,Addr1,4):
                self.addWord(Add,Val)
        elif Wrds[0] == 'fill_by_addr':
            Addr0 = eval(Wrds[1])
            Addr1 = eval(Wrds[2])
            for Addr in range(Addr0,Addr1,self.busWidth):
                self.addWord(Addr,Addr)
                logs.log_info("ADD %x %x" % (Addr,Addr),verbose=self.verbose)
        else:
            logs.log_error('action of axiSlave "%s" failed on "%s"  %s' % (self.Name,Text,Wrds[0]))

                

    def addWord(self,Addr,Data):
        for byte_idx in range(self.busWidth):
            self.Ram[Addr + byte_idx] = (Data >> 8*byte_idx) & 0xff

        logs.log_info('adding %x %x'%(Addr,Data),verbose=self.verbose)
        Addr += self.busWidth
        return Addr

    def run_a(self):   # run this nano before def run(self):
        if self.Initial:
            self.force('awready',self.Awready)
            self.force('wready',1)
            self.force('arready',self.Arready)
        if self.Starvation:
            self.force('awready',0)
            self.force('wready',0)
            self.force('arready',self.Arready)
            if self.peek('rready')==1: self.force('rvalid',0) 
            if self.peek('bready')==1: self.force('bvalid',0) 
            return
        if len(self.arqueue)>6:
            self.force('arready',0)
            self.Arready_int = 0
        else:
            self.force('arready',1)   # self.was_arvalid)
            self.was_arvalid = self.peek('arvalid')
            self.Arready_int = 1

    def run(self):
        if self.Initial:
            self.Initial = False
            self.force('bid',0)
            self.force('rid',0)
            self.force('rresp',0)
            self.force('bresp',0)
            self.force('bvalid',0)
            self.force('arready',0)
        if self.Starvation:
            return
        self.reading()
        self.writing()
        self.sendrqueue()
        self.runbqueue()

    def sendrqueue(self):
#         veri.force('tb.rqueuelen',hex(len(self.rqueue)))
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
        self.force('rresp',self.rresp(Addr))
        self.force('rdata','0x'+rdata)

    def rresp(self,Addr):
        logs.log_info(self.Name + ': RRESP bad=%x nowa=%x  %x   %s' % (self.badRresp , Addr,self.arqueue[0][1],self.arqueue[0]),verbose=self.verbose)
        if self.badRresp == Addr:
            return 2
        return 0

    def idleread(self):
        self.force('rvalid',0)
        self.force('rlast',0)
        self.force('rdata',0)




    def reading(self):

        Arready = self.Arready_int

        if self.peek('arvalid')==1:
            arid=self.peek('arid')
            arburst=self.peek('arburst')
            araddr=self.peek('araddr')
            arlen=self.peek('arlen')
            arsize=self.peek('arsize')
            if Arready == 1:
                self.arqueue.append((arburst,araddr,arlen,arsize))
                self.rqueue.append(('wait',self.WAITREAD,0,0))
                for ii in range(arlen):
                    self.readQueue(arlen,ii,arburst,arsize,araddr,arid,0)
                self.readQueue(arlen,arlen,arburst,arsize,araddr,arid,1)
                self.rqueue.append('pop')
                    
                LastAddr = (araddr + (arlen+1)*(1<<arsize))-1
                X =  (araddr + (arlen+1)*(1<<arsize))
                LastPage = LastAddr & 0xfffff000
                FirstPage = araddr & 0xfffff000
                if (FirstPage != LastPage):
                    logs.log_error('slave %s CROSSING 4K read araddr=%x arlen=%x arsize=%x X=%x  (la=%x lp=%x fp=%x)' % (self.Name,araddr,arlen,arsize,X,LastAddr,LastPage,FirstPage))
                
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

    def runbqueue(self):
#        logs.log_info("BVVV %s %s" % (self.bqueue0,self.bqueue))
        if self.peek('awvalid') and self.peek('awready'):
            self.bqueue0.append((self.peek('awid'),0))
#            logs.log_info("BV0")
        if self.peek('wvalid') and self.peek('wready') and self.peek('wlast'):
            AB = self.bqueue0.pop()
            self.bqueue.append(AB)
            self.bwaiting = 20
#            logs.log_info("BV1 %s" % str(self.bqueue))
        if self.bwaiting>0:
            self.bwaiting -= 1
            self.force('bvalid',0)
        elif self.bqueue!=[]:
            bid,bresp = self.bqueue[0]
            self.bqueue.pop(0)
#            logs.log_info("BID %s" % bid)
            if type(bid) is not int: bid = bid[0]
            self.force('bid',bid)
            self.force('bvalid',1)
        elif self.peek('bready')==1: 
            self.force('bvalid',0)

    def writing(self):
        if self.Name == 'SLV0':
            veri.force('tb.marker0',str(self.awlen & 0xffff))
        if self.Name == 'SLV1':
            veri.force('tb.marker1',str(self.awlen & 0xffff))
        if self.Name == 'SLV2':
            veri.force('tb.marker2',str(self.awlen & 0xffff))
        if self.Name == 'SLV3':
            veri.force('tb.marker3',str(self.awlen & 0xffff))
#        logs.log_info('WRITING bwait=%d %s %s' % (self.bwaiting, self.bqueue,self.bqueue0))
        if len(self.awqueue)>0:
            logs.log_info('AWQUEUE len=%d awvalid=%d awready=%d' % (len(self.awqueue),self.peek('awvalid'),self.Awready))
        if len(self.awqueue)>1000:
            logs.log_warning("AWQUEUE is very long")
            self.force('awready',self.Awready)
        elif self.Passive and (self.peek('awready')==0):
            pass
        elif self.Awready == 0:
            self.force('awready',0)
        elif (self.peek('awvalid')==1) and (len(self.awqueue)>=8):
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
            LastAddr = (awaddr + (awlen+1)*(1<<awsize))-1
            LastPage = LastAddr & 0xffffe000
            FirstPage = awaddr & 0xffffe000
            logs.log_info('PAGES first=%x last=%x   addr=%x lastad=%x' % (FirstPage,LastPage,awaddr,LastAddr))
            if (FirstPage != LastPage):
                logs.log_error('slave %s CROSSING 4K write awaddr=%x awlen=%x awsize=%x  (%x %x %x)' % (self.Name,awaddr,awlen,awsize,LastAddr,LastPage,FirstPage))
            logs.log_info('AxiSlave %s >>>awvalid %x %x %x %x %x'%(self.Name,awburst,awaddr,awlen,awid,awsize) ,verbose=self.verbose)
            self.bqueue0.append((awid,0))
            logs.log_info("BQUEUE0 APPEND %s" % str(self.bqueue0),verbose=True)
        else:
            self.force('awready',1)

        self.wready = 0
#        self.force('marker3',self.waitWready)
        if self.Passive and (self.peek('wready')==0):
            pass
        elif (self.waitWready>0):
            self.waitWready -= 1
            if self.waitWready==0: 
                self.force('wready',1)
            else:
                self.force('wready',0)
                return
        if (self.peek('wvalid')==1)and(self.waitWready==0):
            self.force('wready',1)
            wstrb = self.peek('wstrb')
            wlast = self.peek('wlast')
            wdata = self.peek('wdata')
            self.wqueue.append((wdata,wlast,wstrb))
#            logs.log_info('AXISLAVE0 %s written  wdata=%x wlast=%x wstrb=%x awlen=%d   que=%s' % (self.Name,wdata,wlast,wstrb,self.awlen,self.wqueue) ,verbose=self.verbose)
            self.waitWready = self.WAITWRITE

        if len(self.wqueue) == 0: return    
        if (self.awlen<0) and (len(self.awqueue) == 0): return    
        if self.awlen<0:
            self.awburst,self.awaddr,self.awlen,self.wid,self.awsize = self.awqueue.pop(0)
#        logs.log_info("AXISLAVE1 %s %s " % (self.waitWready,nicew(self.wqueue)),verbose=self.verbose)
        (wdata,wlast,wstrb) = self.wqueue.pop(0)
#        logs.log_info('AXISLAVE2 %s write wstrb=%x wid=%x wlast=%d wlen=%d awaddr=%x burst=%d wdata=0x%x 0d%d'%(self.Name,wstrb,self.wid,wlast,self.awlen,self.awaddr,self.awburst,wdata,wdata),self.Name ,verbose=True)
        for ii in range(self.busWidth):
            if ((wstrb>>ii)&1)==1:
                Byte = (wdata>>(ii*8))& 0xff
                self.Ram[self.awaddr+ii]=Byte
#                    logs.log_info('axiSlave %s write to  ram %x '%(self.Name,self.awaddr+ii) ,verbose=self.verbose)
        self.awaddr += 1<<self.awsize
        if self.Passive and (self.peek('wready')==0):
            pass
        elif self.awlen==0:
            self.awlen = -1
            if wlast!=1:
                logs.log_error('axiSlave "%s" %s: prefix=%s addr=%x   no wlast wdata=%d'%(self.Name,self.Path,self.prefix,self.awaddr,wdata) ,verbose=self.verbose)
        else:
            self.awlen -= 1
            if (wlast==1):
                if self.awqueue!=[]: self.awqueue.pop(0)
                self.awlen = -1

        if (wlast==1):
            logs.log_info('BQUEUE0 %s' % (self.bqueue0),verbose=self.verbose)
            self.bqueue.append(('wait',30))
            if self.bqueue0 == []:
                logs.log_error('axiSlave %s: BQUEUE0 is empty, more lasts than awvalids' % self.Name)
                self.bqueue0.append(0)
            self.bqueue.append((self.bqueue0.pop(0),0))
            logs.log_info('BQUEUE %s' % (self.bqueue),verbose=self.verbose)

def nicew(Queue):
    res = []
    for A,B,C in Queue:
        Str = '(%x,%x,%x)' % (A,B,C)
        res.append(Str)
    return ''.join(res)


def prqueue(Queue):
    Str = '%d ' % len(Queue)
    for Obj in Queue:
        try:
            (rlast,rid,rdata,Addr) = Obj
            Now  = ' %s.%s.%s.0x%x' % (rlast,rid,rdata,Addr)
        except:
            Now  = ' %s' % str(Obj)
        Str += Now
    return Str
