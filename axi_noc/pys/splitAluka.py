import logs

PORTS = ['a_','b_','c_','d_']

class splitAlukaClass(logs.driverClass):
    def __init__(self,Path,Monitors,Prefix,Name='Uprober'):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Enable = True
        self.Name = Name
        self.Prefix = Prefix
        self.Suffix = ''
        self.AWqueue = []

        self.AWqueue = {'a_':[],'b_':[],'c_':[],'d_':[]}
        self.Wqueue = {'a_':[],'b_':[],'c_':[],'d_':[]}
        self.Bids = {'a_':[],'b_':[],'c_':[],'d_':[]}
        self.workAW0 = []
        self.workAW = []
        self.workW = []
        self.AWwait = {'a_':0,'b_':0,'c_':0,'d_':0}
        self.Wwait = {'a_':0,'b_':0,'c_':0,'d_':0}


    def run(self):
        if not self.Enable: return
        if self.valid('awvalid') and self.valid('awready'):
            Awlen = self.peek('awlen')
            Awid = self.peek('awid')
            Awaddr = self.peek('awaddr')
            Port = PORTS[(Awaddr>>30) & 0x3]
            NextAwaddr = (Awaddr<<2) & 0xffffffff
            self.workAW.append((Port,Awlen,Awlen,Awid,NextAwaddr,Awaddr))
            self.workAW0.append((Port,Awlen,Awlen,Awid,NextAwaddr,Awaddr))
            self.Bids[Port].append(Awid)
            
        if self.valid('wvalid') and self.valid('wready'):
            Wdata = self.peek('wdata')
            Wstrb = self.peek('wstrb')
            Wlast = self.peek('wlast')
            self.workW.append((Wdata,Wlast,Wstrb))



        for Port in ['a_','b_','c_','d_'] :
            
            if self.valid(Port+'awvalid') and not self.valid(Port+'awready'):
                self.AWwait[Port] += 1
                if self.AWwait[Port]>500:
                    logs.log_error('aluka Split %s: awvalid %s stuck addr=%x' % (self.Name,Port,self.peek(Port+'awaddr')))
                    self.AWwait[Port] = 0
            elif (not self.valid(Port+'awvalid') or  self.valid(Port+'awready')):
                self.AWwait[Port] = 0

            if self.valid(Port+'wvalid') and not self.valid(Port+'wready'):
                self.Wwait[Port] += 1
                if self.Wwait[Port]>500:
                    logs.log_error('aluka Split %s: wvalid %s stuck' % (self.Name,Port))
                    self.Wwait[Port] = 0
            elif (not self.valid(Port+'wvalid') or  self.valid(Port+'wready')):
                self.Wwait[Port] = 0






            if self.valid(Port+'awvalid') and self.valid(Port+'awready'):
                Awlen = self.peek(Port+'awlen')
                Awid = self.peek(Port+'awid')
                Awaddr = self.peek(Port+'awaddr')
                if self.workAW0==[]:
                    logs.log_error('alukaSplit %s: port=%s workAW0 is empty for len=%x wid=%x awaddr=%x' % (self.Name,Port,Awlen,Awid,Awaddr))
                else:
                    expPort,Run,expAwlen,expAwid,expAwaddr,origAwaddr = self.workAW0[0] 
                    logs.log_ensure(Port == expPort,' alukaSplit %s port=%s exp=%s  awaddr=%x expaddr=%x orig=%x' %(self.Name,Port,expPort,Awaddr,expAwaddr,origAwaddr))
                    logs.log_ensure(Awaddr == expAwaddr,' alukaSplit %s %s awaddr=%x exp=%x orig=%x' %(self.Name,Port,Awaddr,expAwaddr,origAwaddr))
                    self.workAW0.pop(0)
            
            if self.valid(Port+'wvalid') and self.valid(Port+'wready'):
                expPort,Run,Awlen,Awid,Awaddr,origAwaddr = self.workAW[0] 
                Wlast = self.peek(Port+'wlast')
                Wdata = self.peek(Port+'wdata')
                Wstrb = self.peek(Port+'wstrb')
                logs.log_ensure(Port == expPort,' alukaSplit %s port=%s exp=%s  wdata=%x (%d) awaddr= %x %x' %(self.Name,Port,expPort,Wdata,Wdata,Awaddr,origAwaddr))
                expWdata,expWlast,expWstrb = self.workW.pop(0)
            

                logs.log_ensure(expWlast == Wlast,'alukaSplit %s port=%s wlast %x exp=%x' %(self.Name,Port,Wlast,expWlast))
                logs.log_ensure(expWdata == Wdata,'alukaSplit %s port=%s wdata %x exp=%x' %(self.Name,Port,Wdata,expWdata))
                logs.log_ensure(((Run==0) and Wlast)or((Run>0) and (Wlast==0)),'alukaSplit %s port=%s wlastRun0 %x exp=%x' %(self.Name,Port,Run,Wlast))

                if Wlast == 1:
                    self.workAW.pop(0)
                else:
                    self.workAW[0] = Port,Run-1,Awlen,Awid,Awaddr,origAwaddr

    def action(self,Txt):
        if 'enable' in Txt: 
            self.Enable = True
            return
        if 'disable' in Txt: 
            self.Enable = False
            return
    def onFinish(self):
        if self.busy():
            logs.log_error('prober %s remains busy' % (self.Name))
    def busy(self):
        if len(self.AWqueue)>0: return True
        if len(self.Wqueue)>0: return True
        if self.Wqueue != len(self.AWqueue): return True
        return False

