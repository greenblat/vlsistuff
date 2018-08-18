
module msg_joiner3_narrow #(parameter WBUFS=6) (
    input [WBUFS-1:0] msga ,input [WBUFS-1:0] msgb,input [WBUFS-1:0] msgc
    ,output msga_ack, output msgb_ack,output msgc_ack

    ,output [WBUFS-1:0] msgout
    ,output [1:0] msgsrc
    ,input msgout_ack
);
parameter NOTLEGAL  =  (1<<WBUFS)-1;
assign msgout  = 
    (msga!=NOTLEGAL) ? msga :  
    (msgb!=NOTLEGAL) ? msgb : 
    (msgc!=NOTLEGAL) ? msgc : 
    NOTLEGAL;
assign msga_ack  = msgout_ack && (msga!=NOTLEGAL);
assign msgb_ack  = msgout_ack && (msga==NOTLEGAL) && (msgb!=NOTLEGAL);
assign msgc_ack  = msgout_ack && (msga==NOTLEGAL) && (msgb==NOTLEGAL) &&(msgc!=NOTLEGAL);
assign msgsrc = (msga!=NOTLEGAL) ? 1 :  (msgb!=NOTLEGAL) ? 2 : (msgc!=NOTLEGAL) ? 3 : 0 ;

endmodule

