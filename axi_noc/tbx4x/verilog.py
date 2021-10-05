

import os,sys,string,random
random.seed(0x101212)
import veri
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs3'%NewName)
sys.path.append('../pys')
import logs
Monitors=[]
cycles=0
GIVEUP_TIMEOUT = 300000    # how many cycles to run before retirment. 
logs.MAXERRORS = 2000

import axiProbe
Auxs = []
# probe = axiProbe.axiProbeClass('tb.dut',Auxs,'merger0_splitter0_','MtoS')
# probe0 = axiProbe.axiProbeClass('tb.dut',Auxs,'slv0_','SLV0')

import axiMaster
import axiSlave
import panics
import counts
import traffic

import performance
perf = performance.performanceClass('tb',Auxs,4)

slvs = []
msts = []
for II in range(4):
    slvs.append(axiSlave.axiSlaveClass('tb',Monitors,'slv%s_' % II,'','SLV%d' % II))
    msts.append(axiMaster.axiMasterClass('tb',Monitors,'mst%s_' % II,'','MST%d' % II))

import sequenceClass

import mergeAluka
mergeAluka.mergeAlukaClass('tb.dut.merger0',Auxs,'','AlikeM0')
mergeAluka.mergeAlukaClass('tb.dut.merger1',Auxs,'','AlikeM1')
mergeAluka.mergeAlukaClass('tb.dut.merger2',Auxs,'','AlikeM2')
mergeAluka.mergeAlukaClass('tb.dut.merger3',Auxs,'','AlikeM3')

import splitAluka
splitAluka.splitAlukaClass('tb.dut.splitter0',Auxs,'','AlikeS0')
splitAluka.splitAlukaClass('tb.dut.splitter1',Auxs,'','AlikeS1')
splitAluka.splitAlukaClass('tb.dut.splitter2',Auxs,'','AlikeS2')
splitAluka.splitAlukaClass('tb.dut.splitter3',Auxs,'','AlikeS3')

trf = traffic.trafficClass('tb.dut',Auxs,'','Traffic')

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
        self.WrEnable = False
        self.RdEnable = False
        self.Chance = 0
        self.Masters = list(range(16))
        self.Lens = list(range(1,32))
        self.Addresses = []
        self.Incr = 0
        self.Data0 = 0x100


    def run(self):
        self.run_wr()
        self.run_rd()

    def run_wr(self):
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
        
        Datas = []
        for X in range(Len):
            Datas.append(hex(self.Data0))
            self.Data0 += 1

        msts[Mst].makeWrite(1,Len,Addr,3,Datas)
        veri.force('tb.marker3',str(cycles))
        return

    def run_rd(self):
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
        if 'rd_enable' in Txt: 
            self.RdEnable = True
            return
        if 'rd_disable' in Txt: 
            self.RdEnable = False
            return
        if 'wr_disable' in Txt: 
            self.WrEnable = False
            return
        if 'snapshot' in Txt: 
            counts.snapshot()
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
            logs.log_info('ADDRESSES %s' % (list(map(hex,self.Addresses))))
        else:
            logs.log_error('ACTION inrecognized "%s" ' % Txt)
    def onFinish(self):
        counts.snapshot()

drv = driverMonitor('tb',Monitors)

def auxsOnfinish():
    trf.onFinish()
    perf.onFinish()

seq = sequenceClass.sequenceClass('tb',Monitors,'',[('drv',drv),('mst0',msts[0]),('mst1',msts[1]),('mst2',msts[2]),('mst3',msts[3])])
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
        initial()
        veri.listing('tb','100','deep.list')
    if (cycles>30):
        for Mon in Monitors: Mon.run()

def initial():
    for Mst in range(4):
        veri.force('tb.mst%d_arextras' % Mst,'0')
        veri.force('tb.mst%d_awextras' % Mst,'0')
def auxs():
    for Mon in Auxs:
        Mon.run()
    panics.monitorStuffs()

