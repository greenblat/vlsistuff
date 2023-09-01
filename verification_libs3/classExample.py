
import string
import logs
import veri


class vdriverClass(logs.driverClass):
    def __init__(self,Path,Monitors):
        logs.driverClass.__init__(self,Path,Monitors)
        if Monitors: Monitors.append(self)
        self.Queue = []
        self.Width = {}

    def run(self):
        if self.Queue == []: return
        if self.waiting>0:
            self.waiting -= 1
            return
        Cmd = self.Queue.pop(0) 
        if Cmd[0] == 'force':
            Sig = Cmd[1]
            if Sig in self.Width:
                Wid = self.Width[Sig]
            else:
                Wid = 1
            Vdd = self.vdd
            Val = bin(Cmd[2])[2:]
            Res = 0
            for Chr in Val:
                Res = Res<<16
                if Chr == '1':
                    Res += self.vdd
            self.force(Sig,hex(Res))

    def busy(self):
        return self.Queue != []

    def onFinish(self):
        return

    def action(self,Txt,Orig=[]):
        wrds = Txt.split()
        if wrds == []: return
        if wrds[0] == 'vdd':
            self.vdd = self.eval(wrds[1])
        elif wrds[0] == 'width':
            self.Widths[wrds[1] = self.eval(wrds[2])
        elif wrds[0] == 'force':
            for Wrd in wrds[1:]:
                if Wrd[0] in '0123456789':
                    self.Queue.append(('force',Net,self.eval(Wrd)))
                else:
                    self.Net = Wrd
        else:
            logs.log_error('vdriverClass got %s' % Txt)

