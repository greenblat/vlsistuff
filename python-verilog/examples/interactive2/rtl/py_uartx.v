module py_uartx2 (
     input [15:0] baudrate
    ,input    clk
    ,input [7:0] control
    ,input    rst_n
    ,input    read_rx
    ,input    rxd
    ,input [7:0] txdata
    ,input    write_tx
    ,output reg    rx_valid
    ,output reg [7:0] rxdata
    ,output reg [7:0] status
    ,output reg    tx_empty
    ,output reg    txd
);
initial begin
    rx_valid = 0;
    rxdata = 0;
    status = 0;
    tx_empty = 0;
    txd = 0;
end
endmodule
