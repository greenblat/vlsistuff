
DEMO = '''

BURST: 0 - fixed, 1- incrementing 2-wrapping

axi = axiMaster.axiMasterClass('tb',Monitors)

axi.makeRead(1,16,0x100,4)
axi.makeWrite(1,16,0x100,4)
axi.wait(100)
'''
# def makeRead(self,Burst,Len,Address,Size=4,Rid='none'):
# def makeWriteWstrb(self,Burst,Len,Address,Size=4,Wstrb='auto',Wdatas=[]):
# def makeWrite(self,Burst,Len,Address,Size=4,Wdatas=[]):


# in sequence:    axi write Burst Length Address  Size Wdata0 Wdata1 ... WdataN
# bursts: 0 - fixed, 1- incrementing 2-wrapping
# Size = in bytes 1,2,4,8
# Wdatas are optional and if not enough given, it will invent something.
# Id  is set prior in sequence by "axi rid 3" for id 3.
# read is similar just without datas.

import os,sys
import logs
import veri
import traceback

class axiMasterClass:
    def __init__(self,Path,Monitors,Prefix='',Suffix='',Name='"no given name"', write_data_generator=None):
        self.Path = Path
        if Monitors != -1: Monitors.append(self)
        self.Name=Name
        self.Queue=[]
        self.arQueue=[]
        self.awQueue=[]
        self.wQueue=[]
        self.Rid = 1
        self.IncrRid = 0
        self.waiting=0
        self.datawidth = 0
        self.AREADS={}
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
        self.WSTRBS =  []
        self.AXI3 = False
        self.Bscore = []
        self.Starvation = False
        self.arready = 0
        self.defines = {}
        self.callback = False
        self.write_data_generator = write_data_generator
        self.verbose = True
        self.fix_write_bid = False
        self.denyBready = False

    def cannot_find_sig(self,Sig):
        logs.log_error('CANNOT FIND SIG %s' % Sig)

    def onFinish(self):
        if self.Bscore != []:
            logs.log_error('BVALID: some (%d) BID left in BID queue' % (len(self.Bscore)))
            for ii in range(min(10,len(self.Bscore))):
                self.log_info_print('    leftover in BID %x %x' % (self.Bscore[ii]))
        elif self.busy():
            logs.log_error('%s finished busy status' % (self.Name))
            self.busy(True)
            

    def rename(self,Sig):
        if Sig in self.renames:
            return self.renames[Sig]

        if self.prefix:
            Sig = self.prefix + Sig
        if self.suffix:
            Sig = Sig + self.suffix 
        return Sig

    def eval(self,Expr):
        try:
            Res =  eval(Expr,self.defines,self.SeqObj.Translates)
        except:
            logs.log_error('eval of "%s" failed' % Expr)
            return 0
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
    def action(self,Txt,Orig=[]):
        wrds = Txt.split()
        logs.log_info('%s ACTION %s' % (self.Name,Txt))
        if wrds[0] == 'denyBready':
            self.denyBready = self.eval(wrds[1])
        elif wrds[0] == 'force':
            Net = Orig[1]
            Value = wrds[2]
            self.force(Net,Value)
        elif wrds[0] == 'starvation':
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
            if self.WSTRBS!=[]:
                for ww in wrds[1:]:
                    Val = eval(ww)
                    self.WSTRBS.append(Val)
                return
            self.WSTRB = eval(wrds[1])
            if len(wrds)>2:
                for ww in wrds[2:]:
                    Val = eval(ww)
                    self.WSTRBS.append(Val)
        elif wrds[0]=='write_illegal':
            self.makeWriteIllegal(eval(wrds[1]),eval(wrds[2]),eval(wrds[3]),eval(wrds[4]),eval(wrds[5]),list(map(eval,wrds[6:])))
        elif wrds[0]=='write':
            if self.verbose:
                print("WRITE ", len(wrds), wrds)
            if len(wrds)==3:
                self.makeWrite(1,1,self.eval(wrds[1]),self.Size,[self.eval(wrds[2])])
            elif len(wrds) == 5:
                self.makeWrite(self.eval(wrds[1]), self.eval(wrds[2]), self.eval(wrds[3]), self.eval(wrds[4]),[])
            elif len(wrds)>=6:
                self.makeWrite(self.eval(wrds[1]),self.eval(wrds[2]),self.eval(wrds[3]),self.eval(wrds[4]),list(map(self.eval,wrds[5:])))
            else:
                logs.log_error('axiMaster %s write got not enough words in command (%s)' % (self.Name,wrds))
        elif wrds[0]=='read':
            Burst = self.eval(wrds[1])
            Len   = self.eval(wrds[2])
            Addr  = self.eval(wrds[3])
            if len(wrds)>=5:
                Size = self.eval(wrds[4])
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
            self.log_info_print('BUSYWHY %s ' % str(Item))

    def busy(self,Why = False):
        if Why:
            self.log_info_print('BUSY %s q=%d arq=%d awq=%d wq=%d bq=%d areads=%d (%s) ' % (
                self.Name,len(self.Queue),len(self.arQueue),len(self.awQueue),len(self.wQueue),len(self.Bscore),len(self.AREADS),self.AREADS)) 
        if self.Queue!=[]: return True
        if self.arQueue!=[]: return True
        if self.awQueue!=[]: return True
        if self.wQueue!=[]: return True
        if self.Bscore!=[]: return True
        for Key in self.AREADS:
            if len(self.AREADS[Key])!=0: return True
        return False

    def makeRead(self,Burst,Len,Address,Size=4,Rid='none'):
        if Rid!='none': 
            self.Rid = Rid
        else: 
            self.Rid = 1

        num_full_writes, last_write_length = divmod(Len, 256)
        self.log_info_print('%s makeRead %x %x %x %x' % (self.Name, Burst, Len, Address, Size), 'dbg')
        if Len > 256:
            logs.log_info(
                f"Read request is greater than 256, splitting into {num_full_writes + 1 * (last_write_length > 0)} AXI transactions")
            for i in range(num_full_writes):
                Len = 256
                self.Queue.append(('ar','force arvalid=1 arburst=%s arlen=%s araddr=%s arsize=%s arid=%s'%(Burst,Len-1,Address,Size,self.Rid)))
                if Rid not in self.AREADS: self.AREADS[Rid] = []
                self.AREADS[Rid].append((Len,Address,Size,Len))
                self.Queue.append(('ar','force arvalid=0 arburst=0 arlen=0 araddr=0 arsize=0 arid=0'))
                Mask = (1<<len(self.peekbin('arid')))-1
                self.Rid = Mask & (self.IncrRid+self.Rid)
                Address = Address + int(256 * (1<<Size))

        if last_write_length > 0:
            Len = last_write_length
            self.Queue.append(('ar','force arvalid=1 arburst=%s arlen=%s araddr=%s arsize=%s arid=%s'%(Burst,Len-1,Address,Size,self.Rid)))
            if self.Rid not in self.AREADS: self.AREADS[self.Rid] = []
            self.AREADS[self.Rid].append((Len,Address,Size,Len))
            self.Queue.append(('ar','force arvalid=0 arburst=0 arlen=0 araddr=0 arsize=0 arid=0'))
            Mask = (1<<len(self.peekbin('arid')))-1
            self.Rid = Mask & (self.IncrRid+self.Rid)


#        traceback.print_stack()

    def makeWriteIllegal(self,Burst,Len,actualLen,Address,Size=4,Wdatas=[]):
        self.Queue.append(('aw','force awvalid=1 awburst=%s awlen=%s awaddr=%s awsize=%s awid=%s'%(Burst,Len-1,Address,Size,self.Rid)))
        self.Queue.append(('aw','force awvalid=0 awburst=0 awlen=0 awaddr=0 awsize=0 awid=0'))
        self.Bscore.append((self.Rid,Address))
        self.writeDatasLoop(actualLen,Size,Address,Wdatas)
        self.log_debug_print('makeWrite %s >>>>> %x size=%s qu=%d'%(self.Name,Address,Size,len(self.Queue)),Which='dbg')

    def makeWrite(self,Burst,Len,Address,Size=4,Wdatas=[]):
        logs.log_info("Wdatas %s" % (' '.join(list(map(hex,Wdatas)))))
        if Len==0: 
            logs.log_error('axiMaster %s makeWrite got zero length request at addr=%x ' % (self.Name,Address))
            return

        self.log_info_print('%s makeWrite %x %x %x %x %s' % (self.Name, Burst,Len,Address,Size,list(map(hex,Wdatas))),'dbg')
        num_full_writes, last_write_length = divmod(Len, 256)
        if Len > 256:
            logs.log_info(f"Write request is greater than 256, splitting into {num_full_writes + 1*(last_write_length > 0)} AXI transactions")
        for i in range(num_full_writes):
            Len = 256
            self.Queue.append(('aw','force awvalid=1 awburst=%s awlen=%s awaddr=%s awsize=%s awid=%s'%(Burst,Len-1,Address,Size,self.Rid)))
            self.Queue.append(('aw','force awvalid=0 awburst=0 awlen=0 awaddr=0 awsize=0 awid=0'))
            self.Bscore.append((self.Rid,Address))
            if Len<=0:
                logs.log_warning('axiMaster %s got len=%d for write'%(self.Name,Len))
            self.writeDatasLoop(Len,Size,Address,Wdatas)
            self.log_debug_print('makeWrite %s >>>>> %x size=%s qu=%d'%(self.Name,Address,Size,len(self.Queue)),Which='dbg')
            Address = Address + int(256 * (1 << Size))

        if last_write_length != 0:
            self.Queue.append(('aw', 'force awvalid=1 awburst=%s awlen=%s awaddr=%s awsize=%s awid=%s' % (
            Burst, last_write_length - 1, Address, Size, self.Rid)))
            self.Queue.append(('aw', 'force awvalid=0 awburst=0 awlen=0 awaddr=0 awsize=0 awid=0'))
            self.Bscore.append((self.Rid, Address))
            if last_write_length <= 0:
                logs.log_warning('axiMaster %s got len=%d for write' % (self.Name, Len))
            self.writeDatasLoop(last_write_length, Size, Address, Wdatas)
            self.log_debug_print('makeWrite %s >>>>> %x size=%s qu=%d' % (self.Name, Address, Size, len(self.Queue)),
                                 Which='dbg')



    def writeDatasLoop(self,Len,Size,Address,Wdatas):
        BusWid = len(self.peekbin('rdata'))
        if BusWid == 32: BusSize = 2
        if BusWid == 64: BusSize = 3
        if BusWid == 128: BusSize = 4
        if BusWid == 256: BusSize = 5
        if BusWid == 512: BusSize = 6


        for ii in range(Len):
            if type(Wdatas) is int:
                Wdata = Wdatas
            elif len(Wdatas)==0:
                if self.write_data_generator is None:
                    Wdata = Address + ii * 0x8
                else:
                    Wdata = self.write_data_generator()

            elif (type(Wdatas[0]) is str):
                Wdata = Wdatas.pop(0)
            else:
                Wdata = hex(Wdatas.pop(0))
            if ii==(Len-1):
                Wlast=1
            else:
                Wlast = 0

            if self.WSTRB>0:
                Wstrb = self.WSTRB
            elif self.WSTRBS!=[]: 
                self.WSTRB = self.WSTRBS.pop(0)
            elif BusSize == Size:
                Wstrb = (1<<(1<<Size))-1
            elif (BusSize == (1+Size)):
                if (Address & (1<<Size)) == 0: 
                    Wstrb = (1<<(1<<Size))-1
                else:
                    Wstrb = ((1<<(1<<Size))-1)<<(1<<Size)
            else:
                logs.log_info("NNONONONONO")
            logs.log_info("WWWWW0 bus=%d size=%d addr=%x wstrb=%x" % (BusSize,Size,Address,self.WSTRB))
            logs.log_info("WWWWW bus=%d size=%d addr=%x wstrb=%x" % (BusSize,Size,Address,Wstrb))


            Str = 'force wvalid=1 wdata=%s wstrb=0x%x wlast=%d'%(Wdata,Wstrb,Wlast)
            if self.AXI3:
                Str += ' wid=%d'%self.Rid
            self.Queue.append(('w',Str))
            Address += (1<<Size)

        Str = 'force wvalid=0 wdata=0 wstrb=0 wlast=0'
        if self.AXI3:
            Str += ' wid=%d'%self.Rid
        self.Queue.append(('w',Str))
        if not self.fix_write_bid:
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
            self.log_info_print('axiM responce rid=%x rlast=%d rdata=%s rresp=%s     %s'%(rid,rlast,rdatax,rresp,self.Path))
            self.readAction(rid,rlast,rdata,widrid,rresp)
        else:
            self.manageRready(0)

    def readAction(self,rid,rlast,rdatax,widrid,rresp):
        if len(self.AREADS) == 0:
            logs.log_error('READ ACTION %s and no AREADS' % (self.Name))
            return
        if rid not in self.AREADS: 
            logs.log_error('READ ACTION %s rid=%d and no AREADS' % (self.Name,rid))
            return

        Len,Addr,Size,Pos = self.AREADS[rid][0]
        Mul = 1<<Size
        self.log_info_print('axi Master %s READ pos=%d len=%x addr0=%x addr=%x arid=%x || rid=%x rlast=%x data=%x  rresp=%d  areads= %s' % (self.Name,Pos,Len,Addr,Addr+Mul*(Len-Pos),rid,rid,rlast,rdatax,rresp,len(self.AREADS)))
        if Pos == 1:
            if rlast != 1:
                logs.log_error('RLAST not present axi Master %s READ len=%x addr0=%x addr=%x arid=%x || rid=%x rlast=%x data=%x  rresp=%d  areads= %s' % (self.Name,Len,Addr,Addr+Mul*(Len-Pos),rid,rid,rlast,rdatax,rresp,len(self.AREADS)))
            self.AREADS[rid].pop(0)
        else:
            if rlast == 1:
                logs.log_error('RLAST too early axi Master %s READ len=%x addr0=%x addr=%x arid=%x || rid=%x rlast=%x data=%x  rresp=%d  areads= %s' % (self.Name,Len,Addr,Addr+Mul*(Len-Pos),rid,rid,rlast,rdatax,rresp,len(self.AREADS)))
            self.AREADS[rid][0] = (Len,Addr,Size,Pos-1)

        if rresp!=0:
            logs.log_wrong('RRESP came back %s  ADDR=%x  rid=0x%x  name=%s'%(rresp,Addr,rid,self.Name))
        
        ADDR = Addr + Pos * (1<<self.Size)
        if ADDR not in self.RDATAS: self.RDATAS[ADDR] = []
        self.RDATAS[ADDR].append(rdatax)
        if self.callback:
            self.callback(ADDR,rdatax)

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
                self.log_debug_print('ARQUEUE %s' % Cmd,Which='dbg')
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
            self.log_info_print('veri finish from axi Master')
            veri.finish()
            sys.exit()
        elif (wrds[0]=='force'):
            for wrd in wrds[1:]:
                ww = wrd.split('=')
                Var = ww[0]
                Val = eval(ww[1])
                self.force(Var,Val)
       
    
    def runB(self):
        if self.denyBready:
            self.force('bready','0')
        elif self.peek('bvalid')==1:
            Bid = self.peek('bid')
            Bresp = self.peek('bresp')
            if self.Bscore == []:
                logs.log_error('BVALID %s arrived to empty expectant queue bid=%x bresp=%x' % (self.Name,Bid,Bresp))
            else:                
                ii = 0;
                while ii < len(self.Bscore):
                    if self.Bscore[ii][0] == Bid:
                        logs.log_correct('BVALID %s bid=%x bresp=%x' % (self.Name,Bid,Bresp), Print=self.verbose)
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
            self.log_debug_print('DBG AR %s' % str(wrds),Which='dbg')
        self.ARVALID = ('arvalid=1' in Cmd)
        self.arready = self.peek('arready')

    def log_info_print(self, msg, Which=0):
        prefix = f"[{self.Name}]: "
        logs.log_info(prefix + msg, Which, verbose=self.verbose)

    def log_debug_print(self, msg, Which=0):
        prefix = f"[{self.Name}]: "
        logs.log_debug(prefix + msg, Which=Which, verbose=self.verbose)
