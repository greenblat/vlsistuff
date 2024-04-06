

module axi2serdes #(parameter IDWID=4,parameter DWID=64, parameter WSTRB=DWID/8)(

    input clk, input rst_n


    ,input [IDWID-1:0] arid
    ,input [31:0] araddr
    ,input [7:0] arlen
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
    ,input [31:0] awaddr
    ,input [7:0] awlen
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

    ,output [WBUS-1:0] outgoing
    ,input outok

    ,input [WBUS-1:0] incoming
    ,output inok


);

wire softreset = 0;
wire [WBUS-1:0] outgoing_wire;
assign outgoing = {outgoing_wire[WBUS-1:3],(out_fifo_empty ? 3'b0 : outgoing_wire[2:0]};
syncfifo_sampled #(.WID(WBUS),.DEPTH(6)) out_fifo  (
     .clk(clk),.rst_n(rst_n)
    ,.vldin(vldin_outfifo),.din(outbus)
    ,.readout(outok),.doit(outgoing_wire)
    ,.empty(out_fifo_empty),.full(out_fifo_full)
    ,.count(),.softreset(softreset)
);

wire vldin_infifo = incoming[2:0] != 0;
wire [WBUS-1:0] incoming_bus;
wire in_fifo_readout,in_fifo_empty,in_fifo_full;
wire [4:0] in_fifo_count;
syncfifo_sampled #(.WID(WBUS),.DEPTH(6)) in_fifo  (
     .clk(clk),.rst_n(rst_n)
    ,.vldin(vldin_infifo),.din(incoming)
    ,.readout(in_fifo_readout),.doit(incoming_bus)
    ,.empty(in_fifo_empty),.full(in_fifo_full)
    ,.count(in_fifo_count),.softreset(softreset)
);

assign inok = in_fifo_count<5;






wire [63:0]  sign_version = 64'h0001eff822060424 ;
endmodule

