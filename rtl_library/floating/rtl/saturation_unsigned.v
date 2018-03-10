module saturation_unsigned (input [31:0] ain,input [4:0] wid,output [31:0] out);
wire [31:0] mask0 = (1<<wid)-1;
wire [31:0] mask1 = ~mask0;
wire [31:0] data0 = ain & mask1;
wire all_good = (data0==0);
assign out = all_good ? ain : mask0;
endmodule
