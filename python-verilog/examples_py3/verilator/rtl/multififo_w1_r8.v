
module multififo_w1_r8 #(parameter WIDTH=32,parameter DEPTH=8) (input clk,input rst_n,input softreset
    ,input  [0:0] writes
    ,input  [3:0] reads
    ,input  [WIDTH*1-1:0]  din
    ,output [WIDTH*8-1:0]  dout
    ,output taken
    ,output reg [15:0] count
    ,output     [15:0] frees
);

assign frees = DEPTH-count;
reg [DEPTH-1:0] [WIDTH-1:0] fifos;
localparam WIDPTR = $clog2(DEPTH);
reg [WIDPTR:0] wptr,rptr;
wire badwrite = (writes>1);
wire badread  = (reads>8);
wire oktowrite = !badwrite && ((writes+count)<=DEPTH);
wire oktoread = !badread && (reads<=count);
assign taken = oktowrite;
wire [WIDPTR:0] rptr0 = rptr;
wire [WIDPTR:0] rptr1 = ((rptr+1)>=DEPTH) ? ((rptr+1)-DEPTH) : (rptr+1);
wire [WIDPTR:0] rptr2 = ((rptr+2)>=DEPTH) ? ((rptr+2)-DEPTH) : (rptr+2);
wire [WIDPTR:0] rptr3 = ((rptr+3)>=DEPTH) ? ((rptr+3)-DEPTH) : (rptr+3);
wire [WIDPTR:0] rptr4 = ((rptr+4)>=DEPTH) ? ((rptr+4)-DEPTH) : (rptr+4);
wire [WIDPTR:0] rptr5 = ((rptr+5)>=DEPTH) ? ((rptr+5)-DEPTH) : (rptr+5);
wire [WIDPTR:0] rptr6 = ((rptr+6)>=DEPTH) ? ((rptr+6)-DEPTH) : (rptr+6);
wire [WIDPTR:0] rptr7 = ((rptr+7)>=DEPTH) ? ((rptr+7)-DEPTH) : (rptr+7);
assign dout[WIDTH*1-1:WIDTH*0] = fifos[rptr0] ;
assign dout[WIDTH*2-1:WIDTH*1] = fifos[rptr1] ;
assign dout[WIDTH*3-1:WIDTH*2] = fifos[rptr2] ;
assign dout[WIDTH*4-1:WIDTH*3] = fifos[rptr3] ;
assign dout[WIDTH*5-1:WIDTH*4] = fifos[rptr4] ;
assign dout[WIDTH*6-1:WIDTH*5] = fifos[rptr5] ;
assign dout[WIDTH*7-1:WIDTH*6] = fifos[rptr6] ;
assign dout[WIDTH*8-1:WIDTH*7] = fifos[rptr7] ;

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        fifos <= 0;
    end else if (oktowrite) begin
        if (oktowrite && (writes >= 1))  fifos[wptr] <= din[WIDTH-1:0];

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
multififo_dDEPTH_w1_r8 #(32) fifo (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    .reads(reads),.dout(dout)
    .writes(writes),.din(din)
    ,.count(count[COUNT:0])
    ,.frees(frees[COUNT:0])
    ,.taken(taken)
);
*/
