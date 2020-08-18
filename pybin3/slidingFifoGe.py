#! /usr/bin/env python3
import os,sys,string

def main():
    Writes = sys.argv[1]
    Reads  = sys.argv[2]
    Fout = open('/tmp/slidefifo_w%s_r%s.vvv'%(Writes,Reads),'w')
    Fout.write(TEXT)
    Fout.close()
    os.system('genver.py /tmp/slidefifo_w%s_r%s.vvv slidefifo_w%s_r%s.v %s %s'%(Writes,Reads,Writes,Reads,Writes,Reads))


TEXT = '''
#WRITES = int(argv(0))
#READS = int(argv(1))

module slidefifo_wWRITES_rREADS #(parameter WIDTH=32,parameter DEPTH=8) (input clk,input rst_n,input softreset
    ,input  vldin
    ,input  readout
    ,output vldout
    ,input  [WIDTH*WRITES-1:0]  din
    ,output [WIDTH*READS-1:0]  dout
    ,output reg [15:0] count
    ,output     [15:0] frees
);

localparam WIDPTR = $clog2(DEPTH);

assign frees = DEPTH-count;
assign vldout = (count>=READS);
reg [DEPTH-1:0] [WIDTH-1:0] fifos;
reg [WIDPTR:0] wptr,rptr;
wire oktowrite = vldin ? ((WRITES+count)<=DEPTH) : 0;
wire oktoread =  readout ? (READS<=count) : 0 ;
assign taken = oktowrite;


wire [WIDPTR:0] wptr0 = wptr;
#for II in range(1,WRITES):
wire [WIDPTR:0] wptrII = ((wptr+II)>=DEPTH) ? ((wptr+II)-DEPTH) : (wptr+II);
# 

wire [WIDPTR:0] rptr0 = rptr;
#for II in range(1,READS):
wire [WIDPTR:0] rptrII = ((rptr+II)>=DEPTH) ? ((rptr+II)-DEPTH) : (rptr+II);
# 
#for II in range(READS):
assign dout[WIDTH*<>II+1<>-1:WIDTH*II] = oktoread ? fifos[rptrII] : 0;
# 

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        fifos <= 0;
    end else if (oktowrite) begin
#for II in range(WRITES):
        fifos[wptrII] <= din[<>II+1<>*WIDTH-1:II*WIDTH];
#
    end
end
wire [WIDPTR:0] nextwptr =  ((wptr+WRITES)>=DEPTH) ? ((wptr+WRITES)-DEPTH) : (wptr+WRITES);
wire [WIDPTR:0] nextrptr =  ((rptr+READS)>=DEPTH) ? ((rptr+READS)-DEPTH) : (rptr+READS);
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
        count <= (oktowrite && oktoread) ? (count + WRITES -READS) : 
                 (oktowrite) ? (count+ writes) : 
                 (oktoread) ? (count-reads) : 
                 count;
    end 
end
endmodule
'''






if __name__ == '__main__': main()
