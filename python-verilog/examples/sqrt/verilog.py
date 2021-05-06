

import os,sys,string,random,math
import veri
sys.path.append('/Users/ilia/verification_libs3')
import logs

cycles=0
state='idle'
def negedge():
    global cycles,idle,Ain,state,Max
    cycles += 1
    veri.force('tb.cycles',str(cycles))
    if (cycles>1000):
        veri.listing('tb','1000','cucu.list')
        veri.finish()
        return
    veri.force('tb.en','1')

    rst_n = veri.peek('tb.rst_n')
    if (rst_n!='1'):
        ain = veri.peek('tb.ain')
        Len = len(ain)
        Max = 1<<Len
        return


    if state=='idle':
        Ain = random.randint(0,Max)
        veri.force('tb.ain',logs.make_str(Ain))
        veri.force('tb.vldin','1')
        state='work0'
    elif state=='work0':
        veri.force('tb.vldin','0')
        state='wait0'
    elif state=='wait0':
        vldout = logs.peek('tb.vldout')
        if vldout==1:
            Out = logs.peek('tb.out')
            Exp = int(math.sqrt(Ain))
            if Out==Exp:
                logs.log_correct('in=%d out=%d'%(Ain,Out))
            else:
                logs.log_wrong('ain=%d max=%d expected=%d act=%d'%(Ain,Max,int(math.sqrt(Ain)),Out))
            state='idle'


