module tb;
reg [31:0] cycles;   initial cycles=0;
reg [31:0] errors;   initial errors=0;
reg [31:0] wrongs;   initial wrongs=0;
reg [31:0] corrects; initial corrects=0;
reg [31:0] marker;   initial marker=0;
reg [39:0] ain;
reg [31:0] discovered,notdiscovered;
reg checkX; initial checkX=0;
reg forceX; initial forceX=0;


reg [31:0] force_index; initial force_index = 0;

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
glv_sqrt_u40_5 faulted (
     .clk(clk && running0) ,.rst_n(rst_n) ,.en(en)
    ,.ain(ain[39:0]) ,.vldin(vldin)
    ,.out(flt_out) ,.vldout(flt_vldout)
);
wire fault_cought = (flt_vldout!=vldout) || (flt_out != out);



reg makeStuckList; initial makeStuckList=0;

endmodule
