
module rou_msg_build #(
     parameter DWID = 128
    ,parameter AWID = 32
    ,parameter TWID = 5 
    ,parameter BWID = 
        (DWID==512)  ? 6 : 
        (DWID==256)  ? 5 :
        (DWID==128) ? 4 : 
        (DWID==64)  ? 3 : 2 
    ,parameter WID = 2+DWID+AWID+BWID+TWID
)(
     output [WID-1:0] msg
    ,input [DWID-1:0] data
    ,input [AWID-1:0] addr
    ,input [BWID-1:0] bytes
    ,input [TWID-1:0] tags
    ,input [1:0] cmd

);

assign msg = {data[DWID-1:0],addr[AWID-1:0],bytes[BWID-1:0],tags[TWID-1:0],cmd[1:0]} ;



endmodule

