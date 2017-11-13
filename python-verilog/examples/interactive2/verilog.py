

import os,sys,string,random
sys.path.append('../vlibs')
import interactive
import veri
import uartx2
import logs

uartmodel = uartx2.uartx2Class('tb.uartmodel')


def intx(Text):
    if ('z' in Text)or('x' in Text):
        return -1
    return int(Text,2)

cycles=0
def negedge():
    global cycles
    cycles += 1
    veri.force('tb.cycles',str(cycles))
    rst_n = veri.peek('tb.rst_n')
    if (rst_n!='1'):
        return
    uartmodel.run()
    if txqueue!=[]:
        tx_empty = veri.peek('tb.tx_empty0')
        if tx_empty=='1':
            Chr = str(txqueue.pop(0))
            veri.force('tb.write_tx0','1')
            veri.force('tb.txdata0',Chr)
        else:
            veri.force('tb.write_tx0','0')
    else:
        veri.force('tb.write_tx0','0')

    rx_valid0 = veri.peek('tb.rx_valid0')
    if rx_valid0=='1':
        rxdata = veri.peek('tb.rxdata0')
        logs.log_info('rx: %s'%rxdata)


txqueue=[]
def uart_commands(wrds):
    print 'uart commands %s'%(str(wrds))    
    if wrds[0]=='tx':   
        aa = string.join(wrds[1:],' ')
        bb = list(aa)
        cc = map(ord,bb)
        txqueue.extend(cc)








interactive.external_commands = uart_commands



def cucu():
    veri.force('tb.ram_rdata','0')
    veri.force('tb.resetn','0')
    veri.force('tb.rxd','0')
    ram_addr = intx(veri.peek('tb.ram_addr'))
    ram_read = intx(veri.peek('tb.ram_read'))
    ram_wdata = intx(veri.peek('tb.ram_wdata'))
    ram_write = intx(veri.peek('tb.ram_write'))
    txd = intx(veri.peek('tb.txd'))
