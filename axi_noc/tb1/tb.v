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





parameter EXTRAS = 8;
parameter IDWID = 4;
parameter DWID = 64;
parameter WSTRB = (DWID / 8);
wire [31:0] a_araddr;
wire [1:0] a_arburst;
wire [(EXTRAS - 1):0] a_arextras;
wire [(IDWID - 1):0] a_arid;
wire [7:0] a_arlen;
reg  a_arready;
wire  a_arvalid;
wire [31:0] a_awaddr;
wire [1:0] a_awburst;
wire [(EXTRAS - 1):0] a_awextras;
wire [(IDWID - 1):0] a_awid;
wire [7:0] a_awlen;
reg  a_awready;
wire  a_awvalid;
reg [(IDWID - 1):0] a_bid;
wire  a_bready;
reg [1:0] a_bresp;
reg  a_bvalid;
reg [(DWID - 1):0] a_rdata;
reg [(IDWID - 1):0] a_rid;
reg  a_rlast;
wire  a_rready;
reg [1:0] a_rresp;
reg  a_rvalid;
wire [(DWID - 1):0] a_wdata;
wire  a_wlast;
reg  a_wready;
wire [(WSTRB - 1):0] a_wstrb;
wire  a_wvalid;
reg [31:0] araddr;
reg [1:0] arburst;
reg [(EXTRAS - 1):0] arextras;
reg [(IDWID - 1):0] arid;
reg [7:0] arlen;
wire  arready;
reg  arvalid;
reg [31:0] awaddr;
reg [1:0] awburst;
reg [(EXTRAS - 1):0] awextras;
reg [3:0] awid;
reg [7:0] awlen;
wire  awready;
reg  awvalid;
wire [31:0] b_araddr;
wire [1:0] b_arburst;
wire [(EXTRAS - 1):0] b_arextras;
wire [(IDWID - 1):0] b_arid;
wire [7:0] b_arlen;
reg  b_arready;
wire  b_arvalid;
wire [31:0] b_awaddr;
wire [1:0] b_awburst;
wire [(EXTRAS - 1):0] b_awextras;
wire [(IDWID - 1):0] b_awid;
wire [7:0] b_awlen;
reg  b_awready;
wire  b_awvalid;
reg [(IDWID - 1):0] b_bid;
wire  b_bready;
reg [1:0] b_bresp;
reg  b_bvalid;
reg [(DWID - 1):0] b_rdata;
reg [(IDWID - 1):0] b_rid;
reg  b_rlast;
wire  b_rready;
reg [1:0] b_rresp;
reg  b_rvalid;
wire [(DWID - 1):0] b_wdata;
wire  b_wlast;
reg  b_wready;
wire [(WSTRB - 1):0] b_wstrb;
wire  b_wvalid;
wire [(IDWID - 1):0] bid;
reg  bready;
wire [1:0] bresp;
wire  bvalid;
wire [31:0] c_araddr;
wire [1:0] c_arburst;
wire [(EXTRAS - 1):0] c_arextras;
wire [(IDWID - 1):0] c_arid;
wire [7:0] c_arlen;
reg  c_arready;
wire  c_arvalid;
wire [31:0] c_awaddr;
wire [1:0] c_awburst;
wire [(EXTRAS - 1):0] c_awextras;
wire [(IDWID - 1):0] c_awid;
wire [7:0] c_awlen;
reg  c_awready;
wire  c_awvalid;
reg [(IDWID - 1):0] c_bid;
wire  c_bready;
reg [1:0] c_bresp;
reg  c_bvalid;
reg [(DWID - 1):0] c_rdata;
reg [(IDWID - 1):0] c_rid;
reg  c_rlast;
wire  c_rready;
reg [1:0] c_rresp;
reg  c_rvalid;
wire [(DWID - 1):0] c_wdata;
wire  c_wlast;
reg  c_wready;
wire [(WSTRB - 1):0] c_wstrb;
wire  c_wvalid;
reg  clk;
wire [31:0] d_araddr;
wire [1:0] d_arburst;
wire [(EXTRAS - 1):0] d_arextras;
wire [(IDWID - 1):0] d_arid;
wire [7:0] d_arlen;
reg  d_arready;
wire  d_arvalid;
wire [31:0] d_awaddr;
wire [1:0] d_awburst;
wire [(EXTRAS - 1):0] d_awextras;
wire [(IDWID - 1):0] d_awid;
wire [7:0] d_awlen;
reg  d_awready;
wire  d_awvalid;
reg [(IDWID - 1):0] d_bid;
wire  d_bready;
reg [1:0] d_bresp;
reg  d_bvalid;
reg [(DWID - 1):0] d_rdata;
reg [(IDWID - 1):0] d_rid;
reg  d_rlast;
wire  d_rready;
reg [1:0] d_rresp;
reg  d_rvalid;
wire [(DWID - 1):0] d_wdata;
wire  d_wlast;
reg  d_wready;
wire [(WSTRB - 1):0] d_wstrb;
wire  d_wvalid;
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
    a_arready = 0;
    a_awready = 0;
    a_bid = 0;
    a_bresp = 0;
    a_bvalid = 0;
    a_rdata = 0;
    a_rid = 0;
    a_rlast = 0;
    a_rresp = 0;
    a_rvalid = 0;
    a_wready = 0;
    araddr = 0;
    arburst = 0;
    arextras = 0;
    arid = 0;
    arlen = 0;
    arvalid = 0;
    awaddr = 0;
    awburst = 0;
    awextras = 0;
    awid = 0;
    awlen = 0;
    awvalid = 0;
    b_arready = 0;
    b_awready = 0;
    b_bid = 0;
    b_bresp = 0;
    b_bvalid = 0;
    b_rdata = 0;
    b_rid = 0;
    b_rlast = 0;
    b_rresp = 0;
    b_rvalid = 0;
    b_wready = 0;
    bready = 0;
    c_arready = 0;
    c_awready = 0;
    c_bid = 0;
    c_bresp = 0;
    c_bvalid = 0;
    c_rdata = 0;
    c_rid = 0;
    c_rlast = 0;
    c_rresp = 0;
    c_rvalid = 0;
    c_wready = 0;
    clk = 0;
    d_arready = 0;
    d_awready = 0;
    d_bid = 0;
    d_bresp = 0;
    d_bvalid = 0;
    d_rdata = 0;
    d_rid = 0;
    d_rlast = 0;
    d_rresp = 0;
    d_rvalid = 0;
    d_wready = 0;
    rready = 0;
    rst_n = 0;
    wdata = 0;
    wlast = 0;
    wstrb = 0;
    wvalid = 0;
    #100;
    rst_n=1;
end
axi_4_splitter dut (
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


module inout_driver ( inout io , input dflt );

reg val; initial val=0;
reg drive; initial drive=0;
assign io = drive ? val : 1'bz;
assign (pull1,pull0) io = dflt;

endmodule
