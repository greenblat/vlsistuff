
import os,sys,string

import logs
import veri

BASE = 'tb'
CLK = BASE + '.clk'

def peeklocal(Sig,Base=BASE):
    return logs.peek('%s.%s'%(Base,Sig))

Totals = {'aw':0,'ar':0,'dw':0,'dr':0}
veri.trace('aaa','5')
veri.trace('bbb','8')
veri.trace(CLK,'0')
def negedge():
    Time = veri.stime()
    awvalid = peeklocal('awvalid')
    awready = peeklocal('awready')
    if (awvalid==1)and(awready==1):
        veri.force('aaa',str(Time & 0x1f))
        veri.force('bbb',str(~Time & 0x1f))
        awaddr = peeklocal('awaddr')
        awsize = peeklocal('awsize')
        awlen = peeklocal('awlen')
        Totals['aw'] += (awlen+1)*(1<<awsize)
        logs.log_info('#%d aw addr=%x size=%s len=%s totaw=%d '%(Time,awaddr,awsize,awlen,Totals['aw']))


    if (peeklocal('wvalid')==1)and(peeklocal('wready')==1):
        wstrb = peeklocal('wstrb')
        wdata = peeklocal('wdata')
        wlast = peeklocal('wlast')
        wlast = peeklocal('wlast')
        bytes = logs.countOnes(wstrb)
        Totals['dw'] += bytes
        logs.log_info('#%d wd data=%x wstrb=%x  last=%d totdw=%d'%(Time,wdata,wstrb,wlast,Totals['dw']))
        


    arvalid = peeklocal('arvalid')
    arready = peeklocal('arready')
    if (arvalid==1)and(arready==1):
        araddr = peeklocal('araddr')
        arsize = peeklocal('arsize')
        arlen = peeklocal('arlen')
        arid = peeklocal('arid')
        Keep['arid']=arsize
        Totals['ar'] += (arlen+1)*(1<<awsize)
        logs.log_info('#%d ar addr=%x size=%s len=%s totar=%d'%(Time,araddr,arsize,arlen,Totals['ar']))

    if (peeklocal('rvalid')==1)and(peeklocal('rready')==1):
        rdata = peeklocal('rdata')
        rlast = peeklocal('rlast')
        rid = peeklocal('rid')
        Totals['rd'] += (1<<Keep[rid])
        logs.log_info('#%d rd data=%x rlast=%x totrd=%d'%(Time,rdata,rlast,Totals['rd']))

    monitorCommands(Time)



def monitorCommands(Time):
    if peeklocal('cmd_rd')==1:
        bytes = peeklocal('cmd_bytes')
        rmt_addr = peeklocal('cmd_rmt_addr')
        rmt_size = peeklocal('cmd_rmt_size')
        logs.log_info('command read bytes=%d from=0x%x  size=%d'%(bytes,rmt_addr,rmt_size))
    if peeklocal('cmd_wr')==1:
        bytes = peeklocal('cmd_bytes')
        rmt_addr = peeklocal('cmd_rmt_addr')
        rmt_size = peeklocal('cmd_rmt_size')
        logs.log_info('command write bytes=%d to=0x%x  size=%d'%(bytes,rmt_addr,rmt_size))

def monApb():
    if peeklocal('dma_psel')!=1: return
    if peeklocal('penable')!=1: return
    pwrite = peeklocal('pwrite')
    paddr   = peeklocal('paddr')
    if pwrite==1:
        pwdata = peeklocal('pwdata')
        logs.log_info('apb write addr=%04x data=%08x'%(paddr,pwdata))
    else:
        prdata = peeklocal('prdata')
        logs.log_info('apb read  addr=%04x data=%08x'%(paddr,prdata))


# this is how it is connected to the C engine..
veri.sensitive(CLK,'0',"negedge()")
