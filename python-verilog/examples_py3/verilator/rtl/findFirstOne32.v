module findFirstOne32 (input [31:0] src0, output [4:0] most);
wire [31:0] most_wire = 
    (src0[31]) ? 31 : (src0[30]) ? 30 :
    (src0[29]) ? 29 : (src0[28]) ? 28 : (src0[27]) ? 27 :
    (src0[26]) ? 26 : (src0[25]) ? 25 : (src0[24]) ? 24 :
    (src0[23]) ? 23 : (src0[22]) ? 22 : (src0[21]) ? 21 : (src0[20]) ? 20 :
    (src0[19]) ? 19 : (src0[18]) ? 18 : (src0[17]) ? 17 :
    (src0[16]) ? 16 : (src0[15]) ? 15 : (src0[14]) ? 14 :
    (src0[13]) ? 13 : (src0[12]) ? 12 : (src0[11]) ? 11 : (src0[10]) ? 10 :
    (src0[9]) ? 9 : (src0[8]) ? 8 : (src0[7]) ? 7 :
    (src0[6]) ? 6 : (src0[5]) ? 5 : (src0[4]) ? 4 :
    (src0[3]) ? 3 : (src0[2]) ? 2 : (src0[1]) ? 1 : 0 ;
assign most = most_wire[4:0];
endmodule
