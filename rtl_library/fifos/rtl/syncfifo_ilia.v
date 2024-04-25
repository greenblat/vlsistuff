// general purpose rtl of once clock fifo.
// wid and depth are parameters.
// greenblat@mac.com




module syncfifo_ilia #(parameter WID = 32, parameter DEPTH=8, parameter AWID = $clog2(DEPTH))(
     input clk,input rst_n,input softreset
    ,input validin, input [WID-1:0] datain, output full
    ,input readout, output [WID-1:0] dataout, output empty
    ,output reg [AWID:0] count
    ,output overflow
);

parameter DEPTH1 = DEPTH-1;
parameter AWID1  = AWID-1;
reg [WID-1:0] fifos [0:DEPTH1];
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
wire [63:0]  sign_version = 64'h000168c114240424 ;
endmodule

/*
example of instance:
syncfifo_ilia #(32,8) syncfifo (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(validin),.datain(datain[31:0])
    ,.full(full),.empty(empty),.overflow(overflow),.count(count[6:0])
    ,.readout(readout),.dataout(dataout[31:0])
);
*/


