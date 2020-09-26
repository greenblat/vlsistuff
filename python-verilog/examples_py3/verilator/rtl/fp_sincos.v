
module fp_sincos ( input [5:0] what,input [31:0] src0,output [31:0] out,output vldout, input clk,input rst_n,input en,output exception);

assign exception=0;

wire [31:0] one = 32'h3f800000;


reg [5:0] d1_what;  always @(posedge clk) if (en) d1_what<=what;
reg [5:0] d2_what;  always @(posedge clk) if (en) d2_what<=d1_what;
reg [5:0] d3_what;  always @(posedge clk) if (en) d3_what<=d2_what;
reg [5:0] d4_what;  always @(posedge clk) if (en) d4_what<=d3_what;



wire [31:0] half_pi = 32'h3fc90fda;
wire [31:0] one_pi = 32'h40490fda;
wire [31:0] two_thirds_pi = 32'h4096cbe3;
wire [31:0] two_pi =  32'h40c90fda;

wire [31:0] neg_half_pi = 32'hbfc90fda;
wire [31:0] neg_one_pi = 32'hc0490fda;
wire [31:0] neg_two_thirds_pi = 32'hc096cbe3;


wire gt0,gt1,gt2,ngt0,ngt1,ngt2;
wire cordic_vld;
wire was_gt0,was_gt1,was_gt2;
wire was_ngt0,was_ngt1,was_ngt2;


wire [31:0] negsrc0 = {!src0[31],src0[30:0]};

fp_gt i_gt0 (.src0(half_pi),.src1(src0),.out(gt0));
fp_gt i_gt1 (.src0(one_pi),.src1(src0),.out(gt1));
fp_gt i_gt2 (.src0(two_thirds_pi),.src1(src0),.out(gt2));

fp_gt i_gt0_n (.src1(neg_half_pi),.src0(src0),.out(ngt0));
fp_gt i_gt1_n (.src1(neg_one_pi),.src0(src0),.out(ngt1));
fp_gt i_gt2_n (.src1(neg_two_thirds_pi),.src0(src0),.out(ngt2));

wire [31:0] src090,src0180,src0270;
wire [31:0] nsrc090,nsrc0180,nsrc0270;
fp_adder add1 (.src0(one_pi),.src1(negsrc0),.out(src090));
fp_adder add2 (.src0(src0),.src1({1'b1,one_pi[30:0]}),.out(src0180));
fp_adder add3 (.src0(two_pi),.src1(negsrc0),.out(src0270));

fp_adder nadd1 (.src0(one_pi),.src1(src0),.out(nsrc090));
fp_adder nadd2 (.src0(src0),.src1(one_pi),.out(nsrc0180));
fp_adder nadd3 (.src0(two_pi),.src1(src0),.out(nsrc0270));



wire [31:0] cordicin_wire = (what[2:0]!=0) ? src0  :
    src0[31] ?  (
            ngt0 ? {1'b0,src0[30:0]} :
            ngt1 ? nsrc090 :
            ngt2 ? nsrc0180 :
                   nsrc0270

    ) : gt0 ? src0 : gt1 ? src090 : gt2 ?  src0180 : src0270;

reg [31:0] cordicin;
always @(posedge clk) cordicin<=cordicin_wire;


wire [31:0] genericresult;
reducedCordic  cordic(.src0(cordicin),.out(genericresult),.clk(clk)
    ,.atan(d1_what[2]),.sin(d1_what[3]),.cos(d1_what[4])
    ,.done(cordic_vld),.rst_n(rst_n));

wire was_atan = d4_what[2];
wire was_cos = d4_what[4];


delay_reg dlygt0 (.src0(gt0),.out(was_gt0),.tap(3'd3),.clk(clk),.rst_n(rst_n),.en(en));
delay_reg dlygt1 (.src0(gt1),.out(was_gt1),.tap(3'd3),.clk(clk),.rst_n(rst_n),.en(en));
delay_reg dlygt2 (.src0(gt2),.out(was_gt2),.tap(3'd3),.clk(clk),.rst_n(rst_n),.en(en));
delay_reg dlygt3 (.src0(ngt0),.out(was_ngt0),.tap(3'd3),.clk(clk),.rst_n(rst_n),.en(en));
delay_reg dlygt4 (.src0(ngt1),.out(was_ngt1),.tap(3'd3),.clk(clk),.rst_n(rst_n),.en(en));
delay_reg dlygt5 (.src0(ngt2),.out(was_ngt2),.tap(3'd3),.clk(clk),.rst_n(rst_n),.en(en));
delay_reg dlygt6 (.src0(src0[31]),.out(was_neg),.tap(3'd3),.clk(clk),.rst_n(rst_n),.en(en));

wire [31:0] cordicresult = 
    was_atan ? genericresult :
    was_neg ?
    (
        (was_ngt0) ? {!was_cos,genericresult[30:0]} :  
        (was_ngt1) ?           {1'b1,genericresult[30:0]} :  
        (was_ngt2) ?           {was_cos,genericresult[30:0]} :  
        {1'b0,genericresult[30:0]} 

    ) : (
        (was_gt0) ? genericresult :  
        (was_gt1) ?           {was_cos,genericresult[30:0]} :  
        (was_gt2) ?           {1'b1,genericresult[30:0]} :  
        {!was_cos,genericresult[30:0]} 
    );


assign vldout = |d4_what;




assign out =  cordicresult;

endmodule

