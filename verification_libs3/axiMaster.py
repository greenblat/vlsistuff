
DEMO = '''

BURST: 0 - fixed, 1- incremtning 2-wrapping

axi = axiMaster.axiMasterClass('tb',Monitors)

axi.makeRead(1,16,0x100,4)
axi.makeWrite(1,16,0x100,4)
axi.wait(100)
'''
# def makeRead(self,Burst,Len,Address,Size=4,Rid='none'):
# def makeWriteWstrb(self,Burst,Len,Address,Size=4,Wstrb='auto',Wdatas=[]):
# def makeWrite(self,Burst,Len,Address,Size=4,Wdatas=[]):

import os,sys
import logs
import veri

class axiMasterClass:
    def __init__(self,Path,Monitors,Prefix='',Suffix='',Name='"no given name"'):
        self.Path = Path
        if Monitors != -1: Monitors.append(self)
        self.Name=Name
        self.Queue=[]
        self.arQueue=[]
        self.awQueue=[]
        self.wQueue=[]
        self.Rid = 1
        self.waiting=0
        self.datawidth = 0
        self.AREADS=[]
        self.RDATAS={}
        self.rreadyCount = 0
        self.rreadyOnes = 3
        self.rreadyDeny = 0
        self.rreadyDenys = 10
        self.ReadyAlways = True
        self.renames={}
        self.prefix= Prefix
        self.suffix= Suffix
        self.AWVALID = False
        self.ARVALID = False
        self.WVALID = False
        self.Size = 2
        self.WSTRB = -1 
        self.AXI3 = False
        self.Bscore = []

    def cannot_find_sig(self,Sig):
        logs.log_error('CANNOT FIND SIG %s' % Sig)

    def onFinish(self):
        if self.Bscore != []:
            logs.log_error('BVALID: some BID left in BIF queue: %s' % (self.Bscore))

    def rename(self,Sig):
        if Sig in self.renames:
            return self.renames[Sig]

        if self.prefix:
            Sig = self.prefix + Sig
        if self.suffix:
            Sig = Sig + self.suffix 
        return Sig

    def peekbin(self,Sig):
        Sig = self.rename(Sig)
        return veri.peek('%s.%s'%(self.Path,Sig))
    def peek(self,Sig):
        Sig = self.rename(Sig)
        return logs.peek('%s.%s'%(self.Path,Sig))
    def bpeek(self,Sig):
        Sig = self.rename(Sig)
        return veri.peek('%s.%s'%(self.Path,Sig))
    def force(self,Sig,Val):
        Sig = self.rename(Sig)
        veri.force('%s.%s'%(self.Path,Sig),str(Val))
    def action(self,Txt):
        wrds = Txt.split()
        if wrds[0] == 'ready':
            self.ReadyAlways = (eval(wrds[1]) != 0)
        elif wrds[0]=='rid':
            self.Rid = eval(wrds[1])
        elif wrds[0]=='wait':
            self.wait(eval(wrds[1]))
        elif wrds[0]=='size':
            self.Size = eval(wrds[1])
        elif wrds[0]=='axi3':
            self.AXI3 = True
        elif wrds[0]=='axi4':
            self.AXI3 = False
        elif wrds[0]=='wstrb':
            self.WSTRB = eval(wrds[1])
        elif wrds[0]=='write':
            if len(wrds)==3:
                self.makeWrite(1,1,eval(wrds[1]),self.Size,[eval(wrds[2])])
            elif len(wrds)>=6:
                self.makeWrite(eval(wrds[1]),eval(wrds[2]),eval(wrds[3]),eval(wrds[4]),list(map(eval,wrds[5:])))
            else:
                logs.log_error('axiMaster %s write got not enough words in command (%s)' % (self.Name,wrds))
        elif wrds[0]=='read':
            Burst = eval(wrds[1])
            Len   = eval(wrds[2])
            Addr  = eval(wrds[3])
            self.makeRead(Burst,Len,Addr,self.Size,self.Rid)
# axim read  1 32 0x00045600 4 7
        elif wrds[0] in ['readcheck', 'check', 'rdcheck']:
            Addr = eval(wrds[1])
            if len(wrds)<3:
                logs.log_error('CHECK axi master line needs at least 3 params "check address data"')
                return
            Datas = list(map(eval,wrds[2:]))
            if Addr in self.RDATAS:
                Exps = self.RDATAS.pop(Addr)
                while (Datas!=[])and(Exps!=[]):
                    ExpData = Exps.pop(0)
                    ActData = Datas.pop(0)
                    logs.log_ensure(ExpData == ActData, 'RDATA addr=%x exp = %x act = %x'%(Addr,ExpData,ActData))

            else:
                logs.log_error('address %x is not registred in RDATAS %s' % (Addr,list(map(hex,self.RDATAS.keys()))))

            if Datas!=[]:
                logs.log_error('not enough RDATAS for this query, leftover addr=%x %s' % (Addr,list(map(hex,Datas))))

        else:
            logs.log_error('action %s axiMaster unrecognized %s'%(self.Name,Txt))

#    def makeRead(self,Burst,Len,Address,Size=4,Rid='none'):
            
# Burst,Len,Address,Size=4,Wdatas=[]):

    def busy(self):
        if self.Queue!=[]: return True
        if self.arQueue!=[]: return True
        if self.awQueue!=[]: return True
        if self.wQueue!=[]: return True
        return False

    def makeRead(self,Burst,Len,Address,Size=4,Rid='none'):
        if Rid!='none': 
            self.Rid = Rid
        else: 
            self.Rid = 1
        self.Queue.append(('ar','force arvalid=1 arburst=%s arlen=%s araddr=%s arsize=%s arid=%s'%(Burst,Len-1,Address,Size,self.Rid)))
        self.AREADS.append((Len,Address,self.Rid))
        self.Queue.append(('ar','force arvalid=0 arburst=0 arlen=0 araddr=0 arsize=0 arid=0'))
        self.Rid += 1


    def makeWrite(self,Burst,Len,Address,Size=4,Wdatas=[]):
        logs.log_info('makeWrite %x %x %x %x %s' % (Burst,Len,Address,Size,Wdatas))
        self.Queue.append(('aw','force awvalid=1 awburst=%s awlen=%s awaddr=%s awsize=%s awid=%s'%(Burst,Len-1,Address,Size,self.Rid)))
        self.Queue.append(('aw','force awvalid=0 awburst=0 awlen=0 awaddr=0 awsize=0 awid=0'))
        self.Bscore.append((self.Rid,Address))
        if Len<=0:
            logs.log_warning('axiMaster %s got len=%d for write'%(self.Name,Len))
        for ii in range(Len):
            if type(Wdatas) is int:
                Wdata = Wdatas
            elif len(Wdatas)==0:
                Wdata = '0x%08x%08x%08x%08x'%(self.Rid+0x1000*ii,0x100+self.Rid+0x1000*ii,0x200+self.Rid+0x1000*ii,0x300+self.Rid+0x1000*ii)
            elif (type(Wdatas[0]) is str):
                Wdata = Wdatas.pop(0)
            else:
                Wdata = hex(Wdatas.pop(0))
            if ii==(Len-1):
                Wlast=1
            else:
                Wlast = 0
            Wstrb = (1<<(1<<Size))-1
            if self.WSTRB>0:
                Wstrb = self.WSTRB
            Str = 'force wvalid=1 wdata=%s wstrb=0x%x wlast=%d'%(Wdata,Wstrb,Wlast)
            if self.AXI3:
                Str += ' wid=%d'%self.Rid
            self.Queue.append(('w',Str))

        Str = 'force wvalid=0 wdata=0 wstrb=0 wlast=0'
        if self.AXI3:
            Str += ' wid=%d'%self.Rid
        self.Queue.append(('w',Str))
        logs.log_info('makeWrite %s >>>>> %x size=%s qu=%d'%(self.Name,Address,Size,len(self.Queue)))
        self.Rid += 1
            
    def wait(self,Many):
        self.Queue.append(('this','wait %d'%Many))
    def finish(self,Many):
        self.Queue.append(('this','wait %d'%Many))
        self.Queue.append(('this','finish'))

    def queued_force(self,Net,Val):
        self.Queue.append(('w','force %s=%s'%(Net,Val)))

    def run(self):
#        logs.log_info('runn lenaw=%d lenar=%d lenq=%d lenw=%d'%(len(self.awQueue),len(self.arQueue),len(self.Queue),len(self.wQueue)))
        self.runResponce()
        self.runAw()
        self.runAr()
        self.runW()
        self.runB()
        if self.waiting>0:
            self.waiting -= 1
            return
        self.runQueue()

    def manageRready(self,What):
        if self.ReadyAlways:
            self.force('rready',1)
            return 1
            
#        if What==1:
#            print('>>>',What,self.rreadyCount,self.rreadyDeny,self.peek('rvalid'))
        if What==0:
            self.force('rready',0)
            self.rreadyCount=0
            return 0
        if self.rreadyDeny>0:
            self.force('rready',0)
            self.rreadyDeny += 1
            if self.rreadyDeny > self.rreadyDenys:
                self.rreadyDeny=0
                self.rreadyCount=0
            return 0
        elif self.rreadyCount==self.rreadyOnes:
            self.force('rready',0)
            self.rreadyDeny = 1
            self.rreadyCount=0
            return 0
        else:
            self.force('rready',1)
            self.rreadyCount += 1
            return 1

    def runResponce(self):
        if self.peek('rvalid')==1:
            Ready = self.manageRready(1)
            if Ready == 0: return
            rdata = self.peek('rdata')
            if self.datawidth==0:
                rrr = self.bpeek('rdata')
                self.datawidth = len(rrr)
            rid = self.peek('rid')
            widrid = len(self.peekbin('rid'))
            rlast = self.peek('rlast')
            rresp = self.peek('rresp')
            rdatax  = '%032x'%rdata 
            msb  = int(self.datawidth/4) 
#            print('MSB "%s" %s    %s'%(msb,type(msb),rdatax))
            rdatax = rdatax[-msb:]
            logs.log_info('axiM responce rid=%x rlast=%d rdata=%s rresp=%s     %s'%(rid,rlast,rdatax,rresp,self.Path))
            self.readAction(rid,rlast,rdata,widrid,rresp)
        else:
            self.manageRready(0)

    def readAction(self,rid,rlast,rdatax,widrid,rresp):
        if self.AREADS == []:
            logs.log_error('READ ACTION %s and no AREADS' % (self.Name))
            return
            
        Len,Addr,Rid = self.AREADS[0]
        if (Rid & ((1<<widrid)-1)) != rid:
            logs.log_wrong('sent ARID=%d RID=%d'%(Rid,rid))
        if rresp!=0:
            logs.log_wrong('RRESP came back %s  ADDR=%a  rid=%sd'%(rresp,Addr,Rid))
        
        if Addr in self.RDATAS:
            self.RDATAS[Addr].append(rdatax)
        else:
            self.RDATAS[Addr] = [rdatax]
        if rlast == 1:
            self.AREADS.pop(0)
        logs.log_info('ADDRDATAS %s   %s' % (hex(Addr), list(map(hex,self.RDATAS.keys()))))

    def runQueue(self):
#        print('\n\n\n\ 0 RUNQ',self.Queue)
#        print('RUNQ',self.awQueue)
#        print('RUNQ',self.wQueue)
        while self.Queue!=[]:
            Dst,Cmd = self.Queue.pop(0)
            if Dst=='aw':
                self.awQueue.append(Cmd)
            elif Dst=='ar':
                self.arQueue.append(Cmd)
            elif Dst=='w':
                self.wQueue.append(Cmd)
            else:
                self.runThis(Cmd)
                return

    def runThis(self,Cmd):
        wrds = Cmd.split()
        if wrds==[]:
            pass
        elif (wrds[0]=='wait'):
            self.waiting = int(wrds[1])
        elif (wrds[0]=='finish'):
            logs.log_info('veri finish from axi Master')
            veri.finish()
            sys.exit()
        elif (wrds[0]=='force'):
            for wrd in wrds[1:]:
                ww = wrd.split('=')
                Var = ww[0]
                Val = eval(ww[1])
                self.force(Var,Val)
       
    
    def runB(self):
        if self.peek('bvalid')==1:
            Bid = self.peek('bid')
            ii = 0;
            while ii < len(self.Bscore):
                if self.Bscore[ii][0] == Bid:
                    logs.log_correct('BVALID %s bid=%x bresp=%x' % (self.Name,Bid,self.peek('bresp')))
                    self.Bscore.pop(ii)
                    ii = 10000
                else:
                    ii += 1
            if (ii!=10000):
                logs.log_error('BVALID %s not found bid=%x bresp=%x' % (self.Name,Bid,self.peek('bresp')))
            self.force('bready','1')
        else:
            self.force('bready','0')
    def runW(self):
#        if (self.WVALID) and (self.peek('wready')==0): return
        if self.wQueue==[]: 
            self.force('wvalid',0)
            return
        Cmd = self.wQueue[0]
        wrds = Cmd.split()
        if wrds==[]:
            pass
        elif (wrds[0]=='force'):
            self.forces(wrds[1:])
        self.WVALID = ('wvalid=1' in Cmd)
        if (self.peek('wready')==1):
            self.wQueue.pop(0)

    def forces(self,wrds):
        for wrd in wrds:
            ww = wrd.split('=')
            Var = ww[0]
            Val = eval(ww[1])
            self.force(Var,Val)

    def runAw(self):
        if (self.AWVALID) and (self.peek('awready')==0): return
        if self.awQueue==[]: 
            self.force('awvalid',0)
            return
        Cmd = self.awQueue.pop(0)
        wrds = Cmd.split()
        if wrds==[]:
            pass
        elif (wrds[0]=='force'):
            self.forces(wrds[1:])

        self.AWVALID = ('awvalid=1' in Cmd)

    def runAr(self):
        if (self.ARVALID) and (self.peek('arready')==0): return
        if self.arQueue==[]: 
            self.force('arvalid',0)
            return
        Cmd = self.arQueue.pop(0)
        wrds = Cmd.split()
        if wrds==[]:
            pass
        elif (wrds[0]=='force'):
            self.forces(wrds[1:])
        self.ARVALID = ('arvalid=1' in Cmd)


