

import logs


class axiMonitorClass:
    def __init__(self,Path,Monitors,dataWidth=4,Renames={},Prefix='',Suffix=''):
        if Monitors != -1:
            Monitors.append(self)
        self.dataWidth = dataWidth
        self.Logs = 3
        self.Path = Path
        self.Renames = Renames
        self.Prefix = Prefix
        self.Suffix = Suffix
        self.AWQUEUE = []
        self.ARQUEUE = []
        self.RQUEUE = []
        self.RAM = {}
        self.BEXPECT = []
        self.WADDR = -1
        self.RADDR = -1

    def cannot_find_sig(self,Sig):
        logs.log_error('CANNOT FIND SIG %s' % Sig,self.Logs)


    def peek(self,Sig):
        Net = Sig
        if Sig in self.Renames:
            Net = self.Renames[Sig]
        if self.Prefix != '':
            Net = '%s%s' % (self.Prefix,Sig)
        if self.Suffix != '':
            Net = '%s%s' % (Sig,self.Suffix)
        return logs.peek('%s%s' % (self.Path,Net))

    def onFinish(self):
        logs.log_info('ONFINISH OF AXIMONITOR')
        if self.AWQUEUE != []:
            logs.log_error('onFinish axi monitor AWQUEUE not empty',self.Logs)
        if self.ARQUEUE != []:
            logs.log_error('onFinish axi monitor ARQUEUE not empty',self.Logs)
        if self.BEXPECT != []:
            logs.log_error('onFinish axi monitor BEXPECT not empty',self.Logs)

    def run(self):
        self.mon_aw()
        self.mon_w()
        self.mon_b()
        self.mon_ar()
        self.mon_r()

    def mon_aw(self):
        if (self.peek('awvalid') == 1)and(self.peek('awready') == 1):
            Addr = self.peek('awaddr')
            Len = self.peek('awlen')
            Size = self.peek('awsize')
            Burst = self.peek('awburst')
            Id = self.peek('awid')
            self.AWQUEUE.append((Addr,Len,Size,Burst,Id))
            if self.WADDR <0:
                self.WADDR = Addr

    def mon_w(self):
        if (self.peek('wvalid') == 1)and(self.peek('wready') == 1):
            Data = self.peek('wdata')
            Wstrb = self.peek('wstrb')
            Last = self.peek('wlast')
            (Addr,Len,Size,Burst,Id) = self.AWQUEUE[0]
            self.store(self.WADDR,Data,Wstrb)
            logs.log_info('WRITE ad=%x data=%x wstrb=%x' % (self.WADDR,Data,Wstrb),self.Logs)
            if Burst == 1:
                self.WADDR += self.dataWidth

            if Last == 1:
                (Addr,Len,Size,Burst,Id) = self.AWQUEUE.pop(0)
                self.BEXPECT.append(Id)
                if self.AWQUEUE == []:
                    self.WADDR = -1
                else:
                    self.WADDR = self.AWQUEUE[0][0]

    def mon_b(self):
        if (self.peek('bvalid') == 1)and(self.peek('bready') == 1):
            bid = self.peek('bid')
            bresp = self.peek('bresp')
            if bid in self.BEXPECT:
                Ind = self.BEXPECT.index(bid)
                self.BEXPECT.pop(Ind)
            else:
                logs.log_error('BVALID id=%d is not in BEXPECT queue %s' % (bid,self.BEXPECT),self.Logs)


    def mon_ar(self):
        if (self.peek('arvalid') == 1)and(self.peek('arready') == 1):
            Addr = self.peek('araddr')
            Len = self.peek('arlen')
            Size = self.peek('arsize')
            Burst = self.peek('arburst')
            Id = self.peek('arid')
            self.ARQUEUE.append((Addr,Len,Size,Burst,Id))
            if self.RADDR<0:
                self.RADDR = Addr

    def mon_r(self):
        if (self.peek('rvalid') == 1)and(self.peek('rready') == 1):
            Data = self.peek('rdata')
            Last = self.peek('rlast')
            Resp = self.peek('rresp')
            Rid = self.peek('rid')
            (Addr,Len,Size,Burst,Id) = self.ARQUEUE[0]
            Valids,Exp = self.load(self.RADDR)
            logs.log_ensure((Exp & Valids)==(Data & Valids),'READ ad=%x exp=%x act=%x last=%d rid %d<>%d' % (self.RADDR,Exp,Data,Last,Rid,Id),self.Logs)
            if Burst != 0:
                self.RADDR += self.dataWidth
            if Last:
                self.ARQUEUE.pop(0)
                if self.ARQUEUE == []:
                    self.RADDR = -1
                else:
                    self.RADDR = self.ARQUEUE[0][0]

    def store(self,Addr,Data,Wstrb):
        while Wstrb > 0:
            if (Wstrb & 1) == 1:
                self.RAM[Addr] = Data & 0xff
            Wstrb = Wstrb >> 1
            Data = Data >> 8
            Addr += 1
    def load(self,Addr):
        Res = 0
        Valids = 0
#        logs.log_info('XXX Addr=%x RAM = %s' % (Addr,list(map(hex,self.RAM.keys()))))
        for JJ in range(self.dataWidth):
            Ad = Addr + JJ
            if Ad in self.RAM:
                Val = self.RAM[Ad]
                Res += (Val<<(8*JJ))
                Valids += (0xff<<(8*JJ))
        return Valids,Res



