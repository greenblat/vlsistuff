

module rou_nif #(parameter DWID=128, parameter AWID=32, parameter CWID=8,parameter WID = 2+DWID+AWID+CWID) (
    input clk, input rst_n
    ,input  [WID-1:0] rou_in, output reg [2:0] ack_in
    ,output reg [WID-1:0] rou_out, input [2:0] ack_out

    ,input [15:0] uses_pages

    ,input [WID-1:0] msg_out
    ,output reg msg_out_ack

    ,output reg [WID-1:0] msg_in
    ,input  msg_in_ack
);

initial begin
    msg_out_ack<=0;
    msg_in<=0;
    ack_in <= 0;
    rou_out <= 0;
end



endmodule
