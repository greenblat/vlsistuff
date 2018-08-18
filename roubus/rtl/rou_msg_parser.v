
module rou_msg_parser #(
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
    ,output msg_enumerate
    ,output msg_reset
    ,output msg_controls
    ,output msg_report
    ,output msg_mngresponce
    ,output msg_mngrequest
    ,output msg_bad
);

wire [DWID-1:0] data;
wire [AWID-1:0] addr;
wire [BWID-1:0] bytes;
wire [TWID-1:0] tags;
wire [1:0] cmd;

rou_msg_fields msg_fields(.msg(msg), .addr(addr) ,.tags(tags) ,.bytes(bytes) ,.cmd(cmd) ,.data(data));

wire management = cmd==2'b11;

parameter MSG_RESET = 0;
parameter MSG_ENUMERATE = 2;
parameter MSG_CONTROL = 4;
parameter MSG_REPORT = 6;

assign msg_reset = management&&(tags==MSG_RESET);
assign msg_enumerate = management&&(tags==MSG_ENUMERATE);
assign msg_controls = management&&(tags==MSG_CONTROL);
assign msg_report = management&&(tags==MSG_REPORT);
assign msg_mngresponce = management&&tags[0];
assign msg_mngrequest = management&&!tags[0];

assign msg_bad = management && !(msg_reset || msg_enumerate || msg_controls || msg_controls);

endmodule

