
DEMO = '''
axi = axiMaster.axiMasterClass('tb',Monitors)

axi.makeRead(1,16,0x100,4)
axi.makeWrite(1,16,0x100,4)
axi.wait(100)
'''


import os,sys,string
import logs
import veri

class axiMasterClass:
    def __init__(self,Path,Monitors):
        self.Path = Path
        Monitors.append(self)
        self.Queue=[]
        self.Wueue=[]
        self.Rid = 1
        self.waiting=0

    def peek(self,Sig):
        return logs.peek('%s.%s'%(self.Path,Sig))
    def force(self,Sig,Val):
        veri.force('%s.%s'%(self.Path,Sig),str(Val))

    def makeRead(self,Burst,Len,Address,Size=4):
        self.Queue.append('force arvalid=1 arburst=%s arlen=%s araddr=%s arsize=%s arid=%s'%(Burst,Len-1,Address,Size,self.Rid))
        self.Queue.append('force arvalid=0 arburst=0 arlen=0 araddr=0 arsize=0 arid=0')
        self.Rid += 1
    def makeWrite(self,Burst,Len,Address,Size=4):
        self.Queue.append('force awvalid=1 awburst=%s awlen=%s awaddr=%s awsize=%s awid=%s'%(Burst,Len-1,Address,Size,self.Rid))
        self.Queue.append('force awvalid=0 awburst=0 awlen=0 awaddr=0 awsize=0 awid=0')
        self.Rid += 1
        for ii in range(Len-1):
            Wdata = '%08x%08x%08x%08x'%(self.Rid,self.Rid,self.Rid,self.Rid)
            self.Queue.append('force wvalid=1 wdata=0x%s wstrb=0xffff wlast=0'%Wdata)

        Wdata = '%08x%08x%08x%08x'%(self.Rid,self.Rid,self.Rid,self.Rid)
        self.Queue.append('force wvalid=1 wdata=0x%s wstrb=0xffff wlast=1'%Wdata)
        self.Queue.append('force wvalid=0 wdata=0 wstrb=0 wlast=0')
            
    def wait(self,Many):
        self.Queue.append('force arvalid=0 awvalid=0 wvalid=0')
        self.Queue.append('wait %d'%Many)
    def finish(self,Many):
        self.Queue.append('wait %d'%Many)
        self.Queue.append('finish')

    def run(self):
        self.runResponce()
        self.runWueue()
        if self.waiting>0:
            self.waiting -= 1
            return
        self.runQueue()

    def runResponce(self):
        if self.peek('rvalid')==1:
            self.force('rready',1)
            rdata = self.peek('rdata')
            rid = self.peek('rid')
            rlast = self.peek('rlast')
            logs.log_info('axi responce rid=%x rlast=%d rdata=%032x     %s'%(rid,rlast,rdata,self.Path))
        else:
            self.force('rready',0)




    def runQueue(self):
        if self.Queue==[]: return
        Cmd = self.Queue.pop(0)
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
       
    def runWueue(self):
        if self.peek('wready')==0: return
        if self.Wueue==[]: 
            self.force('wvalid',0)
            return
        Cmd = self.Wueue.pop(0)
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
