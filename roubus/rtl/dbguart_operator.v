

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
     input clk, input rst_n 
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




assign txdata = 0;
assign read_rx = 0;
assign write_tx = 0;
assign msg_in_ack = 1;
assign msg_out  = 0;



endmodule




