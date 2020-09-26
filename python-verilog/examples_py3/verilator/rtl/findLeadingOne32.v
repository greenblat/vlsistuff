module findLeadingOne32 ( input [31:0] src0,output [4:0] out);
wire act3 = src0[31:24]!=0;
wire act2 = src0[23:16]!=0;
wire act1 = src0[15:8]!=0;
assign out[4:3] = act3 ? 2'b11 : act2 ? 2'b10 : act1 ? 2'b01 : 2'b00;
wire [7:0] bytex = act3 ? src0[31:24] : act2 ? src0[23:16] : act1 ? src0[15:8] : src0[7:0]; 
assign out[2:0] = 
    bytex[7] ? 3'b111 :
    bytex[6] ? 3'b110 :
    bytex[5] ? 3'b101 :
    bytex[4] ? 3'b100 :
    bytex[3] ? 3'b011 :
    bytex[2] ? 3'b010 :
    bytex[1] ? 3'b001 : 3'b000 ;
endmodule
