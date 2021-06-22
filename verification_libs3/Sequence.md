
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


spi i2c psi frame leaf diag
finish simulation, print some conclusions and exit.
 
 ilia greenblat 054-4927322
SPI:
spi send 0xc0 0x0c 0x0 0x3 sends four bytes through SPI. any number of bytes is ok by this command but may not make sense for triEye SPI. ChipSelect is activated (low) before starting clocking and shifting the data. It is de-activated after last bit clocked.
Additional options will be added as needed.
I2C: user construction
PSI
This interface is generic driver of images. It accepts list of rows (which are lists f pixels) and drives them into PSI_IN.
psi pixelwidth=8 pixelsperclock=3
defines the setup of driving
psi run
drives a frame in (another agent loads in the frame to be driven)
psi waitNotBusy
stops sequence until psi finished driving.
FRAME
This agent configures, generates and passes it to PSI for execution.
frame diagnostic width=140 rows=3
defines the setup of diagnostic rows.
frame dark rows=rnd(8,32) width=WID pixels=noise(10,100)
defines dark rows and their optionally random values.
frame safe rows=5 width=WID pixels=SAFE+(SAFE*8)+(SAFE*16)
defines safe rows
frame visual rows=ROWS width=WID darks=rnd(0,24) source=noise(10,2040)
defines visual rows
frame activate
configures the frame and sends it to PSI. this takes no time. Whole frame is sent to PSI in one clock.
LEAF
This agent configures the LEAF behaviour. It is under construction. The idea is to generate the tables and drive them into LEAF( axi?)
leaf badpix total=rnd(20,100) clusters=3
configuration of bad pixels.
leaf psiout histogram # other options
configuration of PSIOUT
leaf coeffs pairing=random a=rnd(5,10) b=rnd(3,8) sat=rnd(1500,1800)
configuration of DARK and VISUAL pixels pairing and records.
DIAG
is Class that keeps and creates Diagnostic rows. It keeps the reg values, inserts them into correct places in Diagnostic rows and passes it to FRAME, when appropriate.
Here is list of all current fields//regs with representative values:
diag reg bpp=2
diag reg ss=0         # 0..1
diag reg pwseqlen=rnd(0,7)
diag reg pdseqlen=rnd(0,7)
diag reg eseqlen=rnd(0,7)
diag reg dcr=rnd(0,1)
diag reg rb=rnd(0,1)

 ilia greenblat
diag reg cb=rnd(0,1)
054-4927322
diag reg fvr=300
diag reg lvr=600
diag reg fcolumn=10
diag reg lcolumn=30
diag reg sdiagn=2
diag reg ediagn=0   #  0
diag reg srnr=0   #  0..3
diag reg sfndr=4   #  0..0x20
diag reg sffdr=5   #  0..0x20
diag reg efndr=6   #  0..0x21
diag reg effdr=7   #  0..0x21
diag reg sfnsr=0x5   #  0..0x9
diag reg sffsr=0x20   #  0x20..0x28
diag reg efnsr=0x24   #  0x20..0x28
diag reg effsr=0x5   #  0..0x9
expression examples
2*CUCU-3 (dma.bytecount<100) 3+rnd(3,6) noise(Low,High)
: math operatiors on numbers and defined constants (define line) : relational operands are ok two.
: rnd(Low,High) returns random integer between Hi and Low (included) : like rnd(), but evaluated during generation of rows many times.
# 0..12xx
# 0..12xx
   # 0,960
   # 0,960
# 1,2,3
if we write : pixels=rnd(4,5) all pixels will be generated identical and with value 4 or 5. pixels=noise(4,5) pixels randomly will get values either 4 or 5.
procedural sequence
Some conditional additions to basic sequence commands.
label Label
define label location.
goto Label
pass sequence control to specified label
if Expr Label
conditionally pass control to label, otherwise goto next line
example of simple loop:
define CNT 5 label START
force ........
wait ......
define CNT CNT-1 if (CNT>0) START
this loop will be executed 5 times , and then the sequence will move on.

ilia greenblat 054-4927322 Threads
several sequences can be run concurrently.
to define a sub-sequence:
sequence SEQ0 ....
.... .... ....
end
the lines in between can be activated by main sequence using
fork SEQ0
or
spawn SEQ0
the sub-sequence will run in parallel until it ends

