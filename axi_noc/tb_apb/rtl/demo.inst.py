

import os,sys,string,random
import veri
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs3'%NewName)
import logs
Monitors=[]
cycles=0
GIVEUP_TIMEOUT = 1000    # how many cycles to run before retirment. 

import sequenceClass
seq = sequenceClass.sequenceClass('tb',Monitors,'',[])


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
    veri.force('tb.paddr','0')
    veri.force('tb.pclk','0')
    veri.force('tb.penable','0')
    veri.force('tb.presetn','0')
    veri.force('tb.psel','0')
    veri.force('tb.pstrb','0')
    veri.force('tb.pwdata','0')
    veri.force('tb.pwrite','0')
    key0 = logs.peek('tb.key0')
    key1 = logs.peek('tb.key1')
    limits0 = logs.peek('tb.limits0')
    limits1 = logs.peek('tb.limits1')
    prdata = logs.peek('tb.prdata')
    prdata_wire = logs.peek('tb.prdata_wire')
    pready = logs.peek('tb.pready')
    pslverr = logs.peek('tb.pslverr')
