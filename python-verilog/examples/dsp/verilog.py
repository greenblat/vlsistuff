

import os,sys,string,random
import veri
sys.path.append('../vlibs/')
import logs


import traceback
import fir

fir = fir.firClass('tb.fir')

cycles=0
def negedge():
    global cycles
    rst_n = veri.peek('tb.rst_n')
    if (rst_n!='1'):
        return
    cycles += 1
    veri.force('tb.cycles',str(cycles))
    if (cycles==10):
        veri.force('tb.errors','0')
        veri.force('tb.corrects','0')
        veri.force('tb.wrongs','0')
    if (cycles>10):
        monitors()
        apb.run()
        scenario.run()
        fir.run()



class scenarioClass:
    def __init__(self):
        self.queue=[]
        self.readfile('test.scenario')
        self.waiting=0

    def readfile(self,Fname):
        File = open(Fname)
        lines = File.readlines()
        File.close()
        self.queue.extend(lines)
    def run(self):
        if self.waiting>0:
            self.waiting -= 1
            return

        if self.queue==[]: return

        line = self.queue.pop(0)
        wrds = string.split(line)
        if len(wrds)>0:
            if wrds[0]=='finish':
                veri.finish()
                return
            if wrds[0]=='wait':
                self.waiting = int(wrds[1])
                return

            if wrds[0]=='apb':
                Addr = eval(wrds[1])            
                Data = eval(wrds[2])            
                apb.wrqueue.append((Addr,Data))
                return
            if wrds[0]=='force':
                veri.force(wrds[1],wrds[2])
                return

            logs.log_error('what is "%s"'%(line))
            
scenario = scenarioClass()



class ahbClass:
    def __init__(self,Path,Prefix):
        self.hwdata = '%s.%shwdata'%(Path,Prefix) 
        self.hsel   = '%s.%shsel'%(Path,Prefix) 
        self.htrans = '%s.%shtrans'%(Path,Prefix) 
        self.haddr  = '%s.%shaddr'%(Path,Prefix) 
        self.hwrite = '%s.%shwrite'%(Path,Prefix) 
        self.wrqueue=[]
        self.state='idle'
        self.waiting=0
        self.Path=Path

    def run(self):
        if self.state == 'window':
            monitor_all_haddrs('ahb: %08x %08x '%(self.Addr,self.Data))

        print 'apb',self.state,self.waiting,self.Addr,self.Data
        if self.waiting>0: 
            self.waiting -= 1
            return
        ext_core_rst_n = veri.peek('%s.ext_core_rst_n'%self.Path)
        veri.force('%s.tl42x_ocem_core_rst_r'%self.Path,ext_core_rst_n)
        logs.log_info('ahb rst=%s state=%s'%(ext_core_rst_n,self.state))
        if ext_core_rst_n=='0': return

        if self.state=='idle':
            if self.wrqueue==[]: return
            self.Addr,self.Data=self.wrqueue.pop(0)
            self.state='addr'
            return

        if self.state=='addr':
            veri.force(self.haddr,'0x%x'%self.Addr)
            veri.force(self.hwrite,'1')
            veri.force(self.htrans,'3')
            veri.force(self.hsel,'1')
            veri.force(self.hwdata,'0x%x'%self.Data)
            self.state='addr1'
        elif self.state=='addr1':
            veri.force(self.hwrite,'0')
            veri.force(self.htrans,'3')
            veri.force(self.hsel,'1')
            self.state='addr2'
        elif self.state=='addr2':
            veri.force(self.hwrite,'0')
            veri.force(self.htrans,'3')
            veri.force(self.hsel,'1')
            self.waiting=2
            self.state='window'
        elif self.state=='window':
            self.state='idle'
        

# 'paddr psel psize pwrite pwdata prdata penable'
class apbClass:
    def __init__(self,Path,Sigs):
        wrds = string.split(Sigs)
        self.paddr   = '%s.%s'%(Path,wrds[0]) 
        self.psel    = '%s.%s'%(Path,wrds[1]) 
        self.psize    = '%s.%s'%(Path,wrds[2]) 
        self.pwrite  = '%s.%s'%(Path,wrds[3]) 
        self.pwdata  = '%s.%s'%(Path,wrds[4]) 
        self.prdata  = '%s.%s'%(Path,wrds[5]) 
        self.penable  = '%s.%s'%(Path,wrds[6]) 
        self.wrqueue=[]
        self.state='idle'
        self.waiting=0
        self.Path=Path
        self.Addr=0
        self.Data=0

    def run(self):
        if self.waiting>0: 
            self.waiting -= 1
            return

        if self.state=='idle':
            if self.wrqueue==[]: return
            self.Addr,self.Data=self.wrqueue.pop(0)
            self.state='addr'
            return

        if self.state=='addr':
            veri.force(self.paddr,'0x%x'%self.Addr)
            veri.force(self.pwrite,'1')
            veri.force(self.penable,'0')
            veri.force(self.psel,'1')
            veri.force(self.psize,'3')
            veri.force(self.pwdata,'0x%x'%self.Data)
            self.state='addr1'
        elif self.state=='addr1':
            veri.force(self.penable,'1')
            self.state='addr2'
        elif self.state=='addr2':
            veri.force(self.paddr,'0')
            veri.force(self.pwrite,'0')
            veri.force(self.penable,'0')
            veri.force(self.psel,'0')
            veri.force(self.pwdata,'0')
            self.waiting=2
            self.state='window'
        elif self.state=='window':
            self.state='idle'
        



class axiClass:
    def __init__(self,Path):
        self.Path=Path
        self.state='idle'
        self.wrqueue=[]
        self.Addr=-1
        self.Data=-1
        self.Size=2
        self.Kind = False
        self.waiting=0
        self.Area = False

    def write(self,Addr,Data,Note=''):
        self.wrqueue.append(('write',Addr,Data,Note))
    def read(self,Addr,Data,Note=''):
        self.wrqueue.append(('read',Addr,Data,Note))
        
    def run(self,Area):
        if self.state=='read':
            md_rvalid = veri.peek('%s.md_rvalid'%self.Path)
            if md_rvalid == '1':
                md_rdata = logs.peek('%s.md_rdata'%self.Path)
                md_rresp = logs.peek('%s.md_rresp'%self.Path)
                md_rid = logs.peek('%s.md_rid'%self.Path)
                logs.log_info('read addr=0x%x data=0x%x %x %x %s %s'%(self.Addr,md_rdata,md_rresp,md_rid,Area,self.Note))
                self.state='idle'
                self.waiting=100

        if self.waiting>0: 
            self.waiting -= 1
            if (self.waiting<5)and(self.state=='read'):
                logs.log_info('read addr=%0x%x didnt end'%(self.Addr))
                self.state='idle'
            return
        ext_core_rst_n = veri.peek('%s.ext_core_rst_n'%self.Path)
        veri.force('%s.tl42x_ocem_core_rst_r'%self.Path,ext_core_rst_n)
        if ext_core_rst_n=='0': return

        if self.state=='idle':
            if self.wrqueue==[]: return
            self.Kind,self.Addr,self.Data,self.Note=self.wrqueue.pop(0)
            self.state='addr'
            return

        if self.state=='addr':
            Ok = self.driveAddr(self.Addr,True)
            if Ok: self.state='addr1'
        elif self.state=='addr1':
            self.driveAddr(self.Addr,False)
            self.waiting=2
            if self.Kind=='write':
                self.state='data'
            else:
                self.state='read'
                self.waiting=100
        elif self.state=='data':
            Ok = self.driveData(self.Data,True)
            if Ok: self.state='after'
        elif self.state=='after':
            self.driveData(self.Data,False)
            if self.Area:
                Area = self.Area
            logs.log_info('written addr=0x%x data=0x%x %s %s'%(self.Addr,self.Data,Area,self.Note))
            self.state='window'
            self.waiting=100
        elif self.state=='window':
            self.state='idle'


    def driveAddr(self,Address,Drive=True):
        if self.Kind=='write':
            return self.driveWriteAddr(Address,Drive)
        else:
            return self.driveReadAddr(Address,Drive)

    def driveWriteAddr(self,Address,Drive):
        if not Drive:
            veri.force('%s.awaddr_r'%self.Path,'0')
            veri.force('%s.awid_r'%self.Path,'0')
            veri.force('%s.awsize_r'%self.Path,'0')
            veri.force('%s.awvalid_r'%self.Path,'0')
            veri.force('%s.awlen_r'%self.Path,'0')
            veri.force('%s.awburst_r'%self.Path,'0')
            return True
        md_awready = veri.peek('%s.md_awready'%self.Path)
        if md_awready=='0': return False
        veri.force('%s.awaddr_r'%self.Path,str(Address))
        veri.force('%s.awid_r'%self.Path,'0')
        veri.force('%s.awsize_r'%self.Path,str(self.Size))
        veri.force('%s.awvalid_r'%self.Path,'1')
        veri.force('%s.awlen_r'%self.Path,'0')
        veri.force('%s.awburst_r'%self.Path,'1')
        return True
    def driveReadAddr(self,Address,Drive):
        if not Drive:
            veri.force('%s.araddr_r'%self.Path,'0')
            veri.force('%s.arid_r'%self.Path,'0')
            veri.force('%s.arsize_r'%self.Path,'0')
            veri.force('%s.arvalid_r'%self.Path,'0')
            veri.force('%s.arlen_r'%self.Path,'0')
            veri.force('%s.arburst_r'%self.Path,'0')
            return True
        md_awready = veri.peek('%s.md_arready'%self.Path)
        if md_awready=='0': return False
        veri.force('%s.araddr_r'%self.Path,str(Address))
        veri.force('%s.arid_r'%self.Path,'0')
        veri.force('%s.arsize_r'%self.Path,str(self.Size))
        veri.force('%s.arvalid_r'%self.Path,'1')
        veri.force('%s.arlen_r'%self.Path,'0')
        veri.force('%s.arburst_r'%self.Path,'1')
        return True
    
    def driveData(self,Data,Drive=True):    
        if not Drive:
            veri.force('%s.wid_r'%self.Path,'0')
            veri.force('%s.wdata_r'%self.Path,'0')
            veri.force('%s.wid_r'%self.Path,'0')
            veri.force('%s.wstrb_r'%self.Path,'0')
            veri.force('%s.wvalid_r'%self.Path,'0')
            veri.force('%s.wlast_r'%self.Path,'0')
            return True
            
        md_bready = veri.peek('%s.md_bready'%self.Path)
        if md_bready=='0': return False
        veri.force('%s.wdata_r'%self.Path,str(Data))
        veri.force('%s.wid_r'%self.Path,'0')
        veri.force('%s.wstrb_r'%self.Path,'0xff')
        veri.force('%s.wvalid_r'%self.Path,'1')
        veri.force('%s.wlast_r'%self.Path,'1')
        return True


def makeString(Bits):
    res = ''
    while Bits!='':
        Char0 = Bits[-8:]
        Bits = Bits[:-8]
        Code = int(Char0,2)
        if Code==0: return res
        Char = chr(Code)
        res = Char + res
    return res
        
    

apb = apbClass('tb','paddr psel psize pwrite pwdata prdata penable')


MONREG = string.split(' enables start0 start1 start2 jump0 jump1 jump2 gain0 gain1')
monVals={}
def monitors():
    for Reg in MONREG:
        Now = logs.peek('tb.generator.%s'%Reg)
        if Reg not in monVals:
            monVals[Reg]= -1
        if monVals[Reg]!=Now:
            logs.log_info('register change %s %d -> %d'%(Reg,monVals[Reg],Now))
        monVals[Reg]=Now



