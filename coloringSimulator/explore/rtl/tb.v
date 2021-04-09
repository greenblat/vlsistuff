`timescale 1ns/1ps
`define BW 63
module tb;
reg [31:0] cycles;   initial cycles=0;
reg [31:0] errors;   initial errors=0;
reg [31:0] wrongs;   initial wrongs=0;
reg [31:0] panics;   initial panics=0;
reg [31:0] corrects; initial corrects=0;
reg [31:0] marker;   initial marker=0;
reg [31:0] Index;   initial Index=0;
reg [`BW:0] aaa;
reg [`BW:0] bbb;
reg [`BW:0] ccc;
reg [`BW:0] clk0;
reg [`BW:0] clk1;
reg [`BW:0] eee;
wire [`BW:0] qbad;
wire [`BW:0] qgood;
reg clk;
reg rst_n;

always begin
    clk=0;
    #10;
    clk=1;
    #3;
    $python("negedge()");
    #7;
end
reg [31:0] CLK0PHASE = 7;
reg [31:0] CLK1PHASE = 13;

always begin
    clk0 = 2;
    #(CLK0PHASE);
    clk0 = 3;
    #(CLK0PHASE);
end

always begin
    clk1 = 2;
    #(CLK1PHASE);
    clk1 = 3;
    #(CLK1PHASE);
end


initial begin
    $dumpvars(0,tb);
    aaa = 0;
    bbb = 0;
    ccc = 0;
    clk0 = 0;
    clk1 = 0;
    eee = 0;
    #100;
    rst_n=1;
end
xdesign dut (
     .aaa(aaa)
    ,.bbb(bbb)
    ,.ccc(ccc)
    ,.clk0(clk0)
    ,.clk1(clk1)
    ,.eee(eee)
    ,.qbad(qbad)
    ,.qgood(qgood)
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


