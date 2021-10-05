import logs


class trafficClass(logs.driverClass):
    def __init__(self,Path,Monitors,Prefix,Name='Uprober'):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Enable = True
        self.Name = Name
        self.Prefix = Prefix
        self.Suffix = ''
        self.SLAVES = ['slv0_','slv1_','slv2_','slv3_']
        self.MASTERS = ['mst0_','mst1_','mst2_','mst3_']
        self.MERGERS = ['merger0.','merger1.','merger2.','merger3.']
        self.AWslave = {'slv0_':[],'slv1_':[],'slv2_':[],'slv3_':[]}
        self.AWmaster = {'mst0_':[],'mst1_':[],'mst2_':[],'mst3_':[]}
        self.Wslave = {}
        self.Wmaster = {}

    def run(self):
        if not self.Enable: return
        self.accumulate()
        self.clearing()

    def clearing(self):
        Remove = [] 
        for Wdata in self.Wslave:
            (Slv,sAwaddr,sAwid,sAwlen,sWlast) = self.Wslave[Wdata]
            if Wdata in self.Wmaster:
                (Mst,mAwaddr,mAwid,mAwlen,mWlast) = self.Wmaster[Wdata]
                Remove.append(Wdata)
                mLen = len(list(self.Wmaster.keys()))-len(Remove)
                sLen = len(list(self.Wslave.keys()))-len(Remove)
                logs.log_info('TRANS %s->%s %x  addr=%x / %x  last (%x,%x) awlen (%x,%x)   (m%d, s%d)' % (Mst,Slv,Wdata,mAwaddr,sAwaddr,mWlast,sWlast,mAwlen,sAwlen,mLen,sLen),'trf')
        for Wdata in Remove:
            self.Wslave.pop(Wdata)
            self.Wmaster.pop(Wdata)
        Str = ''
        for Wdata in self.Wslave:
            Str += ' %x' % Wdata
        if Str != '':
            logs.log_info('SWDATA %s' % Str,'trf')


    def accumulate(self):
        for Slv in self.SLAVES:
            if self.valid(Slv+'awvalid') and self.valid(Slv+'awready'):
                Awlen = self.peek(Slv+'awlen')
                Awid = self.peek(Slv+'awid')
                Awaddr = self.peek(Slv+'awaddr')
                self.AWslave[Slv].append((Awaddr,Awid,Awlen))

            if self.valid(Slv+'wvalid') and self.valid(Slv+'wready'):
                Wdata = self.peek(Slv+'wdata')
                Wstrb = self.peek(Slv+'wstrb')
                Wlast = self.peek(Slv+'wlast')
                if self.AWslave[Slv]==[]:
                    logs.log_error('AWslave queue of %s is empty on wdata=%x' % (Slv,Wdata))
                else:
                    (Awaddr,Awid,Awlen) = self.AWslave[Slv][0]
                    self.Wslave[Wdata] = (Slv,Awaddr,Awid,Awlen,Wlast)
                    if Wlast == 1:
                        self.AWslave[Slv].pop(0)
                    
        for Mst in self.MASTERS:
            if self.valid(Mst+'awvalid') and self.valid(Mst+'awready'):
                Awlen = self.peek(Mst+'awlen')
                Awid = self.peek(Mst+'awid')
                Awaddr = self.peek(Mst+'awaddr')
                NextAwaddr = (Awaddr<<2) & 0xffffffff
                self.AWmaster[Mst].append((Awaddr,Awid,Awlen))

            if self.valid(Mst+'wvalid') and self.valid(Mst+'wready'):
                Wdata = self.peek(Mst+'wdata')
                Wstrb = self.peek(Mst+'wstrb')
                Wlast = self.peek(Mst+'wlast')
                (Awaddr,Awid,Awlen) = self.AWmaster[Mst][0]
                self.Wmaster[Wdata] = (Mst,Awaddr,Awid,Awlen,Wlast)
                if Wlast == 1:
                    self.AWmaster[Mst].pop(0)



    def action(self,Txt):
        if 'enable' in Txt: 
            self.Enable = True
            return
        if 'disable' in Txt: 
            self.Enable = False
            return
    def onFinish(self):
        for Wdata in self.Wmaster:
            (Mst,Awaddr,Awid,Awlen,Wlast) =  self.Wmaster[Wdata] 
            logs.log_info('LEFT %x  = %s addr=%x wid=%x len=%x last=%x ' % (Wdata,Mst,Awaddr,Awid,Awlen,Wlast),'trf')
            
        for Mst in self.MASTERS:
            if self.valid(Mst+'wvalid') and not self.valid(Mst+'wready'):
                Wdata = self.peek(Mst+'wdata')
                Wstrb = self.peek(Mst+'wstrb')
                Wlast = self.peek(Mst+'wlast')
                logs.log_info('STUCK %s = %x %x %x' % (Mst,Wdata,Wstrb,Wlast),'trf')

        for Mrg in self.MERGERS:
            for Port in ['a_','b_','c_','d_']:
                if self.valid(Mrg+Port+'wvalid') and not self.valid(Mrg+Port+'wready'):
                    Wdata = self.peek(Mrg+Port+'wdata')
                    Wstrb = self.peek(Mrg+Port+'wstrb')
                    Wlast = self.peek(Mrg+Port+'wlast')
                    logs.log_info('STUCK %s.%s = %x %x %x' % (Mrg,Port,Wdata,Wstrb,Wlast),'trf')




    def busy(self):
        return False

