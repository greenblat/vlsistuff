
import string
import logs
import veri
#import pdb
#import pudb
import random


class axiSlaveClass:
    def __init__(self,Path,Monitors,prefix='',suffix='',Name='slv no name'):
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
        self.wready = 0
        self.WAITREAD = 4
        self.WAITWRITE = 0
        self.busWidth = 8   # in bytes
        self.Passive = False

    def busy(self):
        if self.arqueue!=[]: return True
        if self.awqueue!=[]: return True
        if self.wqueue!=[]: return True
        if self.rqueue!=[]: return True
        if self.bqueue!=[]: return True
        if self.bqueue0!=[]: return True

        return False
    def busyWhy(self):
        logs.log_info('%s: SLV Busy ar=%d aw=%d w=%d r=%d b=%d b0=%d ' % (self.Name,len(self.arqueue),len(self.awqueue),len(self.wqueue),len(self.rqueue),len(self.bqueue),len(self.bqueue0)))
        if self.wqueue!=[]:
            logs.log_info('WQUEUE %x %x %x' % self.wqueue[0])
        if self.awqueue!=[]:
            logs.log_info('AWQUEUE %x %x %x %x %x' % self.awqueue[0])

    def peek(self,Sig):
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

    def action(self,Text):
        Wrds = Text.split()
        if Wrds == []:
            pass
        elif Wrds[0] == 'passive':
            self.Passive = True
        elif Wrds[0] == 'active':
            self.Passive = False
        elif Wrds[0] == 'write':
            Addr = eval(Wrds[1])
            logs.log_info('>>>>>>setWord %x %s'%(Addr,Wrds))
            for Wrd in Wrds[2:]:
                Data = eval(Wrd)
                logs.log_info('>>>>>>assWord %x %x'%(Addr,Data))
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
                Addr = self.addWord(Addr,int(Wrd,16))
        elif Wrds[0] == 'waitread':
            self.WAITREAD = int(Wrds[1])
        elif Wrds[0] == 'waitwrite':
            self.WAITWRITE = int(Wrds[1])
        elif Wrds[0] == 'buswidth':
            self.busWidth = int(Wrds[1])
        elif Wrds[0] == 'flood':
            Addr0 = eval(Wrds[1])
            Addr1 = eval(Wrds[2])
            Val   = eval(Wrds[3])
            for Add in range(Addr0,Addr1,4):
                self.addWord(Add,Val)
        else:
            logs.log_error('action of axiSlave "%s" failed on "%s"  %s' % (self.Name,Text,Wrds[0]))

                

    def addWord(self,Addr,Data):
        self.Ram[Addr] = Data & 0xff
        self.Ram[Addr+1] = (Data>>8) & 0xff
        self.Ram[Addr+2] = (Data>>16) & 0xff
        self.Ram[Addr+3] = (Data>>24) & 0xff
        if self.busWidth == 8:
            self.Ram[Addr+4] = (Data >>(8*4)) & 0xff
            self.Ram[Addr+5] = (Data >>(8*5))  & 0xff
            self.Ram[Addr+6] = (Data >>(8*6))  & 0xff
            self.Ram[Addr+7] = (Data >>(8*7))  & 0xff

        if self.busWidth == 16:
            self.Ram[Addr+8] = (Data >>(8*8)) & 0xff
            self.Ram[Addr+9] = (Data >>(8*9))  & 0xff
            self.Ram[Addr+10] = (Data >>(8*10))  & 0xff
            self.Ram[Addr+11] = (Data >>(8*11))  & 0xff
            self.Ram[Addr+12] = (Data >>(8*12))  & 0xff
            self.Ram[Addr+13] = (Data >>(8*13))  & 0xff
            self.Ram[Addr+14] = (Data >>(8*14))  & 0xff
            self.Ram[Addr+15] = (Data >>(8*15))  & 0xff


        logs.log_info('adding %x %x'%(Addr,Data))
        Addr += self.busWidth
        return Addr

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
        if self.rqueue==[]: 
            self.idleread()
            return
        if self.rqueue[0]=='pop':
            self.rqueue.pop(0)
            self.arqueue.pop(0)
            self.idleread()
            return
        if self.peek('rready')==0: 
            (rlast,rid,rdata) = self.rqueue[0]
            if rlast=='wait':
                self.waitread=1
                self.idleread()
            else:
                self.force('rvalid',1)
                self.force('rlast',rlast)
                self.force('rid',rid)
                self.force('rresp',0)
                self.force('rdata','0x'+rdata)
            return
        (rlast,rid,rdata) = self.rqueue.pop(0)
        if rlast=='wait':
            self.waitread=1
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
                
            LastAddr = (araddr + (arlen+1)*(1<<arsize))-1
            LastPage = LastAddr & 0xffffe000
            FirstPage = araddr & 0xffffe000
            if (FirstPage != LastPage):
                logs.log_error('slave %s CROSSING 4K read araddr=%x arlen=%x arsize=%x' % (self.Name,araddr,arlen,arsize))
                
    def readQueue(self,ii,burst,arsize,addr,rid,rlast):
        if (arsize>4): arsize = 4
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
        for ii in range(Incr):
            Add = Addr1 + ii
            if Add in self.Ram:
                AA = '%02x'%(self.Ram[Add])
                takenram += 1
            else:
                AA = '%02x'%(self.bytex)
                self.bytex = (self.bytex+1) & 0xff
            rdata = AA + rdata
        self.rqueue.append((rlast,rid,rdata))
        logs.log_info('axiSlave taken from ram %d bytes  rdata=%s addr=%08x rid=%x'%(takenram,rdata,Addr,rid))



    def writing(self):
        if self.Name == 'SLV0':
            veri.force('tb.marker0',str(self.awlen & 0xffff))
        if self.Name == 'SLV1':
            veri.force('tb.marker1',str(self.awlen & 0xffff))
        if self.Name == 'SLV2':
            veri.force('tb.marker2',str(self.awlen & 0xffff))
        if self.Name == 'SLV3':
            veri.force('tb.marker3',str(self.awlen & 0xffff))
#        logs.log_info('BVALID %s wait=%d bqueue=%s ready=%d' % (self.Name,self.bwaiting,self.bqueue,self.peek('bready')))
        if self.bwaiting>0:
            self.bwaiting -= 1
            self.force('bvalid',0)
        elif self.bqueue!=[]:
            bid,bresp = self.bqueue[0]
            if bid=='wait':
                self.bwaiting=int(bresp)
                self.force('bvalid',0)
                self.bqueue.pop(0)
            else:
                if self.peek('bready')==1: 
                    self.bqueue.pop(0)
                self.force('bid',bid)
                self.force('bresp',bresp)
                self.force('bvalid',1)
        else:
            self.force('bvalid',0)

        if len(self.awqueue)>1000:
            self.force('awready',1)
        elif self.Passive and (self.peek('awready')==0):
            pass
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
            if (FirstPage != LastPage):
                logs.log_error('slave %s CROSSING 4K write awaddr=%x awlen=%x awsize=%x' % (self.Name,awaddr,awlen,awsize))
            logs.log_info('axiSlave %s >>>awvalid %x %x %x %x %x'%(self.Name,awburst,awaddr,awlen,awid,awsize))
            self.bqueue0.append(awid)
        else:
            self.force('awready',1)

        self.force('wready',1)
        self.wready = 0

        if self.Passive and (self.peek('wready')==0):
            pass
        elif (self.peek('wvalid')==1)and(self.peek('wready') == 1):
            wstrb = self.peek('wstrb')
            wlast = self.peek('wlast')
            wdata = self.peek('wdata')
            self.wqueue.append((wdata,wlast,wstrb))
            logs.log_info('ADDWQUEUE %x %x %x' % (wdata,wlast,wstrb),self.Name)

        if len(self.wqueue) == 0: return    
        if (self.awlen<0) and (len(self.awqueue) == 0): return    
        if self.awlen<0:
            self.awburst,self.awaddr,self.awlen,self.wid,self.awsize = self.awqueue.pop(0)
        (wdata,wlast,wstrb) = self.wqueue.pop(0)
        logs.log_info('axiSlave %s write wstrb=%x wid=%x wlast=%d wlen=%d awaddr=%x burst=%d wdata=0x%x 0d%d'%(self.Name,wstrb,self.wid,wlast,self.awlen,self.awaddr,self.awburst,wdata,wdata),self.Name)
        for ii in range(16):
            if ((wstrb>>ii)&1)==1:
                Byte = (wdata>>(ii*8))& 0xff
                self.Ram[self.awaddr+ii]=Byte
#                    logs.log_info('axiSlave %s write to  ram %x '%(self.Name,self.awaddr+ii))
        self.awaddr += 1<<self.awsize
        if self.Passive and (self.peek('wready')==0):
            pass
        elif self.awlen==0:
            self.awlen = -1
            if wlast!=1:
                logs.log_error('axiSlave "%s" %s: prefix=%s addr=%x   no wlast wdata=%d'%(self.Name,self.Path,self.prefix,self.awaddr,wdata))
        else:
            self.awlen -= 1
            if (wlast==1):
                if self.awqueue!=[]: self.awqueue.pop(0)
                self.awlen = -1

        if (wlast==1):
#                logs.log_info('BQUEUE0 %s' % (self.bqueue0))
            self.bqueue.append(('wait',2))
            if self.bqueue0 == []:
                logs.log_error('axiSlave %s: BQUEUE0 is empty, more lasts than awvalids' % self.Name)
                self.bqueue0.append(0)
            self.bqueue.append((self.bqueue0.pop(0),0))
#                logs.log_info('BQUEUE %s' % (self.bqueue))


