

module rou_switch5 #(parameter DWID=128, parameter AWID=32, parameter CWID=8,parameter WID = 2+DWID+AWID+CWID) (
    input clk, input rst_n
    ,input  [WID-1:0] rou0_in, output reg [2:0] ack0_in
    ,output reg [WID-1:0] rou0_out, input [2:0] ack0_out

    ,input  [WID-1:0] rou1_in, output reg [2:0] ack1_in
    ,output reg [WID-1:0] rou1_out, input [2:0] ack1_out

    ,input  [WID-1:0] rou2_in, output reg [2:0] ack2_in
    ,output reg [WID-1:0] rou2_out, input [2:0] ack2_out

    ,input  [WID-1:0] rou3_in, output reg [2:0] ack3_in
    ,output reg [WID-1:0] rou3_out, input [2:0] ack3_out

    ,input  [WID-1:0] rou4_in, output reg [2:0] ack4_in
    ,output reg [WID-1:0] rou4_out, input [2:0] ack4_out
);

initial begin
    ack0_in <= 0; rou0_out <= 0;
    ack1_in <= 0; rou1_out <= 0;
    ack2_in <= 0; rou2_out <= 0;
    ack3_in <= 0; rou3_out <= 0;
    ack4_in <= 0; rou4_out <= 0;
end



endmodule
