




module axi_4_splitter #(parameter AWID=32, parameter EXTRAS = 8,parameter IDWID=4, parameter DWID=64, parameter WSTRB=DWID/8)(

     input clk, input rst_n

    ,input [IDWID-1:0] arid
    ,input [AWID-1:0] araddr
    ,input [7:0] arlen
    ,input [2:0] arsize
    ,input [EXTRAS-1:0] arextras
    ,input [1:0] arburst
    ,input arvalid
    ,output arready
    ,output [IDWID-1:0] rid
    ,output [DWID-1:0] rdata
    ,output [1:0] rresp
    ,output rlast
    ,output rvalid
    ,input rready

    ,input [3:0] awid
    ,input [AWID-1:0] awaddr
    ,input [7:0] awlen
    ,input [2:0] awsize
    ,input [EXTRAS-1:0] awextras
    ,input [1:0] awburst
    ,input awvalid
    ,output awready
    ,input [DWID-1:0] wdata
    ,input [WSTRB-1:0] wstrb
    ,input wlast
    ,input wvalid
    ,output wready
    ,output [IDWID-1:0] bid
    ,output [1:0] bresp
    ,output bvalid
    ,input bready

    ,output [IDWID-1:0] a_arid
    ,output [AWID-1:0] a_araddr
    ,output [7:0] a_arlen
    ,output [2:0] a_arsize
    ,output [EXTRAS-1:0] a_arextras
    ,output [1:0] a_arburst
    ,output a_arvalid
    ,input a_arready
    ,input [IDWID-1:0] a_rid
    ,input [DWID-1:0] a_rdata
    ,input [1:0] a_rresp
    ,input a_rlast
    ,input a_rvalid
    ,output a_rready


    ,output [IDWID-1:0] b_arid
    ,output [AWID-1:0] b_araddr
    ,output [7:0] b_arlen
    ,output [2:0] b_arsize
    ,output [EXTRAS-1:0] b_arextras
    ,output [1:0] b_arburst
    ,output b_arvalid
    ,input b_arready
    ,input [IDWID-1:0] b_rid
    ,input [DWID-1:0] b_rdata
    ,input [1:0] b_rresp
    ,input b_rlast
    ,input b_rvalid
    ,output b_rready

    ,output [IDWID-1:0] c_arid
    ,output [AWID-1:0] c_araddr
    ,output [7:0] c_arlen
    ,output [2:0] c_arsize
    ,output [EXTRAS-1:0] c_arextras
    ,output [1:0] c_arburst
    ,output c_arvalid
    ,input c_arready
    ,input [IDWID-1:0] c_rid
    ,input [DWID-1:0] c_rdata
    ,input [1:0] c_rresp
    ,input c_rlast
    ,input c_rvalid
    ,output c_rready


    ,output [IDWID-1:0] d_arid
    ,output [AWID-1:0] d_araddr
    ,output [7:0] d_arlen
    ,output [2:0] d_arsize
    ,output [EXTRAS-1:0] d_arextras
    ,output [1:0] d_arburst
    ,output d_arvalid
    ,input d_arready
    ,input [IDWID-1:0] d_rid
    ,input [DWID-1:0] d_rdata
    ,input [1:0] d_rresp
    ,input d_rlast
    ,input d_rvalid
    ,output d_rready





    ,output [IDWID-1:0] a_awid
    ,output [AWID-1:0] a_awaddr
    ,output [7:0] a_awlen
    ,output [2:0] a_awsize
    ,output [EXTRAS-1:0] a_awextras
    ,output [1:0] a_awburst
    ,output a_awvalid
    ,input a_awready
    ,output [DWID-1:0] a_wdata
    ,output [WSTRB-1:0] a_wstrb
    ,output a_wlast
    ,output a_wvalid
    ,input a_wready
    ,input [IDWID-1:0] a_bid
    ,input [1:0] a_bresp
    ,input a_bvalid
    ,output a_bready

    ,output [IDWID-1:0] b_awid
    ,output [AWID-1:0] b_awaddr
    ,output [7:0] b_awlen
    ,output [2:0] b_awsize
    ,output [EXTRAS-1:0] b_awextras
    ,output [1:0] b_awburst
    ,output b_awvalid
    ,input b_awready
    ,output [DWID-1:0] b_wdata
    ,output [WSTRB-1:0] b_wstrb
    ,output b_wlast
    ,output b_wvalid
    ,input b_wready
    ,input [IDWID-1:0] b_bid
    ,input [1:0] b_bresp
    ,input b_bvalid
    ,output b_bready


    ,output [IDWID-1:0] c_awid
    ,output [AWID-1:0] c_awaddr
    ,output [7:0] c_awlen
    ,output [2:0] c_awsize
    ,output [EXTRAS-1:0] c_awextras
    ,output [1:0] c_awburst
    ,output c_awvalid
    ,input c_awready
    ,output [DWID-1:0] c_wdata
    ,output [WSTRB-1:0] c_wstrb
    ,output c_wlast
    ,output c_wvalid
    ,input c_wready
    ,input [IDWID-1:0] c_bid
    ,input [1:0] c_bresp
    ,input c_bvalid
    ,output c_bready

    ,output [IDWID-1:0] d_awid
    ,output [AWID-1:0] d_awaddr
    ,output [7:0] d_awlen
    ,output [2:0] d_awsize
    ,output [EXTRAS-1:0] d_awextras
    ,output [1:0] d_awburst
    ,output d_awvalid
    ,input d_awready
    ,output [DWID-1:0] d_wdata
    ,output [WSTRB-1:0] d_wstrb
    ,output d_wlast
    ,output d_wvalid
    ,input d_wready
    ,input [IDWID-1:0] d_bid
    ,input [1:0] d_bresp
    ,input d_bvalid
    ,output d_bready




);

axi_wr_4_splitter  #(.AWID(AWID),.DWID(DWID),.EXTRAS(EXTRAS),.IDWID(IDWID)) axi_wr_4_splitter (
     .clk(clk) ,.rst_n(rst_n)

    ,.awaddr(awaddr[AWID-1:0])
    ,.awburst(awburst[1:0])
    ,.awid(awid[3:0])
    ,.awlen(awlen[7:0])
    ,.awsize(awsize)
    ,.awready(awready)
    ,.awextras(awextras[EXTRAS-1:0])
    ,.awvalid(awvalid)
    ,.bid(bid[(IDWID - 1):0])
    ,.bready(bready)
    ,.bresp(bresp[1:0])
    ,.bvalid(bvalid)
    ,.wdata(wdata[(DWID - 1):0])
    ,.wlast(wlast)
    ,.wready(wready)
    ,.wstrb(wstrb[(WSTRB - 1):0])
    ,.wvalid(wvalid)

    ,.a_awaddr(a_awaddr[AWID-1:0])
    ,.a_awburst(a_awburst[1:0])
    ,.a_awid(a_awid[(IDWID - 1):0])
    ,.a_awlen(a_awlen[7:0])
    ,.a_awsize(a_awsize)
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


    ,.b_awaddr(b_awaddr[AWID-1:0])
    ,.b_awburst(b_awburst[1:0])
    ,.b_awid(b_awid[(IDWID - 1):0])
    ,.b_awlen(b_awlen[7:0])
    ,.b_awsize(b_awsize)
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

    ,.c_awaddr(c_awaddr[AWID-1:0])
    ,.c_awburst(c_awburst[1:0])
    ,.c_awid(c_awid[(IDWID - 1):0])
    ,.c_awlen(c_awlen[7:0])
    ,.c_awsize(c_awsize)
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

    ,.d_awaddr(d_awaddr[AWID-1:0])
    ,.d_awburst(d_awburst[1:0])
    ,.d_awid(d_awid[(IDWID - 1):0])
    ,.d_awlen(d_awlen[7:0])
    ,.d_awsize(d_awsize)
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


axi_rd_4_splitter  #(.AWID(AWID),.DWID(DWID),.EXTRAS(EXTRAS),.IDWID(IDWID)) axi_rd_4_splitter (
     .clk(clk) ,.rst_n(rst_n)

    ,.araddr(araddr[AWID-1:0])
    ,.arburst(arburst[1:0])
    ,.arid(arid[(IDWID - 1):0])
    ,.arlen(arlen[7:0])
    ,.arsize(arsize)
    ,.arready(arready)
    ,.arextras(arextras[EXTRAS-1:0])
    ,.arvalid(arvalid)
    ,.rdata(rdata[(DWID - 1):0])
    ,.rid(rid[(IDWID - 1):0])
    ,.rlast(rlast)
    ,.rready(rready)
    ,.rresp(rresp[1:0])
    ,.rvalid(rvalid)

    ,.a_araddr(a_araddr[AWID-1:0])
    ,.a_arburst(a_arburst[1:0])
    ,.a_arid(a_arid[(IDWID - 1):0])
    ,.a_arlen(a_arlen[7:0])
    ,.a_arsize(a_arsize)
    ,.a_arready(a_arready)
    ,.a_arextras(a_arextras[EXTRAS-1:0])
    ,.a_arvalid(a_arvalid)
    ,.a_rdata(a_rdata[(DWID - 1):0])
    ,.a_rid(a_rid[(IDWID - 1):0])
    ,.a_rlast(a_rlast)
    ,.a_rready(a_rready)
    ,.a_rresp(a_rresp[1:0])
    ,.a_rvalid(a_rvalid)

    ,.b_araddr(b_araddr[AWID-1:0])
    ,.b_arburst(b_arburst[1:0])
    ,.b_arid(b_arid[(IDWID - 1):0])
    ,.b_arlen(b_arlen[7:0])
    ,.b_arsize(b_arsize)
    ,.b_arready(b_arready)
    ,.b_arextras(b_arextras[EXTRAS-1:0])
    ,.b_arvalid(b_arvalid)
    ,.b_rdata(b_rdata[(DWID - 1):0])
    ,.b_rid(b_rid[(IDWID - 1):0])
    ,.b_rlast(b_rlast)
    ,.b_rready(b_rready)
    ,.b_rresp(b_rresp[1:0])
    ,.b_rvalid(b_rvalid)

    ,.c_araddr(c_araddr[AWID-1:0])
    ,.c_arburst(c_arburst[1:0])
    ,.c_arid(c_arid[(IDWID - 1):0])
    ,.c_arlen(c_arlen[7:0])
    ,.c_arsize(c_arsize)
    ,.c_arready(c_arready)
    ,.c_arextras(c_arextras[EXTRAS-1:0])
    ,.c_arvalid(c_arvalid)
    ,.c_rdata(c_rdata[(DWID - 1):0])
    ,.c_rid(c_rid[(IDWID - 1):0])
    ,.c_rlast(c_rlast)
    ,.c_rready(c_rready)
    ,.c_rresp(c_rresp[1:0])
    ,.c_rvalid(c_rvalid)

    ,.d_araddr(d_araddr[AWID-1:0])
    ,.d_arburst(d_arburst[1:0])
    ,.d_arid(d_arid[(IDWID - 1):0])
    ,.d_arlen(d_arlen[7:0])
    ,.d_arsize(d_arsize)
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

wire [63:0]  sign_version = 64'h0009991022060424 ;
endmodule

