
import string
import logs
import veri


class serialApb(logs.driverClass):
    def __init__(self,Path,Monitors,uart):
        logs.driverClass.__init__(self,Path,Monitors)
        Monitors.append(self)
        self.uart = uart
        self.Queue = []

    def run(self):
        return
    def busy(self,Where=False):
        return self.uart.busy(Where)
    def onFinish(self):
        return

    def action(self,Txt,Origs=[]):
        wrds = Txt.split()
        if wrds == []: return
        if wrds[0] == 'write':
            Addr = self.eval(wrds[1])
            Data = self.eval(wrds[2])
            Str = 'tx A%x.w%x.' % (Addr,Data)
            logs.log_info('%s   // %s' % (Str[3:],wrds),'uart')
            self.uart.action(Str)
        elif wrds[0] == 'read':
            Addr = self.eval(wrds[1])
            self.uart.action('tx A%x.R.' % (Addr))
        elif wrds[0] == 'ram':
            Addr = self.eval(wrds[1])
            Data = self.eval(wrds[2])
            Str = 'tx A%x.w%x.' % ((0x10000+Addr),Data)
            logs.log_info('%s   // %s' % (Str[3:],wrds),'uart')
            self.uart.action(Str)
        else:
            logs.log_error('exampleClass got %s' % Txt)

