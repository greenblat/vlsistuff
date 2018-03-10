module asin_acos(input asin, input acos, input [31:0] ain,output [31:0] out, input clk,output reg vldout,input rst_n,output exception);
wire isneg = ain[31];
wire [5:0] shift6 = 20;
wire [31:0] ain0;
fp_float2int fint0(.ain({1'b0,ain[30:0]}),.bin(shift6),.out(ain0));
wire [31:0] ninetyDegrees = 26353589/2;   // pi*(1<<24)/2
wire [31:0] piRadians = 26353589;   // pi*(1<<24)
assign exception = ain0[31:20]!=0;
wire [9:0] diff = ain0[9:0];
wire [9:0] addr0 = ain0[19:10];
wire [24:0] result0;
wire [9:0] addr1 = (addr0==1023)? addr0 : (addr0+1);
wire [24:0] result1;
asin_table asin_table0(.addr(addr0),.result(result0));
asin_table asin_table1(.addr(addr1),.result(result1));
reg [24:0] d1_result1,d1_result0;
reg [24:0] outhold;
reg isneg1,isneg2,acos1,work1,acos2;
reg [9:0] d1_diff;
wire [10:0] d1_less = 11'h400 - d1_diff;
wire [35:0] result2 = d1_result0*d1_less + d1_result1*d1_diff; 
wire [24:0] result3 = result2[35:11];
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        isneg1 <= 0;
        acos1  <= 0;
        work1  <= 0;
        d1_result0 <= 0;
        d1_result1 <= 0;
        d1_diff    <= 0;
        isneg2 <= 0;
        acos2  <= 0;
        vldout  <= 0;
        outhold <= 0;
    end else begin
        isneg1 <= isneg;
        acos1  <= acos;
        work1  <= acos||asin;
        d1_result0 <= result0;
        d1_result1 <= result1;
        d1_diff    <= diff;
        isneg2 <= isneg1;
        acos2  <= acos1;
        vldout  <= work1;
        outhold <= result3;
    end
end
wire [31:0] outhold2;
wire [31:0] forout = (acos2 && isneg2) ? (piRadians - (ninetyDegrees-outhold)) :  acos2 ? (ninetyDegrees-outhold) : outhold ;
wire [5:0] backShift = 64-23;
fp_int2float intf0(.ain(forout),.bin(backShift),.out(outhold2),.is_signed(1'b0));
wire isneg3 = (acos2 && isneg2) ? 0 : isneg2;
assign out = {isneg3,outhold2[30:0]};
endmodule
