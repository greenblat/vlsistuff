#! /usr/bin/env python3

import os,sys,string

HELPSTRING = '''
invocation:     buildFifo.py  <Writes> <Reads>
this script builds RTL of a multi_sync_fifo with optional number of concurrent writes.
and Depth being number of fifo entries.
<Writes> is the number of concurrent writes
<Reads> is the number of concurrent reads

'''


def main():
    try:
        Writes = int(sys.argv[1])
        Reads = int(sys.argv[2])
    except:
        print(HELPSTRING)
        return

    buildFifo(Writes,Reads)

def buildFifo(Writes,Reads):
    Fname = 'multififo_w%d_r%d.v'%(Writes,Reads)
    Fout = open(Fname,'w')
    Str = STRING0
    Str = Str.replace('WRITES',str(Writes))
    Str = Str.replace('READS',str(Reads))
    Str = Str.replace('WWID',str(bitsFor(Writes)-1))
    Str = Str.replace('RWID',str(bitsFor(Reads)-1))
    TXT=''
    Wrts = []
    TEXTWRITE2 = '        if (oktowrite && (writes >= 1))  fifos[wptr] <= din[WIDTH-1:0];\n'
    for II in range(2,Writes+1):
        TEXTWRITE2 += '        if (oktowrite && (writes >= %d)) fifos[wptr%d] <= din[%d*WIDTH-1:%d*WIDTH];\n'%(II,II-1,II,II-1)
    Str = Str.replace('TEXTWRITE0',TXT)

    TEXTWRITE3 = ''
    for II in range(1,Writes):
        TEXTWRITE3 += 'wire [WIDPTR:0] wptr%d = ((wptr+%d)>=DEPTH) ? ((wptr+%d)-DEPTH) : (wptr+%d);\n'%(II,II,II,II)
    TEXTWRITE3 += 'wire [WIDPTR:0] rptr0 = rptr;\n'
    for II in range(1,Reads):
        TEXTWRITE3 += 'wire [WIDPTR:0] rptr%d = ((rptr+%d)>=DEPTH) ? ((rptr+%d)-DEPTH) : (rptr+%d);\n'%(II,II,II,II)

    for II in range(1,Reads+1):
        TEXTWRITE3 += 'assign dout[WIDTH*%d-1:WIDTH*%d] = ((reads>=%d)&&oktoread) ? fifos[rptr%d] : 0;\n'%(II,II-1,II,II-1)

    Str = Str.replace('TEXTWRITE2',TEXTWRITE2)
    Str = Str.replace('TEXTWRITE3',TEXTWRITE3)

    Fout.write(Str)
    Str =  INSTSTRING
    Str = Str.replace('WRITES',str(Writes))
    Str = Str.replace('READS',str(Reads))
    Fout.write(Str)
    Fout.write(');\n*/\n')
    Fout.close()
    


def bitsFor(Num):
    Int = int(Num)
    Bits = len(bin(Int))-2
    return Bits


INSTSTRING = '''
/*
multififo_dDEPTH_wWRITES_rREADS #(32) fifo (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    .reads(reads),.dout(dout)
    .writes(writes),.din(din)
    ,.count(count[COUNT:0])
    ,.frees(frees[COUNT:0])
    ,.taken(taken)
'''

STRING0 = '''
module multififo_wWRITES_rREADS #(parameter WIDTH=32,parameter DEPTH=8) (input clk,input rst_n,input softreset
    ,input  [WWID:0] writes
    ,input  [RWID:0] reads
    ,input  [WIDTH*WRITES-1:0]  din
    ,output [WIDTH*READS-1:0]  dout
    ,output taken
    ,output reg [15:0] count
    ,output     [15:0] frees
);

assign frees = DEPTH-count;
reg [DEPTH-1:0] [WIDTH-1:0] fifos;
localparam WIDPTR = $clog2(DEPTH);
reg [WIDPTR:0] wptr,rptr;
wire badwrite = (writes>WRITES);
wire badread  = (reads>READS);
wire oktowrite = !badwrite && ((writes+count)<=DEPTH);
wire oktoread = !badread && (reads<=count);
assign taken = oktowrite;
TEXTWRITE3
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        fifos <= 0;
    end else if (oktowrite) begin
TEXTWRITE2
    end
end
wire [WIDPTR:0] nextwptr =  ((wptr+writes)>=DEPTH) ? ((wptr+writes)-DEPTH) : (wptr+writes);
wire [WIDPTR:0] nextrptr =  ((rptr+reads)>=DEPTH) ? ((rptr+reads)-DEPTH) : (rptr+reads);
always @(posedge clk or negedge rst_n) begin
    if(!rst_n) begin
        wptr <= 0; rptr <= 0; count<=0;
    end else if(softreset) begin
        wptr <= 0; rptr <= 0; count<=0;
    end else begin
        if(oktowrite) begin
            wptr <= nextwptr;
        end 
        if(oktoread) begin
            rptr <= nextrptr;
        end 
        count <= (oktowrite && oktoread) ? (count + writes -reads) : 
                 (oktowrite) ? (count+ writes) : 
                 (oktoread) ? (count - reads) : 
                 count;
    end 
end
endmodule
'''

main()

