

module ram_operator #(
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
     input clk, input rst_n
    ,input [31:0] control
    ,input [AWID-1:0] base_address
    ,input [WID-1:0] msg_in ,output reg msg_in_ack
    ,output reg [WID-1:0] msg_out ,input  msg_out_ack
    

);

initial begin
    msg_out = 0;
    msg_in_ack = 0;
end

integer myid;
reg [255:0] mypath;
initial begin
    #1;
   myid = tb.iid;
   $swrite(mypath,"%m");
   tb.iid = tb.iid + 1;
   $display("mypath %s %d",mypath,myid);
end

always @(negedge clk) begin
    $python("ram_operator()",myid,mypath);
end

endmodule

