module syncfifo_sampled #(parameter WID = 32, parameter DEPTH=8, parameter AWID = $clog2(DEPTH))(
     input clk,input rst_n,input softreset
    ,input vldin, input [WID-1:0] din, output full
    ,input readout, output [WID-1:0] dout, output reg empty
    ,output [15:0] count
    ,output overflow
);
parameter DEPTH1 = DEPTH-1;
parameter AWID1  = AWID-1;
reg  [0:DEPTH1] [WID-1:0] fifos;
reg [AWID1:0] wptr,rptr;
reg [AWID:0] int_count;
assign count = int_count;
assign   full = int_count == DEPTH;
wire [AWID1:0] next_rptr = (readout && !empty) ? ((rptr==(DEPTH1)) ? 0 : (rptr + 1'b1)) : rptr;

reg [WID-1:0] tmp1; always @(posedge clk) tmp1 <= fifos[next_rptr];
reg [WID-1:0] tmp2; always @(posedge clk) tmp2 <=  din;
reg take_new; always @(posedge clk) take_new <= (empty || ((int_count==1)&&readout));
// always @(posedge clk) dout <= (empty || ((int_count==1)&&readout)) ? din : fifos[next_rptr];
assign dout = take_new ? tmp2 : tmp1;
assign overflow = vldin && full;
always @(posedge clk) begin
    if (vldin && !full) begin
        fifos[wptr] <= din;
    end 
end




wire [AWID:0] next_count = 
        ((vldin && !full)&&(readout && !empty))  ? int_count :
        (vldin && !full)  ? (int_count+1'b1) :
        (readout && !empty)  ? (int_count-1'b1) :
        int_count;


always @(posedge clk or negedge rst_n) begin
    if(!rst_n) begin
        wptr <= 0; rptr <= 0; int_count<=0; empty <= 1;
    end else if(softreset) begin
        wptr <= 0; rptr <= 0; int_count<=0; empty <= 1;
    end else begin
        if(vldin && !full) begin
            wptr <= (wptr==(DEPTH1)) ? 0 : (wptr + 1'b1);
        end 
        if(readout && !empty) begin
            rptr <= (rptr==(DEPTH1)) ? 0 : (rptr + 1'b1);
        end 
        int_count <= next_count;
        empty <= (next_count == 0);
    end 
end
wire [63:0]  sign_version = 64'h0001ecea00250623 ;
endmodule
