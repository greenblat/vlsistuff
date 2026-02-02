# Basic veri (Python - Simulator) interface

it starts with:  **import veri**

**veri.peek(Path):**
   Path is something like "tb.dut.dma.state"
   it returns string with length of wire or reg width. the string is made out of 0,1,x,z characters.
   this is the current value of the variable. 
   You are not allowed to write subbus path, like "state[3:0]".  
   veri.peek returns always full string, and You can chop, substring it in python.

**veri.force(Path,Value)**
   Path is same as in veri.peek
   Value is always string.
   it can be one of three:
    "12345"   - decimal string, it can be up to 32bits. no "-" allowed.
    "0xabcd"  -  hex string. width same restrictions.
    "0b01010101010xz" - binary string. unlimited length. can include x and z characters.

    veri.force is not hard force, it is "deposit"
    there is also hard_force in the library. it comes with release function.




**veri.stime()**
    return current simulation time. dont see much need for it.

**veri.finish()**
    finish and exit simulation.
    sys.exit()  may also do the trick, alas without going through verilog simulator finishing stage (depends on simulator).

**veri.listing(Path,Depth,Filename):**
    like veri.listing("tb","1000","deep.list")
    produce file calle "deep.list" with all current values of all variables, from Path to depth of Depth.
    sorry "0" depth is just like one. i will fix it sometimes to indicated indefinet depth.


- less common:

**veri.peek_mem(Path,ind)**
    like in veri.peek("tb.mem","10")
    returns value from two dimensional  array

**veri.force_mem(Path,ind,val)**
    forces value into two dimensional  array

**veri.peek_3d(Path,ind0,ind1)**
    like in veri.peek("tb.mem","10","20")
    returns value from three dimensional  array

**veri.force_3d(Path,ind0,ind1,val)**
    forces value into three dimensional  array

# Sequence agent
Most of the tests use sequence agent to drive the simulation.
It recognizes limited set of predefined commands. Agents connected to sequencer, used to enhance the set.

**import sequenceClass**

Monitors = []

**seq = sequenceClass("tb",Monitors)**

Sequence needs at least two params: Path to work on, and list that will be run on every clock. 

all these lines should be in verilog.py



### Basic sequence commands

"#"  this is comment, anywhere in line. the text after the “#” char is ignored.
//  this is also a comment start.

**force ready 1**
          deposit “1” to be value of top.ready net.
          The value can be hex, like 0x123f  or decimal or expression:

**force ready 3+5*10**


**define IDLE   5**     # associate value “5” with token IDLE.
    once defined, it may be used in expressions:
    force dma.wr_agent.state IDLE-1


**wait IDLE*5**          # dont do anything new for <EXPR> clocks.

**finish**
	finish simulation, print some conclusions and exit.

**include filename**
           includes external file as part of this sequence.

**print some text and vars**
          prints the text onto screen and pymon.log0
**print DMA STATE dma.state**
         tokens that are legal design nets are looked up in the design and their value is printed.
        Otherwise printed as is.

**waitUntil   EXPR**    
         the sequence is stuck until EXPR becomes true.  EXPR can include signals and comparisons.
**waitUntil (dma.bytecount>100)
         expression can’t have spaces. The evaluation is done on first “token”

**waitUntil (aa&&bb)  GUARDIAN**
	guardian is an optional number, that limits the max number of clocks to wait.
	If Guardian expires before condition is met, an error message generated.

**seed EXPR**
            specify random seed. will override given seed in verilog (xrun, xmverilog)  command line.






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
    wait 1000 clocks before moving on
**apb write 0x100 0x234567**

**apb waitNotBusy 10000**

-  giving command to an agent nicknamed "apb"
-   waitNotBusy stops advance of this sequence untill apb finishes it's tasks.
-  Normally command to agent takes a clock, and then sequence moves on. To make sure apb (or any other agent) finished, You need to wait.
-  second parameter (10000 in this case) is guard counter. If wait is not finished until then, it creates an error. By default, there is some large number assumed.

## Agents structure 
Agent python code should define some routines:
 - **__init__**
          see example below
 - **run(self):**
        called on every clock, from toplevel negedge()
 - **action(self,Text):**
        called when sequencer enocounters agent command (first token in command is agent nickname)
 - **busy(self):**
        return True, when agent is not idle.
        busy method is called, when "waitNotBusy" sequence command is encountered. if busy() return True
        sequencer will wait a clock and retry. If Guard is given in the line (third word), it will retry that number and gives up afterwords.
 - **onFinish(self,Txt):**
        enables to do some queries and prints on simulation finish

# typical agent code

`import string 
 import logs 
 import veri`

`class exampleClass(logs.driverClass):`
    `def __init__(self,Path,Monitors):`
        `logs.driverClass.__init__(self,Path,Monitors)`
        `if Monitors: Monitors.append(self)`
        `self.Queue = []`
        `self.Width = {}`

    def run(self):
        if self.Queue == []: return
        if self.waiting>0:
            self.waiting -= 1
            return
        Cmd = self.Queue.pop(0) 
        if Cmd[0] == 'force':
            Sig = Cmd[1]
            if Sig in self.Width:
                Wid = self.Width[Sig]
            else:
                Wid = 1
            Vdd = self.vdd
            Val = bin(Cmd[2])[2:]
            Res = 0
            for Chr in Val:
                Res = Res<<16
                if Chr == '1':
                    Res += self.vdd
            self.force(Sig,hex(Res))
    
    def busy(self):
        return self.Queue != []
    
    def onFinish(self):
        return
    
    def action(self,Txt,Orig=[]):
        wrds = Txt.split()
        if wrds == []: return
        if wrds[0] == 'vdd':
            self.vdd = self.eval(wrds[1])
        elif wrds[0] == 'width':
            self.Widths[wrds[1] = self.eval(wrds[2])
        elif wrds[0] == 'force':
            for Wrd in wrds[1:]:
                if Wrd[0] in '0123456789':
                    self.Queue.append(('force',Net,self.eval(Wrd)))
                else:
                    self.Net = Wrd
        else:
            logs.log_error('exampleClass got %s' % Txt)
`
### have two objectcs sharing code

import uartDriver
ptx = uartDriver.uartDriver('tb',Monitors,Prefix='',Name='pp')
prxd = uartDriver.uartDriver('tb',Monitors,Prefix='p',Name='prxd')
seq = sequenceClass('tb.dma',Monitors,'',[('ptx',ptx),(prxd',prxd))

- same class has two instances, Second one has Prefix='p'.  
It means that line like :     self.force('rxd',1)  will be interpreted as "veri.force('tb.prxd','1').
- 'tb.' prefixed for full path (first parameter of uartDriver class.
- 'p' is prefixed to signal name.  
- works same for force and peek.
- if different path is needed (for some reason) - use  logs.force("full path","string value").

- in sequence:
apb0  write Addr0 Wdata0 
apb1  write Addr1 Wdata1 





## logs.py helper module
logs.py holds bunch of usefull helper routines. It is used in verilog.py and agents code.

### logging
- logs.log_info(Txt)  : print to screen and to log file.
- logs.log_error(Txt)  : print error message (marked with ERROR)  to screen and to log file.
- logs.log_wrong(Txt)  : print wrong message (marked with WRONG)  to screen and to log file.
- logs.log_correct(Txt)  : print correct message (marked with CORRECT)  to screen and to log file.
- logs.log_ensure(Expr,Txt) : evaluate expression, if true issue correct message, else issue "wrong" one.

- logs.log_info(Txt,Logname) :   all log_* also can accept logname, to create aside logfile.

### conversion
   numerous conversions from string to integer, hex, bin and more.

### logs.peek(Path)

logs.peek helper returns integer conversion of peeked signal. logs.force is not usefull.



## verilog.py

The python driven verilog simulation, needs root of python functions. This is the job of file called verilog.py. it should reside in the directory of simulation. (only ./verilog.py is looked for) 





