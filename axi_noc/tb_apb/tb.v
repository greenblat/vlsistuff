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
parameter IDWID = 4;
parameter DWID = 64;
parameter WSTRB = (DWID / 8);
reg [31:0] araddr;
reg [1:0] arburst;
reg [3:0] arcache;
reg [(IDWID - 1):0] arid;
reg [7:0] arlen;
reg [2:0] arprot;
reg [3:0] arqos;
wire  arready;
reg [2:0] arsize;
reg  arvalid;
reg [31:0] awaddr;
reg [1:0] awburst;
reg [3:0] awcache;
reg [3:0] awid;
reg [7:0] awlen;
reg [2:0] awprot;
reg [3:0] awqos;
wire  awready;
reg [2:0] awsize;
reg  awvalid;
wire [(IDWID - 1):0] bid;
reg  bready;
wire [1:0] bresp;
wire  bvalid;
reg  clk;
wire [31:0] paddr;
wire  penable;
wire [31:0] prdata;
reg  pready;
reg [1:0] presp;
wire  psel;
wire [3:0] pstrb;
wire [31:0] pwdata;
wire  pwrite;
wire [(DWID - 1):0] rdata;
wire [(IDWID - 1):0] rid;
wire  rlast;
reg  rready;
wire [1:0] rresp;
reg  rst_n;
wire  rvalid;
reg [(DWID - 1):0] wdata;
reg  wlast;
wire  wready;
reg [(WSTRB - 1):0] wstrb;
reg  wvalid;

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
    araddr = 0;
    arburst = 0;
    arcache = 0;
    arid = 0;
    arlen = 0;
    arprot = 0;
    arqos = 0;
    arsize = 0;
    arvalid = 0;
    awaddr = 0;
    awburst = 0;
    awcache = 0;
    awid = 0;
    awlen = 0;
    awprot = 0;
    awqos = 0;
    awsize = 0;
    awvalid = 0;
    bready = 0;
    clk = 0;
    presp = 0;
    rready = 0;
    rst_n = 0;
    wdata = 0;
    wlast = 0;
    wstrb = 0;
    wvalid = 0;
    #100;
    rst_n=1;
end
axi2apb dut (
     .araddr(araddr[31:0])
    ,.arburst(arburst[1:0])
    ,.arcache(arcache[3:0])
    ,.arid(arid[(IDWID - 1):0])
    ,.arlen(arlen[7:0])
    ,.arprot(arprot[2:0])
    ,.arqos(arqos[3:0])
    ,.arready(arready)
    ,.arsize(arsize[2:0])
    ,.arvalid(arvalid)
    ,.awaddr(awaddr[31:0])
    ,.awburst(awburst[1:0])
    ,.awcache(awcache[3:0])
    ,.awid(awid[3:0])
    ,.awlen(awlen[7:0])
    ,.awprot(awprot[2:0])
    ,.awqos(awqos[3:0])
    ,.awready(awready)
    ,.awsize(awsize[2:0])
    ,.awvalid(awvalid)
    ,.bid(bid[(IDWID - 1):0])
    ,.bready(bready)
    ,.bresp(bresp[1:0])
    ,.bvalid(bvalid)
    ,.clk(clk)
    ,.paddr(paddr[31:0])
    ,.penable(penable)
    ,.prdata(prdata[31:0])
    ,.pready(pready)
    ,.presp(presp[1:0])
    ,.psel(psel)
    ,.pstrb(pstrb[3:0])
    ,.pwdata(pwdata[31:0])
    ,.pwrite(pwrite)
    ,.rdata(rdata[(DWID - 1):0])
    ,.rid(rid[(IDWID - 1):0])
    ,.rlast(rlast)
    ,.rready(rready)
    ,.rresp(rresp[1:0])
    ,.rst_n(rst_n)
    ,.rvalid(rvalid)
    ,.wdata(wdata[(DWID - 1):0])
    ,.wlast(wlast)
    ,.wready(wready)
    ,.wstrb(wstrb[(WSTRB - 1):0])
    ,.wvalid(wvalid)
);


wire [127:0] key0;
wire [127:0] key1;
wire [7:0][19:0] limits0;
wire [7:0][19:0] limits1;

demo rgf (
     .pclk(clk) ,.presetn(rst_n)

    ,.key0(key0[127:0])
    ,.key1(key1[127:0])
    ,.limits0(limits0)
    ,.limits1(limits1)
    ,.paddr(paddr[19:0])
    ,.penable(penable)
    ,.prdata(prdata[31:0])
    ,.prdata_wire()
    ,.pready(pready)
    ,.psel(psel)
    ,.pslverr()
    ,.pstrb(pstrb[3:0])
    ,.pwdata(pwdata[31:0])
    ,.pwrite(pwrite)
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

