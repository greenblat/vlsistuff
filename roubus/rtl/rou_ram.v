

module rou_ram #(parameter DWID=128, parameter AWID=32, parameter CWID=8,parameter WID = 2+DWID+AWID+CWID, parameter DEPTH=1024) (
    input clk, input rst_n
    ,input  [WID-1:0] rou_in, output [2:0] ack_in
    ,output [WID-1:0] rou_out, input [2:0] ack_out
);

parameter WSTRB = DWID/8;
wire [31:0] TOTBYTES = (DEPTH * DWID /8);

wire [15:0] uses_pages = (TOTBYTES>10)+(TOTBYTES[9:0]!=0);

wire [WID-1:0] msg_in,msg_out;
rou_nif #(.DWID(DWID),.AWID(AWID)) nif (
     .clk(clk) ,.rst_n(rst_n)
    ,.ack_in(ack_in[2:0])
    ,.ack_out(ack_out[2:0])
    ,.msg_in(msg_in[(WID - 1):0])
    ,.msg_in_ack(msg_in_ack)
    ,.msg_out(msg_out[(WID - 1):0])
    ,.msg_out_ack(msg_out_ack)
    ,.rou_in(rou_in[(WID - 1):0])
    ,.rou_out(rou_out[(WID - 1):0])
    ,.uses_pages(uses_pages[15:0])
);

wire [31:0] local_addr;
wire  local_rd;
wire  local_rd_addr_ok = 1;
wire [DWID-1:0] local_rd_data;
wire  local_rd_data_ok = 1;
reg  local_rd_error;
wire  local_wr;
wire [(DWID - 1):0] local_wr_data;
reg  local_wr_error;
reg  local_wr_ok;
wire [(WSTRB - 1):0] local_wstrb;





rou_memif memif (
     .clk(clk) ,.rst_n(rst_n)
    ,.local_addr(local_addr[31:0])
    ,.local_rd(local_rd)
    ,.local_rd_addr_ok(local_rd_addr_ok)
    ,.local_rd_data(local_rd_data)
    ,.local_rd_data_ok(local_rd_data_ok)
    ,.local_rd_error(local_rd_error)
    ,.local_wr(local_wr)
    ,.local_wr_data(local_wr_data)
    ,.local_wr_error(local_wr_error)
    ,.local_wr_ok(local_wr_ok)
    ,.local_wstrb(local_wstrb)
    ,.msg_in(msg_in)
    ,.msg_in_ack(msg_in_ack)
    ,.msg_out(msg_out)
    ,.msg_out_ack(msg_out_ack)
);

wire cen = !local_wr && !local_rd;
wire wen = !local_wr;
wire [DWID-1:0] bwen = 0;
parameter ADDRWID = $clog2(DEPTH);
ram_single_port #(.DWID(DWID),.WORDS(DEPTH),.WORDS(DEPTH)) ram (
    .clk(clk)
    ,.cen(cen)
    ,.wen(wen)
    ,.bwen(bwen)
    ,.addr(local_addr[ADDRWID-1:0])
    ,.wdata(local_wr_data)
    ,.rdata(local_rd_data)
);


endmodule

