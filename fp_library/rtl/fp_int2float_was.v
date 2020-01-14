module fp_int2float_was(
    input [31:0] ain
    ,input [5:0] bin
    ,output [31:0] out
);
wire [31:0] ZERO = 0 ;
wire sign = ain[31];
wire [31:0] value = sign ? -ain : ain ;
wire [4:0] most;
findFirstOne32 find(.ain(value),.most(most[4:0]));
wire [4:0] shift = 31-most;
wire [31:0] svalue = value<<shift;
wire [23:0] man0 = svalue[31:8];
wire guard = svalue[7];
wire round_bit = svalue[6];
wire sticky = svalue[5:0]!=0;
wire rounding = guard &&(round_bit||sticky||man0[0]);
wire [23:0] man1 = man0 + rounding;
wire [7:0] exp0 = 30-shift;
wire [7:0] exp1 = 128+exp0 + (man1==24'hffffff) + {bin[5],bin[5],bin};
assign out = (ain==0) ? ZERO : {sign,exp1,man1[22:0]};
endmodule
