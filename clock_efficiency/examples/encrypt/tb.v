`timescale 1ns/1ps
module tb;
reg [31:0] cycles;   initial cycles=0;
reg [31:0] errors;   initial errors=0;
reg [31:0] wrongs;   initial wrongs=0;
reg [31:0] panics;   initial panics=0;
reg [31:0] corrects; initial corrects=0;
reg [31:0] marker;   initial marker=0;
reg [31:0] marker0;   initial marker0=0;
reg [31:0] marker1;   initial marker1=0;
reg [31:0] marker2;   initial marker2=0;
reg [31:0] marker3;   initial marker3=0;
reg [31:0] Index;   initial Index=0;
reg  clk;
reg [31:0] datain;
wire [31:0] encrypted;
reg [127:0] key;
reg  rst_n;
reg  vldin;
wire  vldout;
reg [15:0] wasted,worked,dropped;
initial wasted = 0;
initial worked = 0;
initial dropped = 0;
wire vlds1 = dut.vlds[1];

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
    clk = 0;
    datain = 0;
    key = 0;
    rst_n = 0;
    vldin = 0;
    #100;
    rst_n=1;
end
encrypt_piped dut (
     .clk(clk)
    ,.datain(datain[31:0])
    ,.encrypted(encrypted[31:0])
    ,.key(key[127:0])
    ,.rst_n(rst_n)
    ,.vldin(vldin)
    ,.vldout(vldout)
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


module inout_driver ( inout io , input dflt );

reg val; initial val=0;
reg drive; initial drive=0;
assign io = drive ? val : 1'bz;
assign (pull1,pull0) io = dflt;

endmodule
