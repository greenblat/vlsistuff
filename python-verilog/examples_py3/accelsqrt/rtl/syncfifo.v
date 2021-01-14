

module syncfifo #(parameter WID = 32, parameter DEPTH=8, parameter AWID = $clog2(DEPTH))(
     input clk,input rst_n,input softreset
    ,input validin, input [WID-1:0] datain, output full 
    ,input readout, output [WID-1:0] dataout, output empty
    ,output reg [AWID:0] count
    ,output overflow
);

parameter DEPTH1 = DEPTH-1;
parameter AWID1  = AWID-1;
reg [WID-1:0] fifos [0:DEPTH1];
// reg [DEPTH-1:0][WID-1:0] fifos;
reg [AWID1:0] wptr,rptr;
assign   empty = count == 0;
assign   full = count == DEPTH;
assign   dataout = fifos[rptr];
assign overflow = validin && full;
always @(posedge clk) begin
    if (validin && !full) begin
        fifos[wptr] <= datain;
    end  
end
always @(posedge clk or negedge rst_n) begin
    if(!rst_n) begin
        wptr <= 0; rptr <= 0; count<=0;
    end else if(softreset) begin
        wptr <= 0; rptr <= 0; count<=0;
    end else begin
        if(validin && !full) begin
            wptr <= (wptr==(DEPTH1)) ? 0 : (wptr + 1'b1);
        end  
        if(readout && !empty) begin
            rptr <= (rptr==(DEPTH1)) ? 0 : (rptr + 1'b1);
        end  
        count <= 
            ((validin && !full)&&(readout && !empty))  ? count :
            (validin && !full)  ? (count+1'b1) :
            (readout && !empty)  ? (count-1'b1) :
            count;

    end  
end
endmodule



