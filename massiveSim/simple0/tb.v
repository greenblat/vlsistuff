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
reg [159:0] msgin; initial msgin=0;
wire [159:0] msgout;
wire  okin;
reg  okout;
reg  rst_n;
reg en;

always begin
    clk=0;
    #10;
    clk=1;
    #3;
    $python("negedge()");
    #7;
end
initial begin
    en = 0;
    rst_n = 0;
    clk = 0;
    msgin = 0;
    okout = 0;
    rst_n = 0;
    #100;
    rst_n=1;
    #100;
    en = 1;
end


wire [159:0] msg0;
wire ok0;
wire [9:0] busy;

integer idles; initial idles=0;
integer busies; initial busies=0;
always @(posedge clk) begin
    if (busy==0) idles <= idles + 1;
    else idles <= 0;
    busies <= busies + busy; 
end
wire finish_ok = (idles>1000) && (busies>100);
always @(posedge finish_ok) begin
    $display("finish on idles");
    $finish;
end

agent dut0 (
     .clk(clk)
    ,.localid(8'h50)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.msgin(msgin)
    ,.msgout(msg0)
    ,.okin(okin)
    ,.okout(ok0)
    ,.busy(busy[0])
);
wire [159:0] msg1;
wire ok1;
agent dut1 (
     .clk(clk)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.localid(8'h51)
    ,.msgin(msg0) ,.okin(ok0)
    ,.msgout(msg1) ,.okout(ok1)
    ,.busy(busy[1])
);
wire [159:0] msg2;
wire ok2;
agent dut2 (
     .clk(clk)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.localid(8'h52)
    ,.msgin(msg1) ,.okin(ok1)
    ,.msgout(msg2) ,.okout(ok2)
    ,.busy(busy[2])
);
wire [159:0] msg3;
wire ok3;
agent dut3 (
     .clk(clk)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.localid(8'h53)
    ,.msgin(msg2) ,.okin(ok2)
    ,.msgout(msg3) ,.okout(ok3)
    ,.busy(busy[3])
);
wire [159:0] msg4;
wire ok4;
agent dut4 (
     .clk(clk)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.localid(8'h54)
    ,.msgin(msg3) ,.okin(ok3)
    ,.msgout(msg4) ,.okout(ok4)
    ,.busy(busy[4])
);
wire [159:0] msg5;
wire ok5;
agent dut5 (
     .clk(clk)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.localid(8'h55)
    ,.msgin(msg4) ,.okin(ok4)
    ,.msgout(msg5) ,.okout(ok5)
    ,.busy(busy[5])
);
wire [159:0] msg6;
wire ok6;
agent dut6 (
     .clk(clk)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.localid(8'h56)
    ,.msgin(msg5) ,.okin(ok5)
    ,.msgout(msg6) ,.okout(ok6)
    ,.busy(busy[6])
);
wire [159:0] msg7;
wire ok7;
agent dut7 (
     .clk(clk)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.localid(8'h57)
    ,.msgin(msg6) ,.okin(ok6)
    ,.msgout(msg7) ,.okout(ok7)
    ,.busy(busy[7])
);
wire [159:0] msg8;
wire ok8;
agent dut8 (
     .clk(clk)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.localid(8'h58)
    ,.msgin(msg7) ,.okin(ok7)
    ,.msgout(msg8) ,.okout(ok8)
    ,.busy(busy[8])
);

agent dut9 (
     .clk(clk)
    ,.localid(8'h59)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.msgin(msg8)
    ,.msgout(msgout)
    ,.okin(ok8)
    ,.okout(okout)
    ,.busy(busy[9])
);
integer ccc=0;
always @(msgout) if (msgout[31:0]!=0) begin
    ccc = ccc + 1;
    $python("msgout()",msgout);
end



always @(posedge clk) okout <= msgout[31:0]!= 0;

reg [1023:0] testname,vcdfile;
initial begin
    if ($value$plusargs("LOG=%s",testname)) begin 
        $python("pymonname()",testname);
    end 

    if ($value$plusargs("PRM0=%s",testname)) begin 
        $sformat(vcdfile,"%s.vcd", testname);
        $dumpfile(vcdfile[8*6-1:0]);
        $dumpvars(0,tb);
        $python("parameter0()",testname);
    end
    if ($value$plusargs("PRM1=%s",testname)) begin 
        $python("parameter1()",testname);
    end

end 
endmodule

