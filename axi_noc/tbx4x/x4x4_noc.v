
    module x4x4 #(parameter IDWID=4, parameter DWID=64, parameter EXTRAS=8, parameter WSTRB=DWID/8) ( input clk, input rst_n

    ,output [IDWID-1:0] slv0_arid
    ,output [31:0] slv0_araddr
    ,output [7:0] slv0_arlen
    ,output [EXTRAS-1:0] slv0_arextras
    ,output [1:0] slv0_arburst
    ,output slv0_arvalid
    ,input slv0_arready
    ,input [IDWID-1:0] slv0_rid
    ,input [DWID-1:0] slv0_rdata
    ,input [1:0] slv0_rresp
    ,input slv0_rlast
    ,input slv0_rvalid
    ,output slv0_rready

    ,output [IDWID-1:0] slv0_awid
    ,output [31:0] slv0_awaddr
    ,output [7:0] slv0_awlen
    ,output [EXTRAS-1:0] slv0_awextras
    ,output [1:0] slv0_awburst
    ,output slv0_awvalid
    ,input slv0_awready
    ,output [DWID-1:0] slv0_wdata
    ,output [WSTRB-1:0] slv0_wstrb
    ,output slv0_wlast
    ,output slv0_wvalid
    ,input slv0_wready
    ,input [IDWID-1:0] slv0_bid
    ,input [1:0] slv0_bresp
    ,input slv0_bvalid
    ,output slv0_bready

    ,output [IDWID-1:0] slv1_arid
    ,output [31:0] slv1_araddr
    ,output [7:0] slv1_arlen
    ,output [EXTRAS-1:0] slv1_arextras
    ,output [1:0] slv1_arburst
    ,output slv1_arvalid
    ,input slv1_arready
    ,input [IDWID-1:0] slv1_rid
    ,input [DWID-1:0] slv1_rdata
    ,input [1:0] slv1_rresp
    ,input slv1_rlast
    ,input slv1_rvalid
    ,output slv1_rready

    ,output [IDWID-1:0] slv1_awid
    ,output [31:0] slv1_awaddr
    ,output [7:0] slv1_awlen
    ,output [EXTRAS-1:0] slv1_awextras
    ,output [1:0] slv1_awburst
    ,output slv1_awvalid
    ,input slv1_awready
    ,output [DWID-1:0] slv1_wdata
    ,output [WSTRB-1:0] slv1_wstrb
    ,output slv1_wlast
    ,output slv1_wvalid
    ,input slv1_wready
    ,input [IDWID-1:0] slv1_bid
    ,input [1:0] slv1_bresp
    ,input slv1_bvalid
    ,output slv1_bready

    ,output [IDWID-1:0] slv2_arid
    ,output [31:0] slv2_araddr
    ,output [7:0] slv2_arlen
    ,output [EXTRAS-1:0] slv2_arextras
    ,output [1:0] slv2_arburst
    ,output slv2_arvalid
    ,input slv2_arready
    ,input [IDWID-1:0] slv2_rid
    ,input [DWID-1:0] slv2_rdata
    ,input [1:0] slv2_rresp
    ,input slv2_rlast
    ,input slv2_rvalid
    ,output slv2_rready

    ,output [IDWID-1:0] slv2_awid
    ,output [31:0] slv2_awaddr
    ,output [7:0] slv2_awlen
    ,output [EXTRAS-1:0] slv2_awextras
    ,output [1:0] slv2_awburst
    ,output slv2_awvalid
    ,input slv2_awready
    ,output [DWID-1:0] slv2_wdata
    ,output [WSTRB-1:0] slv2_wstrb
    ,output slv2_wlast
    ,output slv2_wvalid
    ,input slv2_wready
    ,input [IDWID-1:0] slv2_bid
    ,input [1:0] slv2_bresp
    ,input slv2_bvalid
    ,output slv2_bready

    ,output [IDWID-1:0] slv3_arid
    ,output [31:0] slv3_araddr
    ,output [7:0] slv3_arlen
    ,output [EXTRAS-1:0] slv3_arextras
    ,output [1:0] slv3_arburst
    ,output slv3_arvalid
    ,input slv3_arready
    ,input [IDWID-1:0] slv3_rid
    ,input [DWID-1:0] slv3_rdata
    ,input [1:0] slv3_rresp
    ,input slv3_rlast
    ,input slv3_rvalid
    ,output slv3_rready

    ,output [IDWID-1:0] slv3_awid
    ,output [31:0] slv3_awaddr
    ,output [7:0] slv3_awlen
    ,output [EXTRAS-1:0] slv3_awextras
    ,output [1:0] slv3_awburst
    ,output slv3_awvalid
    ,input slv3_awready
    ,output [DWID-1:0] slv3_wdata
    ,output [WSTRB-1:0] slv3_wstrb
    ,output slv3_wlast
    ,output slv3_wvalid
    ,input slv3_wready
    ,input [IDWID-1:0] slv3_bid
    ,input [1:0] slv3_bresp
    ,input slv3_bvalid
    ,output slv3_bready

    ,input [IDWID-1:0] mst0_arid
    ,input [31:0] mst0_araddr
    ,input [7:0] mst0_arlen
    ,input [EXTRAS-1:0] mst0_arextras
    ,input [1:0] mst0_arburst
    ,input mst0_arvalid
    ,output mst0_arready
    ,output [IDWID-1:0] mst0_rid
    ,output [DWID-1:0] mst0_rdata
    ,output [1:0] mst0_rresp
    ,output mst0_rlast
    ,output mst0_rvalid
    ,input mst0_rready

    ,input [IDWID-1:0] mst0_awid
    ,input [31:0] mst0_awaddr
    ,input [7:0] mst0_awlen
    ,input [EXTRAS-1:0] mst0_awextras
    ,input [1:0] mst0_awburst
    ,input mst0_awvalid
    ,output mst0_awready
    ,input [DWID-1:0] mst0_wdata
    ,input [WSTRB-1:0] mst0_wstrb
    ,input mst0_wlast
    ,input mst0_wvalid
    ,output mst0_wready
    ,output [IDWID-1:0] mst0_bid
    ,output [1:0] mst0_bresp
    ,output mst0_bvalid
    ,input mst0_bready

    ,input [IDWID-1:0] mst1_arid
    ,input [31:0] mst1_araddr
    ,input [7:0] mst1_arlen
    ,input [EXTRAS-1:0] mst1_arextras
    ,input [1:0] mst1_arburst
    ,input mst1_arvalid
    ,output mst1_arready
    ,output [IDWID-1:0] mst1_rid
    ,output [DWID-1:0] mst1_rdata
    ,output [1:0] mst1_rresp
    ,output mst1_rlast
    ,output mst1_rvalid
    ,input mst1_rready

    ,input [IDWID-1:0] mst1_awid
    ,input [31:0] mst1_awaddr
    ,input [7:0] mst1_awlen
    ,input [EXTRAS-1:0] mst1_awextras
    ,input [1:0] mst1_awburst
    ,input mst1_awvalid
    ,output mst1_awready
    ,input [DWID-1:0] mst1_wdata
    ,input [WSTRB-1:0] mst1_wstrb
    ,input mst1_wlast
    ,input mst1_wvalid
    ,output mst1_wready
    ,output [IDWID-1:0] mst1_bid
    ,output [1:0] mst1_bresp
    ,output mst1_bvalid
    ,input mst1_bready

    ,input [IDWID-1:0] mst2_arid
    ,input [31:0] mst2_araddr
    ,input [7:0] mst2_arlen
    ,input [EXTRAS-1:0] mst2_arextras
    ,input [1:0] mst2_arburst
    ,input mst2_arvalid
    ,output mst2_arready
    ,output [IDWID-1:0] mst2_rid
    ,output [DWID-1:0] mst2_rdata
    ,output [1:0] mst2_rresp
    ,output mst2_rlast
    ,output mst2_rvalid
    ,input mst2_rready

    ,input [IDWID-1:0] mst2_awid
    ,input [31:0] mst2_awaddr
    ,input [7:0] mst2_awlen
    ,input [EXTRAS-1:0] mst2_awextras
    ,input [1:0] mst2_awburst
    ,input mst2_awvalid
    ,output mst2_awready
    ,input [DWID-1:0] mst2_wdata
    ,input [WSTRB-1:0] mst2_wstrb
    ,input mst2_wlast
    ,input mst2_wvalid
    ,output mst2_wready
    ,output [IDWID-1:0] mst2_bid
    ,output [1:0] mst2_bresp
    ,output mst2_bvalid
    ,input mst2_bready

    ,input [IDWID-1:0] mst3_arid
    ,input [31:0] mst3_araddr
    ,input [7:0] mst3_arlen
    ,input [EXTRAS-1:0] mst3_arextras
    ,input [1:0] mst3_arburst
    ,input mst3_arvalid
    ,output mst3_arready
    ,output [IDWID-1:0] mst3_rid
    ,output [DWID-1:0] mst3_rdata
    ,output [1:0] mst3_rresp
    ,output mst3_rlast
    ,output mst3_rvalid
    ,input mst3_rready

    ,input [IDWID-1:0] mst3_awid
    ,input [31:0] mst3_awaddr
    ,input [7:0] mst3_awlen
    ,input [EXTRAS-1:0] mst3_awextras
    ,input [1:0] mst3_awburst
    ,input mst3_awvalid
    ,output mst3_awready
    ,input [DWID-1:0] mst3_wdata
    ,input [WSTRB-1:0] mst3_wstrb
    ,input mst3_wlast
    ,input mst3_wvalid
    ,output mst3_wready
    ,output [IDWID-1:0] mst3_bid
    ,output [1:0] mst3_bresp
    ,output mst3_bvalid
    ,input mst3_bready
);

wire [IDWID-1:0] splitter0_merger0_arid ;
wire [31:0] splitter0_merger0_araddr ;
wire [7:0] splitter0_merger0_arlen ;
wire [EXTRAS-1:0] splitter0_merger0_arextras ;
wire [1:0] splitter0_merger0_arburst ;
wire splitter0_merger0_arvalid ;
wire splitter0_merger0_arready ;
wire [IDWID-1:0] splitter0_merger0_rid ;
wire [DWID-1:0] splitter0_merger0_rdata ;
wire [1:0] splitter0_merger0_rresp ;
wire splitter0_merger0_rlast ;
wire splitter0_merger0_rvalid ;
wire splitter0_merger0_rready ;

wire [IDWID-1:0] splitter0_merger0_awid ;
wire [31:0] splitter0_merger0_awaddr ;
wire [7:0] splitter0_merger0_awlen ;
wire [EXTRAS-1:0] splitter0_merger0_awextras ;
wire [1:0] splitter0_merger0_awburst ;
wire splitter0_merger0_awvalid ;
wire splitter0_merger0_awready ;
wire [DWID-1:0] splitter0_merger0_wdata ;
wire [WSTRB-1:0] splitter0_merger0_wstrb ;
wire splitter0_merger0_wlast ;
wire splitter0_merger0_wvalid ;
wire splitter0_merger0_wready ;
wire [IDWID-1:0] splitter0_merger0_bid ;
wire [1:0] splitter0_merger0_bresp ;
wire splitter0_merger0_bvalid ;
wire splitter0_merger0_bready ;


wire [IDWID-1:0] splitter0_merger1_arid ;
wire [31:0] splitter0_merger1_araddr ;
wire [7:0] splitter0_merger1_arlen ;
wire [EXTRAS-1:0] splitter0_merger1_arextras ;
wire [1:0] splitter0_merger1_arburst ;
wire splitter0_merger1_arvalid ;
wire splitter0_merger1_arready ;
wire [IDWID-1:0] splitter0_merger1_rid ;
wire [DWID-1:0] splitter0_merger1_rdata ;
wire [1:0] splitter0_merger1_rresp ;
wire splitter0_merger1_rlast ;
wire splitter0_merger1_rvalid ;
wire splitter0_merger1_rready ;

wire [IDWID-1:0] splitter0_merger1_awid ;
wire [31:0] splitter0_merger1_awaddr ;
wire [7:0] splitter0_merger1_awlen ;
wire [EXTRAS-1:0] splitter0_merger1_awextras ;
wire [1:0] splitter0_merger1_awburst ;
wire splitter0_merger1_awvalid ;
wire splitter0_merger1_awready ;
wire [DWID-1:0] splitter0_merger1_wdata ;
wire [WSTRB-1:0] splitter0_merger1_wstrb ;
wire splitter0_merger1_wlast ;
wire splitter0_merger1_wvalid ;
wire splitter0_merger1_wready ;
wire [IDWID-1:0] splitter0_merger1_bid ;
wire [1:0] splitter0_merger1_bresp ;
wire splitter0_merger1_bvalid ;
wire splitter0_merger1_bready ;


wire [IDWID-1:0] splitter0_merger2_arid ;
wire [31:0] splitter0_merger2_araddr ;
wire [7:0] splitter0_merger2_arlen ;
wire [EXTRAS-1:0] splitter0_merger2_arextras ;
wire [1:0] splitter0_merger2_arburst ;
wire splitter0_merger2_arvalid ;
wire splitter0_merger2_arready ;
wire [IDWID-1:0] splitter0_merger2_rid ;
wire [DWID-1:0] splitter0_merger2_rdata ;
wire [1:0] splitter0_merger2_rresp ;
wire splitter0_merger2_rlast ;
wire splitter0_merger2_rvalid ;
wire splitter0_merger2_rready ;

wire [IDWID-1:0] splitter0_merger2_awid ;
wire [31:0] splitter0_merger2_awaddr ;
wire [7:0] splitter0_merger2_awlen ;
wire [EXTRAS-1:0] splitter0_merger2_awextras ;
wire [1:0] splitter0_merger2_awburst ;
wire splitter0_merger2_awvalid ;
wire splitter0_merger2_awready ;
wire [DWID-1:0] splitter0_merger2_wdata ;
wire [WSTRB-1:0] splitter0_merger2_wstrb ;
wire splitter0_merger2_wlast ;
wire splitter0_merger2_wvalid ;
wire splitter0_merger2_wready ;
wire [IDWID-1:0] splitter0_merger2_bid ;
wire [1:0] splitter0_merger2_bresp ;
wire splitter0_merger2_bvalid ;
wire splitter0_merger2_bready ;


wire [IDWID-1:0] splitter0_merger3_arid ;
wire [31:0] splitter0_merger3_araddr ;
wire [7:0] splitter0_merger3_arlen ;
wire [EXTRAS-1:0] splitter0_merger3_arextras ;
wire [1:0] splitter0_merger3_arburst ;
wire splitter0_merger3_arvalid ;
wire splitter0_merger3_arready ;
wire [IDWID-1:0] splitter0_merger3_rid ;
wire [DWID-1:0] splitter0_merger3_rdata ;
wire [1:0] splitter0_merger3_rresp ;
wire splitter0_merger3_rlast ;
wire splitter0_merger3_rvalid ;
wire splitter0_merger3_rready ;

wire [IDWID-1:0] splitter0_merger3_awid ;
wire [31:0] splitter0_merger3_awaddr ;
wire [7:0] splitter0_merger3_awlen ;
wire [EXTRAS-1:0] splitter0_merger3_awextras ;
wire [1:0] splitter0_merger3_awburst ;
wire splitter0_merger3_awvalid ;
wire splitter0_merger3_awready ;
wire [DWID-1:0] splitter0_merger3_wdata ;
wire [WSTRB-1:0] splitter0_merger3_wstrb ;
wire splitter0_merger3_wlast ;
wire splitter0_merger3_wvalid ;
wire splitter0_merger3_wready ;
wire [IDWID-1:0] splitter0_merger3_bid ;
wire [1:0] splitter0_merger3_bresp ;
wire splitter0_merger3_bvalid ;
wire splitter0_merger3_bready ;


axi_4_splitter splitter0 (
     .clk(clk) ,.rst_n(rst_n)

    ,.araddr(mst0_araddr[31:0])
    ,.arburst(mst0_arburst[1:0])
    ,.arextras(mst0_arextras[(EXTRAS - 1):0])
    ,.arid(mst0_arid[(IDWID - 1):0])
    ,.arlen(mst0_arlen[7:0])
    ,.arready(mst0_arready)
    ,.arvalid(mst0_arvalid)
    ,.awaddr(mst0_awaddr[31:0])
    ,.awburst(mst0_awburst[1:0])
    ,.awextras(mst0_awextras[(EXTRAS - 1):0])
    ,.awid(mst0_awid[3:0])
    ,.awlen(mst0_awlen[7:0])
    ,.awready(mst0_awready)
    ,.awvalid(mst0_awvalid)
    ,.bid(mst0_bid[(IDWID - 1):0])
    ,.bready(mst0_bready)
    ,.bresp(mst0_bresp[1:0])
    ,.bvalid(mst0_bvalid)
    ,.rdata(mst0_rdata[(DWID - 1):0])
    ,.rid(mst0_rid[(IDWID - 1):0])
    ,.rlast(mst0_rlast)
    ,.rready(mst0_rready)
    ,.rresp(mst0_rresp[1:0])
    ,.rvalid(mst0_rvalid)
    ,.wdata(mst0_wdata[(DWID - 1):0])
    ,.wlast(mst0_wlast)
    ,.wready(mst0_wready)
    ,.wstrb(mst0_wstrb[(WSTRB - 1):0])
    ,.wvalid(mst0_wvalid)

    ,.a_araddr(splitter0_merger0_araddr[31:0])
    ,.a_arburst(splitter0_merger0_arburst[1:0])
    ,.a_arextras(splitter0_merger0_arextras[(EXTRAS - 1):0])
    ,.a_arid(splitter0_merger0_arid[(IDWID - 1):0])
    ,.a_arlen(splitter0_merger0_arlen[7:0])
    ,.a_arready(splitter0_merger0_arready)
    ,.a_arvalid(splitter0_merger0_arvalid)
    ,.a_awaddr(splitter0_merger0_awaddr[31:0])
    ,.a_awburst(splitter0_merger0_awburst[1:0])
    ,.a_awextras(splitter0_merger0_awextras[(EXTRAS - 1):0])
    ,.a_awid(splitter0_merger0_awid[(IDWID - 1):0])
    ,.a_awlen(splitter0_merger0_awlen[7:0])
    ,.a_awready(splitter0_merger0_awready)
    ,.a_awvalid(splitter0_merger0_awvalid)
    ,.a_bid(splitter0_merger0_bid[(IDWID - 1):0])
    ,.a_bready(splitter0_merger0_bready)
    ,.a_bresp(splitter0_merger0_bresp[1:0])
    ,.a_bvalid(splitter0_merger0_bvalid)
    ,.a_rdata(splitter0_merger0_rdata[(DWID - 1):0])
    ,.a_rid(splitter0_merger0_rid[(IDWID - 1):0])
    ,.a_rlast(splitter0_merger0_rlast)
    ,.a_rready(splitter0_merger0_rready)
    ,.a_rresp(splitter0_merger0_rresp[1:0])
    ,.a_rvalid(splitter0_merger0_rvalid)
    ,.a_wdata(splitter0_merger0_wdata[(DWID - 1):0])
    ,.a_wlast(splitter0_merger0_wlast)
    ,.a_wready(splitter0_merger0_wready)
    ,.a_wstrb(splitter0_merger0_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(splitter0_merger0_wvalid)
    ,.b_araddr(splitter0_merger1_araddr[31:0])
    ,.b_arburst(splitter0_merger1_arburst[1:0])
    ,.b_arextras(splitter0_merger1_arextras[(EXTRAS - 1):0])
    ,.b_arid(splitter0_merger1_arid[(IDWID - 1):0])
    ,.b_arlen(splitter0_merger1_arlen[7:0])
    ,.b_arready(splitter0_merger1_arready)
    ,.b_arvalid(splitter0_merger1_arvalid)
    ,.b_awaddr(splitter0_merger1_awaddr[31:0])
    ,.b_awburst(splitter0_merger1_awburst[1:0])
    ,.b_awextras(splitter0_merger1_awextras[(EXTRAS - 1):0])
    ,.b_awid(splitter0_merger1_awid[(IDWID - 1):0])
    ,.b_awlen(splitter0_merger1_awlen[7:0])
    ,.b_awready(splitter0_merger1_awready)
    ,.b_awvalid(splitter0_merger1_awvalid)
    ,.b_bid(splitter0_merger1_bid[(IDWID - 1):0])
    ,.b_bready(splitter0_merger1_bready)
    ,.b_bresp(splitter0_merger1_bresp[1:0])
    ,.b_bvalid(splitter0_merger1_bvalid)
    ,.b_rdata(splitter0_merger1_rdata[(DWID - 1):0])
    ,.b_rid(splitter0_merger1_rid[(IDWID - 1):0])
    ,.b_rlast(splitter0_merger1_rlast)
    ,.b_rready(splitter0_merger1_rready)
    ,.b_rresp(splitter0_merger1_rresp[1:0])
    ,.b_rvalid(splitter0_merger1_rvalid)
    ,.b_wdata(splitter0_merger1_wdata[(DWID - 1):0])
    ,.b_wlast(splitter0_merger1_wlast)
    ,.b_wready(splitter0_merger1_wready)
    ,.b_wstrb(splitter0_merger1_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(splitter0_merger1_wvalid)
    ,.c_araddr(splitter0_merger2_araddr[31:0])
    ,.c_arburst(splitter0_merger2_arburst[1:0])
    ,.c_arextras(splitter0_merger2_arextras[(EXTRAS - 1):0])
    ,.c_arid(splitter0_merger2_arid[(IDWID - 1):0])
    ,.c_arlen(splitter0_merger2_arlen[7:0])
    ,.c_arready(splitter0_merger2_arready)
    ,.c_arvalid(splitter0_merger2_arvalid)
    ,.c_awaddr(splitter0_merger2_awaddr[31:0])
    ,.c_awburst(splitter0_merger2_awburst[1:0])
    ,.c_awextras(splitter0_merger2_awextras[(EXTRAS - 1):0])
    ,.c_awid(splitter0_merger2_awid[(IDWID - 1):0])
    ,.c_awlen(splitter0_merger2_awlen[7:0])
    ,.c_awready(splitter0_merger2_awready)
    ,.c_awvalid(splitter0_merger2_awvalid)
    ,.c_bid(splitter0_merger2_bid[(IDWID - 1):0])
    ,.c_bready(splitter0_merger2_bready)
    ,.c_bresp(splitter0_merger2_bresp[1:0])
    ,.c_bvalid(splitter0_merger2_bvalid)
    ,.c_rdata(splitter0_merger2_rdata[(DWID - 1):0])
    ,.c_rid(splitter0_merger2_rid[(IDWID - 1):0])
    ,.c_rlast(splitter0_merger2_rlast)
    ,.c_rready(splitter0_merger2_rready)
    ,.c_rresp(splitter0_merger2_rresp[1:0])
    ,.c_rvalid(splitter0_merger2_rvalid)
    ,.c_wdata(splitter0_merger2_wdata[(DWID - 1):0])
    ,.c_wlast(splitter0_merger2_wlast)
    ,.c_wready(splitter0_merger2_wready)
    ,.c_wstrb(splitter0_merger2_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(splitter0_merger2_wvalid)
    ,.d_araddr(splitter0_merger3_araddr[31:0])
    ,.d_arburst(splitter0_merger3_arburst[1:0])
    ,.d_arextras(splitter0_merger3_arextras[(EXTRAS - 1):0])
    ,.d_arid(splitter0_merger3_arid[(IDWID - 1):0])
    ,.d_arlen(splitter0_merger3_arlen[7:0])
    ,.d_arready(splitter0_merger3_arready)
    ,.d_arvalid(splitter0_merger3_arvalid)
    ,.d_awaddr(splitter0_merger3_awaddr[31:0])
    ,.d_awburst(splitter0_merger3_awburst[1:0])
    ,.d_awextras(splitter0_merger3_awextras[(EXTRAS - 1):0])
    ,.d_awid(splitter0_merger3_awid[(IDWID - 1):0])
    ,.d_awlen(splitter0_merger3_awlen[7:0])
    ,.d_awready(splitter0_merger3_awready)
    ,.d_awvalid(splitter0_merger3_awvalid)
    ,.d_bid(splitter0_merger3_bid[(IDWID - 1):0])
    ,.d_bready(splitter0_merger3_bready)
    ,.d_bresp(splitter0_merger3_bresp[1:0])
    ,.d_bvalid(splitter0_merger3_bvalid)
    ,.d_rdata(splitter0_merger3_rdata[(DWID - 1):0])
    ,.d_rid(splitter0_merger3_rid[(IDWID - 1):0])
    ,.d_rlast(splitter0_merger3_rlast)
    ,.d_rready(splitter0_merger3_rready)
    ,.d_rresp(splitter0_merger3_rresp[1:0])
    ,.d_rvalid(splitter0_merger3_rvalid)
    ,.d_wdata(splitter0_merger3_wdata[(DWID - 1):0])
    ,.d_wlast(splitter0_merger3_wlast)
    ,.d_wready(splitter0_merger3_wready)
    ,.d_wstrb(splitter0_merger3_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(splitter0_merger3_wvalid)

);

wire [IDWID-1:0] splitter1_merger0_arid ;
wire [31:0] splitter1_merger0_araddr ;
wire [7:0] splitter1_merger0_arlen ;
wire [EXTRAS-1:0] splitter1_merger0_arextras ;
wire [1:0] splitter1_merger0_arburst ;
wire splitter1_merger0_arvalid ;
wire splitter1_merger0_arready ;
wire [IDWID-1:0] splitter1_merger0_rid ;
wire [DWID-1:0] splitter1_merger0_rdata ;
wire [1:0] splitter1_merger0_rresp ;
wire splitter1_merger0_rlast ;
wire splitter1_merger0_rvalid ;
wire splitter1_merger0_rready ;

wire [IDWID-1:0] splitter1_merger0_awid ;
wire [31:0] splitter1_merger0_awaddr ;
wire [7:0] splitter1_merger0_awlen ;
wire [EXTRAS-1:0] splitter1_merger0_awextras ;
wire [1:0] splitter1_merger0_awburst ;
wire splitter1_merger0_awvalid ;
wire splitter1_merger0_awready ;
wire [DWID-1:0] splitter1_merger0_wdata ;
wire [WSTRB-1:0] splitter1_merger0_wstrb ;
wire splitter1_merger0_wlast ;
wire splitter1_merger0_wvalid ;
wire splitter1_merger0_wready ;
wire [IDWID-1:0] splitter1_merger0_bid ;
wire [1:0] splitter1_merger0_bresp ;
wire splitter1_merger0_bvalid ;
wire splitter1_merger0_bready ;


wire [IDWID-1:0] splitter1_merger1_arid ;
wire [31:0] splitter1_merger1_araddr ;
wire [7:0] splitter1_merger1_arlen ;
wire [EXTRAS-1:0] splitter1_merger1_arextras ;
wire [1:0] splitter1_merger1_arburst ;
wire splitter1_merger1_arvalid ;
wire splitter1_merger1_arready ;
wire [IDWID-1:0] splitter1_merger1_rid ;
wire [DWID-1:0] splitter1_merger1_rdata ;
wire [1:0] splitter1_merger1_rresp ;
wire splitter1_merger1_rlast ;
wire splitter1_merger1_rvalid ;
wire splitter1_merger1_rready ;

wire [IDWID-1:0] splitter1_merger1_awid ;
wire [31:0] splitter1_merger1_awaddr ;
wire [7:0] splitter1_merger1_awlen ;
wire [EXTRAS-1:0] splitter1_merger1_awextras ;
wire [1:0] splitter1_merger1_awburst ;
wire splitter1_merger1_awvalid ;
wire splitter1_merger1_awready ;
wire [DWID-1:0] splitter1_merger1_wdata ;
wire [WSTRB-1:0] splitter1_merger1_wstrb ;
wire splitter1_merger1_wlast ;
wire splitter1_merger1_wvalid ;
wire splitter1_merger1_wready ;
wire [IDWID-1:0] splitter1_merger1_bid ;
wire [1:0] splitter1_merger1_bresp ;
wire splitter1_merger1_bvalid ;
wire splitter1_merger1_bready ;


wire [IDWID-1:0] splitter1_merger2_arid ;
wire [31:0] splitter1_merger2_araddr ;
wire [7:0] splitter1_merger2_arlen ;
wire [EXTRAS-1:0] splitter1_merger2_arextras ;
wire [1:0] splitter1_merger2_arburst ;
wire splitter1_merger2_arvalid ;
wire splitter1_merger2_arready ;
wire [IDWID-1:0] splitter1_merger2_rid ;
wire [DWID-1:0] splitter1_merger2_rdata ;
wire [1:0] splitter1_merger2_rresp ;
wire splitter1_merger2_rlast ;
wire splitter1_merger2_rvalid ;
wire splitter1_merger2_rready ;

wire [IDWID-1:0] splitter1_merger2_awid ;
wire [31:0] splitter1_merger2_awaddr ;
wire [7:0] splitter1_merger2_awlen ;
wire [EXTRAS-1:0] splitter1_merger2_awextras ;
wire [1:0] splitter1_merger2_awburst ;
wire splitter1_merger2_awvalid ;
wire splitter1_merger2_awready ;
wire [DWID-1:0] splitter1_merger2_wdata ;
wire [WSTRB-1:0] splitter1_merger2_wstrb ;
wire splitter1_merger2_wlast ;
wire splitter1_merger2_wvalid ;
wire splitter1_merger2_wready ;
wire [IDWID-1:0] splitter1_merger2_bid ;
wire [1:0] splitter1_merger2_bresp ;
wire splitter1_merger2_bvalid ;
wire splitter1_merger2_bready ;


wire [IDWID-1:0] splitter1_merger3_arid ;
wire [31:0] splitter1_merger3_araddr ;
wire [7:0] splitter1_merger3_arlen ;
wire [EXTRAS-1:0] splitter1_merger3_arextras ;
wire [1:0] splitter1_merger3_arburst ;
wire splitter1_merger3_arvalid ;
wire splitter1_merger3_arready ;
wire [IDWID-1:0] splitter1_merger3_rid ;
wire [DWID-1:0] splitter1_merger3_rdata ;
wire [1:0] splitter1_merger3_rresp ;
wire splitter1_merger3_rlast ;
wire splitter1_merger3_rvalid ;
wire splitter1_merger3_rready ;

wire [IDWID-1:0] splitter1_merger3_awid ;
wire [31:0] splitter1_merger3_awaddr ;
wire [7:0] splitter1_merger3_awlen ;
wire [EXTRAS-1:0] splitter1_merger3_awextras ;
wire [1:0] splitter1_merger3_awburst ;
wire splitter1_merger3_awvalid ;
wire splitter1_merger3_awready ;
wire [DWID-1:0] splitter1_merger3_wdata ;
wire [WSTRB-1:0] splitter1_merger3_wstrb ;
wire splitter1_merger3_wlast ;
wire splitter1_merger3_wvalid ;
wire splitter1_merger3_wready ;
wire [IDWID-1:0] splitter1_merger3_bid ;
wire [1:0] splitter1_merger3_bresp ;
wire splitter1_merger3_bvalid ;
wire splitter1_merger3_bready ;


axi_4_splitter splitter1 (
     .clk(clk) ,.rst_n(rst_n)

    ,.araddr(mst1_araddr[31:0])
    ,.arburst(mst1_arburst[1:0])
    ,.arextras(mst1_arextras[(EXTRAS - 1):0])
    ,.arid(mst1_arid[(IDWID - 1):0])
    ,.arlen(mst1_arlen[7:0])
    ,.arready(mst1_arready)
    ,.arvalid(mst1_arvalid)
    ,.awaddr(mst1_awaddr[31:0])
    ,.awburst(mst1_awburst[1:0])
    ,.awextras(mst1_awextras[(EXTRAS - 1):0])
    ,.awid(mst1_awid[3:0])
    ,.awlen(mst1_awlen[7:0])
    ,.awready(mst1_awready)
    ,.awvalid(mst1_awvalid)
    ,.bid(mst1_bid[(IDWID - 1):0])
    ,.bready(mst1_bready)
    ,.bresp(mst1_bresp[1:0])
    ,.bvalid(mst1_bvalid)
    ,.rdata(mst1_rdata[(DWID - 1):0])
    ,.rid(mst1_rid[(IDWID - 1):0])
    ,.rlast(mst1_rlast)
    ,.rready(mst1_rready)
    ,.rresp(mst1_rresp[1:0])
    ,.rvalid(mst1_rvalid)
    ,.wdata(mst1_wdata[(DWID - 1):0])
    ,.wlast(mst1_wlast)
    ,.wready(mst1_wready)
    ,.wstrb(mst1_wstrb[(WSTRB - 1):0])
    ,.wvalid(mst1_wvalid)

    ,.a_araddr(splitter1_merger0_araddr[31:0])
    ,.a_arburst(splitter1_merger0_arburst[1:0])
    ,.a_arextras(splitter1_merger0_arextras[(EXTRAS - 1):0])
    ,.a_arid(splitter1_merger0_arid[(IDWID - 1):0])
    ,.a_arlen(splitter1_merger0_arlen[7:0])
    ,.a_arready(splitter1_merger0_arready)
    ,.a_arvalid(splitter1_merger0_arvalid)
    ,.a_awaddr(splitter1_merger0_awaddr[31:0])
    ,.a_awburst(splitter1_merger0_awburst[1:0])
    ,.a_awextras(splitter1_merger0_awextras[(EXTRAS - 1):0])
    ,.a_awid(splitter1_merger0_awid[(IDWID - 1):0])
    ,.a_awlen(splitter1_merger0_awlen[7:0])
    ,.a_awready(splitter1_merger0_awready)
    ,.a_awvalid(splitter1_merger0_awvalid)
    ,.a_bid(splitter1_merger0_bid[(IDWID - 1):0])
    ,.a_bready(splitter1_merger0_bready)
    ,.a_bresp(splitter1_merger0_bresp[1:0])
    ,.a_bvalid(splitter1_merger0_bvalid)
    ,.a_rdata(splitter1_merger0_rdata[(DWID - 1):0])
    ,.a_rid(splitter1_merger0_rid[(IDWID - 1):0])
    ,.a_rlast(splitter1_merger0_rlast)
    ,.a_rready(splitter1_merger0_rready)
    ,.a_rresp(splitter1_merger0_rresp[1:0])
    ,.a_rvalid(splitter1_merger0_rvalid)
    ,.a_wdata(splitter1_merger0_wdata[(DWID - 1):0])
    ,.a_wlast(splitter1_merger0_wlast)
    ,.a_wready(splitter1_merger0_wready)
    ,.a_wstrb(splitter1_merger0_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(splitter1_merger0_wvalid)
    ,.b_araddr(splitter1_merger1_araddr[31:0])
    ,.b_arburst(splitter1_merger1_arburst[1:0])
    ,.b_arextras(splitter1_merger1_arextras[(EXTRAS - 1):0])
    ,.b_arid(splitter1_merger1_arid[(IDWID - 1):0])
    ,.b_arlen(splitter1_merger1_arlen[7:0])
    ,.b_arready(splitter1_merger1_arready)
    ,.b_arvalid(splitter1_merger1_arvalid)
    ,.b_awaddr(splitter1_merger1_awaddr[31:0])
    ,.b_awburst(splitter1_merger1_awburst[1:0])
    ,.b_awextras(splitter1_merger1_awextras[(EXTRAS - 1):0])
    ,.b_awid(splitter1_merger1_awid[(IDWID - 1):0])
    ,.b_awlen(splitter1_merger1_awlen[7:0])
    ,.b_awready(splitter1_merger1_awready)
    ,.b_awvalid(splitter1_merger1_awvalid)
    ,.b_bid(splitter1_merger1_bid[(IDWID - 1):0])
    ,.b_bready(splitter1_merger1_bready)
    ,.b_bresp(splitter1_merger1_bresp[1:0])
    ,.b_bvalid(splitter1_merger1_bvalid)
    ,.b_rdata(splitter1_merger1_rdata[(DWID - 1):0])
    ,.b_rid(splitter1_merger1_rid[(IDWID - 1):0])
    ,.b_rlast(splitter1_merger1_rlast)
    ,.b_rready(splitter1_merger1_rready)
    ,.b_rresp(splitter1_merger1_rresp[1:0])
    ,.b_rvalid(splitter1_merger1_rvalid)
    ,.b_wdata(splitter1_merger1_wdata[(DWID - 1):0])
    ,.b_wlast(splitter1_merger1_wlast)
    ,.b_wready(splitter1_merger1_wready)
    ,.b_wstrb(splitter1_merger1_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(splitter1_merger1_wvalid)
    ,.c_araddr(splitter1_merger2_araddr[31:0])
    ,.c_arburst(splitter1_merger2_arburst[1:0])
    ,.c_arextras(splitter1_merger2_arextras[(EXTRAS - 1):0])
    ,.c_arid(splitter1_merger2_arid[(IDWID - 1):0])
    ,.c_arlen(splitter1_merger2_arlen[7:0])
    ,.c_arready(splitter1_merger2_arready)
    ,.c_arvalid(splitter1_merger2_arvalid)
    ,.c_awaddr(splitter1_merger2_awaddr[31:0])
    ,.c_awburst(splitter1_merger2_awburst[1:0])
    ,.c_awextras(splitter1_merger2_awextras[(EXTRAS - 1):0])
    ,.c_awid(splitter1_merger2_awid[(IDWID - 1):0])
    ,.c_awlen(splitter1_merger2_awlen[7:0])
    ,.c_awready(splitter1_merger2_awready)
    ,.c_awvalid(splitter1_merger2_awvalid)
    ,.c_bid(splitter1_merger2_bid[(IDWID - 1):0])
    ,.c_bready(splitter1_merger2_bready)
    ,.c_bresp(splitter1_merger2_bresp[1:0])
    ,.c_bvalid(splitter1_merger2_bvalid)
    ,.c_rdata(splitter1_merger2_rdata[(DWID - 1):0])
    ,.c_rid(splitter1_merger2_rid[(IDWID - 1):0])
    ,.c_rlast(splitter1_merger2_rlast)
    ,.c_rready(splitter1_merger2_rready)
    ,.c_rresp(splitter1_merger2_rresp[1:0])
    ,.c_rvalid(splitter1_merger2_rvalid)
    ,.c_wdata(splitter1_merger2_wdata[(DWID - 1):0])
    ,.c_wlast(splitter1_merger2_wlast)
    ,.c_wready(splitter1_merger2_wready)
    ,.c_wstrb(splitter1_merger2_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(splitter1_merger2_wvalid)
    ,.d_araddr(splitter1_merger3_araddr[31:0])
    ,.d_arburst(splitter1_merger3_arburst[1:0])
    ,.d_arextras(splitter1_merger3_arextras[(EXTRAS - 1):0])
    ,.d_arid(splitter1_merger3_arid[(IDWID - 1):0])
    ,.d_arlen(splitter1_merger3_arlen[7:0])
    ,.d_arready(splitter1_merger3_arready)
    ,.d_arvalid(splitter1_merger3_arvalid)
    ,.d_awaddr(splitter1_merger3_awaddr[31:0])
    ,.d_awburst(splitter1_merger3_awburst[1:0])
    ,.d_awextras(splitter1_merger3_awextras[(EXTRAS - 1):0])
    ,.d_awid(splitter1_merger3_awid[(IDWID - 1):0])
    ,.d_awlen(splitter1_merger3_awlen[7:0])
    ,.d_awready(splitter1_merger3_awready)
    ,.d_awvalid(splitter1_merger3_awvalid)
    ,.d_bid(splitter1_merger3_bid[(IDWID - 1):0])
    ,.d_bready(splitter1_merger3_bready)
    ,.d_bresp(splitter1_merger3_bresp[1:0])
    ,.d_bvalid(splitter1_merger3_bvalid)
    ,.d_rdata(splitter1_merger3_rdata[(DWID - 1):0])
    ,.d_rid(splitter1_merger3_rid[(IDWID - 1):0])
    ,.d_rlast(splitter1_merger3_rlast)
    ,.d_rready(splitter1_merger3_rready)
    ,.d_rresp(splitter1_merger3_rresp[1:0])
    ,.d_rvalid(splitter1_merger3_rvalid)
    ,.d_wdata(splitter1_merger3_wdata[(DWID - 1):0])
    ,.d_wlast(splitter1_merger3_wlast)
    ,.d_wready(splitter1_merger3_wready)
    ,.d_wstrb(splitter1_merger3_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(splitter1_merger3_wvalid)

);

wire [IDWID-1:0] splitter2_merger0_arid ;
wire [31:0] splitter2_merger0_araddr ;
wire [7:0] splitter2_merger0_arlen ;
wire [EXTRAS-1:0] splitter2_merger0_arextras ;
wire [1:0] splitter2_merger0_arburst ;
wire splitter2_merger0_arvalid ;
wire splitter2_merger0_arready ;
wire [IDWID-1:0] splitter2_merger0_rid ;
wire [DWID-1:0] splitter2_merger0_rdata ;
wire [1:0] splitter2_merger0_rresp ;
wire splitter2_merger0_rlast ;
wire splitter2_merger0_rvalid ;
wire splitter2_merger0_rready ;

wire [IDWID-1:0] splitter2_merger0_awid ;
wire [31:0] splitter2_merger0_awaddr ;
wire [7:0] splitter2_merger0_awlen ;
wire [EXTRAS-1:0] splitter2_merger0_awextras ;
wire [1:0] splitter2_merger0_awburst ;
wire splitter2_merger0_awvalid ;
wire splitter2_merger0_awready ;
wire [DWID-1:0] splitter2_merger0_wdata ;
wire [WSTRB-1:0] splitter2_merger0_wstrb ;
wire splitter2_merger0_wlast ;
wire splitter2_merger0_wvalid ;
wire splitter2_merger0_wready ;
wire [IDWID-1:0] splitter2_merger0_bid ;
wire [1:0] splitter2_merger0_bresp ;
wire splitter2_merger0_bvalid ;
wire splitter2_merger0_bready ;


wire [IDWID-1:0] splitter2_merger1_arid ;
wire [31:0] splitter2_merger1_araddr ;
wire [7:0] splitter2_merger1_arlen ;
wire [EXTRAS-1:0] splitter2_merger1_arextras ;
wire [1:0] splitter2_merger1_arburst ;
wire splitter2_merger1_arvalid ;
wire splitter2_merger1_arready ;
wire [IDWID-1:0] splitter2_merger1_rid ;
wire [DWID-1:0] splitter2_merger1_rdata ;
wire [1:0] splitter2_merger1_rresp ;
wire splitter2_merger1_rlast ;
wire splitter2_merger1_rvalid ;
wire splitter2_merger1_rready ;

wire [IDWID-1:0] splitter2_merger1_awid ;
wire [31:0] splitter2_merger1_awaddr ;
wire [7:0] splitter2_merger1_awlen ;
wire [EXTRAS-1:0] splitter2_merger1_awextras ;
wire [1:0] splitter2_merger1_awburst ;
wire splitter2_merger1_awvalid ;
wire splitter2_merger1_awready ;
wire [DWID-1:0] splitter2_merger1_wdata ;
wire [WSTRB-1:0] splitter2_merger1_wstrb ;
wire splitter2_merger1_wlast ;
wire splitter2_merger1_wvalid ;
wire splitter2_merger1_wready ;
wire [IDWID-1:0] splitter2_merger1_bid ;
wire [1:0] splitter2_merger1_bresp ;
wire splitter2_merger1_bvalid ;
wire splitter2_merger1_bready ;


wire [IDWID-1:0] splitter2_merger2_arid ;
wire [31:0] splitter2_merger2_araddr ;
wire [7:0] splitter2_merger2_arlen ;
wire [EXTRAS-1:0] splitter2_merger2_arextras ;
wire [1:0] splitter2_merger2_arburst ;
wire splitter2_merger2_arvalid ;
wire splitter2_merger2_arready ;
wire [IDWID-1:0] splitter2_merger2_rid ;
wire [DWID-1:0] splitter2_merger2_rdata ;
wire [1:0] splitter2_merger2_rresp ;
wire splitter2_merger2_rlast ;
wire splitter2_merger2_rvalid ;
wire splitter2_merger2_rready ;

wire [IDWID-1:0] splitter2_merger2_awid ;
wire [31:0] splitter2_merger2_awaddr ;
wire [7:0] splitter2_merger2_awlen ;
wire [EXTRAS-1:0] splitter2_merger2_awextras ;
wire [1:0] splitter2_merger2_awburst ;
wire splitter2_merger2_awvalid ;
wire splitter2_merger2_awready ;
wire [DWID-1:0] splitter2_merger2_wdata ;
wire [WSTRB-1:0] splitter2_merger2_wstrb ;
wire splitter2_merger2_wlast ;
wire splitter2_merger2_wvalid ;
wire splitter2_merger2_wready ;
wire [IDWID-1:0] splitter2_merger2_bid ;
wire [1:0] splitter2_merger2_bresp ;
wire splitter2_merger2_bvalid ;
wire splitter2_merger2_bready ;


wire [IDWID-1:0] splitter2_merger3_arid ;
wire [31:0] splitter2_merger3_araddr ;
wire [7:0] splitter2_merger3_arlen ;
wire [EXTRAS-1:0] splitter2_merger3_arextras ;
wire [1:0] splitter2_merger3_arburst ;
wire splitter2_merger3_arvalid ;
wire splitter2_merger3_arready ;
wire [IDWID-1:0] splitter2_merger3_rid ;
wire [DWID-1:0] splitter2_merger3_rdata ;
wire [1:0] splitter2_merger3_rresp ;
wire splitter2_merger3_rlast ;
wire splitter2_merger3_rvalid ;
wire splitter2_merger3_rready ;

wire [IDWID-1:0] splitter2_merger3_awid ;
wire [31:0] splitter2_merger3_awaddr ;
wire [7:0] splitter2_merger3_awlen ;
wire [EXTRAS-1:0] splitter2_merger3_awextras ;
wire [1:0] splitter2_merger3_awburst ;
wire splitter2_merger3_awvalid ;
wire splitter2_merger3_awready ;
wire [DWID-1:0] splitter2_merger3_wdata ;
wire [WSTRB-1:0] splitter2_merger3_wstrb ;
wire splitter2_merger3_wlast ;
wire splitter2_merger3_wvalid ;
wire splitter2_merger3_wready ;
wire [IDWID-1:0] splitter2_merger3_bid ;
wire [1:0] splitter2_merger3_bresp ;
wire splitter2_merger3_bvalid ;
wire splitter2_merger3_bready ;


axi_4_splitter splitter2 (
     .clk(clk) ,.rst_n(rst_n)

    ,.araddr(mst2_araddr[31:0])
    ,.arburst(mst2_arburst[1:0])
    ,.arextras(mst2_arextras[(EXTRAS - 1):0])
    ,.arid(mst2_arid[(IDWID - 1):0])
    ,.arlen(mst2_arlen[7:0])
    ,.arready(mst2_arready)
    ,.arvalid(mst2_arvalid)
    ,.awaddr(mst2_awaddr[31:0])
    ,.awburst(mst2_awburst[1:0])
    ,.awextras(mst2_awextras[(EXTRAS - 1):0])
    ,.awid(mst2_awid[3:0])
    ,.awlen(mst2_awlen[7:0])
    ,.awready(mst2_awready)
    ,.awvalid(mst2_awvalid)
    ,.bid(mst2_bid[(IDWID - 1):0])
    ,.bready(mst2_bready)
    ,.bresp(mst2_bresp[1:0])
    ,.bvalid(mst2_bvalid)
    ,.rdata(mst2_rdata[(DWID - 1):0])
    ,.rid(mst2_rid[(IDWID - 1):0])
    ,.rlast(mst2_rlast)
    ,.rready(mst2_rready)
    ,.rresp(mst2_rresp[1:0])
    ,.rvalid(mst2_rvalid)
    ,.wdata(mst2_wdata[(DWID - 1):0])
    ,.wlast(mst2_wlast)
    ,.wready(mst2_wready)
    ,.wstrb(mst2_wstrb[(WSTRB - 1):0])
    ,.wvalid(mst2_wvalid)

    ,.a_araddr(splitter2_merger0_araddr[31:0])
    ,.a_arburst(splitter2_merger0_arburst[1:0])
    ,.a_arextras(splitter2_merger0_arextras[(EXTRAS - 1):0])
    ,.a_arid(splitter2_merger0_arid[(IDWID - 1):0])
    ,.a_arlen(splitter2_merger0_arlen[7:0])
    ,.a_arready(splitter2_merger0_arready)
    ,.a_arvalid(splitter2_merger0_arvalid)
    ,.a_awaddr(splitter2_merger0_awaddr[31:0])
    ,.a_awburst(splitter2_merger0_awburst[1:0])
    ,.a_awextras(splitter2_merger0_awextras[(EXTRAS - 1):0])
    ,.a_awid(splitter2_merger0_awid[(IDWID - 1):0])
    ,.a_awlen(splitter2_merger0_awlen[7:0])
    ,.a_awready(splitter2_merger0_awready)
    ,.a_awvalid(splitter2_merger0_awvalid)
    ,.a_bid(splitter2_merger0_bid[(IDWID - 1):0])
    ,.a_bready(splitter2_merger0_bready)
    ,.a_bresp(splitter2_merger0_bresp[1:0])
    ,.a_bvalid(splitter2_merger0_bvalid)
    ,.a_rdata(splitter2_merger0_rdata[(DWID - 1):0])
    ,.a_rid(splitter2_merger0_rid[(IDWID - 1):0])
    ,.a_rlast(splitter2_merger0_rlast)
    ,.a_rready(splitter2_merger0_rready)
    ,.a_rresp(splitter2_merger0_rresp[1:0])
    ,.a_rvalid(splitter2_merger0_rvalid)
    ,.a_wdata(splitter2_merger0_wdata[(DWID - 1):0])
    ,.a_wlast(splitter2_merger0_wlast)
    ,.a_wready(splitter2_merger0_wready)
    ,.a_wstrb(splitter2_merger0_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(splitter2_merger0_wvalid)
    ,.b_araddr(splitter2_merger1_araddr[31:0])
    ,.b_arburst(splitter2_merger1_arburst[1:0])
    ,.b_arextras(splitter2_merger1_arextras[(EXTRAS - 1):0])
    ,.b_arid(splitter2_merger1_arid[(IDWID - 1):0])
    ,.b_arlen(splitter2_merger1_arlen[7:0])
    ,.b_arready(splitter2_merger1_arready)
    ,.b_arvalid(splitter2_merger1_arvalid)
    ,.b_awaddr(splitter2_merger1_awaddr[31:0])
    ,.b_awburst(splitter2_merger1_awburst[1:0])
    ,.b_awextras(splitter2_merger1_awextras[(EXTRAS - 1):0])
    ,.b_awid(splitter2_merger1_awid[(IDWID - 1):0])
    ,.b_awlen(splitter2_merger1_awlen[7:0])
    ,.b_awready(splitter2_merger1_awready)
    ,.b_awvalid(splitter2_merger1_awvalid)
    ,.b_bid(splitter2_merger1_bid[(IDWID - 1):0])
    ,.b_bready(splitter2_merger1_bready)
    ,.b_bresp(splitter2_merger1_bresp[1:0])
    ,.b_bvalid(splitter2_merger1_bvalid)
    ,.b_rdata(splitter2_merger1_rdata[(DWID - 1):0])
    ,.b_rid(splitter2_merger1_rid[(IDWID - 1):0])
    ,.b_rlast(splitter2_merger1_rlast)
    ,.b_rready(splitter2_merger1_rready)
    ,.b_rresp(splitter2_merger1_rresp[1:0])
    ,.b_rvalid(splitter2_merger1_rvalid)
    ,.b_wdata(splitter2_merger1_wdata[(DWID - 1):0])
    ,.b_wlast(splitter2_merger1_wlast)
    ,.b_wready(splitter2_merger1_wready)
    ,.b_wstrb(splitter2_merger1_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(splitter2_merger1_wvalid)
    ,.c_araddr(splitter2_merger2_araddr[31:0])
    ,.c_arburst(splitter2_merger2_arburst[1:0])
    ,.c_arextras(splitter2_merger2_arextras[(EXTRAS - 1):0])
    ,.c_arid(splitter2_merger2_arid[(IDWID - 1):0])
    ,.c_arlen(splitter2_merger2_arlen[7:0])
    ,.c_arready(splitter2_merger2_arready)
    ,.c_arvalid(splitter2_merger2_arvalid)
    ,.c_awaddr(splitter2_merger2_awaddr[31:0])
    ,.c_awburst(splitter2_merger2_awburst[1:0])
    ,.c_awextras(splitter2_merger2_awextras[(EXTRAS - 1):0])
    ,.c_awid(splitter2_merger2_awid[(IDWID - 1):0])
    ,.c_awlen(splitter2_merger2_awlen[7:0])
    ,.c_awready(splitter2_merger2_awready)
    ,.c_awvalid(splitter2_merger2_awvalid)
    ,.c_bid(splitter2_merger2_bid[(IDWID - 1):0])
    ,.c_bready(splitter2_merger2_bready)
    ,.c_bresp(splitter2_merger2_bresp[1:0])
    ,.c_bvalid(splitter2_merger2_bvalid)
    ,.c_rdata(splitter2_merger2_rdata[(DWID - 1):0])
    ,.c_rid(splitter2_merger2_rid[(IDWID - 1):0])
    ,.c_rlast(splitter2_merger2_rlast)
    ,.c_rready(splitter2_merger2_rready)
    ,.c_rresp(splitter2_merger2_rresp[1:0])
    ,.c_rvalid(splitter2_merger2_rvalid)
    ,.c_wdata(splitter2_merger2_wdata[(DWID - 1):0])
    ,.c_wlast(splitter2_merger2_wlast)
    ,.c_wready(splitter2_merger2_wready)
    ,.c_wstrb(splitter2_merger2_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(splitter2_merger2_wvalid)
    ,.d_araddr(splitter2_merger3_araddr[31:0])
    ,.d_arburst(splitter2_merger3_arburst[1:0])
    ,.d_arextras(splitter2_merger3_arextras[(EXTRAS - 1):0])
    ,.d_arid(splitter2_merger3_arid[(IDWID - 1):0])
    ,.d_arlen(splitter2_merger3_arlen[7:0])
    ,.d_arready(splitter2_merger3_arready)
    ,.d_arvalid(splitter2_merger3_arvalid)
    ,.d_awaddr(splitter2_merger3_awaddr[31:0])
    ,.d_awburst(splitter2_merger3_awburst[1:0])
    ,.d_awextras(splitter2_merger3_awextras[(EXTRAS - 1):0])
    ,.d_awid(splitter2_merger3_awid[(IDWID - 1):0])
    ,.d_awlen(splitter2_merger3_awlen[7:0])
    ,.d_awready(splitter2_merger3_awready)
    ,.d_awvalid(splitter2_merger3_awvalid)
    ,.d_bid(splitter2_merger3_bid[(IDWID - 1):0])
    ,.d_bready(splitter2_merger3_bready)
    ,.d_bresp(splitter2_merger3_bresp[1:0])
    ,.d_bvalid(splitter2_merger3_bvalid)
    ,.d_rdata(splitter2_merger3_rdata[(DWID - 1):0])
    ,.d_rid(splitter2_merger3_rid[(IDWID - 1):0])
    ,.d_rlast(splitter2_merger3_rlast)
    ,.d_rready(splitter2_merger3_rready)
    ,.d_rresp(splitter2_merger3_rresp[1:0])
    ,.d_rvalid(splitter2_merger3_rvalid)
    ,.d_wdata(splitter2_merger3_wdata[(DWID - 1):0])
    ,.d_wlast(splitter2_merger3_wlast)
    ,.d_wready(splitter2_merger3_wready)
    ,.d_wstrb(splitter2_merger3_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(splitter2_merger3_wvalid)

);

wire [IDWID-1:0] splitter3_merger0_arid ;
wire [31:0] splitter3_merger0_araddr ;
wire [7:0] splitter3_merger0_arlen ;
wire [EXTRAS-1:0] splitter3_merger0_arextras ;
wire [1:0] splitter3_merger0_arburst ;
wire splitter3_merger0_arvalid ;
wire splitter3_merger0_arready ;
wire [IDWID-1:0] splitter3_merger0_rid ;
wire [DWID-1:0] splitter3_merger0_rdata ;
wire [1:0] splitter3_merger0_rresp ;
wire splitter3_merger0_rlast ;
wire splitter3_merger0_rvalid ;
wire splitter3_merger0_rready ;

wire [IDWID-1:0] splitter3_merger0_awid ;
wire [31:0] splitter3_merger0_awaddr ;
wire [7:0] splitter3_merger0_awlen ;
wire [EXTRAS-1:0] splitter3_merger0_awextras ;
wire [1:0] splitter3_merger0_awburst ;
wire splitter3_merger0_awvalid ;
wire splitter3_merger0_awready ;
wire [DWID-1:0] splitter3_merger0_wdata ;
wire [WSTRB-1:0] splitter3_merger0_wstrb ;
wire splitter3_merger0_wlast ;
wire splitter3_merger0_wvalid ;
wire splitter3_merger0_wready ;
wire [IDWID-1:0] splitter3_merger0_bid ;
wire [1:0] splitter3_merger0_bresp ;
wire splitter3_merger0_bvalid ;
wire splitter3_merger0_bready ;


wire [IDWID-1:0] splitter3_merger1_arid ;
wire [31:0] splitter3_merger1_araddr ;
wire [7:0] splitter3_merger1_arlen ;
wire [EXTRAS-1:0] splitter3_merger1_arextras ;
wire [1:0] splitter3_merger1_arburst ;
wire splitter3_merger1_arvalid ;
wire splitter3_merger1_arready ;
wire [IDWID-1:0] splitter3_merger1_rid ;
wire [DWID-1:0] splitter3_merger1_rdata ;
wire [1:0] splitter3_merger1_rresp ;
wire splitter3_merger1_rlast ;
wire splitter3_merger1_rvalid ;
wire splitter3_merger1_rready ;

wire [IDWID-1:0] splitter3_merger1_awid ;
wire [31:0] splitter3_merger1_awaddr ;
wire [7:0] splitter3_merger1_awlen ;
wire [EXTRAS-1:0] splitter3_merger1_awextras ;
wire [1:0] splitter3_merger1_awburst ;
wire splitter3_merger1_awvalid ;
wire splitter3_merger1_awready ;
wire [DWID-1:0] splitter3_merger1_wdata ;
wire [WSTRB-1:0] splitter3_merger1_wstrb ;
wire splitter3_merger1_wlast ;
wire splitter3_merger1_wvalid ;
wire splitter3_merger1_wready ;
wire [IDWID-1:0] splitter3_merger1_bid ;
wire [1:0] splitter3_merger1_bresp ;
wire splitter3_merger1_bvalid ;
wire splitter3_merger1_bready ;


wire [IDWID-1:0] splitter3_merger2_arid ;
wire [31:0] splitter3_merger2_araddr ;
wire [7:0] splitter3_merger2_arlen ;
wire [EXTRAS-1:0] splitter3_merger2_arextras ;
wire [1:0] splitter3_merger2_arburst ;
wire splitter3_merger2_arvalid ;
wire splitter3_merger2_arready ;
wire [IDWID-1:0] splitter3_merger2_rid ;
wire [DWID-1:0] splitter3_merger2_rdata ;
wire [1:0] splitter3_merger2_rresp ;
wire splitter3_merger2_rlast ;
wire splitter3_merger2_rvalid ;
wire splitter3_merger2_rready ;

wire [IDWID-1:0] splitter3_merger2_awid ;
wire [31:0] splitter3_merger2_awaddr ;
wire [7:0] splitter3_merger2_awlen ;
wire [EXTRAS-1:0] splitter3_merger2_awextras ;
wire [1:0] splitter3_merger2_awburst ;
wire splitter3_merger2_awvalid ;
wire splitter3_merger2_awready ;
wire [DWID-1:0] splitter3_merger2_wdata ;
wire [WSTRB-1:0] splitter3_merger2_wstrb ;
wire splitter3_merger2_wlast ;
wire splitter3_merger2_wvalid ;
wire splitter3_merger2_wready ;
wire [IDWID-1:0] splitter3_merger2_bid ;
wire [1:0] splitter3_merger2_bresp ;
wire splitter3_merger2_bvalid ;
wire splitter3_merger2_bready ;


wire [IDWID-1:0] splitter3_merger3_arid ;
wire [31:0] splitter3_merger3_araddr ;
wire [7:0] splitter3_merger3_arlen ;
wire [EXTRAS-1:0] splitter3_merger3_arextras ;
wire [1:0] splitter3_merger3_arburst ;
wire splitter3_merger3_arvalid ;
wire splitter3_merger3_arready ;
wire [IDWID-1:0] splitter3_merger3_rid ;
wire [DWID-1:0] splitter3_merger3_rdata ;
wire [1:0] splitter3_merger3_rresp ;
wire splitter3_merger3_rlast ;
wire splitter3_merger3_rvalid ;
wire splitter3_merger3_rready ;

wire [IDWID-1:0] splitter3_merger3_awid ;
wire [31:0] splitter3_merger3_awaddr ;
wire [7:0] splitter3_merger3_awlen ;
wire [EXTRAS-1:0] splitter3_merger3_awextras ;
wire [1:0] splitter3_merger3_awburst ;
wire splitter3_merger3_awvalid ;
wire splitter3_merger3_awready ;
wire [DWID-1:0] splitter3_merger3_wdata ;
wire [WSTRB-1:0] splitter3_merger3_wstrb ;
wire splitter3_merger3_wlast ;
wire splitter3_merger3_wvalid ;
wire splitter3_merger3_wready ;
wire [IDWID-1:0] splitter3_merger3_bid ;
wire [1:0] splitter3_merger3_bresp ;
wire splitter3_merger3_bvalid ;
wire splitter3_merger3_bready ;


axi_4_splitter splitter3 (
     .clk(clk) ,.rst_n(rst_n)

    ,.araddr(mst3_araddr[31:0])
    ,.arburst(mst3_arburst[1:0])
    ,.arextras(mst3_arextras[(EXTRAS - 1):0])
    ,.arid(mst3_arid[(IDWID - 1):0])
    ,.arlen(mst3_arlen[7:0])
    ,.arready(mst3_arready)
    ,.arvalid(mst3_arvalid)
    ,.awaddr(mst3_awaddr[31:0])
    ,.awburst(mst3_awburst[1:0])
    ,.awextras(mst3_awextras[(EXTRAS - 1):0])
    ,.awid(mst3_awid[3:0])
    ,.awlen(mst3_awlen[7:0])
    ,.awready(mst3_awready)
    ,.awvalid(mst3_awvalid)
    ,.bid(mst3_bid[(IDWID - 1):0])
    ,.bready(mst3_bready)
    ,.bresp(mst3_bresp[1:0])
    ,.bvalid(mst3_bvalid)
    ,.rdata(mst3_rdata[(DWID - 1):0])
    ,.rid(mst3_rid[(IDWID - 1):0])
    ,.rlast(mst3_rlast)
    ,.rready(mst3_rready)
    ,.rresp(mst3_rresp[1:0])
    ,.rvalid(mst3_rvalid)
    ,.wdata(mst3_wdata[(DWID - 1):0])
    ,.wlast(mst3_wlast)
    ,.wready(mst3_wready)
    ,.wstrb(mst3_wstrb[(WSTRB - 1):0])
    ,.wvalid(mst3_wvalid)

    ,.a_araddr(splitter3_merger0_araddr[31:0])
    ,.a_arburst(splitter3_merger0_arburst[1:0])
    ,.a_arextras(splitter3_merger0_arextras[(EXTRAS - 1):0])
    ,.a_arid(splitter3_merger0_arid[(IDWID - 1):0])
    ,.a_arlen(splitter3_merger0_arlen[7:0])
    ,.a_arready(splitter3_merger0_arready)
    ,.a_arvalid(splitter3_merger0_arvalid)
    ,.a_awaddr(splitter3_merger0_awaddr[31:0])
    ,.a_awburst(splitter3_merger0_awburst[1:0])
    ,.a_awextras(splitter3_merger0_awextras[(EXTRAS - 1):0])
    ,.a_awid(splitter3_merger0_awid[(IDWID - 1):0])
    ,.a_awlen(splitter3_merger0_awlen[7:0])
    ,.a_awready(splitter3_merger0_awready)
    ,.a_awvalid(splitter3_merger0_awvalid)
    ,.a_bid(splitter3_merger0_bid[(IDWID - 1):0])
    ,.a_bready(splitter3_merger0_bready)
    ,.a_bresp(splitter3_merger0_bresp[1:0])
    ,.a_bvalid(splitter3_merger0_bvalid)
    ,.a_rdata(splitter3_merger0_rdata[(DWID - 1):0])
    ,.a_rid(splitter3_merger0_rid[(IDWID - 1):0])
    ,.a_rlast(splitter3_merger0_rlast)
    ,.a_rready(splitter3_merger0_rready)
    ,.a_rresp(splitter3_merger0_rresp[1:0])
    ,.a_rvalid(splitter3_merger0_rvalid)
    ,.a_wdata(splitter3_merger0_wdata[(DWID - 1):0])
    ,.a_wlast(splitter3_merger0_wlast)
    ,.a_wready(splitter3_merger0_wready)
    ,.a_wstrb(splitter3_merger0_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(splitter3_merger0_wvalid)
    ,.b_araddr(splitter3_merger1_araddr[31:0])
    ,.b_arburst(splitter3_merger1_arburst[1:0])
    ,.b_arextras(splitter3_merger1_arextras[(EXTRAS - 1):0])
    ,.b_arid(splitter3_merger1_arid[(IDWID - 1):0])
    ,.b_arlen(splitter3_merger1_arlen[7:0])
    ,.b_arready(splitter3_merger1_arready)
    ,.b_arvalid(splitter3_merger1_arvalid)
    ,.b_awaddr(splitter3_merger1_awaddr[31:0])
    ,.b_awburst(splitter3_merger1_awburst[1:0])
    ,.b_awextras(splitter3_merger1_awextras[(EXTRAS - 1):0])
    ,.b_awid(splitter3_merger1_awid[(IDWID - 1):0])
    ,.b_awlen(splitter3_merger1_awlen[7:0])
    ,.b_awready(splitter3_merger1_awready)
    ,.b_awvalid(splitter3_merger1_awvalid)
    ,.b_bid(splitter3_merger1_bid[(IDWID - 1):0])
    ,.b_bready(splitter3_merger1_bready)
    ,.b_bresp(splitter3_merger1_bresp[1:0])
    ,.b_bvalid(splitter3_merger1_bvalid)
    ,.b_rdata(splitter3_merger1_rdata[(DWID - 1):0])
    ,.b_rid(splitter3_merger1_rid[(IDWID - 1):0])
    ,.b_rlast(splitter3_merger1_rlast)
    ,.b_rready(splitter3_merger1_rready)
    ,.b_rresp(splitter3_merger1_rresp[1:0])
    ,.b_rvalid(splitter3_merger1_rvalid)
    ,.b_wdata(splitter3_merger1_wdata[(DWID - 1):0])
    ,.b_wlast(splitter3_merger1_wlast)
    ,.b_wready(splitter3_merger1_wready)
    ,.b_wstrb(splitter3_merger1_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(splitter3_merger1_wvalid)
    ,.c_araddr(splitter3_merger2_araddr[31:0])
    ,.c_arburst(splitter3_merger2_arburst[1:0])
    ,.c_arextras(splitter3_merger2_arextras[(EXTRAS - 1):0])
    ,.c_arid(splitter3_merger2_arid[(IDWID - 1):0])
    ,.c_arlen(splitter3_merger2_arlen[7:0])
    ,.c_arready(splitter3_merger2_arready)
    ,.c_arvalid(splitter3_merger2_arvalid)
    ,.c_awaddr(splitter3_merger2_awaddr[31:0])
    ,.c_awburst(splitter3_merger2_awburst[1:0])
    ,.c_awextras(splitter3_merger2_awextras[(EXTRAS - 1):0])
    ,.c_awid(splitter3_merger2_awid[(IDWID - 1):0])
    ,.c_awlen(splitter3_merger2_awlen[7:0])
    ,.c_awready(splitter3_merger2_awready)
    ,.c_awvalid(splitter3_merger2_awvalid)
    ,.c_bid(splitter3_merger2_bid[(IDWID - 1):0])
    ,.c_bready(splitter3_merger2_bready)
    ,.c_bresp(splitter3_merger2_bresp[1:0])
    ,.c_bvalid(splitter3_merger2_bvalid)
    ,.c_rdata(splitter3_merger2_rdata[(DWID - 1):0])
    ,.c_rid(splitter3_merger2_rid[(IDWID - 1):0])
    ,.c_rlast(splitter3_merger2_rlast)
    ,.c_rready(splitter3_merger2_rready)
    ,.c_rresp(splitter3_merger2_rresp[1:0])
    ,.c_rvalid(splitter3_merger2_rvalid)
    ,.c_wdata(splitter3_merger2_wdata[(DWID - 1):0])
    ,.c_wlast(splitter3_merger2_wlast)
    ,.c_wready(splitter3_merger2_wready)
    ,.c_wstrb(splitter3_merger2_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(splitter3_merger2_wvalid)
    ,.d_araddr(splitter3_merger3_araddr[31:0])
    ,.d_arburst(splitter3_merger3_arburst[1:0])
    ,.d_arextras(splitter3_merger3_arextras[(EXTRAS - 1):0])
    ,.d_arid(splitter3_merger3_arid[(IDWID - 1):0])
    ,.d_arlen(splitter3_merger3_arlen[7:0])
    ,.d_arready(splitter3_merger3_arready)
    ,.d_arvalid(splitter3_merger3_arvalid)
    ,.d_awaddr(splitter3_merger3_awaddr[31:0])
    ,.d_awburst(splitter3_merger3_awburst[1:0])
    ,.d_awextras(splitter3_merger3_awextras[(EXTRAS - 1):0])
    ,.d_awid(splitter3_merger3_awid[(IDWID - 1):0])
    ,.d_awlen(splitter3_merger3_awlen[7:0])
    ,.d_awready(splitter3_merger3_awready)
    ,.d_awvalid(splitter3_merger3_awvalid)
    ,.d_bid(splitter3_merger3_bid[(IDWID - 1):0])
    ,.d_bready(splitter3_merger3_bready)
    ,.d_bresp(splitter3_merger3_bresp[1:0])
    ,.d_bvalid(splitter3_merger3_bvalid)
    ,.d_rdata(splitter3_merger3_rdata[(DWID - 1):0])
    ,.d_rid(splitter3_merger3_rid[(IDWID - 1):0])
    ,.d_rlast(splitter3_merger3_rlast)
    ,.d_rready(splitter3_merger3_rready)
    ,.d_rresp(splitter3_merger3_rresp[1:0])
    ,.d_rvalid(splitter3_merger3_rvalid)
    ,.d_wdata(splitter3_merger3_wdata[(DWID - 1):0])
    ,.d_wlast(splitter3_merger3_wlast)
    ,.d_wready(splitter3_merger3_wready)
    ,.d_wstrb(splitter3_merger3_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(splitter3_merger3_wvalid)

);

axi_4_merger merger0 (
     .clk(clk),.rst_n(rst_n)
    ,.araddr(slv0_araddr[31:0])
    ,.arburst(slv0_arburst[1:0])
    ,.arextras(slv0_arextras[(EXTRAS - 1):0])
    ,.arid(slv0_arid[(IDWID - 1):0])
    ,.arlen(slv0_arlen[7:0])
    ,.arready(slv0_arready)
    ,.arvalid(slv0_arvalid)
    ,.awaddr(slv0_awaddr[31:0])
    ,.awburst(slv0_awburst[1:0])
    ,.awextras(slv0_awextras[(EXTRAS - 1):0])
    ,.awid(slv0_awid[3:0])
    ,.awlen(slv0_awlen[7:0])
    ,.awready(slv0_awready)
    ,.awvalid(slv0_awvalid)
    ,.bid(slv0_bid[(IDWID - 1):0])
    ,.bready(slv0_bready)
    ,.bresp(slv0_bresp[1:0])
    ,.bvalid(slv0_bvalid)
    ,.rid(slv0_rid[(IDWID - 1):0])
    ,.rlast(slv0_rlast)
    ,.rready(slv0_rready)
    ,.rresp(slv0_rresp[1:0])
    ,.rvalid(slv0_rvalid)
    ,.rdata(slv0_rdata[(DWID - 1):0])
    ,.wdata(slv0_wdata[(DWID - 1):0])
    ,.wlast(slv0_wlast)
    ,.wready(slv0_wready)
    ,.wstrb(slv0_wstrb[(WSTRB - 1):0])
    ,.wvalid(slv0_wvalid)


    ,.a_araddr(splitter0_merger0_araddr[31:0])
    ,.a_arburst(splitter0_merger0_arburst[1:0])
    ,.a_arextras(splitter0_merger0_arextras[(EXTRAS - 1):0])
    ,.a_arid(splitter0_merger0_arid[(IDWID - 1):0])
    ,.a_arlen(splitter0_merger0_arlen[7:0])
    ,.a_arready(splitter0_merger0_arready)
    ,.a_arvalid(splitter0_merger0_arvalid)
    ,.a_awaddr(splitter0_merger0_awaddr[31:0])
    ,.a_awburst(splitter0_merger0_awburst[1:0])
    ,.a_awextras(splitter0_merger0_awextras[(EXTRAS - 1):0])
    ,.a_awid(splitter0_merger0_awid[(IDWID - 1):0])
    ,.a_awlen(splitter0_merger0_awlen[7:0])
    ,.a_awready(splitter0_merger0_awready)
    ,.a_awvalid(splitter0_merger0_awvalid)
    ,.a_bid(splitter0_merger0_bid[(IDWID - 1):0])
    ,.a_bready(splitter0_merger0_bready)
    ,.a_bresp(splitter0_merger0_bresp[1:0])
    ,.a_bvalid(splitter0_merger0_bvalid)
    ,.a_rdata(splitter0_merger0_rdata[(DWID - 1):0])
    ,.a_rid(splitter0_merger0_rid[(IDWID - 1):0])
    ,.a_rlast(splitter0_merger0_rlast)
    ,.a_rready(splitter0_merger0_rready)
    ,.a_rresp(splitter0_merger0_rresp[1:0])
    ,.a_rvalid(splitter0_merger0_rvalid)
    ,.a_wdata(splitter0_merger0_wdata[(DWID - 1):0])
    ,.a_wlast(splitter0_merger0_wlast)
    ,.a_wready(splitter0_merger0_wready)
    ,.a_wstrb(splitter0_merger0_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(splitter0_merger0_wvalid)

    ,.b_araddr(splitter1_merger0_araddr[31:0])
    ,.b_arburst(splitter1_merger0_arburst[1:0])
    ,.b_arextras(splitter1_merger0_arextras[(EXTRAS - 1):0])
    ,.b_arid(splitter1_merger0_arid[(IDWID - 1):0])
    ,.b_arlen(splitter1_merger0_arlen[7:0])
    ,.b_arready(splitter1_merger0_arready)
    ,.b_arvalid(splitter1_merger0_arvalid)
    ,.b_awaddr(splitter1_merger0_awaddr[31:0])
    ,.b_awburst(splitter1_merger0_awburst[1:0])
    ,.b_awextras(splitter1_merger0_awextras[(EXTRAS - 1):0])
    ,.b_awid(splitter1_merger0_awid[(IDWID - 1):0])
    ,.b_awlen(splitter1_merger0_awlen[7:0])
    ,.b_awready(splitter1_merger0_awready)
    ,.b_awvalid(splitter1_merger0_awvalid)
    ,.b_bid(splitter1_merger0_bid[(IDWID - 1):0])
    ,.b_bready(splitter1_merger0_bready)
    ,.b_bresp(splitter1_merger0_bresp[1:0])
    ,.b_bvalid(splitter1_merger0_bvalid)
    ,.b_rdata(splitter1_merger0_rdata[(DWID - 1):0])
    ,.b_rid(splitter1_merger0_rid[(IDWID - 1):0])
    ,.b_rlast(splitter1_merger0_rlast)
    ,.b_rready(splitter1_merger0_rready)
    ,.b_rresp(splitter1_merger0_rresp[1:0])
    ,.b_rvalid(splitter1_merger0_rvalid)
    ,.b_wdata(splitter1_merger0_wdata[(DWID - 1):0])
    ,.b_wlast(splitter1_merger0_wlast)
    ,.b_wready(splitter1_merger0_wready)
    ,.b_wstrb(splitter1_merger0_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(splitter1_merger0_wvalid)

    ,.c_araddr(splitter2_merger0_araddr[31:0])
    ,.c_arburst(splitter2_merger0_arburst[1:0])
    ,.c_arextras(splitter2_merger0_arextras[(EXTRAS - 1):0])
    ,.c_arid(splitter2_merger0_arid[(IDWID - 1):0])
    ,.c_arlen(splitter2_merger0_arlen[7:0])
    ,.c_arready(splitter2_merger0_arready)
    ,.c_arvalid(splitter2_merger0_arvalid)
    ,.c_awaddr(splitter2_merger0_awaddr[31:0])
    ,.c_awburst(splitter2_merger0_awburst[1:0])
    ,.c_awextras(splitter2_merger0_awextras[(EXTRAS - 1):0])
    ,.c_awid(splitter2_merger0_awid[(IDWID - 1):0])
    ,.c_awlen(splitter2_merger0_awlen[7:0])
    ,.c_awready(splitter2_merger0_awready)
    ,.c_awvalid(splitter2_merger0_awvalid)
    ,.c_bid(splitter2_merger0_bid[(IDWID - 1):0])
    ,.c_bready(splitter2_merger0_bready)
    ,.c_bresp(splitter2_merger0_bresp[1:0])
    ,.c_bvalid(splitter2_merger0_bvalid)
    ,.c_rdata(splitter2_merger0_rdata[(DWID - 1):0])
    ,.c_rid(splitter2_merger0_rid[(IDWID - 1):0])
    ,.c_rlast(splitter2_merger0_rlast)
    ,.c_rready(splitter2_merger0_rready)
    ,.c_rresp(splitter2_merger0_rresp[1:0])
    ,.c_rvalid(splitter2_merger0_rvalid)
    ,.c_wdata(splitter2_merger0_wdata[(DWID - 1):0])
    ,.c_wlast(splitter2_merger0_wlast)
    ,.c_wready(splitter2_merger0_wready)
    ,.c_wstrb(splitter2_merger0_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(splitter2_merger0_wvalid)

    ,.d_araddr(splitter3_merger0_araddr[31:0])
    ,.d_arburst(splitter3_merger0_arburst[1:0])
    ,.d_arextras(splitter3_merger0_arextras[(EXTRAS - 1):0])
    ,.d_arid(splitter3_merger0_arid[(IDWID - 1):0])
    ,.d_arlen(splitter3_merger0_arlen[7:0])
    ,.d_arready(splitter3_merger0_arready)
    ,.d_arvalid(splitter3_merger0_arvalid)
    ,.d_awaddr(splitter3_merger0_awaddr[31:0])
    ,.d_awburst(splitter3_merger0_awburst[1:0])
    ,.d_awextras(splitter3_merger0_awextras[(EXTRAS - 1):0])
    ,.d_awid(splitter3_merger0_awid[(IDWID - 1):0])
    ,.d_awlen(splitter3_merger0_awlen[7:0])
    ,.d_awready(splitter3_merger0_awready)
    ,.d_awvalid(splitter3_merger0_awvalid)
    ,.d_bid(splitter3_merger0_bid[(IDWID - 1):0])
    ,.d_bready(splitter3_merger0_bready)
    ,.d_bresp(splitter3_merger0_bresp[1:0])
    ,.d_bvalid(splitter3_merger0_bvalid)
    ,.d_rdata(splitter3_merger0_rdata[(DWID - 1):0])
    ,.d_rid(splitter3_merger0_rid[(IDWID - 1):0])
    ,.d_rlast(splitter3_merger0_rlast)
    ,.d_rready(splitter3_merger0_rready)
    ,.d_rresp(splitter3_merger0_rresp[1:0])
    ,.d_rvalid(splitter3_merger0_rvalid)
    ,.d_wdata(splitter3_merger0_wdata[(DWID - 1):0])
    ,.d_wlast(splitter3_merger0_wlast)
    ,.d_wready(splitter3_merger0_wready)
    ,.d_wstrb(splitter3_merger0_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(splitter3_merger0_wvalid)
);


axi_4_merger merger1 (
     .clk(clk),.rst_n(rst_n)
    ,.araddr(slv1_araddr[31:0])
    ,.arburst(slv1_arburst[1:0])
    ,.arextras(slv1_arextras[(EXTRAS - 1):0])
    ,.arid(slv1_arid[(IDWID - 1):0])
    ,.arlen(slv1_arlen[7:0])
    ,.arready(slv1_arready)
    ,.arvalid(slv1_arvalid)
    ,.awaddr(slv1_awaddr[31:0])
    ,.awburst(slv1_awburst[1:0])
    ,.awextras(slv1_awextras[(EXTRAS - 1):0])
    ,.awid(slv1_awid[3:0])
    ,.awlen(slv1_awlen[7:0])
    ,.awready(slv1_awready)
    ,.awvalid(slv1_awvalid)
    ,.bid(slv1_bid[(IDWID - 1):0])
    ,.bready(slv1_bready)
    ,.bresp(slv1_bresp[1:0])
    ,.bvalid(slv1_bvalid)
    ,.rid(slv1_rid[(IDWID - 1):0])
    ,.rlast(slv1_rlast)
    ,.rready(slv1_rready)
    ,.rresp(slv1_rresp[1:0])
    ,.rvalid(slv1_rvalid)
    ,.rdata(slv1_rdata[(DWID - 1):0])
    ,.wdata(slv1_wdata[(DWID - 1):0])
    ,.wlast(slv1_wlast)
    ,.wready(slv1_wready)
    ,.wstrb(slv1_wstrb[(WSTRB - 1):0])
    ,.wvalid(slv1_wvalid)


    ,.a_araddr(splitter0_merger1_araddr[31:0])
    ,.a_arburst(splitter0_merger1_arburst[1:0])
    ,.a_arextras(splitter0_merger1_arextras[(EXTRAS - 1):0])
    ,.a_arid(splitter0_merger1_arid[(IDWID - 1):0])
    ,.a_arlen(splitter0_merger1_arlen[7:0])
    ,.a_arready(splitter0_merger1_arready)
    ,.a_arvalid(splitter0_merger1_arvalid)
    ,.a_awaddr(splitter0_merger1_awaddr[31:0])
    ,.a_awburst(splitter0_merger1_awburst[1:0])
    ,.a_awextras(splitter0_merger1_awextras[(EXTRAS - 1):0])
    ,.a_awid(splitter0_merger1_awid[(IDWID - 1):0])
    ,.a_awlen(splitter0_merger1_awlen[7:0])
    ,.a_awready(splitter0_merger1_awready)
    ,.a_awvalid(splitter0_merger1_awvalid)
    ,.a_bid(splitter0_merger1_bid[(IDWID - 1):0])
    ,.a_bready(splitter0_merger1_bready)
    ,.a_bresp(splitter0_merger1_bresp[1:0])
    ,.a_bvalid(splitter0_merger1_bvalid)
    ,.a_rdata(splitter0_merger1_rdata[(DWID - 1):0])
    ,.a_rid(splitter0_merger1_rid[(IDWID - 1):0])
    ,.a_rlast(splitter0_merger1_rlast)
    ,.a_rready(splitter0_merger1_rready)
    ,.a_rresp(splitter0_merger1_rresp[1:0])
    ,.a_rvalid(splitter0_merger1_rvalid)
    ,.a_wdata(splitter0_merger1_wdata[(DWID - 1):0])
    ,.a_wlast(splitter0_merger1_wlast)
    ,.a_wready(splitter0_merger1_wready)
    ,.a_wstrb(splitter0_merger1_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(splitter0_merger1_wvalid)

    ,.b_araddr(splitter1_merger1_araddr[31:0])
    ,.b_arburst(splitter1_merger1_arburst[1:0])
    ,.b_arextras(splitter1_merger1_arextras[(EXTRAS - 1):0])
    ,.b_arid(splitter1_merger1_arid[(IDWID - 1):0])
    ,.b_arlen(splitter1_merger1_arlen[7:0])
    ,.b_arready(splitter1_merger1_arready)
    ,.b_arvalid(splitter1_merger1_arvalid)
    ,.b_awaddr(splitter1_merger1_awaddr[31:0])
    ,.b_awburst(splitter1_merger1_awburst[1:0])
    ,.b_awextras(splitter1_merger1_awextras[(EXTRAS - 1):0])
    ,.b_awid(splitter1_merger1_awid[(IDWID - 1):0])
    ,.b_awlen(splitter1_merger1_awlen[7:0])
    ,.b_awready(splitter1_merger1_awready)
    ,.b_awvalid(splitter1_merger1_awvalid)
    ,.b_bid(splitter1_merger1_bid[(IDWID - 1):0])
    ,.b_bready(splitter1_merger1_bready)
    ,.b_bresp(splitter1_merger1_bresp[1:0])
    ,.b_bvalid(splitter1_merger1_bvalid)
    ,.b_rdata(splitter1_merger1_rdata[(DWID - 1):0])
    ,.b_rid(splitter1_merger1_rid[(IDWID - 1):0])
    ,.b_rlast(splitter1_merger1_rlast)
    ,.b_rready(splitter1_merger1_rready)
    ,.b_rresp(splitter1_merger1_rresp[1:0])
    ,.b_rvalid(splitter1_merger1_rvalid)
    ,.b_wdata(splitter1_merger1_wdata[(DWID - 1):0])
    ,.b_wlast(splitter1_merger1_wlast)
    ,.b_wready(splitter1_merger1_wready)
    ,.b_wstrb(splitter1_merger1_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(splitter1_merger1_wvalid)

    ,.c_araddr(splitter2_merger1_araddr[31:0])
    ,.c_arburst(splitter2_merger1_arburst[1:0])
    ,.c_arextras(splitter2_merger1_arextras[(EXTRAS - 1):0])
    ,.c_arid(splitter2_merger1_arid[(IDWID - 1):0])
    ,.c_arlen(splitter2_merger1_arlen[7:0])
    ,.c_arready(splitter2_merger1_arready)
    ,.c_arvalid(splitter2_merger1_arvalid)
    ,.c_awaddr(splitter2_merger1_awaddr[31:0])
    ,.c_awburst(splitter2_merger1_awburst[1:0])
    ,.c_awextras(splitter2_merger1_awextras[(EXTRAS - 1):0])
    ,.c_awid(splitter2_merger1_awid[(IDWID - 1):0])
    ,.c_awlen(splitter2_merger1_awlen[7:0])
    ,.c_awready(splitter2_merger1_awready)
    ,.c_awvalid(splitter2_merger1_awvalid)
    ,.c_bid(splitter2_merger1_bid[(IDWID - 1):0])
    ,.c_bready(splitter2_merger1_bready)
    ,.c_bresp(splitter2_merger1_bresp[1:0])
    ,.c_bvalid(splitter2_merger1_bvalid)
    ,.c_rdata(splitter2_merger1_rdata[(DWID - 1):0])
    ,.c_rid(splitter2_merger1_rid[(IDWID - 1):0])
    ,.c_rlast(splitter2_merger1_rlast)
    ,.c_rready(splitter2_merger1_rready)
    ,.c_rresp(splitter2_merger1_rresp[1:0])
    ,.c_rvalid(splitter2_merger1_rvalid)
    ,.c_wdata(splitter2_merger1_wdata[(DWID - 1):0])
    ,.c_wlast(splitter2_merger1_wlast)
    ,.c_wready(splitter2_merger1_wready)
    ,.c_wstrb(splitter2_merger1_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(splitter2_merger1_wvalid)

    ,.d_araddr(splitter3_merger1_araddr[31:0])
    ,.d_arburst(splitter3_merger1_arburst[1:0])
    ,.d_arextras(splitter3_merger1_arextras[(EXTRAS - 1):0])
    ,.d_arid(splitter3_merger1_arid[(IDWID - 1):0])
    ,.d_arlen(splitter3_merger1_arlen[7:0])
    ,.d_arready(splitter3_merger1_arready)
    ,.d_arvalid(splitter3_merger1_arvalid)
    ,.d_awaddr(splitter3_merger1_awaddr[31:0])
    ,.d_awburst(splitter3_merger1_awburst[1:0])
    ,.d_awextras(splitter3_merger1_awextras[(EXTRAS - 1):0])
    ,.d_awid(splitter3_merger1_awid[(IDWID - 1):0])
    ,.d_awlen(splitter3_merger1_awlen[7:0])
    ,.d_awready(splitter3_merger1_awready)
    ,.d_awvalid(splitter3_merger1_awvalid)
    ,.d_bid(splitter3_merger1_bid[(IDWID - 1):0])
    ,.d_bready(splitter3_merger1_bready)
    ,.d_bresp(splitter3_merger1_bresp[1:0])
    ,.d_bvalid(splitter3_merger1_bvalid)
    ,.d_rdata(splitter3_merger1_rdata[(DWID - 1):0])
    ,.d_rid(splitter3_merger1_rid[(IDWID - 1):0])
    ,.d_rlast(splitter3_merger1_rlast)
    ,.d_rready(splitter3_merger1_rready)
    ,.d_rresp(splitter3_merger1_rresp[1:0])
    ,.d_rvalid(splitter3_merger1_rvalid)
    ,.d_wdata(splitter3_merger1_wdata[(DWID - 1):0])
    ,.d_wlast(splitter3_merger1_wlast)
    ,.d_wready(splitter3_merger1_wready)
    ,.d_wstrb(splitter3_merger1_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(splitter3_merger1_wvalid)
);


axi_4_merger merger2 (
     .clk(clk),.rst_n(rst_n)
    ,.araddr(slv2_araddr[31:0])
    ,.arburst(slv2_arburst[1:0])
    ,.arextras(slv2_arextras[(EXTRAS - 1):0])
    ,.arid(slv2_arid[(IDWID - 1):0])
    ,.arlen(slv2_arlen[7:0])
    ,.arready(slv2_arready)
    ,.arvalid(slv2_arvalid)
    ,.awaddr(slv2_awaddr[31:0])
    ,.awburst(slv2_awburst[1:0])
    ,.awextras(slv2_awextras[(EXTRAS - 1):0])
    ,.awid(slv2_awid[3:0])
    ,.awlen(slv2_awlen[7:0])
    ,.awready(slv2_awready)
    ,.awvalid(slv2_awvalid)
    ,.bid(slv2_bid[(IDWID - 1):0])
    ,.bready(slv2_bready)
    ,.bresp(slv2_bresp[1:0])
    ,.bvalid(slv2_bvalid)
    ,.rid(slv2_rid[(IDWID - 1):0])
    ,.rlast(slv2_rlast)
    ,.rready(slv2_rready)
    ,.rresp(slv2_rresp[1:0])
    ,.rvalid(slv2_rvalid)
    ,.rdata(slv2_rdata[(DWID - 1):0])
    ,.wdata(slv2_wdata[(DWID - 1):0])
    ,.wlast(slv2_wlast)
    ,.wready(slv2_wready)
    ,.wstrb(slv2_wstrb[(WSTRB - 1):0])
    ,.wvalid(slv2_wvalid)


    ,.a_araddr(splitter0_merger2_araddr[31:0])
    ,.a_arburst(splitter0_merger2_arburst[1:0])
    ,.a_arextras(splitter0_merger2_arextras[(EXTRAS - 1):0])
    ,.a_arid(splitter0_merger2_arid[(IDWID - 1):0])
    ,.a_arlen(splitter0_merger2_arlen[7:0])
    ,.a_arready(splitter0_merger2_arready)
    ,.a_arvalid(splitter0_merger2_arvalid)
    ,.a_awaddr(splitter0_merger2_awaddr[31:0])
    ,.a_awburst(splitter0_merger2_awburst[1:0])
    ,.a_awextras(splitter0_merger2_awextras[(EXTRAS - 1):0])
    ,.a_awid(splitter0_merger2_awid[(IDWID - 1):0])
    ,.a_awlen(splitter0_merger2_awlen[7:0])
    ,.a_awready(splitter0_merger2_awready)
    ,.a_awvalid(splitter0_merger2_awvalid)
    ,.a_bid(splitter0_merger2_bid[(IDWID - 1):0])
    ,.a_bready(splitter0_merger2_bready)
    ,.a_bresp(splitter0_merger2_bresp[1:0])
    ,.a_bvalid(splitter0_merger2_bvalid)
    ,.a_rdata(splitter0_merger2_rdata[(DWID - 1):0])
    ,.a_rid(splitter0_merger2_rid[(IDWID - 1):0])
    ,.a_rlast(splitter0_merger2_rlast)
    ,.a_rready(splitter0_merger2_rready)
    ,.a_rresp(splitter0_merger2_rresp[1:0])
    ,.a_rvalid(splitter0_merger2_rvalid)
    ,.a_wdata(splitter0_merger2_wdata[(DWID - 1):0])
    ,.a_wlast(splitter0_merger2_wlast)
    ,.a_wready(splitter0_merger2_wready)
    ,.a_wstrb(splitter0_merger2_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(splitter0_merger2_wvalid)

    ,.b_araddr(splitter1_merger2_araddr[31:0])
    ,.b_arburst(splitter1_merger2_arburst[1:0])
    ,.b_arextras(splitter1_merger2_arextras[(EXTRAS - 1):0])
    ,.b_arid(splitter1_merger2_arid[(IDWID - 1):0])
    ,.b_arlen(splitter1_merger2_arlen[7:0])
    ,.b_arready(splitter1_merger2_arready)
    ,.b_arvalid(splitter1_merger2_arvalid)
    ,.b_awaddr(splitter1_merger2_awaddr[31:0])
    ,.b_awburst(splitter1_merger2_awburst[1:0])
    ,.b_awextras(splitter1_merger2_awextras[(EXTRAS - 1):0])
    ,.b_awid(splitter1_merger2_awid[(IDWID - 1):0])
    ,.b_awlen(splitter1_merger2_awlen[7:0])
    ,.b_awready(splitter1_merger2_awready)
    ,.b_awvalid(splitter1_merger2_awvalid)
    ,.b_bid(splitter1_merger2_bid[(IDWID - 1):0])
    ,.b_bready(splitter1_merger2_bready)
    ,.b_bresp(splitter1_merger2_bresp[1:0])
    ,.b_bvalid(splitter1_merger2_bvalid)
    ,.b_rdata(splitter1_merger2_rdata[(DWID - 1):0])
    ,.b_rid(splitter1_merger2_rid[(IDWID - 1):0])
    ,.b_rlast(splitter1_merger2_rlast)
    ,.b_rready(splitter1_merger2_rready)
    ,.b_rresp(splitter1_merger2_rresp[1:0])
    ,.b_rvalid(splitter1_merger2_rvalid)
    ,.b_wdata(splitter1_merger2_wdata[(DWID - 1):0])
    ,.b_wlast(splitter1_merger2_wlast)
    ,.b_wready(splitter1_merger2_wready)
    ,.b_wstrb(splitter1_merger2_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(splitter1_merger2_wvalid)

    ,.c_araddr(splitter2_merger2_araddr[31:0])
    ,.c_arburst(splitter2_merger2_arburst[1:0])
    ,.c_arextras(splitter2_merger2_arextras[(EXTRAS - 1):0])
    ,.c_arid(splitter2_merger2_arid[(IDWID - 1):0])
    ,.c_arlen(splitter2_merger2_arlen[7:0])
    ,.c_arready(splitter2_merger2_arready)
    ,.c_arvalid(splitter2_merger2_arvalid)
    ,.c_awaddr(splitter2_merger2_awaddr[31:0])
    ,.c_awburst(splitter2_merger2_awburst[1:0])
    ,.c_awextras(splitter2_merger2_awextras[(EXTRAS - 1):0])
    ,.c_awid(splitter2_merger2_awid[(IDWID - 1):0])
    ,.c_awlen(splitter2_merger2_awlen[7:0])
    ,.c_awready(splitter2_merger2_awready)
    ,.c_awvalid(splitter2_merger2_awvalid)
    ,.c_bid(splitter2_merger2_bid[(IDWID - 1):0])
    ,.c_bready(splitter2_merger2_bready)
    ,.c_bresp(splitter2_merger2_bresp[1:0])
    ,.c_bvalid(splitter2_merger2_bvalid)
    ,.c_rdata(splitter2_merger2_rdata[(DWID - 1):0])
    ,.c_rid(splitter2_merger2_rid[(IDWID - 1):0])
    ,.c_rlast(splitter2_merger2_rlast)
    ,.c_rready(splitter2_merger2_rready)
    ,.c_rresp(splitter2_merger2_rresp[1:0])
    ,.c_rvalid(splitter2_merger2_rvalid)
    ,.c_wdata(splitter2_merger2_wdata[(DWID - 1):0])
    ,.c_wlast(splitter2_merger2_wlast)
    ,.c_wready(splitter2_merger2_wready)
    ,.c_wstrb(splitter2_merger2_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(splitter2_merger2_wvalid)

    ,.d_araddr(splitter3_merger2_araddr[31:0])
    ,.d_arburst(splitter3_merger2_arburst[1:0])
    ,.d_arextras(splitter3_merger2_arextras[(EXTRAS - 1):0])
    ,.d_arid(splitter3_merger2_arid[(IDWID - 1):0])
    ,.d_arlen(splitter3_merger2_arlen[7:0])
    ,.d_arready(splitter3_merger2_arready)
    ,.d_arvalid(splitter3_merger2_arvalid)
    ,.d_awaddr(splitter3_merger2_awaddr[31:0])
    ,.d_awburst(splitter3_merger2_awburst[1:0])
    ,.d_awextras(splitter3_merger2_awextras[(EXTRAS - 1):0])
    ,.d_awid(splitter3_merger2_awid[(IDWID - 1):0])
    ,.d_awlen(splitter3_merger2_awlen[7:0])
    ,.d_awready(splitter3_merger2_awready)
    ,.d_awvalid(splitter3_merger2_awvalid)
    ,.d_bid(splitter3_merger2_bid[(IDWID - 1):0])
    ,.d_bready(splitter3_merger2_bready)
    ,.d_bresp(splitter3_merger2_bresp[1:0])
    ,.d_bvalid(splitter3_merger2_bvalid)
    ,.d_rdata(splitter3_merger2_rdata[(DWID - 1):0])
    ,.d_rid(splitter3_merger2_rid[(IDWID - 1):0])
    ,.d_rlast(splitter3_merger2_rlast)
    ,.d_rready(splitter3_merger2_rready)
    ,.d_rresp(splitter3_merger2_rresp[1:0])
    ,.d_rvalid(splitter3_merger2_rvalid)
    ,.d_wdata(splitter3_merger2_wdata[(DWID - 1):0])
    ,.d_wlast(splitter3_merger2_wlast)
    ,.d_wready(splitter3_merger2_wready)
    ,.d_wstrb(splitter3_merger2_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(splitter3_merger2_wvalid)
);


axi_4_merger merger3 (
     .clk(clk),.rst_n(rst_n)
    ,.araddr(slv3_araddr[31:0])
    ,.arburst(slv3_arburst[1:0])
    ,.arextras(slv3_arextras[(EXTRAS - 1):0])
    ,.arid(slv3_arid[(IDWID - 1):0])
    ,.arlen(slv3_arlen[7:0])
    ,.arready(slv3_arready)
    ,.arvalid(slv3_arvalid)
    ,.awaddr(slv3_awaddr[31:0])
    ,.awburst(slv3_awburst[1:0])
    ,.awextras(slv3_awextras[(EXTRAS - 1):0])
    ,.awid(slv3_awid[3:0])
    ,.awlen(slv3_awlen[7:0])
    ,.awready(slv3_awready)
    ,.awvalid(slv3_awvalid)
    ,.bid(slv3_bid[(IDWID - 1):0])
    ,.bready(slv3_bready)
    ,.bresp(slv3_bresp[1:0])
    ,.bvalid(slv3_bvalid)
    ,.rid(slv3_rid[(IDWID - 1):0])
    ,.rlast(slv3_rlast)
    ,.rready(slv3_rready)
    ,.rresp(slv3_rresp[1:0])
    ,.rvalid(slv3_rvalid)
    ,.rdata(slv3_rdata[(DWID - 1):0])
    ,.wdata(slv3_wdata[(DWID - 1):0])
    ,.wlast(slv3_wlast)
    ,.wready(slv3_wready)
    ,.wstrb(slv3_wstrb[(WSTRB - 1):0])
    ,.wvalid(slv3_wvalid)


    ,.a_araddr(splitter0_merger3_araddr[31:0])
    ,.a_arburst(splitter0_merger3_arburst[1:0])
    ,.a_arextras(splitter0_merger3_arextras[(EXTRAS - 1):0])
    ,.a_arid(splitter0_merger3_arid[(IDWID - 1):0])
    ,.a_arlen(splitter0_merger3_arlen[7:0])
    ,.a_arready(splitter0_merger3_arready)
    ,.a_arvalid(splitter0_merger3_arvalid)
    ,.a_awaddr(splitter0_merger3_awaddr[31:0])
    ,.a_awburst(splitter0_merger3_awburst[1:0])
    ,.a_awextras(splitter0_merger3_awextras[(EXTRAS - 1):0])
    ,.a_awid(splitter0_merger3_awid[(IDWID - 1):0])
    ,.a_awlen(splitter0_merger3_awlen[7:0])
    ,.a_awready(splitter0_merger3_awready)
    ,.a_awvalid(splitter0_merger3_awvalid)
    ,.a_bid(splitter0_merger3_bid[(IDWID - 1):0])
    ,.a_bready(splitter0_merger3_bready)
    ,.a_bresp(splitter0_merger3_bresp[1:0])
    ,.a_bvalid(splitter0_merger3_bvalid)
    ,.a_rdata(splitter0_merger3_rdata[(DWID - 1):0])
    ,.a_rid(splitter0_merger3_rid[(IDWID - 1):0])
    ,.a_rlast(splitter0_merger3_rlast)
    ,.a_rready(splitter0_merger3_rready)
    ,.a_rresp(splitter0_merger3_rresp[1:0])
    ,.a_rvalid(splitter0_merger3_rvalid)
    ,.a_wdata(splitter0_merger3_wdata[(DWID - 1):0])
    ,.a_wlast(splitter0_merger3_wlast)
    ,.a_wready(splitter0_merger3_wready)
    ,.a_wstrb(splitter0_merger3_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(splitter0_merger3_wvalid)

    ,.b_araddr(splitter1_merger3_araddr[31:0])
    ,.b_arburst(splitter1_merger3_arburst[1:0])
    ,.b_arextras(splitter1_merger3_arextras[(EXTRAS - 1):0])
    ,.b_arid(splitter1_merger3_arid[(IDWID - 1):0])
    ,.b_arlen(splitter1_merger3_arlen[7:0])
    ,.b_arready(splitter1_merger3_arready)
    ,.b_arvalid(splitter1_merger3_arvalid)
    ,.b_awaddr(splitter1_merger3_awaddr[31:0])
    ,.b_awburst(splitter1_merger3_awburst[1:0])
    ,.b_awextras(splitter1_merger3_awextras[(EXTRAS - 1):0])
    ,.b_awid(splitter1_merger3_awid[(IDWID - 1):0])
    ,.b_awlen(splitter1_merger3_awlen[7:0])
    ,.b_awready(splitter1_merger3_awready)
    ,.b_awvalid(splitter1_merger3_awvalid)
    ,.b_bid(splitter1_merger3_bid[(IDWID - 1):0])
    ,.b_bready(splitter1_merger3_bready)
    ,.b_bresp(splitter1_merger3_bresp[1:0])
    ,.b_bvalid(splitter1_merger3_bvalid)
    ,.b_rdata(splitter1_merger3_rdata[(DWID - 1):0])
    ,.b_rid(splitter1_merger3_rid[(IDWID - 1):0])
    ,.b_rlast(splitter1_merger3_rlast)
    ,.b_rready(splitter1_merger3_rready)
    ,.b_rresp(splitter1_merger3_rresp[1:0])
    ,.b_rvalid(splitter1_merger3_rvalid)
    ,.b_wdata(splitter1_merger3_wdata[(DWID - 1):0])
    ,.b_wlast(splitter1_merger3_wlast)
    ,.b_wready(splitter1_merger3_wready)
    ,.b_wstrb(splitter1_merger3_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(splitter1_merger3_wvalid)

    ,.c_araddr(splitter2_merger3_araddr[31:0])
    ,.c_arburst(splitter2_merger3_arburst[1:0])
    ,.c_arextras(splitter2_merger3_arextras[(EXTRAS - 1):0])
    ,.c_arid(splitter2_merger3_arid[(IDWID - 1):0])
    ,.c_arlen(splitter2_merger3_arlen[7:0])
    ,.c_arready(splitter2_merger3_arready)
    ,.c_arvalid(splitter2_merger3_arvalid)
    ,.c_awaddr(splitter2_merger3_awaddr[31:0])
    ,.c_awburst(splitter2_merger3_awburst[1:0])
    ,.c_awextras(splitter2_merger3_awextras[(EXTRAS - 1):0])
    ,.c_awid(splitter2_merger3_awid[(IDWID - 1):0])
    ,.c_awlen(splitter2_merger3_awlen[7:0])
    ,.c_awready(splitter2_merger3_awready)
    ,.c_awvalid(splitter2_merger3_awvalid)
    ,.c_bid(splitter2_merger3_bid[(IDWID - 1):0])
    ,.c_bready(splitter2_merger3_bready)
    ,.c_bresp(splitter2_merger3_bresp[1:0])
    ,.c_bvalid(splitter2_merger3_bvalid)
    ,.c_rdata(splitter2_merger3_rdata[(DWID - 1):0])
    ,.c_rid(splitter2_merger3_rid[(IDWID - 1):0])
    ,.c_rlast(splitter2_merger3_rlast)
    ,.c_rready(splitter2_merger3_rready)
    ,.c_rresp(splitter2_merger3_rresp[1:0])
    ,.c_rvalid(splitter2_merger3_rvalid)
    ,.c_wdata(splitter2_merger3_wdata[(DWID - 1):0])
    ,.c_wlast(splitter2_merger3_wlast)
    ,.c_wready(splitter2_merger3_wready)
    ,.c_wstrb(splitter2_merger3_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(splitter2_merger3_wvalid)

    ,.d_araddr(splitter3_merger3_araddr[31:0])
    ,.d_arburst(splitter3_merger3_arburst[1:0])
    ,.d_arextras(splitter3_merger3_arextras[(EXTRAS - 1):0])
    ,.d_arid(splitter3_merger3_arid[(IDWID - 1):0])
    ,.d_arlen(splitter3_merger3_arlen[7:0])
    ,.d_arready(splitter3_merger3_arready)
    ,.d_arvalid(splitter3_merger3_arvalid)
    ,.d_awaddr(splitter3_merger3_awaddr[31:0])
    ,.d_awburst(splitter3_merger3_awburst[1:0])
    ,.d_awextras(splitter3_merger3_awextras[(EXTRAS - 1):0])
    ,.d_awid(splitter3_merger3_awid[(IDWID - 1):0])
    ,.d_awlen(splitter3_merger3_awlen[7:0])
    ,.d_awready(splitter3_merger3_awready)
    ,.d_awvalid(splitter3_merger3_awvalid)
    ,.d_bid(splitter3_merger3_bid[(IDWID - 1):0])
    ,.d_bready(splitter3_merger3_bready)
    ,.d_bresp(splitter3_merger3_bresp[1:0])
    ,.d_bvalid(splitter3_merger3_bvalid)
    ,.d_rdata(splitter3_merger3_rdata[(DWID - 1):0])
    ,.d_rid(splitter3_merger3_rid[(IDWID - 1):0])
    ,.d_rlast(splitter3_merger3_rlast)
    ,.d_rready(splitter3_merger3_rready)
    ,.d_rresp(splitter3_merger3_rresp[1:0])
    ,.d_rvalid(splitter3_merger3_rvalid)
    ,.d_wdata(splitter3_merger3_wdata[(DWID - 1):0])
    ,.d_wlast(splitter3_merger3_wlast)
    ,.d_wready(splitter3_merger3_wready)
    ,.d_wstrb(splitter3_merger3_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(splitter3_merger3_wvalid)
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

