



module findLeadingOne ( input [31:0] ain,output [5:0] out, output [31:0] outbits);

wire act3 = ain[31:24]!=0;
wire act2 = ain[23:16]!=0;
wire act1 = ain[15:8]!=0;
wire act0 = ain[7:0]!=0;


assign out[5:3] = 
    act0 ? 3'b000 :
    act1 ? 3'b001 :
    act2 ? 3'b010 :
    act3 ? 3'b011 :
    3'b111
    ;

wire [7:0] bytex = act3 ? ain[31:24] : act2 ? ain[23:16] : act1 ? ain[15:8] : ain[7:0];

assign out[2:0] =
    bytex[7] ? 3'b111 :
    bytex[6] ? 3'b110 :
    bytex[5] ? 3'b101 :
    bytex[4] ? 3'b100 :
    bytex[3] ? 3'b011 :
    bytex[2] ? 3'b010 :
    bytex[1] ? 3'b001 : 
    bytex[0] ? 3'b000 :
    3'b111;

assign outbits = (out==6'b111111) ? 0 : (1<<out);


endmodule


