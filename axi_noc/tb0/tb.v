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

reg [2:0] awsize; initial awsize=3;
reg [2:0] arsize; initial arsize=3;
reg [2:0] a_arsize; initial a_arsize=3;
reg [2:0] b_arsize; initial b_arsize=3;
reg [2:0] c_arsize; initial c_arsize=3;
reg [2:0] d_arsize; initial d_arsize=3;
reg [2:0] a_awsize; initial a_awsize=3;
reg [2:0] b_awsize; initial b_awsize=3;
reg [2:0] c_awsize; initial c_awsize=3;
reg [2:0] d_awsize; initial d_awsize=3;

parameter IDWID = 4;
parameter DWID = 64;
parameter WSTRB = (DWID / 8);
parameter EXTRAS = 8;
reg [31:0] a_araddr;
reg [1:0] a_arburst;
reg [(EXTRAS - 1):0] a_arextras;
reg [(IDWID - 1):0] a_arid;
reg [7:0] a_arlen;
wire  a_arready;
reg  a_arvalid;
reg [31:0] a_awaddr;
reg [1:0] a_awburst;
reg [(EXTRAS - 1):0] a_awextras;
reg [(IDWID - 1):0] a_awid;
reg [7:0] a_awlen;
wire  a_awready;
reg  a_awvalid;
wire [(IDWID - 1):0] a_bid;
reg  a_bready;
wire [1:0] a_bresp;
wire  a_bvalid;
wire [(DWID - 1):0] a_rdata;
wire [(IDWID - 1):0] a_rid;
wire  a_rlast;
reg  a_rready;
wire [1:0] a_rresp;
wire  a_rvalid;
reg [(DWID - 1):0] a_wdata;
reg  a_wlast;
wire  a_wready;
reg [(WSTRB - 1):0] a_wstrb;
reg  a_wvalid;
wire [31:0] araddr;
wire [1:0] arburst;
wire [(EXTRAS - 1):0] arextras;
wire [(IDWID - 1):0] arid;
wire [7:0] arlen;
reg  arready;
wire  arvalid;
wire [31:0] awaddr;
wire [1:0] awburst;
wire [(EXTRAS - 1):0] awextras;
wire [3:0] awid;
wire [7:0] awlen;
reg  awready;
wire  awvalid;
reg [31:0] b_araddr;
reg [1:0] b_arburst;
reg [(EXTRAS - 1):0] b_arextras;
reg [(IDWID - 1):0] b_arid;
reg [7:0] b_arlen;
wire  b_arready;
reg  b_arvalid;
reg [31:0] b_awaddr;
reg [1:0] b_awburst;
reg [(EXTRAS - 1):0] b_awextras;
reg [(IDWID - 1):0] b_awid;
reg [7:0] b_awlen;
wire  b_awready;
reg  b_awvalid;
wire [(IDWID - 1):0] b_bid;
reg  b_bready;
wire [1:0] b_bresp;
wire  b_bvalid;
wire [(DWID - 1):0] b_rdata;
wire [(IDWID - 1):0] b_rid;
wire  b_rlast;
reg  b_rready;
wire [1:0] b_rresp;
wire  b_rvalid;
reg [(DWID - 1):0] b_wdata;
reg  b_wlast;
wire  b_wready;
reg [(WSTRB - 1):0] b_wstrb;
reg  b_wvalid;
reg [(IDWID - 1):0] bid;
wire  bready;
reg [1:0] bresp;
reg  bvalid;
reg [31:0] c_araddr;
reg [1:0] c_arburst;
reg [(EXTRAS - 1):0] c_arextras;
reg [(IDWID - 1):0] c_arid;
reg [7:0] c_arlen;
wire  c_arready;
reg  c_arvalid;
reg [31:0] c_awaddr;
reg [1:0] c_awburst;
reg [(EXTRAS - 1):0] c_awextras;
reg [(IDWID - 1):0] c_awid;
reg [7:0] c_awlen;
wire  c_awready;
reg  c_awvalid;
wire [(IDWID - 1):0] c_bid;
reg  c_bready;
wire [1:0] c_bresp;
wire  c_bvalid;
wire [(DWID - 1):0] c_rdata;
wire [(IDWID - 1):0] c_rid;
wire  c_rlast;
reg  c_rready;
wire [1:0] c_rresp;
wire  c_rvalid;
reg [(DWID - 1):0] c_wdata;
reg  c_wlast;
wire  c_wready;
reg [(WSTRB - 1):0] c_wstrb;
reg  c_wvalid;
reg  clk;
reg [31:0] d_araddr;
reg [1:0] d_arburst;
reg [(EXTRAS - 1):0] d_arextras;
reg [(IDWID - 1):0] d_arid;
reg [7:0] d_arlen;
wire  d_arready;
reg  d_arvalid;
reg [31:0] d_awaddr;
reg [1:0] d_awburst;
reg [(EXTRAS - 1):0] d_awextras;
reg [(IDWID - 1):0] d_awid;
reg [7:0] d_awlen;
wire  d_awready;
reg  d_awvalid;
wire [(IDWID - 1):0] d_bid;
reg  d_bready;
wire [1:0] d_bresp;
wire  d_bvalid;
wire [(DWID - 1):0] d_rdata;
wire [(IDWID - 1):0] d_rid;
wire  d_rlast;
reg  d_rready;
wire [1:0] d_rresp;
wire  d_rvalid;
reg [(DWID - 1):0] d_wdata;
reg  d_wlast;
wire  d_wready;
reg [(WSTRB - 1):0] d_wstrb;
reg  d_wvalid;
reg [(DWID - 1):0] rdata;
reg [(IDWID - 1):0] rid;
reg  rlast;
wire  rready;
reg [1:0] rresp;
reg  rst_n;
reg  rvalid;
wire [(DWID - 1):0] wdata;
wire  wlast;
reg  wready;
wire [(WSTRB - 1):0] wstrb;
wire  wvalid;

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
    a_araddr = 0;
    a_arburst = 0;
    a_arextras = 0;
    a_arid = 0;
    a_arlen = 0;
    a_arvalid = 0;
    a_awaddr = 0;
    a_awburst = 0;
    a_awextras = 0;
    a_awid = 0;
    a_awlen = 0;
    a_awvalid = 0;
    a_bready = 0;
    a_rready = 0;
    a_wdata = 0;
    a_wlast = 0;
    a_wstrb = 0;
    a_wvalid = 0;
    arready = 0;
    awready = 0;
    b_araddr = 0;
    b_arburst = 0;
    b_arextras = 0;
    b_arid = 0;
    b_arlen = 0;
    b_arvalid = 0;
    b_awaddr = 0;
    b_awburst = 0;
    b_awextras = 0;
    b_awid = 0;
    b_awlen = 0;
    b_awvalid = 0;
    b_bready = 0;
    b_rready = 0;
    b_wdata = 0;
    b_wlast = 0;
    b_wstrb = 0;
    b_wvalid = 0;
    bid = 0;
    bresp = 0;
    bvalid = 0;
    c_araddr = 0;
    c_arburst = 0;
    c_arextras = 0;
    c_arid = 0;
    c_arlen = 0;
    c_arvalid = 0;
    c_awaddr = 0;
    c_awburst = 0;
    c_awextras = 0;
    c_awid = 0;
    c_awlen = 0;
    c_awvalid = 0;
    c_bready = 0;
    c_rready = 0;
    c_wdata = 0;
    c_wlast = 0;
    c_wstrb = 0;
    c_wvalid = 0;
    clk = 0;
    d_araddr = 0;
    d_arburst = 0;
    d_arextras = 0;
    d_arid = 0;
    d_arlen = 0;
    d_arvalid = 0;
    d_awaddr = 0;
    d_awburst = 0;
    d_awextras = 0;
    d_awid = 0;
    d_awlen = 0;
    d_awvalid = 0;
    d_bready = 0;
    d_rready = 0;
    d_wdata = 0;
    d_wlast = 0;
    d_wstrb = 0;
    d_wvalid = 0;
    rdata = 0;
    rid = 0;
    rlast = 0;
    rresp = 0;
    rst_n = 0;
    rvalid = 0;
    wready = 0;
    #100;
    rst_n=1;
end
axi_4_merger dut (
     .a_araddr(a_araddr[31:0])
    ,.a_arburst(a_arburst[1:0])
    ,.a_arextras(a_arextras[(EXTRAS - 1):0])
    ,.a_arid(a_arid[(IDWID - 1):0])
    ,.a_arlen(a_arlen[7:0])
    ,.a_arready(a_arready)
    ,.a_arvalid(a_arvalid)
    ,.a_awaddr(a_awaddr[31:0])
    ,.a_awburst(a_awburst[1:0])
    ,.a_awextras(a_awextras[(EXTRAS - 1):0])
    ,.a_awid(a_awid[(IDWID - 1):0])
    ,.a_awlen(a_awlen[7:0])
    ,.a_awready(a_awready)
    ,.a_awvalid(a_awvalid)
    ,.a_bid(a_bid[(IDWID - 1):0])
    ,.a_bready(a_bready)
    ,.a_bresp(a_bresp[1:0])
    ,.a_bvalid(a_bvalid)
    ,.a_rdata(a_rdata[(DWID - 1):0])
    ,.a_rid(a_rid[(IDWID - 1):0])
    ,.a_rlast(a_rlast)
    ,.a_rready(a_rready)
    ,.a_rresp(a_rresp[1:0])
    ,.a_rvalid(a_rvalid)
    ,.a_wdata(a_wdata[(DWID - 1):0])
    ,.a_wlast(a_wlast)
    ,.a_wready(a_wready)
    ,.a_wstrb(a_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(a_wvalid)
    ,.araddr(araddr[31:0])
    ,.arburst(arburst[1:0])
    ,.arextras(arextras[(EXTRAS - 1):0])
    ,.arid(arid[(IDWID - 1):0])
    ,.arlen(arlen[7:0])
    ,.arready(arready)
    ,.arvalid(arvalid)
    ,.awaddr(awaddr[31:0])
    ,.awburst(awburst[1:0])
    ,.awextras(awextras[(EXTRAS - 1):0])
    ,.awid(awid[3:0])
    ,.awlen(awlen[7:0])
    ,.awready(awready)
    ,.awvalid(awvalid)
    ,.b_araddr(b_araddr[31:0])
    ,.b_arburst(b_arburst[1:0])
    ,.b_arextras(b_arextras[(EXTRAS - 1):0])
    ,.b_arid(b_arid[(IDWID - 1):0])
    ,.b_arlen(b_arlen[7:0])
    ,.b_arready(b_arready)
    ,.b_arvalid(b_arvalid)
    ,.b_awaddr(b_awaddr[31:0])
    ,.b_awburst(b_awburst[1:0])
    ,.b_awextras(b_awextras[(EXTRAS - 1):0])
    ,.b_awid(b_awid[(IDWID - 1):0])
    ,.b_awlen(b_awlen[7:0])
    ,.b_awready(b_awready)
    ,.b_awvalid(b_awvalid)
    ,.b_bid(b_bid[(IDWID - 1):0])
    ,.b_bready(b_bready)
    ,.b_bresp(b_bresp[1:0])
    ,.b_bvalid(b_bvalid)
    ,.b_rdata(b_rdata[(DWID - 1):0])
    ,.b_rid(b_rid[(IDWID - 1):0])
    ,.b_rlast(b_rlast)
    ,.b_rready(b_rready)
    ,.b_rresp(b_rresp[1:0])
    ,.b_rvalid(b_rvalid)
    ,.b_wdata(b_wdata[(DWID - 1):0])
    ,.b_wlast(b_wlast)
    ,.b_wready(b_wready)
    ,.b_wstrb(b_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(b_wvalid)
    ,.bid(bid[(IDWID - 1):0])
    ,.bready(bready)
    ,.bresp(bresp[1:0])
    ,.bvalid(bvalid)
    ,.c_araddr(c_araddr[31:0])
    ,.c_arburst(c_arburst[1:0])
    ,.c_arextras(c_arextras[(EXTRAS - 1):0])
    ,.c_arid(c_arid[(IDWID - 1):0])
    ,.c_arlen(c_arlen[7:0])
    ,.c_arready(c_arready)
    ,.c_arvalid(c_arvalid)
    ,.c_awaddr(c_awaddr[31:0])
    ,.c_awburst(c_awburst[1:0])
    ,.c_awextras(c_awextras[(EXTRAS - 1):0])
    ,.c_awid(c_awid[(IDWID - 1):0])
    ,.c_awlen(c_awlen[7:0])
    ,.c_awready(c_awready)
    ,.c_awvalid(c_awvalid)
    ,.c_bid(c_bid[(IDWID - 1):0])
    ,.c_bready(c_bready)
    ,.c_bresp(c_bresp[1:0])
    ,.c_bvalid(c_bvalid)
    ,.c_rdata(c_rdata[(DWID - 1):0])
    ,.c_rid(c_rid[(IDWID - 1):0])
    ,.c_rlast(c_rlast)
    ,.c_rready(c_rready)
    ,.c_rresp(c_rresp[1:0])
    ,.c_rvalid(c_rvalid)
    ,.c_wdata(c_wdata[(DWID - 1):0])
    ,.c_wlast(c_wlast)
    ,.c_wready(c_wready)
    ,.c_wstrb(c_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(c_wvalid)
    ,.clk(clk)
    ,.d_araddr(d_araddr[31:0])
    ,.d_arburst(d_arburst[1:0])
    ,.d_arextras(d_arextras[(EXTRAS - 1):0])
    ,.d_arid(d_arid[(IDWID - 1):0])
    ,.d_arlen(d_arlen[7:0])
    ,.d_arready(d_arready)
    ,.d_arvalid(d_arvalid)
    ,.d_awaddr(d_awaddr[31:0])
    ,.d_awburst(d_awburst[1:0])
    ,.d_awextras(d_awextras[(EXTRAS - 1):0])
    ,.d_awid(d_awid[(IDWID - 1):0])
    ,.d_awlen(d_awlen[7:0])
    ,.d_awready(d_awready)
    ,.d_awvalid(d_awvalid)
    ,.d_bid(d_bid[(IDWID - 1):0])
    ,.d_bready(d_bready)
    ,.d_bresp(d_bresp[1:0])
    ,.d_bvalid(d_bvalid)
    ,.d_rdata(d_rdata[(DWID - 1):0])
    ,.d_rid(d_rid[(IDWID - 1):0])
    ,.d_rlast(d_rlast)
    ,.d_rready(d_rready)
    ,.d_rresp(d_rresp[1:0])
    ,.d_rvalid(d_rvalid)
    ,.d_wdata(d_wdata[(DWID - 1):0])
    ,.d_wlast(d_wlast)
    ,.d_wready(d_wready)
    ,.d_wstrb(d_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(d_wvalid)
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


