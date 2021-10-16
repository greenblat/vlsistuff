
`timescale 1ns/1ps
module tb;
parameter IDWID=4; parameter DWID=64; parameter EXTRAS=8; parameter WSTRB=DWID/8;

integer cycles;   initial cycles=0;
integer errors;   initial errors=0;
integer wrongs;   initial wrongs=0;
integer Panics;   initial Panics=0;
integer corrects; initial corrects=0;
integer marker;   initial marker=0;
integer marker0;   initial marker0=0;
integer marker1;   initial marker1=0;
integer marker2;   initial marker2=0;
integer marker3;   initial marker3=0;
integer Index;   initial Index=0;



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


reg clock0; initial clock0 = 0;


integer clock0_HALFPERIOD = 100;
always begin
    clock0 = 0;
    #(clock0_HALFPERIOD);
    clock0 = 1;
    #(3);
    $python("clock0_negedge()");
    #(4);
    $python("clock0_auxs()");
    #(clock0_HALFPERIOD-7);
end


reg clock1; initial clock1 = 0;


integer clock1_HALFPERIOD = 100;
always begin
    clock1 = 0;
    #(clock1_HALFPERIOD);
    clock1 = 1;
    #(3);
    $python("clock1_negedge()");
    #(4);
    $python("clock1_auxs()");
    #(clock1_HALFPERIOD-7);
end

reg  [2:0] slv0_awsize ; initial slv0_awsize = 0;
reg  [2:0] slv0_arsize ; initial slv0_arsize = 0;

wire  [IDWID-1:0] slv0_arid ;
wire  [31:0] slv0_araddr ;
wire  [7:0] slv0_arlen ;
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

reg  [2:0] slv1_awsize ; initial slv1_awsize = 0;
reg  [2:0] slv1_arsize ; initial slv1_arsize = 0;

wire  [IDWID-1:0] slv1_arid ;
wire  [31:0] slv1_araddr ;
wire  [7:0] slv1_arlen ;
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

reg  [2:0] slv2_awsize ; initial slv2_awsize = 0;
reg  [2:0] slv2_arsize ; initial slv2_arsize = 0;

wire  [IDWID-1:0] slv2_arid ;
wire  [31:0] slv2_araddr ;
wire  [7:0] slv2_arlen ;
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

reg  [2:0] slv3_awsize ; initial slv3_awsize = 0;
reg  [2:0] slv3_arsize ; initial slv3_arsize = 0;

wire  [IDWID-1:0] slv3_arid ;
wire  [31:0] slv3_araddr ;
wire  [7:0] slv3_arlen ;
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

reg  [2:0] mst0_awsize ; initial mst0_awsize = 0;
reg  [2:0] mst0_arsize ; initial mst0_arsize = 0;

reg  [IDWID-1:0] mst0_arid ;
reg  [31:0] mst0_araddr ;
reg  [7:0] mst0_arlen ;
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
clk dut ( .clk(clk),.rst_n(rst_n)
   ,.clock0(clock0)
   ,.clock1(clock1)

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

