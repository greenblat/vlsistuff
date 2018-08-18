
import os,sys,string
import veri
import logs
class ramMonitorClass:
    runnum=0
    def __init__(self,Path,Prefix,Monitors,Print=False,Bwen=True):
        self.Prefix = Prefix
        self.Path = Path
        self.Active=False
        self.Print=Print
        self.Bwen=Bwen
        self.Ram={}

        Full = '%s.%s%s'%(self.Path,self.Prefix,'wdata')
        Full = veri.peek(Full)
        self.dataWidth = len(Full)
        self.strD = '%%0%dx'%(self.dataWidth/4)
        Full = '%s.%s%s'%(self.Path,self.Prefix,'addr')
        Full = veri.peek(Full)
        Len = len(Full)
        self.addrWidth = Len
        Monitors.append(self) 
        if self.Bwen:
            Bweb = self.peeks('bwen')
        else:
            Bweb = 0
        logs.log_info('ramMonitor #%d setup %s  dataw=%d addrw=%d bweb=%s'%(ramMonitorClass.runnum,self.Prefix,self.dataWidth,self.addrWidth,Bweb))

        ramMonitorClass.runnum += 1

    def peek(self,Who):
        Full = '%s.%s%s'%(self.Path,self.Prefix,Who)
        return logs.peek(Full)
    def peeks(self,Who):
        Full = '%s.%s%s'%(self.Path,self.Prefix,Who)
        return veri.peek(Full)
    def force(self,Who,What):
        Full = '%s.%s%s'%(self.Path,self.Prefix,Who)
        veri.force(Full,str(What))

    def run(self):
        if self.Active:
            self.Active=False
            if self.Addr in self.Ram:
                Rdata = self.Ram[self.Addr]
            else:
                Rdata = 0
            self.force('rdata',bin(Rdata))
            if self.Print:
                logs.log_info('ramMonitor  read %s ram %s [%x] -> %s'%(self.Path,self.Prefix,self.Addr,self.strD%Rdata))


        Ceb= self.peek('cen')
        Web= self.peek('wen')
        if (Web==0)and(Ceb==0):
            Addr= self.peek('addr')
            Wdata = self.peek('wdata')
            if Wdata== -1:
                logs.log_error('ramMonitor write %s ram %s [%x] <= XXXX'%(self.Path,self.Prefix,Addr))
                return
            if self.Bwen:
                Bweb = self.peek('bwen')
            else:
                Bweb = 0

            if Addr not in self.Ram:
                Was = 0
            else:
                Was = self.Ram[Addr]
            self.Ram[Addr]=(Wdata & ~Bweb)|(Was & Bweb)
            if self.Print:
                logs.log_info('ramMonitor write %s ram %s [%x] <= %s'%(self.Path,self.Prefix,Addr,self.strD%Wdata))
        elif (Web==1)and(Ceb==0):
            self.Active=True
            self.Addr= self.peek('addr')
        return


