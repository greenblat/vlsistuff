

import os,sys,string,random
import veri
NewName = os.path.expanduser('~')
sys.path.append('%s/vlsistuff/verification_libs3'%NewName)
sys.path.append('../../../verification_libs3')
import logs
import apbDriver
Monitors=[]
cycles=0
GIVEUP_TIMEOUT = 10000    # how many cycles to run before retirment. 



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



# mockup of your uvm
class uvmDriver(logs.driverClass):
    def __init__(self,Path,Monitors):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Enable = False

    def run(self):
        if not self.Enable:
            self.force('vldin',0)
            self.force('sample',0)
            return 

        Vld = random.randint(0,100)
        if Vld<33:
            Sample = random.randint(0,255)
            self.force('sample',Sample)
            self.force('vldin',1)
        else:
            self.force('vldin',0)
            self.force('sample',0)
    def  action(self,Txt):
        if 'enable' in Txt: self.Enable = True
        if 'disable' in Txt: self.Enable = False
        return

    def  onFinish(self):
        return
    def  busy(self):
        return False


uvm  = uvmDriver('tb',Monitors)
apb  = apbDriver.apbDriver('tb',Monitors,'','','APB')

import firModel
model = firModel.firModel('tb.dut.fir',[])

import sequenceClass
seq = sequenceClass.sequenceClass('tb',Monitors,'',[('uvm',uvm),('apb',apb),('model',model)])


def run_model():
    if (cycles>30):
        model.run()

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

