

import os,sys,string,random
import veri
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs'%NewName)
import logs
Monitors=[]
cycles=0

import uartClass

uart = uartClass.uartClass('tb',Monitors)
uart.baudRate = 5

import axiSlave
axi = axiSlave.axiSlaveClass('tb',Monitors)


import controllerAluka

control = controllerAluka.controllerClass('tb.dut.debugcontroller',Monitors)

control.uart = uart

import sequenceClass

seq = sequenceClass.sequenceClass('tb',Monitors,'',[(uart,'uart'),(axi,'axi'),(control,'control')])

def sequence(SeqFname):
    Name = logs.bin2string(SeqFname)
    logs.log_info('sequence %s'%Name)
    seq.Sequence = open(Name).readlines()
    seq.workIncludes()




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
    if (cycles>100000):
        veri.finish()
    rst_n = veri.peek('tb.rst_n')
    if (rst_n!='1'):
        return

    if (cycles==30):
        veri.listing('tb','100','deep.list')
    if (cycles>30):
        for Mon in Monitors: Mon.run()
        Baud = logs.peek('tb.dut.uart_baudrate')
        uart.baudRate = Baud

def cucu():
    veri.force('tb.arready','0')
    veri.force('tb.awready','0')
    veri.force('tb.bid','0')
    veri.force('tb.bresp','0')
    veri.force('tb.bvalid','0')
    veri.force('tb.rdata','0')
    veri.force('tb.rid','0')
    veri.force('tb.rlast','0')
    veri.force('tb.rresp','0')
    veri.force('tb.rvalid','0')
    veri.force('tb.rxd','0')
    veri.force('tb.wready','0')
    araddr = logs.peek('tb.araddr')
    arburst = logs.peek('tb.arburst')
    arid = logs.peek('tb.arid')
    arlen = logs.peek('tb.arlen')
    arsize = logs.peek('tb.arsize')
    arvalid = logs.peek('tb.arvalid')
    awaddr = logs.peek('tb.awaddr')
    awburst = logs.peek('tb.awburst')
    awid = logs.peek('tb.awid')
    awlen = logs.peek('tb.awlen')
    awsize = logs.peek('tb.awsize')
    awvalid = logs.peek('tb.awvalid')
    bready = logs.peek('tb.bready')
    rready = logs.peek('tb.rready')
    txd = logs.peek('tb.txd')
    wdata = logs.peek('tb.wdata')
    wlast = logs.peek('tb.wlast')
    wstrb = logs.peek('tb.wstrb')
    wvalid = logs.peek('tb.wvalid')
