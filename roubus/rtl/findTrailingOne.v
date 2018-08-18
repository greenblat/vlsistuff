



module findTrailingOne ( input [31:0] ain,output [5:0] out, output [31:0] outbits);

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

wire [7:0] bytex = act0 ? ain[7:0] : act1 ? ain[15:8] : act2 ? ain[23:16] : ain[31:24];

assign out[2:0] =
    bytex[0] ? 3'b000 :
    bytex[1] ? 3'b001 : 
    bytex[2] ? 3'b010 :
    bytex[3] ? 3'b011 :
    bytex[4] ? 3'b100 :
    bytex[5] ? 3'b101 :
    bytex[6] ? 3'b110 :
    bytex[7] ? 3'b111 :
    3'b111;

assign outbits = (ain==0) ? 0 : (ain & ~(1<<out));


endmodule


