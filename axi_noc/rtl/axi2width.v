


module axi2width #(parameter IDWID=4,parameter ADWID=64, parameter AWSTRB = ADWID/8
    ,parameter BDWID=64, parameter BWSTRB = BDWID/8,
    ,parameter EXTRAS=8
    ) (

    input clk, input rst_n


    ,input [IDWID-1:0] in_arid
    ,input [31:0] in_araddr
    ,input [7:0] in_arlen
    ,input [EXTRAS-1:0] in_arextras
    ,input [1:0] in_arburst
    ,input in_arvalid
    ,output in_arready
    ,output [IDWID-1:0] in_rid
    ,output [ADWID-1:0] in_rdata
    ,output [1:0] in_rresp
    ,output in_rlast
    ,output in_rvalid
    ,input in_rready

    ,input [3:0] in_awid
    ,input [31:0] in_awaddr
    ,input [7:0] in_awlen
    ,input [EXTRAS-1:0] awextras
    ,input [1:0] awburst
    ,input awvalid
    ,output awready
    ,input [ADWID-1:0] in_wdata
    ,input [AWSTRB-1:0] in_wstrb
    ,input in_wlast
    ,input in_wvalid
    ,output in_wready
    ,output [IDWID-1:0] in_bid 
    ,output [1:0] in_bresp
    ,output in_bvalid
    ,input in_bready





    ,output [IDWID-1:0] ou_arid
    ,output [31:0] ou_araddr
    ,output [7:0] ou_arlen
    ,output [EXTRAS-1:0] ou_arextras
    ,output [1:0] ou_arburst
    ,output ou_arvalid
    ,input ou_arready
    ,input [IDWID-1:0] ou_rid
    ,input [BDWID-1:0] ou_rdata
    ,input [1:0] ou_rresp
    ,input ou_rlast
    ,input ou_rvalid
    ,output ou_rready

    ,output [3:0] ou_awid
    ,output [31:0] ou_awaddr
    ,output [7:0] ou_awlen
    ,output [EXTRAS-1:0] awextras
    ,output [1:0] awburst
    ,output awvalid
    ,input awready
    ,output [DWID-1:0] ou_wdata
    ,output [BWSTRB-1:0] ou_wstrb
    ,output ou_wlast
    ,output ou_wvalid
    ,input ou_wready
    ,input [IDWID-1:0] ou_bid 
    ,input [1:0] ou_bresp
    ,input ou_bvalid
    ,output ou_bready
);
    




wire [63:0]  sign_version = 64'h0001e3cf22060424 ;
endmodule

