


`define BW  63


module color #(parameter COLOR="",parameter CLOCK="",parameter REFCLOCK="")(
    input [`BW:0] in0
    ,output reg [`BW:0] out0
);

reg [31:0] base; 
reg [2047:0] path;
initial begin
    $sformat(path,"%m");
    base = 0;
    $python("colorinit()",path);
end

always @in0 begin
    $python("colorrun()",base,in0);
end

wire [1023:0] color = COLOR;
wire [1023:0] clock = CLOCK;
wire [1023:0] refclock = REFCLOCK;

endmodule

module flop ( input [`BW:0] dd, input [`BW:0] clk, output reg [`BW:0] qq);

reg [31:0] base; 
reg [2047:0] path;
initial begin
    base = 0;
    $sformat(path,"%m");
    $python("flopinit()",path);
end

always @(clk) begin
    $python("floprun()",base,1,clk);
end
always @(dd) begin
    $python("floprun()",base,0,dd);
end

endmodule

module blob #(parameter FUNC="") ( 
     input [`BW:0] in0
    ,input [`BW:0] in1
    ,input [`BW:0] in2
    ,input [`BW:0] in3
    ,input [`BW:0] in4
    ,input [`BW:0] in5
    ,input [`BW:0] in6
    ,input [`BW:0] in7
    ,input [`BW:0] in8
    ,input [`BW:0] in9
    ,output reg [`BW:0] out0
);

wire [2047:0] func = FUNC;
reg [31:0] base; 
reg [2047:0] path;
initial begin
    base = 0;
    $sformat(path,"%m");
    $python("blobinit()",path);
end
always @(in0) $python("blobrun()",base,0,in0);
always @(in1) $python("blobrun()",base,1,in1);
always @(in2) $python("blobrun()",base,2,in2);
always @(in3) $python("blobrun()",base,3,in3);
always @(in4) $python("blobrun()",base,4,in4);
always @(in5) $python("blobrun()",base,5,in4);
always @(in6) $python("blobrun()",base,6,in4);
always @(in7) $python("blobrun()",base,7,in4);
always @(in8) $python("blobrun()",base,8,in4);
always @(in9) $python("blobrun()",base,9,in4);


endmodule

