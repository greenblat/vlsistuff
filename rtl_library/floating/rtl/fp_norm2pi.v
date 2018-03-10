module fp_norm2pi (input [31:0] ain,output [31:0] out);
wire sign0 = ain[31];
wire [31:0] mid0,mid1;
wire [31:0] bconst = 32'h49800000;    //    (1<<20)/(2*math.pi)  ===> 166886.05360752725
fp_multiplier mul0 (.ain({1'b0,ain[30:0]}),.bin(bconst),.out(mid0));
fp_float2int f2i (.ain(mid0),.bin(6'd0),.out(mid1));
wire [19:0] mid2 = mid1[19:0];
wire [31:0] mid3 = sign0 ?   -mid2 : mid2;
fp_int2float i2f (.ain(mid3),.bin(6'd44),.out(out),.is_signed(1'b0));
endmodule
