

import os,sys,string,random
import veri
NewName = os.path.expanduser('~/vlsistuff')
sys.path.append('%s/verification_libs3'%NewName)
import logs
Monitors=[]
cycles=0
GIVEUP_TIMEOUT = 100000    # how many cycles to run before retirment. 


import apbSlave 
import jtagDriverClass

apb = apbSlave.apbSlave('tb',Monitors)
jtag = jtagDriverClass.jtagDriverClass('tb',Monitors)


import sequenceClass
seq = sequenceClass.sequenceClass('tb',Monitors,'',[('apb',apb),('jtag',jtag)])

def wrong_force_value(Sig,Value):
    logs.log_info('WRONG FORCE VALUE %s "%s"'%(Sig,Value))

def sequence(TestName):
    Seq = logs.bin2string(TestName)
    seq.readfile(Seq)
    logs.setVar('sequence',Seq)
    Dir = os.path.dirname(Seq)
    logs.setVar('testsdir',Dir)
    logs.log_info('SEQUENCE %d'%len(seq.Sequence))


def cannot_find_sig(Sig):
    logs.log_error('cannot find "%s" signal in the design'%Sig)





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
    veri.force('tb.jtck','0')
    veri.force('tb.jtdi','0')
    veri.force('tb.jtms','0')
    veri.force('tb.prdata','0')
    veri.force('tb.pready','0')
    jtdo = logs.peek('tb.jtdo')
    paddr = logs.peek('tb.paddr')
    penable = logs.peek('tb.penable')
    psel = logs.peek('tb.psel')
    pwdata = logs.peek('tb.pwdata')
    pwrite = logs.peek('tb.pwrite')



