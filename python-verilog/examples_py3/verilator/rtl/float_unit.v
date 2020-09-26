


module float_unit (
     input clk, input rst_n
    ,input [31:0] src0
    ,input [31:0] src1
    ,input [3:0] oper
    ,input vldin

    ,output reg [31:0] result
    ,output reg vldout
);


wire [31:0] fsqrt_out; wire fsqrt_out_vld;
wire [31:0] fdiv_out; wire fdiv_out_vld;




wire fadd_code = oper==1;
wire fsub_code = oper==2;
wire fmul_code = oper==3;
wire fabs_code = oper==4;
wire fmax_code = oper==5;
wire fmin_code = oper==6;
wire fneg_code = oper==7;

wire fdiv_code = oper==8;
wire fsqrt_code = oper==9;

wire fsin_code = oper==10;
wire fcos_code = oper==11;

wire non_code  = vldin && ((oper==0)||(oper>11));


always @(posedge clk)  vldout <= 
      fadd_code||fsub_code||fmul_code 
    ||fabs_code||fneg_code
    || fmax_code || fmin_code  
    || fsqrt_out_vld
    || fdiv_out_vld
    || sincos_vldout
    || non_code 
    ;


wire sincos_vldout;
wire gft_out;
wire [31:0] fadd_out,fmul_out,sincos_out;
always @(posedge clk)  result <= 
    fabs_code ? {1'b0,src0[30:0]} :
    fneg_code ? {!src0[31],src0[30:0]} :
    fadd_code ? fadd_out :
    fsub_code ? fadd_out :
    fmul_code ? fmul_out :
    (fmin_code && fgt_out) ? src1 :
    (fmin_code && !fgt_out) ? src0 :
    (fmax_code && fgt_out) ? src0 :
    (fmax_code && !fgt_out) ? src1 :
    fsqrt_out_vld ? fsqrt_out :
    fdiv_out_vld ? fdiv_out :
    sincos_vldout ? sincos_out :
    32'b0;


fp_gt        fp_gt   (.src0(src0),.src1(src1),.out(fgt_out));


wire [31:0] src1_mod = (src1==0) ? 0 : fsub_code ? {!src1[31],src1[30:0]} : src1;
fp_adder faddr(.src0(src0),.src1(src1_mod),.out(fadd_out));

fp_multiplier fmul(.src0(src0),.src1(src1),.out(fmul_out));


fp_sqrt     fsqrt (.clk(clk),.rst_n(rst_n),.en(1'b1),.vldin(fsqrt_code ),.vldout(fsqrt_out_vld),.out(fsqrt_out),.src0(src0));
fp_divider  fdiv  (.clk(clk),.rst_n(rst_n),.en(1'b1),.vldin(fdiv_code),.vldout(fdiv_out_vld),.out(fdiv_out)
    ,.src0(src0),.src1(src1),.take_mod(1'b0));

fp_sincos sincos (.clk(clk),.rst_n(rst_n),.en(1'b1)
    ,.src0(src0),.out(sincos_out),.vldout(sincos_vldout)
    ,.what({1'b0,fcos_code,fsin_code,1'b0,1'b0,1'b0})
    ,.exception(panic)
);




endmodule

