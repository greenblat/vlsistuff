
module multififo_w4_r4 #(parameter WIDTH=32,parameter DEPTH=8, parameter INIT=0) (input clk,input rst_n,input softreset
    ,input  [2:0] writes
    ,input  [2:0] reads
    ,input  [WIDTH*4-1:0]  din
    ,output [WIDTH*4-1:0]  dout
    ,output taken
    ,output reg [15:0] count
    ,output     [15:0] frees
);

assign frees = DEPTH-count;
reg [DEPTH-1:0] [WIDTH-1:0] fifos;
localparam WIDPTR = $clog2(DEPTH);
reg [WIDPTR:0] wptr,rptr;
wire badwrite = (writes>4);
wire badread  = (reads>4);
wire oktowrite = !badwrite && ((writes+count)<=DEPTH);
wire oktoread = !badread && (reads<=count);
assign taken = oktowrite;
wire [WIDPTR:0] wptr1 = ((wptr+1)>=DEPTH) ? ((wptr+1)-DEPTH) : (wptr+1);
wire [WIDPTR:0] wptr2 = ((wptr+2)>=DEPTH) ? ((wptr+2)-DEPTH) : (wptr+2);
wire [WIDPTR:0] wptr3 = ((wptr+3)>=DEPTH) ? ((wptr+3)-DEPTH) : (wptr+3);
wire [WIDPTR:0] rptr0 = rptr;
wire [WIDPTR:0] rptr1 = ((rptr+1)>=DEPTH) ? ((rptr+1)-DEPTH) : (rptr+1);
wire [WIDPTR:0] rptr2 = ((rptr+2)>=DEPTH) ? ((rptr+2)-DEPTH) : (rptr+2);
wire [WIDPTR:0] rptr3 = ((rptr+3)>=DEPTH) ? ((rptr+3)-DEPTH) : (rptr+3);
assign dout[WIDTH*1-1:WIDTH*0] = ((reads>=1)&&oktoread) ? fifos[rptr0] : 0;
assign dout[WIDTH*2-1:WIDTH*1] = ((reads>=2)&&oktoread) ? fifos[rptr1] : 0;
assign dout[WIDTH*3-1:WIDTH*2] = ((reads>=3)&&oktoread) ? fifos[rptr2] : 0;
assign dout[WIDTH*4-1:WIDTH*3] = ((reads>=4)&&oktoread) ? fifos[rptr3] : 0;

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        fifos <= INIT;
    end else if (oktowrite) begin
        if (oktowrite && (writes >= 1))  fifos[wptr] <= din[WIDTH-1:0];
        if (oktowrite && (writes >= 2)) fifos[wptr1] <= din[2*WIDTH-1:1*WIDTH];
        if (oktowrite && (writes >= 3)) fifos[wptr2] <= din[3*WIDTH-1:2*WIDTH];
        if (oktowrite && (writes >= 4)) fifos[wptr3] <= din[4*WIDTH-1:3*WIDTH];

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

/*
multififo_dDEPTH_w4_r4 #(32) fifo (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    .reads(reads),.dout(dout)
    .writes(writes),.din(din)
    ,.count(count[COUNT:0])
    ,.frees(frees[COUNT:0])
    ,.taken(taken)
);
*/
