import logs
class mergeAlukaClass(logs.driverClass):
    def __init__(self,Path,Monitors,Prefix,Name='Uprober'):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Enable = True
        self.Name = Name
        self.Prefix = Prefix
        self.Suffix = ''
        self.AWqueue = {'a_':[],'b_':[],'c_':[],'d_':[]}
        self.Wqueue = {'a_':[],'b_':[],'c_':[],'d_':[]}
        self.Bids = {'a_':[],'b_':[],'c_':[],'d_':[]}
        self.AWwait = {'a_':0,'b_':0,'c_':0,'d_':0}
        self.Wwait = {'a_':0,'b_':0,'c_':0,'d_':0}
        self.AWstart = {'a_':0,'b_':0,'c_':0,'d_':0}
        self.Wstart = {'a_':0,'b_':0,'c_':0,'d_':0}
        self.workAW = []
        self.workW = []

    def run(self):
        if not self.Enable: return

        for Port in ['a_','b_','c_','d_'] :
            if logs.getVar('wr_action') != 0 :
                self.Wwait[Port] = 0
                self.AWwait[Port] = 0
            if self.valid(Port+'awvalid') and not self.valid(Port+'awready'):
                if self.AWwait[Port]==0:
                    self.AWstart[Port] = logs.peek('tb.cycles')
                self.AWwait[Port] += 1
                if self.AWwait[Port]>500:
                    logs.log_error('aluka merge %s: awvalid %s stuck addr=%x from %d' % (self.Name,Port,self.peek(Port+'awaddr'),self.Wstart[Port] ))
                    self.AWwait[Port] = 0
            elif (not self.valid(Port+'awvalid') or  self.valid(Port+'awready')):
                self.AWwait[Port] = 0

            if self.valid(Port+'wvalid') and not self.valid(Port+'wready'):
                if self.Wwait[Port]==0:
                    self.Wstart[Port] = logs.peek('tb.cycles')
                self.Wwait[Port] += 1
                if self.Wwait[Port]>500:
                    logs.log_error('aluka merge %s: wvalid %s stuck from %d' % (self.Name,Port,self.Wstart[Port] ))
                    self.Wwait[Port] = 0
            elif (not self.valid(Port+'wvalid') or  self.valid(Port+'wready')):
                self.Wwait[Port] = 0




            if self.valid(Port+'awvalid') and self.valid(Port+'awready'):
                Awlen = self.peek(Port+'awlen')
                Awid = self.peek(Port+'awid')
                Awaddr = self.peek(Port+'awaddr')
                self.AWqueue[Port].append((Awlen,Awlen,Awid,Awaddr))
            
            if self.valid(Port+'wvalid') and self.valid(Port+'wready'):
                Wlast = self.peek(Port+'wlast')
                Wdata = self.peek(Port+'wdata')
                Wstrb = self.peek(Port+'wstrb')
                self.Wqueue[Port].append((Wlast,Wstrb,Wdata))
            
        if self.valid('awvalid') and self.valid('awready'):
            Wid = self.peek('awid')
            if (Wid == 1): 
                A,B,C,D = self.AWqueue['a_'].pop(0)
                self.workAW.append(('a_',A,B,C,D))
            if (Wid == 2): 
                A,B,C,D = self.AWqueue['b_'].pop(0)
                self.workAW.append(('b_',A,B,C,D))
            if Wid == 3: 
                A,B,C,D = self.AWqueue['c_'].pop(0)
                self.workAW.append(('c_',A,B,C,D))
            if Wid == 4: 
                A,B,C,D = self.AWqueue['d_'].pop(0)
                self.workAW.append(('d_',A,B,C,D))
        if self.valid('wvalid') and self.valid('wready'):
            Wlast = self.peek('wlast')
            Wdata = self.peek('wdata')
            Wstrb = self.peek('wstrb')
            if self.workAW == []:
                logs.log_error('aluka %s: workAW is empty!!!   wlast=%x wstrb=%x wdata=%x' % (self.Name,Wlast,Wstrb,Wdata))
                return
            Port,Run,Awlen,Awid,Awaddr = self.workAW[0]
            if self.Wqueue[Port] == []:
                logs.log_error('wr aluka %s port %s has empty wqueue workaw = %d %d %d awaddr=%x' % ( self.Name,Port,Run,Awlen,Awid,Awaddr))
                logs.log_error('wr aluka %s port %s actual %d %x' % (self.Name,Port,Wlast,Wdata))
            else:
                (expWlast,expWstrb,expWdata) = self.Wqueue[Port].pop(0)
                logs.log_ensure( (((Run>0)and(Wlast==0)) or ((Run==0) and (Wlast==1))) and (Wlast == expWlast) and (Wdata == expWdata) and (Wstrb == expWstrb),
                    'aluka %s : port=%s addr=%x len=%x last %d %d wdata a= %x (%d) e=%x (%d) wstrb %x %x' % (self.Name,Port,Awaddr,Awlen,Wlast, expWlast, Wdata, Wdata,expWdata, expWdata, Wstrb, expWstrb))
                
                if Wlast == 1:
                    self.workAW.pop(0)
                else:
                    self.workAW[0] = Port,Run-1,Awlen,Awid,Awaddr 
        if self.valid(Port+'bvalid') and self.valid(Port+'bready'):
            self.AWwait[Port] = 0
            self.Wwait[Port] = 0

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

