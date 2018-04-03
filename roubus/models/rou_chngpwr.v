

module rou_chngpwr #(parameter DWID=128, parameter AWID=32, parameter CWID=8,parameter WID = 2+DWID+AWID+CWID) (
    input clk0, input rst0_n
    ,input  [WID-1:0] rou0_in, output reg [2:0] ack0_in
    ,output reg [WID-1:0] rou0_out, input [2:0] ack0_out
    ,input otherside0_powered

    ,input clk1, input rst1_n
    ,input  [WID-1:0] rou1_in, output reg [2:0] ack1_in
    ,output reg [WID-1:0] rou1_out, input [2:0] ack1_out
    ,input otherside1_powered
);

initial begin
    ack0_in<=0;
    ack1_in<=0;
    rou0_out<=0;
    rou1_out<=0;
end


endmodule

