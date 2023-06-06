
import string
import logs
import veri


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
        if self.Lines != []:
            print("ADADA",self.state,self.progCounter,self.Lines[self.progCounter])
        if self.state == 'idle' : return
        if self.waiting>0:
            self.waiting -= 1
            return
        if self.state == 'wait':
            self.state = 'idle'
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

    def execute(self):
        Line = self.Lines[self.progCounter]
        wrds = Line.split()
        if wrds == []:
            self.progCounter += 1
            return
        if wrds[0] == 'wait':
            self.waiting = self.lcleval(wrds[1])
            self.state = 'wait'
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
        if wrds[0] == 'if':
            Eval = self.lcleval(wrds[1])
            if Eval:
                self.jumpTo(wrds[2])
            else:
                self.progCounter += 1

        if wrds[1] == '=':
            Val = self.lcleval(' '.join(wrds[2:]))
            self.Vars[wrds[0]] = Val
            self.progCounter += 1
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
            self.progCounter = 0
            return
        if wrds[0] == 'idle':
            self.state = 'idle'
            self.progCounter = 0
            return
            
    def jumpTo(self,Label):
        if Label not in self.Labels:
            for ind,Line in enumerate(self.Lines):
                wrds = Lines.split()
                if wrds[0] == 'label':
                    self.Labels[wrds[1]] = ind
        if Label in self.Labels:
            self.progCounter = self.Labels[Label]
            return
        else:
            logs.log_error('jumpTo %s failed' % Label)
            sys.exit()

    def busy(self):
        return self.state != 'idle' 
    def onFinish(self):
        return

    def action(self,Txt):
        wrds = Txt.split()
        if wrds == []: return
        if wrds[0] == 'program':
            self.readProgram(wrds[1])
            logs.log_info('Program loaded %s %d lines' % (wrds[1],len(self.Lines)))
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
    
