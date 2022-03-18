
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
        self.Starvation = False
        self.arready = 0
        self.defines = {}
        self.callback = False

    def cannot_find_sig(self,Sig):
        logs.log_error('CANNOT FIND SIG %s' % Sig)

    def onFinish(self):
        if self.Bscore != []:
            logs.log_error('BVALID: some (%d) BID left in BID queue' % (len(self.Bscore)))
            for ii in range(min(10,len(self.Bscore))):
                logs.log_info('    leftover in BID %x %x' % (self.Bscore[ii]))
        elif self.busy():
            logs.log_error('%s finished busy status' % (self.Name))
            

    def rename(self,Sig):
        if Sig in self.renames:
            return self.renames[Sig]

        if self.prefix:
            Sig = self.prefix + Sig
        if self.suffix:
            Sig = Sig + self.suffix 
        return Sig

    def eval(self,Expr):
        Res =  eval(Expr,self.defines,self.SeqObj.Translates)
        return Res
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
        logs.log_info('ACTION %s' % Txt)
        if wrds[0] == 'starvation':
            if wrds[1] in [1,'1','on']:
                self.Starvation = True
                veri.force('tb.marker0','5')
            elif wrds[1] in [0,'0','off']:
                self.Starvation = False
                veri.force('tb.marker0','0')
            else:
                logs.log_error('Starvation accepts only on / off , given is "%s"' % wrds[1])
        elif wrds[0] == 'ready':
            self.ReadyAlways = (eval(wrds[1]) != 0)
        elif wrds[0]=='rid':
            self.Rid = eval(wrds[1])
        elif wrds[0]=='wait':
            self.wait(eval(wrds[1]))
        elif wrds[0] in ['wsize','size']:
            self.Size = eval(wrds[1])
        elif wrds[0]=='axi3':
            self.AXI3 = True
        elif wrds[0]=='axi4':
            self.AXI3 = False
        elif wrds[0]=='wstrb':
            self.WSTRB = eval(wrds[1])
        elif wrds[0]=='write_illegal':
            self.makeWriteIllegal(eval(wrds[1]),eval(wrds[2]),eval(wrds[3]),eval(wrds[4]),eval(wrds[5]),list(map(eval,wrds[6:])))
        elif wrds[0]=='write':
            if len(wrds)==3:
                self.makeWrite(1,1,self.eval(wrds[1]),self.Size,[self.eval(wrds[2])])
            elif len(wrds)>=6:
                self.makeWrite(self.eval(wrds[1]),self.eval(wrds[2]),self.eval(wrds[3]),self.eval(wrds[4]),list(map(self.eval,wrds[5:])))
            else:
                logs.log_error('axiMaster %s write got not enough words in command (%s)' % (self.Name,wrds))
        elif wrds[0]=='read':
            Burst = eval(wrds[1])
            Len   = eval(wrds[2])
            Addr  = eval(wrds[3])
            if len(wrds)>=5:
                Size = eval(wrds[4])
            else:
                Size = self.Size
            self.makeRead(Burst,Len,Addr,Size,self.Rid)
# axim read  1 32 0x00045600 4 7
        elif wrds[0] in ['readcheck', 'check', 'rdcheck']:
            Addr = eval(wrds[1])
            if len(wrds)<3:
                logs.log_error('CHECK axi master line needs at least 3 params "check address data"')
                return
            Datas = list(map(eval,wrds[2:]))
            if Addr in self.RDATAS:
                Exps = self.RDATAS[Addr]
                while (Datas!=[])and(Exps!=[]):
                    ActData = Exps.pop(0)
                    ExpData = Datas.pop(0)
                    logs.log_ensure(ExpData == ActData, 'RDATA addr=%x exp = %x act = %x tail=%d'%(Addr,ExpData,ActData,len(Exps)))

            else:
                logs.log_error('address %x is not registred in RDATAS %s' % (Addr,list(map(hex,self.RDATAS.keys()))))

            if Datas!=[]:
                logs.log_error('not enough RDATAS for this query, leftover addr=%x %s' % (Addr,list(map(hex,Datas))))

        else:
            logs.log_error('action %s axiMaster unrecognized %s'%(self.Name,Txt))

#    def makeRead(self,Burst,Len,Address,Size=4,Rid='none'):
            
# Burst,Len,Address,Size=4,Wdatas=[]):

    def busyWhy(self):
        for Item in self.wQueue:
            logs.log_info('BUSYWHY %s ' % str(Item))

    def busy(self,Why = False):
        if Why:
            logs.log_info('BUSY %s q=%d arq=%d awq=%d wq=%d bq=%d ' % (self.Name,len(self.Queue),len(self.arQueue),len(self.awQueue),len(self.wQueue),len(self.Bscore))) 
        if self.Queue!=[]: return True
        if self.arQueue!=[]: return True
        if self.awQueue!=[]: return True
        if self.wQueue!=[]: return True
        if self.Bscore!=[]: return True
        return False

    def makeRead(self,Burst,Len,Address,Size=4,Rid='none'):
        if Rid!='none': 
            self.Rid = Rid
        else: 
            self.Rid = 1
        self.Queue.append(('ar','force arvalid=1 arburst=%s arlen=%s araddr=%s arsize=%s arid=%s'%(Burst,Len-1,Address,Size,self.Rid)))

        self.AREADS.append((Len,Address,self.Rid,0))
        self.Queue.append(('ar','force arvalid=0 arburst=0 arlen=0 araddr=0 arsize=0 arid=0'))
        Mask = (1<<len(self.peekbin('arid')))-1
        self.Rid = Mask & (1+self.Rid)

    def makeWriteIllegal(self,Burst,Len,actualLen,Address,Size=4,Wdatas=[]):
        self.Queue.append(('aw','force awvalid=1 awburst=%s awlen=%s awaddr=%s awsize=%s awid=%s'%(Burst,Len-1,Address,Size,self.Rid)))
        self.Queue.append(('aw','force awvalid=0 awburst=0 awlen=0 awaddr=0 awsize=0 awid=0'))
        self.Bscore.append((self.Rid,Address))
        self.writeDatasLoop(actualLen,Size,Address,Wdatas)
        logs.log_info('makeWrite %s >>>>> %x size=%s qu=%d'%(self.Name,Address,Size,len(self.Queue)))

    def makeWrite(self,Burst,Len,Address,Size=4,Wdatas=[]):
        if Len==0: 
            logs.log_error('axiMaster %s makeWrite got zero length request at addr=%x ' % (self.Name,Address))
            return
        logs.log_info('makeWrite %x %x %x %x %s' % (Burst,Len,Address,Size,Wdatas))
        self.Queue.append(('aw','force awvalid=1 awburst=%s awlen=%s awaddr=%s awsize=%s awid=%s'%(Burst,Len-1,Address,Size,self.Rid)))
        self.Queue.append(('aw','force awvalid=0 awburst=0 awlen=0 awaddr=0 awsize=0 awid=0'))
        self.Bscore.append((self.Rid,Address))
        if Len<=0:
            logs.log_warning('axiMaster %s got len=%d for write'%(self.Name,Len))
        self.writeDatasLoop(Len,Size,Address,Wdatas)
        logs.log_info('makeWrite %s >>>>> %x size=%s qu=%d'%(self.Name,Address,Size,len(self.Queue)))

    def writeDatasLoop(self,Len,Size,Address,Wdatas):
        for ii in range(Len):
            if type(Wdatas) is int:
                Wdata = Wdatas
            elif len(Wdatas)==0:
                Wdata = '0x%08x%08x%08x%08x'%(self.Rid+0x1000*ii,0x100+self.Rid+0x1000*ii,0x200+self.Rid+0x1000*ii,0x300+self.Rid+0x1000*ii)
                Wdata = Address + ii * 0x8
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
        Mask = (1<<len(self.peekbin('awid')))-1
        self.Rid = Mask & (1+self.Rid)
            
    def wait(self,Many):
        self.Queue.append(('this','wait %d'%Many))
    def finish(self,Many):
        self.Queue.append(('this','wait %d'%Many))
        self.Queue.append(('this','finish'))

    def queued_force(self,Net,Val):
        self.Queue.append(('w','force %s=%s'%(Net,Val)))

    def run(self):
#        logs.log_info('runn lenaw=%d lenar=%d lenq=%d lenw=%d'%(len(self.awQueue),len(self.arQueue),len(self.Queue),len(self.wQueue)))
        if self.Starvation:
            self.force('rready',0)
            self.force('bready',0)
            return
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
        Len,Addr,Rid,Pos = self.AREADS[0]
        logs.log_info('axi Master %s READ len=%x addr0=%x addr=%x arid=%x || rid=%x rlast=%x data=%x  rresp=%d  areads= %s' % (self.Name,Len,Addr,Addr+8*Pos,Rid,rid,rlast,rdatax,rresp,self.AREADS))
        self.AREADS[0] = (Len,Addr,Rid,Pos+1)

        if (Rid & ((1<<widrid)-1)) != rid:
            logs.log_wrong('sent ARID=%d RID=%d'%(Rid,rid))
        if rresp!=0:
            logs.log_wrong('RRESP came back %s  ADDR=%x  rid=0x%x'%(rresp,Addr,Rid))
        
        ADDR = Addr + Pos * (1<<self.Size)
        if ADDR not in self.RDATAS: self.RDATAS[ADDR] = []
        self.RDATAS[ADDR].append(rdatax)
        if self.callback:
            self.callback(ADDR,rdatax)
        if rlast == 1:
            self.AREADS.pop(0)
#        logs.log_info('ADDRDATAS %s len=%d  %s' % (hex(Addr), len(self.RDATAS[Addr]),list(map(hex,self.RDATAS.keys()))))

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
                logs.log_info('ARQUEUE %s' % Cmd)
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
            Bresp = self.peek('bresp')
            if self.Bscore == []:
                logs.log_error('BVALID %s arrived to empty expectant queue bid=%x bresp=%x' % (self.Name,Bid,Bresp))
            else:                
                ii = 0;
                while ii < len(self.Bscore):
                    if self.Bscore[ii][0] == Bid:
                        logs.log_correct('BVALID %s bid=%x bresp=%x' % (self.Name,Bid,Bresp))
                        self.Bscore.pop(ii)
                        ii = 10000
                    else:
                        ii += 1
                if (ii!=10000):
                    logs.log_error('BVALID %s not found bid=%x bresp=%x lenqueue=%d' % (self.Name,Bid,Bresp,len(self.Bscore)))
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
        if (self.peek('wready')==1) or ('wvalid=0' in Cmd) :
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
        if (self.ARVALID) and (self.arready==0): 
            self.arready = self.peek('arready')
            return
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
        self.arready = self.peek('arready')


