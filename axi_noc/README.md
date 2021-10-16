
NOC made out of 4-to-1 axi merger and 1-to-4 axi splitter.
plan to use .dot language to specify.

additional lego pieces:
1. clock changerr (in private repository)
2. width changer (in private repository)
3. nice to have: serdes


18.Sep.2021
Idea: addressing run by two MSB bits to select the branch to go.
On Each splitter, it will use two MSB address bits. Downstrea, it will shift the address left by two.

Branching factor is four. 

Idea2: 
   Upstream comms through read data channel, with special RID (like==0).
   Slave will send interrupts and errors this way.
   Addressing will be done by two MSBit of RDATA. and RDATA shifted left by two (only upper 32 bits).

Idea3:
    replace all stupid fields (prot,cache, size) with one configurable field "extras".


21.sep.2021
tb0 is testbench for merger
tb1 is testbench for splitter
tb2 is testbench for full network
tb3 same as tb2 but with ram
tb_ram testbench for ram
tb_apb testbench for apb
docs is the document.

