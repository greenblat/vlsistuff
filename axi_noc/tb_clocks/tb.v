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
parameter EXTRAS = 8;
parameter WSTRB = (DWID / 8);
reg  clk;
reg  clock0;
reg  clock1;
reg [31:0] mst0_araddr;
reg [1:0] mst0_arburst;
reg [(EXTRAS - 1):0] mst0_arextras;
reg [(IDWID - 1):0] mst0_arid;
reg [7:0] mst0_arlen;
wire  mst0_arready;
reg  mst0_arvalid;
reg [31:0] mst0_awaddr;
reg [1:0] mst0_awburst;
reg [(EXTRAS - 1):0] mst0_awextras;
reg [(IDWID - 1):0] mst0_awid;
reg [7:0] mst0_awlen;
wire  mst0_awready;
reg  mst0_awvalid;
wire [(IDWID - 1):0] mst0_bid;
reg  mst0_bready;
wire [1:0] mst0_bresp;
wire  mst0_bvalid;
wire [(DWID - 1):0] mst0_rdata;
wire [(IDWID - 1):0] mst0_rid;
wire  mst0_rlast;
reg  mst0_rready;
wire [1:0] mst0_rresp;
wire  mst0_rvalid;
reg [(DWID - 1):0] mst0_wdata;
reg  mst0_wlast;
wire  mst0_wready;
reg [(WSTRB - 1):0] mst0_wstrb;
reg  mst0_wvalid;
reg  rst_n;
wire [31:0] slv0_araddr;
wire [1:0] slv0_arburst;
wire [(EXTRAS - 1):0] slv0_arextras;
wire [(IDWID - 1):0] slv0_arid;
wire [7:0] slv0_arlen;
reg  slv0_arready;
wire  slv0_arvalid;
wire [31:0] slv0_awaddr;
wire [1:0] slv0_awburst;
wire [(EXTRAS - 1):0] slv0_awextras;
wire [(IDWID - 1):0] slv0_awid;
wire [7:0] slv0_awlen;
reg  slv0_awready;
wire  slv0_awvalid;
reg [(IDWID - 1):0] slv0_bid;
wire  slv0_bready;
reg [1:0] slv0_bresp;
reg  slv0_bvalid;
reg [(DWID - 1):0] slv0_rdata;
reg [(IDWID - 1):0] slv0_rid;
reg  slv0_rlast;
wire  slv0_rready;
reg [1:0] slv0_rresp;
reg  slv0_rvalid;
wire [(DWID - 1):0] slv0_wdata;
wire  slv0_wlast;
reg  slv0_wready;
wire [(WSTRB - 1):0] slv0_wstrb;
wire  slv0_wvalid;
wire [31:0] slv1_araddr;
wire [1:0] slv1_arburst;
wire [(EXTRAS - 1):0] slv1_arextras;
wire [(IDWID - 1):0] slv1_arid;
wire [7:0] slv1_arlen;
reg  slv1_arready;
wire  slv1_arvalid;
wire [31:0] slv1_awaddr;
wire [1:0] slv1_awburst;
wire [(EXTRAS - 1):0] slv1_awextras;
wire [(IDWID - 1):0] slv1_awid;
wire [7:0] slv1_awlen;
reg  slv1_awready;
wire  slv1_awvalid;
reg [(IDWID - 1):0] slv1_bid;
wire  slv1_bready;
reg [1:0] slv1_bresp;
reg  slv1_bvalid;
reg [(DWID - 1):0] slv1_rdata;
reg [(IDWID - 1):0] slv1_rid;
reg  slv1_rlast;
wire  slv1_rready;
reg [1:0] slv1_rresp;
reg  slv1_rvalid;
wire [(DWID - 1):0] slv1_wdata;
wire  slv1_wlast;
reg  slv1_wready;
wire [(WSTRB - 1):0] slv1_wstrb;
wire  slv1_wvalid;
wire [31:0] slv2_araddr;
wire [1:0] slv2_arburst;
wire [(EXTRAS - 1):0] slv2_arextras;
wire [(IDWID - 1):0] slv2_arid;
wire [7:0] slv2_arlen;
reg  slv2_arready;
wire  slv2_arvalid;
wire [31:0] slv2_awaddr;
wire [1:0] slv2_awburst;
wire [(EXTRAS - 1):0] slv2_awextras;
wire [(IDWID - 1):0] slv2_awid;
wire [7:0] slv2_awlen;
reg  slv2_awready;
wire  slv2_awvalid;
reg [(IDWID - 1):0] slv2_bid;
wire  slv2_bready;
reg [1:0] slv2_bresp;
reg  slv2_bvalid;
reg [(DWID - 1):0] slv2_rdata;
reg [(IDWID - 1):0] slv2_rid;
reg  slv2_rlast;
wire  slv2_rready;
reg [1:0] slv2_rresp;
reg  slv2_rvalid;
wire [(DWID - 1):0] slv2_wdata;
wire  slv2_wlast;
reg  slv2_wready;
wire [(WSTRB - 1):0] slv2_wstrb;
wire  slv2_wvalid;
wire [31:0] slv3_araddr;
wire [1:0] slv3_arburst;
wire [(EXTRAS - 1):0] slv3_arextras;
wire [(IDWID - 1):0] slv3_arid;
wire [7:0] slv3_arlen;
reg  slv3_arready;
wire  slv3_arvalid;
wire [31:0] slv3_awaddr;
wire [1:0] slv3_awburst;
wire [(EXTRAS - 1):0] slv3_awextras;
wire [(IDWID - 1):0] slv3_awid;
wire [7:0] slv3_awlen;
reg  slv3_awready;
wire  slv3_awvalid;
reg [(IDWID - 1):0] slv3_bid;
wire  slv3_bready;
reg [1:0] slv3_bresp;
reg  slv3_bvalid;
reg [(DWID - 1):0] slv3_rdata;
reg [(IDWID - 1):0] slv3_rid;
reg  slv3_rlast;
wire  slv3_rready;
reg [1:0] slv3_rresp;
reg  slv3_rvalid;
wire [(DWID - 1):0] slv3_wdata;
wire  slv3_wlast;
reg  slv3_wready;
wire [(WSTRB - 1):0] slv3_wstrb;
wire  slv3_wvalid;

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
    clk = 0;
    clock0 = 0;
    clock1 = 0;
    mst0_araddr = 0;
    mst0_arburst = 0;
    mst0_arextras = 0;
    mst0_arid = 0;
    mst0_arlen = 0;
    mst0_arvalid = 0;
    mst0_awaddr = 0;
    mst0_awburst = 0;
    mst0_awextras = 0;
    mst0_awid = 0;
    mst0_awlen = 0;
    mst0_awvalid = 0;
    mst0_bready = 0;
    mst0_rready = 0;
    mst0_wdata = 0;
    mst0_wlast = 0;
    mst0_wstrb = 0;
    mst0_wvalid = 0;
    rst_n = 0;
    slv0_arready = 0;
    slv0_awready = 0;
    slv0_bid = 0;
    slv0_bresp = 0;
    slv0_bvalid = 0;
    slv0_rdata = 0;
    slv0_rid = 0;
    slv0_rlast = 0;
    slv0_rresp = 0;
    slv0_rvalid = 0;
    slv0_wready = 0;
    slv1_arready = 0;
    slv1_awready = 0;
    slv1_bid = 0;
    slv1_bresp = 0;
    slv1_bvalid = 0;
    slv1_rdata = 0;
    slv1_rid = 0;
    slv1_rlast = 0;
    slv1_rresp = 0;
    slv1_rvalid = 0;
    slv1_wready = 0;
    slv2_arready = 0;
    slv2_awready = 0;
    slv2_bid = 0;
    slv2_bresp = 0;
    slv2_bvalid = 0;
    slv2_rdata = 0;
    slv2_rid = 0;
    slv2_rlast = 0;
    slv2_rresp = 0;
    slv2_rvalid = 0;
    slv2_wready = 0;
    slv3_arready = 0;
    slv3_awready = 0;
    slv3_bid = 0;
    slv3_bresp = 0;
    slv3_bvalid = 0;
    slv3_rdata = 0;
    slv3_rid = 0;
    slv3_rlast = 0;
    slv3_rresp = 0;
    slv3_rvalid = 0;
    slv3_wready = 0;
    #100;
    rst_n=1;
end
clk dut (
     .clk(clk)
    ,.clock0(clock0)
    ,.clock1(clock1)
    ,.mst0_araddr(mst0_araddr[31:0])
    ,.mst0_arburst(mst0_arburst[1:0])
    ,.mst0_arextras(mst0_arextras[(EXTRAS - 1):0])
    ,.mst0_arid(mst0_arid[(IDWID - 1):0])
    ,.mst0_arlen(mst0_arlen[7:0])
    ,.mst0_arready(mst0_arready)
    ,.mst0_arvalid(mst0_arvalid)
    ,.mst0_awaddr(mst0_awaddr[31:0])
    ,.mst0_awburst(mst0_awburst[1:0])
    ,.mst0_awextras(mst0_awextras[(EXTRAS - 1):0])
    ,.mst0_awid(mst0_awid[(IDWID - 1):0])
    ,.mst0_awlen(mst0_awlen[7:0])
    ,.mst0_awready(mst0_awready)
    ,.mst0_awvalid(mst0_awvalid)
    ,.mst0_bid(mst0_bid[(IDWID - 1):0])
    ,.mst0_bready(mst0_bready)
    ,.mst0_bresp(mst0_bresp[1:0])
    ,.mst0_bvalid(mst0_bvalid)
    ,.mst0_rdata(mst0_rdata[(DWID - 1):0])
    ,.mst0_rid(mst0_rid[(IDWID - 1):0])
    ,.mst0_rlast(mst0_rlast)
    ,.mst0_rready(mst0_rready)
    ,.mst0_rresp(mst0_rresp[1:0])
    ,.mst0_rvalid(mst0_rvalid)
    ,.mst0_wdata(mst0_wdata[(DWID - 1):0])
    ,.mst0_wlast(mst0_wlast)
    ,.mst0_wready(mst0_wready)
    ,.mst0_wstrb(mst0_wstrb[(WSTRB - 1):0])
    ,.mst0_wvalid(mst0_wvalid)
    ,.rst_n(rst_n)
    ,.slv0_araddr(slv0_araddr[31:0])
    ,.slv0_arburst(slv0_arburst[1:0])
    ,.slv0_arextras(slv0_arextras[(EXTRAS - 1):0])
    ,.slv0_arid(slv0_arid[(IDWID - 1):0])
    ,.slv0_arlen(slv0_arlen[7:0])
    ,.slv0_arready(slv0_arready)
    ,.slv0_arvalid(slv0_arvalid)
    ,.slv0_awaddr(slv0_awaddr[31:0])
    ,.slv0_awburst(slv0_awburst[1:0])
    ,.slv0_awextras(slv0_awextras[(EXTRAS - 1):0])
    ,.slv0_awid(slv0_awid[(IDWID - 1):0])
    ,.slv0_awlen(slv0_awlen[7:0])
    ,.slv0_awready(slv0_awready)
    ,.slv0_awvalid(slv0_awvalid)
    ,.slv0_bid(slv0_bid[(IDWID - 1):0])
    ,.slv0_bready(slv0_bready)
    ,.slv0_bresp(slv0_bresp[1:0])
    ,.slv0_bvalid(slv0_bvalid)
    ,.slv0_rdata(slv0_rdata[(DWID - 1):0])
    ,.slv0_rid(slv0_rid[(IDWID - 1):0])
    ,.slv0_rlast(slv0_rlast)
    ,.slv0_rready(slv0_rready)
    ,.slv0_rresp(slv0_rresp[1:0])
    ,.slv0_rvalid(slv0_rvalid)
    ,.slv0_wdata(slv0_wdata[(DWID - 1):0])
    ,.slv0_wlast(slv0_wlast)
    ,.slv0_wready(slv0_wready)
    ,.slv0_wstrb(slv0_wstrb[(WSTRB - 1):0])
    ,.slv0_wvalid(slv0_wvalid)
    ,.slv1_araddr(slv1_araddr[31:0])
    ,.slv1_arburst(slv1_arburst[1:0])
    ,.slv1_arextras(slv1_arextras[(EXTRAS - 1):0])
    ,.slv1_arid(slv1_arid[(IDWID - 1):0])
    ,.slv1_arlen(slv1_arlen[7:0])
    ,.slv1_arready(slv1_arready)
    ,.slv1_arvalid(slv1_arvalid)
    ,.slv1_awaddr(slv1_awaddr[31:0])
    ,.slv1_awburst(slv1_awburst[1:0])
    ,.slv1_awextras(slv1_awextras[(EXTRAS - 1):0])
    ,.slv1_awid(slv1_awid[(IDWID - 1):0])
    ,.slv1_awlen(slv1_awlen[7:0])
    ,.slv1_awready(slv1_awready)
    ,.slv1_awvalid(slv1_awvalid)
    ,.slv1_bid(slv1_bid[(IDWID - 1):0])
    ,.slv1_bready(slv1_bready)
    ,.slv1_bresp(slv1_bresp[1:0])
    ,.slv1_bvalid(slv1_bvalid)
    ,.slv1_rdata(slv1_rdata[(DWID - 1):0])
    ,.slv1_rid(slv1_rid[(IDWID - 1):0])
    ,.slv1_rlast(slv1_rlast)
    ,.slv1_rready(slv1_rready)
    ,.slv1_rresp(slv1_rresp[1:0])
    ,.slv1_rvalid(slv1_rvalid)
    ,.slv1_wdata(slv1_wdata[(DWID - 1):0])
    ,.slv1_wlast(slv1_wlast)
    ,.slv1_wready(slv1_wready)
    ,.slv1_wstrb(slv1_wstrb[(WSTRB - 1):0])
    ,.slv1_wvalid(slv1_wvalid)
    ,.slv2_araddr(slv2_araddr[31:0])
    ,.slv2_arburst(slv2_arburst[1:0])
    ,.slv2_arextras(slv2_arextras[(EXTRAS - 1):0])
    ,.slv2_arid(slv2_arid[(IDWID - 1):0])
    ,.slv2_arlen(slv2_arlen[7:0])
    ,.slv2_arready(slv2_arready)
    ,.slv2_arvalid(slv2_arvalid)
    ,.slv2_awaddr(slv2_awaddr[31:0])
    ,.slv2_awburst(slv2_awburst[1:0])
    ,.slv2_awextras(slv2_awextras[(EXTRAS - 1):0])
    ,.slv2_awid(slv2_awid[(IDWID - 1):0])
    ,.slv2_awlen(slv2_awlen[7:0])
    ,.slv2_awready(slv2_awready)
    ,.slv2_awvalid(slv2_awvalid)
    ,.slv2_bid(slv2_bid[(IDWID - 1):0])
    ,.slv2_bready(slv2_bready)
    ,.slv2_bresp(slv2_bresp[1:0])
    ,.slv2_bvalid(slv2_bvalid)
    ,.slv2_rdata(slv2_rdata[(DWID - 1):0])
    ,.slv2_rid(slv2_rid[(IDWID - 1):0])
    ,.slv2_rlast(slv2_rlast)
    ,.slv2_rready(slv2_rready)
    ,.slv2_rresp(slv2_rresp[1:0])
    ,.slv2_rvalid(slv2_rvalid)
    ,.slv2_wdata(slv2_wdata[(DWID - 1):0])
    ,.slv2_wlast(slv2_wlast)
    ,.slv2_wready(slv2_wready)
    ,.slv2_wstrb(slv2_wstrb[(WSTRB - 1):0])
    ,.slv2_wvalid(slv2_wvalid)
    ,.slv3_araddr(slv3_araddr[31:0])
    ,.slv3_arburst(slv3_arburst[1:0])
    ,.slv3_arextras(slv3_arextras[(EXTRAS - 1):0])
    ,.slv3_arid(slv3_arid[(IDWID - 1):0])
    ,.slv3_arlen(slv3_arlen[7:0])
    ,.slv3_arready(slv3_arready)
    ,.slv3_arvalid(slv3_arvalid)
    ,.slv3_awaddr(slv3_awaddr[31:0])
    ,.slv3_awburst(slv3_awburst[1:0])
    ,.slv3_awextras(slv3_awextras[(EXTRAS - 1):0])
    ,.slv3_awid(slv3_awid[(IDWID - 1):0])
    ,.slv3_awlen(slv3_awlen[7:0])
    ,.slv3_awready(slv3_awready)
    ,.slv3_awvalid(slv3_awvalid)
    ,.slv3_bid(slv3_bid[(IDWID - 1):0])
    ,.slv3_bready(slv3_bready)
    ,.slv3_bresp(slv3_bresp[1:0])
    ,.slv3_bvalid(slv3_bvalid)
    ,.slv3_rdata(slv3_rdata[(DWID - 1):0])
    ,.slv3_rid(slv3_rid[(IDWID - 1):0])
    ,.slv3_rlast(slv3_rlast)
    ,.slv3_rready(slv3_rready)
    ,.slv3_rresp(slv3_rresp[1:0])
    ,.slv3_rvalid(slv3_rvalid)
    ,.slv3_wdata(slv3_wdata[(DWID - 1):0])
    ,.slv3_wlast(slv3_wlast)
    ,.slv3_wready(slv3_wready)
    ,.slv3_wstrb(slv3_wstrb[(WSTRB - 1):0])
    ,.slv3_wvalid(slv3_wvalid)
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
