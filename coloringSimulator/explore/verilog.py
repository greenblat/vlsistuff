

import os,sys,string,random
import veri

sys.path = ['',
    '/Library/Frameworks/Python.framework/Versions/3.9/lib/python39.zip',
    '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9',
    '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload',
    '/Users/ilia/Library/Python/3.9/lib/python/site-packages',
    '/Users/ilia/Library/Python/3.9/lib/python/site-packages/pyglet-2.0.dev0-py3.9.egg',
    '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages'
]




NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs3'%NewName)
import logs
Monitors=[]
cycles=0
GIVEUP_TIMEOUT = 1000    # how many cycles to run before retirment. 

import sequenceClass
seq = sequenceClass.sequenceClass('tb',Monitors,'',[])

import colorlib

def sequence(TestName):
    Seq = logs.bin2string(TestName)
    seq.readfile(Seq)
    logs.setVar('sequence',Seq)
    Dir = os.path.dirname(Seq)
    logs.setVar('testsdir',Dir)
    logs.log_info('SEQUENCE %d'%len(seq.Sequence))




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

def flopinit(AA):
    colorlib.flopinit(AA)
def floprun(AA,Pin,Val):
    colorlib.floprun(logs.intx(AA),logs.intx(Pin),logs.intx(Val))

def colorinit(AA):
    colorlib.colorinit(AA)
def colorrun(AA,Val):
    colorlib.colorrun(logs.intx(AA),logs.intx(Val))

def blobinit(AA):
    colorlib.blobinit(AA)
def blobrun(AA,Pin,Val):
    colorlib.blobrun(logs.intx(AA),logs.intx(Pin),logs.intx(Val))




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
    veri.force('tb.aaa','0')
    veri.force('tb.bbb','0')
    veri.force('tb.ccc','0')
    veri.force('tb.clk0','0')
    veri.force('tb.clk1','0')
    veri.force('tb.eee','0')
    qbad = logs.peek('tb.qbad')
    qgood = logs.peek('tb.qgood')
