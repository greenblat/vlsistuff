module fp_int2float #(
    parameter WIDE=32
)(
    input [WIDE-1:0] src0
    ,input [5:0] src1
    ,input is_signed
    ,output [31:0] out
);
wire [31:0] ZERO = 0 ;
wire sign = src0[WIDE-1] && is_signed;
wire [WIDE-1:0] value0 = sign ? -src0 : src0 ;
wire [31:0] value = value0;
wire [4:0] most;
findFirstOne32 find(.src0(value),.most(most[4:0]));
wire [4:0] shift = 5'd31-most;
wire [31:0] svalue = value<<shift;
wire [23:0] man0 = svalue[31:8];
wire guard = svalue[7];
wire round_bit = svalue[6];
wire sticky = svalue[5:0]!=0;
wire rounding = guard &&(round_bit||sticky||man0[0]);
wire [23:0] man1 = man0 + rounding;
wire [7:0] exp0 = 6'd30-shift;
wire [7:0] exp1 = 8'd128+exp0 + (man1==24'hffffff) + {src1[5],src1[5],src1};
assign out = (src0==0) ? ZERO : {sign,exp1,man1[22:0]};
endmodule
