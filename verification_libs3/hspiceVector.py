

import sys
import veri
import logs


class hspiceVector(logs.driverClass):
    def __init__(self,Path,Monitors,IOlist = ''):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Path = Path
        self.IOlist=IOlist.split()
        self.Fout = False
        self.Sigs = []
        self.Step = 1
        self.Time = 0
        self.fileName = 'hspice.vec'
        self.Enable = False
        self.lastLine = ''

    def action(self,Text):
        wrds = Text.split()
        if wrds[0] == 'step':
            self.Step = eval(wrds[1])
        elif wrds[0] == 'filename':
            self.fileName = wrds[1]
            logs.log_info('hspice filename %s'%self.fileName)
        elif wrds[0] == 'sigs':
            self.IOlist.extend(wrds[1:])
        elif wrds[0] == 'enable':
            self.Enable = True
            logs.log_info('hspice enabled')
        else:
            logs.log_error('wrong action %s" accept are enable,filename, step, sigs'%(wrds[0]))

    def busy(self):
        return False

    def onFinish(self):
        if self.Fout:
            self.Fout.close()

    def run(self):
        if not self.Enable: return
        if self.IOlist == []: return
        if not self.Fout:
            self.opening()
        if self.Sigs == []:
            logs.log_error('no signals?')
            sys.exit()
        newLine = ''
        for Wid,Sig in self.Sigs:
            Val = self.peek(Sig)
            if Val<0: Val = 0
            newLine += ' %0%dx'%(Wid,Val)
        if newLine != self.lastLine:
            self.Fout.write('%8d %s\n'%(self.Time,newLine))
            self.lastLine = newLine
        self.Time += self.Step
            

    def opening(self):
        self.Fout = open(self.fileName,'w')
        self.Fout.write('; dump of hspice from %s\n' % self.Path)
        Radix = ''
        Vname = ''
        IO = ''
        print('OPENING',self.IOlist)
        self.Sigs = []
        for Pin in self.IOlist:
            WW = Pin.split(':')
            if (len(WW) != 2)or(WW[0] not in 'iob'):
                logs.log_error('name must include direction io, like i:CLK (%s)' % (Pin))
            IO += ' '+WW[0]
            Sig = WW[1]
            Val = veri.peek('%s%s'%(self.Path,Sig))
            Wid = len(Val)
            if Wid == 1:
                Vname += ' '+Sig
                Radix += ' 1'
                self.Sigs.append((1,Sig))
            elif Wid < 5:
                Vname += ' '+Sig
                Radix += ' %s' % Wid
                self.Sigs.append((1,Sig))
            else:
                Vname += ' %s[[%s:0]]'%(Sig,Wid-1)
                X = int(Wid/4)
                AA = '4' * X
                Y = Wid % 4
                if (Y>0):
                    AA = str(Y)+AA
                Radix += ' '+ AA
                self.Sigs.append((len(AA),Sig))

        self.Fout.write('radix %s\n'%Radix)                
        self.Fout.write('vname %s\n'%Vname)                
        self.Fout.write('io    %s\n'%IO)                
        self.Fout.write('tunit  ns\n')                
        self.Fout.write('; Tabular  data\n')                
                 


