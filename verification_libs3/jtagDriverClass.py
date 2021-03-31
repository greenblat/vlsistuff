#! /usr/bin/python

import logs
import veri

# jtag = jtagDriverClass.jtagDriverClass('tb',Monitors,'JTCK','JTDI','JTMS','JTDO')

class jtagDriverClass(logs.driverClass):
    def __init__(self,Path,Monitors,JTCK='jtck',JTDI='jtdi',JTMS='jtms',JTDO='jtdo'):
        logs.driverClass.__init__(self,Path,Monitors)
        self.queue=[]
        self.commands=[]
        self.jtck = JTCK
        self.jtdi = JTDI
        self.jtdo = JTDO
        self.jtms = JTMS
        self.responce=''
        self.callback=False
        self.Fout=False
        self.lastIr = (0x20,8)

    def busy(self):
        if self.queue!=[]: return True
        if self.commands!=[]: return True
        return False


    def action(self,Txt):
        wrds = Txt.split()
        if wrds[0] == 'ir':
            Len = eval(wrds[1])
            Ir = eval(wrds[2])
            self.sendIr(Ir,Len)

        elif wrds[0] == 'ir1':
            Len = eval(wrds[1])
            Ir = eval(wrds[2])
            self.sendIr1(Ir,Len)

        elif wrds[0] == 'dr':
            Len = eval(wrds[1])
            Dr = eval(wrds[2])
            self.sendDr(Dr,Len)

        elif wrds[0] == 'dr1':
            Len = eval(wrds[1])
            Dr = eval(wrds[2])
            self.sendDr1(Dr,Len)

        elif wrds[0] == 'dr1check':
            Len = eval(wrds[1])
            Dr = eval(wrds[2])
            self.sendDr1Check(Dr,Len)
        elif wrds[0] == 'idle':
            Len = eval(wrds[1])
            Tms = eval(wrds[2])
            self.sendIdle(Len,Tms)
        else:
            logs.log_error('action text %s is not recognized'%(Txt))

    def run(self):
        if self.state=='idle':
            if self.queue!=[]:
                self.Tms,self.Tdi,self.Catch = self.queue.pop(0)
                if self.Tms=='force':
                    veri.force(self.Tdi,str(self.Catch))
                    return
                if self.Tms=='label':
                    self.Catch.write('%s\n'%self.Tdi)
                    return
                if self.Tms=='finish':
                    logs.log_info('finishing from jtag sequence')
#                    self.Catch.write(self.Tdi)
                    veri.finish()
                    return
                self.force(self.jtck,0)
                self.force(self.jtms,self.Tms)
                self.force(self.jtdi,self.Tdi)
                self.state='step0'
            else:
                self.force(self.jtck,0)
                self.force(self.jtms,0)
                self.force(self.jtdi,0)
            return 
        elif self.state=='step0':
            self.force(self.jtck,1)
            self.state='step1'
        elif self.state=='step1':
            self.force(self.jtck,0)
            if self.Catch==1:
                self.responce = str(self.peek(self.jtdo))+self.responce
            elif self.Catch=='x':
                self.responce = 'X'+self.responce
            elif self.responce!='':
                (Cmd,Val,Len) = self.commands.pop(0)
                RR = logs.intx(self.responce)
                try:
                    logs.log_info('jtag RES 0x%x %s %x %s %x %s lastir=(%x)'%(RR,self.responce,logs.intx(self.responce),Cmd,Val,Len[0],Len[1]))
                except:
                    logs.log_info('jtag RES 0x%x %s %s %s (x) %s lastir=(%s)'%(RR,self.responce,Cmd,Val,Len,Len))
                if self.callback:
                    self.callback(logs.intx(self.responce),Cmd,Val,Len)
                self.responce=''
            else:
                self.responce=''
               
            self.state='idle'
    def sendLabel(self,Text,Fout):
        self.queue.append(('label',Text,Fout))
            
    def sendFinish(self,Txt,Fout=False):
        self.queue.append(('finish',Txt,Fout))

    def force1(self,Whome,What):
        self.queue.append(('force',Whome,str(What)))


    def sendIdle(self,Many,Tms=0):
        for ii in range(Many):
            self.queue.append((Tms,0,0))

    def sendIr1(self,Ir,irLen=8):
        self.queue.extend([(0,0,0),(1,0,0),(1,0,0),(0,0,0),(0,0,0)])
        irString = make_bin_i(Ir,irLen)
        for Bit in irString[:-1]:
            self.queue.append((0,int(Bit),0))
        self.queue.append((1,int(irString[-1]),0))
        self.queue.extend([(1,0,0)])
        self.queue.extend([(0,0,0)])
        self.commands.append(('ir',Ir,(irLen,0x20)))
        self.lastIr = (Ir,irLen)

    def sendIr(self,Ir,irLen=8):
        self.queue.extend([(0,0,0),(1,0,0),(1,0,0),(0,0,0),(0,0,0)])
        irString = make_bin_i(Ir,irLen)
        logs.log_info('irString %s'%(irString))
        for Bit in irString[:-1]:
            self.queue.append((0,int(Bit),1))
        self.queue.append((1,int(irString[-1]),1))
        self.queue.extend([(1,0,0)])
        self.queue.extend([(0,0,0)])
        self.commands.append(('ir',Ir,irLen))
        self.lastIr = (Ir,irLen)

    def sendDr1(self,Dr,drLen=32,Label=''):
        self.queue.extend([(0,0,0),(1,0,0),(0,0,0),(0,0,0)])
        drString = make_bin_i(Dr,drLen)
        Ind=0
        for Bit in drString[:-1]:
            if Label:
                self.queue.append(('label','%s_%d:'%(Label,Ind),self.Fout))
                Ind += 1
            self.queue.append((0,int(Bit),0))
        if Label:
            self.queue.append(('label','%s_%d:'%(Label,Ind),self.Fout))
        self.queue.append((1,int(drString[-1]),0))
        self.queue.extend([(1,0,0)])
        self.queue.extend([(0,0,0)])
        self.commands.append(('dr',Dr,(drLen,self.lastIr[0])))

    def sendDr1Check(self,Dr,drLen=32,Label=''):
        self.queue.extend([(0,0,0),(1,0,0),(0,0,0),(0,0,0)])
        drString = make_bin_i(Dr,drLen)
        Ind=0
        for Bit in drString[:-1]:
            if Label:
                self.queue.append(('label','%s_%d:'%(Label,Ind),self.Fout))
                Ind += 1
            self.queue.append((0,int(Bit),1))
        if Label:
            self.queue.append(('label','%s_%d:'%(Label,Ind),self.Fout))
        self.queue.append((1,int(drString[-1]),1))
        self.queue.extend([(1,0,0)])
        self.queue.extend([(0,0,0)])
        self.commands.append(('dr',Dr,(drLen,self.lastIr[0])))

    def sendDr(self,Dr,drLen=32):
        self.queue.extend([(0,0,0),(1,0,0),(0,0,0),(0,0,0)])
        drString = make_bin_i(Dr,drLen)
        for Bit in drString[:-1]:
            self.queue.append((0,int(Bit),1))
        self.queue.append((1,int(drString[-1]),1))
        self.queue.extend([(1,0,0),(0,0,0)])
        self.commands.append(('dr',Dr,drLen))




def make_bin_i(Data,Len):
    X = list(make_bin(Data,Len))
    X.reverse()
    return ''.join(X)


def make_bin(Data,Len):
    if (type(Data) is str):
        if len(Data)==Len:
            return Data
        
    X = bin(Data)[2:]
    Y = '0'*Len+X
    Z = Y[-Len:]
    return Z





# self testbench: activation: no parameters., just this as a script: python pybin/jtagClass.py

def main():
    Fout = open('jtag.log','w')
    jtag = jtagClass()
    jtag.sendIdle(100,0)
    jtag.sendIdle(100,1)
    jtag.sendIr(0x1234,17)
    jtag.sendIdle(100,1)
    jtag.sendDr(0x555666777,77)
    jtag.sendIdle(100,1)
    for A,B in jtag.queue:
        Fout.write('%s %s\n'%(A,B))

     

if (__name__ == '__main__'):
    main()



