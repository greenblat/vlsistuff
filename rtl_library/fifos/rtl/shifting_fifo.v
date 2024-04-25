

module shifting_fifo #(parameter WID = 32)(
     input clk,input rst_n
    ,input vldin, input [WID-1:0] din, output full
    ,input readout, output [WID-1:0] dout, output empty
    ,output [15:0] count
);

wire empty0,readout0;
wire [WID-1:0] dout0;
dstagefifo dtsage0 (.clk(clk),.rst_n(rst_n),.vldin(vldin),.din(din),.full(full),.empty(empty0),.dout(dout0),.readout(readout0));

wire full1,empty1,readout1;
wire [WID-1:0] dout1;
assign readout0 = !empty0 && !full1;
dstagefifo dtsage1 (.clk(clk),.rst_n(rst_n),.vldin(readout0),.din(dout0),.full(full1),.empty(empty1),.dout(dout1),.readout(readout1));
wire full2,empty2,readout2;
wire [WID-1:0] dout2;
assign readout1 = !empty1 && !full2;
dstagefifo dtsage2 (.clk(clk),.rst_n(rst_n),.vldin(readout1),.din(dout1),.full(full2),.empty(empty2),.dout(dout2),.readout(readout2));
wire full3,empty3,readout3;
wire [WID-1:0] dout3;
assign readout2 = !empty2 && !full3;
dstagefifo dtsage3 (.clk(clk),.rst_n(rst_n),.vldin(readout2),.din(dout2),.full(full3),.empty(empty3),.dout(dout3),.readout(readout3));
wire full4,empty4,readout4;
wire [WID-1:0] dout4;
assign readout3 = !empty3 && !full4;
dstagefifo dtsage4 (.clk(clk),.rst_n(rst_n),.vldin(readout3),.din(dout3),.full(full4),.empty(empty4),.dout(dout4),.readout(readout4));
wire full5,empty5,readout5;
wire [WID-1:0] dout5;
assign readout4 = !empty4 && !full5;
dstagefifo dtsage5 (.clk(clk),.rst_n(rst_n),.vldin(readout4),.din(dout4),.full(full5),.empty(empty5),.dout(dout5),.readout(readout5));
wire full6,empty6,readout6;
wire [WID-1:0] dout6;
assign readout5 = !empty5 && !full6;
dstagefifo dtsage6 (.clk(clk),.rst_n(rst_n),.vldin(readout5),.din(dout5),.full(full6),.empty(empty6),.dout(dout6),.readout(readout6));
assign readout6 = !empty6 && !full7;
dstagefifo dtsage7 (.clk(clk),.rst_n(rst_n),.vldin(readout6),.din(dout6),.full(full7),.empty(empty),.dout(dout),.readout(readout));


wire [63:0]  sign_version = 64'h000265e914240424 ;
endmodule


module dstagefifo #(parameter WID = 32) ( input clk,input rst_n
  ,input vldin, input [WID-1:0] din, output full
  ,input readout, output [WID-1:0] dout, output empty
);
reg [WID-1:0] aa,bb;
reg aavld,bbvld;

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        aavld <= 0;
        bbvld <= 0;
        aa <= 0;
        bb <= 0;
    end else begin
        case ({vldin,readout,aavld,bbvld})
        4'b0000 : begin end
        4'b0010 : begin bb <= aa; bbvld <= 1; aavld <= 0; end
        4'b0001 : begin end
        4'b0011 : begin end

        4'b1000 : begin bb <= din; bbvld <= 1; end

        4'b1001 : begin aa <= din; aavld <= 1; end
        4'b1101 : begin bb <= din; bbvld <= 1; end
        4'b1110 : begin bb <= din; bbvld <= 1; aavld <= 0; end
        4'b1111 : begin aa <= din; aavld <= 1; bb <= aa; bbvld <= 1; end

        4'b0100 : begin end
        4'b0101 : begin bb <= 0; bbvld <= 0; end
        4'b0110 : begin aa <= 0; aavld <= 0; end
        4'b0111 : begin aa <= 0; aavld <= 0; bb <= aa; bbvld <= 1; end
        default: $display("UNTREATED ",vldin,readout,aavld,bbvld);
        endcase
    end
end
assign full = aavld && bbvld ;
assign empty = !bbvld && !aavld;
assign dout = bbvld ? bb : aavld ? aa : 0 ;
wire [63:0]  sign_version = 64'h00012a0d14240424 ;
endmodule





