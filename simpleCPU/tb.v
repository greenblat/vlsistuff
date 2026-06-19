`timescale 1ns/1ps
module tb;
integer    cycles;   initial cycles=0;
integer    errors;   initial errors=0;
integer    wrongs;   initial wrongs=0;
integer    warnings;   initial warnings=0;
integer    panics;   initial panics=0;
integer    corrects; initial corrects=0;
integer    seqptr; initial seqptr=0;
reg [255:0] markstr;   initial markstr=0;
reg [31:0] mark;   initial mark=0;
reg [31:0] marker;   initial marker=0;
reg [31:0] marker0;   initial marker0=0;
reg [31:0] marker1;   initial marker1=0;
reg [31:0] marker2;   initial marker2=0;
reg [31:0] marker3;   initial marker3=0;
reg [31:0] Index;   initial Index=0;
reg [31:0] ID;   initial ID=0;
reg  clk;
wire  irq;
reg  rst_n;

always begin
    clk=0;
    #10;
    clk=1;
    #3;
`ifdef SIMPY
    $python("negedge()");
`endif
    #7;
    cycles = cycles + 1;
end
initial begin
    $dumpvars(0,tb);
    rst_n = 0;
    clk = 0;
    rst_n = 0;
    #100;
    rst_n=1;

end
assign irq= (cycles==30);
wire finish_good,finish_bad;
dut dut (
     .clk(clk)
    ,.irq(irq)
    ,.rst_n(rst_n)
    ,.finish_good(finish_good)
    ,.finish_bad(finish_bad)
);

always @(posedge finish_good)  begin
    $display("FINISH GOOD");
    #200;
    $finish;
end
always @(posedge finish_bad)  begin
    $display("FINISH BAD");
    #200;
    $finish;
end

reg [1023:0] testname;
 initial begin
     if ($value$plusargs("SEQ=%s",testname)) begin 
        $display("RUN %s Code", testname);
     end 
// 
// 
//     if ($value$plusargs("SEQ=%s",testname)) begin 
//          $display(" Running SEQ= %s.",testname); 
//     end else begin
//         testname = 0;
//         $display(" default test");
//     end 
//     #10;
//     if (testname!=0) $python("sequence()",testname);
end 
endmodule
