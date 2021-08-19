



# sequenceClass usage and opcodes

sequenceClass.py implements sequence of commands to drive various tests.
It accepts file (usually extension .seq) to drive the simulation.

## invocation:
```
import sequenceClass
AGENTS = [('nickname',classInst),('ahb',ahb),('jtag',jtag)]
seq = sequenceClass.sequenceClass('tb',Monitors,'seq',AGENTS)

```


- // this is a comment start for this line.

- **define IDLE 5 **  
   associate value “5” with token IDLE. once defined, it may be used in expressions:
   force dma.wr_agent.state IDLE-1

    Define line accepts functions:  rnd(High) rnd(High,Low) producing random number in range.
    or envir("ENVIRON") : accepts setenv (or export for bash) variable name.
    also math expressions:    (A+B) with no spaces. Where A,B can be numbers of previously defined.

- **force ready 1**
    deposit “1” to be value of top.ready net.
    The value can be hex, like 0x123f or decimal or expression:
    force ready 3+5*10
- **wait IDLE*5**
    dont do anything new for <EXPR> clocks. each sequence is "hung" on Monitor list.
- **finish**
    finish simulation and exit
- **include filename**
      includes external file as part of this sequence.
- **print some text and vars**
    prints the text onto screen and pymon.log0
    print DMA STATE dma.state
    tokens that are legal design nets are looked up in the design and their value is printed. Otherwise printed as is.
- **waitUntil EXPR**
    the sequence is stuck until EXPR becomes true. EXPR can include signals:
    waitUntil (dma.bytecount>100)
    expression can’t have spaces. The evaluation is done on first “token”
- **waitUntil (aa&&bb) GUARDIAN**
    guardian is an optional number, that limits the max number of clocks to wait. If Guardian expires before condition is met, an error message generated.
## AGENTS
to drive or monitor interfaces we connect objects of classes that play these interfaces.
to address an agent, first token in line is the nickname of the agent. All following tokens are sent to the agent “action()” function for execution.

 Agent is class, that must have 
    def run(self)
    def activate(self,Txt)
    def busy(self)
    def onFinish(self):



##  procedural sequence

Some conditional additions to basic sequence commands.

###  label Label

​    defines label location.

###  goto Label

​    pass sequence control to specified label

###  if

**if Expr Label**
conditionally pass control to label, otherwise goto next line
example of simple loop:
`define CNT 5 label START`
`force ........`
`wait ......`
`define CNT CNT-1 if (CNT>0) START`
this loop will be executed 5 times , and then the sequence will move on.

## Threads

several sequences can be run concurrently.
to define a sub-sequence:
`sequence SEQ0 ....`
`.... .... ....`
`end`
the lines in between can be activated by main sequence using
**fork SEQ0**
or
**spawn SEQ0**
the sub-sequence will run in parallel until it ends
**call SEQ9**  
this will behave like subroutine
**return**
to exit subroutine
