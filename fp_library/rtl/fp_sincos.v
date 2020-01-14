module fp_sincos2 ( input [5:0] what,input [31:0] ain,output [31:0] out,output vldout, input clk,input rst_n,input en,output exception);

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


wire [31:0] negain = {!ain[31],ain[30:0]};

fp_gt i_gt0 (.ain(half_pi),.bin(ain),.out(gt0));
fp_gt i_gt1 (.ain(one_pi),.bin(ain),.out(gt1));
fp_gt i_gt2 (.ain(two_thirds_pi),.bin(ain),.out(gt2));

fp_gt i_gt0_n (.bin(neg_half_pi),.ain(ain),.out(ngt0));
fp_gt i_gt1_n (.bin(neg_one_pi),.ain(ain),.out(ngt1));
fp_gt i_gt2_n (.bin(neg_two_thirds_pi),.ain(ain),.out(ngt2));

wire [31:0] ain90,ain180,ain270;
wire [31:0] nain90,nain180,nain270;
fp_adder add1 (.ain(one_pi),.bin(negain),.out(ain90));
fp_adder add2 (.ain(ain),.bin({1'b1,one_pi[30:0]}),.out(ain180));
fp_adder add3 (.ain(two_pi),.bin(negain),.out(ain270));

fp_adder nadd1 (.ain(one_pi),.bin(ain),.out(nain90));
fp_adder nadd2 (.ain(ain),.bin(one_pi),.out(nain180));
fp_adder nadd3 (.ain(two_pi),.bin(ain),.out(nain270));



wire [31:0] cordicin_wire = (what[2:0]!=0) ? ain  :
    ain[31] ?  (
            ngt0 ? {1'b0,ain[30:0]} :
            ngt1 ? nain90 :
            ngt2 ? nain180 :
                   nain270

    ) : gt0 ? ain : gt1 ? ain90 : gt2 ?  ain180 : ain270;

reg [31:0] cordicin;
always @(posedge clk) cordicin<=cordicin_wire;


wire [31:0] genericresult;
reducedCordic  cordic(.ain(cordicin),.out(genericresult),.clk(clk)
    ,.atan(d1_what[2]),.sin(d1_what[3]),.cos(d1_what[4])
    ,.done(cordic_vld),.rst_n(rst_n));

wire was_atan = d4_what[2];
wire was_cos = d4_what[4];


delay_reg dlygt0 (.ain(gt0),.out(was_gt0),.tap(3'd3),.clk(clk),.rst_n(rst_n),.en(en));
delay_reg dlygt1 (.ain(gt1),.out(was_gt1),.tap(3'd3),.clk(clk),.rst_n(rst_n),.en(en));
delay_reg dlygt2 (.ain(gt2),.out(was_gt2),.tap(3'd3),.clk(clk),.rst_n(rst_n),.en(en));
delay_reg dlygt3 (.ain(ngt0),.out(was_ngt0),.tap(3'd3),.clk(clk),.rst_n(rst_n),.en(en));
delay_reg dlygt4 (.ain(ngt1),.out(was_ngt1),.tap(3'd3),.clk(clk),.rst_n(rst_n),.en(en));
delay_reg dlygt5 (.ain(ngt2),.out(was_ngt2),.tap(3'd3),.clk(clk),.rst_n(rst_n),.en(en));
delay_reg dlygt6 (.ain(ain[31]),.out(was_neg),.tap(3'd3),.clk(clk),.rst_n(rst_n),.en(en));

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

