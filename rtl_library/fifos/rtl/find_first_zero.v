
module find_first_zero ( input [31:0] din, output [5:0] dout);

assign dout = 

    !din[0] ? 0 :

    !din[1] ? 1 :

    !din[2] ? 2 :

    !din[3] ? 3 :

    !din[4] ? 4 :

    !din[5] ? 5 :

    !din[6] ? 6 :

    !din[7] ? 7 :

    !din[8] ? 8 :

    !din[9] ? 9 :

    !din[10] ? 10 :

    !din[11] ? 11 :

    !din[12] ? 12 :

    !din[13] ? 13 :

    !din[14] ? 14 :

    !din[15] ? 15 :

    !din[16] ? 16 :

    !din[17] ? 17 :

    !din[18] ? 18 :

    !din[19] ? 19 :

    !din[20] ? 20 :

    !din[21] ? 21 :

    !din[22] ? 22 :

    !din[23] ? 23 :

    !din[24] ? 24 :

    !din[25] ? 25 :

    !din[26] ? 26 :

    !din[27] ? 27 :

    !din[28] ? 28 :

    !din[29] ? 29 :

    !din[30] ? 30 :

    !din[31] ? 31 :

    6'b100000 ; 


wire [63:0]  sign_version = 64'h000085c814240424 ;
endmodule

