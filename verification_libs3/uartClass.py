
import veri
import logs


class uartClass(logs.driverClass):
    def __init__(self,Path,Monitors,rxd='rxd',txd='txd'):
        logs.driverClass.__init__(self,Path,Monitors)
        self.rxd = rxd
        self.txd = txd
        self.baudRate = 100
        self.txQueue = []
        self.txWaiting=0

        self.rxState = 'idle'
        self.rxQueue = []
        self.rxWaiting=0
        self.rxByte=''
        self.force(self.rxd,1)
        self.RxStr = ''

    def busy(self,Why=False):
        return (self.txQueue != []) or (self.rxQueue != [])
      
    def run(self):
        self.runTx()
        self.runRx()

    def action(self,Str):
        Wrds  = Str.split()
        if Wrds[0]=='tx':
            for Wrd in Wrds[1:]:
                self.send(Wrd)
            self.send('\x0a')
        elif Wrds[0]=='baudrate':
            self.baudRate = eval(Wrds[1])
        elif Wrds[0]=='rx':
            logs.log_info('UART RX  "%s" '%(self.RxStr))
        else:
            logs.log_error('action by uart is not : %s'%(Str))

    def send(self,Byte):
        if type(Byte) is str:
            if len(Byte)==1:
                Byte = ord(Byte)
                self.send(Byte)
                return
            elif Byte == 'CRLF':
                self.send(10)
                return
            else:
                for Chr in Byte:
                    self.send(Chr)
                return
        self.txQueue.append(0)
        for II in range(0,8):
            Val = (Byte>>II)&1
            self.txQueue.append(Val)
        self.txQueue.append(1)
        self.txQueue.append(1)
        self.txQueue.append(1)


    def runTx(self):
        if self.txWaiting>0:
            self.txWaiting -= 1
            return

        if self.txQueue==[]:
            self.force(self.rxd,1)
            return

        Bit = self.txQueue.pop(0)
        self.force(self.rxd,Bit)
        self.txWaiting = self.baudRate

    
    def runRx(self):
        if self.rxWaiting>0:
            self.rxWaiting -= 1
#            if (self.rxWaiting == 1):
#                logs.log_info("rxwait %s %s " % (self.rxState,self.rxByte))
            return
        
        if self.rxState=='idle':
            Rxd = self.peek(self.txd)
            if Rxd==0:
                self.rxState='bit0'
                self.rxWaiting = self.baudRate/2
                return
        elif self.rxState=='bit0':
                self.rxState='bitx'
                self.rxWaiting = self.baudRate
                Rxd = self.peek(self.txd)
                if Rxd!=0: 
                    logs.log_error('ilia rxd start bit isnt there')
                    self.rxState='idle'
                return
        elif self.rxState=='bitx':
            Rxd = self.peek(self.txd)
            self.rxByte = str(Rxd) + self.rxByte 
            if len(self.rxByte)==8:
                self.rxState = 'stop'
#                self.rxQueue.append(self.rxByte)
                Int = logs.intx(self.rxByte)
                if ((Int>=0)and(Int<256)):
                    Chr = chr(logs.intx(self.rxByte))
                else:
                    Chr = '(ERR%s)'%self.rxByte
                self.RxStr += Chr
#                logs.log_info('uart rxByte %s   "%s" '%(self.rxByte,self.RxStr))
                try:
                    if ord(Chr) <= 10:
                        logs.log_info('UART RX  "%s" '%(self.RxStr[:-1]))
                        self.RxStr = ''
                except:
                    logs.log_info('UART RX ERROR |%s|  "%s" '%(Chr,self.RxStr))
                    self.RxStr = ''

#                veri.force('tb.marker','0b'+self.rxByte)
                self.rxByte=''
            self.rxWaiting = self.baudRate
        elif self.rxState=='stop':
            Rxd = self.peek(self.txd)
            if Rxd==0:
                logs.log_error('ilia rxd stop bit isnt there')
            self.rxState='idle'

    def onFinish(self):
        return

                



