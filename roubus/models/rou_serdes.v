

module rou_serdes #(parameter SERWID=4,parameter DWID=128, parameter AWID=32, parameter CWID=8,parameter WID = 2+DWID+AWID+CWID) (
    input clk, input rst_n
    ,input  [WID-1:0] rou_in, output reg [2:0] ack_in
    ,output reg [WID-1:0] rou_out, input [2:0] ack_out


    ,output reg [SERWID-1:0] serout
    ,input [SERWID-1:0] serin
    ,input serclk    // fast clock for serial link


);

initial begin
    ack_in <= 0;
    rou_out <= 0;
    serout<=0;
end



endmodule
