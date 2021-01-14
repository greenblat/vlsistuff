

import os,sys,string,random
import veri
import math
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs3'%NewName)
import logs
Monitors=[]
cycles=0
GIVEUP_TIMEOUT = 1000    # how many cycles to run before retirment. 

import axiMaster
import sequenceClass

axi = axiMaster.axiMasterClass('tb',-1)
seq = sequenceClass.sequenceClass('tb',Monitors,'',[('axi',axi)],{})



Expecteds = [0]

def axi_clk():
    axi.run()
    if veri.peek('tb.wvalid')=='1':
        wdata = logs.peek('tb.wdata')
        Expecteds[-1] += int(math.sqrt(wdata))
        wlast = logs.peek('tb.wlast')
        if wlast==1:
            Expecteds.append(0)

def pclk():
    if veri.peek('tb.pready')=='0': 
        veri.force('tb.psel','0')
        veri.force('tb.penable','0')
        return
    prdata = logs.peek('tb.prdata')
    veri.force('tb.psel','1')
    veri.force('tb.penable','1')
    Exp = Expecteds.pop(0)
    logs.log_info('RESULT %d  exp %d'%(prdata,Exp))


def sys_clk():
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


def sequence(TestName):
    Seq = logs.bin2string(TestName)
    seq.readfile(Seq)
    logs.setVar('sequence',Seq)
    Dir = os.path.dirname(Seq)
    logs.setVar('testsdir',Dir)
    logs.log_info('SEQUENCE %d'%len(seq.Sequence))




