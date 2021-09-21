

import os,sys,string,random
import veri
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs3'%NewName)
import logs
Monitors=[]
cycles=0
GIVEUP_TIMEOUT = 1000    # how many cycles to run before retirment. 


import axiMaster
import axiSlave

ma = axiMaster.axiMasterClass('tb',Monitors,'a_','','MA')
mb = axiMaster.axiMasterClass('tb',Monitors,'b_','','MB')
mc = axiMaster.axiMasterClass('tb',Monitors,'c_','','MC')
md = axiMaster.axiMasterClass('tb',Monitors,'d_','','MD')

slv = axiSlave.axiSlaveClass('tb',Monitors)

import sequenceClass
seq = sequenceClass.sequenceClass('tb',Monitors,'',[('ma',ma),('mb',mb),('mc',mc),('md',md),('slv',slv)])

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

