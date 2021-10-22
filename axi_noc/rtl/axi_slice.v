
// module to cut long physical wires with rest-stop.

module axi_slice #(parameter AWID=32, parameter IDWID=4,parameter DWID=64, parameter WSTRB = DWID/8, parameter EXTRAS=8)(

    input clk, input rst_n

    ,input [IDWID-1:0] in_arid
    ,input [AWID-1:0] in_araddr
    ,input [7:0] in_arlen
    ,input [EXTRAS-1:0] in_arextras
    ,input [1:0] in_arburst
    ,input in_arvalid
    ,output in_arready
    ,output [IDWID-1:0] in_rid
    ,output [DWID-1:0] in_rdata
    ,output [1:0] in_rresp
    ,output in_rlast
    ,output in_rvalid
    ,input in_rready

    ,input [IDWID-1:0] in_awid
    ,input [AWID-1:0] in_awaddr
    ,input [7:0] in_awlen
    ,input [EXTRAS-1:0] in_awextras
    ,input [1:0] in_awburst
    ,input in_awvalid
    ,output in_awready
    ,input [DWID-1:0] in_wdata
    ,input [WSTRB-1:0] in_wstrb
    ,input in_wlast
    ,input in_wvalid
    ,output in_wready
    ,output [IDWID-1:0] in_bid
    ,output [1:0] in_bresp
    ,output in_bvalid
    ,input in_bready





    ,output [IDWID-1:0] ou_arid
    ,output [AWID-1:0] ou_araddr
    ,output [7:0] ou_arlen
    ,output [EXTRAS-1:0] ou_arextras
    ,output [1:0] ou_arburst
    ,output ou_arvalid
    ,input ou_arready

    ,input [IDWID-1:0] ou_rid
    ,input [DWID-1:0] ou_rdata
    ,input [1:0] ou_rresp
    ,input ou_rlast
    ,input ou_rvalid
    ,output ou_rready

    ,output [IDWID-1:0] ou_awid
    ,output [AWID-1:0] ou_awaddr
    ,output [7:0] ou_awlen
    ,output [EXTRAS-1:0] ou_awextras
    ,output [1:0] ou_awburst
    ,output ou_awvalid
    ,input ou_awready
    ,output [DWID-1:0] ou_wdata
    ,output [WSTRB-1:0] ou_wstrb
    ,output ou_wlast
    ,output ou_wvalid
    ,input ou_wready
    ,input [IDWID-1:0] ou_bid
    ,input [1:0] ou_bresp
    ,input ou_bvalid
    ,output ou_bready
);

wire aw_empty,aw_full;
assign ou_awvalid = !aw_empty;
assign in_awready = !aw_full;
syncfifo #(.WID(AWID+IDWID+8+EXTRAS+2),.DEPTH(2)) aw_fifo (
     .rst_n(rst_n)
    ,.clk(clk)
    ,.dout({ou_awid,ou_awlen,ou_awextras,ou_awburst,ou_awaddr})
    ,.readout(ou_awready && !aw_empty)
    ,.empty(aw_empty)

    ,.din({in_awid,in_awlen,in_awextras,in_awburst,in_awaddr})
    ,.full(aw_full)
    ,.vldin(in_awvalid && in_awready)
    ,.count(),.overflow()
);


wire w_empty,w_full;
assign ou_wvalid = !w_empty;
assign in_wready = !w_full;
syncfifo #(.WID(DWID+WSTRB+1),.DEPTH(2)) w_fifo (
     .rst_n(rst_n)
    ,.clk(clk)
    ,.din({ou_wdata,ou_wstrb,ou_wlast})
    ,.readout(ou_wready && !w_empty)
    ,.empty(w_empty)

    ,.dout({in_wdata,in_wstrb,in_wlast})
    ,.full(w_full)
    ,.vldin(in_wvalid && in_wready)
    ,.count(),.overflow()
);



wire b_empty,b_full;
assign in_bvalid = !b_empty;
assign ou_bready = !b_full;
syncfifo #(.WID(IDWID+2),.DEPTH(2)) b_fifo (
     .rst_n(rst_n)
    ,.clk(clk)
    ,.dout({in_bid,in_bresp})
    ,.readout(in_bready && !b_empty)
    ,.empty(b_empty)

    ,.din({ou_bid,ou_bresp})
    ,.full(b_full)
    ,.vldin(ou_bvalid && ou_bready)
    ,.count(),.overflow()
);



wire ar_empty,ar_full;
assign ou_arvalid = !ar_empty;
assign in_arready = !ar_full;
syncfifo #(.WID(AWID+IDWID+8+EXTRAS+2),.DEPTH(2)) ar_fifo (
     .rst_n(rst_n)
    ,.clk(clk)
    ,.dout({ou_araddr,ou_arid,ou_arlen,ou_arextras,ou_arburst})
    ,.readout(ou_arready && !ar_empty)
    ,.empty(ar_empty)

    ,.din({in_araddr,in_arid,in_arlen,in_arextras,in_arburst})
    ,.full(ar_full)
    ,.vldin(in_arvalid && in_arready)
    ,.count(),.overflow()
);



wire r_empty,r_full;
assign in_rvalid = !r_empty;
assign ou_rready = !r_full;
syncfifo #(.WID(DWID+IDWID+1+2),.DEPTH(2)) r_fifo (
     .rst_n(rst_n)
    ,.clk(clk)
    ,.din({in_rdata,in_rid,in_rlast,in_rresp})
    ,.readout(in_rready && !r_empty)
    ,.empty(r_empty)

    ,.dout({ou_rdata,ou_rid,ou_rlast,ou_rresp})
    ,.full(r_full)
    ,.vldin(ou_rvalid && ou_rready)
    ,.count(),.overflow()
);

endmodule


