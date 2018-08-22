

module dbguart_operator #(
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
     input clk, input rst_n , input softreset
    ,input [7:0] status
    ,output [7:0] txdata
    ,input [7:0] rxdata
    ,input rx_valid
    ,input tx_empty
    ,output read_rx
    ,output write_tx
    ,output [15:0] baudrate



    ,input [WID-1:0] msg_in
    ,output msg_in_ack

    ,output [WID-1:0] msg_out
    ,input  msg_out_ack


    ,output [7:0] uart_control
    ,input [31:0] control
    ,input [AWID-1:0] base_address

);

wire [4:0] addr;
wire rsel,rwrite;
wire [31:0] wrdata,rdata;
wire [1:0] rsize = 2;


assign addr=0;
assign rsel=0;
assign rwrite=0;
assign wrdata = 0;
dbguart_rgf dbguart_rgf (
     .clk(clk) ,.rst_n(rst_n)
    ,.addr(addr[4:0])
    ,.base_address(base_address[31:0])
    ,.baudrate(baudrate[15:0])
    ,.control(control[31:0])
    ,.rdata(rdata[31:0])
    ,.rsel(rsel)
    ,.rsize(rsize[1:0])
    ,.rwrite(rwrite)
    ,.uart_control(uart_control[7:0])
    ,.wrdata(wrdata[31:0])
);




assign read_rx = 0;
assign msg_out  = 0;


wire in_msg_fifo_full,in_msg_fifo_empty,take_msg_in;
wire [WID-1:0] msg_in_raw;
syncfifo #(WID,4) in_msg_fifo (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(msg_in[1:0]!=2'b00),.datain(msg_in)
    ,.full(in_msg_fifo_full),.empty(in_msg_fifo_empty),.overflow(),.count()
    ,.readout(take_msg_in),.dataout(msg_in_raw)
);

assign msg_in_ack = !in_msg_fifo_full;

wire [1:0] msg_in_cmd;
wire [AWID-1:0] msg_in_addr;
wire [DWID-1:0] msg_in_data;
wire [TWID-1:0] msg_in_tags;
wire [BWID-1:0] msg_in_bytes;

rou_msg_fields msg_in_fields(.msg(msg_in), .addr(msg_in_addr) ,.tags(msg_in_tags) ,.bytes(msg_in_bytes) ,.cmd(msg_in_cmd) ,.data(msg_in_data));

wire [415:0] hcmd;
hexdigits #(2,1) hcmd_builder (.infield(msg_in_cmd),.outchar(hcmd[7:0]));
assign hcmd[15:8] = 8'h20;
hexdigits #(TWID,2) htags_builder (.infield(msg_in_tags),.outchar(hcmd[31:16]));
assign hcmd[39:32] = 8'h20;
hexdigits #(BWID,2) hbyts_builder (.infield(msg_in_bytes),.outchar(hcmd[55:40]));

assign hcmd[63:56] = 8'h20;
hexdigits #(AWID,8) haddr_builder (.infield(msg_in_addr),.outchar(hcmd[127:64]));
assign hcmd[135:128] = 8'h20;
hexdigits #(32,8) hdata0_builder (.infield(msg_in_data[127:96]),.outchar(hcmd[199:136]));
assign hcmd[207:200] = 8'h20;
hexdigits #(32,8) hdata1_builder (.infield(msg_in_data[95:64]),.outchar(hcmd[271:208]));
assign hcmd[279:272] = 8'h20;
hexdigits #(32,8) hdata2_builder (.infield(msg_in_data[63:32]),.outchar(hcmd[343:280]));
assign hcmd[351:344] = 8'h20;
hexdigits #(32,8) hdata3_builder (.infield(msg_in_data[31:0]),.outchar(hcmd[415:352]));


reg msg_in_active;
reg [5:0] msg_cnt;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        msg_in_active <= 1'b0;
        msg_cnt <= 0;
    end else begin
        if (!msg_in_active &&  !in_msg_fifo_empty) begin
            msg_in_active<=1'b1;
            msg_cnt <= 1'b0;
        end else if (msg_in_active) begin
            if (!tx_fifo_full) begin
                if (msg_cnt==52) begin
                    msg_cnt <=0;
                    msg_in_active<=1'b0;
                end else msg_cnt <= msg_cnt + 1'b1;
            end
        end
    end
end

assign take_msg_in = (msg_cnt==52) && !tx_fifo_full && msg_in_active;
wire [7:0] msg_in_txdata = (msg_cnt==52) ? 8'ha : (hcmd >> (msg_cnt*8));
wire [7:0] txdata_for_fifo = msg_in_active ? msg_in_txdata : 0;
wire txdata_write = msg_in_active;

wire tx_fifo_full,tx_fifo_empty;
syncfifo #(8,60) txdata_fifo (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(txdata_write),.datain(txdata_for_fifo)
    ,.full(tx_fifo_full),.empty(tx_fifo_empty),.overflow(),.count()
    ,.readout(tx_empty),.dataout(txdata)
);

assign write_tx = !tx_fifo_empty;

wire [7:0] rxdata_raw;
wire rxfifo_readout = 1'b0;

syncfifo #(8,60) rxdata_fifo (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(rx_valid),.datain(rxdata)
    ,.full(rx_fifo_full),.empty(rx_fifo_empty),.overflow(),.count()
    ,.readout(rxfifo_readout),.dataout(rxdata_raw)
);

endmodule




