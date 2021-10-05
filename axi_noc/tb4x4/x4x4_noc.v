
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

wire [IDWID-1:0] merger0_splitter0_arid ;
wire [31:0] merger0_splitter0_araddr ;
wire [7:0] merger0_splitter0_arlen ;
wire [EXTRAS-1:0] merger0_splitter0_arextras ;
wire [1:0] merger0_splitter0_arburst ;
wire merger0_splitter0_arvalid ;
wire merger0_splitter0_arready ;
wire [IDWID-1:0] merger0_splitter0_rid ;
wire [DWID-1:0] merger0_splitter0_rdata ;
wire [1:0] merger0_splitter0_rresp ;
wire merger0_splitter0_rlast ;
wire merger0_splitter0_rvalid ;
wire merger0_splitter0_rready ;

wire [IDWID-1:0] merger0_splitter0_awid ;
wire [31:0] merger0_splitter0_awaddr ;
wire [7:0] merger0_splitter0_awlen ;
wire [EXTRAS-1:0] merger0_splitter0_awextras ;
wire [1:0] merger0_splitter0_awburst ;
wire merger0_splitter0_awvalid ;
wire merger0_splitter0_awready ;
wire [DWID-1:0] merger0_splitter0_wdata ;
wire [WSTRB-1:0] merger0_splitter0_wstrb ;
wire merger0_splitter0_wlast ;
wire merger0_splitter0_wvalid ;
wire merger0_splitter0_wready ;
wire [IDWID-1:0] merger0_splitter0_bid ;
wire [1:0] merger0_splitter0_bresp ;
wire merger0_splitter0_bvalid ;
wire merger0_splitter0_bready ;


axi_4_merger merger0 (
     .clk(clk),.rst_n(rst_n)
    ,.araddr(merger0_splitter0_araddr[31:0])
    ,.arburst(merger0_splitter0_arburst[1:0])
    ,.arextras(merger0_splitter0_arextras[(EXTRAS - 1):0])
    ,.arid(merger0_splitter0_arid[(IDWID - 1):0])
    ,.arlen(merger0_splitter0_arlen[7:0])
    ,.arready(merger0_splitter0_arready)
    ,.arvalid(merger0_splitter0_arvalid)
    ,.awaddr(merger0_splitter0_awaddr[31:0])
    ,.awburst(merger0_splitter0_awburst[1:0])
    ,.awextras(merger0_splitter0_awextras[(EXTRAS - 1):0])
    ,.awid(merger0_splitter0_awid[3:0])
    ,.awlen(merger0_splitter0_awlen[7:0])
    ,.awready(merger0_splitter0_awready)
    ,.awvalid(merger0_splitter0_awvalid)
    ,.bid(merger0_splitter0_bid[(IDWID - 1):0])
    ,.bready(merger0_splitter0_bready)
    ,.bresp(merger0_splitter0_bresp[1:0])
    ,.bvalid(merger0_splitter0_bvalid)
    ,.rid(merger0_splitter0_rid[(IDWID - 1):0])
    ,.rlast(merger0_splitter0_rlast)
    ,.rready(merger0_splitter0_rready)
    ,.rresp(merger0_splitter0_rresp[1:0])
    ,.rvalid(merger0_splitter0_rvalid)
    ,.rdata(merger0_splitter0_rdata[(DWID - 1):0])
    ,.wdata(merger0_splitter0_wdata[(DWID - 1):0])
    ,.wlast(merger0_splitter0_wlast)
    ,.wready(merger0_splitter0_wready)
    ,.wstrb(merger0_splitter0_wstrb[(WSTRB - 1):0])
    ,.wvalid(merger0_splitter0_wvalid)


    ,.a_araddr(mst0_araddr[31:0])
    ,.a_arburst(mst0_arburst[1:0])
    ,.a_arextras(mst0_arextras[(EXTRAS - 1):0])
    ,.a_arid(mst0_arid[(IDWID - 1):0])
    ,.a_arlen(mst0_arlen[7:0])
    ,.a_arready(mst0_arready)
    ,.a_arvalid(mst0_arvalid)
    ,.a_awaddr(mst0_awaddr[31:0])
    ,.a_awburst(mst0_awburst[1:0])
    ,.a_awextras(mst0_awextras[(EXTRAS - 1):0])
    ,.a_awid(mst0_awid[(IDWID - 1):0])
    ,.a_awlen(mst0_awlen[7:0])
    ,.a_awready(mst0_awready)
    ,.a_awvalid(mst0_awvalid)
    ,.a_bid(mst0_bid[(IDWID - 1):0])
    ,.a_bready(mst0_bready)
    ,.a_bresp(mst0_bresp[1:0])
    ,.a_bvalid(mst0_bvalid)
    ,.a_rdata(mst0_rdata[(DWID - 1):0])
    ,.a_rid(mst0_rid[(IDWID - 1):0])
    ,.a_rlast(mst0_rlast)
    ,.a_rready(mst0_rready)
    ,.a_rresp(mst0_rresp[1:0])
    ,.a_rvalid(mst0_rvalid)
    ,.a_wdata(mst0_wdata[(DWID - 1):0])
    ,.a_wlast(mst0_wlast)
    ,.a_wready(mst0_wready)
    ,.a_wstrb(mst0_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(mst0_wvalid)

    ,.b_araddr(mst1_araddr[31:0])
    ,.b_arburst(mst1_arburst[1:0])
    ,.b_arextras(mst1_arextras[(EXTRAS - 1):0])
    ,.b_arid(mst1_arid[(IDWID - 1):0])
    ,.b_arlen(mst1_arlen[7:0])
    ,.b_arready(mst1_arready)
    ,.b_arvalid(mst1_arvalid)
    ,.b_awaddr(mst1_awaddr[31:0])
    ,.b_awburst(mst1_awburst[1:0])
    ,.b_awextras(mst1_awextras[(EXTRAS - 1):0])
    ,.b_awid(mst1_awid[(IDWID - 1):0])
    ,.b_awlen(mst1_awlen[7:0])
    ,.b_awready(mst1_awready)
    ,.b_awvalid(mst1_awvalid)
    ,.b_bid(mst1_bid[(IDWID - 1):0])
    ,.b_bready(mst1_bready)
    ,.b_bresp(mst1_bresp[1:0])
    ,.b_bvalid(mst1_bvalid)
    ,.b_rdata(mst1_rdata[(DWID - 1):0])
    ,.b_rid(mst1_rid[(IDWID - 1):0])
    ,.b_rlast(mst1_rlast)
    ,.b_rready(mst1_rready)
    ,.b_rresp(mst1_rresp[1:0])
    ,.b_rvalid(mst1_rvalid)
    ,.b_wdata(mst1_wdata[(DWID - 1):0])
    ,.b_wlast(mst1_wlast)
    ,.b_wready(mst1_wready)
    ,.b_wstrb(mst1_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(mst1_wvalid)

    ,.c_araddr(mst2_araddr[31:0])
    ,.c_arburst(mst2_arburst[1:0])
    ,.c_arextras(mst2_arextras[(EXTRAS - 1):0])
    ,.c_arid(mst2_arid[(IDWID - 1):0])
    ,.c_arlen(mst2_arlen[7:0])
    ,.c_arready(mst2_arready)
    ,.c_arvalid(mst2_arvalid)
    ,.c_awaddr(mst2_awaddr[31:0])
    ,.c_awburst(mst2_awburst[1:0])
    ,.c_awextras(mst2_awextras[(EXTRAS - 1):0])
    ,.c_awid(mst2_awid[(IDWID - 1):0])
    ,.c_awlen(mst2_awlen[7:0])
    ,.c_awready(mst2_awready)
    ,.c_awvalid(mst2_awvalid)
    ,.c_bid(mst2_bid[(IDWID - 1):0])
    ,.c_bready(mst2_bready)
    ,.c_bresp(mst2_bresp[1:0])
    ,.c_bvalid(mst2_bvalid)
    ,.c_rdata(mst2_rdata[(DWID - 1):0])
    ,.c_rid(mst2_rid[(IDWID - 1):0])
    ,.c_rlast(mst2_rlast)
    ,.c_rready(mst2_rready)
    ,.c_rresp(mst2_rresp[1:0])
    ,.c_rvalid(mst2_rvalid)
    ,.c_wdata(mst2_wdata[(DWID - 1):0])
    ,.c_wlast(mst2_wlast)
    ,.c_wready(mst2_wready)
    ,.c_wstrb(mst2_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(mst2_wvalid)

    ,.d_araddr(mst3_araddr[31:0])
    ,.d_arburst(mst3_arburst[1:0])
    ,.d_arextras(mst3_arextras[(EXTRAS - 1):0])
    ,.d_arid(mst3_arid[(IDWID - 1):0])
    ,.d_arlen(mst3_arlen[7:0])
    ,.d_arready(mst3_arready)
    ,.d_arvalid(mst3_arvalid)
    ,.d_awaddr(mst3_awaddr[31:0])
    ,.d_awburst(mst3_awburst[1:0])
    ,.d_awextras(mst3_awextras[(EXTRAS - 1):0])
    ,.d_awid(mst3_awid[(IDWID - 1):0])
    ,.d_awlen(mst3_awlen[7:0])
    ,.d_awready(mst3_awready)
    ,.d_awvalid(mst3_awvalid)
    ,.d_bid(mst3_bid[(IDWID - 1):0])
    ,.d_bready(mst3_bready)
    ,.d_bresp(mst3_bresp[1:0])
    ,.d_bvalid(mst3_bvalid)
    ,.d_rdata(mst3_rdata[(DWID - 1):0])
    ,.d_rid(mst3_rid[(IDWID - 1):0])
    ,.d_rlast(mst3_rlast)
    ,.d_rready(mst3_rready)
    ,.d_rresp(mst3_rresp[1:0])
    ,.d_rvalid(mst3_rvalid)
    ,.d_wdata(mst3_wdata[(DWID - 1):0])
    ,.d_wlast(mst3_wlast)
    ,.d_wready(mst3_wready)
    ,.d_wstrb(mst3_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(mst3_wvalid)
);


axi_4_splitter splitter0 (
     .clk(clk) ,.rst_n(rst_n)

    ,.araddr(merger0_splitter0_araddr[31:0])
    ,.arburst(merger0_splitter0_arburst[1:0])
    ,.arextras(merger0_splitter0_arextras[(EXTRAS - 1):0])
    ,.arid(merger0_splitter0_arid[(IDWID - 1):0])
    ,.arlen(merger0_splitter0_arlen[7:0])
    ,.arready(merger0_splitter0_arready)
    ,.arvalid(merger0_splitter0_arvalid)
    ,.awaddr(merger0_splitter0_awaddr[31:0])
    ,.awburst(merger0_splitter0_awburst[1:0])
    ,.awextras(merger0_splitter0_awextras[(EXTRAS - 1):0])
    ,.awid(merger0_splitter0_awid[3:0])
    ,.awlen(merger0_splitter0_awlen[7:0])
    ,.awready(merger0_splitter0_awready)
    ,.awvalid(merger0_splitter0_awvalid)
    ,.bid(merger0_splitter0_bid[(IDWID - 1):0])
    ,.bready(merger0_splitter0_bready)
    ,.bresp(merger0_splitter0_bresp[1:0])
    ,.bvalid(merger0_splitter0_bvalid)
    ,.rdata(merger0_splitter0_rdata[(DWID - 1):0])
    ,.rid(merger0_splitter0_rid[(IDWID - 1):0])
    ,.rlast(merger0_splitter0_rlast)
    ,.rready(merger0_splitter0_rready)
    ,.rresp(merger0_splitter0_rresp[1:0])
    ,.rvalid(merger0_splitter0_rvalid)
    ,.wdata(merger0_splitter0_wdata[(DWID - 1):0])
    ,.wlast(merger0_splitter0_wlast)
    ,.wready(merger0_splitter0_wready)
    ,.wstrb(merger0_splitter0_wstrb[(WSTRB - 1):0])
    ,.wvalid(merger0_splitter0_wvalid)

    ,.a_araddr(slv0_araddr[31:0])
    ,.a_arburst(slv0_arburst[1:0])
    ,.a_arextras(slv0_arextras[(EXTRAS - 1):0])
    ,.a_arid(slv0_arid[(IDWID - 1):0])
    ,.a_arlen(slv0_arlen[7:0])
    ,.a_arready(slv0_arready)
    ,.a_arvalid(slv0_arvalid)
    ,.a_awaddr(slv0_awaddr[31:0])
    ,.a_awburst(slv0_awburst[1:0])
    ,.a_awextras(slv0_awextras[(EXTRAS - 1):0])
    ,.a_awid(slv0_awid[(IDWID - 1):0])
    ,.a_awlen(slv0_awlen[7:0])
    ,.a_awready(slv0_awready)
    ,.a_awvalid(slv0_awvalid)
    ,.a_bid(slv0_bid[(IDWID - 1):0])
    ,.a_bready(slv0_bready)
    ,.a_bresp(slv0_bresp[1:0])
    ,.a_bvalid(slv0_bvalid)
    ,.a_rdata(slv0_rdata[(DWID - 1):0])
    ,.a_rid(slv0_rid[(IDWID - 1):0])
    ,.a_rlast(slv0_rlast)
    ,.a_rready(slv0_rready)
    ,.a_rresp(slv0_rresp[1:0])
    ,.a_rvalid(slv0_rvalid)
    ,.a_wdata(slv0_wdata[(DWID - 1):0])
    ,.a_wlast(slv0_wlast)
    ,.a_wready(slv0_wready)
    ,.a_wstrb(slv0_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(slv0_wvalid)
    ,.b_araddr(slv1_araddr[31:0])
    ,.b_arburst(slv1_arburst[1:0])
    ,.b_arextras(slv1_arextras[(EXTRAS - 1):0])
    ,.b_arid(slv1_arid[(IDWID - 1):0])
    ,.b_arlen(slv1_arlen[7:0])
    ,.b_arready(slv1_arready)
    ,.b_arvalid(slv1_arvalid)
    ,.b_awaddr(slv1_awaddr[31:0])
    ,.b_awburst(slv1_awburst[1:0])
    ,.b_awextras(slv1_awextras[(EXTRAS - 1):0])
    ,.b_awid(slv1_awid[(IDWID - 1):0])
    ,.b_awlen(slv1_awlen[7:0])
    ,.b_awready(slv1_awready)
    ,.b_awvalid(slv1_awvalid)
    ,.b_bid(slv1_bid[(IDWID - 1):0])
    ,.b_bready(slv1_bready)
    ,.b_bresp(slv1_bresp[1:0])
    ,.b_bvalid(slv1_bvalid)
    ,.b_rdata(slv1_rdata[(DWID - 1):0])
    ,.b_rid(slv1_rid[(IDWID - 1):0])
    ,.b_rlast(slv1_rlast)
    ,.b_rready(slv1_rready)
    ,.b_rresp(slv1_rresp[1:0])
    ,.b_rvalid(slv1_rvalid)
    ,.b_wdata(slv1_wdata[(DWID - 1):0])
    ,.b_wlast(slv1_wlast)
    ,.b_wready(slv1_wready)
    ,.b_wstrb(slv1_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(slv1_wvalid)
    ,.c_araddr(slv2_araddr[31:0])
    ,.c_arburst(slv2_arburst[1:0])
    ,.c_arextras(slv2_arextras[(EXTRAS - 1):0])
    ,.c_arid(slv2_arid[(IDWID - 1):0])
    ,.c_arlen(slv2_arlen[7:0])
    ,.c_arready(slv2_arready)
    ,.c_arvalid(slv2_arvalid)
    ,.c_awaddr(slv2_awaddr[31:0])
    ,.c_awburst(slv2_awburst[1:0])
    ,.c_awextras(slv2_awextras[(EXTRAS - 1):0])
    ,.c_awid(slv2_awid[(IDWID - 1):0])
    ,.c_awlen(slv2_awlen[7:0])
    ,.c_awready(slv2_awready)
    ,.c_awvalid(slv2_awvalid)
    ,.c_bid(slv2_bid[(IDWID - 1):0])
    ,.c_bready(slv2_bready)
    ,.c_bresp(slv2_bresp[1:0])
    ,.c_bvalid(slv2_bvalid)
    ,.c_rdata(slv2_rdata[(DWID - 1):0])
    ,.c_rid(slv2_rid[(IDWID - 1):0])
    ,.c_rlast(slv2_rlast)
    ,.c_rready(slv2_rready)
    ,.c_rresp(slv2_rresp[1:0])
    ,.c_rvalid(slv2_rvalid)
    ,.c_wdata(slv2_wdata[(DWID - 1):0])
    ,.c_wlast(slv2_wlast)
    ,.c_wready(slv2_wready)
    ,.c_wstrb(slv2_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(slv2_wvalid)
    ,.d_araddr(slv3_araddr[31:0])
    ,.d_arburst(slv3_arburst[1:0])
    ,.d_arextras(slv3_arextras[(EXTRAS - 1):0])
    ,.d_arid(slv3_arid[(IDWID - 1):0])
    ,.d_arlen(slv3_arlen[7:0])
    ,.d_arready(slv3_arready)
    ,.d_arvalid(slv3_arvalid)
    ,.d_awaddr(slv3_awaddr[31:0])
    ,.d_awburst(slv3_awburst[1:0])
    ,.d_awextras(slv3_awextras[(EXTRAS - 1):0])
    ,.d_awid(slv3_awid[(IDWID - 1):0])
    ,.d_awlen(slv3_awlen[7:0])
    ,.d_awready(slv3_awready)
    ,.d_awvalid(slv3_awvalid)
    ,.d_bid(slv3_bid[(IDWID - 1):0])
    ,.d_bready(slv3_bready)
    ,.d_bresp(slv3_bresp[1:0])
    ,.d_bvalid(slv3_bvalid)
    ,.d_rdata(slv3_rdata[(DWID - 1):0])
    ,.d_rid(slv3_rid[(IDWID - 1):0])
    ,.d_rlast(slv3_rlast)
    ,.d_rready(slv3_rready)
    ,.d_rresp(slv3_rresp[1:0])
    ,.d_rvalid(slv3_rvalid)
    ,.d_wdata(slv3_wdata[(DWID - 1):0])
    ,.d_wlast(slv3_wlast)
    ,.d_wready(slv3_wready)
    ,.d_wstrb(slv3_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(slv3_wvalid)

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

