
module rou_msg_fields #(
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
     input [WID-1:0] msg
    ,output [DWID-1:0] data
    ,output [AWID-1:0] addr
    ,output [BWID-1:0] bytes
    ,output [TWID-1:0] tags
    ,output [1:0] cmd

);

assign {data[DWID-1:0],addr[AWID-1:0],bytes[BWID-1:0],tags[TWID-1:0],cmd[1:0]} = msg;



endmodule

