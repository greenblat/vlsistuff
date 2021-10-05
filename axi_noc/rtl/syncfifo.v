
module syncfifo #(parameter WID = 32, parameter DEPTH=8, parameter AWID = $clog2(DEPTH))(
     input clk,input rst_n
    ,input vldin, input [WID-1:0] din, output full
    ,input readout, output [WID-1:0] dout, output empty
    ,output [15:0] count
    ,input softreset
    ,output overflow
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
wire panic_in = vldin && full;
wire panic_out = readout && empty;
always @(posedge clk) begin
    if (vldin && !full) begin
        fifos[wptr] <= din;
    end 
end
assign overflow = vldin && full;
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

always @(posedge clk) begin
     #1;
     if (rst_n == 1) begin
         if (vldin)  $display("@%d  VLDIN %m cnt=%d  %h",tb.cycles,count,din);
         if (readout)  $display("@%d  READOUT %m cnt=%d  %h",tb.cycles,count,dout);
     end
end
endmodule




