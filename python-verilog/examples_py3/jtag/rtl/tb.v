`timescale 1ns/1ps
module tb;
reg [31:0] cycles;   initial cycles=0;
reg [31:0] errors;   initial errors=0;
reg [31:0] wrongs;   initial wrongs=0;
reg [31:0] panics;   initial panics=0;
reg [31:0] corrects; initial corrects=0;
reg [31:0] marker;   initial marker=0;
reg [31:0] Index;   initial Index=0;
reg [15:0] seqptr; initial seqptr=0;
reg [255:0] markstr0; initial markstr0=0;
reg  clk;
reg  jtck;
reg  jtdi;
wire  jtdo;
reg  jtms;
wire [15:0] paddr;
wire  penable;
reg [31:0] prdata;
reg [29:0] status; initial status = 5;
reg  pready;
wire  psel;
wire [31:0] pwdata;
wire  pwrite;
reg  rst_n;
reg  por_n;

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
    por_n = 0;
    clk = 0;
    jtck = 0;
    jtdi = 0;
    jtms = 0;
    prdata = 0;
    pready = 0;
    rst_n = 0;
    #100;
    por_n = 1;
    #100;
    rst_n=1;
end
jtag2apb dut (
     .clk(clk)
    ,.jtck(jtck)
    ,.jtdi(jtdi)
    ,.jtdo(jtdo)
    ,.jtms(jtms)
    ,.paddr(paddr[15:0])
    ,.penable(penable)
    ,.prdata(prdata[31:0])
    ,.pready(pready)
    ,.psel(psel)
    ,.pwdata(pwdata[31:0])
    ,.pwrite(pwrite)
    ,.rst_n(rst_n)
    ,.por_n(por_n)
    ,.status(status)
);

reg [1023:0] testname;
initial begin
    if ($value$plusargs("SEQ=%s",testname)) begin 
         $display(" Running SEQ= %s.",testname); 
    end else begin
        testname = 0;
        $display(" default test");
    end 
    #10;
    if (testname!=0) $python("sequence()",testname);
end 
endmodule

