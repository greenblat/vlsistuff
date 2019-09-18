

import os,sys,string,random
import veri
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs'%NewName)
import logs
Monitors=[]
cycles=0


class driverMonitor:
    def __init__(self,Path,Monitors):
        Monitors.append(self)
        self.Path = Path

    def force(self,Sig,Val):
        veri.force('%s.%s'%(self.Path,Sig),str(Val))

    def peek(self,Sig):
        return logs.peek('%s.%s'%(self.Path,Sig))

    def valid(self,Sig):
        return self.peek(Sig)==1

    def run(self):
        if self.valid('validin')and self.valid('takenin'):
            return


# driverMonitor('tb',Monitors)



def negedge():
    global cycles
    cycles += 1
    veri.force('tb.cycles',str(cycles))
    if (cycles>1000):
        veri.finish()
    rst_n = veri.peek('tb.rst_n')
    if (rst_n!='1'):
        return

    if (cycles==30):
        veri.listing('tb','100','deep.list')
    if (cycles>30):
        for Mon in Monitors: Mon.run()

def cucu():
    veri.force('tb.ms_arready','0')
    veri.force('tb.ms_awready','0')
    veri.force('tb.ms_bid','0')
    veri.force('tb.ms_bresp','0')
    veri.force('tb.ms_bvalid','0')
    veri.force('tb.ms_rdata','0')
    veri.force('tb.ms_rid','0')
    veri.force('tb.ms_rlast','0')
    veri.force('tb.ms_rresp','0')
    veri.force('tb.ms_rvalid','0')
    veri.force('tb.ms_wready','0')
    veri.force('tb.paddr','0')
    veri.force('tb.penable','0')
    veri.force('tb.psel','0')
    veri.force('tb.pwdata','0')
    veri.force('tb.pwrite','0')
    veri.force('tb.sl_araddr','0')
    veri.force('tb.sl_arburst','0')
    veri.force('tb.sl_arcache','0')
    veri.force('tb.sl_arid','0')
    veri.force('tb.sl_arlen','0')
    veri.force('tb.sl_arprot','0')
    veri.force('tb.sl_arqos','0')
    veri.force('tb.sl_arsize','0')
    veri.force('tb.sl_arvalid','0')
    veri.force('tb.sl_awaddr','0')
    veri.force('tb.sl_awburst','0')
    veri.force('tb.sl_awcache','0')
    veri.force('tb.sl_awid','0')
    veri.force('tb.sl_awlen','0')
    veri.force('tb.sl_awprot','0')
    veri.force('tb.sl_awqos','0')
    veri.force('tb.sl_awsize','0')
    veri.force('tb.sl_awvalid','0')
    veri.force('tb.sl_bready','0')
    veri.force('tb.sl_rready','0')
    veri.force('tb.sl_wdata','0')
    veri.force('tb.sl_wlast','0')
    veri.force('tb.sl_wstrb','0')
    veri.force('tb.sl_wvalid','0')
    ms_araddr = logs.peek('tb.ms_araddr')
    ms_arburst = logs.peek('tb.ms_arburst')
    ms_arcache = logs.peek('tb.ms_arcache')
    ms_arid = logs.peek('tb.ms_arid')
    ms_arlen = logs.peek('tb.ms_arlen')
    ms_arprot = logs.peek('tb.ms_arprot')
    ms_arqos = logs.peek('tb.ms_arqos')
    ms_arsize = logs.peek('tb.ms_arsize')
    ms_arvalid = logs.peek('tb.ms_arvalid')
    ms_awaddr = logs.peek('tb.ms_awaddr')
    ms_awburst = logs.peek('tb.ms_awburst')
    ms_awcache = logs.peek('tb.ms_awcache')
    ms_awid = logs.peek('tb.ms_awid')
    ms_awlen = logs.peek('tb.ms_awlen')
    ms_awprot = logs.peek('tb.ms_awprot')
    ms_awqos = logs.peek('tb.ms_awqos')
    ms_awsize = logs.peek('tb.ms_awsize')
    ms_awvalid = logs.peek('tb.ms_awvalid')
    ms_bready = logs.peek('tb.ms_bready')
    ms_rready = logs.peek('tb.ms_rready')
    ms_wdata = logs.peek('tb.ms_wdata')
    ms_wlast = logs.peek('tb.ms_wlast')
    ms_wstrb = logs.peek('tb.ms_wstrb')
    ms_wvalid = logs.peek('tb.ms_wvalid')
    prdata = logs.peek('tb.prdata')
    pready = logs.peek('tb.pready')
    pslverr = logs.peek('tb.pslverr')
    sl_arready = logs.peek('tb.sl_arready')
    sl_awready = logs.peek('tb.sl_awready')
    sl_bid = logs.peek('tb.sl_bid')
    sl_bresp = logs.peek('tb.sl_bresp')
    sl_bvalid = logs.peek('tb.sl_bvalid')
    sl_rdata = logs.peek('tb.sl_rdata')
    sl_rid = logs.peek('tb.sl_rid')
    sl_rlast = logs.peek('tb.sl_rlast')
    sl_rresp = logs.peek('tb.sl_rresp')
    sl_rvalid = logs.peek('tb.sl_rvalid')
    sl_wready = logs.peek('tb.sl_wready')
