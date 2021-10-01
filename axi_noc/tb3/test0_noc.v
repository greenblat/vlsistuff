
    module test0 #(parameter IDWID=4, parameter DWID=64, parameter EXTRAS=8, parameter WSTRB=DWID/8) ( input clk, input rst_n

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

    ,output [IDWID-1:0] slv10_arid
    ,output [31:0] slv10_araddr
    ,output [7:0] slv10_arlen
    ,output [EXTRAS-1:0] slv10_arextras
    ,output [1:0] slv10_arburst
    ,output slv10_arvalid
    ,input slv10_arready
    ,input [IDWID-1:0] slv10_rid
    ,input [DWID-1:0] slv10_rdata
    ,input [1:0] slv10_rresp
    ,input slv10_rlast
    ,input slv10_rvalid
    ,output slv10_rready

    ,output [IDWID-1:0] slv10_awid
    ,output [31:0] slv10_awaddr
    ,output [7:0] slv10_awlen
    ,output [EXTRAS-1:0] slv10_awextras
    ,output [1:0] slv10_awburst
    ,output slv10_awvalid
    ,input slv10_awready
    ,output [DWID-1:0] slv10_wdata
    ,output [WSTRB-1:0] slv10_wstrb
    ,output slv10_wlast
    ,output slv10_wvalid
    ,input slv10_wready
    ,input [IDWID-1:0] slv10_bid
    ,input [1:0] slv10_bresp
    ,input slv10_bvalid
    ,output slv10_bready

    ,output [IDWID-1:0] slv11_arid
    ,output [31:0] slv11_araddr
    ,output [7:0] slv11_arlen
    ,output [EXTRAS-1:0] slv11_arextras
    ,output [1:0] slv11_arburst
    ,output slv11_arvalid
    ,input slv11_arready
    ,input [IDWID-1:0] slv11_rid
    ,input [DWID-1:0] slv11_rdata
    ,input [1:0] slv11_rresp
    ,input slv11_rlast
    ,input slv11_rvalid
    ,output slv11_rready

    ,output [IDWID-1:0] slv11_awid
    ,output [31:0] slv11_awaddr
    ,output [7:0] slv11_awlen
    ,output [EXTRAS-1:0] slv11_awextras
    ,output [1:0] slv11_awburst
    ,output slv11_awvalid
    ,input slv11_awready
    ,output [DWID-1:0] slv11_wdata
    ,output [WSTRB-1:0] slv11_wstrb
    ,output slv11_wlast
    ,output slv11_wvalid
    ,input slv11_wready
    ,input [IDWID-1:0] slv11_bid
    ,input [1:0] slv11_bresp
    ,input slv11_bvalid
    ,output slv11_bready

    ,output [IDWID-1:0] slv12_arid
    ,output [31:0] slv12_araddr
    ,output [7:0] slv12_arlen
    ,output [EXTRAS-1:0] slv12_arextras
    ,output [1:0] slv12_arburst
    ,output slv12_arvalid
    ,input slv12_arready
    ,input [IDWID-1:0] slv12_rid
    ,input [DWID-1:0] slv12_rdata
    ,input [1:0] slv12_rresp
    ,input slv12_rlast
    ,input slv12_rvalid
    ,output slv12_rready

    ,output [IDWID-1:0] slv12_awid
    ,output [31:0] slv12_awaddr
    ,output [7:0] slv12_awlen
    ,output [EXTRAS-1:0] slv12_awextras
    ,output [1:0] slv12_awburst
    ,output slv12_awvalid
    ,input slv12_awready
    ,output [DWID-1:0] slv12_wdata
    ,output [WSTRB-1:0] slv12_wstrb
    ,output slv12_wlast
    ,output slv12_wvalid
    ,input slv12_wready
    ,input [IDWID-1:0] slv12_bid
    ,input [1:0] slv12_bresp
    ,input slv12_bvalid
    ,output slv12_bready

    ,output [IDWID-1:0] slv13_arid
    ,output [31:0] slv13_araddr
    ,output [7:0] slv13_arlen
    ,output [EXTRAS-1:0] slv13_arextras
    ,output [1:0] slv13_arburst
    ,output slv13_arvalid
    ,input slv13_arready
    ,input [IDWID-1:0] slv13_rid
    ,input [DWID-1:0] slv13_rdata
    ,input [1:0] slv13_rresp
    ,input slv13_rlast
    ,input slv13_rvalid
    ,output slv13_rready

    ,output [IDWID-1:0] slv13_awid
    ,output [31:0] slv13_awaddr
    ,output [7:0] slv13_awlen
    ,output [EXTRAS-1:0] slv13_awextras
    ,output [1:0] slv13_awburst
    ,output slv13_awvalid
    ,input slv13_awready
    ,output [DWID-1:0] slv13_wdata
    ,output [WSTRB-1:0] slv13_wstrb
    ,output slv13_wlast
    ,output slv13_wvalid
    ,input slv13_wready
    ,input [IDWID-1:0] slv13_bid
    ,input [1:0] slv13_bresp
    ,input slv13_bvalid
    ,output slv13_bready

    ,output [IDWID-1:0] slv14_arid
    ,output [31:0] slv14_araddr
    ,output [7:0] slv14_arlen
    ,output [EXTRAS-1:0] slv14_arextras
    ,output [1:0] slv14_arburst
    ,output slv14_arvalid
    ,input slv14_arready
    ,input [IDWID-1:0] slv14_rid
    ,input [DWID-1:0] slv14_rdata
    ,input [1:0] slv14_rresp
    ,input slv14_rlast
    ,input slv14_rvalid
    ,output slv14_rready

    ,output [IDWID-1:0] slv14_awid
    ,output [31:0] slv14_awaddr
    ,output [7:0] slv14_awlen
    ,output [EXTRAS-1:0] slv14_awextras
    ,output [1:0] slv14_awburst
    ,output slv14_awvalid
    ,input slv14_awready
    ,output [DWID-1:0] slv14_wdata
    ,output [WSTRB-1:0] slv14_wstrb
    ,output slv14_wlast
    ,output slv14_wvalid
    ,input slv14_wready
    ,input [IDWID-1:0] slv14_bid
    ,input [1:0] slv14_bresp
    ,input slv14_bvalid
    ,output slv14_bready

    ,output [IDWID-1:0] slv15_arid
    ,output [31:0] slv15_araddr
    ,output [7:0] slv15_arlen
    ,output [EXTRAS-1:0] slv15_arextras
    ,output [1:0] slv15_arburst
    ,output slv15_arvalid
    ,input slv15_arready
    ,input [IDWID-1:0] slv15_rid
    ,input [DWID-1:0] slv15_rdata
    ,input [1:0] slv15_rresp
    ,input slv15_rlast
    ,input slv15_rvalid
    ,output slv15_rready

    ,output [IDWID-1:0] slv15_awid
    ,output [31:0] slv15_awaddr
    ,output [7:0] slv15_awlen
    ,output [EXTRAS-1:0] slv15_awextras
    ,output [1:0] slv15_awburst
    ,output slv15_awvalid
    ,input slv15_awready
    ,output [DWID-1:0] slv15_wdata
    ,output [WSTRB-1:0] slv15_wstrb
    ,output slv15_wlast
    ,output slv15_wvalid
    ,input slv15_wready
    ,input [IDWID-1:0] slv15_bid
    ,input [1:0] slv15_bresp
    ,input slv15_bvalid
    ,output slv15_bready

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

    ,output [IDWID-1:0] slv4_arid
    ,output [31:0] slv4_araddr
    ,output [7:0] slv4_arlen
    ,output [EXTRAS-1:0] slv4_arextras
    ,output [1:0] slv4_arburst
    ,output slv4_arvalid
    ,input slv4_arready
    ,input [IDWID-1:0] slv4_rid
    ,input [DWID-1:0] slv4_rdata
    ,input [1:0] slv4_rresp
    ,input slv4_rlast
    ,input slv4_rvalid
    ,output slv4_rready

    ,output [IDWID-1:0] slv4_awid
    ,output [31:0] slv4_awaddr
    ,output [7:0] slv4_awlen
    ,output [EXTRAS-1:0] slv4_awextras
    ,output [1:0] slv4_awburst
    ,output slv4_awvalid
    ,input slv4_awready
    ,output [DWID-1:0] slv4_wdata
    ,output [WSTRB-1:0] slv4_wstrb
    ,output slv4_wlast
    ,output slv4_wvalid
    ,input slv4_wready
    ,input [IDWID-1:0] slv4_bid
    ,input [1:0] slv4_bresp
    ,input slv4_bvalid
    ,output slv4_bready

    ,output [IDWID-1:0] slv5_arid
    ,output [31:0] slv5_araddr
    ,output [7:0] slv5_arlen
    ,output [EXTRAS-1:0] slv5_arextras
    ,output [1:0] slv5_arburst
    ,output slv5_arvalid
    ,input slv5_arready
    ,input [IDWID-1:0] slv5_rid
    ,input [DWID-1:0] slv5_rdata
    ,input [1:0] slv5_rresp
    ,input slv5_rlast
    ,input slv5_rvalid
    ,output slv5_rready

    ,output [IDWID-1:0] slv5_awid
    ,output [31:0] slv5_awaddr
    ,output [7:0] slv5_awlen
    ,output [EXTRAS-1:0] slv5_awextras
    ,output [1:0] slv5_awburst
    ,output slv5_awvalid
    ,input slv5_awready
    ,output [DWID-1:0] slv5_wdata
    ,output [WSTRB-1:0] slv5_wstrb
    ,output slv5_wlast
    ,output slv5_wvalid
    ,input slv5_wready
    ,input [IDWID-1:0] slv5_bid
    ,input [1:0] slv5_bresp
    ,input slv5_bvalid
    ,output slv5_bready

    ,output [IDWID-1:0] slv6_arid
    ,output [31:0] slv6_araddr
    ,output [7:0] slv6_arlen
    ,output [EXTRAS-1:0] slv6_arextras
    ,output [1:0] slv6_arburst
    ,output slv6_arvalid
    ,input slv6_arready
    ,input [IDWID-1:0] slv6_rid
    ,input [DWID-1:0] slv6_rdata
    ,input [1:0] slv6_rresp
    ,input slv6_rlast
    ,input slv6_rvalid
    ,output slv6_rready

    ,output [IDWID-1:0] slv6_awid
    ,output [31:0] slv6_awaddr
    ,output [7:0] slv6_awlen
    ,output [EXTRAS-1:0] slv6_awextras
    ,output [1:0] slv6_awburst
    ,output slv6_awvalid
    ,input slv6_awready
    ,output [DWID-1:0] slv6_wdata
    ,output [WSTRB-1:0] slv6_wstrb
    ,output slv6_wlast
    ,output slv6_wvalid
    ,input slv6_wready
    ,input [IDWID-1:0] slv6_bid
    ,input [1:0] slv6_bresp
    ,input slv6_bvalid
    ,output slv6_bready

    ,output [IDWID-1:0] slv7_arid
    ,output [31:0] slv7_araddr
    ,output [7:0] slv7_arlen
    ,output [EXTRAS-1:0] slv7_arextras
    ,output [1:0] slv7_arburst
    ,output slv7_arvalid
    ,input slv7_arready
    ,input [IDWID-1:0] slv7_rid
    ,input [DWID-1:0] slv7_rdata
    ,input [1:0] slv7_rresp
    ,input slv7_rlast
    ,input slv7_rvalid
    ,output slv7_rready

    ,output [IDWID-1:0] slv7_awid
    ,output [31:0] slv7_awaddr
    ,output [7:0] slv7_awlen
    ,output [EXTRAS-1:0] slv7_awextras
    ,output [1:0] slv7_awburst
    ,output slv7_awvalid
    ,input slv7_awready
    ,output [DWID-1:0] slv7_wdata
    ,output [WSTRB-1:0] slv7_wstrb
    ,output slv7_wlast
    ,output slv7_wvalid
    ,input slv7_wready
    ,input [IDWID-1:0] slv7_bid
    ,input [1:0] slv7_bresp
    ,input slv7_bvalid
    ,output slv7_bready

    ,output [IDWID-1:0] slv8_arid
    ,output [31:0] slv8_araddr
    ,output [7:0] slv8_arlen
    ,output [EXTRAS-1:0] slv8_arextras
    ,output [1:0] slv8_arburst
    ,output slv8_arvalid
    ,input slv8_arready
    ,input [IDWID-1:0] slv8_rid
    ,input [DWID-1:0] slv8_rdata
    ,input [1:0] slv8_rresp
    ,input slv8_rlast
    ,input slv8_rvalid
    ,output slv8_rready

    ,output [IDWID-1:0] slv8_awid
    ,output [31:0] slv8_awaddr
    ,output [7:0] slv8_awlen
    ,output [EXTRAS-1:0] slv8_awextras
    ,output [1:0] slv8_awburst
    ,output slv8_awvalid
    ,input slv8_awready
    ,output [DWID-1:0] slv8_wdata
    ,output [WSTRB-1:0] slv8_wstrb
    ,output slv8_wlast
    ,output slv8_wvalid
    ,input slv8_wready
    ,input [IDWID-1:0] slv8_bid
    ,input [1:0] slv8_bresp
    ,input slv8_bvalid
    ,output slv8_bready

    ,output [IDWID-1:0] slv9_arid
    ,output [31:0] slv9_araddr
    ,output [7:0] slv9_arlen
    ,output [EXTRAS-1:0] slv9_arextras
    ,output [1:0] slv9_arburst
    ,output slv9_arvalid
    ,input slv9_arready
    ,input [IDWID-1:0] slv9_rid
    ,input [DWID-1:0] slv9_rdata
    ,input [1:0] slv9_rresp
    ,input slv9_rlast
    ,input slv9_rvalid
    ,output slv9_rready

    ,output [IDWID-1:0] slv9_awid
    ,output [31:0] slv9_awaddr
    ,output [7:0] slv9_awlen
    ,output [EXTRAS-1:0] slv9_awextras
    ,output [1:0] slv9_awburst
    ,output slv9_awvalid
    ,input slv9_awready
    ,output [DWID-1:0] slv9_wdata
    ,output [WSTRB-1:0] slv9_wstrb
    ,output slv9_wlast
    ,output slv9_wvalid
    ,input slv9_wready
    ,input [IDWID-1:0] slv9_bid
    ,input [1:0] slv9_bresp
    ,input slv9_bvalid
    ,output slv9_bready

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

wire [IDWID-1:0] split0_merge0_arid ;
wire [31:0] split0_merge0_araddr ;
wire [7:0] split0_merge0_arlen ;
wire [EXTRAS-1:0] split0_merge0_arextras ;
wire [1:0] split0_merge0_arburst ;
wire split0_merge0_arvalid ;
wire split0_merge0_arready ;
wire [IDWID-1:0] split0_merge0_rid ;
wire [DWID-1:0] split0_merge0_rdata ;
wire [1:0] split0_merge0_rresp ;
wire split0_merge0_rlast ;
wire split0_merge0_rvalid ;
wire split0_merge0_rready ;

wire [IDWID-1:0] split0_merge0_awid ;
wire [31:0] split0_merge0_awaddr ;
wire [7:0] split0_merge0_awlen ;
wire [EXTRAS-1:0] split0_merge0_awextras ;
wire [1:0] split0_merge0_awburst ;
wire split0_merge0_awvalid ;
wire split0_merge0_awready ;
wire [DWID-1:0] split0_merge0_wdata ;
wire [WSTRB-1:0] split0_merge0_wstrb ;
wire split0_merge0_wlast ;
wire split0_merge0_wvalid ;
wire split0_merge0_wready ;
wire [IDWID-1:0] split0_merge0_bid ;
wire [1:0] split0_merge0_bresp ;
wire split0_merge0_bvalid ;
wire split0_merge0_bready ;


wire [IDWID-1:0] split0_merge1_arid ;
wire [31:0] split0_merge1_araddr ;
wire [7:0] split0_merge1_arlen ;
wire [EXTRAS-1:0] split0_merge1_arextras ;
wire [1:0] split0_merge1_arburst ;
wire split0_merge1_arvalid ;
wire split0_merge1_arready ;
wire [IDWID-1:0] split0_merge1_rid ;
wire [DWID-1:0] split0_merge1_rdata ;
wire [1:0] split0_merge1_rresp ;
wire split0_merge1_rlast ;
wire split0_merge1_rvalid ;
wire split0_merge1_rready ;

wire [IDWID-1:0] split0_merge1_awid ;
wire [31:0] split0_merge1_awaddr ;
wire [7:0] split0_merge1_awlen ;
wire [EXTRAS-1:0] split0_merge1_awextras ;
wire [1:0] split0_merge1_awburst ;
wire split0_merge1_awvalid ;
wire split0_merge1_awready ;
wire [DWID-1:0] split0_merge1_wdata ;
wire [WSTRB-1:0] split0_merge1_wstrb ;
wire split0_merge1_wlast ;
wire split0_merge1_wvalid ;
wire split0_merge1_wready ;
wire [IDWID-1:0] split0_merge1_bid ;
wire [1:0] split0_merge1_bresp ;
wire split0_merge1_bvalid ;
wire split0_merge1_bready ;


wire [IDWID-1:0] split0_merge2_arid ;
wire [31:0] split0_merge2_araddr ;
wire [7:0] split0_merge2_arlen ;
wire [EXTRAS-1:0] split0_merge2_arextras ;
wire [1:0] split0_merge2_arburst ;
wire split0_merge2_arvalid ;
wire split0_merge2_arready ;
wire [IDWID-1:0] split0_merge2_rid ;
wire [DWID-1:0] split0_merge2_rdata ;
wire [1:0] split0_merge2_rresp ;
wire split0_merge2_rlast ;
wire split0_merge2_rvalid ;
wire split0_merge2_rready ;

wire [IDWID-1:0] split0_merge2_awid ;
wire [31:0] split0_merge2_awaddr ;
wire [7:0] split0_merge2_awlen ;
wire [EXTRAS-1:0] split0_merge2_awextras ;
wire [1:0] split0_merge2_awburst ;
wire split0_merge2_awvalid ;
wire split0_merge2_awready ;
wire [DWID-1:0] split0_merge2_wdata ;
wire [WSTRB-1:0] split0_merge2_wstrb ;
wire split0_merge2_wlast ;
wire split0_merge2_wvalid ;
wire split0_merge2_wready ;
wire [IDWID-1:0] split0_merge2_bid ;
wire [1:0] split0_merge2_bresp ;
wire split0_merge2_bvalid ;
wire split0_merge2_bready ;


wire [IDWID-1:0] split0_merge3_arid ;
wire [31:0] split0_merge3_araddr ;
wire [7:0] split0_merge3_arlen ;
wire [EXTRAS-1:0] split0_merge3_arextras ;
wire [1:0] split0_merge3_arburst ;
wire split0_merge3_arvalid ;
wire split0_merge3_arready ;
wire [IDWID-1:0] split0_merge3_rid ;
wire [DWID-1:0] split0_merge3_rdata ;
wire [1:0] split0_merge3_rresp ;
wire split0_merge3_rlast ;
wire split0_merge3_rvalid ;
wire split0_merge3_rready ;

wire [IDWID-1:0] split0_merge3_awid ;
wire [31:0] split0_merge3_awaddr ;
wire [7:0] split0_merge3_awlen ;
wire [EXTRAS-1:0] split0_merge3_awextras ;
wire [1:0] split0_merge3_awburst ;
wire split0_merge3_awvalid ;
wire split0_merge3_awready ;
wire [DWID-1:0] split0_merge3_wdata ;
wire [WSTRB-1:0] split0_merge3_wstrb ;
wire split0_merge3_wlast ;
wire split0_merge3_wvalid ;
wire split0_merge3_wready ;
wire [IDWID-1:0] split0_merge3_bid ;
wire [1:0] split0_merge3_bresp ;
wire split0_merge3_bvalid ;
wire split0_merge3_bready ;


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

    ,.a_araddr(split0_merge0_araddr[31:0])
    ,.a_arburst(split0_merge0_arburst[1:0])
    ,.a_arextras(split0_merge0_arextras[(EXTRAS - 1):0])
    ,.a_arid(split0_merge0_arid[(IDWID - 1):0])
    ,.a_arlen(split0_merge0_arlen[7:0])
    ,.a_arready(split0_merge0_arready)
    ,.a_arvalid(split0_merge0_arvalid)
    ,.a_awaddr(split0_merge0_awaddr[31:0])
    ,.a_awburst(split0_merge0_awburst[1:0])
    ,.a_awextras(split0_merge0_awextras[(EXTRAS - 1):0])
    ,.a_awid(split0_merge0_awid[(IDWID - 1):0])
    ,.a_awlen(split0_merge0_awlen[7:0])
    ,.a_awready(split0_merge0_awready)
    ,.a_awvalid(split0_merge0_awvalid)
    ,.a_bid(split0_merge0_bid[(IDWID - 1):0])
    ,.a_bready(split0_merge0_bready)
    ,.a_bresp(split0_merge0_bresp[1:0])
    ,.a_bvalid(split0_merge0_bvalid)
    ,.a_rdata(split0_merge0_rdata[(DWID - 1):0])
    ,.a_rid(split0_merge0_rid[(IDWID - 1):0])
    ,.a_rlast(split0_merge0_rlast)
    ,.a_rready(split0_merge0_rready)
    ,.a_rresp(split0_merge0_rresp[1:0])
    ,.a_rvalid(split0_merge0_rvalid)
    ,.a_wdata(split0_merge0_wdata[(DWID - 1):0])
    ,.a_wlast(split0_merge0_wlast)
    ,.a_wready(split0_merge0_wready)
    ,.a_wstrb(split0_merge0_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(split0_merge0_wvalid)
    ,.b_araddr(split0_merge1_araddr[31:0])
    ,.b_arburst(split0_merge1_arburst[1:0])
    ,.b_arextras(split0_merge1_arextras[(EXTRAS - 1):0])
    ,.b_arid(split0_merge1_arid[(IDWID - 1):0])
    ,.b_arlen(split0_merge1_arlen[7:0])
    ,.b_arready(split0_merge1_arready)
    ,.b_arvalid(split0_merge1_arvalid)
    ,.b_awaddr(split0_merge1_awaddr[31:0])
    ,.b_awburst(split0_merge1_awburst[1:0])
    ,.b_awextras(split0_merge1_awextras[(EXTRAS - 1):0])
    ,.b_awid(split0_merge1_awid[(IDWID - 1):0])
    ,.b_awlen(split0_merge1_awlen[7:0])
    ,.b_awready(split0_merge1_awready)
    ,.b_awvalid(split0_merge1_awvalid)
    ,.b_bid(split0_merge1_bid[(IDWID - 1):0])
    ,.b_bready(split0_merge1_bready)
    ,.b_bresp(split0_merge1_bresp[1:0])
    ,.b_bvalid(split0_merge1_bvalid)
    ,.b_rdata(split0_merge1_rdata[(DWID - 1):0])
    ,.b_rid(split0_merge1_rid[(IDWID - 1):0])
    ,.b_rlast(split0_merge1_rlast)
    ,.b_rready(split0_merge1_rready)
    ,.b_rresp(split0_merge1_rresp[1:0])
    ,.b_rvalid(split0_merge1_rvalid)
    ,.b_wdata(split0_merge1_wdata[(DWID - 1):0])
    ,.b_wlast(split0_merge1_wlast)
    ,.b_wready(split0_merge1_wready)
    ,.b_wstrb(split0_merge1_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(split0_merge1_wvalid)
    ,.c_araddr(split0_merge2_araddr[31:0])
    ,.c_arburst(split0_merge2_arburst[1:0])
    ,.c_arextras(split0_merge2_arextras[(EXTRAS - 1):0])
    ,.c_arid(split0_merge2_arid[(IDWID - 1):0])
    ,.c_arlen(split0_merge2_arlen[7:0])
    ,.c_arready(split0_merge2_arready)
    ,.c_arvalid(split0_merge2_arvalid)
    ,.c_awaddr(split0_merge2_awaddr[31:0])
    ,.c_awburst(split0_merge2_awburst[1:0])
    ,.c_awextras(split0_merge2_awextras[(EXTRAS - 1):0])
    ,.c_awid(split0_merge2_awid[(IDWID - 1):0])
    ,.c_awlen(split0_merge2_awlen[7:0])
    ,.c_awready(split0_merge2_awready)
    ,.c_awvalid(split0_merge2_awvalid)
    ,.c_bid(split0_merge2_bid[(IDWID - 1):0])
    ,.c_bready(split0_merge2_bready)
    ,.c_bresp(split0_merge2_bresp[1:0])
    ,.c_bvalid(split0_merge2_bvalid)
    ,.c_rdata(split0_merge2_rdata[(DWID - 1):0])
    ,.c_rid(split0_merge2_rid[(IDWID - 1):0])
    ,.c_rlast(split0_merge2_rlast)
    ,.c_rready(split0_merge2_rready)
    ,.c_rresp(split0_merge2_rresp[1:0])
    ,.c_rvalid(split0_merge2_rvalid)
    ,.c_wdata(split0_merge2_wdata[(DWID - 1):0])
    ,.c_wlast(split0_merge2_wlast)
    ,.c_wready(split0_merge2_wready)
    ,.c_wstrb(split0_merge2_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(split0_merge2_wvalid)
    ,.d_araddr(split0_merge3_araddr[31:0])
    ,.d_arburst(split0_merge3_arburst[1:0])
    ,.d_arextras(split0_merge3_arextras[(EXTRAS - 1):0])
    ,.d_arid(split0_merge3_arid[(IDWID - 1):0])
    ,.d_arlen(split0_merge3_arlen[7:0])
    ,.d_arready(split0_merge3_arready)
    ,.d_arvalid(split0_merge3_arvalid)
    ,.d_awaddr(split0_merge3_awaddr[31:0])
    ,.d_awburst(split0_merge3_awburst[1:0])
    ,.d_awextras(split0_merge3_awextras[(EXTRAS - 1):0])
    ,.d_awid(split0_merge3_awid[(IDWID - 1):0])
    ,.d_awlen(split0_merge3_awlen[7:0])
    ,.d_awready(split0_merge3_awready)
    ,.d_awvalid(split0_merge3_awvalid)
    ,.d_bid(split0_merge3_bid[(IDWID - 1):0])
    ,.d_bready(split0_merge3_bready)
    ,.d_bresp(split0_merge3_bresp[1:0])
    ,.d_bvalid(split0_merge3_bvalid)
    ,.d_rdata(split0_merge3_rdata[(DWID - 1):0])
    ,.d_rid(split0_merge3_rid[(IDWID - 1):0])
    ,.d_rlast(split0_merge3_rlast)
    ,.d_rready(split0_merge3_rready)
    ,.d_rresp(split0_merge3_rresp[1:0])
    ,.d_rvalid(split0_merge3_rvalid)
    ,.d_wdata(split0_merge3_wdata[(DWID - 1):0])
    ,.d_wlast(split0_merge3_wlast)
    ,.d_wready(split0_merge3_wready)
    ,.d_wstrb(split0_merge3_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(split0_merge3_wvalid)

);

wire [IDWID-1:0] merge0_split4_arid ;
wire [31:0] merge0_split4_araddr ;
wire [7:0] merge0_split4_arlen ;
wire [EXTRAS-1:0] merge0_split4_arextras ;
wire [1:0] merge0_split4_arburst ;
wire merge0_split4_arvalid ;
wire merge0_split4_arready ;
wire [IDWID-1:0] merge0_split4_rid ;
wire [DWID-1:0] merge0_split4_rdata ;
wire [1:0] merge0_split4_rresp ;
wire merge0_split4_rlast ;
wire merge0_split4_rvalid ;
wire merge0_split4_rready ;

wire [IDWID-1:0] merge0_split4_awid ;
wire [31:0] merge0_split4_awaddr ;
wire [7:0] merge0_split4_awlen ;
wire [EXTRAS-1:0] merge0_split4_awextras ;
wire [1:0] merge0_split4_awburst ;
wire merge0_split4_awvalid ;
wire merge0_split4_awready ;
wire [DWID-1:0] merge0_split4_wdata ;
wire [WSTRB-1:0] merge0_split4_wstrb ;
wire merge0_split4_wlast ;
wire merge0_split4_wvalid ;
wire merge0_split4_wready ;
wire [IDWID-1:0] merge0_split4_bid ;
wire [1:0] merge0_split4_bresp ;
wire merge0_split4_bvalid ;
wire merge0_split4_bready ;


wire [IDWID-1:0] split1_merge0_arid ;
wire [31:0] split1_merge0_araddr ;
wire [7:0] split1_merge0_arlen ;
wire [EXTRAS-1:0] split1_merge0_arextras ;
wire [1:0] split1_merge0_arburst ;
wire split1_merge0_arvalid ;
wire split1_merge0_arready ;
wire [IDWID-1:0] split1_merge0_rid ;
wire [DWID-1:0] split1_merge0_rdata ;
wire [1:0] split1_merge0_rresp ;
wire split1_merge0_rlast ;
wire split1_merge0_rvalid ;
wire split1_merge0_rready ;

wire [IDWID-1:0] split1_merge0_awid ;
wire [31:0] split1_merge0_awaddr ;
wire [7:0] split1_merge0_awlen ;
wire [EXTRAS-1:0] split1_merge0_awextras ;
wire [1:0] split1_merge0_awburst ;
wire split1_merge0_awvalid ;
wire split1_merge0_awready ;
wire [DWID-1:0] split1_merge0_wdata ;
wire [WSTRB-1:0] split1_merge0_wstrb ;
wire split1_merge0_wlast ;
wire split1_merge0_wvalid ;
wire split1_merge0_wready ;
wire [IDWID-1:0] split1_merge0_bid ;
wire [1:0] split1_merge0_bresp ;
wire split1_merge0_bvalid ;
wire split1_merge0_bready ;


wire [IDWID-1:0] split2_merge0_arid ;
wire [31:0] split2_merge0_araddr ;
wire [7:0] split2_merge0_arlen ;
wire [EXTRAS-1:0] split2_merge0_arextras ;
wire [1:0] split2_merge0_arburst ;
wire split2_merge0_arvalid ;
wire split2_merge0_arready ;
wire [IDWID-1:0] split2_merge0_rid ;
wire [DWID-1:0] split2_merge0_rdata ;
wire [1:0] split2_merge0_rresp ;
wire split2_merge0_rlast ;
wire split2_merge0_rvalid ;
wire split2_merge0_rready ;

wire [IDWID-1:0] split2_merge0_awid ;
wire [31:0] split2_merge0_awaddr ;
wire [7:0] split2_merge0_awlen ;
wire [EXTRAS-1:0] split2_merge0_awextras ;
wire [1:0] split2_merge0_awburst ;
wire split2_merge0_awvalid ;
wire split2_merge0_awready ;
wire [DWID-1:0] split2_merge0_wdata ;
wire [WSTRB-1:0] split2_merge0_wstrb ;
wire split2_merge0_wlast ;
wire split2_merge0_wvalid ;
wire split2_merge0_wready ;
wire [IDWID-1:0] split2_merge0_bid ;
wire [1:0] split2_merge0_bresp ;
wire split2_merge0_bvalid ;
wire split2_merge0_bready ;


wire [IDWID-1:0] split3_merge0_arid ;
wire [31:0] split3_merge0_araddr ;
wire [7:0] split3_merge0_arlen ;
wire [EXTRAS-1:0] split3_merge0_arextras ;
wire [1:0] split3_merge0_arburst ;
wire split3_merge0_arvalid ;
wire split3_merge0_arready ;
wire [IDWID-1:0] split3_merge0_rid ;
wire [DWID-1:0] split3_merge0_rdata ;
wire [1:0] split3_merge0_rresp ;
wire split3_merge0_rlast ;
wire split3_merge0_rvalid ;
wire split3_merge0_rready ;

wire [IDWID-1:0] split3_merge0_awid ;
wire [31:0] split3_merge0_awaddr ;
wire [7:0] split3_merge0_awlen ;
wire [EXTRAS-1:0] split3_merge0_awextras ;
wire [1:0] split3_merge0_awburst ;
wire split3_merge0_awvalid ;
wire split3_merge0_awready ;
wire [DWID-1:0] split3_merge0_wdata ;
wire [WSTRB-1:0] split3_merge0_wstrb ;
wire split3_merge0_wlast ;
wire split3_merge0_wvalid ;
wire split3_merge0_wready ;
wire [IDWID-1:0] split3_merge0_bid ;
wire [1:0] split3_merge0_bresp ;
wire split3_merge0_bvalid ;
wire split3_merge0_bready ;


axi_4_merger merge0 (
     .clk(clk),.rst_n(rst_n)
    ,.araddr(merge0_split4_araddr[31:0])
    ,.arburst(merge0_split4_arburst[1:0])
    ,.arextras(merge0_split4_arextras[(EXTRAS - 1):0])
    ,.arid(merge0_split4_arid[(IDWID - 1):0])
    ,.arlen(merge0_split4_arlen[7:0])
    ,.arready(merge0_split4_arready)
    ,.arvalid(merge0_split4_arvalid)
    ,.awaddr(merge0_split4_awaddr[31:0])
    ,.awburst(merge0_split4_awburst[1:0])
    ,.awextras(merge0_split4_awextras[(EXTRAS - 1):0])
    ,.awid(merge0_split4_awid[3:0])
    ,.awlen(merge0_split4_awlen[7:0])
    ,.awready(merge0_split4_awready)
    ,.awvalid(merge0_split4_awvalid)
    ,.bid(merge0_split4_bid[(IDWID - 1):0])
    ,.bready(merge0_split4_bready)
    ,.bresp(merge0_split4_bresp[1:0])
    ,.bvalid(merge0_split4_bvalid)
    ,.rid(merge0_split4_rid[(IDWID - 1):0])
    ,.rlast(merge0_split4_rlast)
    ,.rready(merge0_split4_rready)
    ,.rresp(merge0_split4_rresp[1:0])
    ,.rvalid(merge0_split4_rvalid)
    ,.rdata(merge0_split4_rdata[(DWID - 1):0])
    ,.wdata(merge0_split4_wdata[(DWID - 1):0])
    ,.wlast(merge0_split4_wlast)
    ,.wready(merge0_split4_wready)
    ,.wstrb(merge0_split4_wstrb[(WSTRB - 1):0])
    ,.wvalid(merge0_split4_wvalid)


    ,.a_araddr(split0_merge0_araddr[31:0])
    ,.a_arburst(split0_merge0_arburst[1:0])
    ,.a_arextras(split0_merge0_arextras[(EXTRAS - 1):0])
    ,.a_arid(split0_merge0_arid[(IDWID - 1):0])
    ,.a_arlen(split0_merge0_arlen[7:0])
    ,.a_arready(split0_merge0_arready)
    ,.a_arvalid(split0_merge0_arvalid)
    ,.a_awaddr(split0_merge0_awaddr[31:0])
    ,.a_awburst(split0_merge0_awburst[1:0])
    ,.a_awextras(split0_merge0_awextras[(EXTRAS - 1):0])
    ,.a_awid(split0_merge0_awid[(IDWID - 1):0])
    ,.a_awlen(split0_merge0_awlen[7:0])
    ,.a_awready(split0_merge0_awready)
    ,.a_awvalid(split0_merge0_awvalid)
    ,.a_bid(split0_merge0_bid[(IDWID - 1):0])
    ,.a_bready(split0_merge0_bready)
    ,.a_bresp(split0_merge0_bresp[1:0])
    ,.a_bvalid(split0_merge0_bvalid)
    ,.a_rdata(split0_merge0_rdata[(DWID - 1):0])
    ,.a_rid(split0_merge0_rid[(IDWID - 1):0])
    ,.a_rlast(split0_merge0_rlast)
    ,.a_rready(split0_merge0_rready)
    ,.a_rresp(split0_merge0_rresp[1:0])
    ,.a_rvalid(split0_merge0_rvalid)
    ,.a_wdata(split0_merge0_wdata[(DWID - 1):0])
    ,.a_wlast(split0_merge0_wlast)
    ,.a_wready(split0_merge0_wready)
    ,.a_wstrb(split0_merge0_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(split0_merge0_wvalid)

    ,.b_araddr(split1_merge0_araddr[31:0])
    ,.b_arburst(split1_merge0_arburst[1:0])
    ,.b_arextras(split1_merge0_arextras[(EXTRAS - 1):0])
    ,.b_arid(split1_merge0_arid[(IDWID - 1):0])
    ,.b_arlen(split1_merge0_arlen[7:0])
    ,.b_arready(split1_merge0_arready)
    ,.b_arvalid(split1_merge0_arvalid)
    ,.b_awaddr(split1_merge0_awaddr[31:0])
    ,.b_awburst(split1_merge0_awburst[1:0])
    ,.b_awextras(split1_merge0_awextras[(EXTRAS - 1):0])
    ,.b_awid(split1_merge0_awid[(IDWID - 1):0])
    ,.b_awlen(split1_merge0_awlen[7:0])
    ,.b_awready(split1_merge0_awready)
    ,.b_awvalid(split1_merge0_awvalid)
    ,.b_bid(split1_merge0_bid[(IDWID - 1):0])
    ,.b_bready(split1_merge0_bready)
    ,.b_bresp(split1_merge0_bresp[1:0])
    ,.b_bvalid(split1_merge0_bvalid)
    ,.b_rdata(split1_merge0_rdata[(DWID - 1):0])
    ,.b_rid(split1_merge0_rid[(IDWID - 1):0])
    ,.b_rlast(split1_merge0_rlast)
    ,.b_rready(split1_merge0_rready)
    ,.b_rresp(split1_merge0_rresp[1:0])
    ,.b_rvalid(split1_merge0_rvalid)
    ,.b_wdata(split1_merge0_wdata[(DWID - 1):0])
    ,.b_wlast(split1_merge0_wlast)
    ,.b_wready(split1_merge0_wready)
    ,.b_wstrb(split1_merge0_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(split1_merge0_wvalid)

    ,.c_araddr(split2_merge0_araddr[31:0])
    ,.c_arburst(split2_merge0_arburst[1:0])
    ,.c_arextras(split2_merge0_arextras[(EXTRAS - 1):0])
    ,.c_arid(split2_merge0_arid[(IDWID - 1):0])
    ,.c_arlen(split2_merge0_arlen[7:0])
    ,.c_arready(split2_merge0_arready)
    ,.c_arvalid(split2_merge0_arvalid)
    ,.c_awaddr(split2_merge0_awaddr[31:0])
    ,.c_awburst(split2_merge0_awburst[1:0])
    ,.c_awextras(split2_merge0_awextras[(EXTRAS - 1):0])
    ,.c_awid(split2_merge0_awid[(IDWID - 1):0])
    ,.c_awlen(split2_merge0_awlen[7:0])
    ,.c_awready(split2_merge0_awready)
    ,.c_awvalid(split2_merge0_awvalid)
    ,.c_bid(split2_merge0_bid[(IDWID - 1):0])
    ,.c_bready(split2_merge0_bready)
    ,.c_bresp(split2_merge0_bresp[1:0])
    ,.c_bvalid(split2_merge0_bvalid)
    ,.c_rdata(split2_merge0_rdata[(DWID - 1):0])
    ,.c_rid(split2_merge0_rid[(IDWID - 1):0])
    ,.c_rlast(split2_merge0_rlast)
    ,.c_rready(split2_merge0_rready)
    ,.c_rresp(split2_merge0_rresp[1:0])
    ,.c_rvalid(split2_merge0_rvalid)
    ,.c_wdata(split2_merge0_wdata[(DWID - 1):0])
    ,.c_wlast(split2_merge0_wlast)
    ,.c_wready(split2_merge0_wready)
    ,.c_wstrb(split2_merge0_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(split2_merge0_wvalid)

    ,.d_araddr(split3_merge0_araddr[31:0])
    ,.d_arburst(split3_merge0_arburst[1:0])
    ,.d_arextras(split3_merge0_arextras[(EXTRAS - 1):0])
    ,.d_arid(split3_merge0_arid[(IDWID - 1):0])
    ,.d_arlen(split3_merge0_arlen[7:0])
    ,.d_arready(split3_merge0_arready)
    ,.d_arvalid(split3_merge0_arvalid)
    ,.d_awaddr(split3_merge0_awaddr[31:0])
    ,.d_awburst(split3_merge0_awburst[1:0])
    ,.d_awextras(split3_merge0_awextras[(EXTRAS - 1):0])
    ,.d_awid(split3_merge0_awid[(IDWID - 1):0])
    ,.d_awlen(split3_merge0_awlen[7:0])
    ,.d_awready(split3_merge0_awready)
    ,.d_awvalid(split3_merge0_awvalid)
    ,.d_bid(split3_merge0_bid[(IDWID - 1):0])
    ,.d_bready(split3_merge0_bready)
    ,.d_bresp(split3_merge0_bresp[1:0])
    ,.d_bvalid(split3_merge0_bvalid)
    ,.d_rdata(split3_merge0_rdata[(DWID - 1):0])
    ,.d_rid(split3_merge0_rid[(IDWID - 1):0])
    ,.d_rlast(split3_merge0_rlast)
    ,.d_rready(split3_merge0_rready)
    ,.d_rresp(split3_merge0_rresp[1:0])
    ,.d_rvalid(split3_merge0_rvalid)
    ,.d_wdata(split3_merge0_wdata[(DWID - 1):0])
    ,.d_wlast(split3_merge0_wlast)
    ,.d_wready(split3_merge0_wready)
    ,.d_wstrb(split3_merge0_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(split3_merge0_wvalid)
);


wire [IDWID-1:0] merge1_split5_arid ;
wire [31:0] merge1_split5_araddr ;
wire [7:0] merge1_split5_arlen ;
wire [EXTRAS-1:0] merge1_split5_arextras ;
wire [1:0] merge1_split5_arburst ;
wire merge1_split5_arvalid ;
wire merge1_split5_arready ;
wire [IDWID-1:0] merge1_split5_rid ;
wire [DWID-1:0] merge1_split5_rdata ;
wire [1:0] merge1_split5_rresp ;
wire merge1_split5_rlast ;
wire merge1_split5_rvalid ;
wire merge1_split5_rready ;

wire [IDWID-1:0] merge1_split5_awid ;
wire [31:0] merge1_split5_awaddr ;
wire [7:0] merge1_split5_awlen ;
wire [EXTRAS-1:0] merge1_split5_awextras ;
wire [1:0] merge1_split5_awburst ;
wire merge1_split5_awvalid ;
wire merge1_split5_awready ;
wire [DWID-1:0] merge1_split5_wdata ;
wire [WSTRB-1:0] merge1_split5_wstrb ;
wire merge1_split5_wlast ;
wire merge1_split5_wvalid ;
wire merge1_split5_wready ;
wire [IDWID-1:0] merge1_split5_bid ;
wire [1:0] merge1_split5_bresp ;
wire merge1_split5_bvalid ;
wire merge1_split5_bready ;


wire [IDWID-1:0] split1_merge1_arid ;
wire [31:0] split1_merge1_araddr ;
wire [7:0] split1_merge1_arlen ;
wire [EXTRAS-1:0] split1_merge1_arextras ;
wire [1:0] split1_merge1_arburst ;
wire split1_merge1_arvalid ;
wire split1_merge1_arready ;
wire [IDWID-1:0] split1_merge1_rid ;
wire [DWID-1:0] split1_merge1_rdata ;
wire [1:0] split1_merge1_rresp ;
wire split1_merge1_rlast ;
wire split1_merge1_rvalid ;
wire split1_merge1_rready ;

wire [IDWID-1:0] split1_merge1_awid ;
wire [31:0] split1_merge1_awaddr ;
wire [7:0] split1_merge1_awlen ;
wire [EXTRAS-1:0] split1_merge1_awextras ;
wire [1:0] split1_merge1_awburst ;
wire split1_merge1_awvalid ;
wire split1_merge1_awready ;
wire [DWID-1:0] split1_merge1_wdata ;
wire [WSTRB-1:0] split1_merge1_wstrb ;
wire split1_merge1_wlast ;
wire split1_merge1_wvalid ;
wire split1_merge1_wready ;
wire [IDWID-1:0] split1_merge1_bid ;
wire [1:0] split1_merge1_bresp ;
wire split1_merge1_bvalid ;
wire split1_merge1_bready ;


wire [IDWID-1:0] split2_merge1_arid ;
wire [31:0] split2_merge1_araddr ;
wire [7:0] split2_merge1_arlen ;
wire [EXTRAS-1:0] split2_merge1_arextras ;
wire [1:0] split2_merge1_arburst ;
wire split2_merge1_arvalid ;
wire split2_merge1_arready ;
wire [IDWID-1:0] split2_merge1_rid ;
wire [DWID-1:0] split2_merge1_rdata ;
wire [1:0] split2_merge1_rresp ;
wire split2_merge1_rlast ;
wire split2_merge1_rvalid ;
wire split2_merge1_rready ;

wire [IDWID-1:0] split2_merge1_awid ;
wire [31:0] split2_merge1_awaddr ;
wire [7:0] split2_merge1_awlen ;
wire [EXTRAS-1:0] split2_merge1_awextras ;
wire [1:0] split2_merge1_awburst ;
wire split2_merge1_awvalid ;
wire split2_merge1_awready ;
wire [DWID-1:0] split2_merge1_wdata ;
wire [WSTRB-1:0] split2_merge1_wstrb ;
wire split2_merge1_wlast ;
wire split2_merge1_wvalid ;
wire split2_merge1_wready ;
wire [IDWID-1:0] split2_merge1_bid ;
wire [1:0] split2_merge1_bresp ;
wire split2_merge1_bvalid ;
wire split2_merge1_bready ;


wire [IDWID-1:0] split3_merge1_arid ;
wire [31:0] split3_merge1_araddr ;
wire [7:0] split3_merge1_arlen ;
wire [EXTRAS-1:0] split3_merge1_arextras ;
wire [1:0] split3_merge1_arburst ;
wire split3_merge1_arvalid ;
wire split3_merge1_arready ;
wire [IDWID-1:0] split3_merge1_rid ;
wire [DWID-1:0] split3_merge1_rdata ;
wire [1:0] split3_merge1_rresp ;
wire split3_merge1_rlast ;
wire split3_merge1_rvalid ;
wire split3_merge1_rready ;

wire [IDWID-1:0] split3_merge1_awid ;
wire [31:0] split3_merge1_awaddr ;
wire [7:0] split3_merge1_awlen ;
wire [EXTRAS-1:0] split3_merge1_awextras ;
wire [1:0] split3_merge1_awburst ;
wire split3_merge1_awvalid ;
wire split3_merge1_awready ;
wire [DWID-1:0] split3_merge1_wdata ;
wire [WSTRB-1:0] split3_merge1_wstrb ;
wire split3_merge1_wlast ;
wire split3_merge1_wvalid ;
wire split3_merge1_wready ;
wire [IDWID-1:0] split3_merge1_bid ;
wire [1:0] split3_merge1_bresp ;
wire split3_merge1_bvalid ;
wire split3_merge1_bready ;


axi_4_merger merge1 (
     .clk(clk),.rst_n(rst_n)
    ,.araddr(merge1_split5_araddr[31:0])
    ,.arburst(merge1_split5_arburst[1:0])
    ,.arextras(merge1_split5_arextras[(EXTRAS - 1):0])
    ,.arid(merge1_split5_arid[(IDWID - 1):0])
    ,.arlen(merge1_split5_arlen[7:0])
    ,.arready(merge1_split5_arready)
    ,.arvalid(merge1_split5_arvalid)
    ,.awaddr(merge1_split5_awaddr[31:0])
    ,.awburst(merge1_split5_awburst[1:0])
    ,.awextras(merge1_split5_awextras[(EXTRAS - 1):0])
    ,.awid(merge1_split5_awid[3:0])
    ,.awlen(merge1_split5_awlen[7:0])
    ,.awready(merge1_split5_awready)
    ,.awvalid(merge1_split5_awvalid)
    ,.bid(merge1_split5_bid[(IDWID - 1):0])
    ,.bready(merge1_split5_bready)
    ,.bresp(merge1_split5_bresp[1:0])
    ,.bvalid(merge1_split5_bvalid)
    ,.rid(merge1_split5_rid[(IDWID - 1):0])
    ,.rlast(merge1_split5_rlast)
    ,.rready(merge1_split5_rready)
    ,.rresp(merge1_split5_rresp[1:0])
    ,.rvalid(merge1_split5_rvalid)
    ,.rdata(merge1_split5_rdata[(DWID - 1):0])
    ,.wdata(merge1_split5_wdata[(DWID - 1):0])
    ,.wlast(merge1_split5_wlast)
    ,.wready(merge1_split5_wready)
    ,.wstrb(merge1_split5_wstrb[(WSTRB - 1):0])
    ,.wvalid(merge1_split5_wvalid)


    ,.a_araddr(split0_merge1_araddr[31:0])
    ,.a_arburst(split0_merge1_arburst[1:0])
    ,.a_arextras(split0_merge1_arextras[(EXTRAS - 1):0])
    ,.a_arid(split0_merge1_arid[(IDWID - 1):0])
    ,.a_arlen(split0_merge1_arlen[7:0])
    ,.a_arready(split0_merge1_arready)
    ,.a_arvalid(split0_merge1_arvalid)
    ,.a_awaddr(split0_merge1_awaddr[31:0])
    ,.a_awburst(split0_merge1_awburst[1:0])
    ,.a_awextras(split0_merge1_awextras[(EXTRAS - 1):0])
    ,.a_awid(split0_merge1_awid[(IDWID - 1):0])
    ,.a_awlen(split0_merge1_awlen[7:0])
    ,.a_awready(split0_merge1_awready)
    ,.a_awvalid(split0_merge1_awvalid)
    ,.a_bid(split0_merge1_bid[(IDWID - 1):0])
    ,.a_bready(split0_merge1_bready)
    ,.a_bresp(split0_merge1_bresp[1:0])
    ,.a_bvalid(split0_merge1_bvalid)
    ,.a_rdata(split0_merge1_rdata[(DWID - 1):0])
    ,.a_rid(split0_merge1_rid[(IDWID - 1):0])
    ,.a_rlast(split0_merge1_rlast)
    ,.a_rready(split0_merge1_rready)
    ,.a_rresp(split0_merge1_rresp[1:0])
    ,.a_rvalid(split0_merge1_rvalid)
    ,.a_wdata(split0_merge1_wdata[(DWID - 1):0])
    ,.a_wlast(split0_merge1_wlast)
    ,.a_wready(split0_merge1_wready)
    ,.a_wstrb(split0_merge1_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(split0_merge1_wvalid)

    ,.b_araddr(split1_merge1_araddr[31:0])
    ,.b_arburst(split1_merge1_arburst[1:0])
    ,.b_arextras(split1_merge1_arextras[(EXTRAS - 1):0])
    ,.b_arid(split1_merge1_arid[(IDWID - 1):0])
    ,.b_arlen(split1_merge1_arlen[7:0])
    ,.b_arready(split1_merge1_arready)
    ,.b_arvalid(split1_merge1_arvalid)
    ,.b_awaddr(split1_merge1_awaddr[31:0])
    ,.b_awburst(split1_merge1_awburst[1:0])
    ,.b_awextras(split1_merge1_awextras[(EXTRAS - 1):0])
    ,.b_awid(split1_merge1_awid[(IDWID - 1):0])
    ,.b_awlen(split1_merge1_awlen[7:0])
    ,.b_awready(split1_merge1_awready)
    ,.b_awvalid(split1_merge1_awvalid)
    ,.b_bid(split1_merge1_bid[(IDWID - 1):0])
    ,.b_bready(split1_merge1_bready)
    ,.b_bresp(split1_merge1_bresp[1:0])
    ,.b_bvalid(split1_merge1_bvalid)
    ,.b_rdata(split1_merge1_rdata[(DWID - 1):0])
    ,.b_rid(split1_merge1_rid[(IDWID - 1):0])
    ,.b_rlast(split1_merge1_rlast)
    ,.b_rready(split1_merge1_rready)
    ,.b_rresp(split1_merge1_rresp[1:0])
    ,.b_rvalid(split1_merge1_rvalid)
    ,.b_wdata(split1_merge1_wdata[(DWID - 1):0])
    ,.b_wlast(split1_merge1_wlast)
    ,.b_wready(split1_merge1_wready)
    ,.b_wstrb(split1_merge1_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(split1_merge1_wvalid)

    ,.c_araddr(split2_merge1_araddr[31:0])
    ,.c_arburst(split2_merge1_arburst[1:0])
    ,.c_arextras(split2_merge1_arextras[(EXTRAS - 1):0])
    ,.c_arid(split2_merge1_arid[(IDWID - 1):0])
    ,.c_arlen(split2_merge1_arlen[7:0])
    ,.c_arready(split2_merge1_arready)
    ,.c_arvalid(split2_merge1_arvalid)
    ,.c_awaddr(split2_merge1_awaddr[31:0])
    ,.c_awburst(split2_merge1_awburst[1:0])
    ,.c_awextras(split2_merge1_awextras[(EXTRAS - 1):0])
    ,.c_awid(split2_merge1_awid[(IDWID - 1):0])
    ,.c_awlen(split2_merge1_awlen[7:0])
    ,.c_awready(split2_merge1_awready)
    ,.c_awvalid(split2_merge1_awvalid)
    ,.c_bid(split2_merge1_bid[(IDWID - 1):0])
    ,.c_bready(split2_merge1_bready)
    ,.c_bresp(split2_merge1_bresp[1:0])
    ,.c_bvalid(split2_merge1_bvalid)
    ,.c_rdata(split2_merge1_rdata[(DWID - 1):0])
    ,.c_rid(split2_merge1_rid[(IDWID - 1):0])
    ,.c_rlast(split2_merge1_rlast)
    ,.c_rready(split2_merge1_rready)
    ,.c_rresp(split2_merge1_rresp[1:0])
    ,.c_rvalid(split2_merge1_rvalid)
    ,.c_wdata(split2_merge1_wdata[(DWID - 1):0])
    ,.c_wlast(split2_merge1_wlast)
    ,.c_wready(split2_merge1_wready)
    ,.c_wstrb(split2_merge1_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(split2_merge1_wvalid)

    ,.d_araddr(split3_merge1_araddr[31:0])
    ,.d_arburst(split3_merge1_arburst[1:0])
    ,.d_arextras(split3_merge1_arextras[(EXTRAS - 1):0])
    ,.d_arid(split3_merge1_arid[(IDWID - 1):0])
    ,.d_arlen(split3_merge1_arlen[7:0])
    ,.d_arready(split3_merge1_arready)
    ,.d_arvalid(split3_merge1_arvalid)
    ,.d_awaddr(split3_merge1_awaddr[31:0])
    ,.d_awburst(split3_merge1_awburst[1:0])
    ,.d_awextras(split3_merge1_awextras[(EXTRAS - 1):0])
    ,.d_awid(split3_merge1_awid[(IDWID - 1):0])
    ,.d_awlen(split3_merge1_awlen[7:0])
    ,.d_awready(split3_merge1_awready)
    ,.d_awvalid(split3_merge1_awvalid)
    ,.d_bid(split3_merge1_bid[(IDWID - 1):0])
    ,.d_bready(split3_merge1_bready)
    ,.d_bresp(split3_merge1_bresp[1:0])
    ,.d_bvalid(split3_merge1_bvalid)
    ,.d_rdata(split3_merge1_rdata[(DWID - 1):0])
    ,.d_rid(split3_merge1_rid[(IDWID - 1):0])
    ,.d_rlast(split3_merge1_rlast)
    ,.d_rready(split3_merge1_rready)
    ,.d_rresp(split3_merge1_rresp[1:0])
    ,.d_rvalid(split3_merge1_rvalid)
    ,.d_wdata(split3_merge1_wdata[(DWID - 1):0])
    ,.d_wlast(split3_merge1_wlast)
    ,.d_wready(split3_merge1_wready)
    ,.d_wstrb(split3_merge1_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(split3_merge1_wvalid)
);


wire [IDWID-1:0] merge2_split6_arid ;
wire [31:0] merge2_split6_araddr ;
wire [7:0] merge2_split6_arlen ;
wire [EXTRAS-1:0] merge2_split6_arextras ;
wire [1:0] merge2_split6_arburst ;
wire merge2_split6_arvalid ;
wire merge2_split6_arready ;
wire [IDWID-1:0] merge2_split6_rid ;
wire [DWID-1:0] merge2_split6_rdata ;
wire [1:0] merge2_split6_rresp ;
wire merge2_split6_rlast ;
wire merge2_split6_rvalid ;
wire merge2_split6_rready ;

wire [IDWID-1:0] merge2_split6_awid ;
wire [31:0] merge2_split6_awaddr ;
wire [7:0] merge2_split6_awlen ;
wire [EXTRAS-1:0] merge2_split6_awextras ;
wire [1:0] merge2_split6_awburst ;
wire merge2_split6_awvalid ;
wire merge2_split6_awready ;
wire [DWID-1:0] merge2_split6_wdata ;
wire [WSTRB-1:0] merge2_split6_wstrb ;
wire merge2_split6_wlast ;
wire merge2_split6_wvalid ;
wire merge2_split6_wready ;
wire [IDWID-1:0] merge2_split6_bid ;
wire [1:0] merge2_split6_bresp ;
wire merge2_split6_bvalid ;
wire merge2_split6_bready ;


wire [IDWID-1:0] split1_merge2_arid ;
wire [31:0] split1_merge2_araddr ;
wire [7:0] split1_merge2_arlen ;
wire [EXTRAS-1:0] split1_merge2_arextras ;
wire [1:0] split1_merge2_arburst ;
wire split1_merge2_arvalid ;
wire split1_merge2_arready ;
wire [IDWID-1:0] split1_merge2_rid ;
wire [DWID-1:0] split1_merge2_rdata ;
wire [1:0] split1_merge2_rresp ;
wire split1_merge2_rlast ;
wire split1_merge2_rvalid ;
wire split1_merge2_rready ;

wire [IDWID-1:0] split1_merge2_awid ;
wire [31:0] split1_merge2_awaddr ;
wire [7:0] split1_merge2_awlen ;
wire [EXTRAS-1:0] split1_merge2_awextras ;
wire [1:0] split1_merge2_awburst ;
wire split1_merge2_awvalid ;
wire split1_merge2_awready ;
wire [DWID-1:0] split1_merge2_wdata ;
wire [WSTRB-1:0] split1_merge2_wstrb ;
wire split1_merge2_wlast ;
wire split1_merge2_wvalid ;
wire split1_merge2_wready ;
wire [IDWID-1:0] split1_merge2_bid ;
wire [1:0] split1_merge2_bresp ;
wire split1_merge2_bvalid ;
wire split1_merge2_bready ;


wire [IDWID-1:0] split2_merge2_arid ;
wire [31:0] split2_merge2_araddr ;
wire [7:0] split2_merge2_arlen ;
wire [EXTRAS-1:0] split2_merge2_arextras ;
wire [1:0] split2_merge2_arburst ;
wire split2_merge2_arvalid ;
wire split2_merge2_arready ;
wire [IDWID-1:0] split2_merge2_rid ;
wire [DWID-1:0] split2_merge2_rdata ;
wire [1:0] split2_merge2_rresp ;
wire split2_merge2_rlast ;
wire split2_merge2_rvalid ;
wire split2_merge2_rready ;

wire [IDWID-1:0] split2_merge2_awid ;
wire [31:0] split2_merge2_awaddr ;
wire [7:0] split2_merge2_awlen ;
wire [EXTRAS-1:0] split2_merge2_awextras ;
wire [1:0] split2_merge2_awburst ;
wire split2_merge2_awvalid ;
wire split2_merge2_awready ;
wire [DWID-1:0] split2_merge2_wdata ;
wire [WSTRB-1:0] split2_merge2_wstrb ;
wire split2_merge2_wlast ;
wire split2_merge2_wvalid ;
wire split2_merge2_wready ;
wire [IDWID-1:0] split2_merge2_bid ;
wire [1:0] split2_merge2_bresp ;
wire split2_merge2_bvalid ;
wire split2_merge2_bready ;


wire [IDWID-1:0] split3_merge2_arid ;
wire [31:0] split3_merge2_araddr ;
wire [7:0] split3_merge2_arlen ;
wire [EXTRAS-1:0] split3_merge2_arextras ;
wire [1:0] split3_merge2_arburst ;
wire split3_merge2_arvalid ;
wire split3_merge2_arready ;
wire [IDWID-1:0] split3_merge2_rid ;
wire [DWID-1:0] split3_merge2_rdata ;
wire [1:0] split3_merge2_rresp ;
wire split3_merge2_rlast ;
wire split3_merge2_rvalid ;
wire split3_merge2_rready ;

wire [IDWID-1:0] split3_merge2_awid ;
wire [31:0] split3_merge2_awaddr ;
wire [7:0] split3_merge2_awlen ;
wire [EXTRAS-1:0] split3_merge2_awextras ;
wire [1:0] split3_merge2_awburst ;
wire split3_merge2_awvalid ;
wire split3_merge2_awready ;
wire [DWID-1:0] split3_merge2_wdata ;
wire [WSTRB-1:0] split3_merge2_wstrb ;
wire split3_merge2_wlast ;
wire split3_merge2_wvalid ;
wire split3_merge2_wready ;
wire [IDWID-1:0] split3_merge2_bid ;
wire [1:0] split3_merge2_bresp ;
wire split3_merge2_bvalid ;
wire split3_merge2_bready ;


axi_4_merger merge2 (
     .clk(clk),.rst_n(rst_n)
    ,.araddr(merge2_split6_araddr[31:0])
    ,.arburst(merge2_split6_arburst[1:0])
    ,.arextras(merge2_split6_arextras[(EXTRAS - 1):0])
    ,.arid(merge2_split6_arid[(IDWID - 1):0])
    ,.arlen(merge2_split6_arlen[7:0])
    ,.arready(merge2_split6_arready)
    ,.arvalid(merge2_split6_arvalid)
    ,.awaddr(merge2_split6_awaddr[31:0])
    ,.awburst(merge2_split6_awburst[1:0])
    ,.awextras(merge2_split6_awextras[(EXTRAS - 1):0])
    ,.awid(merge2_split6_awid[3:0])
    ,.awlen(merge2_split6_awlen[7:0])
    ,.awready(merge2_split6_awready)
    ,.awvalid(merge2_split6_awvalid)
    ,.bid(merge2_split6_bid[(IDWID - 1):0])
    ,.bready(merge2_split6_bready)
    ,.bresp(merge2_split6_bresp[1:0])
    ,.bvalid(merge2_split6_bvalid)
    ,.rid(merge2_split6_rid[(IDWID - 1):0])
    ,.rlast(merge2_split6_rlast)
    ,.rready(merge2_split6_rready)
    ,.rresp(merge2_split6_rresp[1:0])
    ,.rvalid(merge2_split6_rvalid)
    ,.rdata(merge2_split6_rdata[(DWID - 1):0])
    ,.wdata(merge2_split6_wdata[(DWID - 1):0])
    ,.wlast(merge2_split6_wlast)
    ,.wready(merge2_split6_wready)
    ,.wstrb(merge2_split6_wstrb[(WSTRB - 1):0])
    ,.wvalid(merge2_split6_wvalid)


    ,.a_araddr(split0_merge2_araddr[31:0])
    ,.a_arburst(split0_merge2_arburst[1:0])
    ,.a_arextras(split0_merge2_arextras[(EXTRAS - 1):0])
    ,.a_arid(split0_merge2_arid[(IDWID - 1):0])
    ,.a_arlen(split0_merge2_arlen[7:0])
    ,.a_arready(split0_merge2_arready)
    ,.a_arvalid(split0_merge2_arvalid)
    ,.a_awaddr(split0_merge2_awaddr[31:0])
    ,.a_awburst(split0_merge2_awburst[1:0])
    ,.a_awextras(split0_merge2_awextras[(EXTRAS - 1):0])
    ,.a_awid(split0_merge2_awid[(IDWID - 1):0])
    ,.a_awlen(split0_merge2_awlen[7:0])
    ,.a_awready(split0_merge2_awready)
    ,.a_awvalid(split0_merge2_awvalid)
    ,.a_bid(split0_merge2_bid[(IDWID - 1):0])
    ,.a_bready(split0_merge2_bready)
    ,.a_bresp(split0_merge2_bresp[1:0])
    ,.a_bvalid(split0_merge2_bvalid)
    ,.a_rdata(split0_merge2_rdata[(DWID - 1):0])
    ,.a_rid(split0_merge2_rid[(IDWID - 1):0])
    ,.a_rlast(split0_merge2_rlast)
    ,.a_rready(split0_merge2_rready)
    ,.a_rresp(split0_merge2_rresp[1:0])
    ,.a_rvalid(split0_merge2_rvalid)
    ,.a_wdata(split0_merge2_wdata[(DWID - 1):0])
    ,.a_wlast(split0_merge2_wlast)
    ,.a_wready(split0_merge2_wready)
    ,.a_wstrb(split0_merge2_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(split0_merge2_wvalid)

    ,.b_araddr(split1_merge2_araddr[31:0])
    ,.b_arburst(split1_merge2_arburst[1:0])
    ,.b_arextras(split1_merge2_arextras[(EXTRAS - 1):0])
    ,.b_arid(split1_merge2_arid[(IDWID - 1):0])
    ,.b_arlen(split1_merge2_arlen[7:0])
    ,.b_arready(split1_merge2_arready)
    ,.b_arvalid(split1_merge2_arvalid)
    ,.b_awaddr(split1_merge2_awaddr[31:0])
    ,.b_awburst(split1_merge2_awburst[1:0])
    ,.b_awextras(split1_merge2_awextras[(EXTRAS - 1):0])
    ,.b_awid(split1_merge2_awid[(IDWID - 1):0])
    ,.b_awlen(split1_merge2_awlen[7:0])
    ,.b_awready(split1_merge2_awready)
    ,.b_awvalid(split1_merge2_awvalid)
    ,.b_bid(split1_merge2_bid[(IDWID - 1):0])
    ,.b_bready(split1_merge2_bready)
    ,.b_bresp(split1_merge2_bresp[1:0])
    ,.b_bvalid(split1_merge2_bvalid)
    ,.b_rdata(split1_merge2_rdata[(DWID - 1):0])
    ,.b_rid(split1_merge2_rid[(IDWID - 1):0])
    ,.b_rlast(split1_merge2_rlast)
    ,.b_rready(split1_merge2_rready)
    ,.b_rresp(split1_merge2_rresp[1:0])
    ,.b_rvalid(split1_merge2_rvalid)
    ,.b_wdata(split1_merge2_wdata[(DWID - 1):0])
    ,.b_wlast(split1_merge2_wlast)
    ,.b_wready(split1_merge2_wready)
    ,.b_wstrb(split1_merge2_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(split1_merge2_wvalid)

    ,.c_araddr(split2_merge2_araddr[31:0])
    ,.c_arburst(split2_merge2_arburst[1:0])
    ,.c_arextras(split2_merge2_arextras[(EXTRAS - 1):0])
    ,.c_arid(split2_merge2_arid[(IDWID - 1):0])
    ,.c_arlen(split2_merge2_arlen[7:0])
    ,.c_arready(split2_merge2_arready)
    ,.c_arvalid(split2_merge2_arvalid)
    ,.c_awaddr(split2_merge2_awaddr[31:0])
    ,.c_awburst(split2_merge2_awburst[1:0])
    ,.c_awextras(split2_merge2_awextras[(EXTRAS - 1):0])
    ,.c_awid(split2_merge2_awid[(IDWID - 1):0])
    ,.c_awlen(split2_merge2_awlen[7:0])
    ,.c_awready(split2_merge2_awready)
    ,.c_awvalid(split2_merge2_awvalid)
    ,.c_bid(split2_merge2_bid[(IDWID - 1):0])
    ,.c_bready(split2_merge2_bready)
    ,.c_bresp(split2_merge2_bresp[1:0])
    ,.c_bvalid(split2_merge2_bvalid)
    ,.c_rdata(split2_merge2_rdata[(DWID - 1):0])
    ,.c_rid(split2_merge2_rid[(IDWID - 1):0])
    ,.c_rlast(split2_merge2_rlast)
    ,.c_rready(split2_merge2_rready)
    ,.c_rresp(split2_merge2_rresp[1:0])
    ,.c_rvalid(split2_merge2_rvalid)
    ,.c_wdata(split2_merge2_wdata[(DWID - 1):0])
    ,.c_wlast(split2_merge2_wlast)
    ,.c_wready(split2_merge2_wready)
    ,.c_wstrb(split2_merge2_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(split2_merge2_wvalid)

    ,.d_araddr(split3_merge2_araddr[31:0])
    ,.d_arburst(split3_merge2_arburst[1:0])
    ,.d_arextras(split3_merge2_arextras[(EXTRAS - 1):0])
    ,.d_arid(split3_merge2_arid[(IDWID - 1):0])
    ,.d_arlen(split3_merge2_arlen[7:0])
    ,.d_arready(split3_merge2_arready)
    ,.d_arvalid(split3_merge2_arvalid)
    ,.d_awaddr(split3_merge2_awaddr[31:0])
    ,.d_awburst(split3_merge2_awburst[1:0])
    ,.d_awextras(split3_merge2_awextras[(EXTRAS - 1):0])
    ,.d_awid(split3_merge2_awid[(IDWID - 1):0])
    ,.d_awlen(split3_merge2_awlen[7:0])
    ,.d_awready(split3_merge2_awready)
    ,.d_awvalid(split3_merge2_awvalid)
    ,.d_bid(split3_merge2_bid[(IDWID - 1):0])
    ,.d_bready(split3_merge2_bready)
    ,.d_bresp(split3_merge2_bresp[1:0])
    ,.d_bvalid(split3_merge2_bvalid)
    ,.d_rdata(split3_merge2_rdata[(DWID - 1):0])
    ,.d_rid(split3_merge2_rid[(IDWID - 1):0])
    ,.d_rlast(split3_merge2_rlast)
    ,.d_rready(split3_merge2_rready)
    ,.d_rresp(split3_merge2_rresp[1:0])
    ,.d_rvalid(split3_merge2_rvalid)
    ,.d_wdata(split3_merge2_wdata[(DWID - 1):0])
    ,.d_wlast(split3_merge2_wlast)
    ,.d_wready(split3_merge2_wready)
    ,.d_wstrb(split3_merge2_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(split3_merge2_wvalid)
);


wire [IDWID-1:0] merge3_split7_arid ;
wire [31:0] merge3_split7_araddr ;
wire [7:0] merge3_split7_arlen ;
wire [EXTRAS-1:0] merge3_split7_arextras ;
wire [1:0] merge3_split7_arburst ;
wire merge3_split7_arvalid ;
wire merge3_split7_arready ;
wire [IDWID-1:0] merge3_split7_rid ;
wire [DWID-1:0] merge3_split7_rdata ;
wire [1:0] merge3_split7_rresp ;
wire merge3_split7_rlast ;
wire merge3_split7_rvalid ;
wire merge3_split7_rready ;

wire [IDWID-1:0] merge3_split7_awid ;
wire [31:0] merge3_split7_awaddr ;
wire [7:0] merge3_split7_awlen ;
wire [EXTRAS-1:0] merge3_split7_awextras ;
wire [1:0] merge3_split7_awburst ;
wire merge3_split7_awvalid ;
wire merge3_split7_awready ;
wire [DWID-1:0] merge3_split7_wdata ;
wire [WSTRB-1:0] merge3_split7_wstrb ;
wire merge3_split7_wlast ;
wire merge3_split7_wvalid ;
wire merge3_split7_wready ;
wire [IDWID-1:0] merge3_split7_bid ;
wire [1:0] merge3_split7_bresp ;
wire merge3_split7_bvalid ;
wire merge3_split7_bready ;


wire [IDWID-1:0] split1_merge3_arid ;
wire [31:0] split1_merge3_araddr ;
wire [7:0] split1_merge3_arlen ;
wire [EXTRAS-1:0] split1_merge3_arextras ;
wire [1:0] split1_merge3_arburst ;
wire split1_merge3_arvalid ;
wire split1_merge3_arready ;
wire [IDWID-1:0] split1_merge3_rid ;
wire [DWID-1:0] split1_merge3_rdata ;
wire [1:0] split1_merge3_rresp ;
wire split1_merge3_rlast ;
wire split1_merge3_rvalid ;
wire split1_merge3_rready ;

wire [IDWID-1:0] split1_merge3_awid ;
wire [31:0] split1_merge3_awaddr ;
wire [7:0] split1_merge3_awlen ;
wire [EXTRAS-1:0] split1_merge3_awextras ;
wire [1:0] split1_merge3_awburst ;
wire split1_merge3_awvalid ;
wire split1_merge3_awready ;
wire [DWID-1:0] split1_merge3_wdata ;
wire [WSTRB-1:0] split1_merge3_wstrb ;
wire split1_merge3_wlast ;
wire split1_merge3_wvalid ;
wire split1_merge3_wready ;
wire [IDWID-1:0] split1_merge3_bid ;
wire [1:0] split1_merge3_bresp ;
wire split1_merge3_bvalid ;
wire split1_merge3_bready ;


wire [IDWID-1:0] split2_merge3_arid ;
wire [31:0] split2_merge3_araddr ;
wire [7:0] split2_merge3_arlen ;
wire [EXTRAS-1:0] split2_merge3_arextras ;
wire [1:0] split2_merge3_arburst ;
wire split2_merge3_arvalid ;
wire split2_merge3_arready ;
wire [IDWID-1:0] split2_merge3_rid ;
wire [DWID-1:0] split2_merge3_rdata ;
wire [1:0] split2_merge3_rresp ;
wire split2_merge3_rlast ;
wire split2_merge3_rvalid ;
wire split2_merge3_rready ;

wire [IDWID-1:0] split2_merge3_awid ;
wire [31:0] split2_merge3_awaddr ;
wire [7:0] split2_merge3_awlen ;
wire [EXTRAS-1:0] split2_merge3_awextras ;
wire [1:0] split2_merge3_awburst ;
wire split2_merge3_awvalid ;
wire split2_merge3_awready ;
wire [DWID-1:0] split2_merge3_wdata ;
wire [WSTRB-1:0] split2_merge3_wstrb ;
wire split2_merge3_wlast ;
wire split2_merge3_wvalid ;
wire split2_merge3_wready ;
wire [IDWID-1:0] split2_merge3_bid ;
wire [1:0] split2_merge3_bresp ;
wire split2_merge3_bvalid ;
wire split2_merge3_bready ;


wire [IDWID-1:0] split3_merge3_arid ;
wire [31:0] split3_merge3_araddr ;
wire [7:0] split3_merge3_arlen ;
wire [EXTRAS-1:0] split3_merge3_arextras ;
wire [1:0] split3_merge3_arburst ;
wire split3_merge3_arvalid ;
wire split3_merge3_arready ;
wire [IDWID-1:0] split3_merge3_rid ;
wire [DWID-1:0] split3_merge3_rdata ;
wire [1:0] split3_merge3_rresp ;
wire split3_merge3_rlast ;
wire split3_merge3_rvalid ;
wire split3_merge3_rready ;

wire [IDWID-1:0] split3_merge3_awid ;
wire [31:0] split3_merge3_awaddr ;
wire [7:0] split3_merge3_awlen ;
wire [EXTRAS-1:0] split3_merge3_awextras ;
wire [1:0] split3_merge3_awburst ;
wire split3_merge3_awvalid ;
wire split3_merge3_awready ;
wire [DWID-1:0] split3_merge3_wdata ;
wire [WSTRB-1:0] split3_merge3_wstrb ;
wire split3_merge3_wlast ;
wire split3_merge3_wvalid ;
wire split3_merge3_wready ;
wire [IDWID-1:0] split3_merge3_bid ;
wire [1:0] split3_merge3_bresp ;
wire split3_merge3_bvalid ;
wire split3_merge3_bready ;


axi_4_merger merge3 (
     .clk(clk),.rst_n(rst_n)
    ,.araddr(merge3_split7_araddr[31:0])
    ,.arburst(merge3_split7_arburst[1:0])
    ,.arextras(merge3_split7_arextras[(EXTRAS - 1):0])
    ,.arid(merge3_split7_arid[(IDWID - 1):0])
    ,.arlen(merge3_split7_arlen[7:0])
    ,.arready(merge3_split7_arready)
    ,.arvalid(merge3_split7_arvalid)
    ,.awaddr(merge3_split7_awaddr[31:0])
    ,.awburst(merge3_split7_awburst[1:0])
    ,.awextras(merge3_split7_awextras[(EXTRAS - 1):0])
    ,.awid(merge3_split7_awid[3:0])
    ,.awlen(merge3_split7_awlen[7:0])
    ,.awready(merge3_split7_awready)
    ,.awvalid(merge3_split7_awvalid)
    ,.bid(merge3_split7_bid[(IDWID - 1):0])
    ,.bready(merge3_split7_bready)
    ,.bresp(merge3_split7_bresp[1:0])
    ,.bvalid(merge3_split7_bvalid)
    ,.rid(merge3_split7_rid[(IDWID - 1):0])
    ,.rlast(merge3_split7_rlast)
    ,.rready(merge3_split7_rready)
    ,.rresp(merge3_split7_rresp[1:0])
    ,.rvalid(merge3_split7_rvalid)
    ,.rdata(merge3_split7_rdata[(DWID - 1):0])
    ,.wdata(merge3_split7_wdata[(DWID - 1):0])
    ,.wlast(merge3_split7_wlast)
    ,.wready(merge3_split7_wready)
    ,.wstrb(merge3_split7_wstrb[(WSTRB - 1):0])
    ,.wvalid(merge3_split7_wvalid)


    ,.a_araddr(split0_merge3_araddr[31:0])
    ,.a_arburst(split0_merge3_arburst[1:0])
    ,.a_arextras(split0_merge3_arextras[(EXTRAS - 1):0])
    ,.a_arid(split0_merge3_arid[(IDWID - 1):0])
    ,.a_arlen(split0_merge3_arlen[7:0])
    ,.a_arready(split0_merge3_arready)
    ,.a_arvalid(split0_merge3_arvalid)
    ,.a_awaddr(split0_merge3_awaddr[31:0])
    ,.a_awburst(split0_merge3_awburst[1:0])
    ,.a_awextras(split0_merge3_awextras[(EXTRAS - 1):0])
    ,.a_awid(split0_merge3_awid[(IDWID - 1):0])
    ,.a_awlen(split0_merge3_awlen[7:0])
    ,.a_awready(split0_merge3_awready)
    ,.a_awvalid(split0_merge3_awvalid)
    ,.a_bid(split0_merge3_bid[(IDWID - 1):0])
    ,.a_bready(split0_merge3_bready)
    ,.a_bresp(split0_merge3_bresp[1:0])
    ,.a_bvalid(split0_merge3_bvalid)
    ,.a_rdata(split0_merge3_rdata[(DWID - 1):0])
    ,.a_rid(split0_merge3_rid[(IDWID - 1):0])
    ,.a_rlast(split0_merge3_rlast)
    ,.a_rready(split0_merge3_rready)
    ,.a_rresp(split0_merge3_rresp[1:0])
    ,.a_rvalid(split0_merge3_rvalid)
    ,.a_wdata(split0_merge3_wdata[(DWID - 1):0])
    ,.a_wlast(split0_merge3_wlast)
    ,.a_wready(split0_merge3_wready)
    ,.a_wstrb(split0_merge3_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(split0_merge3_wvalid)

    ,.b_araddr(split1_merge3_araddr[31:0])
    ,.b_arburst(split1_merge3_arburst[1:0])
    ,.b_arextras(split1_merge3_arextras[(EXTRAS - 1):0])
    ,.b_arid(split1_merge3_arid[(IDWID - 1):0])
    ,.b_arlen(split1_merge3_arlen[7:0])
    ,.b_arready(split1_merge3_arready)
    ,.b_arvalid(split1_merge3_arvalid)
    ,.b_awaddr(split1_merge3_awaddr[31:0])
    ,.b_awburst(split1_merge3_awburst[1:0])
    ,.b_awextras(split1_merge3_awextras[(EXTRAS - 1):0])
    ,.b_awid(split1_merge3_awid[(IDWID - 1):0])
    ,.b_awlen(split1_merge3_awlen[7:0])
    ,.b_awready(split1_merge3_awready)
    ,.b_awvalid(split1_merge3_awvalid)
    ,.b_bid(split1_merge3_bid[(IDWID - 1):0])
    ,.b_bready(split1_merge3_bready)
    ,.b_bresp(split1_merge3_bresp[1:0])
    ,.b_bvalid(split1_merge3_bvalid)
    ,.b_rdata(split1_merge3_rdata[(DWID - 1):0])
    ,.b_rid(split1_merge3_rid[(IDWID - 1):0])
    ,.b_rlast(split1_merge3_rlast)
    ,.b_rready(split1_merge3_rready)
    ,.b_rresp(split1_merge3_rresp[1:0])
    ,.b_rvalid(split1_merge3_rvalid)
    ,.b_wdata(split1_merge3_wdata[(DWID - 1):0])
    ,.b_wlast(split1_merge3_wlast)
    ,.b_wready(split1_merge3_wready)
    ,.b_wstrb(split1_merge3_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(split1_merge3_wvalid)

    ,.c_araddr(split2_merge3_araddr[31:0])
    ,.c_arburst(split2_merge3_arburst[1:0])
    ,.c_arextras(split2_merge3_arextras[(EXTRAS - 1):0])
    ,.c_arid(split2_merge3_arid[(IDWID - 1):0])
    ,.c_arlen(split2_merge3_arlen[7:0])
    ,.c_arready(split2_merge3_arready)
    ,.c_arvalid(split2_merge3_arvalid)
    ,.c_awaddr(split2_merge3_awaddr[31:0])
    ,.c_awburst(split2_merge3_awburst[1:0])
    ,.c_awextras(split2_merge3_awextras[(EXTRAS - 1):0])
    ,.c_awid(split2_merge3_awid[(IDWID - 1):0])
    ,.c_awlen(split2_merge3_awlen[7:0])
    ,.c_awready(split2_merge3_awready)
    ,.c_awvalid(split2_merge3_awvalid)
    ,.c_bid(split2_merge3_bid[(IDWID - 1):0])
    ,.c_bready(split2_merge3_bready)
    ,.c_bresp(split2_merge3_bresp[1:0])
    ,.c_bvalid(split2_merge3_bvalid)
    ,.c_rdata(split2_merge3_rdata[(DWID - 1):0])
    ,.c_rid(split2_merge3_rid[(IDWID - 1):0])
    ,.c_rlast(split2_merge3_rlast)
    ,.c_rready(split2_merge3_rready)
    ,.c_rresp(split2_merge3_rresp[1:0])
    ,.c_rvalid(split2_merge3_rvalid)
    ,.c_wdata(split2_merge3_wdata[(DWID - 1):0])
    ,.c_wlast(split2_merge3_wlast)
    ,.c_wready(split2_merge3_wready)
    ,.c_wstrb(split2_merge3_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(split2_merge3_wvalid)

    ,.d_araddr(split3_merge3_araddr[31:0])
    ,.d_arburst(split3_merge3_arburst[1:0])
    ,.d_arextras(split3_merge3_arextras[(EXTRAS - 1):0])
    ,.d_arid(split3_merge3_arid[(IDWID - 1):0])
    ,.d_arlen(split3_merge3_arlen[7:0])
    ,.d_arready(split3_merge3_arready)
    ,.d_arvalid(split3_merge3_arvalid)
    ,.d_awaddr(split3_merge3_awaddr[31:0])
    ,.d_awburst(split3_merge3_awburst[1:0])
    ,.d_awextras(split3_merge3_awextras[(EXTRAS - 1):0])
    ,.d_awid(split3_merge3_awid[(IDWID - 1):0])
    ,.d_awlen(split3_merge3_awlen[7:0])
    ,.d_awready(split3_merge3_awready)
    ,.d_awvalid(split3_merge3_awvalid)
    ,.d_bid(split3_merge3_bid[(IDWID - 1):0])
    ,.d_bready(split3_merge3_bready)
    ,.d_bresp(split3_merge3_bresp[1:0])
    ,.d_bvalid(split3_merge3_bvalid)
    ,.d_rdata(split3_merge3_rdata[(DWID - 1):0])
    ,.d_rid(split3_merge3_rid[(IDWID - 1):0])
    ,.d_rlast(split3_merge3_rlast)
    ,.d_rready(split3_merge3_rready)
    ,.d_rresp(split3_merge3_rresp[1:0])
    ,.d_rvalid(split3_merge3_rvalid)
    ,.d_wdata(split3_merge3_wdata[(DWID - 1):0])
    ,.d_wlast(split3_merge3_wlast)
    ,.d_wready(split3_merge3_wready)
    ,.d_wstrb(split3_merge3_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(split3_merge3_wvalid)
);


axi_4_splitter split1 (
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

    ,.a_araddr(split1_merge0_araddr[31:0])
    ,.a_arburst(split1_merge0_arburst[1:0])
    ,.a_arextras(split1_merge0_arextras[(EXTRAS - 1):0])
    ,.a_arid(split1_merge0_arid[(IDWID - 1):0])
    ,.a_arlen(split1_merge0_arlen[7:0])
    ,.a_arready(split1_merge0_arready)
    ,.a_arvalid(split1_merge0_arvalid)
    ,.a_awaddr(split1_merge0_awaddr[31:0])
    ,.a_awburst(split1_merge0_awburst[1:0])
    ,.a_awextras(split1_merge0_awextras[(EXTRAS - 1):0])
    ,.a_awid(split1_merge0_awid[(IDWID - 1):0])
    ,.a_awlen(split1_merge0_awlen[7:0])
    ,.a_awready(split1_merge0_awready)
    ,.a_awvalid(split1_merge0_awvalid)
    ,.a_bid(split1_merge0_bid[(IDWID - 1):0])
    ,.a_bready(split1_merge0_bready)
    ,.a_bresp(split1_merge0_bresp[1:0])
    ,.a_bvalid(split1_merge0_bvalid)
    ,.a_rdata(split1_merge0_rdata[(DWID - 1):0])
    ,.a_rid(split1_merge0_rid[(IDWID - 1):0])
    ,.a_rlast(split1_merge0_rlast)
    ,.a_rready(split1_merge0_rready)
    ,.a_rresp(split1_merge0_rresp[1:0])
    ,.a_rvalid(split1_merge0_rvalid)
    ,.a_wdata(split1_merge0_wdata[(DWID - 1):0])
    ,.a_wlast(split1_merge0_wlast)
    ,.a_wready(split1_merge0_wready)
    ,.a_wstrb(split1_merge0_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(split1_merge0_wvalid)
    ,.b_araddr(split1_merge1_araddr[31:0])
    ,.b_arburst(split1_merge1_arburst[1:0])
    ,.b_arextras(split1_merge1_arextras[(EXTRAS - 1):0])
    ,.b_arid(split1_merge1_arid[(IDWID - 1):0])
    ,.b_arlen(split1_merge1_arlen[7:0])
    ,.b_arready(split1_merge1_arready)
    ,.b_arvalid(split1_merge1_arvalid)
    ,.b_awaddr(split1_merge1_awaddr[31:0])
    ,.b_awburst(split1_merge1_awburst[1:0])
    ,.b_awextras(split1_merge1_awextras[(EXTRAS - 1):0])
    ,.b_awid(split1_merge1_awid[(IDWID - 1):0])
    ,.b_awlen(split1_merge1_awlen[7:0])
    ,.b_awready(split1_merge1_awready)
    ,.b_awvalid(split1_merge1_awvalid)
    ,.b_bid(split1_merge1_bid[(IDWID - 1):0])
    ,.b_bready(split1_merge1_bready)
    ,.b_bresp(split1_merge1_bresp[1:0])
    ,.b_bvalid(split1_merge1_bvalid)
    ,.b_rdata(split1_merge1_rdata[(DWID - 1):0])
    ,.b_rid(split1_merge1_rid[(IDWID - 1):0])
    ,.b_rlast(split1_merge1_rlast)
    ,.b_rready(split1_merge1_rready)
    ,.b_rresp(split1_merge1_rresp[1:0])
    ,.b_rvalid(split1_merge1_rvalid)
    ,.b_wdata(split1_merge1_wdata[(DWID - 1):0])
    ,.b_wlast(split1_merge1_wlast)
    ,.b_wready(split1_merge1_wready)
    ,.b_wstrb(split1_merge1_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(split1_merge1_wvalid)
    ,.c_araddr(split1_merge2_araddr[31:0])
    ,.c_arburst(split1_merge2_arburst[1:0])
    ,.c_arextras(split1_merge2_arextras[(EXTRAS - 1):0])
    ,.c_arid(split1_merge2_arid[(IDWID - 1):0])
    ,.c_arlen(split1_merge2_arlen[7:0])
    ,.c_arready(split1_merge2_arready)
    ,.c_arvalid(split1_merge2_arvalid)
    ,.c_awaddr(split1_merge2_awaddr[31:0])
    ,.c_awburst(split1_merge2_awburst[1:0])
    ,.c_awextras(split1_merge2_awextras[(EXTRAS - 1):0])
    ,.c_awid(split1_merge2_awid[(IDWID - 1):0])
    ,.c_awlen(split1_merge2_awlen[7:0])
    ,.c_awready(split1_merge2_awready)
    ,.c_awvalid(split1_merge2_awvalid)
    ,.c_bid(split1_merge2_bid[(IDWID - 1):0])
    ,.c_bready(split1_merge2_bready)
    ,.c_bresp(split1_merge2_bresp[1:0])
    ,.c_bvalid(split1_merge2_bvalid)
    ,.c_rdata(split1_merge2_rdata[(DWID - 1):0])
    ,.c_rid(split1_merge2_rid[(IDWID - 1):0])
    ,.c_rlast(split1_merge2_rlast)
    ,.c_rready(split1_merge2_rready)
    ,.c_rresp(split1_merge2_rresp[1:0])
    ,.c_rvalid(split1_merge2_rvalid)
    ,.c_wdata(split1_merge2_wdata[(DWID - 1):0])
    ,.c_wlast(split1_merge2_wlast)
    ,.c_wready(split1_merge2_wready)
    ,.c_wstrb(split1_merge2_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(split1_merge2_wvalid)
    ,.d_araddr(split1_merge3_araddr[31:0])
    ,.d_arburst(split1_merge3_arburst[1:0])
    ,.d_arextras(split1_merge3_arextras[(EXTRAS - 1):0])
    ,.d_arid(split1_merge3_arid[(IDWID - 1):0])
    ,.d_arlen(split1_merge3_arlen[7:0])
    ,.d_arready(split1_merge3_arready)
    ,.d_arvalid(split1_merge3_arvalid)
    ,.d_awaddr(split1_merge3_awaddr[31:0])
    ,.d_awburst(split1_merge3_awburst[1:0])
    ,.d_awextras(split1_merge3_awextras[(EXTRAS - 1):0])
    ,.d_awid(split1_merge3_awid[(IDWID - 1):0])
    ,.d_awlen(split1_merge3_awlen[7:0])
    ,.d_awready(split1_merge3_awready)
    ,.d_awvalid(split1_merge3_awvalid)
    ,.d_bid(split1_merge3_bid[(IDWID - 1):0])
    ,.d_bready(split1_merge3_bready)
    ,.d_bresp(split1_merge3_bresp[1:0])
    ,.d_bvalid(split1_merge3_bvalid)
    ,.d_rdata(split1_merge3_rdata[(DWID - 1):0])
    ,.d_rid(split1_merge3_rid[(IDWID - 1):0])
    ,.d_rlast(split1_merge3_rlast)
    ,.d_rready(split1_merge3_rready)
    ,.d_rresp(split1_merge3_rresp[1:0])
    ,.d_rvalid(split1_merge3_rvalid)
    ,.d_wdata(split1_merge3_wdata[(DWID - 1):0])
    ,.d_wlast(split1_merge3_wlast)
    ,.d_wready(split1_merge3_wready)
    ,.d_wstrb(split1_merge3_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(split1_merge3_wvalid)

);

axi_4_splitter split2 (
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

    ,.a_araddr(split2_merge0_araddr[31:0])
    ,.a_arburst(split2_merge0_arburst[1:0])
    ,.a_arextras(split2_merge0_arextras[(EXTRAS - 1):0])
    ,.a_arid(split2_merge0_arid[(IDWID - 1):0])
    ,.a_arlen(split2_merge0_arlen[7:0])
    ,.a_arready(split2_merge0_arready)
    ,.a_arvalid(split2_merge0_arvalid)
    ,.a_awaddr(split2_merge0_awaddr[31:0])
    ,.a_awburst(split2_merge0_awburst[1:0])
    ,.a_awextras(split2_merge0_awextras[(EXTRAS - 1):0])
    ,.a_awid(split2_merge0_awid[(IDWID - 1):0])
    ,.a_awlen(split2_merge0_awlen[7:0])
    ,.a_awready(split2_merge0_awready)
    ,.a_awvalid(split2_merge0_awvalid)
    ,.a_bid(split2_merge0_bid[(IDWID - 1):0])
    ,.a_bready(split2_merge0_bready)
    ,.a_bresp(split2_merge0_bresp[1:0])
    ,.a_bvalid(split2_merge0_bvalid)
    ,.a_rdata(split2_merge0_rdata[(DWID - 1):0])
    ,.a_rid(split2_merge0_rid[(IDWID - 1):0])
    ,.a_rlast(split2_merge0_rlast)
    ,.a_rready(split2_merge0_rready)
    ,.a_rresp(split2_merge0_rresp[1:0])
    ,.a_rvalid(split2_merge0_rvalid)
    ,.a_wdata(split2_merge0_wdata[(DWID - 1):0])
    ,.a_wlast(split2_merge0_wlast)
    ,.a_wready(split2_merge0_wready)
    ,.a_wstrb(split2_merge0_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(split2_merge0_wvalid)
    ,.b_araddr(split2_merge1_araddr[31:0])
    ,.b_arburst(split2_merge1_arburst[1:0])
    ,.b_arextras(split2_merge1_arextras[(EXTRAS - 1):0])
    ,.b_arid(split2_merge1_arid[(IDWID - 1):0])
    ,.b_arlen(split2_merge1_arlen[7:0])
    ,.b_arready(split2_merge1_arready)
    ,.b_arvalid(split2_merge1_arvalid)
    ,.b_awaddr(split2_merge1_awaddr[31:0])
    ,.b_awburst(split2_merge1_awburst[1:0])
    ,.b_awextras(split2_merge1_awextras[(EXTRAS - 1):0])
    ,.b_awid(split2_merge1_awid[(IDWID - 1):0])
    ,.b_awlen(split2_merge1_awlen[7:0])
    ,.b_awready(split2_merge1_awready)
    ,.b_awvalid(split2_merge1_awvalid)
    ,.b_bid(split2_merge1_bid[(IDWID - 1):0])
    ,.b_bready(split2_merge1_bready)
    ,.b_bresp(split2_merge1_bresp[1:0])
    ,.b_bvalid(split2_merge1_bvalid)
    ,.b_rdata(split2_merge1_rdata[(DWID - 1):0])
    ,.b_rid(split2_merge1_rid[(IDWID - 1):0])
    ,.b_rlast(split2_merge1_rlast)
    ,.b_rready(split2_merge1_rready)
    ,.b_rresp(split2_merge1_rresp[1:0])
    ,.b_rvalid(split2_merge1_rvalid)
    ,.b_wdata(split2_merge1_wdata[(DWID - 1):0])
    ,.b_wlast(split2_merge1_wlast)
    ,.b_wready(split2_merge1_wready)
    ,.b_wstrb(split2_merge1_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(split2_merge1_wvalid)
    ,.c_araddr(split2_merge2_araddr[31:0])
    ,.c_arburst(split2_merge2_arburst[1:0])
    ,.c_arextras(split2_merge2_arextras[(EXTRAS - 1):0])
    ,.c_arid(split2_merge2_arid[(IDWID - 1):0])
    ,.c_arlen(split2_merge2_arlen[7:0])
    ,.c_arready(split2_merge2_arready)
    ,.c_arvalid(split2_merge2_arvalid)
    ,.c_awaddr(split2_merge2_awaddr[31:0])
    ,.c_awburst(split2_merge2_awburst[1:0])
    ,.c_awextras(split2_merge2_awextras[(EXTRAS - 1):0])
    ,.c_awid(split2_merge2_awid[(IDWID - 1):0])
    ,.c_awlen(split2_merge2_awlen[7:0])
    ,.c_awready(split2_merge2_awready)
    ,.c_awvalid(split2_merge2_awvalid)
    ,.c_bid(split2_merge2_bid[(IDWID - 1):0])
    ,.c_bready(split2_merge2_bready)
    ,.c_bresp(split2_merge2_bresp[1:0])
    ,.c_bvalid(split2_merge2_bvalid)
    ,.c_rdata(split2_merge2_rdata[(DWID - 1):0])
    ,.c_rid(split2_merge2_rid[(IDWID - 1):0])
    ,.c_rlast(split2_merge2_rlast)
    ,.c_rready(split2_merge2_rready)
    ,.c_rresp(split2_merge2_rresp[1:0])
    ,.c_rvalid(split2_merge2_rvalid)
    ,.c_wdata(split2_merge2_wdata[(DWID - 1):0])
    ,.c_wlast(split2_merge2_wlast)
    ,.c_wready(split2_merge2_wready)
    ,.c_wstrb(split2_merge2_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(split2_merge2_wvalid)
    ,.d_araddr(split2_merge3_araddr[31:0])
    ,.d_arburst(split2_merge3_arburst[1:0])
    ,.d_arextras(split2_merge3_arextras[(EXTRAS - 1):0])
    ,.d_arid(split2_merge3_arid[(IDWID - 1):0])
    ,.d_arlen(split2_merge3_arlen[7:0])
    ,.d_arready(split2_merge3_arready)
    ,.d_arvalid(split2_merge3_arvalid)
    ,.d_awaddr(split2_merge3_awaddr[31:0])
    ,.d_awburst(split2_merge3_awburst[1:0])
    ,.d_awextras(split2_merge3_awextras[(EXTRAS - 1):0])
    ,.d_awid(split2_merge3_awid[(IDWID - 1):0])
    ,.d_awlen(split2_merge3_awlen[7:0])
    ,.d_awready(split2_merge3_awready)
    ,.d_awvalid(split2_merge3_awvalid)
    ,.d_bid(split2_merge3_bid[(IDWID - 1):0])
    ,.d_bready(split2_merge3_bready)
    ,.d_bresp(split2_merge3_bresp[1:0])
    ,.d_bvalid(split2_merge3_bvalid)
    ,.d_rdata(split2_merge3_rdata[(DWID - 1):0])
    ,.d_rid(split2_merge3_rid[(IDWID - 1):0])
    ,.d_rlast(split2_merge3_rlast)
    ,.d_rready(split2_merge3_rready)
    ,.d_rresp(split2_merge3_rresp[1:0])
    ,.d_rvalid(split2_merge3_rvalid)
    ,.d_wdata(split2_merge3_wdata[(DWID - 1):0])
    ,.d_wlast(split2_merge3_wlast)
    ,.d_wready(split2_merge3_wready)
    ,.d_wstrb(split2_merge3_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(split2_merge3_wvalid)

);

axi_4_splitter split3 (
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

    ,.a_araddr(split3_merge0_araddr[31:0])
    ,.a_arburst(split3_merge0_arburst[1:0])
    ,.a_arextras(split3_merge0_arextras[(EXTRAS - 1):0])
    ,.a_arid(split3_merge0_arid[(IDWID - 1):0])
    ,.a_arlen(split3_merge0_arlen[7:0])
    ,.a_arready(split3_merge0_arready)
    ,.a_arvalid(split3_merge0_arvalid)
    ,.a_awaddr(split3_merge0_awaddr[31:0])
    ,.a_awburst(split3_merge0_awburst[1:0])
    ,.a_awextras(split3_merge0_awextras[(EXTRAS - 1):0])
    ,.a_awid(split3_merge0_awid[(IDWID - 1):0])
    ,.a_awlen(split3_merge0_awlen[7:0])
    ,.a_awready(split3_merge0_awready)
    ,.a_awvalid(split3_merge0_awvalid)
    ,.a_bid(split3_merge0_bid[(IDWID - 1):0])
    ,.a_bready(split3_merge0_bready)
    ,.a_bresp(split3_merge0_bresp[1:0])
    ,.a_bvalid(split3_merge0_bvalid)
    ,.a_rdata(split3_merge0_rdata[(DWID - 1):0])
    ,.a_rid(split3_merge0_rid[(IDWID - 1):0])
    ,.a_rlast(split3_merge0_rlast)
    ,.a_rready(split3_merge0_rready)
    ,.a_rresp(split3_merge0_rresp[1:0])
    ,.a_rvalid(split3_merge0_rvalid)
    ,.a_wdata(split3_merge0_wdata[(DWID - 1):0])
    ,.a_wlast(split3_merge0_wlast)
    ,.a_wready(split3_merge0_wready)
    ,.a_wstrb(split3_merge0_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(split3_merge0_wvalid)
    ,.b_araddr(split3_merge1_araddr[31:0])
    ,.b_arburst(split3_merge1_arburst[1:0])
    ,.b_arextras(split3_merge1_arextras[(EXTRAS - 1):0])
    ,.b_arid(split3_merge1_arid[(IDWID - 1):0])
    ,.b_arlen(split3_merge1_arlen[7:0])
    ,.b_arready(split3_merge1_arready)
    ,.b_arvalid(split3_merge1_arvalid)
    ,.b_awaddr(split3_merge1_awaddr[31:0])
    ,.b_awburst(split3_merge1_awburst[1:0])
    ,.b_awextras(split3_merge1_awextras[(EXTRAS - 1):0])
    ,.b_awid(split3_merge1_awid[(IDWID - 1):0])
    ,.b_awlen(split3_merge1_awlen[7:0])
    ,.b_awready(split3_merge1_awready)
    ,.b_awvalid(split3_merge1_awvalid)
    ,.b_bid(split3_merge1_bid[(IDWID - 1):0])
    ,.b_bready(split3_merge1_bready)
    ,.b_bresp(split3_merge1_bresp[1:0])
    ,.b_bvalid(split3_merge1_bvalid)
    ,.b_rdata(split3_merge1_rdata[(DWID - 1):0])
    ,.b_rid(split3_merge1_rid[(IDWID - 1):0])
    ,.b_rlast(split3_merge1_rlast)
    ,.b_rready(split3_merge1_rready)
    ,.b_rresp(split3_merge1_rresp[1:0])
    ,.b_rvalid(split3_merge1_rvalid)
    ,.b_wdata(split3_merge1_wdata[(DWID - 1):0])
    ,.b_wlast(split3_merge1_wlast)
    ,.b_wready(split3_merge1_wready)
    ,.b_wstrb(split3_merge1_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(split3_merge1_wvalid)
    ,.c_araddr(split3_merge2_araddr[31:0])
    ,.c_arburst(split3_merge2_arburst[1:0])
    ,.c_arextras(split3_merge2_arextras[(EXTRAS - 1):0])
    ,.c_arid(split3_merge2_arid[(IDWID - 1):0])
    ,.c_arlen(split3_merge2_arlen[7:0])
    ,.c_arready(split3_merge2_arready)
    ,.c_arvalid(split3_merge2_arvalid)
    ,.c_awaddr(split3_merge2_awaddr[31:0])
    ,.c_awburst(split3_merge2_awburst[1:0])
    ,.c_awextras(split3_merge2_awextras[(EXTRAS - 1):0])
    ,.c_awid(split3_merge2_awid[(IDWID - 1):0])
    ,.c_awlen(split3_merge2_awlen[7:0])
    ,.c_awready(split3_merge2_awready)
    ,.c_awvalid(split3_merge2_awvalid)
    ,.c_bid(split3_merge2_bid[(IDWID - 1):0])
    ,.c_bready(split3_merge2_bready)
    ,.c_bresp(split3_merge2_bresp[1:0])
    ,.c_bvalid(split3_merge2_bvalid)
    ,.c_rdata(split3_merge2_rdata[(DWID - 1):0])
    ,.c_rid(split3_merge2_rid[(IDWID - 1):0])
    ,.c_rlast(split3_merge2_rlast)
    ,.c_rready(split3_merge2_rready)
    ,.c_rresp(split3_merge2_rresp[1:0])
    ,.c_rvalid(split3_merge2_rvalid)
    ,.c_wdata(split3_merge2_wdata[(DWID - 1):0])
    ,.c_wlast(split3_merge2_wlast)
    ,.c_wready(split3_merge2_wready)
    ,.c_wstrb(split3_merge2_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(split3_merge2_wvalid)
    ,.d_araddr(split3_merge3_araddr[31:0])
    ,.d_arburst(split3_merge3_arburst[1:0])
    ,.d_arextras(split3_merge3_arextras[(EXTRAS - 1):0])
    ,.d_arid(split3_merge3_arid[(IDWID - 1):0])
    ,.d_arlen(split3_merge3_arlen[7:0])
    ,.d_arready(split3_merge3_arready)
    ,.d_arvalid(split3_merge3_arvalid)
    ,.d_awaddr(split3_merge3_awaddr[31:0])
    ,.d_awburst(split3_merge3_awburst[1:0])
    ,.d_awextras(split3_merge3_awextras[(EXTRAS - 1):0])
    ,.d_awid(split3_merge3_awid[(IDWID - 1):0])
    ,.d_awlen(split3_merge3_awlen[7:0])
    ,.d_awready(split3_merge3_awready)
    ,.d_awvalid(split3_merge3_awvalid)
    ,.d_bid(split3_merge3_bid[(IDWID - 1):0])
    ,.d_bready(split3_merge3_bready)
    ,.d_bresp(split3_merge3_bresp[1:0])
    ,.d_bvalid(split3_merge3_bvalid)
    ,.d_rdata(split3_merge3_rdata[(DWID - 1):0])
    ,.d_rid(split3_merge3_rid[(IDWID - 1):0])
    ,.d_rlast(split3_merge3_rlast)
    ,.d_rready(split3_merge3_rready)
    ,.d_rresp(split3_merge3_rresp[1:0])
    ,.d_rvalid(split3_merge3_rvalid)
    ,.d_wdata(split3_merge3_wdata[(DWID - 1):0])
    ,.d_wlast(split3_merge3_wlast)
    ,.d_wready(split3_merge3_wready)
    ,.d_wstrb(split3_merge3_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(split3_merge3_wvalid)

);

axi_4_splitter split4 (
     .clk(clk) ,.rst_n(rst_n)

    ,.araddr(merge0_split4_araddr[31:0])
    ,.arburst(merge0_split4_arburst[1:0])
    ,.arextras(merge0_split4_arextras[(EXTRAS - 1):0])
    ,.arid(merge0_split4_arid[(IDWID - 1):0])
    ,.arlen(merge0_split4_arlen[7:0])
    ,.arready(merge0_split4_arready)
    ,.arvalid(merge0_split4_arvalid)
    ,.awaddr(merge0_split4_awaddr[31:0])
    ,.awburst(merge0_split4_awburst[1:0])
    ,.awextras(merge0_split4_awextras[(EXTRAS - 1):0])
    ,.awid(merge0_split4_awid[3:0])
    ,.awlen(merge0_split4_awlen[7:0])
    ,.awready(merge0_split4_awready)
    ,.awvalid(merge0_split4_awvalid)
    ,.bid(merge0_split4_bid[(IDWID - 1):0])
    ,.bready(merge0_split4_bready)
    ,.bresp(merge0_split4_bresp[1:0])
    ,.bvalid(merge0_split4_bvalid)
    ,.rdata(merge0_split4_rdata[(DWID - 1):0])
    ,.rid(merge0_split4_rid[(IDWID - 1):0])
    ,.rlast(merge0_split4_rlast)
    ,.rready(merge0_split4_rready)
    ,.rresp(merge0_split4_rresp[1:0])
    ,.rvalid(merge0_split4_rvalid)
    ,.wdata(merge0_split4_wdata[(DWID - 1):0])
    ,.wlast(merge0_split4_wlast)
    ,.wready(merge0_split4_wready)
    ,.wstrb(merge0_split4_wstrb[(WSTRB - 1):0])
    ,.wvalid(merge0_split4_wvalid)

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

axi_4_splitter split5 (
     .clk(clk) ,.rst_n(rst_n)

    ,.araddr(merge1_split5_araddr[31:0])
    ,.arburst(merge1_split5_arburst[1:0])
    ,.arextras(merge1_split5_arextras[(EXTRAS - 1):0])
    ,.arid(merge1_split5_arid[(IDWID - 1):0])
    ,.arlen(merge1_split5_arlen[7:0])
    ,.arready(merge1_split5_arready)
    ,.arvalid(merge1_split5_arvalid)
    ,.awaddr(merge1_split5_awaddr[31:0])
    ,.awburst(merge1_split5_awburst[1:0])
    ,.awextras(merge1_split5_awextras[(EXTRAS - 1):0])
    ,.awid(merge1_split5_awid[3:0])
    ,.awlen(merge1_split5_awlen[7:0])
    ,.awready(merge1_split5_awready)
    ,.awvalid(merge1_split5_awvalid)
    ,.bid(merge1_split5_bid[(IDWID - 1):0])
    ,.bready(merge1_split5_bready)
    ,.bresp(merge1_split5_bresp[1:0])
    ,.bvalid(merge1_split5_bvalid)
    ,.rdata(merge1_split5_rdata[(DWID - 1):0])
    ,.rid(merge1_split5_rid[(IDWID - 1):0])
    ,.rlast(merge1_split5_rlast)
    ,.rready(merge1_split5_rready)
    ,.rresp(merge1_split5_rresp[1:0])
    ,.rvalid(merge1_split5_rvalid)
    ,.wdata(merge1_split5_wdata[(DWID - 1):0])
    ,.wlast(merge1_split5_wlast)
    ,.wready(merge1_split5_wready)
    ,.wstrb(merge1_split5_wstrb[(WSTRB - 1):0])
    ,.wvalid(merge1_split5_wvalid)

    ,.a_araddr(slv4_araddr[31:0])
    ,.a_arburst(slv4_arburst[1:0])
    ,.a_arextras(slv4_arextras[(EXTRAS - 1):0])
    ,.a_arid(slv4_arid[(IDWID - 1):0])
    ,.a_arlen(slv4_arlen[7:0])
    ,.a_arready(slv4_arready)
    ,.a_arvalid(slv4_arvalid)
    ,.a_awaddr(slv4_awaddr[31:0])
    ,.a_awburst(slv4_awburst[1:0])
    ,.a_awextras(slv4_awextras[(EXTRAS - 1):0])
    ,.a_awid(slv4_awid[(IDWID - 1):0])
    ,.a_awlen(slv4_awlen[7:0])
    ,.a_awready(slv4_awready)
    ,.a_awvalid(slv4_awvalid)
    ,.a_bid(slv4_bid[(IDWID - 1):0])
    ,.a_bready(slv4_bready)
    ,.a_bresp(slv4_bresp[1:0])
    ,.a_bvalid(slv4_bvalid)
    ,.a_rdata(slv4_rdata[(DWID - 1):0])
    ,.a_rid(slv4_rid[(IDWID - 1):0])
    ,.a_rlast(slv4_rlast)
    ,.a_rready(slv4_rready)
    ,.a_rresp(slv4_rresp[1:0])
    ,.a_rvalid(slv4_rvalid)
    ,.a_wdata(slv4_wdata[(DWID - 1):0])
    ,.a_wlast(slv4_wlast)
    ,.a_wready(slv4_wready)
    ,.a_wstrb(slv4_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(slv4_wvalid)
    ,.b_araddr(slv5_araddr[31:0])
    ,.b_arburst(slv5_arburst[1:0])
    ,.b_arextras(slv5_arextras[(EXTRAS - 1):0])
    ,.b_arid(slv5_arid[(IDWID - 1):0])
    ,.b_arlen(slv5_arlen[7:0])
    ,.b_arready(slv5_arready)
    ,.b_arvalid(slv5_arvalid)
    ,.b_awaddr(slv5_awaddr[31:0])
    ,.b_awburst(slv5_awburst[1:0])
    ,.b_awextras(slv5_awextras[(EXTRAS - 1):0])
    ,.b_awid(slv5_awid[(IDWID - 1):0])
    ,.b_awlen(slv5_awlen[7:0])
    ,.b_awready(slv5_awready)
    ,.b_awvalid(slv5_awvalid)
    ,.b_bid(slv5_bid[(IDWID - 1):0])
    ,.b_bready(slv5_bready)
    ,.b_bresp(slv5_bresp[1:0])
    ,.b_bvalid(slv5_bvalid)
    ,.b_rdata(slv5_rdata[(DWID - 1):0])
    ,.b_rid(slv5_rid[(IDWID - 1):0])
    ,.b_rlast(slv5_rlast)
    ,.b_rready(slv5_rready)
    ,.b_rresp(slv5_rresp[1:0])
    ,.b_rvalid(slv5_rvalid)
    ,.b_wdata(slv5_wdata[(DWID - 1):0])
    ,.b_wlast(slv5_wlast)
    ,.b_wready(slv5_wready)
    ,.b_wstrb(slv5_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(slv5_wvalid)
    ,.c_araddr(slv6_araddr[31:0])
    ,.c_arburst(slv6_arburst[1:0])
    ,.c_arextras(slv6_arextras[(EXTRAS - 1):0])
    ,.c_arid(slv6_arid[(IDWID - 1):0])
    ,.c_arlen(slv6_arlen[7:0])
    ,.c_arready(slv6_arready)
    ,.c_arvalid(slv6_arvalid)
    ,.c_awaddr(slv6_awaddr[31:0])
    ,.c_awburst(slv6_awburst[1:0])
    ,.c_awextras(slv6_awextras[(EXTRAS - 1):0])
    ,.c_awid(slv6_awid[(IDWID - 1):0])
    ,.c_awlen(slv6_awlen[7:0])
    ,.c_awready(slv6_awready)
    ,.c_awvalid(slv6_awvalid)
    ,.c_bid(slv6_bid[(IDWID - 1):0])
    ,.c_bready(slv6_bready)
    ,.c_bresp(slv6_bresp[1:0])
    ,.c_bvalid(slv6_bvalid)
    ,.c_rdata(slv6_rdata[(DWID - 1):0])
    ,.c_rid(slv6_rid[(IDWID - 1):0])
    ,.c_rlast(slv6_rlast)
    ,.c_rready(slv6_rready)
    ,.c_rresp(slv6_rresp[1:0])
    ,.c_rvalid(slv6_rvalid)
    ,.c_wdata(slv6_wdata[(DWID - 1):0])
    ,.c_wlast(slv6_wlast)
    ,.c_wready(slv6_wready)
    ,.c_wstrb(slv6_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(slv6_wvalid)
    ,.d_araddr(slv7_araddr[31:0])
    ,.d_arburst(slv7_arburst[1:0])
    ,.d_arextras(slv7_arextras[(EXTRAS - 1):0])
    ,.d_arid(slv7_arid[(IDWID - 1):0])
    ,.d_arlen(slv7_arlen[7:0])
    ,.d_arready(slv7_arready)
    ,.d_arvalid(slv7_arvalid)
    ,.d_awaddr(slv7_awaddr[31:0])
    ,.d_awburst(slv7_awburst[1:0])
    ,.d_awextras(slv7_awextras[(EXTRAS - 1):0])
    ,.d_awid(slv7_awid[(IDWID - 1):0])
    ,.d_awlen(slv7_awlen[7:0])
    ,.d_awready(slv7_awready)
    ,.d_awvalid(slv7_awvalid)
    ,.d_bid(slv7_bid[(IDWID - 1):0])
    ,.d_bready(slv7_bready)
    ,.d_bresp(slv7_bresp[1:0])
    ,.d_bvalid(slv7_bvalid)
    ,.d_rdata(slv7_rdata[(DWID - 1):0])
    ,.d_rid(slv7_rid[(IDWID - 1):0])
    ,.d_rlast(slv7_rlast)
    ,.d_rready(slv7_rready)
    ,.d_rresp(slv7_rresp[1:0])
    ,.d_rvalid(slv7_rvalid)
    ,.d_wdata(slv7_wdata[(DWID - 1):0])
    ,.d_wlast(slv7_wlast)
    ,.d_wready(slv7_wready)
    ,.d_wstrb(slv7_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(slv7_wvalid)

);

axi_4_splitter split6 (
     .clk(clk) ,.rst_n(rst_n)

    ,.araddr(merge2_split6_araddr[31:0])
    ,.arburst(merge2_split6_arburst[1:0])
    ,.arextras(merge2_split6_arextras[(EXTRAS - 1):0])
    ,.arid(merge2_split6_arid[(IDWID - 1):0])
    ,.arlen(merge2_split6_arlen[7:0])
    ,.arready(merge2_split6_arready)
    ,.arvalid(merge2_split6_arvalid)
    ,.awaddr(merge2_split6_awaddr[31:0])
    ,.awburst(merge2_split6_awburst[1:0])
    ,.awextras(merge2_split6_awextras[(EXTRAS - 1):0])
    ,.awid(merge2_split6_awid[3:0])
    ,.awlen(merge2_split6_awlen[7:0])
    ,.awready(merge2_split6_awready)
    ,.awvalid(merge2_split6_awvalid)
    ,.bid(merge2_split6_bid[(IDWID - 1):0])
    ,.bready(merge2_split6_bready)
    ,.bresp(merge2_split6_bresp[1:0])
    ,.bvalid(merge2_split6_bvalid)
    ,.rdata(merge2_split6_rdata[(DWID - 1):0])
    ,.rid(merge2_split6_rid[(IDWID - 1):0])
    ,.rlast(merge2_split6_rlast)
    ,.rready(merge2_split6_rready)
    ,.rresp(merge2_split6_rresp[1:0])
    ,.rvalid(merge2_split6_rvalid)
    ,.wdata(merge2_split6_wdata[(DWID - 1):0])
    ,.wlast(merge2_split6_wlast)
    ,.wready(merge2_split6_wready)
    ,.wstrb(merge2_split6_wstrb[(WSTRB - 1):0])
    ,.wvalid(merge2_split6_wvalid)

    ,.a_araddr(slv8_araddr[31:0])
    ,.a_arburst(slv8_arburst[1:0])
    ,.a_arextras(slv8_arextras[(EXTRAS - 1):0])
    ,.a_arid(slv8_arid[(IDWID - 1):0])
    ,.a_arlen(slv8_arlen[7:0])
    ,.a_arready(slv8_arready)
    ,.a_arvalid(slv8_arvalid)
    ,.a_awaddr(slv8_awaddr[31:0])
    ,.a_awburst(slv8_awburst[1:0])
    ,.a_awextras(slv8_awextras[(EXTRAS - 1):0])
    ,.a_awid(slv8_awid[(IDWID - 1):0])
    ,.a_awlen(slv8_awlen[7:0])
    ,.a_awready(slv8_awready)
    ,.a_awvalid(slv8_awvalid)
    ,.a_bid(slv8_bid[(IDWID - 1):0])
    ,.a_bready(slv8_bready)
    ,.a_bresp(slv8_bresp[1:0])
    ,.a_bvalid(slv8_bvalid)
    ,.a_rdata(slv8_rdata[(DWID - 1):0])
    ,.a_rid(slv8_rid[(IDWID - 1):0])
    ,.a_rlast(slv8_rlast)
    ,.a_rready(slv8_rready)
    ,.a_rresp(slv8_rresp[1:0])
    ,.a_rvalid(slv8_rvalid)
    ,.a_wdata(slv8_wdata[(DWID - 1):0])
    ,.a_wlast(slv8_wlast)
    ,.a_wready(slv8_wready)
    ,.a_wstrb(slv8_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(slv8_wvalid)
    ,.b_araddr(slv9_araddr[31:0])
    ,.b_arburst(slv9_arburst[1:0])
    ,.b_arextras(slv9_arextras[(EXTRAS - 1):0])
    ,.b_arid(slv9_arid[(IDWID - 1):0])
    ,.b_arlen(slv9_arlen[7:0])
    ,.b_arready(slv9_arready)
    ,.b_arvalid(slv9_arvalid)
    ,.b_awaddr(slv9_awaddr[31:0])
    ,.b_awburst(slv9_awburst[1:0])
    ,.b_awextras(slv9_awextras[(EXTRAS - 1):0])
    ,.b_awid(slv9_awid[(IDWID - 1):0])
    ,.b_awlen(slv9_awlen[7:0])
    ,.b_awready(slv9_awready)
    ,.b_awvalid(slv9_awvalid)
    ,.b_bid(slv9_bid[(IDWID - 1):0])
    ,.b_bready(slv9_bready)
    ,.b_bresp(slv9_bresp[1:0])
    ,.b_bvalid(slv9_bvalid)
    ,.b_rdata(slv9_rdata[(DWID - 1):0])
    ,.b_rid(slv9_rid[(IDWID - 1):0])
    ,.b_rlast(slv9_rlast)
    ,.b_rready(slv9_rready)
    ,.b_rresp(slv9_rresp[1:0])
    ,.b_rvalid(slv9_rvalid)
    ,.b_wdata(slv9_wdata[(DWID - 1):0])
    ,.b_wlast(slv9_wlast)
    ,.b_wready(slv9_wready)
    ,.b_wstrb(slv9_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(slv9_wvalid)
    ,.c_araddr(slv10_araddr[31:0])
    ,.c_arburst(slv10_arburst[1:0])
    ,.c_arextras(slv10_arextras[(EXTRAS - 1):0])
    ,.c_arid(slv10_arid[(IDWID - 1):0])
    ,.c_arlen(slv10_arlen[7:0])
    ,.c_arready(slv10_arready)
    ,.c_arvalid(slv10_arvalid)
    ,.c_awaddr(slv10_awaddr[31:0])
    ,.c_awburst(slv10_awburst[1:0])
    ,.c_awextras(slv10_awextras[(EXTRAS - 1):0])
    ,.c_awid(slv10_awid[(IDWID - 1):0])
    ,.c_awlen(slv10_awlen[7:0])
    ,.c_awready(slv10_awready)
    ,.c_awvalid(slv10_awvalid)
    ,.c_bid(slv10_bid[(IDWID - 1):0])
    ,.c_bready(slv10_bready)
    ,.c_bresp(slv10_bresp[1:0])
    ,.c_bvalid(slv10_bvalid)
    ,.c_rdata(slv10_rdata[(DWID - 1):0])
    ,.c_rid(slv10_rid[(IDWID - 1):0])
    ,.c_rlast(slv10_rlast)
    ,.c_rready(slv10_rready)
    ,.c_rresp(slv10_rresp[1:0])
    ,.c_rvalid(slv10_rvalid)
    ,.c_wdata(slv10_wdata[(DWID - 1):0])
    ,.c_wlast(slv10_wlast)
    ,.c_wready(slv10_wready)
    ,.c_wstrb(slv10_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(slv10_wvalid)
    ,.d_araddr(slv11_araddr[31:0])
    ,.d_arburst(slv11_arburst[1:0])
    ,.d_arextras(slv11_arextras[(EXTRAS - 1):0])
    ,.d_arid(slv11_arid[(IDWID - 1):0])
    ,.d_arlen(slv11_arlen[7:0])
    ,.d_arready(slv11_arready)
    ,.d_arvalid(slv11_arvalid)
    ,.d_awaddr(slv11_awaddr[31:0])
    ,.d_awburst(slv11_awburst[1:0])
    ,.d_awextras(slv11_awextras[(EXTRAS - 1):0])
    ,.d_awid(slv11_awid[(IDWID - 1):0])
    ,.d_awlen(slv11_awlen[7:0])
    ,.d_awready(slv11_awready)
    ,.d_awvalid(slv11_awvalid)
    ,.d_bid(slv11_bid[(IDWID - 1):0])
    ,.d_bready(slv11_bready)
    ,.d_bresp(slv11_bresp[1:0])
    ,.d_bvalid(slv11_bvalid)
    ,.d_rdata(slv11_rdata[(DWID - 1):0])
    ,.d_rid(slv11_rid[(IDWID - 1):0])
    ,.d_rlast(slv11_rlast)
    ,.d_rready(slv11_rready)
    ,.d_rresp(slv11_rresp[1:0])
    ,.d_rvalid(slv11_rvalid)
    ,.d_wdata(slv11_wdata[(DWID - 1):0])
    ,.d_wlast(slv11_wlast)
    ,.d_wready(slv11_wready)
    ,.d_wstrb(slv11_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(slv11_wvalid)

);

axi_4_splitter split7 (
     .clk(clk) ,.rst_n(rst_n)

    ,.araddr(merge3_split7_araddr[31:0])
    ,.arburst(merge3_split7_arburst[1:0])
    ,.arextras(merge3_split7_arextras[(EXTRAS - 1):0])
    ,.arid(merge3_split7_arid[(IDWID - 1):0])
    ,.arlen(merge3_split7_arlen[7:0])
    ,.arready(merge3_split7_arready)
    ,.arvalid(merge3_split7_arvalid)
    ,.awaddr(merge3_split7_awaddr[31:0])
    ,.awburst(merge3_split7_awburst[1:0])
    ,.awextras(merge3_split7_awextras[(EXTRAS - 1):0])
    ,.awid(merge3_split7_awid[3:0])
    ,.awlen(merge3_split7_awlen[7:0])
    ,.awready(merge3_split7_awready)
    ,.awvalid(merge3_split7_awvalid)
    ,.bid(merge3_split7_bid[(IDWID - 1):0])
    ,.bready(merge3_split7_bready)
    ,.bresp(merge3_split7_bresp[1:0])
    ,.bvalid(merge3_split7_bvalid)
    ,.rdata(merge3_split7_rdata[(DWID - 1):0])
    ,.rid(merge3_split7_rid[(IDWID - 1):0])
    ,.rlast(merge3_split7_rlast)
    ,.rready(merge3_split7_rready)
    ,.rresp(merge3_split7_rresp[1:0])
    ,.rvalid(merge3_split7_rvalid)
    ,.wdata(merge3_split7_wdata[(DWID - 1):0])
    ,.wlast(merge3_split7_wlast)
    ,.wready(merge3_split7_wready)
    ,.wstrb(merge3_split7_wstrb[(WSTRB - 1):0])
    ,.wvalid(merge3_split7_wvalid)

    ,.a_araddr(slv12_araddr[31:0])
    ,.a_arburst(slv12_arburst[1:0])
    ,.a_arextras(slv12_arextras[(EXTRAS - 1):0])
    ,.a_arid(slv12_arid[(IDWID - 1):0])
    ,.a_arlen(slv12_arlen[7:0])
    ,.a_arready(slv12_arready)
    ,.a_arvalid(slv12_arvalid)
    ,.a_awaddr(slv12_awaddr[31:0])
    ,.a_awburst(slv12_awburst[1:0])
    ,.a_awextras(slv12_awextras[(EXTRAS - 1):0])
    ,.a_awid(slv12_awid[(IDWID - 1):0])
    ,.a_awlen(slv12_awlen[7:0])
    ,.a_awready(slv12_awready)
    ,.a_awvalid(slv12_awvalid)
    ,.a_bid(slv12_bid[(IDWID - 1):0])
    ,.a_bready(slv12_bready)
    ,.a_bresp(slv12_bresp[1:0])
    ,.a_bvalid(slv12_bvalid)
    ,.a_rdata(slv12_rdata[(DWID - 1):0])
    ,.a_rid(slv12_rid[(IDWID - 1):0])
    ,.a_rlast(slv12_rlast)
    ,.a_rready(slv12_rready)
    ,.a_rresp(slv12_rresp[1:0])
    ,.a_rvalid(slv12_rvalid)
    ,.a_wdata(slv12_wdata[(DWID - 1):0])
    ,.a_wlast(slv12_wlast)
    ,.a_wready(slv12_wready)
    ,.a_wstrb(slv12_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(slv12_wvalid)
    ,.b_araddr(slv13_araddr[31:0])
    ,.b_arburst(slv13_arburst[1:0])
    ,.b_arextras(slv13_arextras[(EXTRAS - 1):0])
    ,.b_arid(slv13_arid[(IDWID - 1):0])
    ,.b_arlen(slv13_arlen[7:0])
    ,.b_arready(slv13_arready)
    ,.b_arvalid(slv13_arvalid)
    ,.b_awaddr(slv13_awaddr[31:0])
    ,.b_awburst(slv13_awburst[1:0])
    ,.b_awextras(slv13_awextras[(EXTRAS - 1):0])
    ,.b_awid(slv13_awid[(IDWID - 1):0])
    ,.b_awlen(slv13_awlen[7:0])
    ,.b_awready(slv13_awready)
    ,.b_awvalid(slv13_awvalid)
    ,.b_bid(slv13_bid[(IDWID - 1):0])
    ,.b_bready(slv13_bready)
    ,.b_bresp(slv13_bresp[1:0])
    ,.b_bvalid(slv13_bvalid)
    ,.b_rdata(slv13_rdata[(DWID - 1):0])
    ,.b_rid(slv13_rid[(IDWID - 1):0])
    ,.b_rlast(slv13_rlast)
    ,.b_rready(slv13_rready)
    ,.b_rresp(slv13_rresp[1:0])
    ,.b_rvalid(slv13_rvalid)
    ,.b_wdata(slv13_wdata[(DWID - 1):0])
    ,.b_wlast(slv13_wlast)
    ,.b_wready(slv13_wready)
    ,.b_wstrb(slv13_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(slv13_wvalid)
    ,.c_araddr(slv14_araddr[31:0])
    ,.c_arburst(slv14_arburst[1:0])
    ,.c_arextras(slv14_arextras[(EXTRAS - 1):0])
    ,.c_arid(slv14_arid[(IDWID - 1):0])
    ,.c_arlen(slv14_arlen[7:0])
    ,.c_arready(slv14_arready)
    ,.c_arvalid(slv14_arvalid)
    ,.c_awaddr(slv14_awaddr[31:0])
    ,.c_awburst(slv14_awburst[1:0])
    ,.c_awextras(slv14_awextras[(EXTRAS - 1):0])
    ,.c_awid(slv14_awid[(IDWID - 1):0])
    ,.c_awlen(slv14_awlen[7:0])
    ,.c_awready(slv14_awready)
    ,.c_awvalid(slv14_awvalid)
    ,.c_bid(slv14_bid[(IDWID - 1):0])
    ,.c_bready(slv14_bready)
    ,.c_bresp(slv14_bresp[1:0])
    ,.c_bvalid(slv14_bvalid)
    ,.c_rdata(slv14_rdata[(DWID - 1):0])
    ,.c_rid(slv14_rid[(IDWID - 1):0])
    ,.c_rlast(slv14_rlast)
    ,.c_rready(slv14_rready)
    ,.c_rresp(slv14_rresp[1:0])
    ,.c_rvalid(slv14_rvalid)
    ,.c_wdata(slv14_wdata[(DWID - 1):0])
    ,.c_wlast(slv14_wlast)
    ,.c_wready(slv14_wready)
    ,.c_wstrb(slv14_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(slv14_wvalid)
    ,.d_araddr(slv15_araddr[31:0])
    ,.d_arburst(slv15_arburst[1:0])
    ,.d_arextras(slv15_arextras[(EXTRAS - 1):0])
    ,.d_arid(slv15_arid[(IDWID - 1):0])
    ,.d_arlen(slv15_arlen[7:0])
    ,.d_arready(slv15_arready)
    ,.d_arvalid(slv15_arvalid)
    ,.d_awaddr(slv15_awaddr[31:0])
    ,.d_awburst(slv15_awburst[1:0])
    ,.d_awextras(slv15_awextras[(EXTRAS - 1):0])
    ,.d_awid(slv15_awid[(IDWID - 1):0])
    ,.d_awlen(slv15_awlen[7:0])
    ,.d_awready(slv15_awready)
    ,.d_awvalid(slv15_awvalid)
    ,.d_bid(slv15_bid[(IDWID - 1):0])
    ,.d_bready(slv15_bready)
    ,.d_bresp(slv15_bresp[1:0])
    ,.d_bvalid(slv15_bvalid)
    ,.d_rdata(slv15_rdata[(DWID - 1):0])
    ,.d_rid(slv15_rid[(IDWID - 1):0])
    ,.d_rlast(slv15_rlast)
    ,.d_rready(slv15_rready)
    ,.d_rresp(slv15_rresp[1:0])
    ,.d_rvalid(slv15_rvalid)
    ,.d_wdata(slv15_wdata[(DWID - 1):0])
    ,.d_wlast(slv15_wlast)
    ,.d_wready(slv15_wready)
    ,.d_wstrb(slv15_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(slv15_wvalid)

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

