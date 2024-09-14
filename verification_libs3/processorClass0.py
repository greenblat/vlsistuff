

import veri
import logs


class processorClass(logs.driverClass):
    def __init__(self,Path,Monitors,Axi):
        logs.driverClass.__init__(self,Path,Monitors)
        self.waitExpr = False
        self.state = 'idle'
        self.Axi = Axi
        self.activates = []
        self.was_state = '0'
        self.armCallback = False
        self.Code = False
        self.defines = {}
        self.Done = False

    def eval(self,Expr):
        Res =  self.SeqObj.eval(Expr)
        return Res

    def onFinish(self,Txt):
        return

    def callback(self,Addr,Data):
#        if (self.activates == []): 
#            logs.log_info('NO CALLBACK %s %s %x -> %x' % (self.Axi,self.state,Addr,Data))
#            return
#        self.state = self.activates.pop(0)
        logs.log_info('CALLBACK %s %s %x -> %x' % (self.Axi,self.state,Addr,Data))
        self.Data = Data
        self.armCallback = False


        
    def run(self):
        if self.waiting>0:
            self.waiting -= 1

        if self.waitExpr:
            Ok = self.eval(self.waitExpr)
#            logs.log_info('EVAL %s %s' % (self.waitExpr,Ok))
            if not Ok: return
            self.waitExpr = False
        if self.armCallback:
            return
        if not self.Code:
            self.Code = self.code()
        X = next(self.Code)
        if self.Done:
            self.Done = False
            self.Code = False

    def issue(self,Text):
        wrds = Text.split()
        Agent = wrds[0]
        if Agent in self.SeqObj.agents:
            self.SeqObj.agents[Agent].action(' '.join(wrds[1:]))
            self.SeqObj.agents[Agent].callback = self.callback
        else:
            logs.log_error('AGENT %s is not part of sequence' % Agent)


    def waitTill(self,Expr):
        self.waitExpr = Expr 

#    def code(self):
#        while not self.valid('xl_interrupt'):
#            self.waitExpr = 'dut0.xl_interrupt'
#            yield 'Ok'
#
#        self.issue('%s read 1 1 XL+status 2' % self.Axi)
#        self.armCallback = True
#        yield 'Ok'
#        self.status = self.Data
#        logs.log_info('GOT DATA111 %x' % self.status)
#   
#        self.issue('%s read 1 1 XL+rx_buffer_status 2' % self.Axi)
#        self.armCallback = True
#        yield 'Ok'
#        self.rx_buffer_status = self.Data
#        logs.log_info('RX_BUFFER_STATUS %x' % self.rx_buffer_status)
#        while self.valid('xl_interrupt'):
#            self.waitExpr = 'not dut0.xl_interrupt'
#            yield 'Wait'
#        self.Done = True
#        yield 'NotOk'
#
#    def code_source(self):
#        posedge('xl_interrupt')
#        axi_read('status')
#        axi_read('rx_buffer_status')
#        axi_read('rx_wide_packet')
#        negedge('xl_interrupt')
#


