module fp_divider ( input [31:0] ain,input [31:0] bin, output [31:0] out,input vldin, input take_mod, output vldout, input clk,input rst_n,input en);
wire a_sign = ain[31];
wire [7:0] a_exp = ain[30:23];
wire [23:0] a_val = {1'b1,ain[22:0]};
wire b_sign = bin[31];
wire [7:0] b_exp = bin[30:23];
wire [23:0] b_val = {1'b1,bin[22:0]};
wire [8:0]  m_exp = a_exp-b_exp;
wire m_sign = a_sign != b_sign;
wire m_zero = (bin[30:0]==0)||(ain[30:0]==0);
wire [47:0] mid;
wire [22:0] remainder;
divi_u48_u24_8 divi (.clk(clk),.rst_n(rst_n),.en(en),.vldin(vldin),.vldout(vldout),.ain({a_val,24'b0}),.bin(b_val),.out(mid[47:0]),.remainder(remainder[22:0]));
reg [8:0] sh_zero;
reg [8:0] sh_sign;
reg [8:0] sh_mod;
reg [9*8-1:0] sh_exps;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        sh_zero <= 0;
        sh_sign <= 0;
        sh_mod <= 0;
        sh_exps <= 45'b0;
    end else if (en) begin
        sh_sign <= {sh_sign[7:0],m_sign};
        sh_zero <= {sh_zero[7:0],m_zero};
        sh_mod <= {sh_mod[7:0],take_mod};
        sh_exps <= { sh_exps[9*8-1:0],m_exp};
    end
end
wire z_sign = sh_sign[7];
wire z_mod = sh_mod[7];
wire z_zero = sh_zero[7];
wire [8:0] mm_exp = sh_exps[9*8-1:9*8-9];
wire [5:0] lead;
wire [47:0] midx = z_mod ? { 25'b0,remainder[22:0]} : mid;
findLeadingOne48 fone (.ain(midx),.out(lead));
wire [47:0] mid2 = mid << (47-lead);
wire [22:0] z_mat = mid2[46:24];
wire [8:0] mid_exp = mm_exp -(5'd24-lead) + (z_mod ? 5'd13 : 5'd0);
wire [8:0] z_exp = mid_exp+7'd127;
assign out = (z_zero||z_exp[8])  ? 0 : {z_sign,z_exp[7:0],z_mat};
endmodule
