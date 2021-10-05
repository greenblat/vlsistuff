import logs
class axiProbeClass(logs.driverClass):
    def __init__(self,Path,Monitors,Prefix,Name='Uprober'):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Enable = True
        self.Awqueue = []
        self.Awqueueb = []
        self.Wqueue = 0
        self.Bids = []
        self.Name = Name
        self.Prefix = Prefix
        self.Suffix = ''

    def run(self):
        if not self.Enable: return
        if self.valid('awvalid') and self.valid('awready'):
            Awid = self.peek('awid')
            Awaddr = self.peek('awaddr')
            self.Awqueue.append((Awid,Awaddr))
            self.Awqueueb.append((Awid,Awaddr))

        if self.valid('wvalid') and self.valid('wready') and self.valid('wlast'):
            self.Wqueue += 1

        if self.valid('bvalid') and self.valid('bready'):
            bid = self.peek('bid')
            self.Bids.append(bid)

        
        if (self.Bids!=[]) and (self.Wqueue>0) and (self.Awqueue!=[]):
            if self.Wqueue>len(self.Awqueue):
                logs.log_error('prober %s: wqueue=%d > awqueue=%d' % (self.Name,self.Wqueue,len(self.Awqueue)))
            
            bid0 = self.Bids[0]
            for ind,(bid1,addr1) in enumerate(self.Awqueueb):
                if bid0 == bid1:
                    self.Awqueueb.pop(ind)
                    self.Bids.pop(0)
                    bid0 = 10000
            if bid0 != 10000:
                logs.log_error('prober %s: bid=%d  not in the awqueue=%s' % (self.Name,bid0,self.Awqueueb))
                self.Bids.pop(0)
                


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
        if len(self.Awqueueb)>0: return True
        if len(self.Bids)>0: return True
        if self.Wqueue != len(self.Awqueue): return True
        return False

