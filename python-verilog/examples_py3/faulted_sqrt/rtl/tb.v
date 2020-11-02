module tb;
reg [31:0] cycles;   initial cycles=0;
reg [31:0] errors;   initial errors=0;
reg [31:0] wrongs;   initial wrongs=0;
reg [31:0] corrects; initial corrects=0;
reg [31:0] marker;   initial marker=0;
reg [39:0] ain;
reg [31:0] discovered,notdiscovered;
reg checkX; initial checkX=0;

initial discovered = 0;
initial notdiscovered = 0;
reg  clk,en,rst_n,vldin;
wire [19:0] out;
wire  vldout;

always begin
    clk=0;
    #10;
    clk=1;
    #3; $python("negedge()"); #7;
end
initial begin
    $dumpvars(0,tb);
    ain[39:0] = 0;
    en = 0;
    rst_n = 0;
    vldin = 0;
    #100;
    rst_n=1;
end
sqrt_u40_5 golden (
     .clk(clk) ,.rst_n(rst_n) ,.en(en)
    ,.ain(ain[39:0]) ,.vldin(vldin)
    ,.out(out[19:0]) ,.vldout(vldout)
);

reg running0; initial running0 = 1;
wire [19:0] flt_out;
wire flt_vldout;
Flt_sqrt_u40_5 faulted (
     .clk(clk && running0) ,.rst_n(rst_n) ,.en(en)
    ,.ain(ain[39:0]) ,.vldin(vldin)
    ,.out(flt_out) ,.vldout(flt_vldout)
);
wire fault_cought = (flt_vldout!=vldout) || (flt_out != out);



reg running1; initial running1 = 1;
wire [19:0] flt_out1;
wire flt_vldout1;
Flt_sqrt_u40_5 faulted1 (
     .clk(clk && running1) ,.rst_n(rst_n) ,.en(en)
    ,.ain(ain[39:0]) ,.vldin(vldin)
    ,.out(flt_out1) ,.vldout(flt_vldout1)
);
wire fault_cought1 = (flt_vldout1!=vldout) || (flt_out1 != out);
reg running2; initial running2 = 1;
wire [19:0] flt_out2;
wire flt_vldout2;
Flt_sqrt_u40_5 faulted2 (
     .clk(clk && running2) ,.rst_n(rst_n) ,.en(en)
    ,.ain(ain[39:0]) ,.vldin(vldin)
    ,.out(flt_out2) ,.vldout(flt_vldout2)
);
wire fault_cought2 = (flt_vldout2!=vldout) || (flt_out2 !=out);
reg running3; initial running3 = 1;
wire [19:0] flt_out3;
wire flt_vldout3;
Flt_sqrt_u40_5 faulted3 (
     .clk(clk && running3) ,.rst_n(rst_n) ,.en(en)
    ,.ain(ain[39:0]) ,.vldin(vldin)
    ,.out(flt_out3) ,.vldout(flt_vldout3)
);
wire fault_cought3 = (flt_vldout3!=vldout) || (flt_out3 !=out);
reg running4; initial running4 = 1;
wire [19:0] flt_out4;
wire flt_vldout4;
Flt_sqrt_u40_5 faulted4 (
     .clk(clk && running4) ,.rst_n(rst_n) ,.en(en)
    ,.ain(ain[39:0]) ,.vldin(vldin)
    ,.out(flt_out4) ,.vldout(flt_vldout4)
);
wire fault_cought4 = (flt_vldout4!=vldout) || (flt_out4 !=out);
reg running5; initial running5 = 1;
wire [19:0] flt_out5;
wire flt_vldout5;
Flt_sqrt_u40_5 faulted5 (
     .clk(clk && running5) ,.rst_n(rst_n) ,.en(en)
    ,.ain(ain[39:0]) ,.vldin(vldin)
    ,.out(flt_out5) ,.vldout(flt_vldout5)
);
wire fault_cought5 = (flt_vldout5!=vldout) || (flt_out5 !=out);
reg running6; initial running6 = 1;
wire [19:0] flt_out6;
wire flt_vldout6;
Flt_sqrt_u40_5 faulted6 (
     .clk(clk && running6) ,.rst_n(rst_n) ,.en(en)
    ,.ain(ain[39:0]) ,.vldin(vldin)
    ,.out(flt_out6) ,.vldout(flt_vldout6)
);
wire fault_cought6 = (flt_vldout6!=vldout) || (flt_out6 !=out);
reg running7; initial running7 = 1;
wire [19:0] flt_out7;
wire flt_vldout7;
Flt_sqrt_u40_5 faulted7 (
     .clk(clk && running7) ,.rst_n(rst_n) ,.en(en)
    ,.ain(ain[39:0]) ,.vldin(vldin)
    ,.out(flt_out7) ,.vldout(flt_vldout7)
);
wire fault_cought7 = (flt_vldout7!=vldout) || (flt_out7 !=out);
reg running8; initial running8 = 1;
wire [19:0] flt_out8;
wire flt_vldout8;
Flt_sqrt_u40_5 faulted8 (
     .clk(clk && running8) ,.rst_n(rst_n) ,.en(en)
    ,.ain(ain[39:0]) ,.vldin(vldin)
    ,.out(flt_out8) ,.vldout(flt_vldout8)
);
wire fault_cought8 = (flt_vldout8!=vldout) || (flt_out8 !=out);
reg running9; initial running9 = 1;
wire [19:0] flt_out9;
wire flt_vldout9;
Flt_sqrt_u40_5 faulted9 (
     .clk(clk && running9) ,.rst_n(rst_n) ,.en(en)
    ,.ain(ain[39:0]) ,.vldin(vldin)
    ,.out(flt_out9) ,.vldout(flt_vldout9)
);
wire fault_cought9 = (flt_vldout9!=vldout) || (flt_out9 !=out);



reg makeStuckList; initial makeStuckList=0;

endmodule
