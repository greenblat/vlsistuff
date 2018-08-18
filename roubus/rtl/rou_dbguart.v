


module rou_dbguart #(
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
    input clk, input rst_n ,input rxd, output txd
    ,input rou_in_seen, output rou_out_seen
    ,input [WID-1:0] rou_in, output [2:0] ack_in 
    ,output [WID-1:0] rou_out, input [2:0] ack_out

);


wire [31:0] pages = 1;
wire [31:0] whoami = 32'hdbcf0123;


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



wire write_tx;
wire rx_valid;
wire tx_empty;


wire [7:0] txdata,rxdata,status,uart_control;
wire [15:0] baudrate;

uartx2 uartx2 (
   .clk(clk)
  ,.nreset(rst_n)
  ,.txd(txd)
  ,.rxd(rxd)

  ,.control(uart_control[7:0])
  ,.write_tx(write_tx)
  ,.read_rx(rx_valid)
  ,.rxdata(rxdata[7:0])
  ,.txdata(txdata[7:0])
  ,.tx_empty(tx_empty)
  ,.status(status[7:0])
  ,.baudrate(baudrate[15:0])
  ,.rx_valid(rx_valid)
);

dbguart_operator dbguart_operator (
    .clk(clk),.rst_n(rst_n)
    ,.control(control)
    ,.uart_control(uart_control)
   ,.write_tx(write_tx),.txdata(txdata),.tx_empty(tx_empty)
   ,.rx_valid(rx_valid),.rxdata(rxdata)
   ,.baudrate(baudrate),.status(status)

    ,.base_address(base_address)
    ,.msg_in(msg_in[(WID - 1):0])
    ,.msg_in_ack(msg_in_ack)
    ,.msg_out(msg_out[(WID - 1):0])
    ,.msg_out_ack(msg_out_ack)
);

endmodule

