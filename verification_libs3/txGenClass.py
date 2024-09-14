
# writes the correct stuff to tx parameters to send a frame
import logs
import random
import sys

ClFields = [('dlc',11),('idfield',11),('extendidfield',18),('remote',1),('extended',1)]
FdFields = [('dlc',11),('idfield',11),('extendidfield',18),('extended',1),('esi',1),('brs',1)]
XlFields = [('dlc',11),('idfield',11),('sdt',8),('sec',1),('rrs',1),('sbc',3),('pcrc',13),('vcid',8),('af',32)]

class txGenClass:
    def __init__(self,Father):
        self.clParams = {'dlc':0,'idfield':0x111,'extendidfield':0x3344,'remote':1,'extended':1}
        self.fdParams = {'esi':0,'brs':0,'idfield':0x111,'extendidfield':0x3344,'extended':1}
        self.xlParams = {'dlc':11 ,'idfield':11 ,'sdt':8 ,'sec':1 ,'rrs':1 ,'vcid':8 ,'af':32}
        self.Father = Father

    def action(self,Txt,Origs=[]):
        wrds = Txt.split()
        if wrds[0] == 'from_file':
            ww = wrds[1].split('=')
            if self.Father.txLines == []:
                File = open(ww[1])
                self.Father.txLines = File.readlines()
                ind = 0
                while ind<len(self.Father.txLines):
                    line = self.Father.txLines[ind]
                    if len(line)<5:
                        self.Father.txLines.pop(ind)
                    else:
                        ind += 1
                File.close()
            if self.Father.txLines == []: return
            Line = self.Father.txLines.pop(0)
            params = logs.getParams(Line)
            more = logs.getParams(' '.join(wrds[2:]))
            for prm in more: params[prm] = more[prm]
            wrds = Line.split()
            for prm in params:
                Expr = params[prm]
                Val = self.eval(Expr)
                self.clParams[prm] = Val
                self.fdParams[prm] = Val
                self.xlParams[prm] = Val
            self.action('send %s' % wrds[0])
            return
            
        if wrds[0] == 'cl':
            for wrd in wrds[1:]:
                ww = wrd.split('=')
                self.clParams[ww[0]] = self.eval(ww[1])
        elif wrds[0] == 'fd':
            for wrd in wrds[1:]:
                ww = wrd.split('=')
                self.fdParams[ww[0]] = self.eval(ww[1])
        elif wrds[0] == 'xl':
            for wrd in wrds[1:]:
                ww = wrd.split('=')
                self.xlParams[ww[0]] = self.eval(ww[1])
        elif wrds[0] == 'send':
            if wrds[1] == 'cl': self.generateCL()
            elif wrds[1] == 'fd': self.generateFD()
            elif wrds[1] == 'xl': self.generateXL()
            else:
                logs.log_error('!!!!txGenClass got wrong protocol (cl,fd,xl)!= %s' % Txt)

        else:
            logs.log_error('txGenClass got %s %s' % (wrds,Txt))

    def generateCL(self):
        
        Header0 = 0x10000000
        Header0 += self.clParams['dlc']
        Header0 += (self.clParams['idfield'])<<12
        if self.clParams['remote']:
            Header0 += 0x04000000
        if self.clParams['extended']:
            Header0 += 0x08000000
        self.addr = self.clParams['addr']
        Header1 = self.clParams['extendidfield']
        Header2 = 0
        self.apbs_ram(self.addr,Header0)
        self.apbs_ram(self.addr+4,Header1)
        self.apbs_ram(self.addr+8,Header2)
        Dlc = min(self.clParams['dlc'],8)
        Mask0 = 0xffffffff
        if (Dlc<4): Mask0 = (1<<8*Dlc)-1

        Mask1 = 0 
        if (Dlc>4):
            Dlc -= 4
            Mask1 = (1<<8*Dlc)-1


        Bytes0 = random.randint(0,0xffffffff) & Mask0
        Bytes1 = random.randint(0,0xffffffff) & Mask1
#        Bytes0 = 0x11223344
#        Bytes1 = 0x55667788
        self.apbs_ram(self.addr+12,Bytes0)
        self.apbs_ram(self.addr+16,Bytes1)

    def generateFD(self):
        self.addr = self.fdParams['addr']
        Header0 = 0x20000000
        Header0 += self.fdParams['dlc']
        Header0 += (self.fdParams['idfield'])<<12
        if self.fdParams['extended']:
            Header0 += 0x08000000

        if self.fdParams['brs']:
            Header0 += 0x02000000
        if self.fdParams['esi']:
            Header0 += 0x01000000

        Header1 = self.clParams['extendidfield']
        Header2 = 0
        self.apbs_ram(self.addr,Header0)
        self.apbs_ram(self.addr+4,Header1)
        self.apbs_ram(self.addr+8,Header2)
        for ii in range(16):
            Bytes0 = random.randint(0,0xffffffff)
            self.apbs_ram(self.addr+12+(ii*4),Bytes0)



    def generateXL(self):
        logs.log_info("generateXL %s %s" % (self.apb,self.apbs))
        Header0 = 0x30000000
        Header0 += self.xlParams['dlc']-1
        Header0 += (self.xlParams['idfield'])<<12

        Header2 = self.xlParams['af']
        Header1 = (self.xlParams['vcid']) << 3
        Header1 += (self.xlParams['sec']) << 11
        Header1 += (self.xlParams['sdt']) << 12
        Header1 += (self.xlParams['rrs']) << 20

        self.apbs(self.Addr,Header0)
        self.apbs(self.Addr+4,Header1)
        self.apbs(self.Addr+8,Header2)
        Dlc = self.xlParams['dlc']
        Data = []
        More = Dlc & 0x3
        for II in range(Dlc+1):
            Byte = random.randint(0,255)
            Byte = II+8
            Data.append(Byte)
        if More == 1: Data.extend([0xff,0xff,0xff])
        if More == 2: Data.extend([0xff,0xff])
        if More == 3: Data.extend([0xff])
        Datax = Data[:]
        ii = 0
        Words = []
#        while len(Datax)>=4:
#            Word = Datax[0]+(Datax[1]<<8)+(Datax[2]<<16)+(Datax[3]<<24)
#            Datax = Datax[4:]
#            Word = (self.XLhigh << 16) + self.XLlow
#            self.apbs(self.Addr+12+ii,Word)
#            ii += 4
#            self.XLlow += 0x11
        logs.log_info('GENSEND XL %s %s header0  %s' % (self.Apbs,hex(self.Addr),hex(Header0)),'txx')
        logs.log_info('GENSEND XL %s %s header1 %s' % (self.Apbs,hex(self.Addr+4),hex(Header1)),'txx')
        logs.log_info('GENSEND XL %s %s header2 %s' % (self.Apbs,hex(self.Addr+8),hex(Header2)),'txx')
        
        Dlc1 = Dlc + 1
        More = Dlc1 & 0x3
        Times = Dlc1 // 4
        if More>0 : Times += 1
        for ii in range(Times):
            Word = (self.XLhigh << 16) + self.XLlow
            self.XLlow += 0x11
            self.apbs(self.Addr+12+(4*ii),Word)
            logs.log_info('GENSEND XL %s %s bytes0 %s' % (self.Apbs,hex(self.Addr+12+(4*ii)),hex(Word)),'txx')
            Words.append(Word)
        self.XLhigh += 0x11
        self.addapb(self.eval('%stxfifo' % self.Fifo),self.Addr)

        logs.log_info('GENSEND XL %s  %stxfifo %s' % (self.Apb,self.Fifo,hex(self.Addr)),'txx')
        self.putAside(Header0,Header1,Header2,Words)
        self.Addr += 0x1000

    def putAside(self,Header0,Header1,Header2,Words):
        logs.log_info("putAside: i am a hook, replace me")
        return

    def addapb(self,Fifo,Addr):
        self.Sent += 1
        self.apbQueue.append((Fifo,Addr))
        self.Fpga.write('A%x.w%x.\n' % (Fifo,Addr))
        logs.log_info('A%x. w%x.    // txfifo' % (Fifo,Addr),'uart')


    def apbs(self,Addr,Data):
        logs.log_info("apbs write `h%x `h%x" % (Addr,Data),"seq")
        self.SeqObj.agents[self.Apbs].action('ram %s %s' % (hex(Addr),hex(Data)))
        self.Fpga.write('A%x.w%x.\n' % (Addr+0x10000,Data))
        logs.log_info('A%x. w%x.' % (Addr+0x10000,Data),'uart')
    def apb(self,Addr,Data):
        logs.log_info("apb write `h%x `h%x" % (Addr,Data),"seq")
        self.SeqObj.agents[self.Apb].action('write %s %s' % (hex(Addr),hex(Data)))
        self.Fpga.write('A%x.w%x.\n' % (Addr,Data))
        logs.log_info('A%x. w%x.' % (Addr,Data),'uart')

    def run(self):
        if self.waiting:
            self.waiting -= 1
            return
        if self.apbQueue == []: return

        if '2' in self.Apb:
            Path = 'dut2.canc_fdcl.tx_frames_ptr_fifo_full'
        else:
            Path = 'dut.canc_fdcl.tx_frames_ptr_fifo_full'
        if self.valid(Path): 
            self.waiting = 50
            return
        self.actuallySent += 1
        Fifo,Buffer = self.apbQueue.pop(0)
        logs.log_info("TXPTR %s write %s full=%s addr=%x" % (self.Apb,Path,self.valid(Path),Buffer))
        self.apb(Fifo,Buffer)
        self.waiting = 50

