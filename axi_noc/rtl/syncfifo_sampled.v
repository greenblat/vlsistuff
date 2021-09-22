module syncfifo_sampled #(parameter WID = 32, parameter DEPTH=8, parameter AWID = $clog2(DEPTH))(
     input clk,input rst_n,input softreset
    ,input vldin, input [WID-1:0] din, output full
    ,input readout, output reg [WID-1:0] dout, output reg empty
    ,output reg [AWID:0] count
    ,output overflow
);
parameter DEPTH1 = DEPTH-1;
parameter AWID1  = AWID-1;
reg [WID-1:0] fifos [0:DEPTH1];
reg [AWID1:0] wptr,rptr;
assign   full = count == DEPTH;
wire [AWID1:0] next_rptr = (readout && !empty) ? ((rptr==(DEPTH1)) ? 0 : (rptr + 1'b1)) : rptr;
always @(posedge clk) dout <= (empty || ((count==1)&&readout)) ? din : fifos[next_rptr];
assign overflow = vldin && full;
always @(posedge clk) begin
    if (vldin && !full) begin
        fifos[wptr] <= din;
    end 
end




wire [AWID:0] next_count = 
        ((vldin && !full)&&(readout && !empty))  ? count :
        (vldin && !full)  ? (count+1'b1) :
        (readout && !empty)  ? (count-1'b1) :
        count;


always @(posedge clk or negedge rst_n) begin
    if(!rst_n) begin
        wptr <= 0; rptr <= 0; count<=0; empty <= 1;
    end else if(softreset) begin
        wptr <= 0; rptr <= 0; count<=0; empty <= 1;
    end else begin
        if(vldin && !full) begin
            wptr <= (wptr==(DEPTH1)) ? 0 : (wptr + 1'b1);
        end 
        if(readout && !empty) begin
            rptr <= (rptr==(DEPTH1)) ? 0 : (rptr + 1'b1);
        end 
        count <= next_count;
        empty <= (next_count == 0);
    end 
end
endmodule
