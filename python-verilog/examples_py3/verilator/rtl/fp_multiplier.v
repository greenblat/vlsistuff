module fp_multiplier ( input [31:0] src0,input [31:0] src1, output [31:0] out);
wire [31:0] ZERO = 32'b0;
wire [31:0] NEGZERO = 32'h80000000;
wire zeroes = (ZERO==src0)||(ZERO==src1)||(NEGZERO==src0)||(NEGZERO==src1);
wire a_sign = src0[31];
wire [7:0] a_exp = src0[30:23];
wire [23:0] a_val = {1'b1,src0[22:0]};
wire b_sign = src1[31];
wire [7:0] b_exp = src1[30:23];
wire [23:0] b_val = {1'b1,src1[22:0]};
wire [50:0] product = {24'b0,a_val} * {24'b0,b_val};
wire is48 = product[47];
wire z_sign = a_sign != b_sign;
wire [8:0]  exp0 = a_exp+ b_exp+is48-7'd127 ;
wire [7:0]  z_exp = exp0[8] ? 8'd255 : exp0[7:0] ;
wire [22:0] z_mat = is48 ? product[46:24] : product[45:23];
assign out = zeroes ? ZERO : {z_sign,z_exp,z_mat};
endmodule
