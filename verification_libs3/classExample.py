
import string
import logs
import veri


class exampleClass(logs.driverClass):
    def __init__(self,Path,Monitors):
        logs.driverClass.__init__(self,Path,Monitors)
        if Monitors: Monitors.append(self)
        self.Queue = []

    def run(self):
        if self.Queue == []: return
        if self.waiting>0:
            self.waiting -= 1
            return
        Cmd = self.Queue.pop(0) 
        if Cmd[0] == 'force':
            for Sig,Val in Cmd[1:]:
                self.force(Sig',Val)
        elif Cmd[0] == 'display':
            Res = ''
            for Sig in Cmd[1:]:
                Val = self.peek(Sig')
                Res += ' %s=%x' % (Sig,Val)
            logs.log_info("DISPLAY: %s" % Res)
    def busy(self):
        return self.Queue != []
    def onFinish(self):
        return

    def action(self,Txt):
        wrds = Txt.split()
        if wrds == []: return
        if wrds[0] == 'write':
            Addr = hex(self.eval(wrds[1]))
            Data = hex(self.eval(wrds[2]))
            self.Queue.append(['force',('addr',Addr),('addr',Addr),('data',Data),('data',Data)])
            self.Queue.append(['force',('ld',1),('ld',1)])
            self.Queue.append(['force',('ld',0),('ld',0)])

        elif wrds[0] == 'read':
            Addr = hex(self.eval(wrds[1]))
            self.Queue.append(['force',('addr',Addr),('addr',Addr)])
            self.Queue.append(['force',('read_en',1),('read_en',1)])
            self.Queue.append(['display','drv_rout'])
            self.Queue.append(['force',('read_en',0),('read_en',0)])


        else:
            logs.log_error('exampleClass got %s' % Txt)

