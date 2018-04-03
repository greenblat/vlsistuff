

module rou_chngwid #(parameter DWID0=128, parameter DWID1=64, parameter AWID=32, parameter CWID0=8,
    parameter WID0 = 2+DWID0+AWID+CWID0, 
    parameter WID1 = 2+DWID1+AWID+CWID0-1
) (
    input clk, input rst_n
    ,input  [WID0-1:0] rou0_in, output reg [2:0] ack0_in
    ,output reg [WID0-1:0] rou0_out, input [2:0] ack0_out

    ,input  [WID1-1:0] rou1_in, output reg [2:0] ack1_in
    ,output reg [WID1-1:0] rou1_out, input [2:0] ack1_out
);

initial begin
    ack0_in<=0;
    ack1_in<=0;
    rou0_out<=0;
    rou1_out<=0;
end


endmodule

