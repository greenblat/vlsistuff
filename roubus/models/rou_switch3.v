

module rou_switch3 #(parameter DWID=128, parameter AWID=32, parameter CWID=8,parameter WID = 2+DWID+AWID+CWID) (
    input clk, input rst_n
    ,input  [WID-1:0] rou0_in, output reg [2:0] ack0_in
    ,output reg [WID-1:0] rou0_out, input [2:0] ack0_out

    ,input  [WID-1:0] rou1_in, output reg [2:0] ack1_in
    ,output reg [WID-1:0] rou1_out, input [2:0] ack1_out

    ,input  [WID-1:0] rou2_in, output reg [2:0] ack2_in
    ,output reg [WID-1:0] rou2_out, input [2:0] ack2_out
);

initial begin
    ack0_in <= 0; rou0_out <= 0;
    ack1_in <= 0; rou1_out <= 0;
    ack2_in <= 0; rou2_out <= 0;
end
reg [255:0] path;
reg [15:0] myid;
initial begin
    #1; 
    $swrite(path,"%m");
    myid = tb.idindex;
    tb.idindex = tb.idindex+1;
    tb.paths[myid] = path;
    $python("initial()",myid);
end

always @(negedge clk) begin
    if (rst_n==1) $python("work_ant()",myid,"switch3");
end




endmodule
