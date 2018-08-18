

module rou_changeclk 


 #(
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
     input clka, input rsta_n
    ,input clkb, input rstb_n
    ,input  [WID-1:0] roua_in, input roua_in_seen, output [2:0] acka_in
    ,output [WID-1:0] roub_out, output roub_out_seen,  input [2:0] ackb_out
);

wire wfull,rempty;
wire [WID:0] rdata;

wire msgin_valid = roua_in[1:0]!=2'b0;
wire readx = (ackb_out!=0) && !rempty;
assign acka_in = wfull ? 0 : 1;

async4fifo #(.WID(WID+1)) async4fifo (
     .wclk(clka),.rst_n(rsta_n),.writex(msgin_valid),.wdata({roua_in_seen,roua_in}),.wfull(wfull)
    ,.rclk(clkb),.readx(readx),.rempty(rempty),.rdata(rdata)
);

assign {roub_out_seen,roub_out} = rempty ? {(WID+1){1'b0}} : rdata;

endmodule




