
DEMO = '''
axi = axiMaster.axiMasterClass('tb',Monitors)

axi.makeRead(1,16,0x100,4)
axi.makeWrite(1,16,0x100,4)
axi.wait(100)
'''
# def makeRead(self,Burst,Len,Address,Size=4,Rid='none'):
# def makeWriteWstrb(self,Burst,Len,Address,Size=4,Wstrb='auto',Wdatas=[]):

import os,sys,string,types
import logs
import veri

class axiMasterClass:
    def __init__(self,Path,Monitors,Name='?'):
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
        self.readAction = False
        self.READS=[]
        self.rreadyCount = 0
        self.rreadyOnes = 3
        self.rreadyDeny = 0
        self.rreadyDenys = 10
        self.renames={}
        self.prefix=''
        self.suffix=''
        self.AWVALID = False
        self.ARVALID = False
        self.WVALID = False

    def rename(self,Sig):
        if Sig in self.renames:
            return self.renames[Sig]

        if self.prefix:
            Sig = self.prefix + Sig
        if self.suffix:
            Sig = Sig + self.suffix 
        return Sig

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
        print('ACT',Txt)
        wrds = Txt.split()
        if wrds[0]=='write':
            self.makeWrite(eval(wrds[1]),eval(wrds[2]),eval(wrds[3]),eval(wrds[4]),list(map(eval,wrds[5:])))
        elif wrds[0]=='read':
            self.makeRead(eval(wrds[1]),eval(wrds[2]),eval(wrds[2]),2)
        else:
            logs.log_error('action %s axiMater unrecognized %s'%(self.Name,Txt))
            
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
        if self.readAction:
            self.READS.append((Len,Address,self.Rid))
        self.Queue.append(('ar','force arvalid=0 arburst=0 arlen=0 araddr=0 arsize=0 arid=0'))
        self.Rid += 1

    def makeWriteWstrb(self,Burst,Len,Address,Size=4,Wstrb='auto',Wdatas=[]):
        if Wstrb == 'auto':
            self.makeWrite(Burst,Len,Address,Size,Wdatas)
            return
        self.Queue.append(('aw','force awvalid=1 awburst=%s awlen=%s awaddr=%s awsize=%s awid=%s'%(Burst,Len-1,Address,Size,self.Rid)))
        self.Queue.append(('aw','force awvalid=0 awburst=0 awlen=0 awaddr=0 awsize=0 awid=0'))
        self.Rid += 1
        for ii in range(Len):
            if len(Wdatas)==0:
                Wdata = '0x%08x%08x%08x%08x'%(self.Rid+0x1000*ii,0x100+self.Rid+0x1000*ii,0x200+self.Rid+0x1000*ii,0x300+self.Rid+0x1000*ii)
            else:
                Wdata = Wdatas.pop(0)
                if type(Wdata) is not str:
                    Wdata = hex(Wdatas.pop(0))
            if ii==(Len-1):
                Wlast=1
            else:
                Wlast = 0
            self.Queue.append(('w','force wvalid=1 wdata=%s wstrb=0x%x wlast=%d'%(Wdata,Wstrb,Wlast)))

        self.Queue.append(('w','force wvalid=0 wdata=0 wstrb=0 wlast=0'))


    def makeWrite(self,Burst,Len,Address,Size=4,Wdatas=[]):
        self.Queue.append(('aw','force awvalid=1 awburst=%s awlen=%s awaddr=%s awsize=%s awid=%s'%(Burst,Len-1,Address,Size,self.Rid)))
        self.Queue.append(('aw','force awvalid=0 awburst=0 awlen=0 awaddr=0 awsize=0 awid=0'))
        self.Rid += 1
        if Len<=0:
            logs.log_warning('axiMaster %s got len=%d for write'%(self.Name,Len))
        for ii in range(Len):
            if len(Wdatas)==0:
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
            self.Queue.append(('w','force wvalid=1 wdata=%s wstrb=0x%x wlast=%d'%(Wdata,Wstrb,Wlast)))

        self.Queue.append(('w','force wvalid=0 wdata=0 wstrb=0 wlast=0'))
        logs.log_info('makeWrite %s >>>>> %x size=%s qu=%d'%(self.Name,Address,Size,len(self.Queue)))
            
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
        if What==1:
            print('>>>',What,self.rreadyCount,self.rreadyDeny,self.peek('rvalid'))
        if What==0:
            self.force('rready',0)
            self.rreadyCount=0
            return
        if self.rreadyDeny>0:
            self.force('rready',0)
            self.rreadyDeny += 1
            if self.rreadyDeny > self.rreadyDenys:
                self.rreadyDeny=0
                self.rreadyCount=0
        elif self.rreadyCount==self.rreadyOnes:
            self.force('rready',0)
            self.rreadyDeny = 1
            self.rreadyCount=0
        else:
            self.force('rready',1)
            self.rreadyCount += 1

    def runResponce(self):
        if self.peek('rvalid')==1:
            self.manageRready(1)
            rdata = self.peek('rdata')
            if self.datawidth==0:
                rrr = self.bpeek('rdata')
                self.datawidth = len(rrr)
            rid = self.peek('rid')
            rlast = self.peek('rlast')
            rdatax  = '%032x'%rdata 
            msb  = int(self.datawidth/4) 
#            print('MSB "%s" %s    %s'%(msb,type(msb),rdatax))
            rdatax = rdatax[-msb:]
            logs.log_info('axiM responce rid=%x rlast=%d rdata=%s     %s'%(rid,rlast,rdatax,self.Path))
            if self.readAction:
                self.readAction(rid,rlast,rdatax)
        else:
            self.manageRready(0)




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
#        logs.log_info('runB %s %s peek %s %s'%(self.peek('bvalid'),self.peek('bready'),logs.peek('tb.ext_bvalid'),logs.peek('tb.ext_bready')))
        if self.peek('bvalid')==1:
            self.force('bready','1')
        else:
            self.force('bready','0')
    def runW(self):
        if (self.WVALID) and (self.peek('wready')==0): return
        if self.wQueue==[]: 
            self.force('wvalid',0)
            return
        Cmd = self.wQueue.pop(0)
        wrds = Cmd.split()
        if wrds==[]:
            pass
        elif (wrds[0]=='force'):
            self.forces(wrds[1:])
        self.WVALID = ('wvalid=1' in Cmd)

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
        print('runAw',wrds)
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


