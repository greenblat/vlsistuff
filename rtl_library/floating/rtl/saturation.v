module saturation (input [31:0] ain,input [4:0] wid,output [31:0] out);
wire [31:0] mask0 = (1<<(wid-1))-1;
wire [31:0] mask1 = ~mask0;
wire [31:0] data0 = ain & mask1;
wire [31:0] data1 = data0 | mask0;
wire all_good =  (data0==0) || (data1==32'hffffffff);
assign out = 
    all_good ? ain :
    ain[31] ? -mask0 : mask0;
endmodule
