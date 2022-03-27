


import logs
import veri
import sys,string,os
TB = 'tb'
class i2cSlaveClass(logs.driverClass):
    def __init__(self,Path,Monitors,Freq=1,Renames={}):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Queue = []
        self.bitqueue = []
        self.Renames = Renames
        self.force('sda_out',1)
        self.Freq =Freq
        self.RX = []
        self.Check = False
        self.SDA = '1111'
        self.SCL = '1111'
        self.BYTE = ''
        self.state = 'idle'

    def force(self,Sig,Val):
        if Sig in self.Renames: Sig = self.Renames[Sig]
        logs.driverClass.force(self,Sig,Val)

    def peek(self,Sig):
        if Sig in self.Renames: Sig = self.Renames[Sig]
        return logs.driverClass.peek(self,Sig)

    def analyze(self):
        if self.state == 'idle':
            self.state = 'command'
            self.slave_addr = logs.intx(self.BYTE[:-2])
            self.read_notwrite = logs.intx(self.BYTE[-2])
            logs.log_info('I2C SLAVE ADDR  %02x READ/WRITE=%d' % (self.slave_addr,self.read_notwrite))
        elif self.state == 'command':
            self.command = logs.intx(self.BYTE[:-1])
            logs.log_info('I2C COMMAND  %02x addr=%02x READ/WRITE=%d' % (self.command,self.slave_addr,self.read_notwrite))
            self.state = 'writing0'
        elif self.state == 'writing0':
            self.lobyte = logs.intx(self.BYTE[:-1])
            logs.log_info('I2C LOBYTE  %02x cmd=%02x addr=%02x READ/WRITE=%d' % (self.lobyte,self.command,self.slave_addr,self.read_notwrite))
            self.state = 'writing1'
        elif self.state == 'writing1':
            self.hibyte = logs.intx(self.BYTE[:-1])
            logs.log_info('I2C HIBYTE  %02x cmd=%02x addr=%02x READ/WRITE=%d' % (self.hibyte,self.command,self.slave_addr,self.read_notwrite))
            self.state = 'stop'
        elif self.state == 'reading':
            self.read_notwrite = logs.intx(self.BYTE[-2])
            logs.log_info('I2C SLAVE ADDR AGAIN  %02x READ/WRITE=%d' % (self.slave_addr,self.read_notwrite))
            self.state = 'readinglo'
        elif self.state == 'readinglo':
            self.state = 'readinghi'
            self.rlobyte = logs.intx(self.BYTE[:-1])
            logs.log_info('I2C RLOBYTE  %02x cmd=%02x addr=%02x READ/WRITE=%d' % (self.rlobyte,self.command,self.slave_addr,self.read_notwrite))
        elif self.state == 'readinghi':
            self.state = 'stop'
            self.rhibyte = logs.intx(self.BYTE[:-1])
            logs.log_info('I2C RHYBYTE  %02x cmd=%02x addr=%02x READ/WRITE=%d' % (self.rhibyte,self.command,self.slave_addr,self.read_notwrite))


    def run(self):
        sda = self.peekbin('sda')
        scl = self.peekbin('scl')
        self.SDA += sda
        self.SDA = self.SDA[1:]
        self.SCL += scl
        self.SCL = self.SCL[1:]
        if self.SCL == '1111':
            if self.SDA == '0011':
                logs.log_info('STOP')
                self.BYTE = ''
                if self.state == 'stop':
                    self.state = 'idle'
                else:
                    logs.log_error('expected stop state (%s)' % self.state)
                    self.state = 'idle'
            if self.SDA == '1100':
                logs.log_info('START %s ' %self.state)
                if self.state == 'writing0':
                    self.state = 'reading'
                self.BYTE = ''
        elif self.SCL == '0000':
            if len(self.BYTE) == 8:
                self.force('sda_slave',0)
            else:
                self.force('sda_slave',1)
        elif self.SCL == '0011':
            if self.SDA == '1111':
                if len(self.BYTE) == 9: 
                    self.analyze()
                    self.BYTE = ''
                self.BYTE += '1'
            if self.SDA == '0000':
                if len(self.BYTE) == 9: 
                    self.analyze()
                    self.BYTE = ''
                self.BYTE += '0'
        self.force('LEN',len(self.BYTE))
        self.force('dbgsda','0b'+self.SDA)
        self.force('dbgscl','0b'+self.SCL)

