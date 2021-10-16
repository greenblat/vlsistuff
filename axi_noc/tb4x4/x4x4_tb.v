
`timescale 1ns/1ps
module tb;
parameter IDWID=4; parameter DWID=64; parameter EXTRAS=8; parameter WSTRB=DWID/8;

reg [31:0] cycles;   initial cycles=0;
reg [31:0] errors;   initial errors=0;
reg [31:0] wrongs;   initial wrongs=0;
reg [31:0] Panics;   initial Panics=0;
reg [31:0] corrects; initial corrects=0;
reg [31:0] marker;   initial marker=0;
reg [31:0] marker0;   initial marker0=0;
reg [31:0] marker1;   initial marker1=0;
reg [31:0] marker2;   initial marker2=0;
reg [31:0] marker3;   initial marker3=0;
reg [31:0] Index;   initial Index=0;



reg clk; reg rst_n;
integer clk_HALFPERIOD = 100;
always begin
    clk = 0;
    #(clk_HALFPERIOD);
    clk = 1;
    #3;
    $python("negedge()");
    #3;
    $python("auxs()");
    #(clk_HALFPERIOD-6);
end
initial begin
    $dumpvars(0,tb);
    rst_n = 0;
    #100;
    rst_n = 1;
end

// reg  [2:0] slv0_awsize ; initial slv0_awsize = 0;
// reg  [2:0] slv0_arsize ; initial slv0_arsize = 0;

wire  [IDWID-1:0] slv0_arid ;
wire  [31:0] slv0_araddr ;
wire  [7:0] slv0_arlen ;
wire  [2:0] slv0_arsize ;
wire  [EXTRAS-1:0] slv0_arextras ;
wire  [1:0] slv0_arburst ;
wire  slv0_arvalid ;
reg  slv0_arready ;
reg  [IDWID-1:0] slv0_rid ;
reg  [DWID-1:0] slv0_rdata ;
reg  [1:0] slv0_rresp ;
reg  slv0_rlast ;
reg  slv0_rvalid ;
wire  slv0_rready ;

wire  [IDWID-1:0] slv0_awid ;
wire  [31:0] slv0_awaddr ;
wire  [7:0] slv0_awlen ;
wire  [2:0] slv0_awsize ;
wire  [EXTRAS-1:0] slv0_awextras ;
wire  [1:0] slv0_awburst ;
wire  slv0_awvalid ;
reg  slv0_awready ;
wire  [DWID-1:0] slv0_wdata ;
wire  [WSTRB-1:0] slv0_wstrb ;
wire  slv0_wlast ;
wire  slv0_wvalid ;
reg  slv0_wready ;
reg  [IDWID-1:0] slv0_bid ;
reg  [1:0] slv0_bresp ;
reg  slv0_bvalid ;
wire  slv0_bready ;

initial slv0_arready = 0;
initial slv0_awready = 0;
initial slv0_rvalid = 0;
initial slv0_bvalid = 0;

// reg  [2:0] slv1_awsize ; initial slv1_awsize = 0;
// reg  [2:0] slv1_arsize ; initial slv1_arsize = 0;

wire  [IDWID-1:0] slv1_arid ;
wire  [31:0] slv1_araddr ;
wire  [7:0] slv1_arlen ;
wire  [2:0] slv1_arsize ;
wire  [EXTRAS-1:0] slv1_arextras ;
wire  [1:0] slv1_arburst ;
wire  slv1_arvalid ;
reg  slv1_arready ;
reg  [IDWID-1:0] slv1_rid ;
reg  [DWID-1:0] slv1_rdata ;
reg  [1:0] slv1_rresp ;
reg  slv1_rlast ;
reg  slv1_rvalid ;
wire  slv1_rready ;

wire  [IDWID-1:0] slv1_awid ;
wire  [31:0] slv1_awaddr ;
wire  [7:0] slv1_awlen ;
wire  [2:0] slv1_awsize ;
wire  [EXTRAS-1:0] slv1_awextras ;
wire  [1:0] slv1_awburst ;
wire  slv1_awvalid ;
reg  slv1_awready ;
wire  [DWID-1:0] slv1_wdata ;
wire  [WSTRB-1:0] slv1_wstrb ;
wire  slv1_wlast ;
wire  slv1_wvalid ;
reg  slv1_wready ;
reg  [IDWID-1:0] slv1_bid ;
reg  [1:0] slv1_bresp ;
reg  slv1_bvalid ;
wire  slv1_bready ;

initial slv1_arready = 0;
initial slv1_awready = 0;
initial slv1_rvalid = 0;
initial slv1_bvalid = 0;

// reg  [2:0] slv2_awsize ; initial slv2_awsize = 0;
// reg  [2:0] slv2_arsize ; initial slv2_arsize = 0;

wire  [IDWID-1:0] slv2_arid ;
wire  [31:0] slv2_araddr ;
wire  [7:0] slv2_arlen ;
wire  [2:0] slv2_arsize ;
wire  [EXTRAS-1:0] slv2_arextras ;
wire  [1:0] slv2_arburst ;
wire  slv2_arvalid ;
reg  slv2_arready ;
reg  [IDWID-1:0] slv2_rid ;
reg  [DWID-1:0] slv2_rdata ;
reg  [1:0] slv2_rresp ;
reg  slv2_rlast ;
reg  slv2_rvalid ;
wire  slv2_rready ;

wire  [IDWID-1:0] slv2_awid ;
wire  [31:0] slv2_awaddr ;
wire  [7:0] slv2_awlen ;
wire  [2:0] slv2_awsize ;
wire  [EXTRAS-1:0] slv2_awextras ;
wire  [1:0] slv2_awburst ;
wire  slv2_awvalid ;
reg  slv2_awready ;
wire  [DWID-1:0] slv2_wdata ;
wire  [WSTRB-1:0] slv2_wstrb ;
wire  slv2_wlast ;
wire  slv2_wvalid ;
reg  slv2_wready ;
reg  [IDWID-1:0] slv2_bid ;
reg  [1:0] slv2_bresp ;
reg  slv2_bvalid ;
wire  slv2_bready ;

initial slv2_arready = 0;
initial slv2_awready = 0;
initial slv2_rvalid = 0;
initial slv2_bvalid = 0;

// reg  [2:0] slv3_awsize ; initial slv3_awsize = 0;
// reg  [2:0] slv3_arsize ; initial slv3_arsize = 0;

wire  [IDWID-1:0] slv3_arid ;
wire  [31:0] slv3_araddr ;
wire  [7:0] slv3_arlen ;
wire  [2:0] slv3_arsize ;
wire  [EXTRAS-1:0] slv3_arextras ;
wire  [1:0] slv3_arburst ;
wire  slv3_arvalid ;
reg  slv3_arready ;
reg  [IDWID-1:0] slv3_rid ;
reg  [DWID-1:0] slv3_rdata ;
reg  [1:0] slv3_rresp ;
reg  slv3_rlast ;
reg  slv3_rvalid ;
wire  slv3_rready ;

wire  [IDWID-1:0] slv3_awid ;
wire  [31:0] slv3_awaddr ;
wire  [7:0] slv3_awlen ;
wire  [2:0] slv3_awsize ;
wire  [EXTRAS-1:0] slv3_awextras ;
wire  [1:0] slv3_awburst ;
wire  slv3_awvalid ;
reg  slv3_awready ;
wire  [DWID-1:0] slv3_wdata ;
wire  [WSTRB-1:0] slv3_wstrb ;
wire  slv3_wlast ;
wire  slv3_wvalid ;
reg  slv3_wready ;
reg  [IDWID-1:0] slv3_bid ;
reg  [1:0] slv3_bresp ;
reg  slv3_bvalid ;
wire  slv3_bready ;

initial slv3_arready = 0;
initial slv3_awready = 0;
initial slv3_rvalid = 0;
initial slv3_bvalid = 0;

// reg  [2:0] mst0_awsize ; initial mst0_awsize = 0;
// reg  [2:0] mst0_arsize ; initial mst0_arsize = 0;

reg  [IDWID-1:0] mst0_arid ;
reg  [31:0] mst0_araddr ;
reg  [7:0] mst0_arlen ;
reg  [2:0] mst0_arsize ;
reg  [EXTRAS-1:0] mst0_arextras ;
reg  [1:0] mst0_arburst ;
reg  mst0_arvalid ;
wire  mst0_arready ;
wire  [IDWID-1:0] mst0_rid ;
wire  [DWID-1:0] mst0_rdata ;
wire  [1:0] mst0_rresp ;
wire  mst0_rlast ;
wire  mst0_rvalid ;
reg  mst0_rready ;

reg  [IDWID-1:0] mst0_awid ;
reg  [31:0] mst0_awaddr ;
reg  [7:0] mst0_awlen ;
reg  [2:0] mst0_awsize ;
reg  [EXTRAS-1:0] mst0_awextras ;
reg  [1:0] mst0_awburst ;
reg  mst0_awvalid ;
wire  mst0_awready ;
reg  [DWID-1:0] mst0_wdata ;
reg  [WSTRB-1:0] mst0_wstrb ;
reg  mst0_wlast ;
reg  mst0_wvalid ;
wire  mst0_wready ;
wire  [IDWID-1:0] mst0_bid ;
wire  [1:0] mst0_bresp ;
wire  mst0_bvalid ;
reg  mst0_bready ;

initial mst0_bready = 0;
initial mst0_wvalid = 0;
initial mst0_arvalid = 0;
initial mst0_awvalid = 0;
initial mst0_rready = 0;

// reg  [2:0] mst1_awsize ; initial mst1_awsize = 0;
// reg  [2:0] mst1_arsize ; initial mst1_arsize = 0;

reg  [IDWID-1:0] mst1_arid ;
reg  [31:0] mst1_araddr ;
reg  [7:0] mst1_arlen ;
reg  [2:0] mst1_arsize ;
reg  [EXTRAS-1:0] mst1_arextras ;
reg  [1:0] mst1_arburst ;
reg  mst1_arvalid ;
wire  mst1_arready ;
wire  [IDWID-1:0] mst1_rid ;
wire  [DWID-1:0] mst1_rdata ;
wire  [1:0] mst1_rresp ;
wire  mst1_rlast ;
wire  mst1_rvalid ;
reg  mst1_rready ;

reg  [IDWID-1:0] mst1_awid ;
reg  [31:0] mst1_awaddr ;
reg  [7:0] mst1_awlen ;
reg  [2:0] mst1_awsize ;
reg  [EXTRAS-1:0] mst1_awextras ;
reg  [1:0] mst1_awburst ;
reg  mst1_awvalid ;
wire  mst1_awready ;
reg  [DWID-1:0] mst1_wdata ;
reg  [WSTRB-1:0] mst1_wstrb ;
reg  mst1_wlast ;
reg  mst1_wvalid ;
wire  mst1_wready ;
wire  [IDWID-1:0] mst1_bid ;
wire  [1:0] mst1_bresp ;
wire  mst1_bvalid ;
reg  mst1_bready ;

initial mst1_bready = 0;
initial mst1_wvalid = 0;
initial mst1_arvalid = 0;
initial mst1_awvalid = 0;
initial mst1_rready = 0;

// reg  [2:0] mst2_awsize ; initial mst2_awsize = 0;
// reg  [2:0] mst2_arsize ; initial mst2_arsize = 0;

reg  [IDWID-1:0] mst2_arid ;
reg  [31:0] mst2_araddr ;
reg  [7:0] mst2_arlen ;
reg  [2:0] mst2_arsize ;
reg  [EXTRAS-1:0] mst2_arextras ;
reg  [1:0] mst2_arburst ;
reg  mst2_arvalid ;
wire  mst2_arready ;
wire  [IDWID-1:0] mst2_rid ;
wire  [DWID-1:0] mst2_rdata ;
wire  [1:0] mst2_rresp ;
wire  mst2_rlast ;
wire  mst2_rvalid ;
reg  mst2_rready ;

reg  [IDWID-1:0] mst2_awid ;
reg  [31:0] mst2_awaddr ;
reg  [7:0] mst2_awlen ;
reg  [2:0] mst2_awsize ;
reg  [EXTRAS-1:0] mst2_awextras ;
reg  [1:0] mst2_awburst ;
reg  mst2_awvalid ;
wire  mst2_awready ;
reg  [DWID-1:0] mst2_wdata ;
reg  [WSTRB-1:0] mst2_wstrb ;
reg  mst2_wlast ;
reg  mst2_wvalid ;
wire  mst2_wready ;
wire  [IDWID-1:0] mst2_bid ;
wire  [1:0] mst2_bresp ;
wire  mst2_bvalid ;
reg  mst2_bready ;

initial mst2_bready = 0;
initial mst2_wvalid = 0;
initial mst2_arvalid = 0;
initial mst2_awvalid = 0;
initial mst2_rready = 0;

// reg  [2:0] mst3_awsize ; initial mst3_awsize = 0;
// reg  [2:0] mst3_arsize ; initial mst3_arsize = 0;

reg  [IDWID-1:0] mst3_arid ;
reg  [31:0] mst3_araddr ;
reg  [7:0] mst3_arlen ;
reg  [2:0] mst3_arsize ;
reg  [EXTRAS-1:0] mst3_arextras ;
reg  [1:0] mst3_arburst ;
reg  mst3_arvalid ;
wire  mst3_arready ;
wire  [IDWID-1:0] mst3_rid ;
wire  [DWID-1:0] mst3_rdata ;
wire  [1:0] mst3_rresp ;
wire  mst3_rlast ;
wire  mst3_rvalid ;
reg  mst3_rready ;

reg  [IDWID-1:0] mst3_awid ;
reg  [31:0] mst3_awaddr ;
reg  [7:0] mst3_awlen ;
reg  [2:0] mst3_awsize ;
reg  [EXTRAS-1:0] mst3_awextras ;
reg  [1:0] mst3_awburst ;
reg  mst3_awvalid ;
wire  mst3_awready ;
reg  [DWID-1:0] mst3_wdata ;
reg  [WSTRB-1:0] mst3_wstrb ;
reg  mst3_wlast ;
reg  mst3_wvalid ;
wire  mst3_wready ;
wire  [IDWID-1:0] mst3_bid ;
wire  [1:0] mst3_bresp ;
wire  mst3_bvalid ;
reg  mst3_bready ;

initial mst3_bready = 0;
initial mst3_wvalid = 0;
initial mst3_arvalid = 0;
initial mst3_awvalid = 0;
initial mst3_rready = 0;
x4x4 dut ( .clk(clk),.rst_n(rst_n)

    ,.slv0_araddr(slv0_araddr[31:0])
    ,.slv0_arburst(slv0_arburst[1:0])
    ,.slv0_arextras(slv0_arextras[(EXTRAS - 1):0])
    ,.slv0_arid(slv0_arid)
    ,.slv0_arlen(slv0_arlen)
    ,.slv0_arsize(slv0_arsize)
    ,.slv0_arready(slv0_arready)
    ,.slv0_arvalid(slv0_arvalid)
    ,.slv0_awaddr(slv0_awaddr[31:0])
    ,.slv0_awburst(slv0_awburst[1:0])
    ,.slv0_awextras(slv0_awextras[(EXTRAS - 1):0])
    ,.slv0_awid(slv0_awid[(IDWID - 1):0])
    ,.slv0_awlen(slv0_awlen)
    ,.slv0_awsize(slv0_awsize)
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
    ,.slv1_arid(slv1_arid)
    ,.slv1_arlen(slv1_arlen)
    ,.slv1_arsize(slv1_arsize)
    ,.slv1_arready(slv1_arready)
    ,.slv1_arvalid(slv1_arvalid)
    ,.slv1_awaddr(slv1_awaddr[31:0])
    ,.slv1_awburst(slv1_awburst[1:0])
    ,.slv1_awextras(slv1_awextras[(EXTRAS - 1):0])
    ,.slv1_awid(slv1_awid[(IDWID - 1):0])
    ,.slv1_awlen(slv1_awlen)
    ,.slv1_awsize(slv1_awsize)
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
    ,.slv2_arid(slv2_arid)
    ,.slv2_arlen(slv2_arlen)
    ,.slv2_arsize(slv2_arsize)
    ,.slv2_arready(slv2_arready)
    ,.slv2_arvalid(slv2_arvalid)
    ,.slv2_awaddr(slv2_awaddr[31:0])
    ,.slv2_awburst(slv2_awburst[1:0])
    ,.slv2_awextras(slv2_awextras[(EXTRAS - 1):0])
    ,.slv2_awid(slv2_awid[(IDWID - 1):0])
    ,.slv2_awlen(slv2_awlen)
    ,.slv2_awsize(slv2_awsize)
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
    ,.slv3_arid(slv3_arid)
    ,.slv3_arlen(slv3_arlen)
    ,.slv3_arsize(slv3_arsize)
    ,.slv3_arready(slv3_arready)
    ,.slv3_arvalid(slv3_arvalid)
    ,.slv3_awaddr(slv3_awaddr[31:0])
    ,.slv3_awburst(slv3_awburst[1:0])
    ,.slv3_awextras(slv3_awextras[(EXTRAS - 1):0])
    ,.slv3_awid(slv3_awid[(IDWID - 1):0])
    ,.slv3_awlen(slv3_awlen)
    ,.slv3_awsize(slv3_awsize)
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


    ,.mst0_araddr(mst0_araddr[31:0])
    ,.mst0_arburst(mst0_arburst[1:0])
    ,.mst0_arextras(mst0_arextras[(EXTRAS - 1):0])
    ,.mst0_arid(mst0_arid)
    ,.mst0_arlen(mst0_arlen)
    ,.mst0_arsize(mst0_arsize)
    ,.mst0_arready(mst0_arready)
    ,.mst0_arvalid(mst0_arvalid)
    ,.mst0_awaddr(mst0_awaddr[31:0])
    ,.mst0_awburst(mst0_awburst[1:0])
    ,.mst0_awextras(mst0_awextras[(EXTRAS - 1):0])
    ,.mst0_awid(mst0_awid[(IDWID - 1):0])
    ,.mst0_awlen(mst0_awlen)
    ,.mst0_awsize(mst0_awsize)
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

    ,.mst1_araddr(mst1_araddr[31:0])
    ,.mst1_arburst(mst1_arburst[1:0])
    ,.mst1_arextras(mst1_arextras[(EXTRAS - 1):0])
    ,.mst1_arid(mst1_arid)
    ,.mst1_arlen(mst1_arlen)
    ,.mst1_arsize(mst1_arsize)
    ,.mst1_arready(mst1_arready)
    ,.mst1_arvalid(mst1_arvalid)
    ,.mst1_awaddr(mst1_awaddr[31:0])
    ,.mst1_awburst(mst1_awburst[1:0])
    ,.mst1_awextras(mst1_awextras[(EXTRAS - 1):0])
    ,.mst1_awid(mst1_awid[(IDWID - 1):0])
    ,.mst1_awlen(mst1_awlen)
    ,.mst1_awsize(mst1_awsize)
    ,.mst1_awready(mst1_awready)
    ,.mst1_awvalid(mst1_awvalid)
    ,.mst1_bid(mst1_bid[(IDWID - 1):0])
    ,.mst1_bready(mst1_bready)
    ,.mst1_bresp(mst1_bresp[1:0])
    ,.mst1_bvalid(mst1_bvalid)
    ,.mst1_rdata(mst1_rdata[(DWID - 1):0])
    ,.mst1_rid(mst1_rid[(IDWID - 1):0])
    ,.mst1_rlast(mst1_rlast)
    ,.mst1_rready(mst1_rready)
    ,.mst1_rresp(mst1_rresp[1:0])
    ,.mst1_rvalid(mst1_rvalid)
    ,.mst1_wdata(mst1_wdata[(DWID - 1):0])
    ,.mst1_wlast(mst1_wlast)
    ,.mst1_wready(mst1_wready)
    ,.mst1_wstrb(mst1_wstrb[(WSTRB - 1):0])
    ,.mst1_wvalid(mst1_wvalid)

    ,.mst2_araddr(mst2_araddr[31:0])
    ,.mst2_arburst(mst2_arburst[1:0])
    ,.mst2_arextras(mst2_arextras[(EXTRAS - 1):0])
    ,.mst2_arid(mst2_arid)
    ,.mst2_arlen(mst2_arlen)
    ,.mst2_arsize(mst2_arsize)
    ,.mst2_arready(mst2_arready)
    ,.mst2_arvalid(mst2_arvalid)
    ,.mst2_awaddr(mst2_awaddr[31:0])
    ,.mst2_awburst(mst2_awburst[1:0])
    ,.mst2_awextras(mst2_awextras[(EXTRAS - 1):0])
    ,.mst2_awid(mst2_awid[(IDWID - 1):0])
    ,.mst2_awlen(mst2_awlen)
    ,.mst2_awsize(mst2_awsize)
    ,.mst2_awready(mst2_awready)
    ,.mst2_awvalid(mst2_awvalid)
    ,.mst2_bid(mst2_bid[(IDWID - 1):0])
    ,.mst2_bready(mst2_bready)
    ,.mst2_bresp(mst2_bresp[1:0])
    ,.mst2_bvalid(mst2_bvalid)
    ,.mst2_rdata(mst2_rdata[(DWID - 1):0])
    ,.mst2_rid(mst2_rid[(IDWID - 1):0])
    ,.mst2_rlast(mst2_rlast)
    ,.mst2_rready(mst2_rready)
    ,.mst2_rresp(mst2_rresp[1:0])
    ,.mst2_rvalid(mst2_rvalid)
    ,.mst2_wdata(mst2_wdata[(DWID - 1):0])
    ,.mst2_wlast(mst2_wlast)
    ,.mst2_wready(mst2_wready)
    ,.mst2_wstrb(mst2_wstrb[(WSTRB - 1):0])
    ,.mst2_wvalid(mst2_wvalid)

    ,.mst3_araddr(mst3_araddr[31:0])
    ,.mst3_arburst(mst3_arburst[1:0])
    ,.mst3_arextras(mst3_arextras[(EXTRAS - 1):0])
    ,.mst3_arid(mst3_arid)
    ,.mst3_arlen(mst3_arlen)
    ,.mst3_arsize(mst3_arsize)
    ,.mst3_arready(mst3_arready)
    ,.mst3_arvalid(mst3_arvalid)
    ,.mst3_awaddr(mst3_awaddr[31:0])
    ,.mst3_awburst(mst3_awburst[1:0])
    ,.mst3_awextras(mst3_awextras[(EXTRAS - 1):0])
    ,.mst3_awid(mst3_awid[(IDWID - 1):0])
    ,.mst3_awlen(mst3_awlen)
    ,.mst3_awsize(mst3_awsize)
    ,.mst3_awready(mst3_awready)
    ,.mst3_awvalid(mst3_awvalid)
    ,.mst3_bid(mst3_bid[(IDWID - 1):0])
    ,.mst3_bready(mst3_bready)
    ,.mst3_bresp(mst3_bresp[1:0])
    ,.mst3_bvalid(mst3_bvalid)
    ,.mst3_rdata(mst3_rdata[(DWID - 1):0])
    ,.mst3_rid(mst3_rid[(IDWID - 1):0])
    ,.mst3_rlast(mst3_rlast)
    ,.mst3_rready(mst3_rready)
    ,.mst3_rresp(mst3_rresp[1:0])
    ,.mst3_rvalid(mst3_rvalid)
    ,.mst3_wdata(mst3_wdata[(DWID - 1):0])
    ,.mst3_wlast(mst3_wlast)
    ,.mst3_wready(mst3_wready)
    ,.mst3_wstrb(mst3_wstrb[(WSTRB - 1):0])
    ,.mst3_wvalid(mst3_wvalid)
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

