module fp_adder ( input [31:0] src0,input [31:0] src1, output [31:0] out);
wire [31:0] ZERO = 0;
wire a_sign = src0[31];
wire [7:0] a_exp = src0[30:23];
wire [26:0] a_val = {4'b1,src0[22:0]};
wire b_sign = src1[31];
wire [7:0] b_exp = src1[30:23];
wire [26:0] b_val = {4'b1,src1[22:0]};
wire [7:0] max_exp = (a_exp>b_exp) ? a_exp : b_exp;
wire [7:0] diff0 = max_exp-a_exp;
wire [7:0] diff1 = max_exp-b_exp;
wire [26:0] a_val_sh = (a_val >> diff0);
wire [26:0] b_val_sh = (b_val >> diff1);
wire [7:0] z_exp = max_exp;
wire [27:0] sum = 
    (a_sign==b_sign) ? (a_val_sh+b_val_sh) :
    (a_val_sh>b_val_sh) ? (a_val_sh-b_val_sh) :
    (b_val_sh-a_val_sh);
wire zero = sum==0;
wire z_sign = 
    zero                ? 0 :
    (a_sign==b_sign)    ? a_sign :
    (a_val_sh>b_val_sh) ? a_sign : b_sign;
wire [4:0] lead;
findLeadingOne32 onea (.src0({4'b0,sum}),.out(lead));
wire [27:0] sum_sh = zero ? sum : (lead>23) ? sum >> (lead-23) : (sum << (23-lead));
wire [7:0] z_exp_sh = zero ? 0 : z_exp+lead-23;
assign out = (src0[30:0]==ZERO) ? src1 : (src1[30:0]==ZERO) ? src0 : {z_sign,z_exp_sh,sum_sh[22:0]};
endmodule
