
import os,sys
import veri
import logs
import random

class apbSlave(logs.driverClass):
    def __init__(self,Path,Monitors,Prefix='',Suffix='',Name='noName'):
        logs.driverClass.__init__(self,Path,Monitors)
        self.state = 'idle'
        self.RAM = {}
        self.prefix = Prefix
        self.suffix = Suffix
        self.READY = 0
        self.Name = Name


    def onFinish(self):
        return

    def busy(self):
        return (self.waiting!=0)or(self.state != 'idle')


    def prdata(self):
        Who,Act,Addr = self.Backs.pop(0)
        return Act

    def action(self,Cmd):
        logs.log_info('XXXXXXXX %s' % Cmd)
        wrds = Cmd.split()
        if wrds[0] == 'ready':
            self.READY = eval(wrds[1])
            return
        if wrds[0] == 'ram':
            Addr = self.eval(wrds[1])
            for X in wrds[2:]:
                Data = self.eval(X)
                self.RAM[Addr] = Data
                logs.log_info('SLV "%s" RAM %x -> [%x]' % (self.Name,Data,Addr))
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
        if self.waiting>0:
            self.waiting -= 1
            return
#        logs.forceAscii('tb.markstr0',self.state)
        if self.state == 'idle':
            self.lcl_force('pready',0)
            if self.lcl_valid('psel'):
                self.state = 'work'
                self.addr = self.lcl_peek('paddr')
                self.pwrite = self.lcl_peek('pwrite')
                self.waiting = self.READY
        elif self.state == 'work':
            self.lcl_force('pready',1)
            if self.lcl_valid('penable'):
                if self.pwrite == 1:
                    self.wdata = self.lcl_peek('pwdata')
                    self.RAM[self.addr] = self.wdata
                    logs.log_info('APBSLAVE %s write %x %x' % (self.Name,self.addr,self.wdata))
                else:
                    if self.addr not in self.RAM:
                        self.RAM[self.addr] = random.randint(0,0xffffffff)
                    self.lcl_force('prdata',self.RAM[self.addr])
                    logs.log_info('APBSLAVE %s read %x %x' % (self.Name,self.addr,self.RAM[self.addr]))
                self.state = 'idle'
