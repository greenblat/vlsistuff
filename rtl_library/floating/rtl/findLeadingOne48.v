module findLeadingOne48 ( input [47:0] ain,output [5:0] out);
wire act5 = ain[47:40]!=0;
wire act4 = ain[39:32]!=0;
wire act3 = ain[31:24]!=0;
wire act2 = ain[23:16]!=0;
wire act1 = ain[15:8]!=0;
assign out[5:3] = act5 ? 3'd5 : act4 ? 3'd4 : act3 ? 3'd3 : act2 ? 3'd2 : act1 ? 3'd1 : 3'd0;
wire [7:0] bytex = 
    act5 ? ain[47:40] : 
    act4 ? ain[39:32] : 
    act3 ? ain[31:24] : 
    act2 ? ain[23:16] : 
    act1 ? ain[15:8] : ain[7:0]; 
assign out[2:0] = 
    bytex[7] ? 3'b111 :
    bytex[6] ? 3'b110 :
    bytex[5] ? 3'b101 :
    bytex[4] ? 3'b100 :
    bytex[3] ? 3'b011 :
    bytex[2] ? 3'b010 :
    bytex[1] ? 3'b001 : 3'b000 ;
endmodule
