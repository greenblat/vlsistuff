
import os,sys
import veri
import logs

class apbSlave(logs.driverClass):
    def __init__(self,Path,Monitors,Translations={},Name='noName'):
        logs.driverClass.__init__(self,Path,Monitors)
        self.state = 'idle'
        self.RAM = {}


    def onFinish(self):
        return

    def busy(self):
        return False


    def prdata(self):
        Who,Act,Addr = self.Backs.pop(0)
        return Act

    def action(self,Cmd):
        logs.log_error('action not recogninzed "%s"'%Cmd)

        
    def run(self):
        if self.state == 'idle':
            self.force('pready',0)
            if self.valid('psel'):
                self.state = 'work'
                self.addr = self.peek('paddr')
                self.pwrite = self.peek('pwrite')
        elif self.state == 'work':
            self.force('pready',1)
            if self.pwrite == 1:
                self.wdata = self.peek('pwdata')
                self.RAM[self.addr] = self.wdata
                logs.log_info('APBSLAVE %s write %x %x' % (self.Name,self.addr,self.wdata))
            else:
                if self.addr not in self.RAM:
                    self.RAM[self.addr] = 0
                self.force('prdata',self.RAM[self.addr])
                logs.log_info('APBSLAVE %s read %x %x' % (self.Name,self.addr,self.RAM[self.addr]))
            self.state = 'idle'
