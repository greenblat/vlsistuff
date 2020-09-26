
// Ilia Greenblat: legacy. best to replace by int2float.



module fp_int2float_was(
    input [31:0] src0
    ,input [5:0] src1
    ,output [31:0] out
);



wire [31:0] ZERO = 0 ;



wire sign = src0[31];
wire [31:0] value = sign ? -src0 : src0 ;


wire [4:0] most;

findFirstOne32 find(.src0(value),.most(most[4:0]));

wire [4:0] shift = 31-most;

wire [31:0] svalue = value<<shift;
wire [23:0] man0 = svalue[31:8];
wire guard = svalue[7];
wire round_bit = svalue[6];
wire sticky = svalue[5:0]!=0;

wire rounding = guard &&(round_bit||sticky||man0[0]);
wire [23:0] man1 = man0 + rounding;

wire [7:0] exp0 = 30-shift;
wire [7:0] exp1 = 128+exp0 + (man1==24'hffffff) + {src1[5],src1[5],src1};

assign out = (src0==0) ? ZERO : {sign,exp1,man1[22:0]};


endmodule


