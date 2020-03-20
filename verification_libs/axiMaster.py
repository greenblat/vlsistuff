
DEMO = '''
axi = axiMaster.axiMasterClass('tb',Monitors)

axi.makeRead(1,16,0x100,4)
axi.makeWrite(1,16,0x100,4)
axi.wait(100)
'''


import os,sys,string,types
import logs
import veri

class axiMasterClass:
    def __init__(self,Path,Monitors):
        self.Path = Path
        Monitors.append(self)
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

    def makeRead(self,Burst,Len,Address,Size=4):
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
                if type(Wdata)!=types.StringType:
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
        logs.log_info('makeWrite >>>>> %x size=%s'%(Address,Size))
        self.Rid += 1
        for ii in range(Len):
            if len(Wdatas)==0:
                Wdata = '0x%08x%08x%08x%08x'%(self.Rid+0x1000*ii,0x100+self.Rid+0x1000*ii,0x200+self.Rid+0x1000*ii,0x300+self.Rid+0x1000*ii)
            elif (type(Wdatas[0])==types.StringType):
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
            
    def wait(self,Many):
        self.Queue.append(('this','wait %d'%Many))
    def finish(self,Many):
        self.Queue.append(('this','wait %d'%Many))
        self.Queue.append(('this','finish'))

    def run(self):
#        logs.log_info('runn lenaw=%d lenar=%d lenq=%d lenw=%d'%(len(self.awQueue),len(self.arQueue),len(self.Queue),len(self.wQueue)))
        self.runResponce()
        self.runAw()
        self.runAr()
        self.runW()
        if self.waiting>0:
            self.waiting -= 1
            return
        self.runQueue()

    def manageRready(self,What):
        if What==1:
            print '>>>',What,self.rreadyCount,self.rreadyDeny,self.peek('rvalid')
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
            msb  = (self.datawidth/4) 
            rdatax = rdatax[-msb:]
            logs.log_info('axi responce rid=%x rlast=%d rdata=%s     %s'%(rid,rlast,rdatax,self.Path))
            if self.readAction:
                self.readAction(rid,rlast,rdatax)
        else:
            self.manageRready(0)




    def runQueue(self):
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
        wrds = string.split(Cmd)
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
                ww = string.split(wrd,'=')
                Var = ww[0]
                Val = eval(ww[1])
                self.force(Var,Val)
       
    def runW(self):
        if self.peek('wready')==0: return
        if self.wQueue==[]: 
            self.force('wvalid',0)
            return
        Cmd = self.wQueue.pop(0)
        wrds = string.split(Cmd)
        if wrds==[]:
            pass
        elif (wrds[0]=='force'):
            self.forces(wrds[1:])

    def forces(self,wrds):
        for wrd in wrds:
            ww = string.split(wrd,'=')
            Var = ww[0]
            Val = eval(ww[1])
            self.force(Var,Val)

    def runAw(self):
        if self.peek('awready')==0: return
        if self.awQueue==[]: 
            self.force('awvalid',0)
            return
        Cmd = self.awQueue.pop(0)
        wrds = string.split(Cmd)
        if wrds==[]:
            pass
        elif (wrds[0]=='force'):
            self.forces(wrds[1:])

    def runAr(self):
        if self.peek('arready')==0: return
        if self.arQueue==[]: 
            self.force('arvalid',0)
            return
        Cmd = self.arQueue.pop(0)
        wrds = string.split(Cmd)
        if wrds==[]:
            pass
        elif (wrds[0]=='force'):
            self.forces(wrds[1:])


