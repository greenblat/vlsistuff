

import logs
import veri
import sys,string,os

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

    def action(self,Txt):
        wrds = Txt.split()
        Cmd = wrds[0]
        if Cmd =='read':
            if len(wrds)==2:
                self.read(wrds[1])
            else:
                self.read(wrds[1],wrds[2])
        elif Cmd =='write':
            self.write(wrds[1],wrds[2])
        elif Cmd =='wait':
            self.wait(wrds[1])
        elif Cmd =='waitNotBusy':
            return
        else:
            logs.log_error('action not recogninzed "%s"'%Cmd)


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
        for Chr in LL:
#                             clk,chr,ss
            self.Queue.append((1,Chr,0))
            self.Queue.append(('wait',self.Freq))
            self.Queue.append((0,Chr,0))
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
        if (What[0]==0)and(self.was==1):            
            self.Back.append(str(self.peek('spi_miso')))
            self.Forw.append(str(What[1]))
#            veri.force('tb.help0',str(len(self.Back)))
        self.was = What[0]
        self.force('spi_clk',What[0])
        self.force('spi_mosi',What[1])
        self.force('spi_ss',What[2])

        if len(self.Back)>=32:
            FL = self.Forw[:32]
            self.Forw = self.Forw[32:]
            Part = FL[:12]
            Part.reverse()
            Addr = int(''.join(Part),2)
            Cmd = '?'
            if FL[12]=='0': Cmd='RD'
            if FL[12]=='1': Cmd='WR'


            LL = self.Back[:32]
            self.Back = self.Back[32:]
            AA = ''.join(LL)
            LL.reverse()
            BB = ''.join(LL)
            AX,BX = 'x','x'
            if '-1' not in AA:
                AX = '%08x'%(int(AA,2))
            if '-1' not in BB:
                BX = '%08x'%(int(BB,2))
            logs.log_info('SPI MISO %s %s cmd=%s addr=%x'%(AX,BX,Cmd,Addr))
            if Cmd=='RD':
                if Addr in self.Expects:
                    Exp,Mask,Comment = self.Expects[Addr]
                    Exp = '%04x'%Exp
                    try:
                        Act = '%04x'%(int(BX[:4],16) & ((1<<Mask)-1))
                    except:
                        Act = 'x'
                    if Exp==Act:
                        logs.log_correct('MISO "%s" exp=%s act=%s for add=%x'%(Comment,Exp,Act,Addr))
                    else:
                        logs.log_wrong('MISO "%s" exp=%s act=%s for add=%x   %s %s '%(Comment,Exp,Act,Addr,type(Exp),type(Act)))
                        


def reverseBin(Txt):
    List = list(Txt)
    List.reverse()
    Str = ''.join(List)
    return Str
