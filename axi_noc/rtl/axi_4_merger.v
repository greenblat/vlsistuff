




module axi_4_merger #(parameter IDWID=4,parameter DWID=64, parameter WSTRB=DWID/8, parameter EXTRAS=8)(

    input clk, input rst_n

    ,input [IDWID-1:0] a_arid
    ,input [31:0] a_araddr
    ,input [7:0] a_arlen
    ,input [EXTRAS-1:0] a_arextras
    ,input [1:0] a_arburst
    ,input a_arvalid
    ,output a_arready
    ,output [IDWID-1:0] a_rid
    ,output [DWID-1:0] a_rdata
    ,output [1:0] a_rresp
    ,output a_rlast
    ,output a_rvalid
    ,input a_rready

    ,output [3:0] awid
    ,output [31:0] awaddr
    ,output [7:0] awlen
    ,output [EXTRAS-1:0] awextras
    ,output [1:0] awburst
    ,output awvalid
    ,input awready
    ,output [DWID-1:0] wdata
    ,output [WSTRB-1:0] wstrb
    ,output wlast
    ,output wvalid
    ,input wready
    ,input [IDWID-1:0] bid
    ,input [1:0] bresp
    ,input bvalid
    ,output bready

    ,input [IDWID-1:0] b_arid
    ,input [31:0] b_araddr
    ,input [7:0] b_arlen
    ,input [EXTRAS-1:0] b_arextras
    ,input [1:0] b_arburst
    ,input b_arvalid
    ,output b_arready
    ,output [IDWID-1:0] b_rid
    ,output [DWID-1:0] b_rdata
    ,output [1:0] b_rresp
    ,output b_rlast
    ,output b_rvalid
    ,input b_rready

    ,input [IDWID-1:0] c_arid
    ,input [31:0] c_araddr
    ,input [7:0] c_arlen
    ,input [EXTRAS-1:0] c_arextras
    ,input [1:0] c_arburst
    ,input c_arvalid
    ,output c_arready
    ,output [IDWID-1:0] c_rid
    ,output [DWID-1:0] c_rdata
    ,output [1:0] c_rresp
    ,output c_rlast
    ,output c_rvalid
    ,input c_rready


    ,input [IDWID-1:0] d_arid
    ,input [31:0] d_araddr
    ,input [7:0] d_arlen
    ,input [EXTRAS-1:0] d_arextras
    ,input [1:0] d_arburst
    ,input d_arvalid
    ,output d_arready
    ,output [IDWID-1:0] d_rid
    ,output [DWID-1:0] d_rdata
    ,output [1:0] d_rresp
    ,output d_rlast
    ,output d_rvalid
    ,input d_rready


    ,output [IDWID-1:0] arid
    ,output [31:0] araddr
    ,output [7:0] arlen
    ,output [EXTRAS-1:0] arextras
    ,output [1:0] arburst
    ,output arvalid
    ,input arready
    ,input [IDWID-1:0] rid
    ,input [DWID-1:0] rdata
    ,input [1:0] rresp
    ,input rlast
    ,input rvalid
    ,output rready


    ,input [IDWID-1:0] a_awid
    ,input [31:0] a_awaddr
    ,input [7:0] a_awlen
    ,input [EXTRAS-1:0] a_awextras
    ,input [1:0] a_awburst
    ,input a_awvalid
    ,output a_awready
    ,input [DWID-1:0] a_wdata
    ,input [WSTRB-1:0] a_wstrb
    ,input a_wlast
    ,input a_wvalid
    ,output a_wready
    ,output [IDWID-1:0] a_bid
    ,output [1:0] a_bresp
    ,output a_bvalid
    ,input a_bready

    ,input [IDWID-1:0] b_awid
    ,input [31:0] b_awaddr
    ,input [7:0] b_awlen
    ,input [EXTRAS-1:0] b_awextras
    ,input [1:0] b_awburst
    ,input b_awvalid
    ,output b_awready
    ,input [DWID-1:0] b_wdata
    ,input [WSTRB-1:0] b_wstrb
    ,input b_wlast
    ,input b_wvalid
    ,output b_wready
    ,output [IDWID-1:0] b_bid
    ,output [1:0] b_bresp
    ,output b_bvalid
    ,input b_bready


    ,input [IDWID-1:0] c_awid
    ,input [31:0] c_awaddr
    ,input [7:0] c_awlen
    ,input [EXTRAS-1:0] c_awextras
    ,input [1:0] c_awburst
    ,input c_awvalid
    ,output c_awready
    ,input [DWID-1:0] c_wdata
    ,input [WSTRB-1:0] c_wstrb
    ,input c_wlast
    ,input c_wvalid
    ,output c_wready
    ,output [IDWID-1:0] c_bid
    ,output [1:0] c_bresp
    ,output c_bvalid
    ,input c_bready

    ,input [IDWID-1:0] d_awid
    ,input [31:0] d_awaddr
    ,input [7:0] d_awlen
    ,input [EXTRAS-1:0] d_awextras
    ,input [1:0] d_awburst
    ,input d_awvalid
    ,output d_awready
    ,input [DWID-1:0] d_wdata
    ,input [WSTRB-1:0] d_wstrb
    ,input d_wlast
    ,input d_wvalid
    ,output d_wready
    ,output [IDWID-1:0] d_bid
    ,output [1:0] d_bresp
    ,output d_bvalid
    ,input d_bready




);

axi_wr_4_merger  #(.DWID(DWID),.EXTRAS(EXTRAS),.IDWID(IDWID)) axi_wr_4_merger (
     .clk(clk) ,.rst_n(rst_n)

    ,.awaddr(awaddr[31:0])
    ,.awburst(awburst[1:0])
    ,.awid(awid[3:0])
    ,.awlen(awlen[7:0])
    ,.awready(awready)
    ,.awextras(awextras[EXTRAS-1:0])
    ,.awvalid(awvalid)
    ,.wdata(wdata[(DWID - 1):0])
    ,.wlast(wlast)
    ,.wready(wready)
    ,.wstrb(wstrb[(WSTRB - 1):0])
    ,.wvalid(wvalid)
    ,.bid(bid[(IDWID - 1):0])
    ,.bready(bready)
    ,.bresp(bresp[1:0])
    ,.bvalid(bvalid)

    ,.a_awaddr(a_awaddr[31:0])
    ,.a_awburst(a_awburst[1:0])
    ,.a_awid(a_awid[(IDWID - 1):0])
    ,.a_awlen(a_awlen[7:0])
    ,.a_awready(a_awready)
    ,.a_awextras(a_awextras[EXTRAS-1:0])
    ,.a_awvalid(a_awvalid)
    ,.a_bid(a_bid[(IDWID - 1):0])
    ,.a_bready(a_bready)
    ,.a_bresp(a_bresp[1:0])
    ,.a_bvalid(a_bvalid)
    ,.a_wdata(a_wdata[(DWID - 1):0])
    ,.a_wlast(a_wlast)
    ,.a_wready(a_wready)
    ,.a_wstrb(a_wstrb[(WSTRB - 1):0])
    ,.a_wvalid(a_wvalid)

    ,.b_awaddr(b_awaddr[31:0])
    ,.b_awburst(b_awburst[1:0])
    ,.b_awid(b_awid[(IDWID - 1):0])
    ,.b_awlen(b_awlen[7:0])
    ,.b_awready(b_awready)
    ,.b_awextras(b_awextras[EXTRAS-1:0])
    ,.b_awvalid(b_awvalid)
    ,.b_bid(b_bid[(IDWID - 1):0])
    ,.b_bready(b_bready)
    ,.b_bresp(b_bresp[1:0])
    ,.b_bvalid(b_bvalid)
    ,.b_wdata(b_wdata[(DWID - 1):0])
    ,.b_wlast(b_wlast)
    ,.b_wready(b_wready)
    ,.b_wstrb(b_wstrb[(WSTRB - 1):0])
    ,.b_wvalid(b_wvalid)

    ,.c_awaddr(c_awaddr[31:0])
    ,.c_awburst(c_awburst[1:0])
    ,.c_awid(c_awid[(IDWID - 1):0])
    ,.c_awlen(c_awlen[7:0])
    ,.c_awready(c_awready)
    ,.c_awextras(c_awextras[EXTRAS-1:0])
    ,.c_awvalid(c_awvalid)
    ,.c_bid(c_bid[(IDWID - 1):0])
    ,.c_bready(c_bready)
    ,.c_bresp(c_bresp[1:0])
    ,.c_bvalid(c_bvalid)
    ,.c_wdata(c_wdata[(DWID - 1):0])
    ,.c_wlast(c_wlast)
    ,.c_wready(c_wready)
    ,.c_wstrb(c_wstrb[(WSTRB - 1):0])
    ,.c_wvalid(c_wvalid)

    ,.d_awaddr(d_awaddr[31:0])
    ,.d_awburst(d_awburst[1:0])
    ,.d_awid(d_awid[(IDWID - 1):0])
    ,.d_awlen(d_awlen[7:0])
    ,.d_awready(d_awready)
    ,.d_awextras(d_awextras[EXTRAS-1:0])
    ,.d_awvalid(d_awvalid)
    ,.d_bid(d_bid[(IDWID - 1):0])
    ,.d_bready(d_bready)
    ,.d_bresp(d_bresp[1:0])
    ,.d_bvalid(d_bvalid)
    ,.d_wdata(d_wdata[(DWID - 1):0])
    ,.d_wlast(d_wlast)
    ,.d_wready(d_wready)
    ,.d_wstrb(d_wstrb[(WSTRB - 1):0])
    ,.d_wvalid(d_wvalid)


);


axi_rd_4_merger #(.DWID(DWID),.EXTRAS(EXTRAS),.IDWID(IDWID)) axi_rd_4_merger (
    .clk(clk) ,.rst_n(rst_n)

    ,.araddr(araddr[31:0])
    ,.arburst(arburst[1:0])
    ,.arid(arid[(IDWID - 1):0])
    ,.arlen(arlen[7:0])
    ,.arready(arready)
    ,.arextras(arextras[EXTRAS-1:0])
    ,.arvalid(arvalid)
    ,.rdata(rdata[(DWID - 1):0])
    ,.rid(rid[(IDWID - 1):0])
    ,.rlast(rlast)
    ,.rready(rready)
    ,.rresp(rresp[1:0])
    ,.rvalid(rvalid)

    ,.a_araddr(a_araddr[31:0])
    ,.a_arburst(a_arburst[1:0])
    ,.a_arid(a_arid[(IDWID - 1):0])
    ,.a_arlen(a_arlen[7:0])
    ,.a_arready(a_arready)
    ,.a_arextras(a_arextras[EXTRAS-1:0])
    ,.a_arvalid(a_arvalid)
    ,.a_rdata(a_rdata[(DWID - 1):0])
    ,.a_rid(a_rid[(IDWID - 1):0])
    ,.a_rlast(a_rlast)
    ,.a_rready(a_rready)
    ,.a_rresp(a_rresp[1:0])
    ,.a_rvalid(a_rvalid)

    ,.b_araddr(b_araddr[31:0])
    ,.b_arburst(b_arburst[1:0])
    ,.b_arid(b_arid[(IDWID - 1):0])
    ,.b_arlen(b_arlen[7:0])
    ,.b_arready(b_arready)
    ,.b_arextras(b_arextras[EXTRAS-1:0])
    ,.b_arvalid(b_arvalid)
    ,.b_rdata(b_rdata[(DWID - 1):0])
    ,.b_rid(b_rid[(IDWID - 1):0])
    ,.b_rlast(b_rlast)
    ,.b_rready(b_rready)
    ,.b_rresp(b_rresp[1:0])
    ,.b_rvalid(b_rvalid)

    ,.c_araddr(c_araddr[31:0])
    ,.c_arburst(c_arburst[1:0])
    ,.c_arid(c_arid[(IDWID - 1):0])
    ,.c_arlen(c_arlen[7:0])
    ,.c_arready(c_arready)
    ,.c_arextras(c_arextras[EXTRAS-1:0])
    ,.c_arvalid(c_arvalid)
    ,.c_rdata(c_rdata[(DWID - 1):0])
    ,.c_rid(c_rid[(IDWID - 1):0])
    ,.c_rlast(c_rlast)
    ,.c_rready(c_rready)
    ,.c_rresp(c_rresp[1:0])
    ,.c_rvalid(c_rvalid)

    ,.d_araddr(d_araddr[31:0])
    ,.d_arburst(d_arburst[1:0])
    ,.d_arid(d_arid[(IDWID - 1):0])
    ,.d_arlen(d_arlen[7:0])
    ,.d_arready(d_arready)
    ,.d_arextras(d_arextras[EXTRAS-1:0])
    ,.d_arvalid(d_arvalid)
    ,.d_rdata(d_rdata[(DWID - 1):0])
    ,.d_rid(d_rid[(IDWID - 1):0])
    ,.d_rlast(d_rlast)
    ,.d_rready(d_rready)
    ,.d_rresp(d_rresp[1:0])
    ,.d_rvalid(d_rvalid)
);

endmodule

