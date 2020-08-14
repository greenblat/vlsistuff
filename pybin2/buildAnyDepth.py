#! /usr/bin/python

import os,sys,string

HELPSTRING = '''
invocation:     buildFifo.py  <Depth> <Writes>
this script builds RTL of a multi_sync_fifo with optional number of concurrent writes.
and Depth being number of fifo entries.
<Writes> is the number of cincurrent writes

'''


def main():
    try:
        Depth = int(sys.argv[1])
        Writes = int(sys.argv[2])
    except:
        print HELPSTRING
        return

    buildFifo(Depth,Writes)

def buildFifo(Depth,Writes):
    Fname = 'multififo_%d_%d.v'%(Depth,Writes)
    Fout = open(Fname,'w')
    Str = STRING0
    Str = string.replace(Str,'DEPTH',str(Depth))
    Str = string.replace(Str,'WRITES',str(Writes))
    Str = string.replace(Str,'DDD',str(Depth-1))
    Count  = bitsFor(Depth)+1
    Str = string.replace(Str,'WCOUNT',str(Count-2))
    Str = string.replace(Str,'COUNT',str(Count-1))
    TXT=''
    Wrts = []
    TEXTWRITE2 = '    if (write0) fifos[wptr] <= datain0;\n'
    for II in range(1,Writes):
        TEXTWRITE2 += '    if (write%d) fifos[wptr%d] <= datain%d;\n'%(II,II,II)
    for II in range(Writes):
        TXT += '    ,input write%d, input [WIDTH-1:0] datain%d\n'%(II,II)
        Wrts.append('write%d'%II)
    Str = string.replace(Str,'TEXTWRITE0',TXT)
    Str = string.replace(Str,'TEXTWRITE1','wire [%d:0] currentwrites = %d\'b0 + %s;\n'%(bitsFor(Writes)-1,bitsFor(Writes),string.join(Wrts,' +')))

    TEXTWRITE3 = ''
    for II in range(1,Writes):
        XX=[]
        for JJ in range(II):
            XX.append('write%d'%JJ)
        TEXTWRITE3 += 'wire [%d:0] offset%d = %d\'b0 + %s ;\n'%(Count-2,II,Count-1,string.join(XX,'+'))
        TEXTWRITE3 += 'wire [%d:0] wptr%d = ((wptr+offset%d)>=%d) ? ((wptr+offset%d)-%d) : (wptr+offset%d);\n'%(Count-2,II,II,Depth,II,Depth,II)
    Str = string.replace(Str,'TEXTWRITE2',TEXTWRITE2)
    Str = string.replace(Str,'TEXTWRITE3',TEXTWRITE3)

    Fout.write(Str)
    Str =  INSTSTRING
    Str = string.replace(Str,'DEPTH',str(Depth))
    Str = string.replace(Str,'WRITES',str(Writes))
    Str = string.replace(Str,'COUNT',str(Count-1))
    Fout.write(Str)
    for II in range(Writes):
        Fout.write('    ,.write%d(write%d),.datain%d(datain%d[31:0])\n'%(II,II,II,II))
    Fout.write(');\n*/\n')
    Fout.close()
    


def bitsFor(Num):
    Int = int(Num)
    Bits = len(bin(Int))-2
    return Bits

SIMPLECOUNT = 'assign   count = (wptr >= rptr) ? (wptr - rptr) :  (((2 * DEPTH) - rptr) + wptr);'

INSTSTRING = '''
/*
multififo_DEPTH_WRITES #(32) fifo (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    .readout(readout),.dataout(dataout[31:0])
    .full(full)
    .empty(empty)
    ,.count(count[COUNT:0])
    .overflow(overflow)
'''

STRING0 = '''
module multififo_DEPTH_WRITES #(parameter WIDTH=32) (input clk,input rst_n,input softreset
TEXTWRITE0
    ,input readout, output [WIDTH-1:0] dataout, output empty, output full
    ,output taken
    ,output reg [COUNT:0] count
    ,output overflow
);

reg [WIDTH-1:0] fifos [0:DDD];
reg [COUNT:0] wptr,rptr;
TEXTWRITE1
wire oktowrite = (currentwrites+count)<=DEPTH;
assign taken = oktowrite;
assign overflow = !oktowrite && (currentwrites>0);
assign   empty = count == 0;
assign   full = count == DEPTH;
assign   dataout = empty ? 0 : fifos[rptr];
TEXTWRITE3
always @(posedge clk) if (oktowrite) begin
TEXTWRITE2
end
wire [COUNT:0] nextwptr =  ((wptr+currentwrites)>=DEPTH) ? ((wptr+currentwrites)-DEPTH) : (wptr+currentwrites);
always @(posedge clk or negedge rst_n) begin
    if(!rst_n) begin
        wptr <= 0; rptr <= 0; count<=0;
    end else if(softreset) begin
        wptr <= 0; rptr <= 0; count<=0;
    end else begin
        if(oktowrite && !full) begin
            wptr <= nextwptr;
        end 
        if(readout && !empty) begin
            rptr <= (rptr==(DEPTH-1)) ? 0 : (rptr + 1);
        end 
        count <= ((oktowrite && !full)&&(readout && !empty)) ? (count+ currentwrites -1) : 
                 (oktowrite && !full) ? (count+ currentwrites) : 
                 (readout && !empty) ? (count -1) : 
                 count;
    end 
end
endmodule
'''

main()

