
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
        self.Uart = False


    def onFinish(self):
        return

    def busy(self):
        return (self.waiting!=0)or(self.state != 'idle')


    def prdata(self):
        Who,Act,Addr = self.Backs.pop(0)
        return Act
    def write(self,Addr,Data):
        if type(Data) is list:
            for Dd in Data:
                self.write(Addr,Dd)
                Addr += 4
        else:
            self.RAM[Addr] = Data
            if self.Uart:
                self.Uart('ram',Addr,Data)
        logs.log_info('SLV "%s" RAM %s -> [%s]' % (self.Name,hex(Addr)))
        
    def action(self,Cmd,Orig=[]):
        wrds = Cmd.split()
        if wrds[0] == 'ready':
            self.READY = eval(wrds[1])
            return
        if wrds[0] in ['write','ram']:
            Addr = self.eval(wrds[1])
            for X in wrds[2:]:
                Data = self.eval(X)
                self.RAM[Addr] = Data
                if self.Uart:
                    self.Uart('ram',Addr,Data)
                logs.log_info('SLV "%s" RAM %s -> [%s]' % (self.Name,hex(Data),hex(Addr)))
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
        logs.forceAscii('tb.markstr0',self.state)
        if self.state == 'idle':
            self.lcl_force('pready',0)
            if self.lcl_valid('psel'):
                self.state = 'work'
                self.addr = self.lcl_peek('paddr')
                self.pwrite = self.lcl_peek('pwrite')
                self.waiting = self.READY
        elif self.state == 'work':
            self.lcl_force('pready',1)
            self.addr = self.lcl_peek('paddr')
            self.pwrite = self.lcl_peek('pwrite')
            self.pstrb = self.lcl_peek('pstrb')
            if self.lcl_valid('penable'):
                logs.log_info('APBWRITE %s %s write %x' % (self.Name,self.pwrite,self.addr))
                if self.pwrite == 1:
                    self.wdata = self.lcl_peek('pwdata')
                    if self.addr&0xfffc not in self.RAM:
                        was = 0
                    else:
                        was = self.RAM[self.addr&0xfffc]
                    mask = 0
                    if self.pstrb & 1: mask = 0xff
                    if self.pstrb & 2: mask += 0xff00
                    if self.pstrb & 4: mask += 0xff0000
                    if self.pstrb & 8: mask += 0xff000000

                    now_data = was & ~mask | self.wdata & mask
                    self.RAM[self.addr&0xfffc] = now_data
                    logs.log_info('APBSLAVE %s write %x %x strb=%x now_data=%x' % (self.Name,self.addr,self.wdata,self.pstrb,now_data))
                else:
                    Addr = self.addr & 0xfffffffc;
                    if Addr not in self.RAM:
                        self.RAM[Addr] = self.addr
                        logs.log_info('APBSLAVE %s invent read %x %x' % (self.Name,self.addr,self.RAM[Addr]))
                    self.lcl_force('prdata',self.RAM[Addr])
                self.state = 'idle'
