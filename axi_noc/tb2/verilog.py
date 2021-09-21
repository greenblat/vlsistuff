

import os,sys,string,random
import veri
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs3'%NewName)
import logs
Monitors=[]
cycles=0
GIVEUP_TIMEOUT = 10000    # how many cycles to run before retirment. 



import axiMaster
import axiSlave

ma = axiMaster.axiMasterClass('tb',Monitors,'mst0_','','MA')
mb = axiMaster.axiMasterClass('tb',Monitors,'mst1_','','MB')
mc = axiMaster.axiMasterClass('tb',Monitors,'mst2_','','MC')
md = axiMaster.axiMasterClass('tb',Monitors,'mst3_','','MD')
slvs = []
for II in range(16):
    slvs.append(axiSlave.axiSlaveClass('tb',Monitors,'slv%s_' % II,'','SLV%d' % II))

import sequenceClass




def sequence(TestName):
    Seq = logs.bin2string(TestName)
    seq.readfile(Seq)
    logs.setVar('sequence',Seq)
    Dir = os.path.dirname(Seq)
    logs.setVar('testsdir',Dir)
    logs.log_info('SEQUENCE %d'%len(seq.Sequence))


def pymonname(Name):
    logs.pymonname(Name)



def cannot_find_sig(Sig):
    logs.log_error('cannot find "%s" signal in the design'%Sig)




class driverMonitor(logs.driverClass):
    def __init__(self,Path,Monitors):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Code = 100
        self.Prefs = list(range(16))
        self.Pref = 0

    def run(self):
        return
    def action(self,_):
        self.round()
        if self.Prefs != []:
            Pref = self.Prefs.pop(0)
            self.Pref = Pref<<28
    def round(self):
        ma.makeWrite(1,1,self.Pref+0x00001000,3,self.Code)
        mb.makeWrite(1,1,self.Pref+0x00002000,3,self.Code+1)
        mc.makeWrite(1,1,self.Pref+0x00003000,3,self.Code+2)
        md.makeWrite(1,1,self.Pref+0x00004000,3,self.Code+3)

        ma.makeRead(1,1,self.Pref+0x00001000,3,self.Code)
        mb.makeRead(1,1,self.Pref+0x00002000,3,self.Code+1)
        mc.makeRead(1,1,self.Pref+0x00003000,3,self.Code+2)
        md.makeRead(1,1,self.Pref+0x00004000,3,self.Code+3)
        self.Code += 4

drv = driverMonitor('tb',Monitors)


seq = sequenceClass.sequenceClass('tb',Monitors,'',[('ma',ma),('mb',mb),('mc',mc),('md',md),('drv',drv)])
seq.msgCode = 100


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

