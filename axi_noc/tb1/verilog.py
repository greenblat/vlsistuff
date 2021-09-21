

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

mst = axiMaster.axiMasterClass('tb',Monitors,'','','MST')
sa = axiSlave.axiSlaveClass('tb',Monitors,'a_','','SLVA')
sb = axiSlave.axiSlaveClass('tb',Monitors,'b_','','SLVB')
sc = axiSlave.axiSlaveClass('tb',Monitors,'c_','','SLVC')
sd = axiSlave.axiSlaveClass('tb',Monitors,'d_','','SLVD')



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
    veri.force('tb.a_arready','0')
    veri.force('tb.a_awready','0')
    veri.force('tb.a_bid','0')
    veri.force('tb.a_bresp','0')
    veri.force('tb.a_bvalid','0')
    veri.force('tb.a_rdata','0')
    veri.force('tb.a_rid','0')
    veri.force('tb.a_rlast','0')
    veri.force('tb.a_rresp','0')
    veri.force('tb.a_rvalid','0')
    veri.force('tb.a_wready','0')
    veri.force('tb.araddr','0')
    veri.force('tb.arburst','0')
    veri.force('tb.arextras','0')
    veri.force('tb.arid','0')
    veri.force('tb.arlen','0')
    veri.force('tb.arvalid','0')
    veri.force('tb.awaddr','0')
    veri.force('tb.awburst','0')
    veri.force('tb.awextras','0')
    veri.force('tb.awid','0')
    veri.force('tb.awlen','0')
    veri.force('tb.awvalid','0')
    veri.force('tb.b_arready','0')
    veri.force('tb.b_awready','0')
    veri.force('tb.b_bid','0')
    veri.force('tb.b_bresp','0')
    veri.force('tb.b_bvalid','0')
    veri.force('tb.b_rdata','0')
    veri.force('tb.b_rid','0')
    veri.force('tb.b_rlast','0')
    veri.force('tb.b_rresp','0')
    veri.force('tb.b_rvalid','0')
    veri.force('tb.b_wready','0')
    veri.force('tb.bready','0')
    veri.force('tb.c_arready','0')
    veri.force('tb.c_awready','0')
    veri.force('tb.c_bid','0')
    veri.force('tb.c_bresp','0')
    veri.force('tb.c_bvalid','0')
    veri.force('tb.c_rdata','0')
    veri.force('tb.c_rid','0')
    veri.force('tb.c_rlast','0')
    veri.force('tb.c_rresp','0')
    veri.force('tb.c_rvalid','0')
    veri.force('tb.c_wready','0')
    veri.force('tb.d_arready','0')
    veri.force('tb.d_awready','0')
    veri.force('tb.d_bid','0')
    veri.force('tb.d_bresp','0')
    veri.force('tb.d_bvalid','0')
    veri.force('tb.d_rdata','0')
    veri.force('tb.d_rid','0')
    veri.force('tb.d_rlast','0')
    veri.force('tb.d_rresp','0')
    veri.force('tb.d_rvalid','0')
    veri.force('tb.d_wready','0')
    veri.force('tb.rready','0')
    veri.force('tb.wdata','0')
    veri.force('tb.wlast','0')
    veri.force('tb.wstrb','0')
    veri.force('tb.wvalid','0')
    a_araddr = logs.peek('tb.a_araddr')
    a_arburst = logs.peek('tb.a_arburst')
    a_arextras = logs.peek('tb.a_arextras')
    a_arid = logs.peek('tb.a_arid')
    a_arlen = logs.peek('tb.a_arlen')
    a_arvalid = logs.peek('tb.a_arvalid')
    a_awaddr = logs.peek('tb.a_awaddr')
    a_awburst = logs.peek('tb.a_awburst')
    a_awextras = logs.peek('tb.a_awextras')
    a_awid = logs.peek('tb.a_awid')
    a_awlen = logs.peek('tb.a_awlen')
    a_awvalid = logs.peek('tb.a_awvalid')
    a_bready = logs.peek('tb.a_bready')
    a_rready = logs.peek('tb.a_rready')
    a_wdata = logs.peek('tb.a_wdata')
    a_wlast = logs.peek('tb.a_wlast')
    a_wstrb = logs.peek('tb.a_wstrb')
    a_wvalid = logs.peek('tb.a_wvalid')
    arready = logs.peek('tb.arready')
    awready = logs.peek('tb.awready')
    b_araddr = logs.peek('tb.b_araddr')
    b_arburst = logs.peek('tb.b_arburst')
    b_arextras = logs.peek('tb.b_arextras')
    b_arid = logs.peek('tb.b_arid')
    b_arlen = logs.peek('tb.b_arlen')
    b_arvalid = logs.peek('tb.b_arvalid')
    b_awaddr = logs.peek('tb.b_awaddr')
    b_awburst = logs.peek('tb.b_awburst')
    b_awextras = logs.peek('tb.b_awextras')
    b_awid = logs.peek('tb.b_awid')
    b_awlen = logs.peek('tb.b_awlen')
    b_awvalid = logs.peek('tb.b_awvalid')
    b_bready = logs.peek('tb.b_bready')
    b_rready = logs.peek('tb.b_rready')
    b_wdata = logs.peek('tb.b_wdata')
    b_wlast = logs.peek('tb.b_wlast')
    b_wstrb = logs.peek('tb.b_wstrb')
    b_wvalid = logs.peek('tb.b_wvalid')
    bid = logs.peek('tb.bid')
    bresp = logs.peek('tb.bresp')
    bvalid = logs.peek('tb.bvalid')
    c_araddr = logs.peek('tb.c_araddr')
    c_arburst = logs.peek('tb.c_arburst')
    c_arextras = logs.peek('tb.c_arextras')
    c_arid = logs.peek('tb.c_arid')
    c_arlen = logs.peek('tb.c_arlen')
    c_arvalid = logs.peek('tb.c_arvalid')
    c_awaddr = logs.peek('tb.c_awaddr')
    c_awburst = logs.peek('tb.c_awburst')
    c_awextras = logs.peek('tb.c_awextras')
    c_awid = logs.peek('tb.c_awid')
    c_awlen = logs.peek('tb.c_awlen')
    c_awvalid = logs.peek('tb.c_awvalid')
    c_bready = logs.peek('tb.c_bready')
    c_rready = logs.peek('tb.c_rready')
    c_wdata = logs.peek('tb.c_wdata')
    c_wlast = logs.peek('tb.c_wlast')
    c_wstrb = logs.peek('tb.c_wstrb')
    c_wvalid = logs.peek('tb.c_wvalid')
    d_araddr = logs.peek('tb.d_araddr')
    d_arburst = logs.peek('tb.d_arburst')
    d_arextras = logs.peek('tb.d_arextras')
    d_arid = logs.peek('tb.d_arid')
    d_arlen = logs.peek('tb.d_arlen')
    d_arvalid = logs.peek('tb.d_arvalid')
    d_awaddr = logs.peek('tb.d_awaddr')
    d_awburst = logs.peek('tb.d_awburst')
    d_awextras = logs.peek('tb.d_awextras')
    d_awid = logs.peek('tb.d_awid')
    d_awlen = logs.peek('tb.d_awlen')
    d_awvalid = logs.peek('tb.d_awvalid')
    d_bready = logs.peek('tb.d_bready')
    d_rready = logs.peek('tb.d_rready')
    d_wdata = logs.peek('tb.d_wdata')
    d_wlast = logs.peek('tb.d_wlast')
    d_wstrb = logs.peek('tb.d_wstrb')
    d_wvalid = logs.peek('tb.d_wvalid')
    rdata = logs.peek('tb.rdata')
    rid = logs.peek('tb.rid')
    rlast = logs.peek('tb.rlast')
    rresp = logs.peek('tb.rresp')
    rvalid = logs.peek('tb.rvalid')
    wready = logs.peek('tb.wready')
