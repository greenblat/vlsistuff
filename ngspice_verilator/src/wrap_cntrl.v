module wrap_cntrl (input incrdbg
  ,input  rst_n
  ,input  clk
  ,output  a0
  ,output  a1
  ,output  a2
  ,output  a3
  ,output [3:0] aa
  ,output reg [31:0] cycles
  ,output reg [31:0] errors
  ,output reg [31:0] wrongs
  ,output reg [31:0] panics
  ,output reg [31:0] corrects
  ,output reg [31:0] marker0
  ,output reg [31:0] marker1
  ,output reg [31:0] marker2
);
cntrl dut(
     .rst_n(rst_n)
    ,.clk(clk)
    ,.a0(a0)
    ,.a1(a1)
    ,.a2(a2)
    ,.a3(a3)
);
assign aa = dut.aa;

reg dbg;
always @(posedge clk) if (incrdbg) begin
    cycles <= cycles + 1;
    errors <= errors + cycles;
    wrongs <= wrongs + errors;
    panics <= panics + wrongs;
    corrects <= corrects + panics;
    marker0 <= marker0 + marker0;
    marker1 <= marker1 + marker1;
    marker2 <= marker2 + marker2;
    dbg <= |(cycles^errors^wrongs^panics^corrects^marker0^marker1^marker2);
end
endmodule
