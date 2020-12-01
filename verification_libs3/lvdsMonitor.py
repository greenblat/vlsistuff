
# import tenTo8
import encdec_8b10b
import veri


# encdec_8b10b.trans10to8(ten)

def negate(Str):
    X = Str.replace('0','x')
    X = X.replace('1','0')
    X = X.replace('x','1')
    return X

K280_m = '0011110100'
K280_p = negate(K280_m)


K281_m = '0011111001'
K281_p = negate(K281_m)

K283_m = '0011110011'
K283_p = negate(K283_m)

K284_m = '0011110010'
K284_p = negate(K284_m)

K285_m = '0011111010'
K285_p = negate(K285_m)

K287_m = '0011111000'
K287_p = negate(K287_m)



import logs

class lvdsMonitor(logs.driverClass):
    def __init__(self,Path,Monitors):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Pin0 = 'lvds0'
        self.Pin1 = 'lvds1'
        self.LVDS0 = ''
        self.LVDS1 = ''
        self.state0 = 'idle'
        self.state1 = 'idle'
        self.CRC = []
        self.Ones0 = 0
        self.Ones1 = 0
        self.txc_0 = -1 
        self.txd_0 = -1 
        self.txc_1 = -1 
        self.txd_1 = -1 
        self.Stream = [[],[]]
        self.Chars0,self.Chars1 = [],[]
        self.syncState = 'idle'
        self.dins = []
        self.State = 'idle'
        self.Frame = []
        self.FrameId = 0
        self.Bytes = 0
        self.Indx = 0
        self.keep = False

    def run(self):
#        self.run1()
        self.run0()



    def run1(self):
        if veri.peek('tb.dut.dig_top.usat_tx.enable')!='1': return
        cnt = logs.peek('tb.dut.dig_top.usat_tx.serializer.cnt')
        if cnt!=11: return
        din0 = veri.peek('tb.dut.dig_top.usat_tx.serializer.data_in_0')
        din1 = veri.peek('tb.dut.dig_top.usat_tx.serializer.data_in_1')
        Chr0 = encdec_8b10b.trans10to8(din0)
        Chr1 = encdec_8b10b.trans10to8(din1)
        Chr0 = nice(Chr0)
        Chr1 = nice(Chr1)
        self.Stream[0].append(Chr0)
        self.Stream[1].append(Chr1)
        self.dins.append(('%03x'%(logs.intx(din1)),'%03x'%(logs.intx(din0))))
        if len(self.dins)>8: self.dins.pop(0)
        if len(self.Stream[0])>8: self.Stream[0].pop(0)
        if len(self.Stream[1])>8: self.Stream[1].pop(0)
#        if len(self.Stream[0])==8:
#            logs.log_info('STREAM side0 %d %s %s'%(len(self.Stream[0]),self.Stream[0],self.Stream[1]))
#            logs.log_info('STREAM side1 %d %s %s'%(len(self.Stream[0]),self.Stream[0],self.Stream[1]))

        if syncAll(self.Stream[0]) and syncAll(self.Stream[1]):
            self.syncState = 'idle'
        if self.syncState == 'idle':
            if sync8(self.Stream[0]) and sync8(self.Stream[1]): 
                self.syncState = 'sync8'
                self.Stream[0]=[]
                self.Stream[1]=[]
        elif self.syncState == 'sync8':
            if len(self.Stream[0])==8:
                logs.log_info('STREAM8   %s %s'%(self.Stream[1],self.Stream[0]))
#                logs.log_info('STREAM8 X  %s'%str(self.dins))
                self.Stream[0]=[]
                self.Stream[1]=[]
                




        txc_0 = logs.peek('tb.dut.dig_top.usat_tx.txc_0')
        txd_0 = logs.peek('tb.dut.dig_top.usat_tx.txd_0')
        txc_1 = logs.peek('tb.dut.dig_top.usat_tx.txc_1')
        txd_1 = logs.peek('tb.dut.dig_top.usat_tx.txd_1')

#        logs.log_info('side0 %s %s  %s %02x     side1 %s %s    %s %02x'%(din0,Chr0,self.txc_0,self.txd_0,din1,Chr1,self.txc_1,self.txd_1))

        self.txc_0 = txc_0
        self.txd_0 = txd_0
        self.txc_1 = txc_1
        self.txd_1 = txd_1


    def run0(self):
        lvds0 = self.peekbin(self.Pin0)
        lvds1 = self.peekbin(self.Pin1)
        self.run_lvds(lvds0,lvds1) 


    def run_lvds(self,lvds0,lvds1):
        if lvds0 == '1': self.Ones0 += 1
        if lvds0 == '0': self.Ones0 -= 1
        if lvds1 == '1': self.Ones1 += 1
        if lvds1 == '0': self.Ones1 -= 1

        self.LVDS0 += lvds0
        if len(self.LVDS0)>80: self.LVDS0 = self.LVDS0[-80:]
        self.LVDS1 += lvds1 
        if len(self.LVDS1)>80: self.LVDS1 = self.LVDS1[-80:]

        if self.state0 == 'idle':
            if len(self.LVDS0)>60:
                if  idleChar(self.LVDS0[:10]) and idleChar(self.LVDS0[10:20]) and idleChar(self.LVDS0[20:30]):
                    if  idleChar(self.LVDS0[30:40]) and idleChar(self.LVDS0[40:50]) and idleChar(self.LVDS0[50:60]):
                        self.state0 = 'sync8'
                        self.LVDS0 = self.LVDS0[60:]
        elif self.state0 == 'sync8':
            if len(self.LVDS0)>=10:
                Chr0 = encdec_8b10b.trans10to8(self.LVDS0[:10])
                Chr0 = nice(Chr0)
                self.Chars0.append(Chr0)
                logs.log_info('CHARS0 %s %s'%(str(self.Chars0),str(self.LVDS0)),2)
                self.LVDS0 = self.LVDS0[10:]
                    
                
        if self.state1 == 'idle':
            if len(self.LVDS1)>60:
                if  idleChar(self.LVDS1[:10]) and idleChar(self.LVDS1[10:20]) and idleChar(self.LVDS1[20:30]):
                    if  idleChar(self.LVDS1[30:40]) and idleChar(self.LVDS1[40:50]) and idleChar(self.LVDS1[50:60]):
                        self.state1 = 'sync8'
                        self.LVDS1 = self.LVDS1[60:]
        elif self.state1 == 'sync8':
            if len(self.LVDS1)>=10:
                Chr1 = encdec_8b10b.trans10to8(self.LVDS1[:10])
                Chr1 = nice(Chr1)
                self.Chars1.append(Chr1)
                logs.log_info('CHARS1 %s %s'%(str(self.Chars1),str(self.LVDS1)),2)
                self.LVDS1 = self.LVDS1[10:]

        if self.State == 'idle':
#            if self.keep:
#                logs.log_info('CCCC 1=%s 0=%s'%(self.Chars1,self.Chars0))
            if len(self.Chars1)>=10:
                if (self.Chars1[0] in ['K285','K283','K280'])and(self.Chars1[1] == '00')and(self.Chars1[2]=='K281'):
                    if (self.Chars0[0] in ['K285','K283','K280'])and(self.Chars0[1] == '00'):
                        self.State = 'inframe'
                        self.Frame = self.Chars1[2:10]+ self.Chars0[2:10]
                        self.Chars1 = self.Chars1[10:]
                        self.Chars0 = self.Chars0[10:]
                        logs.log_info('FRAMEStart1 %s'%str(self.Frame))
            elif len(self.Chars1)==8:
                if (self.Chars1[0]=='K281'):
                    self.State = 'inframe'
                    self.Frame = self.Chars1[:8]+ self.Chars0[:8]
                    self.Chars1 = self.Chars1[8:]
                    self.Chars0 = self.Chars0[8:]
                    logs.log_info('FRAMEStart2 %s'%str(self.Frame))
        
        elif self.State == 'inframe':
            if len(self.Chars1)>=8:
                self.Frame += self.Chars1[:8]+ self.Chars0[:8]
                self.Chars1 = self.Chars1[8:]
                self.Chars0 = self.Chars0[8:]

                if 'K287' in self.Frame:
                    FRM = self.Frame[:self.Frame.index('K287')] 
                    FRM = FRM[self.Frame.index('K281'):] 
                    self.Frame = self.Frame[self.Frame.index('K287'):]
                    Len = len(FRM)-8 
                    self.Bytes += Len
                    logs.log_info('FRAME #%d bytes=%d / %d : %s'%(self.FrameId,Len,self.Bytes,FRM))
                    if Len>100:
                      self.assembleData2(FRM[1:-1]) 
                    self.FrameId += 1
                    self.State = 'idle'
                    self.keep =True
            



        if len(self.Chars1)>10: self.Chars1.pop(0)
        if len(self.Chars0)>10: self.Chars0.pop(0)

    def assembleData2(self,Bytes):
        while Bytes[-1] == 'K284': Bytes.pop(-1)
        state = 0
        while Bytes!=[]:
            P0 = self.sngl(Bytes.pop(0))
            P1 = self.sngl(Bytes.pop(0))
            state = self.runPair(P0,P1,state)

    def sngl(self,X):
        try:
            return int(X,16)
        except:
            return X



    def assembleData(self,Bytes):
        while Bytes[-1] == 'K284': Bytes.pop(-1)
        state = 0
        while Bytes!=[]:
            Seq0 = Bytes[:8]
            Seq1 = Bytes[8:16]
            logs.log_info('SEQ 1=%s 0=%s'%(Seq0,Seq1))
            while Seq1!=[]:
                P1 = int(Seq1.pop(0),16)
                P0 = int(Seq0.pop(0),16)
                state = self.runPair(P0,P1,state)
            Bytes  = Bytes[16:]

    def report__(self,St):
        Exp1,Exp0,Indx = extract(self.Pix1,self.Pix0)
        Lefts = len(list(PIXELS[3].keys()))
        if Indx<0: 
            logs.log_wrong('#%d %s %d (left %d) self.Pix1 = %x  self.Pix0 = %x (E1=%x E0=%x)'%(self.Indx,St,Indx,Lefts,self.Pix1,self.Pix0,Exp1,Exp0))
        else:
            logs.log_info('#%d %s %d self.Pix1 = %x  self.Pix0 = %x (E1=%x E0=%x)'%(self.Indx,St,Indx,self.Pix1,self.Pix0,Exp1,Exp0))
        self.Indx += 1
        if self.Indx>2368:
            for Key in PIXELS[3]:
                logs.log_info('leftovers ind=%d pix %04x %04x'%(PIXELS[3][Key],Key[0],Key[1]))
    def report(self,St):
        Gr1e = gray_encode(self.Pix1)
        Gr1d = gray_decode(self.Pix1)

        Gr0e = gray_encode(self.Pix0)
        Gr0d = gray_decode(self.Pix0)

        logs.log_info('REPORT %s %04x %04x en(%04x %04x)'%(St,self.Pix0,self.Pix1,Gr0e,Gr1e)) 
        
    def runPair(self,P0,P1,state):
        if state==0:
            self.Pix1 = (P1>>6)& 3
            self.Pix0 = ((P1&0x3f)<<8)+P0
            state = 1
        elif state==1:
            self.Pix1 = self.Pix1 + (P0<<2) + ((P1 & 0xf)<<10)
            self.report('st1')
            self.Pix0 = (P1>>4)&0xf
            state = 2
        elif state==2:
            self.Pix0 = self.Pix0 + (P0<<4) + ((P1 & 3)<<12)
            self.Pix1 = P1>>2
            state = 3
        elif state==3:
            self.Pix1 = self.Pix1 + (P0<<6)
            self.report('st3')
            self.Pix0 = P1
            state = 4
        elif state==4:
            self.Pix0 = self.Pix0 + ((P0 & 0x3f)<<8)
            self.Pix1 = ((P0 >>6) & 0x3) + (P1<<2)
            state = 5
        elif state==5:
            self.Pix1 = self.Pix1 + ((P0 & 0xf)<<10)
            self.report('st5')
            self.Pix0 = (P1<<4)+ ((P0>>4) & 0xf)
            state = 6
        elif state==6:
            self.Pix1 = (P1<<6)+(P0>>2)
            self.Pix0 = self.Pix0 + ((P0&3)<<12)
            self.report('st6')
            state = 0
        return state

        


    def trace(self,LVDS,state,Side):
        if len(LVDS)<10:
            return state,LVDS
        if state=='idle':
            LVDS = self.idles(LVDS)
            if LVDS:
                return 'sync0',LVDS
            return False
        elif state=='sync0':
            Chr = encdec_8b10b.trans10to8(LVDS[5:10]+LVDS[0:5])
            self.Stream[Side].append(Chr)
            if len(self.Stream[Side])>8:
                self.Stream[Side].pop(0)
#            if len(self.Stream[Side])==8:
            logs.log_info('STREAM %s %d %s'%(Side,len(self.Stream[Side]),self.Stream[Side]))

        elif state=='sync':
            Chr = encdec_8b10b.trans10to8(LVDS[5:10]+LVDS[0:5])
            logs.log_info('%s sync %s   %s'%(Side,Chr,state),2)
            Str = self.cutIt(LVDS,[K281_m,K281_p])
            if Str:
                return 'sof',Str
            else:
                Str = self.cutIt(LVDS,[K280_m,K280_p,K283_m,K283_p,K285_m,K285_p])
                if not Str:
                    What = encdec_8b10b.trans10to8(LVDS[5:10]+LVDS[0:5])
                    logs.log_info('token? %s    %s '%(LVDS[:10],What),2)
                    return 'sync',LVDS[10:]
                else:
                    return 'sync',Str
        elif state=='sof':
            Str = self.cutIt(LVDS,[K287_m,K287_p])
            if Str:
                return 'eof',Str
                
            Chr = LVDS[:10]
            What = encdec_8b10b.trans10to8(LVDS[5:10]+LVDS[0:5])
            logs.log_info('header %s    %s'%(Chr,What),3)
            return 'sof',LVDS[10:]
        elif state=='eof':
            Chr = LVDS[:10]
            Str = LVDS[10:]
            logs.log_info('reserved %s'%(Chr),3)
            return 'res',LVDS
        elif state=='res':
            Chr = LVDS[:10]
            Str = LVDS[10:]
            logs.log_info('crc %s'%(Chr),3)
            self.CRC.append(Chr)
            if (len(self.CRC)==4): 
                return 'crc',Str
            return 'res',LVDS
        elif state=='crc':
            Chr = LVDS[:10]
            Str = LVDS[10:]
            logs.log_info('token %s'%(Chr),3)
            return 'sync',Str

            






    def idles(self,LVDS):
        Str = self.cutIt(LVDS,[K280_m,K280_p,K283_m,K283_p,K285_m,K285_p])
        if not Str: return False
        Str = Str[10:]
        Str = self.cutIt(Str,[K280_m,K280_p,K283_m,K283_p,K285_m,K285_p])
        if not Str: return False
        Str = Str[10:]
        Str = self.cutIt(Str,[K280_m,K280_p,K283_m,K283_p,K285_m,K285_p])
        if not Str: return False
        Str = Str[10:]
        return Str


    def cutIt(self,Str,Chars):
        for Char in Chars:
            Chrx = Char
            if ((Chrx) in Str) and (Str.index(Chrx)<10):
                Str = Str[Str.index(Chrx):]
                return Str
        return False 


def extract(Pix0,Pix1):
    Key = (Pix0,Pix1)
    if Key in PIXELS[2]:
        Ind = PIXELS[2].index(Key)
        Exp0,Exp1 = PIXELS[2][Ind]
        if Key in PIXELS[3]: PIXELS[3].pop(Key)
        return Exp1,Exp0,Ind
    return (0x9999,0x9999,-9999) 



def nice(Char):
    if type(Char) is tuple: return str(Char)

    if Char[0] in '01': return '%02x'%int(Char,2)
    return Char
    
def sync8(Seq):
    if len(Seq)<8: return False
    if (Seq[7][0]=='K'): return False
    for II in range(7):
        if (Seq[II][0]!='K'): return False
    return True

def syncAll(Seq):
    if len(Seq)<8: return False
    for II in range(8):
        if (Seq[II][0]!='K'): return False
    return True

def idleChar(Str):
    return Str in [K280_m,K280_p,K283_m,K283_p,K285_m,K285_p]


def gray_encode(n):
    return n ^ n >> 1

def gray_decode(n):
    m = n >> 1
    while m:
        n ^= m
        m >>= 1
    return n


