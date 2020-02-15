

import os,sys,string,random
import veri
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs'%NewName)
import logs
import math
Monitors=[]
cycles=0

RAD = 1024*16
ONE = 0x40000000/45.0



def divide(AA,BB):
    res = []
    for ind,A in enumerate(AA):
        B = BB[ind]
        if B==0:
            res.append('*')
        else:
            res.append(A/B)
    return res

class driverMonitor:
    def __init__(self,Path,Monitors):
        Monitors.append(self)
        self.Path = Path
        self.state='idle'
        self.Angle = 0
        self.Golden = []
        self.Revised = []
        self.vector_mode = False

    def force(self,Sig,Val):
        veri.force('%s.%s'%(self.Path,Sig),str(Val))

    def peek(self,Sig):
        return logs.peek('%s.%s'%(self.Path,Sig))
    def peeksigned(self,Sig):
        return logs.peeksigned('%s.%s'%(self.Path,Sig))

    def valid(self,Sig):
        return self.peek(Sig)==1

    def mergers(self):
        if (self.Golden!=[])and(self.Revised!=[]):
            gpx,gpy,gnx,gny  = self.Golden.pop(0)
            rpx,rpy,rnx,rny  = self.Revised.pop(0)
            divs = divide((gpx,gpy,gnx,gny),(rpx,rpy,rnx,rny))
            logs.log_info3('%d %d %d %d   <> %d %d %d %d            %s '%(gpx,gpy,gnx,gny,rpx,rpy,rnx,rny,divs))

    def run(self):
        if (self.state=='idle'):
            self.state='work0'
            self.force('startpulse',1)
            self.X = int(RAD*cosinus(self.Angle)) & 0xffffffff
            self.Y = int(RAD*sinus(self.Angle)) & 0xffffffff
            self.X = 0x4000
            self.Y = 0x2000
            self.force('Angle',self.Angle)
            if self.vector_mode:
                self.force('yin',self.Y)
                self.force('xin',self.X)
                self.force('anglein',0)
                self.force('vector_mode',1)
            else:
                self.force('yin',0)
                self.force('xin',39798)
                self.force('anglein',int(ONE*25))
                self.force('vector_mode',0)



        elif (self.state=='work0'):
            self.state='work0_1'
            self.force('startpulse',0)
            self.monitor()
        elif (self.state=='work0_1'):
            self.state='work0_2'
            self.monitor()
        elif (self.state=='work0_2'):
            self.state='work1'
            self.monitor()
        elif (self.state=='work1'):
            donepulse = self.peek('donepulse')
            self.monitor()
            self.monitorOrig()
            self.mergers()
            if donepulse:
                o_real_part = self.peek('xout')
                o_imag_part = self.peek('yout')
                o_angle = self.peeksigned('angleout')
                if (o_angle<0): o_angle = -o_angle
                try:
                    Ratio = (o_angle/self.Angle)
                except:
                    Ratio = 'nonw'
                One = 0x10000000/45.0
                angabs = abs(o_angle)
                Deg = angabs/One

                logs.log_info('REVISED expng=%d sync=%s real=%x imag=%x angle=%d (0x%x) (deg=%d)  exp=%d  x=%x y=%x ratio=%s'%(self.Angle,donepulse,o_real_part,o_imag_part,o_angle,o_angle,Deg,self.Angle,self.X,self.Y,Ratio))
                self.Angle += 1
                self.state='wait'
        elif (self.state=='wait'):
            veri.finish()
            sys.exit()
            self.state='idle'
            self.Revised = []
            self.Golden  = []

    def monitor(self):
        count = self.peek('dut.shiftcount')
#        if count==0: return
        ccw = self.peek('dut.rotate_ccw')
        prevx = self.peeksigned('dut.prevx')
        prevy = self.peeksigned('dut.prevy')
        nextx = self.peeksigned('dut.nextx')
        nexty = self.peeksigned('dut.nexty')
        angleaccum = self.peeksigned('dut.angleaccum')
        nextangle = self.peeksigned('dut.nextangle')
        diffangle = self.peeksigned('dut.diffangle')
        xtanphi = self.peeksigned('dut.xtanphi')
        ytanphi = self.peeksigned('dut.ytanphi')

        Vec = int(math.sqrt(prevx*prevx+prevy*prevy))

        logs.log_info2('REVISED %d count=%d tanphi = %d / %d  next = %d / %d   prev = %d / %d   ccw=%d nextangle=%d diffangle=%d angleaccum=%d  %f'%(Vec,count,xtanphi,ytanphi,nextx,nexty,prevx,prevy,ccw,nextangle,diffangle,angleaccum,1.0*angleaccum/ONE))
        self.Revised.append((prevx,prevy,nextx,nexty))


    def monitorOrig(self):
        if self.peek('golden.donepulse')==1: 
            angleout = self.peeksigned('golden.angleout')
            xout = self.peeksigned('golden.xout')
            yout = self.peeksigned('golden.yout')
            try:
                Ratio = (-angleout/self.Angle)
            except:
                Ratio = 0
            logs.log_info('GOLDEN ratio=%d angle=%d xout=%d (0x%x)  yout=%d  (0x%x) xin=%d yin=%d'%(Ratio,angleout,xout,xout,yout,yout,self.peek('xin'),self.peek('yin')))

        if self.peek('golden.working')==1: 
            nextx = self.peeksigned('golden.nextx')
            nexty = self.peeksigned('golden.nexty')
            prevx = self.peeksigned('golden.prevx')
            prevy = self.peeksigned('golden.prevy')
            nextangle = self.peeksigned('golden.nextangle')
            angleaccum = self.peeksigned('golden.angleaccum')
            shiftcount = self.peek('golden.shiftcount')
            logs.log_info('GOLDEN work count=%d prevx=%d prevy=%d nextx=%d nexty=%d   angles %d %d'%(shiftcount,prevx,prevy,nextx,nexty,nextangle/181,angleaccum/181))
            self.Golden.append((prevx,prevy,nextx,nexty))


import math
def sinus(Degrees):
    Rads = (Degrees * 2 * math.pi)/360.0
    return math.sin(Rads)
def cosinus(Degrees):
    Rads = (Degrees * 2 * math.pi)/360.0
    return math.cos(Rads)





driverMonitor('tb',Monitors)



def negedge():
    global cycles
    cycles += 1
    veri.force('tb.cycles',str(cycles))
    if (cycles>2000):
        veri.finish()
    rst_n = veri.peek('tb.rst_n')
    if (rst_n!='1'):
        return

    if (cycles==30):
        veri.listing('tb','100','deep.list')
    if (cycles>30):
        for Mon in Monitors: Mon.run()

def cucu():
    veri.force('tb.anglein','0')
    veri.force('tb.nreset','0')
    veri.force('tb.startpulse','0')
    veri.force('tb.vector_mode','1')
    veri.force('tb.xin','0')
    veri.force('tb.yin','0')
    angleout = logs.peek('tb.angleout')
    donepulse = logs.peek('tb.donepulse')
    xout = logs.peek('tb.xout')
    yout = logs.peek('tb.yout')
