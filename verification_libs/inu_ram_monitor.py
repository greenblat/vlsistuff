import veri
import logs
class ramMonitorClass:
    def __init__(self,Path,Prefix,Monitors,Print=False):
        self.Prefix = Prefix
        self.Path = Path
        self.Active=False
        self.Print=Print
        self.Ram={}

        Full = '%s.%s_%s'%(self.Path,self.Prefix,'outputs')
        Full = veri.peek(Full)
        self.dataWidth = len(Full)
        Full = '%s.%s_%s'%(self.Path,self.Prefix,'inputs')
        Full = veri.peek(Full)
        Len = len(Full)
        if Len>(self.dataWidth*2):
            self.addrWidth = Len - 2 - (self.dataWidth*2)
            self.Bweb=True
        else:
            self.addrWidth = Len - 2 - (self.dataWidth)
            self.Bweb=False
        Monitors.append(self) 
        logs.log_info('ramMonitor setup %s bweb=%s  dataw=%d addrw=%d'%(self.Prefix,self.Bweb,self.dataWidth,self.addrWidth))

    def peek(self,Who):
        Full = '%s.%s_%s'%(self.Path,self.Prefix,Who)
        return veri.peek(Full)
    def force(self,Who,What):
        Full = '%s.%s_%s'%(self.Path,self.Prefix,Who)
        veri.force(Full,str(What))

    def run(self):
        if self.Active:
            self.Active=False
            if self.Addr in self.Ram:
                Rdata = self.Ram[self.Addr]
            else:
                Rdata = 0
            self.force('outputs',bin(Rdata))
            if self.Print:
                logs.log_info('read ram %s [%x] -> %x'%(self.Prefix,self.Addr,Rdata))


        Access= self.peek('inputs')
        Ceb = Access[-1]
        Web = Access[-2]
        Access = Access[:-2]
        if self.Bweb:
            Bweb = Access[-self.dataWidth:]
            Access = Access[:-self.dataWidth]
        else:
            Bweb='0'*self.dataWidth
        
        Addr = logs.intx(Access[-self.addrWidth:])
        Access = Access[:-self.addrWidth]

        Wbits = logs.intx(Bweb)
        Wdata = logs.intx(Access)

        if (Web=='0')and(Ceb=='0'):
            if Addr in self.Ram:
                Rdata = self.Ram[Addr]
            else:
                Rdata = 0
            newData = (~Wbits & Wdata)|((Wbits) & Rdata)
            self.Ram[Addr]=newData
            if self.Print:
                logs.log_info('write ram %s [%x] <= %x    (%x&%x)|(%x&%x)'%(self.Prefix,Addr,newData,Wdata,Wbits,(~Wbits),Rdata))
        elif (Web=='1')and(Ceb=='0'):
            self.Active=True
            self.Addr=Addr
        return


