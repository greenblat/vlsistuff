module fp_adder10 ( 
    input [31:0] in0,input [31:0] in1, input [31:0] in2, input [31:0] in3
    ,input [31:0] in4,input [31:0] in5, input [31:0] in6, input [31:0] in7
    ,input [31:0] in8,input [31:0] in9
    , output [31:0] out);
wire a_sign = in0[31];
wire [7:0] a_exp = in0[30:23];
wire [26:0] a_val = {4'b1,in0[22:0]};
wire b_sign = in1[31];
wire [7:0] b_exp = in1[30:23];
wire [26:0] b_val = {4'b1,in1[22:0]};
wire c_sign = in2[31];
wire [7:0] c_exp = in2[30:23];
wire [26:0] c_val = {4'b1,in2[22:0]};
wire d_sign = in3[31];
wire [7:0] d_exp = in3[30:23];
wire [26:0] d_val = {4'b1,in3[22:0]};
wire e_sign = in4[31];
wire [7:0] e_exp = in4[30:23];
wire [26:0] e_val = {4'b1,in4[22:0]};
wire f_sign = in5[31];
wire [7:0] f_exp = in5[30:23];
wire [26:0] f_val = {4'b1,in5[22:0]};
wire g_sign = in6[31];
wire [7:0] g_exp = in6[30:23];
wire [26:0] g_val = {4'b1,in6[22:0]};
wire h_sign = in7[31];
wire [7:0] h_exp = in7[30:23];
wire [26:0] h_val = {4'b1,in7[22:0]};
wire i_sign = in8[31];
wire [7:0] i_exp = in8[30:23];
wire [26:0] i_val = {4'b1,in8[22:0]};
wire j_sign = in9[31];
wire [7:0] j_exp = in9[30:23];
wire [26:0] j_val = {4'b1,in9[22:0]};
wire [7:0] exp0 = (a_exp>b_exp) ? a_exp : b_exp;
wire [7:0] exp1 = (c_exp>d_exp) ? c_exp : d_exp;
wire [7:0] exp2 = (e_exp>f_exp) ? e_exp : f_exp;
wire [7:0] exp3 = (g_exp>h_exp) ? g_exp : h_exp;
wire [7:0] exp4 = (i_exp>j_exp) ? i_exp : j_exp;
wire [7:0] exp5 = (exp0>exp1) ? exp0 : exp1;
wire [7:0] exp6 = (exp2>exp3) ? exp2 : exp3;
wire [7:0] exp7 = (exp4>exp5) ? exp5 :exp6;
wire [7:0] maxexp = (exp4>exp7) ? exp4 :exp7;
wire [7:0] diffa = maxexp-a_exp;
wire [7:0] diffb = maxexp-b_exp;
wire [7:0] diffc = maxexp-c_exp;
wire [7:0] diffd = maxexp-d_exp;
wire [7:0] diffe = maxexp-e_exp;
wire [7:0] difff = maxexp-f_exp;
wire [7:0] diffg = maxexp-g_exp;
wire [7:0] diffh = maxexp-h_exp;
wire [7:0] diffi = maxexp-i_exp;
wire [7:0] diffj = maxexp-j_exp;
wire [26:0] a_val_sh = (a_val >> diffa);
wire [26:0] b_val_sh = (b_val >> diffb);
wire [26:0] c_val_sh = (c_val >> diffc);
wire [26:0] d_val_sh = (d_val >> diffd);
wire [26:0] e_val_sh = (e_val >> diffe);
wire [26:0] f_val_sh = (f_val >> difff);
wire [26:0] g_val_sh = (g_val >> diffg);
wire [26:0] h_val_sh = (h_val >> diffh);
wire [26:0] i_val_sh = (i_val >> diffi);
wire [26:0] j_val_sh = (j_val >> diffj);
wire [7:0] z_exp = maxexp;
wire [31:0] sum = 
    (a_sign ? -a_val_sh : a_val_sh ) +
    (b_sign ? -b_val_sh : b_val_sh ) +
    (c_sign ? -c_val_sh : c_val_sh ) +
    (d_sign ? -d_val_sh : d_val_sh ) +
    (e_sign ? -e_val_sh : e_val_sh ) +
    (f_sign ? -f_val_sh : f_val_sh ) +
    (g_sign ? -g_val_sh : g_val_sh ) +
    (h_sign ? -h_val_sh : h_val_sh ) +
    (i_sign ? -i_val_sh : i_val_sh ) +
    (j_sign ? -j_val_sh : j_val_sh );
wire z_sign = sum[31];
wire [31:0] possum = z_sign ? -sum : sum;
wire [4:0] lead;
findLeadingOne32 onea (.ain(possum),.out(lead));
wire [31:0] sum_sh = (lead>23) ? possum >> (lead-23) : (possum << (23-lead));
wire [7:0] z_exp_final = z_exp+lead-23;
assign out = {z_sign,z_exp_final,sum_sh[22:0]};
endmodule
