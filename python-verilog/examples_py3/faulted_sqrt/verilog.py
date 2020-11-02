

import os,sys,string,random,math
import veri
sys.path.append('/Users/ilia/verification_libs3')
import logs
Monitors = []

#   Fname =  os.getenv('STUCK_FILE')
#   if Fname=='': 
#       Fname = 'STUCKS.shuffled'
#   
#   
#   if (not Fname) or not os.path.exists(Fname):
#       logs.log_error('STUCK base file "%s" doesnt exist, setenv STUCK_FILE should work'%Fname)
#       sys.exit()
#   File = open(Fname)
#   Lines = File.readlines()
#   File.close()
#   
#   random.shuffle(Lines)
#   random.shuffle(Lines)
#   random.shuffle(Lines)
#   
#   Fout = open('shuffled.faultd','w')
#   for Line in Lines:
#       Fout.write(Line)
#   Fout.close()
#   
#   
#   sys.exit()



import faultsimulator 
faults = faultsimulator.faultsimulatorClass('tb',Monitors) 



Pause = 50
def rerunTest():
    global cycles,idle,Ain,state,Max,Pause
    veri.force('tb.rst_n','0')
    state = 'reset'
    Pause = 50

faults.rerunTest = rerunTest    
    


cycles=0
state='idle'
def negedge():
    global cycles,idle,Ain,state,Max,Pause
    cycles += 1
    veri.force('tb.cycles',str(cycles))
    if (cycles>1000000):
        veri.listing('tb','1000','cucu.list')
        veri.finish()
        return
    veri.force('tb.en','1')

    rst_n = veri.peek('tb.rst_n')
    if (rst_n!='1')and (cycles<100):
        ain = veri.peek('tb.ain')
        Len = len(ain)
        Max = 1<<Len
        veri.force('tb.makeStuckList','1')
        return

    if (cycles>30):
        for Mon in Monitors:
            Mon.run()

    if state=='reset':
        Pause -= 1
        if Pause==0:
            state = 'idle'
            veri.force('tb.rst_n','1')
    elif state=='idle':
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
            state='idle'
            return
            Out = logs.peek('tb.out')
            Exp = int(math.sqrt(Ain))
            if Out==Exp:
                logs.log_correct('in=%d out=%d'%(Ain,Out))
            else:
                logs.log_wrong('ain=%d max=%d expected=%d act=%d'%(Ain,Max,int(math.sqrt(Ain)),Out))
            state='idle'

    


def discovered():
    vldout = veri.peek('tb.vldout')
    fault_cought = veri.peek('tb.fault_cought')
    flt_vldout = veri.peek('tb.flt_vldout')
    Disc =  (fault_cought == '1')and((vldout=='1')or(flt_vldout == '1'))
    return Disc


faults.discovered = discovered



