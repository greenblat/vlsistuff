module fp_adder3 ( input [31:0] in0,input [31:0] in1, input [31:0] in2, output [31:0] out);
wire a_sign = in0[31];
wire [7:0] a_exp = in0[30:23];
wire [26:0] a_val = {4'b1,in0[22:0]};
wire b_sign = in1[31];
wire [7:0] b_exp = in1[30:23];
wire [26:0] b_val = {4'b1,in1[22:0]};
wire c_sign = in2[31];
wire [7:0] c_exp = in2[30:23];
wire [26:0] c_val = {4'b1,in2[22:0]};
wire [7:0] exp0 = (a_exp>b_exp) ? a_exp : b_exp;
wire [7:0] maxexp = (exp0>c_exp) ? exp0 : c_exp;
wire [7:0] diffa = maxexp-a_exp;
wire [7:0] diffb = maxexp-b_exp;
wire [7:0] diffc = maxexp-c_exp;
wire [26:0] a_val_sh = (a_val >> diffa);
wire [26:0] b_val_sh = (b_val >> diffb);
wire [26:0] c_val_sh = (c_val >> diffc);
wire [7:0] z_exp = maxexp;
wire [28:0] sum = 
    (a_sign ? -a_val_sh : a_val_sh ) +
    (b_sign ? -b_val_sh : b_val_sh ) +
    (c_sign ? -c_val_sh : c_val_sh ); 
wire z_sign = sum[28];
wire [28:0] possum = z_sign ? -sum : sum;
wire [4:0] lead;
findLeadingOne32 onea (.ain({3'b0,possum}),.out(lead));
wire [27:0] sum_sh = (lead>23) ? possum >> (lead-23) : (possum << (23-lead));
wire [7:0] z_exp_final = z_exp+lead-23;
assign out = {z_sign,z_exp_final,sum_sh[22:0]};
endmodule
