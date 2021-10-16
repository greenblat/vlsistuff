
    module clk #(parameter IDWID=4, parameter DWID=64, parameter EXTRAS=8, parameter WSTRB=DWID/8) ( input clk, input rst_n

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
    ,input clock0
    ,input clock1
);

wire [IDWID-1:0] split0_clock0_arid ;
wire [31:0] split0_clock0_araddr ;
wire [7:0] split0_clock0_arlen ;
wire [EXTRAS-1:0] split0_clock0_arextras ;
wire [1:0] split0_clock0_arburst ;
wire split0_clock0_arvalid ;
wire split0_clock0_arready ;
wire [IDWID-1:0] split0_clock0_rid ;
wire [DWID-1:0] split0_clock0_rdata ;
wire [1:0] split0_clock0_rresp ;
wire split0_clock0_rlast ;
wire split0_clock0_rvalid ;
wire split0_clock0_rready ;

wire [IDWID-1:0] split0_clock0_awid ;
wire [31:0] split0_clock0_awaddr ;
wire [7:0] split0_clock0_awlen ;
wire [EXTRAS-1:0] split0_clock0_awextras ;
wire [1:0] split0_clock0_awburst ;
wire split0_clock0_awvalid ;
wire split0_clock0_awready ;
wire [DWID-1:0] split0_clock0_wdata ;
wire [WSTRB-1:0] split0_clock0_wstrb ;
wire split0_clock0_wlast ;
wire split0_clock0_wvalid ;
wire split0_clock0_wready ;
wire [IDWID-1:0] split0_clock0_bid ;
wire [1:0] split0_clock0_bresp ;
wire split0_clock0_bvalid ;
wire split0_clock0_bready ;


wire [IDWID-1:0] split0_clock1_arid ;
wire [31:0] split0_clock1_araddr ;
wire [7:0] split0_clock1_arlen ;
wire [EXTRAS-1:0] split0_clock1_arextras ;
wire [1:0] split0_clock1_arburst ;
wire split0_clock1_arvalid ;
wire split0_clock1_arready ;
wire [IDWID-1:0] split0_clock1_rid ;
wire [DWID-1:0] split0_clock1_rdata ;
wire [1:0] split0_clock1_rresp ;
wire split0_clock1_rlast ;
wire split0_clock1_rvalid ;
wire split0_clock1_rready ;

wire [IDWID-1:0] split0_clock1_awid ;
wire [31:0] split0_clock1_awaddr ;
wire [7:0] split0_clock1_awlen ;
wire [EXTRAS-1:0] split0_clock1_awextras ;
wire [1:0] split0_clock1_awburst ;
wire split0_clock1_awvalid ;
wire split0_clock1_awready ;
wire [DWID-1:0] split0_clock1_wdata ;
wire [WSTRB-1:0] split0_clock1_wstrb ;
wire split0_clock1_wlast ;
wire split0_clock1_wvalid ;
wire split0_clock1_wready ;
wire [IDWID-1:0] split0_clock1_bid ;
wire [1:0] split0_clock1_bresp ;
wire split0_clock1_bvalid ;
wire split0_clock1_bready ;


axi_4_splitter split0 (
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

    ,.a_araddr(split0_clock0_araddr[31:0])
    ,.a_arburst(split0_clock0_arburst[1:0])
    ,.a_arextras(split0_clock0_arextras[(EXTRAS - 1):0])
    ,.a_arid(split0_clock0_arid[(IDWID - 1):0])
    ,.a_arlen(split0_clock0_arlen[7:0])
    ,.a_arready(split0_clock0_arready)
    ,.a_arvalid(split0_clock0_arvalid)
    ,.a_awaddr(split0_clock0_awaddr[31:0])
    ,.a_awburst(split0_clock0_awburst[1:0])
    ,.a_awextras(split0_clock0_awextras[(EXTRAS - 1):0])
    ,.a_awid(split0_clock0_awid[(IDWID - 1):0])
    ,.a_awlen(split0_clock0_awlen[7:0])
    ,.a_awready(split0_clock0_awready)
    ,.a_awvalid(split0_clock0_awvalid)
    ,.a_bid(split0_clock0_bid[(IDWID - 1):0])
    ,.a_bready(split0_clock0_bready)
    ,.a_bresp(split0_clock0_bresp[1:0])
    ,.a_bvalid(split0_clock0_bvalid)
    ,.a_rdata(split0_clock0_rdata[(DWID - 1):0])
    ,.a_rid(split0_clock0_rid[(IDWID - 1):0])
    ,.a_rlast(split0_clock0_rlast)
    ,.a_rready(split0_clock0_rready)
    ,.a_rresp(split0_clock0_rresp[1:0])
    ,.a_rvalid(split0_clock0_rvalid)
    ,.a_wdata(split0_clock0_wdata[(DWID - 1):0])
    ,.a_wlast(split0_clock0_wlast)
    ,.a_wready(split0_clock0_wready)
    ,.a_wstrb(split0_clock0_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(split0_clock0_wvalid)
    ,.b_araddr(split0_clock1_araddr[31:0])
    ,.b_arburst(split0_clock1_arburst[1:0])
    ,.b_arextras(split0_clock1_arextras[(EXTRAS - 1):0])
    ,.b_arid(split0_clock1_arid[(IDWID - 1):0])
    ,.b_arlen(split0_clock1_arlen[7:0])
    ,.b_arready(split0_clock1_arready)
    ,.b_arvalid(split0_clock1_arvalid)
    ,.b_awaddr(split0_clock1_awaddr[31:0])
    ,.b_awburst(split0_clock1_awburst[1:0])
    ,.b_awextras(split0_clock1_awextras[(EXTRAS - 1):0])
    ,.b_awid(split0_clock1_awid[(IDWID - 1):0])
    ,.b_awlen(split0_clock1_awlen[7:0])
    ,.b_awready(split0_clock1_awready)
    ,.b_awvalid(split0_clock1_awvalid)
    ,.b_bid(split0_clock1_bid[(IDWID - 1):0])
    ,.b_bready(split0_clock1_bready)
    ,.b_bresp(split0_clock1_bresp[1:0])
    ,.b_bvalid(split0_clock1_bvalid)
    ,.b_rdata(split0_clock1_rdata[(DWID - 1):0])
    ,.b_rid(split0_clock1_rid[(IDWID - 1):0])
    ,.b_rlast(split0_clock1_rlast)
    ,.b_rready(split0_clock1_rready)
    ,.b_rresp(split0_clock1_rresp[1:0])
    ,.b_rvalid(split0_clock1_rvalid)
    ,.b_wdata(split0_clock1_wdata[(DWID - 1):0])
    ,.b_wlast(split0_clock1_wlast)
    ,.b_wready(split0_clock1_wready)
    ,.b_wstrb(split0_clock1_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(split0_clock1_wvalid)
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

axi2clock axi_clock0 (
     .in_clk(clk),.rst_n(rst_n)
    ,.ou_clk(clock0)


    ,.in_araddr(split0_clock0_araddr[31:0])
    ,.in_arburst(split0_clock0_arburst[1:0])
    ,.in_arextras(split0_clock0_arextras[(EXTRAS - 1):0])
    ,.in_arid(split0_clock0_arid[(IDWID - 1):0])
    ,.in_arlen(split0_clock0_arlen[7:0])
    ,.in_arready(split0_clock0_arready)
    ,.in_arvalid(split0_clock0_arvalid)
    ,.in_awaddr(split0_clock0_awaddr[31:0])
    ,.in_awburst(split0_clock0_awburst[1:0])
    ,.in_awextras(split0_clock0_awextras[(EXTRAS - 1):0])
    ,.in_awid(split0_clock0_awid[(IDWID - 1):0])
    ,.in_awlen(split0_clock0_awlen[7:0])
    ,.in_awready(split0_clock0_awready)
    ,.in_awvalid(split0_clock0_awvalid)
    ,.in_bid(split0_clock0_bid[(IDWID - 1):0])
    ,.in_bready(split0_clock0_bready)
    ,.in_bresp(split0_clock0_bresp[1:0])
    ,.in_bvalid(split0_clock0_bvalid)
    ,.in_rdata(split0_clock0_rdata[(DWID - 1):0])
    ,.in_rid(split0_clock0_rid[(IDWID - 1):0])
    ,.in_rlast(split0_clock0_rlast)
    ,.in_rready(split0_clock0_rready)
    ,.in_rresp(split0_clock0_rresp[1:0])
    ,.in_rvalid(split0_clock0_rvalid)
    ,.in_wdata(split0_clock0_wdata[(DWID - 1):0])
    ,.in_wlast(split0_clock0_wlast)
    ,.in_wready(split0_clock0_wready)
    ,.in_wstrb(split0_clock0_wstrb[(WSTRB - 1):0])
    ,.in_wvalid(split0_clock0_wvalid)

    ,.ou_araddr(slv0_araddr[31:0])
    ,.ou_arburst(slv0_arburst[1:0])
    ,.ou_arextras(slv0_arextras[(EXTRAS - 1):0])
    ,.ou_arid(slv0_arid[(IDWID - 1):0])
    ,.ou_arlen(slv0_arlen[7:0])
    ,.ou_arready(slv0_arready)
    ,.ou_arvalid(slv0_arvalid)
    ,.ou_awaddr(slv0_awaddr[31:0])
    ,.ou_awburst(slv0_awburst[1:0])
    ,.ou_awextras(slv0_awextras[(EXTRAS - 1):0])
    ,.ou_awid(slv0_awid[(IDWID - 1):0])
    ,.ou_awlen(slv0_awlen[7:0])
    ,.ou_awready(slv0_awready)
    ,.ou_awvalid(slv0_awvalid)
    ,.ou_bid(slv0_bid[(IDWID - 1):0])
    ,.ou_bready(slv0_bready)
    ,.ou_bresp(slv0_bresp[1:0])
    ,.ou_bvalid(slv0_bvalid)
    ,.ou_rdata(slv0_rdata[(DWID - 1):0])
    ,.ou_rid(slv0_rid[(IDWID - 1):0])
    ,.ou_rlast(slv0_rlast)
    ,.ou_rready(slv0_rready)
    ,.ou_rresp(slv0_rresp[1:0])
    ,.ou_rvalid(slv0_rvalid)
    ,.ou_wdata(slv0_wdata[(DWID - 1):0])
    ,.ou_wlast(slv0_wlast)
    ,.ou_wready(slv0_wready)
    ,.ou_wstrb(slv0_wstrb[(WSTRB - 1):0])
    ,.ou_wvalid(slv0_wvalid)

);


axi2clock axi_clock1 (
     .in_clk(clk),.rst_n(rst_n)
    ,.ou_clk(clock1)


    ,.in_araddr(split0_clock1_araddr[31:0])
    ,.in_arburst(split0_clock1_arburst[1:0])
    ,.in_arextras(split0_clock1_arextras[(EXTRAS - 1):0])
    ,.in_arid(split0_clock1_arid[(IDWID - 1):0])
    ,.in_arlen(split0_clock1_arlen[7:0])
    ,.in_arready(split0_clock1_arready)
    ,.in_arvalid(split0_clock1_arvalid)
    ,.in_awaddr(split0_clock1_awaddr[31:0])
    ,.in_awburst(split0_clock1_awburst[1:0])
    ,.in_awextras(split0_clock1_awextras[(EXTRAS - 1):0])
    ,.in_awid(split0_clock1_awid[(IDWID - 1):0])
    ,.in_awlen(split0_clock1_awlen[7:0])
    ,.in_awready(split0_clock1_awready)
    ,.in_awvalid(split0_clock1_awvalid)
    ,.in_bid(split0_clock1_bid[(IDWID - 1):0])
    ,.in_bready(split0_clock1_bready)
    ,.in_bresp(split0_clock1_bresp[1:0])
    ,.in_bvalid(split0_clock1_bvalid)
    ,.in_rdata(split0_clock1_rdata[(DWID - 1):0])
    ,.in_rid(split0_clock1_rid[(IDWID - 1):0])
    ,.in_rlast(split0_clock1_rlast)
    ,.in_rready(split0_clock1_rready)
    ,.in_rresp(split0_clock1_rresp[1:0])
    ,.in_rvalid(split0_clock1_rvalid)
    ,.in_wdata(split0_clock1_wdata[(DWID - 1):0])
    ,.in_wlast(split0_clock1_wlast)
    ,.in_wready(split0_clock1_wready)
    ,.in_wstrb(split0_clock1_wstrb[(WSTRB - 1):0])
    ,.in_wvalid(split0_clock1_wvalid)

    ,.ou_araddr(slv1_araddr[31:0])
    ,.ou_arburst(slv1_arburst[1:0])
    ,.ou_arextras(slv1_arextras[(EXTRAS - 1):0])
    ,.ou_arid(slv1_arid[(IDWID - 1):0])
    ,.ou_arlen(slv1_arlen[7:0])
    ,.ou_arready(slv1_arready)
    ,.ou_arvalid(slv1_arvalid)
    ,.ou_awaddr(slv1_awaddr[31:0])
    ,.ou_awburst(slv1_awburst[1:0])
    ,.ou_awextras(slv1_awextras[(EXTRAS - 1):0])
    ,.ou_awid(slv1_awid[(IDWID - 1):0])
    ,.ou_awlen(slv1_awlen[7:0])
    ,.ou_awready(slv1_awready)
    ,.ou_awvalid(slv1_awvalid)
    ,.ou_bid(slv1_bid[(IDWID - 1):0])
    ,.ou_bready(slv1_bready)
    ,.ou_bresp(slv1_bresp[1:0])
    ,.ou_bvalid(slv1_bvalid)
    ,.ou_rdata(slv1_rdata[(DWID - 1):0])
    ,.ou_rid(slv1_rid[(IDWID - 1):0])
    ,.ou_rlast(slv1_rlast)
    ,.ou_rready(slv1_rready)
    ,.ou_rresp(slv1_rresp[1:0])
    ,.ou_rvalid(slv1_rvalid)
    ,.ou_wdata(slv1_wdata[(DWID - 1):0])
    ,.ou_wlast(slv1_wlast)
    ,.ou_wready(slv1_wready)
    ,.ou_wstrb(slv1_wstrb[(WSTRB - 1):0])
    ,.ou_wvalid(slv1_wvalid)

);

endmodule
