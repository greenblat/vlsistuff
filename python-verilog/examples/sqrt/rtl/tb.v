module tb;
reg [31:0] cycles;   initial cycles=0;
reg [31:0] errors;   initial errors=0;
reg [31:0] wrongs;   initial wrongs=0;
reg [31:0] corrects; initial corrects=0;
reg [31:0] marker;   initial marker=0;
reg [39:0] ain;
reg  clk;
reg  en;
wire [19:0] out;
reg  rst_n;
reg  vldin;
wire  vldout;

always begin
    clk=0;
    #10;
    clk=1;
    #3;
    $python("negedge()");
    #7;
end
initial begin
    $dumpvars(0,tb);
    ain[39:0] = 0;
    clk = 0;
    en = 0;
    rst_n = 0;
    vldin = 0;
    #100;
    rst_n=1;
end
sqrt_u40_5 sqrt_u40_5 (
     .ain(ain[39:0])
    ,.clk(clk)
    ,.en(en)
    ,.out(out[19:0])
    ,.rst_n(rst_n)
    ,.vldin(vldin)
    ,.vldout(vldout)
);
endmodule
