`timescale 1ns/1ps
module tb;
integer    cycles;   initial cycles=0;
reg  clk;
reg [135:0] msg_msgin;
reg [135:0] msgin;
wire [135:0] msgout;
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
    msg_msgin = 0;
    okout = 0;
    rst_n = 0;
    #100;
    rst_n=1;
    en=1;
end


wire [135:0] msg0;
wire ok0;

always @(negedge clk) begin
    if (msg_msgin != msgin) begin
        msgin <= msg_msgin;
    end else begin
        msg_msgin <= 0;
        msgin <= 0;
    end
end

agent dut0 (
     .clk(clk)
    ,.localid(8'h50)
    ,.last_one(1'b0)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.msgin(msgin)
    ,.msgout(msg0)
    ,.okin(okin)
    ,.okout(ok0)
);
wire [135:0] msg1;
wire ok1;
agent dut1 (
     .clk(clk)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.last_one(1'b0)
    ,.localid(8'h51)
    ,.msgin(msg0) ,.okin(ok0)
    ,.msgout(msg1) ,.okout(ok1)
);
wire [135:0] msg2;
wire ok2;
agent dut2 (
     .clk(clk)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.last_one(1'b0)
    ,.localid(8'h52)
    ,.msgin(msg1) ,.okin(ok1)
    ,.msgout(msg2) ,.okout(ok2)
);
wire [135:0] msg3;
wire ok3;
agent dut3 (
     .clk(clk)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.last_one(1'b0)
    ,.localid(8'h53)
    ,.msgin(msg2) ,.okin(ok2)
    ,.msgout(msg3) ,.okout(ok3)
);
wire [135:0] msg4;
wire ok4;
agent dut4 (
     .clk(clk)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.last_one(1'b0)
    ,.localid(8'h54)
    ,.msgin(msg3) ,.okin(ok3)
    ,.msgout(msg4) ,.okout(ok4)
);
wire [135:0] msg5;
wire ok5;
agent dut5 (
     .clk(clk)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.last_one(1'b0)
    ,.localid(8'h55)
    ,.msgin(msg4) ,.okin(ok4)
    ,.msgout(msg5) ,.okout(ok5)
);
wire [135:0] msg6;
wire ok6;
agent dut6 (
     .clk(clk)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.last_one(1'b0)
    ,.localid(8'h56)
    ,.msgin(msg5) ,.okin(ok5)
    ,.msgout(msg6) ,.okout(ok6)
);
wire [135:0] msg7;
wire ok7;
agent dut7 (
     .clk(clk)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.last_one(1'b0)
    ,.localid(8'h57)
    ,.msgin(msg6) ,.okin(ok6)
    ,.msgout(msg7) ,.okout(ok7)
);
wire [135:0] msg8;
wire ok8;
agent dut8 (
     .clk(clk)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.last_one(1'b0)
    ,.localid(8'h58)
    ,.msgin(msg7) ,.okin(ok7)
    ,.msgout(msg8) ,.okout(ok8)
);

agent dut9 (
     .clk(clk)
    ,.localid(8'h59)
    ,.last_one(1'b1)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.msgin(msg8)
    ,.msgout(msgout)
    ,.okin(ok8)
    ,.okout(okout)
);


reg [1023:0] testname;
reg [8*6-1:0] vcdname;
initial begin
    if ($value$plusargs("PRM0=%s",testname)) begin 
        $python("parameter0()",testname);
        $sformat(vcdname,"%s.vcd",testname[15:0]);
        $display(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> %s ",vcdname,vcdname);
        $dumpfile(vcdname);
        $dumpvars(0,tb);
    end 
    if ($value$plusargs("PRM1=%s",testname)) begin 
        $python("parameter1()",testname);
    end 


end 
endmodule

