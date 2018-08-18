
import veri
import string
import logs


class i2cDriverClass:
    def __init__(self,SCL,SDA_DRIVE,SDA,BAUD,Monitors):
        self.scl =SCL
        self.sda_drive =SDA_DRIVE
        self.sda =SDA
        self.queue = []
        self.getting=''
        self.baudrate = BAUD
        self.baudcount=0
        Monitors.append(self)


    def transmit(self,String):
        wrds = string.split(String)
        for word in wrds:
            if (word in ['start','stop','idle','finish']):
                self.box(word)
            elif ('idle' in word)or('wait' in word):
                Cnt = int(word[4:])
                for ii in range(Cnt):
                    self.box('idle')
            else:
                for Char in word:
                    self.box(Char)

    def box(self,What):
        if (str(What)=='1'):
            self.queue.extend([(0,1),(1,1),(0,1)])
        elif (str(What)=='0'):
            self.queue.extend([(0,0),(1,0),(0,0)])
        elif (str(What)=='start'):
            self.queue.extend([(1,1),(1,0),(0,0)])
        elif (str(What)=='stop'):
            self.queue.extend([(0,0),(1,0),(1,1)])
        elif (str(What)=='idle'):
            self.queue.extend([(0,1)])
        elif (str(What)=='finish'):
            self.queue.append('finish')
        else:
            logs.log_error('box of i2c driver got "%s"  - not recognized'%str(What))
            
    def run(self):
        if (self.baudcount>0):
            self.baudcount -= 1
            return
        if (self.queue!=[]):
            self.baudcount=self.baudrate 
            if self.queue[0]=='finish':
                logs.finish_now('i2c driver asked to finish')
                return
            (Scl,Dat) = self.queue.pop(0)
#            print self.scl,Scl,self.sda_drive,Dat,len(self.queue),self.sda
            veri.force(self.scl,str(Scl))
            veri.force(self.sda_drive,str(Dat))
            if (Scl==0)and(Dat==1):
                Get = veri.peek(self.sda)
                self.getting += Get
