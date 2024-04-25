
module syncfifo #(parameter WID = 32, parameter DEPTH=8, parameter AWID = $clog2(DEPTH))(
     input clk,input rst_n, input softreset
    ,input vldin, input [WID-1:0] din, output full
    ,input readout, output [WID-1:0] dout, output empty
    ,output [15:0] count
);

reg [AWID:0] int_count;
assign count = int_count;
parameter DEPTH1 = DEPTH-1;
parameter AWID1  = AWID-1;
reg [WID-1:0] fifos [0:DEPTH1];
reg [AWID1:0] wptr,rptr;
assign   empty = int_count == 0;
assign   full = int_count == DEPTH;
assign   dout = fifos[rptr];
wire overflow = vldin && full;
always @(posedge clk) begin
    if (vldin && !full) begin
        fifos[wptr] <= din;
    end 
end
always @(posedge clk or negedge rst_n) begin
    if(!rst_n) begin
        wptr <= 0; rptr <= 0; int_count<=0;
    end else if(softreset) begin
        wptr <= 0; rptr <= 0; int_count<=0;
    end else begin
        if(vldin && !full) begin
            wptr <= (wptr==(DEPTH1)) ? 0 : (wptr + 1'b1);
        end 
        if(readout && !empty) begin
            rptr <= (rptr==(DEPTH1)) ? 0 : (rptr + 1'b1);
        end 
        int_count <= 
            ((vldin && !full)&&(readout && !empty))  ? int_count :
            (vldin && !full)  ? (int_count+1'b1) :
            (readout && !empty)  ? (int_count-1'b1) :
            int_count;

    end 
end

// always @(posedge clk) begin
//     #1;
//     if (rst_n == 1) begin
//         if (vldin === 1'bx)  $display("VLDIN X %m");
//         if (readout === 1'bx) $display("READOUT X %m");
//     end
// end
wire [63:0]  sign_version = 64'h0001815a14240424 ;
endmodule




