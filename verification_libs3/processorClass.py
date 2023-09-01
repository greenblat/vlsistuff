# mockup of software. simple "assembly" opcodes play like a software.

Verbose = False
Verbose = True

import logs
import veri
import sys


class processorClass(logs.driverClass):
    def __init__(self,Path,Monitors,Apbs,Apbm,Dut):
        logs.driverClass.__init__(self,Path,Monitors)
        Monitors.append(self)
        self.Apbs = Apbs
        self.Apbm = Apbm
        self.Dut = Dut
        self.state = 'idle'
        self.progCounter = 0
        self.Lines = []
        self.stack = []
        self.Vars = {}
        self.Labels = {}
        self.saveTo = False

    def lcleval(self,Txt):
        Trs = self.SeqObj.Translates
        X = eval(Txt,Trs,self.Vars)
        return X

    def run(self):
        if (self.Lines != [])and Verbose:
            logs.log_info("%s ADADA %s %s line=|%s| wait=%s" % (self.Dut,self.state,self.progCounter,self.Lines[self.progCounter][:-1],self.waiting))
        xst = self.state+'   '
        xval = str(ord(xst[3]) + (ord(xst[2])<<8)+ (ord(xst[1])<<16)+(ord(xst[    0])<<24))
        veri.force('tb.xst'+self.Apbs,xval)
        veri.force('tb.lin'+self.Apbs,str(self.progCounter))
        if self.state == 'idle' : return
        if self.waiting>0:
            self.waiting -= 1
            return
        if self.state == 'wait':
            self.state = 'run'
            return
        if self.state == 'wait_for_interrupt':
            if self.peek('%s.int_to_arm' % self.Dut) == 1:
                self.state = 'run'
                self.progCounter = 0
        elif self.state == 'run':
            while self.state == 'run':
                self.execute()
        elif self.state == 'apb':
            Aobj = self.SeqObj.agents[self.Apbs]
            if self.SeqObj.agents[self.Apbs].busy(): return
            if self.saveTo:
                Val = Aobj.prdata()
                self.Vars[self.saveTo] = Val
            self.state = 'run'
            return
        elif self.state == 'ram':
            Aobj = self.SeqObj.agents[self.Apbm]
            if self.SeqObj.agents[self.Apbm].busy(): return
            self.state = 'run'
            return

    def execute(self):
        Line = self.Lines[self.progCounter]
        wrds = Line.split()
        if wrds == []:
            self.progCounter += 1
            return
        if wrds[0] == 'print':
            Res = ''
            for X in wrds[1:]:
                if X in self.Vars:
                    Res += ' '+X+'='+hex(self.Vars[X])
                else:
                    Res += ' '+X
            logs.log_info("@%s: PR: %s" % (self.Dut,Res))
            self.progCounter += 1
            return
        if wrds[0] == 'wait':
            self.waiting = self.lcleval(wrds[1])
            self.state = 'wait'
            self.progCounter += 1
            return
        if wrds[0] == 'return':
            self.progCounter = self.stack.pop(-1)
            return
        if wrds[0] == 'call':
            self.stack.append(self.progCounter+1)
            self.jumpTo(wrds[1])
            return
        if wrds[0] == 'goto':
            self.jumpTo(wrds[1])
            return
        if wrds[0] == 'peek':
            X = self.peek(wrds[1])
            self.Vars[wrds[1]] = X
        if wrds[0] == 'if':
            Eval = self.lcleval(wrds[1])
            if Eval:
                if wrds[2] == 'goto': 
                    self.jumpTo(wrds[3])
                    return
                elif wrds[2] == 'call':
                    self.stack.append(self.progCounter+1)
                    self.jumpTo(wrds[3])
                    return
                else:
                    logs.log_error("@s: if wrds[2]=%s wrds |%a|s" % (self.Dut,wrds[2],' '.join(wrds)))
                    self.progCounter += 1
                    sys.exit()
                    return
            else:
                self.progCounter += 1
                return


        if (len(wrds)>2) and (wrds[1] == '='):
            Val = self.lcleval(' '.join(wrds[2:]))
            self.Vars[wrds[0]] = Val
            self.progCounter += 1
            return

        if wrds[0] == 'ram':
            self.state = 'ram'
            self.progCounter += 1
            Addr = self.lcleval(wrds[1])
            Data = self.lcleval(wrds[2])
            self.SeqObj.agents[self.Apbm].action('ram %s %s' % (hex(Addr),hex(Data)))
            return

        if wrds[0] == 'apb':
            self.state = 'apb'
            self.progCounter += 1
            if wrds[1] == 'write':
                Addr = self.lcleval(wrds[2])
                Data = self.lcleval(wrds[3])
                self.SeqObj.agents[self.Apbs].action('write %s %s' % (hex(Addr),hex(Data)))
                self.saveTo = False
                return

            if wrds[1] == 'read':
                Addr = self.lcleval(wrds[2])
                self.SeqObj.agents[self.Apbs].action('read %s' % (hex(Addr)))
                self.saveTo = wrds[3]
                return

        if wrds[0] == 'label':
            self.progCounter  += 1
            return

        if wrds[0] == 'stop':
            self.state = 'wait_for_interrupt'
            self.buildLabels(wrds[1])
            self.progCounter = self.Labels[wrds[1]]
            return
        if wrds[0] == 'idle':
            self.state = 'idle'
            self.progCounter = 0
            return
            
    def jumpTo(self,Label):
        if Label not in self.Labels:
            for ind,Line in enumerate(self.Lines):
                wrds = Line.split()
                if (wrds!=[]) and (wrds[0] == 'label'):
                    self.Labels[wrds[1]] = ind
        if Label in self.Labels:
            self.progCounter = self.Labels[Label]
            return
        else:
            logs.log_error('jumpTo %s failed' % Label)
            sys.exit()

    def buildLabels(self,Label):
        if Label not in self.Labels:
            for ind,Line in enumerate(self.Lines):
                wrds = Line.split()
                if (wrds!=[]) and (wrds[0] == 'label'):
                    self.Labels[wrds[1]] = ind


    def busy(self):
        return (self.state not in ['idle','wait_for_interrupt']) 
    def onFinish(self):
        return

    def action(self,Txt,Orig=[]):
        wrds = Txt.split()
        if wrds == []: return
        if wrds[0] == 'program':
            self.readProgram(wrds[1])
            logs.log_info('Program loaded %s %d lines' % (wrds[1],len(self.Lines)))
            return
        if wrds[0] == 'idle':
            self.state = 'idle'
            return
        if wrds[0] == 'run':
            if self.Lines == []:
                logs.log_error('load program before running')
                return
            if wrds[1] == 'stop':
                self.state = 'idle'
            else:
                self.state = 'run'
                self.programCounter = 0
        else:
            logs.log_error('processorClass got %s' % Txt)

    def readProgram(self,Fname):
        File = open(Fname)
        Lines = File.readlines()
        File.close()
        self.Lines = Lines
        self.state = 'idle'
        self.progCounter = 0
    
