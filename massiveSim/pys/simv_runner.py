#! /usr/bin/env python3
import subprocess
import time
import shutil
import os, sys, select


NewName = os.path.expanduser('~')
vpi_name = 'vpi3_72'
if os.path.exists('%s/vlsistuff' % NewName):
    sys.path.append('%s/vlsistuff/verification_libs3'%NewName)
elif 'VLSISTUFF' in os.environ:
    sys.path.append('%s/verification_libs3'%os.environ['VLSISTUFF'])
else:
    print("please set VLSISTUFF to where You cloned vlsistuff repository. like:  /home/cucu/softs/vlsistuff")
    sys.exit()





Fout = False
simv_command = "vvp  -MHOME/vlsistuff/python-verilog/vpi3 -mVPI_NAME  tb.vvp +PRM0=XXX"
simv_command = simv_command.replace('HOME',NewName)
simv_command = simv_command.replace('VPI_NAME',vpi_name)

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
    should_finish = False
    while Ok:
        # Check if there is data available on stdin and the queues
        if not queue.empty():
            command = queue.get(block=True)
            print(PROC,' received ',command)
            if 'quit' in command: Ok = False
            if 'exit' in command: Ok = False
            if 'finish' in command:
                Ok = False

            Fin.write(f"{command}\n")
            Fin.flush()

        # Check for any available output from stdout or stderr
        read_output(response_queue)

        # Sleep to prevent high CPU usage
        time.sleep(1.3)
        read_output(response_queue)


    # Check for any available output from stdout or stderr
    read_output(response_queue)

    # Sleep to prevent high CPU usage
    time.sleep(1.3)
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
