module tb (input incrdbg
  ,input  clk
  ,input  rst_n
  ,input  rxd
  ,output  txd
  ,output [15:0] baudrate
  ,output [7:0] fractional
  ,output [15:0] txcount
  ,output  softreset
  ,output  tx_empty
  ,output  write_tx
  ,output [7:0] control
  ,output [7:0] rxdata
  ,output [7:0] txdata
  ,output [31:0] result
  ,output  vldout
  ,output [7:0] status
  ,output  rx_valid
  ,output [7:0] dst
  ,output [7:0] letA
  ,output [7:0] letB
  ,output [7:0] letC
  ,output [7:0] letD
  ,output [7:0] letE
  ,output [7:0] letF
  ,output [7:0] letG
  ,output [7:0] letH
  ,output [7:0] letI
  ,output [7:0] letJ
  ,output [7:0] letK
  ,output [7:0] letL
  ,output [7:0] letM
  ,output [7:0] letN
  ,output [7:0] letO
  ,output [7:0] letP
  ,output [7:0] letQ
  ,output [7:0] letR
  ,output [7:0] letS
  ,output [7:0] letT
  ,output [7:0] letU
  ,output [7:0] letV
  ,output [7:0] letW
  ,output [7:0] letX
  ,output [7:0] letY
  ,output [7:0] letZ
  ,output [7:0] letCR
  ,output [7:0] let0
  ,output [7:0] let1
  ,output [7:0] let2
  ,output [7:0] let3
  ,output [7:0] let4
  ,output [7:0] let5
  ,output [7:0] let6
  ,output [7:0] let7
  ,output [7:0] let8
  ,output [7:0] let9
  ,output [3:0] reads
  ,output  writes
  ,output [15:0] count
  ,output [15:0] frees
  ,output [79:0] dout
  ,output  taken
  ,output  wr_baudrate
  ,output  wr_fractional
  ,output  wr_reg
  ,output  rd_reg
  ,output  work
  ,output  pop
  ,output  clean
  ,output [31:0] reg0
  ,output [31:0] reg1
  ,output [31:0] reg2
  ,output [31:0] reg3
  ,output [31:0] reg4
  ,output [31:0] reg5
  ,output [31:0] reg6
  ,output [31:0] reg7
  ,output [31:0] fvalue
  ,output [7:0] AA
  ,output [7:0] BB
  ,output [7:0] CC
  ,output [3:0] oper
  ,output [7:0] sel0
  ,output [7:0] sel1
  ,output [7:0] dst_wire
  ,output [31:0] src0
  ,output [31:0] src1
  ,output [63:0] resultout
  ,output [15:0] txfrees
  ,output  txtaken
  ,output [31:0] selected_reg
  ,output [63:0] selected_hex
  ,output [3:0] txwrites
  ,output reg [31:0] cycles
  ,output reg [31:0] errors
  ,output reg [31:0] wrongs
  ,output reg [31:0] panics
  ,output reg [31:0] corrects
  ,output reg [31:0] marker0
  ,output reg [31:0] marker1
  ,output reg [31:0] marker2
);
fltserver dut(
     .clk(clk)
    ,.rst_n(rst_n)
    ,.rxd(rxd)
    ,.txd(txd)
);
assign baudrate = dut.baudrate;
assign fractional = dut.fractional;
assign txcount = dut.txcount;
assign softreset = dut.softreset;
assign tx_empty = dut.tx_empty;
assign write_tx = dut.write_tx;
assign control = dut.control;
assign rxdata = dut.rxdata;
assign txdata = dut.txdata;
assign result = dut.result;
assign vldout = dut.vldout;
assign status = dut.status;
assign rx_valid = dut.rx_valid;
assign dst = dut.dst;
assign letA = dut.letA;
assign letB = dut.letB;
assign letC = dut.letC;
assign letD = dut.letD;
assign letE = dut.letE;
assign letF = dut.letF;
assign letG = dut.letG;
assign letH = dut.letH;
assign letI = dut.letI;
assign letJ = dut.letJ;
assign letK = dut.letK;
assign letL = dut.letL;
assign letM = dut.letM;
assign letN = dut.letN;
assign letO = dut.letO;
assign letP = dut.letP;
assign letQ = dut.letQ;
assign letR = dut.letR;
assign letS = dut.letS;
assign letT = dut.letT;
assign letU = dut.letU;
assign letV = dut.letV;
assign letW = dut.letW;
assign letX = dut.letX;
assign letY = dut.letY;
assign letZ = dut.letZ;
assign letCR = dut.letCR;
assign let0 = dut.let0;
assign let1 = dut.let1;
assign let2 = dut.let2;
assign let3 = dut.let3;
assign let4 = dut.let4;
assign let5 = dut.let5;
assign let6 = dut.let6;
assign let7 = dut.let7;
assign let8 = dut.let8;
assign let9 = dut.let9;
assign reads = dut.reads;
assign writes = dut.writes;
assign count = dut.count;
assign frees = dut.frees;
assign dout = dut.dout;
assign taken = dut.taken;
assign wr_baudrate = dut.wr_baudrate;
assign wr_fractional = dut.wr_fractional;
assign wr_reg = dut.wr_reg;
assign rd_reg = dut.rd_reg;
assign work = dut.work;
assign pop = dut.pop;
assign clean = dut.clean;
assign reg0 = dut.reg0;
assign reg1 = dut.reg1;
assign reg2 = dut.reg2;
assign reg3 = dut.reg3;
assign reg4 = dut.reg4;
assign reg5 = dut.reg5;
assign reg6 = dut.reg6;
assign reg7 = dut.reg7;
assign fvalue = dut.fvalue;
assign AA = dut.AA;
assign BB = dut.BB;
assign CC = dut.CC;
assign oper = dut.oper;
assign sel0 = dut.sel0;
assign sel1 = dut.sel1;
assign dst_wire = dut.dst_wire;
assign src0 = dut.src0;
assign src1 = dut.src1;
assign resultout = dut.resultout;
assign txfrees = dut.txfrees;
assign txtaken = dut.txtaken;
assign selected_reg = dut.selected_reg;
assign selected_hex = dut.selected_hex;
assign txwrites = dut.txwrites;

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
