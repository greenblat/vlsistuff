

import os,sys,string,random
random.seed(0x101212)

import veri
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs3'%NewName)
sys.path.append('../pys/')
import logs
Monitors=[]
Monitors0=[]
Monitors1=[]
Auxs = []
cycles=0
GIVEUP_TIMEOUT = 30000    # how many cycles to run before retirment. 
import driverClass
import axiSlave
import axiMaster
import axiMonitor
import sequenceClass

import splitAluka
splitAluka.splitAlukaClass('tb.dut.split0',Auxs,'','AlukeS0')
import axiProbe
probe0 = axiProbe.axiProbeClass('tb.dut',Auxs,'split0_clock0_','CLK0')
probe1 = axiProbe.axiProbeClass('tb.dut',Auxs,'split0_clock1_','CLK1')
probes0 = axiProbe.axiProbeClass('tb.dut',-1,'slv0_','SLVX0')
probes1 = axiProbe.axiProbeClass('tb.dut',-1,'slv1_','SLVX1')

mon1 = axiMonitor.axiMonitorClass('tb.',-1,3,{},'slv1_')
import panics

drv = driverClass.driverClass('tb',Monitors)


slvs = [0,0,0,0]
II = 0
slvs[0] =  slvs.append(axiSlave.axiSlaveClass('tb',Monitors0,'slv%s_' % II,'','SLV%d' % II))
II = 1
slvs[1] =  slvs.append(axiSlave.axiSlaveClass('tb',Monitors1,'slv%s_' % II,'','SLV%d' % II))
II = 2
slvs[2] =  slvs.append(axiSlave.axiSlaveClass('tb',Monitors,'slv%s_' % II,'','SLV%d' % II))
II = 3
slvs[2] =  slvs.append(axiSlave.axiSlaveClass('tb',Monitors,'slv%s_' % II,'','SLV%d' % II))

mst = axiMaster.axiMasterClass('tb',Monitors,'mst0_','','MST0')
drv.msts = [mst]


seq = sequenceClass.sequenceClass('tb',Monitors,'',[('drv',drv),('mst0',mst)])


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
    logs.log_error('cannot find "%s" signal in the design'%Sig,0,True,True)


def clock0_negedge():
    if (cycles>30): 
        for Mon in Monitors0: Mon.run()
def clock1_negedge():
    if (cycles>30): 
        for Mon in Monitors1: Mon.run()
def clock0_auxs():
    if (cycles>30): 
        probes0.run()
        panics.monitorStuffs()
def clock1_auxs():
    if (cycles>30): 
        probes1.run()
        panics.monitorStuffs()
        mon1.run()


def auxs():
    if (cycles>30): 
        for Mon in Auxs: Mon.run()
        panics.monitorStuffs()

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
    veri.force('tb.clock0','0')
    veri.force('tb.clock1','0')
    veri.force('tb.mst0_araddr','0')
    veri.force('tb.mst0_arburst','0')
    veri.force('tb.mst0_arextras','0')
    veri.force('tb.mst0_arid','0')
    veri.force('tb.mst0_arlen','0')
    veri.force('tb.mst0_arvalid','0')
    veri.force('tb.mst0_awaddr','0')
    veri.force('tb.mst0_awburst','0')
    veri.force('tb.mst0_awextras','0')
    veri.force('tb.mst0_awid','0')
    veri.force('tb.mst0_awlen','0')
    veri.force('tb.mst0_awvalid','0')
    veri.force('tb.mst0_bready','0')
    veri.force('tb.mst0_rready','0')
    veri.force('tb.mst0_wdata','0')
    veri.force('tb.mst0_wlast','0')
    veri.force('tb.mst0_wstrb','0')
    veri.force('tb.mst0_wvalid','0')
    veri.force('tb.slv0_arready','0')
    veri.force('tb.slv0_awready','0')
    veri.force('tb.slv0_bid','0')
    veri.force('tb.slv0_bresp','0')
    veri.force('tb.slv0_bvalid','0')
    veri.force('tb.slv0_rdata','0')
    veri.force('tb.slv0_rid','0')
    veri.force('tb.slv0_rlast','0')
    veri.force('tb.slv0_rresp','0')
    veri.force('tb.slv0_rvalid','0')
    veri.force('tb.slv0_wready','0')
    veri.force('tb.slv1_arready','0')
    veri.force('tb.slv1_awready','0')
    veri.force('tb.slv1_bid','0')
    veri.force('tb.slv1_bresp','0')
    veri.force('tb.slv1_bvalid','0')
    veri.force('tb.slv1_rdata','0')
    veri.force('tb.slv1_rid','0')
    veri.force('tb.slv1_rlast','0')
    veri.force('tb.slv1_rresp','0')
    veri.force('tb.slv1_rvalid','0')
    veri.force('tb.slv1_wready','0')
    veri.force('tb.slv2_arready','0')
    veri.force('tb.slv2_awready','0')
    veri.force('tb.slv2_bid','0')
    veri.force('tb.slv2_bresp','0')
    veri.force('tb.slv2_bvalid','0')
    veri.force('tb.slv2_rdata','0')
    veri.force('tb.slv2_rid','0')
    veri.force('tb.slv2_rlast','0')
    veri.force('tb.slv2_rresp','0')
    veri.force('tb.slv2_rvalid','0')
    veri.force('tb.slv2_wready','0')
    veri.force('tb.slv3_arready','0')
    veri.force('tb.slv3_awready','0')
    veri.force('tb.slv3_bid','0')
    veri.force('tb.slv3_bresp','0')
    veri.force('tb.slv3_bvalid','0')
    veri.force('tb.slv3_rdata','0')
    veri.force('tb.slv3_rid','0')
    veri.force('tb.slv3_rlast','0')
    veri.force('tb.slv3_rresp','0')
    veri.force('tb.slv3_rvalid','0')
    veri.force('tb.slv3_wready','0')
    mst0_arready = logs.peek('tb.mst0_arready')
    mst0_awready = logs.peek('tb.mst0_awready')
    mst0_bid = logs.peek('tb.mst0_bid')
    mst0_bresp = logs.peek('tb.mst0_bresp')
    mst0_bvalid = logs.peek('tb.mst0_bvalid')
    mst0_rdata = logs.peek('tb.mst0_rdata')
    mst0_rid = logs.peek('tb.mst0_rid')
    mst0_rlast = logs.peek('tb.mst0_rlast')
    mst0_rresp = logs.peek('tb.mst0_rresp')
    mst0_rvalid = logs.peek('tb.mst0_rvalid')
    mst0_wready = logs.peek('tb.mst0_wready')
    slv0_araddr = logs.peek('tb.slv0_araddr')
    slv0_arburst = logs.peek('tb.slv0_arburst')
    slv0_arextras = logs.peek('tb.slv0_arextras')
    slv0_arid = logs.peek('tb.slv0_arid')
    slv0_arlen = logs.peek('tb.slv0_arlen')
    slv0_arvalid = logs.peek('tb.slv0_arvalid')
    slv0_awaddr = logs.peek('tb.slv0_awaddr')
    slv0_awburst = logs.peek('tb.slv0_awburst')
    slv0_awextras = logs.peek('tb.slv0_awextras')
    slv0_awid = logs.peek('tb.slv0_awid')
    slv0_awlen = logs.peek('tb.slv0_awlen')
    slv0_awvalid = logs.peek('tb.slv0_awvalid')
    slv0_bready = logs.peek('tb.slv0_bready')
    slv0_rready = logs.peek('tb.slv0_rready')
    slv0_wdata = logs.peek('tb.slv0_wdata')
    slv0_wlast = logs.peek('tb.slv0_wlast')
    slv0_wstrb = logs.peek('tb.slv0_wstrb')
    slv0_wvalid = logs.peek('tb.slv0_wvalid')
    slv1_araddr = logs.peek('tb.slv1_araddr')
    slv1_arburst = logs.peek('tb.slv1_arburst')
    slv1_arextras = logs.peek('tb.slv1_arextras')
    slv1_arid = logs.peek('tb.slv1_arid')
    slv1_arlen = logs.peek('tb.slv1_arlen')
    slv1_arvalid = logs.peek('tb.slv1_arvalid')
    slv1_awaddr = logs.peek('tb.slv1_awaddr')
    slv1_awburst = logs.peek('tb.slv1_awburst')
    slv1_awextras = logs.peek('tb.slv1_awextras')
    slv1_awid = logs.peek('tb.slv1_awid')
    slv1_awlen = logs.peek('tb.slv1_awlen')
    slv1_awvalid = logs.peek('tb.slv1_awvalid')
    slv1_bready = logs.peek('tb.slv1_bready')
    slv1_rready = logs.peek('tb.slv1_rready')
    slv1_wdata = logs.peek('tb.slv1_wdata')
    slv1_wlast = logs.peek('tb.slv1_wlast')
    slv1_wstrb = logs.peek('tb.slv1_wstrb')
    slv1_wvalid = logs.peek('tb.slv1_wvalid')
    slv2_araddr = logs.peek('tb.slv2_araddr')
    slv2_arburst = logs.peek('tb.slv2_arburst')
    slv2_arextras = logs.peek('tb.slv2_arextras')
    slv2_arid = logs.peek('tb.slv2_arid')
    slv2_arlen = logs.peek('tb.slv2_arlen')
    slv2_arvalid = logs.peek('tb.slv2_arvalid')
    slv2_awaddr = logs.peek('tb.slv2_awaddr')
    slv2_awburst = logs.peek('tb.slv2_awburst')
    slv2_awextras = logs.peek('tb.slv2_awextras')
    slv2_awid = logs.peek('tb.slv2_awid')
    slv2_awlen = logs.peek('tb.slv2_awlen')
    slv2_awvalid = logs.peek('tb.slv2_awvalid')
    slv2_bready = logs.peek('tb.slv2_bready')
    slv2_rready = logs.peek('tb.slv2_rready')
    slv2_wdata = logs.peek('tb.slv2_wdata')
    slv2_wlast = logs.peek('tb.slv2_wlast')
    slv2_wstrb = logs.peek('tb.slv2_wstrb')
    slv2_wvalid = logs.peek('tb.slv2_wvalid')
    slv3_araddr = logs.peek('tb.slv3_araddr')
    slv3_arburst = logs.peek('tb.slv3_arburst')
    slv3_arextras = logs.peek('tb.slv3_arextras')
    slv3_arid = logs.peek('tb.slv3_arid')
    slv3_arlen = logs.peek('tb.slv3_arlen')
    slv3_arvalid = logs.peek('tb.slv3_arvalid')
    slv3_awaddr = logs.peek('tb.slv3_awaddr')
    slv3_awburst = logs.peek('tb.slv3_awburst')
    slv3_awextras = logs.peek('tb.slv3_awextras')
    slv3_awid = logs.peek('tb.slv3_awid')
    slv3_awlen = logs.peek('tb.slv3_awlen')
    slv3_awvalid = logs.peek('tb.slv3_awvalid')
    slv3_bready = logs.peek('tb.slv3_bready')
    slv3_rready = logs.peek('tb.slv3_rready')
    slv3_wdata = logs.peek('tb.slv3_wdata')
    slv3_wlast = logs.peek('tb.slv3_wlast')
    slv3_wstrb = logs.peek('tb.slv3_wstrb')
    slv3_wvalid = logs.peek('tb.slv3_wvalid')
