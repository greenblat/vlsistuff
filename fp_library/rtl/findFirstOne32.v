module findFirstOne32 (input [31:0] ain, output [4:0] most);
wire [31:0] most_wire = 
    (ain[31]) ? 31 : (ain[30]) ? 30 :
    (ain[29]) ? 29 : (ain[28]) ? 28 : (ain[27]) ? 27 :
    (ain[26]) ? 26 : (ain[25]) ? 25 : (ain[24]) ? 24 :
    (ain[23]) ? 23 : (ain[22]) ? 22 : (ain[21]) ? 21 : (ain[20]) ? 20 :
    (ain[19]) ? 19 : (ain[18]) ? 18 : (ain[17]) ? 17 :
    (ain[16]) ? 16 : (ain[15]) ? 15 : (ain[14]) ? 14 :
    (ain[13]) ? 13 : (ain[12]) ? 12 : (ain[11]) ? 11 : (ain[10]) ? 10 :
    (ain[9]) ? 9 : (ain[8]) ? 8 : (ain[7]) ? 7 :
    (ain[6]) ? 6 : (ain[5]) ? 5 : (ain[4]) ? 4 :
    (ain[3]) ? 3 : (ain[2]) ? 2 : (ain[1]) ? 1 : 0 ;
assign most = most_wire[4:0];
endmodule
