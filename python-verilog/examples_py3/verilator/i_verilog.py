

import os,sys,string,random
import veri
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs3'%NewName)
import logs
Monitors=[]
cycles=0
GIVEUP_TIMEOUT = 200000    # how many cycles to run before retirment. 

import uartClass
uart =  uartClass.uartClass('tb',Monitors)

uart.baudRate = 100

uart.action('tx w30202aabb w0abcd0123  w112345678 w243210fde r0  r1  oadd123 r3 omul324  odiv425 r5  osin446 r6 ocos667 r7 ')

class driverMonitor(logs.driverClass):
    def __init__(self,Path,Monitors):
        logs.driverClass.__init__(self,Path,Monitors)
    def run(self):
        if self.waiting>0:
            self.waiting -= 1
        elif self.state=='idle':
            self.state='work0'
        elif self.state=='work0':
            self.state='work1'
        elif self.state=='work1':
            self.state='idle'


        if self.valid('validin')and self.valid('takenin'):
            return


# driverMonitor('tb',Monitors)

def initial(AAA):
    print('AAAA',AAA)


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

