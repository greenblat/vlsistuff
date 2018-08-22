
module hexdigits #(parameter WBITS=8, parameter CHARS=2) ( input [WBITS-1:0] infield, output [CHARS*8-1:0] outchar);




wire [31:0] fatvector = 32'b0 | infield;

wire [63:0] manychars;

assign manychars[7:0]   = onehex(fatvector[3:0]);
assign manychars[15:8]  = onehex(fatvector[7:4]);
assign manychars[23:16] = onehex(fatvector[11:8]);
assign manychars[31:24] = onehex(fatvector[15:12]);
assign manychars[39:32] = onehex(fatvector[19:16]);
assign manychars[47:40] = onehex(fatvector[23:20]);
assign manychars[55:48] = onehex(fatvector[27:24]);
assign manychars[63:56] = onehex(fatvector[31:28]);


assign outchar = manychars[8*CHARS-1:0];


function [7:0] onehex( input [3:0] inx);
begin
    if (inx==0) onehex = 8'h30;
    else if (inx==1) onehex = 8'h31;
    else if (inx==2) onehex = 8'h32;
    else if (inx==3) onehex = 8'h33;
    else if (inx==4) onehex = 8'h34;
    else if (inx==5) onehex = 8'h35;
    else if (inx==6) onehex = 8'h36;
    else if (inx==7) onehex = 8'h37;
    else if (inx==8) onehex = 8'h38;
    else if (inx==9) onehex = 8'h39;
    else if (inx==10) onehex = 8'h61;
    else if (inx==11) onehex = 8'h62;
    else if (inx==12) onehex = 8'h63;
    else if (inx==13) onehex = 8'h64;
    else if (inx==14) onehex = 8'h65;
    else if (inx==15) onehex = 8'h66;
    else onehex = 8'bx;
end
endfunction



endmodule

