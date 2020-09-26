// Ilia Greenblat

module fp_gt ( input [31:0] src0,input [31:0] src1, output out);
wire a_sign = src0[31];
wire [7:0] a_exp = src0[30:23];
wire [26:0] a_mat = {4'b1,src0[22:0]};
wire b_sign = src1[31];
wire [7:0] b_exp = src1[30:23];
wire [26:0] b_mat = {4'b1,src1[22:0]};
assign out = 
    (a_sign && !b_sign) ? 1'b0 :
    (!a_sign && b_sign) ? 1'b1 :
    (!a_sign && !b_sign) ?  ( (a_exp>b_exp) ? 1'b1 : (b_exp>a_exp) ? 1'b0 : (a_mat>b_mat)) :
    (a_sign && b_sign) ?  ( (a_exp>b_exp) ? 1'b0 : (b_exp>a_exp) ? 1'b1 : (a_mat<b_mat)) :
    1'bx;
endmodule
