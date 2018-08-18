
module msg_joiner3_wide #(parameter WID=132) (
    input [WID-1:0] msga ,input [WID-1:0] msgb,input [WID-1:0] msgc
    ,output msga_ack, output msgb_ack, output msgc_ack

    ,output [WID-1:0] msgout
    ,input msgout_ack
);

assign msgout  = 
    msgValid(msga) ? msga :  
    msgValid(msgb) ? msgb :  
    msgValid(msgc) ? msgc :  
    {WID{1'b0}};

assign msga_ack  = msgout_ack && msgValid(msga);
assign msgb_ack  = msgout_ack && msgValid(msgb) && !msgValid(msga);
assign msgc_ack  = msgout_ack && msgValid(msgc) && !msgValid(msgb) && !msgValid(msga);

endmodule

