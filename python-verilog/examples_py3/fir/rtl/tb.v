`timescale 1ns/1ps
module tb;
integer    cycles;   initial cycles=0;
integer    errors;   initial errors=0;
integer    wrongs;   initial wrongs=0;
integer    panics;   initial panics=0;
integer    corrects; initial corrects=0;
reg [31:0] marker;   initial marker=0;
reg [31:0] marker0;   initial marker0=0;
reg [31:0] marker1;   initial marker1=0;
reg [31:0] marker2;   initial marker2=0;
reg [31:0] marker3;   initial marker3=0;
reg [31:0] Index;   initial Index=0;
reg [31:0] ID;   initial ID=0;
reg  clk;
reg [31:0] paddr;
reg  penable;
wire [31:0] prdata;
wire  pready;
reg  psel;
reg [31:0] pwdata;
reg  pwrite;
wire [7:0] result;
reg  rst_n;
reg [7:0] sample;
reg  vldin;
wire  vldout;

always begin
    clk=0;
    #10;
    clk=1;
    #10;
end
always @(posedge clk) begin
    #1;
    $python("negedge()");
    #1;
    $python("run_model()");
end

initial begin
    $dumpvars(0,tb);
    clk = 0;
    paddr = 0;
    penable = 0;
    psel = 0;
    pwdata = 0;
    pwrite = 0;
    rst_n = 0;
    sample = 0;
    vldin = 0;
    #100;
    rst_n=1;
end
fir_top dut (
     .clk(clk)
    ,.paddr(paddr[31:0])
    ,.penable(penable)
    ,.prdata(prdata[31:0])
    ,.pready(pready)
    ,.psel(psel)
    ,.pwdata(pwdata[31:0])
    ,.pwrite(pwrite)
    ,.result(result[7:0])
    ,.rst_n(rst_n)
    ,.sample(sample[7:0])
    ,.vldin(vldin)
    ,.vldout(vldout)
);

reg [1023:0] testname;
initial begin
    if ($value$plusargs("LOG=%s",testname)) begin 
        $python("pymonname()",testname);
    end 


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

