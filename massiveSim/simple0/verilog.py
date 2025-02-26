


import os,sys, select
import veri



NewName = os.path.expanduser('~')
if os.path.exists('%s/vlsistuff' % NewName):
    sys.path.append('%s/vlsistuff/verification_libs3'%NewName)
elif 'VLSISTUFF' in os.environ:
    sys.path.append('%s/verification_libs3'%os.environ['VLSISTUFF'])
else:
    print("please set VLSISTUFF to where You cloned vlsistuff repository. like:  /home/cucu/softs/vlsistuff")
    sys.exit()

import logs
Monitors=[]

OurName = False
Listen = False
def parameter0(Name):
    global OurName,Fout
    OurName = logs.bin2str(Name)
    Fout = open('%s' % OurName,'w')

def parameter1(Name):
    global Listen
    Listen = logs.bin2str(Name)
cycles = 0
def negedge():
    global cycles
    cycles += 1
    if veri.peek('tb.rst_n') == '0': return
    check_comms()
    do_finish()
    

def msgout(msgout):
    Id = hex(logs.intx(msgout[128:]))
    AA = hex(logs.intx(msgout[:64]))
    BB = hex(logs.intx(msgout[64:128]))
    Fout.write('JOB %s %s %s\n' % (Id,AA,BB))
    Fout.flush()

Fin = False
Finishing = False
def check_comms():
    global Fin,Finishing
    if not Fin:
        if os.path.exists(Listen):
            Fin = open(Listen,'r')
        else:
            return
    rlist, _, _ = select.select([Fin], [], [], 0.01)  # 0.1 is the timeout

    if rlist:
        line = Fin.readline()
        if not line:
            veri.force('tb.msgin','0')
        if line:
            wrds = line.split()
            if (wrds==[]):
                pass
            elif (wrds[0] != 'JOB'):
                veri.force('tb.msgin','0')
            if (wrds==[]):
                pass
            elif wrds[0] == 'JOB':
                Id = eval(wrds[1])
                AA = eval(wrds[2])
                BB = eval(wrds[3])
                Msg = Id + (AA<<32) + (BB<<96)
                veri.force('tb.msgin',hex(Msg))
            elif wrds[0] == 'CFG':
                logs.log_info('CFG %s %s' % (OurName,wrds[1:]))

                if 'finish' in wrds[1:]:
                    Finishing = True
                else:
                    logs.log_info("UNREC COMMAND %s" % line,OurName)

waiting = 1000
def do_finish():
    global waiting
#    print(cycles,Finishing,veri.peek('tb.busy') )
    if (not Finishing): return;
    Busy = veri.peek('tb.busy')
    if '1' in Busy: return
    if (waiting == 999):
        Fout.write('CFG finish\n')
        Fout.close()
    waiting -= 1
    if waiting>0: return
    logs.log_info('%s: finishing on command'%OurName,OurName)
    logs.closeLogs()
    veri.finish()
    sys.exit()





