

module rou_admin #(parameter DWID=128, parameter AWID=32, parameter CWID=8,parameter WID = 2+DWID+AWID+CWID) (
    input clk, input rst_n
    ,input  [WID-1:0] rou_in, output reg [2:0] ack_in
    ,output reg [WID-1:0] rou_out, input [2:0] ack_out


    ,output reg [WID-1:0] msg_in
    ,input  msg_in_ack

    ,output reg [7:0] resp_count
    ,output reg [63:0] resp_data
    ,input  resp_read

);

reg [255:0] path;
reg [15:0] myid;
initial begin
    msg_in<=0;
    ack_in <= 0;
    rou_out <= 0;

    resp_count<=0;
    resp_data<=0;

    #1;

    $swrite(path,"%m");
    myid = tb.idindex;
    tb.idindex = tb.idindex+1;
    tb.paths[myid] = path;
    $python("initial()",myid);
end


always @(negedge clk) begin
    if (rst_n==1) $python("work_ant()",myid,"admin");
end



endmodule
