#! /usr/bin/env python3
import subprocess
import time
import shutil
import os, sys, select

Fout = False
simv_command = "vvp  -M/Users/iliagreenblat/vlsistuff/python-verilog/vpi3 -mvpi3_local  tb.vvp +PRM0=XXX"

PROC = 0
def simv_runner(proc_id, queue, response_queue):
    global Fin,PROC
    PROC = proc_id
    simv_com = simv_command.replace('XXX',str(proc_id))
    Fin = open('%s.inx' % proc_id,'w')
    print("SIMVCMD %s %s" % (proc_id,simv_com))
    process = subprocess.Popen(
        simv_com,  
        shell=True, 
#        stdin=subprocess.PIPE,
#        stdout=subprocess.PIPE,
#        stderr=subprocess.PIPE,
        text=True,
        env=os.environ  
    )

    # Non-blocking reading of stdout and stderr using select.select()
    Ok = True
    while Ok:
        # Check if there is data available on stdin and the queues
        if not queue.empty():
            command = queue.get()
            print(PROC,' received ',command)
            if 'quit' in command: Ok = False
            if 'exit' in command: Ok = False
            if 'finish' in command: Ok = False
            Fin.write(f"{command}\n")
            Fin.flush()

        # Check for any available output from stdout or stderr
        read_output(response_queue)

        # Sleep to prevent high CPU usage
        time.sleep(0.1)
        read_output(response_queue)

    # Terminate the process once done
    print("Terminating the simv process.")
    process.terminate()


def read_output(response_queue):
    global Fout
    if not os.path.exists('%s.outx' % PROC): return

    if not Fout: Fout = open('%s.outx' % PROC, 'r')
    rlist, _, _ = select.select([Fout], [], [], 0.01)  # 0.1 sec timeout
    if Fout in rlist:
        output = Fout.readline()
        if output:
            response_queue.put(output)
            print(PROC,'return',output)
