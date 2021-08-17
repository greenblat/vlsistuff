
# Agents in Sequence

sequenceClass.py has set of commands it recognizes in sequence file.
it also can deliver commands to agents - agent like apbDriver or axiMaster or axiSlave.
commands that can configure or cause action in agents.

## in verilog.py

**apb = apbDriverClass("tb",Monitors)**
this line in verilog.py will  constructs apb agent.

**seq = sequenceClass("tb",Monitors,'MyName',[ ('apb',apb), ('axim',axim),('spi',spi)])**
#adding agents (apb,axi and spi ) as example
the pair is ('nickname',agent)

## reference in the sequence test  file:

**wait 1000**
**apb write 0x100 0x234567**

**apb waitNotBusy 10000**

-  giving command to an agent nicknamed "apb"
-   waitNotBusy stops advance of this sequence untill apb finished it's tasks.
-  Normally command to agent takes a clock, and then sequence moves on. To make sure apb (or any other agent) finished, You need to wait.

## add in agents

def action(self,Txt):
    wrds = Txt.split()
    if wrds[0] == 'disable'
        self.Enable = False

action method is called from sequence when the first token of sequence line has the agent's nickname. You are free to add as many if / elif with command keywords as You deem necessary.  s

def busy(self):
    if self.Queue!=[]: return True
    if self.waiting>=0: return True
    return False
busy method is called, when "waitNotBusy" sequence command is encountered. if busy() return True
sequencer will wait a clock and retry. If Guard is given in the line (third word), it will retry that number and gives up afterwords.



