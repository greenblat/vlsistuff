

import os,sys,string,random
random.seed(0x101212)
import veri
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs3'%NewName)
sys.path.append('../pys')
import logs
Monitors=[]
Auxs = []
cycles=0
GIVEUP_TIMEOUT = 100000    # how many cycles to run before retirment. 

import counts

import axiMaster
import axiSlave
import panics

import axiProbe
import mergeAluka 

import performance
perf = performance.performanceClass('tb',Auxs,16)
logs.log_info('SLAVES %s' % str(perf.SLAVES))

mergeAluka.mergeAlukaClass('tb.dut.merge3',Auxs,'','AlikeM3')

axiProbe.axiProbeClass('tb.dut',Auxs,'split100_merge208_','split100_merge208_')
axiProbe.axiProbeClass('tb.dut',Auxs,'split103_merge203_','split103_merge203_')
axiProbe.axiProbeClass('tb.dut',Auxs,'split0_merge3_','split0_merge3_')
axiProbe.axiProbeClass('tb.dut',Auxs,'merge3_split103_','merge3_split103')


slvs = []
msts = []
for II in range(16):
    slvs.append(axiSlave.axiSlaveClass('tb',Monitors,'slv%s_' % II,'','SLV%d' % II))
    msts.append(axiMaster.axiMasterClass('tb',Monitors,'mst%s_' % II,'','MST%d' % II))

import sequenceClass

## slvx = axiSlave.axiSlaveClass('tb.dut',Monitors,'split0_merge3_','','S0M3')
## slvx.Passive = True
## slvx.Fixed = {'awsize':3,'arsize':3}


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
        self.RdEnable = False
        self.WrEnable = False
        self.Chance = 0
        self.Masters = list(range(16))
        self.Lens = list(range(1,32))
        self.Addresses = []
        self.Incr = 0

    def run(self):
        self.wr_run()
        self.rd_run()

    def wr_run(self):
        if not self.WrEnable: return
        X = random.randint(0,100)
        if (X<self.Chance): return
        Mst = random.choice(self.Masters)
        Len = random.choice(self.Lens)
        if self.Addresses == []:
            Addr = random.randint(0x0,0xffffffff)
            Addr = Addr & 0xffffff00
        else:
            Addr = self.Incr + random.choice(self.Addresses)
            self.Incr += 0x100
        msts[Mst].makeWrite(1,Len,Addr,3)
        return

    def rd_run(self):
        if not self.RdEnable: return
        X = random.randint(0,100)
        if (X<self.Chance): return
        Mst = random.choice(self.Masters)
        Len = random.choice(self.Lens)
        if self.Addresses == []:
            Addr = random.randint(0x0,0xffffffff)
            Addr = Addr & 0xffffff00
        else:
            Addr = self.Incr + random.choice(self.Addresses)
            self.Incr += 0x100
        msts[Mst].makeRead(1,Len,Addr,3)
        return

    def action(self,Txt):
        if 'wr_enable' in Txt: 
            self.WrEnable = True
            return
        if 'wr_disable' in Txt: 
            self.WrEnable = False
            return
        if 'rd_enable' in Txt: 
            self.RdEnable = True
            return
        if 'rd_disable' in Txt: 
            self.RdEnable = False
            return
        wrds = Txt.split()
        if wrds[0] == []:
            pass
        elif wrds[0] == 'chance':
            self.Chance = eval(wrds[1])+1
        elif wrds[0] == 'masters':
            self.Masters = []
            for X in wrds[1:]:
                self.Masters.append(eval(X))
        elif wrds[0] == 'lens':
            self.Lens = []
            for X in wrds[1:]:
                self.Lens.append(eval(X))
        elif wrds[0] == 'address':
            self.Addresses = []
            for X in wrds[1:]:
                self.Addresses.append(eval(X))
        else:
            logs.log_error('ACTION inrecognized "%s" ' % Txt)

    def onFinish(self):
        return
        counts.snapshot()

drv = driverMonitor('tb',Monitors)


def auxsOnfinish():
    perf.onFinish()



seq = sequenceClass.sequenceClass('tb',Monitors,'',[('drv',drv),('mst0',msts[0]),('mst1',msts[1]),('mst2',msts[2]),('mst3',msts[3]),('mst4',msts[4]),('mst5',msts[5])])
seq.msgCode = 100
seq.onFinishes = auxsOnfinish


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

def auxs():
    if (cycles<30): return
    for Mon in Auxs: Mon.run()
    panics.monitorStuffs()
