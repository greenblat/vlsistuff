
'''
    apb = apbSlave.apbSlave('tb.cpu',Monitors,'apb')
    apb.translations['setupreg']=0x100
    apb.write(Addr,Data)
    apb.read(Addr)
    apb.wait(100)


'''

import os,sys,string,types
import veri
import logs


class apbSlave:
    def __init__(self,Path,Monitors,Name='optional'):
        self.Path = Path
        self.Name = Name

        self.RAM = {}
        self.waiting=0
        Monitors.append(self)

    def peek(self,Sig):
        Full = '%s.%s'%(self.Path,Sig)
        return logs.peek(Full)

    def valid(self,Sig):
        return (self.peek(Sig)==1)


    def force(self,Sig,Val):
        veri.force('%s.%s'%(self.Path,Sig),str(Val))


    def run(self):
        if self.waiting>0:
            self.waiting -= 1
            return
        self.force('pready',1)
#        print('psel',self.peek('psel'),self.valid('psel'))
#        print('aaaaaa',self.peek('paddr'),self.valid('pwrite'),self.valid('penable'),self.valid('psel'))
        if self.valid('psel'):
            self.addr = self.peek('paddr')
            if self.valid('pwrite'):
                if self.valid('penable'):
                    self.pwdata = self.peek('pwdata')
                    self.RAM[self.addr]=self.pwdata
                    logs.log_info('slave wrie addr=%x wdata=%08x'%(self.addr,self.pwdata))
            elif self.valid('penable'):            
                if self.addr not in self.RAM:
                    self.RAM[self.addr]=0xdeadbeef;
                self.force('prdata',self.RAM[self.addr])
                logs.log_info('slave read addr=%x rdata=%08x'%(self.addr,self.RAM[self.addr]))


