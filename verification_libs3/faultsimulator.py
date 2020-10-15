


import logs
import veri
import random
import os,sys


import time
StartTime = time.time()



Fname =  os.getenv('STUCK_FILE')
if Fname=='': 
    Fname = 'STUCKS.shuffled'


if (not Fname) or not os.path.exists(Fname):
    logs.log_error('STUCK base file "%s" doesnt exist, setenv STUCK_FILE should work'%Fname)
    sys.exit()
File = open(Fname)
Lines = File.readlines()
File.close()


TESTDURATION = 500

class faultsimulatorClass(logs.driverClass):
    def __init__(self,Path,Monitors):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Lines = Lines[:]
        self.faulted = 0 
        self.peekOneFault()
        self.gracePeriod = 100
        self.Discovered = 0 
        self.notDiscovered = 0 
        self.testDuration = TESTDURATION

    def peekOneFault(self):
        EndTime = time.time()
        Elapsed = int(EndTime-StartTime)

        Ok = False
        if self.Lines==[]: 
            logs.log_info('exosted %s stucks file'%Fname)
            veri.finish()

        while not Ok:
            Pop = random.randint(0,len(self.Lines))
            self.Line = self.Lines.pop(Pop)
            wrds = self.Line.split()
            if wrds[0]=='register':
                self.Fpath = wrds[1] 
                self.Wid  = int(wrds[2])
                self.Pos  = int(wrds[3])
                veri.force(self.Fpath,hex(1<<self.Pos))
                self.faulted += 1
                logs.log_info('@%d seconds FAULTING DISC %d %s'%(Elapsed,self.faulted,self.Line))
                self.Kind = 'register'
                Ok = True
            elif wrds[0]=='glvfault':
                self.Fpath = wrds[1] 
                self.Kind = 'glvfault'
                veri.force(self.Fpath,'1')
                self.faulted += 1
                logs.log_info('@%d seconds FAULTING DISC %d %s'%(Elapsed,self.faulted,self.Line))
                Ok = True

    def discoveredx(self,How='def'):
        self.Discovered += 1
        logs.log_info('YESDISCOVERED at=%d (%d,yes%d,no%d) %s %s'%(TESTDURATION-self.testDuration,self.faulted,self.Discovered,self.notDiscovered,How,self.Line))
        if self.Kind == 'glvfault':
            veri.force(self.Fpath,'0')
        else:
            veri.force(self.Fpath,hex(0<<self.Pos))
        self.peekOneFault()
        self.rerunTest()
        self.gracePeriod = 100
        veri.force('tb.discovered',str(self.Discovered))
        self.testDuration = TESTDURATION


    def run(self):
        if self.gracePeriod>0:
            self.gracePeriod -= 1
            return
        if self.discovered():
            self.discoveredx()
                
        self.testDuration  -= 1
        if (self.testDuration==0):
            self.testDuration = TESTDURATION
            self.finish()

            
    def finish(self,How='fin'):
        if self.Kind == 'glvfault':
            veri.force(self.Fpath,'0')
        else:
            veri.force(self.Fpath,hex(0<<self.Pos))
        self.peekOneFault()
        self.rerunTest()
        self.gracePeriod = 50
        self.notDiscovered += 1
        veri.force('tb.notdiscovered',str(self.notDiscovered))
        logs.log_info('NOTDISCOVERED (%d,yes%d,no%d) %s %s'%(self.faulted,self.Discovered,self.notDiscovered,How,self.Line))
        





