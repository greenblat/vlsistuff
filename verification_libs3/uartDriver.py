
# drives uart for debug on testbench.
import logs
import veri


class uartDriver(logs.driverClass):
    def __init__(self,Path,Monitors):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Queue = []
        self.rxstr = ''
        

    def run(self):
        self.txtx()
        self.rxrx()

    def rxrx(self):
        if self.peek('rx_valid') == 1:
            rxdata = self.peek('rxdata')
            if (rxdata<0): rxdata = 0
            logs.log_info('RX %x %s   "%s"' % (rxdata,chr(rxdata),self.rxstr))
            if rxdata == 10: 
                self.rxstr = self.rxstr + ' <CRLF>'
            else:
                self.rxstr = self.rxstr + chr(rxdata)
            if rxdata == 10:
                logs.log_info('RXSTR %s'% self.rxstr)
                self.rxstr = ''


    def txtx(self):
        if self.waiting>0:
            self.force('write_tx',0)
            self.waiting -= 1
            return
        if self.Queue == []: return
        if self.peek('tx_empty')==0: return
        Char = self.Queue.pop(0) 
        if len(Char) == 1:
            Code = ord(Char)
            self.force('txdata',hex(Code))
            self.force('write_tx',1)
        elif Char.startswith('0x'):
            Code = eval(Char)
            self.force('txdata',hex(Code))
            self.force('write_tx',1)
        elif Char == 'CRLF':
            self.force('txdata',0xa)
            self.force('write_tx',1)
        else:
            logs.log_error('bad token for uartDriver "%a"s' % Char)
        self.waiting = 8
    def busy(self,Why=False):
        return self.Queue != []

    def onFinish(self):
        return

    def read(self,Addr,Data=0):
        self.action('read %s' % (hex(Addr)))
    def write(self,Addr,Data):
        self.action('write %s %s' % (hex(Addr),hex(Data)))

    def action(self,Txt,Orig=[]):
        wrds = Txt.split()
        if wrds == []: return
        elif (wrds[0] == 'uartfile'):
            Fname = wrds[1]
            File = open(Fname)
            Lines = File.readlines()
            File.close()
            for line in Lines:
                Str = 'tx %s' % (line)
                self.action(Str)
            logs.log_info("GIVENFILE %d" % len(self.Queue))

        elif (wrds[0] == 'tx'):
            logs.log_info('TX %s' % Txt,'uart')
            for wrd in wrds[1:]:
                if  wrd.startswith('0x'):
                    self.Queue.append(wrd)
                elif  wrd == 'CRLF':
                    self.Queue.append(wrd)
                else:
                    for Chr in wrd:
                        self.Queue.append(Chr)
        elif (wrds[0] == 'write'):
            Addr = self.eval(wrds[1])
            Data = self.eval(wrds[2])
            Str = 'tx A%x. W%x. CRLF' % (Addr,Data)
            self.action(Str)

        elif (wrds[0] == 'read'):
            Addr = self.eval(wrds[1])
            Str = 'tx A%x. R. CRLF' % (Addr)
            self.action(Str)
        else:
            logs.log_error('vdriverClass got %s' % Txt)


