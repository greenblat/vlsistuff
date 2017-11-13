module tb;
reg [31:0] cycles;   initial cycles=0;
reg [31:0] errors;   initial errors=0;
reg [31:0] wrongs;   initial wrongs=0;
reg [31:0] corrects; initial corrects=0;
reg [31:0] marker;   initial marker=0;
reg [31:0] bads,goods,fline;   initial fline=0;
initial bads=0;
initial goods=0;



reg jtck_dr,jtck_va;
reg jtdi_dr,jtdi_va;
reg jtdo_dr,jtdo_va;
reg jtms_dr,jtms_va;
reg rst_n_dr,rst_n_va;


wire jtck = jtck_dr ? jtck_va : 1'bz;
wire jtdi = jtdi_dr ? jtdi_va : 1'bz;
wire jtdo = jtdo_dr ? jtdo_va : 1'bz;
wire jtms = jtms_dr ? jtms_va : 1'bz;
wire rst_n = rst_n_dr ? rst_n_va : 1'bz;

always begin
    $python("negedge()");
    #10;
end
initial begin
    $dumpvars(0,tb);
    jtck_va = 0;
    jtdi_va = 0;
    jtdo_va = 0;
    jtms_va = 0;
    rst_n_va = 0;
    jtck_dr = 0;
    jtdi_dr = 0;
    jtdo_dr = 0;
    jtms_dr = 0;
    rst_n_dr = 0;
end
jtagreg jtagreg (
     .jtck(jtck)
    ,.jtdi(jtdi)
    ,.jtdo(jtdo)
    ,.jtms(jtms)
    ,.rst_n(rst_n)
);
endmodule
