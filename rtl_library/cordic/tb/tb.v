module tb;
reg [31:0] cycles;   initial cycles=0;
reg [31:0] errors;   initial errors=0;
reg [31:0] wrongs;   initial wrongs=0;
reg [31:0] panics;   initial panics=0;
reg [31:0] corrects; initial corrects=0;
reg [31:0] marker;   initial marker=0;
reg [31:0] Angle;   initial Angle=0;
parameter INWID = 20;
parameter MAX_SHIFT_COUNT = 16;
parameter OUWID = (INWID + 4);
parameter ANGWID = (INWID + 6);
reg [31:0] anglein;
wire [31:0] angleout;
reg  clk,rst_n;
wire  donepulse;
reg  startpulse;
reg  vector_mode;
reg [31:0] xin;
wire [31:0] xout;
reg [31:0] yin;
wire [31:0] yout;

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
    anglein = 0;
    clk = 0;
    rst_n = 0;
    startpulse = 0;
    vector_mode = 0;
    xin = 0;
    yin = 0;
    #100;
    rst_n=1;
end
cordic_generic dut (
     .anglein(anglein)
    ,.angleout(angleout)
    ,.clk(clk)
    ,.donepulse(donepulse)
    ,.rst_n(rst_n)
    ,.startpulse(startpulse)
    ,.vector_mode(vector_mode)
    ,.xin(xin)
    ,.xout(xout)
    ,.yin(yin)
    ,.yout(yout)
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
