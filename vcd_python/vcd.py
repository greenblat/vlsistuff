
import os,sys,string

MYSELF = os.path.expanduser('~')
sys.path.insert(0,'%s/verification_libs'%MYSELF)
import logs

cycles=0

def get_cycles():
    return cycles

logs.get_cycles = get_cycles

Values = {}
Base = 'tb'
def peek(Sig):
    Full = '%s.%s'%(Base,Sig)
    if Full not in Values: 
        logs.log_error('sig %s not in path %s'%(Sig,Base))
        return -1
    return logs.intx(Values[Full][0])

argv={}

def setVar(Var,Val):
    argv[Var]=Val


Panics = []
Clk0=0
def observer(Sig,Str,Time):
    global cycles,Clk0
    Values[Sig]=(Str,Time)
    if Time<argv['startTime']:
        return
    if '%s.clk'%Base not in Values: return
    Clk = peek('clk')
    if 'panic' in Sig: Panics.append(Sig)
    if (Clk==0)and(Clk0==1):
        negedge(Time)
        cycles += 1
    Clk0 = Clk

    if (argv['endTime']>0)and (Time>=argv['endTime']):
        logs.log_info('exiting on time=%d because of endTime=%d'%(Time,argv['endTime']))
        sys.exit()

Totals = {'aw':0,'ar':0,'dw':0,'dr':0}
def negedge(Time):
    for Panic in Panics:
        if (Panic in Values)and(Values[Panic]=='1'):
            logs.log_error('panic %s fired'%Panic)
    awvalid = peek('awvalid')
    awready = peek('awready')
    if (awvalid==1)and(awready==1):
        awaddr = peek('awaddr')
        awsize = peek('awsize')
        awlen = peek('awlen')
        Totals['aw'] += (awlen+1)*(1<<awsize)
        logs.log_info('#%d aw addr=%x size=%s len=%s totaw=%d '%(Time,awaddr,awsize,awlen,Totals['aw']))


    if (peek('wvalid')==1)and(peek('wready')==1):
        wstrb = peek('wstrb')
        wdata = peek('wdata')
        wlast = peek('wlast')
        wlast = peek('wlast')
        bytes = logs.countOnes(wstrb)
        Totals['dw'] += bytes
        logs.log_info('#%d wd data=%x wstrb=%x  last=%d totdw=%d'%(Time,wdata,wstrb,wlast,Totals['dw']))
        


    arvalid = peek('arvalid')
    arready = peek('arready')
    if (arvalid==1)and(arready==1):
        araddr = peek('araddr')
        arsize = peek('arsize')
        arlen = peek('arlen')
        arid = peek('arid')
        Keep['arid']=arsize
        Totals['ar'] += (arlen+1)*(1<<awsize)
        logs.log_info('#%d ar addr=%x size=%s len=%s totar=%d'%(Time,araddr,arsize,arlen,Totals['ar']))

    if (peek('rvalid')==1)and(peek('rready')==1):
        rdata = peek('rdata')
        rlast = peek('rlast')
        rid = peek('rid')
        Totals['rd'] += (1<<Keep[rid])
        logs.log_info('#%d rd data=%x rlast=%x totrd=%d'%(Time,rdata,rlast,Totals['rd']))

    monitorCommands(Time)



def monitorCommands(Time):
    if peek('cmd_rd')==1:
        bytes = peek('cmd_bytes')
        rmt_addr = peek('cmd_rmt_addr')
        rmt_size = peek('cmd_rmt_size')
        logs.log_info('command read bytes=%d from=0x%x  size=%d'%(bytes,rmt_addr,rmt_size))
    if peek('cmd_wr')==1:
        bytes = peek('cmd_bytes')
        rmt_addr = peek('cmd_rmt_addr')
        rmt_size = peek('cmd_rmt_size')
        logs.log_info('command write bytes=%d to=0x%x  size=%d'%(bytes,rmt_addr,rmt_size))

def monApb():
    if peek('dma_psel')!=1: return
    if peek('penable')!=1: return
    pwrite = peek('pwrite')
    paddr   = peek('paddr')
    if pwrite==1:
        pwdata = peek('pwdata')
        logs.log_info('apb write addr=%04x data=%08x'%(paddr,pwdata))
    else:
        prdata = peek('prdata')
        logs.log_info('apb read  addr=%04x data=%08x'%(paddr,prdata))





