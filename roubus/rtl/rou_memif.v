

module rou_memif #(parameter DWID=128, parameter AWID=32, parameter CWID=8,parameter WID = 2+DWID+AWID+CWID,
    parameter WSTRB = DWID/8
) (
    input clk, input rst_n


    ,output [WID-1:0] msg_out
    ,input msg_out_ack

    ,input [WID-1:0] msg_in
    ,output reg  msg_in_ack

 // local memory interface
    ,output reg local_wr ,output reg local_rd
    ,output reg [31:0] local_addr
    ,output reg [DWID-1:0] local_wr_data
    ,output reg [WSTRB-1:0] local_wstrb
    ,input  local_wr_ok
    ,input  local_wr_error

    ,input [127:0] local_rd_data
    ,input  local_rd_addr_ok
    ,input  local_rd_data_ok
    ,input  local_rd_error

);

syncfifo didox();



initial begin
    local_wr <= 0 ;
    local_rd <= 0;
    local_addr <= 0;
    local_wr_data <= 0;
    local_wstrb <= 0;
end



endmodule


