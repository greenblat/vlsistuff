module rou_align_buffer (
    input clk,input rst_n

    ,input [127:0]  indata
    ,input [4:0]    inbytes
    ,input invalid
    ,input softreset
    ,output intaken


    ,input reading
    ,input [4:0] reading_bytes
    ,input [3:0] wstrb_offset
    ,output [127:0] oline
    ,output [4:0] ovalids
);



reg [7:0] buf0 [0:63];
reg [6:0] wptra,rptra;
wire [5:0] wptr = wptra[5:0];
wire [5:0] rptr = rptra[5:0];
wire [6:0] count = (wptra>=rptra) ? (wptra-rptra) : (128-rptra+wptra);

assign ovalids = (count>=16) ? 16 : count;

wire [5:0] dst0 = rptr + 0;
wire [7:0] fifrd0 =  ((wstrb_offset>0)||(0>=count)) ? 0 : buf0[dst0];

wire [5:0] dst1 = rptr + 1 -wstrb_offset; wire [7:0] fifrd1 =  ((wstrb_offset>1)||((1-wstrb_offset)>=count)) ? 0 : buf0[dst1];
wire [5:0] dst2 = rptr + 2 -wstrb_offset; wire [7:0] fifrd2 =  ((wstrb_offset>2)||((2-wstrb_offset)>=count)) ? 0 : buf0[dst2];
wire [5:0] dst3 = rptr + 3 -wstrb_offset; wire [7:0] fifrd3 =  ((wstrb_offset>3)||((3-wstrb_offset)>=count)) ? 0 : buf0[dst3];
wire [5:0] dst4 = rptr + 4 -wstrb_offset; wire [7:0] fifrd4 =  ((wstrb_offset>4)||((4-wstrb_offset)>=count)) ? 0 : buf0[dst4];
wire [5:0] dst5 = rptr + 5 -wstrb_offset; wire [7:0] fifrd5 =  ((wstrb_offset>5)||((5-wstrb_offset)>=count)) ? 0 : buf0[dst5];
wire [5:0] dst6 = rptr + 6 -wstrb_offset; wire [7:0] fifrd6 =  ((wstrb_offset>6)||((6-wstrb_offset)>=count)) ? 0 : buf0[dst6];
wire [5:0] dst7 = rptr + 7 -wstrb_offset; wire [7:0] fifrd7 =  ((wstrb_offset>7)||((7-wstrb_offset)>=count)) ? 0 : buf0[dst7];
wire [5:0] dst8 = rptr + 8 -wstrb_offset; wire [7:0] fifrd8 =  ((wstrb_offset>8)||((8-wstrb_offset)>=count)) ? 0 : buf0[dst8];
wire [5:0] dst9 = rptr + 9 -wstrb_offset; wire [7:0] fifrd9 =  ((wstrb_offset>9)||((9-wstrb_offset)>=count)) ? 0 : buf0[dst9];

wire [5:0] dst10 = rptr + 10 -wstrb_offset; wire [7:0] fifrd10 =  ((wstrb_offset>10)||((10-wstrb_offset)>=count)) ? 0 : buf0[dst10];
wire [5:0] dst11 = rptr + 11 -wstrb_offset; wire [7:0] fifrd11 =  ((wstrb_offset>11)||((11-wstrb_offset)>=count)) ? 0 : buf0[dst11];
wire [5:0] dst12 = rptr + 12 -wstrb_offset; wire [7:0] fifrd12 =  ((wstrb_offset>12)||((12-wstrb_offset)>=count)) ? 0 : buf0[dst12];
wire [5:0] dst13 = rptr + 13 -wstrb_offset; wire [7:0] fifrd13 =  ((wstrb_offset>13)||((13-wstrb_offset)>=count)) ? 0 : buf0[dst13];
wire [5:0] dst14 = rptr + 14 -wstrb_offset; wire [7:0] fifrd14 =  ((wstrb_offset>14)||((14-wstrb_offset)>=count)) ? 0 : buf0[dst14];
wire [5:0] dst15 = rptr + 15 -wstrb_offset; wire [7:0] fifrd15 =  ((wstrb_offset>15)||((15-wstrb_offset)>=count)) ? 0 : buf0[dst15];

wire [7:0] dbg0 = buf0[0];
wire [7:0] dbg1 = buf0[1];
wire [7:0] dbg2 = buf0[2];
wire [7:0] dbg3 = buf0[3];
wire [7:0] dbg4 = buf0[4];
wire [7:0] dbg5 = buf0[5];
wire [7:0] dbg6 = buf0[6];
wire [7:0] dbg7 = buf0[7];
wire [7:0] dbg8 = buf0[8];
wire [7:0] dbg9 = buf0[9];


assign oline =  {
     fifrd15,fifrd14,fifrd13,fifrd12
    ,fifrd11,fifrd10,fifrd9,fifrd8
    ,fifrd7,fifrd6,fifrd5,fifrd4
    ,fifrd3,fifrd2,fifrd1,fifrd0
};

assign intaken = ((16'b0 + inbytes + count) < 64);

integer ii;


wire [5:0] wptr1 =  wptr + 1;
wire [5:0] wptr2 =  wptr + 2;
wire [5:0] wptr3 =  wptr + 3;
wire [5:0] wptr4 =  wptr + 4;
wire [5:0] wptr5 =  wptr + 5;
wire [5:0] wptr6 =  wptr + 6;
wire [5:0] wptr7 =  wptr + 7;
wire [5:0] wptr8 =  wptr + 8;
wire [5:0] wptr9 =  wptr + 9;
wire [5:0] wptr10 =  wptr + 10;
wire [5:0] wptr11 =  wptr + 11;
wire [5:0] wptr12 =  wptr + 12;
wire [5:0] wptr13 =  wptr + 13;
wire [5:0] wptr14 =  wptr + 14;
wire [5:0] wptr15 =  wptr + 15;

always @(posedge clk ) begin
    if (!rst_n) begin
        wptra <= 0;
        rptra <= 0;
        for (ii=0;ii<64;ii=ii+1) buf0[ii]<=0;
    end else begin
        if (softreset && !invalid)  begin
            wptra<=0;
        end else if (invalid && intaken) begin
            wptra <= wptra + inbytes;
            if (inbytes>0) buf0[wptr]     <= indata[7:0];
            if (inbytes>1) buf0[wptr1]   <= indata[15:8];
            if (inbytes>2) buf0[wptr2]   <= indata[23:16];
            if (inbytes>3) buf0[wptr3]   <= indata[31:24];
            if (inbytes>4) buf0[wptr4]   <= indata[39:32];
            if (inbytes>5) buf0[wptr5]   <= indata[47:40];
            if (inbytes>6) buf0[wptr6]   <= indata[55:48];
            if (inbytes>7) buf0[wptr7]   <= indata[63:56];
            if (inbytes>8) buf0[wptr8]   <= indata[71:64];
            if (inbytes>9) buf0[wptr9]   <= indata[79:72];
            if (inbytes>10) buf0[wptr10] <= indata[87:80];
            if (inbytes>11) buf0[wptr11] <= indata[95:88];
            if (inbytes>12) buf0[wptr12] <= indata[103:96];
            if (inbytes>13) buf0[wptr13] <= indata[111:104];
            if (inbytes>14) buf0[wptr14] <= indata[119:112];
            if (inbytes>15) buf0[wptr15] <= indata[127:120];
        end
        if (softreset) begin
            rptra<=0;
            wptra<=0;
        end else if (reading && (reading_bytes <= count)) begin
            if (count==reading_bytes) begin
                rptra<=0;
                wptra<=0;
            end else begin
                rptra <= rptra + reading_bytes;
            end
        end 
    end
end


endmodule


