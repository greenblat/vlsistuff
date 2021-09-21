

import os,sys,string,random
import veri
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs3'%NewName)
import logs
Monitors=[]
cycles=0
GIVEUP_TIMEOUT = 1000    # how many cycles to run before retirment. 


import axiMaster

mst = axiMaster.axiMasterClass('tb',Monitors)


import sequenceClass
seq = sequenceClass.sequenceClass('tb',Monitors,'',[('mst',mst)])


def pymonname(Name):
    logs.pymonname(Name)



def sequence(TestName):
    Seq = logs.bin2string(TestName)
    seq.readfile(Seq)
    logs.setVar('sequence',Seq)
    Dir = os.path.dirname(Seq)
    logs.setVar('testsdir',Dir)
    logs.log_info('SEQUENCE %d'%len(seq.Sequence))


def cannot_find_sig(Sig):
    logs.log_error('cannot find "%s" signal in the design'%Sig)




class driverMonitor(logs.driverClass):
    def __init__(self,Path,Monitors):
        logs.driverClass.__init__(self,Path,Monitors)
#        Monitors.append(self)
#        self.Path = Path
#        self.state='idle'
#        self.waiting  = 0
#
#    def force(self,Sig,Val):
#        veri.force('%s.%s'%(self.Path,Sig),str(Val))
#
#    def peek(self,Sig):
#        return logs.peek('%s.%s'%(self.Path,Sig))
#    def peeksigned(self,Sig):
#        return logs.peeksigned('%s.%s'%(self.Path,Sig))
#
#    def valid(self,Sig):
#        return self.peek(Sig)==1
#
    def run(self):
        if self.waiting>0:
            self.waiting -= 1
        elif self.state=='idle':
            self.state='work0'
        elif self.state=='work0':
            self.state='work1'
        elif self.state=='work1':
            self.state='idle'


        if self.valid('validin')and self.valid('takenin'):
            return

# example of driver class usage
# driverMonitor('tb',Monitors)



def negedge():
    global cycles
    cycles += 1
    veri.force('tb.cycles',str(cycles))
    if (cycles>GIVEUP_TIMEOUT):
        logs.log_info('finishing on default guard of %d'%GIVEUP_TIMEOUT)
        veri.finish()
    rst_n = veri.peek('tb.rst_n')
    if (rst_n!='1'):
        return

    if (cycles==30):
        veri.listing('tb','100','deep.list')
    if (cycles>30):
        for Mon in Monitors: Mon.run()

def cucu():
    veri.force('tb.araddr','0')
    veri.force('tb.arburst','0')
    veri.force('tb.arcache','0')
    veri.force('tb.arid','0')
    veri.force('tb.arlen','0')
    veri.force('tb.arprot','0')
    veri.force('tb.arqos','0')
    veri.force('tb.arsize','0')
    veri.force('tb.arvalid','0')
    veri.force('tb.awaddr','0')
    veri.force('tb.awburst','0')
    veri.force('tb.awcache','0')
    veri.force('tb.awid','0')
    veri.force('tb.awlen','0')
    veri.force('tb.awprot','0')
    veri.force('tb.awqos','0')
    veri.force('tb.awsize','0')
    veri.force('tb.awvalid','0')
    veri.force('tb.bready','0')
    veri.force('tb.prdata','0')
    veri.force('tb.pready','0')
    veri.force('tb.presp','0')
    veri.force('tb.rready','0')
    veri.force('tb.wdata','0')
    veri.force('tb.wlast','0')
    veri.force('tb.wstrb','0')
    veri.force('tb.wvalid','0')
    arready = logs.peek('tb.arready')
    awready = logs.peek('tb.awready')
    bid = logs.peek('tb.bid')
    bresp = logs.peek('tb.bresp')
    bvalid = logs.peek('tb.bvalid')
    paddr = logs.peek('tb.paddr')
    penable = logs.peek('tb.penable')
    psel = logs.peek('tb.psel')
    pstrb = logs.peek('tb.pstrb')
    pwdata = logs.peek('tb.pwdata')
    pwrite = logs.peek('tb.pwrite')
    rdata = logs.peek('tb.rdata')
    rid = logs.peek('tb.rid')
    rlast = logs.peek('tb.rlast')
    rresp = logs.peek('tb.rresp')
    rvalid = logs.peek('tb.rvalid')
    wready = logs.peek('tb.wready')
