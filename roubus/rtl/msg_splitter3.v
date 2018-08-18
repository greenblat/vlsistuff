

module msg_splitter3 #(parameter WID=132) (
    input [WID-1:0] msgin, output msginack

    ,output [WID-1:0] msga ,output [WID-1:0] msgb ,output [WID-1:0] msgc
    ,input acka, input ackb, input ackc

    ,input [1:0] sel
    ,input [WID-1:0] default_option

);

assign msga = (sel==1) ? msgin : default_option;
assign msgb = (sel==2) ? msgin : default_option;
assign msgc = (sel==3) ? msgin : default_option;

assign msginack = (sel==1) ? acka : (sel==2) ? ackb :  (sel==3) ? ackc : 1'b0;


endmodule

