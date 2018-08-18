
module rou_axi_master #(
     parameter DWID = 128 
    ,parameter AWID = 32
    ,parameter TWID = 5 
    ,parameter BWID = 
        (DWID==512)  ? 6 : 
        (DWID==256)  ? 5 : 
        (DWID==128) ? 4 : 
        (DWID==64)  ? 3 : 2 
    ,parameter WID = 2+DWID+AWID+BWID+TWID
) (
    input clk, input rst_n
    ,input rou_in_seen, output rou_out_seen
    ,input [WID-1:0] rou_in, output [2:0] ack_in 
    ,output [WID-1:0] rou_out, input [2:0] ack_out
    ,input [31:0] pages, input [31:0] whoami



// axi write addr channel
    ,output [3:0] awid           // addr write id
    ,output [ADWID-1:0] awaddr
    ,output [7:0] awlen
    ,output [3:0] awqos
    ,output [2:0] awsize
    ,output [1:0] awburst
    //,output awlock
    ,output [3:0] awcache
    ,output [2:0] awprot
    ,output awvalid
    ,input awready

// axi write data channel
    ,output [127:0] wdata
    ,output [15:0] wstrb
    ,output wlast
    ,output wvalid
    ,input wready

// axi write responce channel
    ,input [3:0] bid 
    ,input [1:0] bresp
    ,input bvalid
    ,output bready

// axi read addr channel
    ,output [3:0] arid
    ,output [ADWID-1:0] araddr
    ,output [7:0] arlen
    ,output [3:0] arqos
    ,output [2:0] arsize
    ,output [1:0] arburst
    //,output arlock
    ,output [3:0] arcache
    ,output [2:0] arprot
    ,output arvalid
    ,input arready
    
// axi read data channel
    ,input [3:0] rid 
    ,input [127:0] rdata
    ,input [1:0] rresp
    ,input rlast
    ,input rvalid
    ,output rready




);

wire [31:0] control;
wire [WID-1:0] msg_in,msg_out;
wire msg_in_ack,msg_out_ack;

wire [AWID-1:0] base_address;

rou_nif nif (
     .ack_in(ack_in[2:0])
    ,.ack_out(ack_out[2:0])
    ,.clk(clk)
    ,.control(control[31:0])
    ,.base_address(base_address)
    ,.msg_in(msg_in[(WID - 1):0])
    ,.msg_in_ack(msg_in_ack)
    ,.msg_out(msg_out[(WID - 1):0])
    ,.msg_out_ack(msg_out_ack)

    ,.rou_in_seen(rou_in_seen)
    ,.rou_out_seen(rou_out_seen)

    ,.rou_in(rou_in[(WID - 1):0])
    ,.rou_out(rou_out[(WID - 1):0])
    ,.rst_n(rst_n)
    ,.uses_pages(pages[15:0])
    ,.whoami(whoami[15:0])
    ,.seen_monitor(1'b0)
);



endmodule

