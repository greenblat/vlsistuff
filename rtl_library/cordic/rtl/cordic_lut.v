
// 32 positions, 45 degress == 0x10000000
// for lesser resiltion, shift the output left (regular shift, not arith)
// output (lut) is 32 bits.

module cordic_lut ( input [4:0] pos, output [31:0] lut);
assign lut = 
     (pos==0) ? 268435456 :
     (pos==1) ? 158466702 :
     (pos==2) ? 83729453 :
     (pos==3) ? 42502378 :
     (pos==4) ? 21333665 :
     (pos==5) ? 10677232 :
     (pos==6) ? 5339919 :
     (pos==7) ? 2670122 :
     (pos==8) ? 1335081 :
     (pos==9) ? 667543 :
     (pos==10) ? 333772 :
     (pos==11) ? 166886 :
     (pos==12) ? 83443 :
     (pos==13) ? 41721 :
     (pos==14) ? 20860 :
     (pos==15) ? 10430 :
     (pos==16) ? 5215 :
     (pos==17) ? 2607 :
     (pos==18) ? 1303 :
     (pos==19) ? 651 :
     (pos==20) ? 325 :
     (pos==21) ? 162 :
     (pos==22) ? 81 :
     (pos==23) ? 40 :
     (pos==24) ? 20 :
     (pos==25) ? 10 :
     (pos==26) ? 5 :
     (pos==27) ? 2 :
     (pos==28) ? 1 :
     (pos==29) ? 0 :
     (pos==30) ? 0 :
     (pos==31) ? 0 :
    0;
endmodule
