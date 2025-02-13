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
cycles=0
GIVEUP_TIMEOUT = 100000    # how many cycles to run before retirment. 

OurName = 'none'
Fin = False
def parameter0(Name):
    global OurName,Fout,Fin
    OurName = logs.bin2str(Name)
    logs.log_info("PARAM0 %s" % OurName,OurName)
    Fout = open('%s.outx' % OurName,'w')
    Fin = open('%s.inx' % OurName,'r')
    logs.log_info("OPENED %s fin and fout" % OurName,OurName)





def cannot_find_sig(Sig):
    logs.log_error('cannot find "%s" signal in the design'%Sig)







def check_comms():
    if not Fin:
        logs.log_error("NOT OPENED %s fin and fout" % OurName,OurName)
        return
    rlist, _, _ = select.select([Fin], [], [], 0.01)  # 0.1 is the timeout

    if rlist:
        line = Fin.readline()
        if line:
            wrds = line.split()
            if wrds[0] == 'msg':
                veri.force('tb.msg_%s' % wrds[1],str(wrds[2]))
                logs.log_info("MSG COMMAND %s" % line,OurName)
            elif 'finish' in line:
                logs.log_info('%s: finishing on command'%OurName,OurName)
                Fout.write('finish\n')
                Fout.flush()
                logs.closeLogs()
                veri.finish()
            else:
                logs.log_info("UNREC COMMAND %s" % line,OurName)
                


def negedge():
    check_comms()
    global cycles
    cycles += 1
    veri.force('tb.cycles',str(cycles))
#    print("CYCLES %s %d" % (OurName,cycles))
    if (cycles>GIVEUP_TIMEOUT):
        logs.log_info('%s: finishing on default guard of %d'%(OurName,GIVEUP_TIMEOUT),OurName)
        logs.closeLogs()
        veri.finish()
    rst_n = veri.peek('tb.rst_n')
    if (rst_n!='1'):
        return
    veri.force('tb.okout','1')
    msgout = logs.peek('tb.msgout')
    if (msgout & 0xff)!=0:
       Fout.write('MSG %s 0x%x\n' % (OurName,msgout))
       Fout.flush()
        
        
        
