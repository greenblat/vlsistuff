import random
import logs

class firModel(logs.driverClass):
    def __init__(self,Path,Monitors):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Enable = False
        self.Queue = []
        self.Samples = [0,0,0,0,0,0,0,0]

    def run(self):
        if not self.Enable:
            return 
        self.incoming()
        self.outgoing()

    def incoming(self):
        if not self.valid('vldin'):return
        Sample = self.peek('sample')
        self.Samples.insert(0,Sample)
        self.Samples.pop(-1)
        Coeffs = self.peek('coeffs')
        Sum = 0
        Coefsum = 0
        for ii in range(8):
            Coeff = (Coeffs>>(8*ii)) & 0xff
            Coefsum += Coeff
            Sum += Coeff * self.Samples[ii]
#            logs.log_info('ii=%x sum=%x coeff=%x sample=%x' % (ii,Sum,Coeff,self.Samples[ii]))

        ScaleFactor = self.peek('scalefactor')
        Sum = Sum >>ScaleFactor
        Max = (Coefsum * 255) >> ScaleFactor
        Sum = min(255,Sum)  #saturation
        if (Max>255):
            logs.log_warning('ScaleFactor is not enough max takes %d bits' % Max.bit_length())
        self.Queue.append(Sum)

    def outgoing(self):
        if not self.valid('vldout'): return
        Result = self.peek('result')
        Exp = self.Queue.pop(0)
        if Result>=0:
            logs.log_ensure(Result==Exp," exp=%x act=%x" % (Exp,Result))

    def  action(self,Txt):
        if 'enable' in Txt: self.Enable = True
        if 'disable' in Txt: self.Enable = False
        return

    def  onFinish(self):
        return
    def  busy(self):
        return False




