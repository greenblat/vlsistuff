
// Ilia Greenblat


module fp_over (input [31:0] ain, output [31:0] out);

wire [31:0] tmp;
wire [7:0] expo0 = ain[30:23]-127;
wire [7:0] expo1 = tmp[30:23]-127;
wire [7:0] expo = expo1-expo0+127;
assign out[31] = ain[31];
assign out[30:23] = (ain==0) ? 127 : expo;
assign out[22:0] = tmp[22:0];


invertab invertab (.ain(ain[22:13]),.out(tmp));

endmodule

