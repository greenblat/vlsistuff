

import logs


class axiMonitorClass:
    def __init__(self,Path,Monitors,dataWidth=4,Renames={},Prefix='',Suffix='', Name='mon1'):
        if Monitors != -1:
            Monitors.append(self)
        self.dataWidth = dataWidth
        self.Name = Name
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
        self.WLEN = -1
        self.RADDR = []
        self.RespRAM = {}
        self.RespADDR = 0
        self.verbose = True
        self.checkRam = False
        self.verify_read_mem = True

    def cannot_find_sig(self,Sig):
        logs.log_error('CANNOT FIND SIG %s' % Sig,self.Logs)

    def action(self,Txt):
        wrds = Txt.split()
        if wrds==[]:
            pass
        elif wrds[0]== 'verbose':
            self.verbose = eval(wrds[1])
        elif wrds[0]== 'checkRam':
            self.checkRam = eval(wrds[1])
        else:
            logs.log_error('action of axi monitor accepts only "verbose" or "checkRam" directives, not "%s"' % Txt)

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
        self.log_info_msg('ONFINISH OF AXIMONITOR')
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
            if self.AWQUEUE != []:
                (Addr,Len,Size,Burst,Id) = self.AWQUEUE[0]
            else:
                logs.log_wrong("MON_W got empty AWQUQUE")
                (Addr,Len,Size,Burst,Id) = (0,0,0,0,5)
            self.store(self.RAM, self.WADDR,Data,Wstrb)
            self.log_info_msg('AXIMON %s WRITE ad=0x%x wlen=%d data=0x%x (%d) wstrb=%x' % (self.Name,self.WADDR,self.WLEN,Data,Data,Wstrb),Which=self.Logs)
            if Burst == 1:
                self.WADDR += self.dataWidth
            self.WLEN -= 1

            if Last == 1:
                if self.AWQUEUE != []:
                    (Addr,Len,Size,Burst,Id) = self.AWQUEUE.pop(0)
                else:
                    logs.log_wrong("MON_W (2)  got empty AWQUQUE")
                    Id = 5
                self.BEXPECT.append(Id)
                if self.AWQUEUE == []:
                    self.WADDR = -1
                    self.WLEN = -1
                else:
                    self.WADDR = self.AWQUEUE[0][0]
                    self.WLEN = self.AWQUEUE[0][1]

    def mon_b(self):
        if (self.peek('bvalid') == 1)and(self.peek('bready') == 1):
            bid = self.peek('bid')
            bresp = self.peek('bresp')
            if bid in self.BEXPECT:
                Ind = self.BEXPECT.index(bid)
                self.BEXPECT.pop(Ind)
            else:
                if self.BEXPECT!=[]: self.BEXPECT.pop(0)
                logs.log_error('BVALID id=%d is not in BEXPECT queue %s' % (bid,self.BEXPECT),self.Logs)


    def mon_ar(self):
        if (self.peek('arvalid') == 1)and(self.peek('arready') == 1):
            Addr = self.peek('araddr')
            Len = self.peek('arlen')
            Size = self.peek('arsize')
            Burst = self.peek('arburst')
            Id = self.peek('arid')
            self.ARQUEUE.append((Addr,Len,Size,Burst,Id))
            if Burst == 2:
                Mask0 = ~len(bin((1<<Size)*(Len+1)))-2
                AddrLo = Addr & Mask0
                AddrHi = AddrLo + (1<<Size)*(Len+1)
                Addrs = [Addr]
                for x in range(Len):
                    X = Addr + (1<<Size)
                    if X>=AddrHi:
                        Addrs.append(AddrLo)
                        Addr = AddrLo
                    else:
                        Addrs.append(X)
                        Addr = X
            elif Burst == 1:
                Addrs = [Addr]
                for x in range(Len):
                    X = Addr + (1<<Size)
                    Addrs.append(X)
                    Addr = X
            else:
                Addrs = (Len+1) * [Addr]
            self.RADDR.extend(Addrs)

    def mon_r(self):
        if (self.peek('rvalid') == 1)and(self.peek('rready') == 1):
            Data = self.peek('rdata')
            Last = self.peek('rlast')
            Resp = self.peek('rresp')
            Rid = self.peek('rid')
            if self.ARQUEUE == []:
                logs.log_error('RVALID and ARQUEUE is empty data=%x rid=%x' % (Data,Rid))
                return
            (Addr,Len,Size,Burst,Id) = self.ARQUEUE[0]
            if self.verify_read_mem:
                Valids,Exp = self.load(self.RADDR[0])
                logs.log_ensure(((Exp & Valids)==(Data & Valids)) and (Data>=0),'READ vlds=%x rresp=%x ad=%x exp=%x act=%x last=%d rid %d<>%d' % (Valids,Resp,self.RADDR[0],Exp,Data,Last,Rid,Id),self.Logs)
            self.RADDR.pop(0)
            if Last == 1:
                self.ARQUEUE.pop(0)
            self.store(self.RespRAM, self.RespADDR, Data)
            self.log_info_msg("RespRAM: Write {data} to address: {address}".format(data=Data, address=self.RespADDR))
            self.RespADDR += self.dataWidth

    def store(self, memory, Addr, Data, Wstrb=None):
        if Wstrb is None:  # if no Wstrb, assume all data is valid
            Wstrb = int('1'*self.dataWidth, base=2)
        while Wstrb > 0:
            if (Wstrb & 1) == 1:
                memory[Addr] = Data & 0xff
            Wstrb = Wstrb >> 1
            Data = Data >> 8
            Addr += 1

    def load(self,Addr, readSize=None, memtype='RAM'):
        if not self.checkRam:
            return False,0
        if memtype == 'RAM':
            mem = self.RAM
        if memtype == "RespRAM":
            mem = self.RespRAM
        dataWidth = self.dataWidth
        if readSize is not None:
            dataWidth = readSize
        Res = 0
        Valids = 0
#        log_info_msg('XXX Addr=%x RAM = %s' % (Addr,list(map(hex,self.RAM.keys()))))
        for JJ in range(dataWidth):
            Ad = Addr + JJ
            if Ad in mem:
                Val = mem[Ad]
                Res += (Val<<(8*JJ))
                Valids += (0xff<<(8*JJ))
        return Valids,Res

    def log_info_msg(self, msg, Which=0):
        prefix = "[" + self.Name + "]: "
        full_msg = prefix + msg
        logs.log_info(full_msg, Which=Which, verbose=self.verbose)



