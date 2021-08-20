

import os,sys,random
import veri
NewName = os.path.expanduser('~')
sys.path.append('%s/vlsistuff/verification_libs3'%NewName)
import logs
Monitors=[]
cycles=0
GIVEUP_TIMEOUT = 10000    # how many cycles to run before retirment. 


import encrypt_piped_efficiency
enc = encrypt_piped_efficiency.encrypt_piped_efficiency('tb.dut.',Monitors)
enc.run = enc.run_posedge_clk



import sequenceClass
seq = sequenceClass.sequenceClass('tb',Monitors,'',[])


def sequence(TestName):
    Seq = logs.bin2string(TestName)
    seq.readfile(Seq)
    logs.setVar('sequence',Seq)
    Dir = os.path.dirname(Seq)
    logs.setVar('testsdir',Dir)
    logs.log_info('SEQUENCE %d'%len(seq.Sequence))


def cannot_find_sig(Sig):
    logs.log_error('cannot find "%s" signal in the design'%Sig)


KEY = '0x0123456789abcdef4455667788'

class driverMonitor(logs.driverClass):
    def __init__(self,Path,Monitors):
        logs.driverClass.__init__(self,Path,Monitors)
        self.QUEUE = []
    def run(self):
        self.force('key',KEY)
        vldin = int(random.randint(0,100)>75)
        if vldin:
            datain = random.randint(0,0xffffffff)
            self.force('datain',datain)
            self.QUEUE.append(datain)
        else:
            self.force('datain',0)
        self.force('vldin',vldin)

        if self.valid('vldout'):
            dataout = self.peek('encrypted')
            In = self.QUEUE.pop(0)
            logs.log_info('IN %08x OUT %08x' % (In,dataout))


drv =  driverMonitor('tb',Monitors)



def negedge():
    global cycles
    cycles += 1
    veri.force('tb.cycles',str(cycles))
    if (cycles>GIVEUP_TIMEOUT):
        logs.log_info('finishing on default guard of %d'%GIVEUP_TIMEOUT)
        enc.onFinish()
        logs.closeLogs()
        veri.finish()
    rst_n = veri.peek('tb.rst_n')
    if (rst_n!='1'):
        return

    if (cycles==30):
        veri.listing('tb','100','deep.list')
    if (cycles>30):
        for Mon in Monitors: Mon.run()

def cucu():
    veri.force('tb.datain','0')
    veri.force('tb.key','0')
    veri.force('tb.vldin','0')
    encrypted = logs.peek('tb.encrypted')
    vldout = logs.peek('tb.vldout')
