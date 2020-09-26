// Ilia Greenblat : coric square root

module fp_sqrt ( input [31:0] src0,output [31:0] out,input vldin, output vldout, input clk,input rst_n,input en);
wire [31:0] ZERO = 0;
wire a_sign = src0[31];
wire [7:0] a_exp = src0[30:23]-127;
wire [23:0] a_val = {1'b1,src0[22:0]};
wire [47:0] amat_odd  = {a_val,24'b0};
wire [47:0] amat_even = {1'b0,a_val,23'b0};
wire [47:0] amat = a_exp[0] ? amat_odd : amat_even;
wire [23:0] mid;
sqrt_u48_10 sqrt (.clk(clk),.rst_n(rst_n),.en(en),.vldin(vldin),.vldout(vldout),.src0(amat),.out(mid[23:0]));
wire [7:0] m_exp = {a_exp[7],a_exp[7:1]};
wire m_sign = a_sign;
wire m_zero = src0[30:0]==0;
reg [8:0] sh_sign;
reg [8:0] sh_zero;
reg [63:0] sh_exps;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        sh_sign <= 0;
        sh_zero <= 0;
        sh_exps <= 64'b0;
    end else if (en) begin
        sh_zero <= {sh_zero[7:0],m_zero};
        sh_sign <= {sh_sign[7:0],m_sign};
        sh_exps <= { sh_exps[55:0],m_exp};
    end
end
wire z_sign = sh_sign[7];
wire [7:0] last_exp = sh_exps[63:56];
wire [7:0] z_exp = sh_zero[7] ? 0 : (last_exp+127);
wire [22:0] z_mat = sh_zero[7] ? 0 : mid[22:0];
assign out = {z_sign,z_exp,z_mat};
endmodule
