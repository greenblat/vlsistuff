
import string
import logs
import veri
#import pdb
#import pudb
import random


class axiSlaveClass:
    def __init__(self,Path,Monitors,prefix='',suffix=''):
        self.Path = Path
        if self.Path != '':
            self.Path = self.Path + '.'
        if Monitors!= -1:
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
        self.prefix = prefix
        self.suffix = suffix
        self.Translates = {}
        self.Ram = {}
        self.wready = 0
        self.bvalid_armed = False
        self.WAITREAD = 4
        self.WAITWRITE = 0
        self.busWidth = 8   # in bytes

    def peek(self,Sig):
        if self.prefix!='': Sig = '%s%s'%(self.prefix,Sig)
        if self.suffix!='': Sig = '%s%s'%(Sig,self.suffix)
#        print('PEEK ',self.Path,Sig,Sig in self.Translates)
        if Sig in self.Translates: 
            Sig = self.Translates[Sig]
#        else:
#            print('PEEK NO %s %s'%(Sig,list(self.Translates.keys())))
        return logs.peek('%s%s'%(self.Path,Sig))

    def force(self,Sig,Val):
        if self.prefix!='': Sig = '%s%s'%(self.prefix,Sig)
        if self.suffix!='': Sig = '%s%s'%(Sig,self.suffix)
        if Sig in self.Translates: Sig = self.Translates[Sig]
        veri.force('%s%s'%(self.Path,Sig),str(Val))

    def action(self,Text):
        Wrds = Text.split()
        if Wrds == []:
            pass
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
            logs.log_error('action of axiSlave failed on "%s"  %s' % (Text,Wrds[0]))

                

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
                
            LastAddr = (araddr + (arlen+1)*(1<<arsize))-1
            LastPage = LastAddr & 0xffffe000
            FirstPage = araddr & 0xffffe000
            if (FirstPage != LastPage):
                logs.log_error('CROSSING 4K read araddr=%x arlen=%x arsize=%x' % (araddr,arlen,arsize))
                
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
#                logs.log_info('axiSlave addr in ram %x %s %d %s'%(Add,AA,Incr,rdata))
            else:
#                AA = '%02x'%(0xff)
                AA = '%02x'%(self.bytex)
                self.bytex = (self.bytex+1) & 0xff
#                logs.log_info('axiSlave addr not in ram %x %s %d %s'%(Add,AA,Incr,rdata))
            rdata = AA + rdata
        self.rqueue.append((rlast,rid,rdata))
        logs.log_info('axiSlave taken from ram %d bytes  rdata=%s addr=%08x rid=%x'%(takenram,rdata,Addr,rid))



    def writing(self):
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

        if len(self.awqueue)>4:
            self.force('awready',1)
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
                logs.log_error('CROSSING 4K write awaddr=%x awlen=%x awsize=%x' % (awaddr,awlen,awsize))
            logs.log_info('axiSlave >>>awvalid %x %x %x %x %x'%(awburst,awaddr,awlen,awid,awsize))

#        if self.wready>0:
#            self.wready -= 1
#            self.force('wready',1)
#        else:
#            self.wready = self.WAITWRITE
        self.force('wready',1)
        self.wready = 0
            
        if (self.peek('wvalid')==1)and((self.wready==self.WAITWRITE)):
            veri.force('tb.marker','0x77')
            if self.awlen<0:
                if len(self.awqueue)==0:
                    logs.log_error('axiSlave awqueue empty and wvalid is on')
                    self.awburst,self.awaddr,self.awlen,self.wid,self.awsize = -1,-1,-1,-1,0
                else:
                    self.awburst,self.awaddr,self.awlen,self.wid,self.awsize = self.awqueue.pop(0)
#            logs.log_info('axiSlave <<<<< awaddr=%x wready=%d awlen=%d '%(self.awaddr,self.wready,self.awlen))
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
                    logs.log_error('axiSlave %s: prefix=%s addr=%x   no wlast'%(self.Path,self.prefix,self.awaddr))
            else:
                self.awlen -= 1

            if (wlast==1)and(not self.bvalid_armed):
                self.bqueue.append(('wait',10))
                self.bqueue.append((self.wid,0))
                self.bvalid_armed = True
        if (self.bvalid_armed):               
            wlast = self.peek('wlast')
            if (wlast==0): 
                self.bvalid_armed = False



