

module rou_availables #(parameter BUFS=8,parameter WBUFS=6) (
    input [BUFS-1:0] occupied
    ,output [WBUFS-1:0] free0indx
    ,output [WBUFS-1:0] free1indx
    ,output [WBUFS-1:0] free2indx
    ,output [WBUFS-1:0] availables
);

wire [31:0] tmp =  {32'b0,~occupied};

wire [31:0] taken0,taken1,taken2;
findTrailingOne frees0(.ain(tmp),.out(free0indx),.outbits(taken0));
findTrailingOne frees1(.ain(taken0),.out(free1indx),.outbits(taken1));
findTrailingOne frees2(.ain(taken1),.out(free2indx),.outbits(taken2));


assign availables  =  0 
    +taken2[0] +taken2[1] +taken2[2] +taken2[3] +taken2[4] +taken2[5] +taken2[6] +taken2[7] +taken2[8] +taken2[9]
    +taken2[10] +taken2[11] +taken2[12] +taken2[13] +taken2[14] +taken2[15] +taken2[16] +taken2[17] +taken2[18] +taken2[19]
    +taken2[20] +taken2[21] +taken2[22] +taken2[23] +taken2[24] +taken2[25] +taken2[26] +taken2[27] +taken2[28] +taken2[29]
    +taken2[30] +taken2[31];
endmodule





