
module multififo_w1_r2 #(parameter WIDTH=32,parameter DEPTH=8) (input clk,input rst_n,input softreset
    ,input  [0:0] writes
    ,input  [1:0] reads
    ,input  [WIDTH*1-1:0]  din
    ,output [WIDTH*2-1:0]  dout
    ,output taken
    ,output reg [15:0] count
    ,output     [15:0] frees
);

assign frees = DEPTH-count;
reg [DEPTH-1:0] [WIDTH-1:0] fifos;
localparam WIDPTR = $clog2(DEPTH);
reg [WIDPTR:0] wptr,rptr;
wire badwrite = (writes>1);
wire badread  = (reads>2);
wire oktowrite = !badwrite && ((writes+count)<=DEPTH);
wire oktoread = !badread && (reads<=count);
assign taken = oktowrite;
wire [WIDPTR:0] rptr0 = rptr;
wire [WIDPTR:0] rptr1 = ((rptr+1)>=DEPTH) ? ((rptr+1)-DEPTH) : (rptr+1);
assign dout[WIDTH*1-1:WIDTH*0] = (count>0) ? fifos[rptr0] : 0;
assign dout[WIDTH*2-1:WIDTH*1] = (count>0) ? fifos[rptr1] : 0;

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
multififo_dDEPTH_w1_r2 #(32) fifo (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    .reads(reads),.dout(dout)
    .writes(writes),.din(din)
    ,.count(count[COUNT:0])
    ,.frees(frees[COUNT:0])
    ,.taken(taken)
);
*/
