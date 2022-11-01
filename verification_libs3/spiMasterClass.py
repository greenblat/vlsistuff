

import logs
import veri
import sys,string,os
TB = 'tb'
class spiMasterClass(logs.driverClass):
    def __init__(self,Path,Monitors,Freq=1,Renames={}):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Queue = []
        self.qu = []
        self.Renames = Renames
        self.force('spi_ss',1)
        self.force('spi_clk',0)
        self.Freq = Freq
        self.Back = []
        self.Forw = []
        self.was = 0
        self.Expects = {}
        self.Catch = False
        self.Miso = ''
    def callback(self,Txt):
        return Txt
    def force(self,Sig,Val):
        if Sig in self.Renames: Sig = self.Renames[Sig]
        logs.driverClass.force(self,Sig,Val)

    def peek(self,Sig):
        if Sig in self.Renames: Sig = self.Renames[Sig]
        return logs.driverClass.peek(self,Sig)

    def idle(self):
        if self.Queue!=[]: return False
        if self.qu!=[]: return False
        if self.waiting>0: return False
        return True
    def busy(self):
        return not self.idle()

    def action(self,Txt):
        wrds = Txt.split()
        Cmd = wrds[0]
        if Cmd =='send':
            Str = ''
            for Wrd in wrds[1:]:
                if Wrd == '?':
                    Str += '????????'
                else:
                    Abin = logs.binx(Wrd,8)
                    Str += Abin
            logs.log_info('SEND SPI %d %s'%(len(Str),Str))
            self.send(Str,1)
            return
                
        if Cmd =='read':
            if len(wrds)==2:
                self.read(wrds[1])
            else:
                self.read(wrds[1],wrds[2])
        elif Cmd =='write':
            self.write(wrds[1],wrds[2])
        elif Cmd =='wreg':
            Addr = eval(wrds[1])
            Data = eval(wrds[2])
            Str = 'send %s %s %s %s %s %s' % ( hex(0x00+((Addr>>8) & 0x7f)),hex(Addr & 0xff), hex((Data>>24)&0xff),hex((Data>>16)&0xff),hex((Data>>8)&0xff),hex(Data&0xff)   )
            self.action(Str)

        elif Cmd =='rreg':
            Addr = eval(wrds[1])
            Data = 0
            if len(wrds)>2:
                self.Expects[Addr] = eval(wrds[2]),0xffffffff,"RREG"
            Str = 'send %s %s %s %s %s %s' % ( hex(0x80+((Addr>>8) & 0x7f)),hex(Addr & 0xff), hex((Data>>24)&0xff),hex((Data>>16)&0xff),hex((Data>>8)&0xff),hex(Data&0xff)   )
            self.action(Str)


        elif Cmd =='wait':
            self.wait(wrds[1])
        elif Cmd =='waitNotBusy':
            return
        else:
            logs.log_error('spiMaster action not recogninzed "%s"'%Txt)


    def write(self,Addr,Data):
        Abin = logs.binx(Addr,12)
        Abin = reverseBin(Abin)

        Dbin = logs.binx(Data,16)
        Dbin = reverseBin(Dbin)
        Str = Abin+'1'+'000'+Dbin
        if 'b' in Str:
            logs.log_error('SPI WRITE %s'%Str)
        else:
            self.send(Str,1)


    def read(self,Addr,Check='no',Mask = 0xffff,Comment=''):
        logs.log_info('READ %x %s %s %s' % (Addr,Check,Mask,Comment))
        Abin = logs.binx(Addr,12)
        Abin = reverseBin(Abin)

        Dbin = 16*'0'
        Str = Abin+'0'+'000'+Dbin
        self.send(Str,1)
        if Check!='no':
            self.Expects[Addr] = Check,Mask,Comment


    def send(self,BinStr,Csn=1):
        if BinStr=='finish':
            self.Queue.append('finish')
            return
        if 'wait' in BinStr:
            wrds = BinStr.split()
            self.Queue.append(('wait',eval(wrds[1])))
            return

        Bin = BinStr.replace(' ','')
        LL = list(Bin)
#        LL.reverse()
        self.Queue.append((0,0,1))
        self.Queue.append(('wait',self.Freq))
        self.Queue.append((0,0,0))
        self.Queue.append(('wait',self.Freq))
        for Chr in LL:
#                             clk,chr,ss
            self.Queue.append((0,Chr,0))
            self.Queue.append(('wait',self.Freq))
            self.Queue.append((1,Chr,0))
            self.Queue.append(('wait',self.Freq))
        self.Queue.append((0,0,0))
        self.Queue.append(('wait',self.Freq))
        self.Queue.append((0,0,Csn))
        self.Queue.append(('wait',100))
        

    def run(self):
        if self.waiting>0:
            self.waiting -= 1
            return
        if self.Queue==[]: return
        What = self.Queue.pop(0)
        if What == 'finish':
            veri.finish()
            sys.exit()

        if What[0]=='wait': 
            self.waiting = What[1]
            return
        if self.Catch:
            self.Miso += str(self.peek('spi_miso'))
            self.Catch = False
            if len(self.Miso)>=32:
                self.callback(self.Miso)
                self.Miso = ''

        if (What[0]==0)and(self.was==1):            
            self.Back.append(str(self.peek('spi_miso')))
            self.Forw.append(str(What[1]))
#            veri.force(TB+'.help0',str(len(self.Back)))
        if What[1] == '?':
            if (What[0]==0)and(self.was==1):            
                self.force('spi_mosi',0)
                self.Catch = True
        else:
            self.Catch = False
            self.force('spi_mosi',What[1])
        self.force('spi_ss',What[2])
        self.was = What[0]
        self.force('spi_clk',What[0])

        if len(self.Back)>=48:
            logs.log_info('BACK %s\n                  %s' % (''.join(self.Back),''.join(self.Forw)))
            FL = self.Forw[:48]
            self.Forw = []
            Addr = int(''.join(FL[:15]).replace('?','0'),2)
            Cmd = '?'
            if FL[0]=='0': Cmd='RD'
            if FL[0]=='1': Cmd='WR'


            LL = self.Back[15:47]
            self.Back = []

            AA = ''.join(LL)
            try:
                AX = '%08x'%(int(AA,2))
            except:
                AX = AA
            logs.log_info('SPI MISO rdata=%s cmd=%s addr=%x'%(AX,Cmd,Addr))
            if Cmd=='RD':
                if Addr in self.Expects:
                    Exp,Mask,Comment = self.Expects[Addr]
                    Exp = '%04x'%Exp
                    try:
                        
                        Act = '%04x'%(int(AX,16) & ((1<<Mask)-1))
                    except:
                        logs.log_error("GOT %s " % AX)
                        Act = 'AX'
                    if Exp==Act:
                        logs.log_correct('MISO "%s" exp=%s act=%s for add=%x'%(Comment,Exp,Act,Addr))
                    else:
                        logs.log_wrong('MISO "%s" exp=%s act=%s for add=%x   %s %s '%(Comment,Exp,Act,Addr,type(Exp),type(Act)))
                        


def reverseBin(Txt):
    List = list(Txt)
    List.reverse()
    Str = ''.join(List)
    return Str

