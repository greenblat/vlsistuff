#! /usr/bin/env python3
import multiprocessing
import time
from simv_runner import simv_runner
import random


import os,sys
NewName = os.path.expanduser('~')
if os.path.exists('%s/vlsistuff' % NewName):
    sys.path.append('%s/vlsistuff/verification_libs3'%NewName)
elif 'VLSISTUFF' in os.environ:
    sys.path.append('%s/verification_libs3'%os.environ['VLSISTUFF'])
else:
    print("please set VLSISTUFF to where You cloned vlsistuff repository. like:  /home/cucu/softs/vlsistuff")
    sys.exit()

import logs

RUNNERS = 10

def main():
    queue = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    response_queue = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    proc = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for II in range(RUNNERS):
        queue[II] = multiprocessing.Queue()
        response_queue[II] = multiprocessing.Queue()
        proc[II] = multiprocessing.Process(target=simv_runner, args=(II+10, queue[II], response_queue[II]))
        proc[II].start()

    time.sleep(1)  # Give the process time to start

    generateIngress(queue)
    playingNoc(queue,response_queue)
        
    time.sleep(5)
    for II in range(RUNNERS):
        queue[II].put('finish')


    logs.log_info("JOINING");
    for II in range(RUNNERS):
        proc[II].join()
        logs.log_info("JOIN %d" % II);
    logs.log_info("MAIN EXIT")


# MSG 10 0x500000000000000080f38fe3ae9bf67081
def playingNoc(queue,response_queue):
    Ok = True
    while Ok:
        for II in range(RUNNERS):
            if not response_queue[II].empty():
                Txt = response_queue[II].get() 
                wrds = Txt.split()
                if II == (RUNNERS-1):
                    logs.log_info("EGRESS %s %s" % (II,Txt))
                    if 'finish' in Txt: return
                elif 'finish' in Txt:
                    queue[II+1].put("finish") 
                    logs.log_info("PASS FINISH %s" % (II))
                elif wrds[0] == 'MSG':
                    Src = int(wrds[1])-1
                    Msg = eval(wrds[2])
                    Num = Msg & 0x7f
                    AA = (Msg>>8) & 0xffffffffffffffff
                    R0 =  random.randint(0,0xffffffff)
                    R1 =  random.randint(0,0xffffffff)
    
                    Str = '%08x%08x%016x%02x' % (R0,R1,AA,Num)
                    logs.log_info("PASS NEXT %d %s  << %s " % (II,Str,Txt))
                    queue[II+1].put("msg msgin 0x%s" % Str) 
                else:
                    logs.log_error("UNKNOWN line %d %s" % (II,Txt))


def generateIngress(queue):
    for ii in range(10):
        R0 =  random.randint(0,0xffffffff)
        R1 =  random.randint(0,0xffffffff)
        R2 =  random.randint(0,0xffffffff)
        R3 =  random.randint(0,0xffffffff)
        Str = '%08x%08x%08x%08x%02x' % (R0,R1,R2,R3,ii& 0xff)
        queue[0].put("msg msgin 0x%s" % Str) 
    queue[0].put("finish")

if __name__ == "__main__":
    main()
