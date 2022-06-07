
import os,sys
import veri
import logs

class apbSlave(logs.driverClass):
    def __init__(self,Path,Monitors,Prefix,Suffix,Name='noName'):
        logs.driverClass.__init__(self,Path,Monitors)
        self.state = 'idle'
        self.RAM = {}
        self.prefix = Prefix
        self.suffix = Suffix


    def onFinish(self):
        return

    def busy(self):
        return False


    def prdata(self):
        Who,Act,Addr = self.Backs.pop(0)
        return Act

    def action(self,Cmd):
        wrds = Cmd.split()
        if wrds[0] == 'ram':
            Addr = eval(wrds[1])
            for X in wrds[2:]:
                Data = eval(X)
                self.RAM[Addr] = Data
                Addr += 4
            return
        logs.log_error('action not recogninzed "%s"'%Cmd)

    def rename(self,Sig):
        if self.suffix != '': Sig = Sig + self.suffix
        if self.prefix != '': Sig = self.prefix + Sig
        return Sig
        
    def lcl_force(self,Sig,Val):
        Sig = self.rename(Sig)
        self.force(Sig,Val)

    def lcl_peek(self,Sig):
        Sig = self.rename(Sig)
        return self.peek(Sig)

    def lcl_valid(self,Sig):
        Sig = self.rename(Sig)
        return self.valid(Sig)

    def run(self):
        if self.state == 'idle':
            self.lcl_force('pready',0)
            if self.lcl_valid('psel'):
                self.state = 'work'
                self.addr = self.lcl_peek('paddr')
                self.pwrite = self.lcl_peek('pwrite')
        elif self.state == 'work':
            self.lcl_force('pready',1)
            if self.lcl_valid('penable'):
                if self.pwrite == 1:
                    self.wdata = self.lcl_peek('pwdata')
                    self.RAM[self.addr] = self.wdata
                    logs.log_info('APBSLAVE %s write %x %x' % (self.Name,self.addr,self.wdata))
                else:
                    if self.addr not in self.RAM:
                        self.RAM[self.addr] = 0
                    self.lcl_force('prdata',self.RAM[self.addr])
                    logs.log_info('APBSLAVE %s read %x %x' % (self.Name,self.addr,self.RAM[self.addr]))
                self.state = 'idle'
