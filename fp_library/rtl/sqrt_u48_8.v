module sqrt_u48_8 (input clk, input rst_n,input [47:0] ain,output reg [23:0] out,input vldin,input en, output reg vldout);

wire [47:0] What0 = 48'h400000000000;
wire [47:0] AxA0 =  (What0<=ain) ? What0 : 0 ;
wire [23:0]  AA0  =  (What0<=ain) ? 24'h800000 : 0 ;

wire [47:0] What1 = 48'h100000000000;
wire [47:0] New1 = AxA0 + What1 + (AA0<<23);
wire [47:0] AxA1 = (New1<=ain) ? New1 : AxA0 ;
wire [23:0] AA1  = (New1<=ain) ? (AA0|24'h400000) : AA0 ;
wire [47:0] What2 = 48'h40000000000;
wire [47:0] wire_New2 = AxA1 + What2 + (AA1<<22);
wire [47:0] wire_AxA2 = (wire_New2<=ain) ? wire_New2 : AxA1 ;
wire [23:0] wire_AA2  = (wire_New2<=ain) ? (AA1|24'h200000) : AA1 ;
reg [47:0] AxA2,AA2; always @(posedge clk) begin AxA2<=wire_AxA2; AA2<=wire_AA2; end
reg [47:0] ain2;  always @(posedge clk) if (en) ain2 <= ain;
reg vld2;  always @(posedge clk) if (en) vld2 <= vldin;

wire [47:0] What3 = 48'h10000000000;
wire [47:0] New3 = AxA2 + What3 + (AA2<<21);
wire [47:0] AxA3 = (New3<=ain2) ? New3 : AxA2 ;
wire [23:0] AA3  = (New3<=ain2) ? (AA2|24'h100000) : AA2 ;
wire [47:0] What4 = 48'h4000000000;
wire [47:0] New4 = AxA3 + What4 + (AA3<<20);
wire [47:0] AxA4 = (New4<=ain2) ? New4 : AxA3 ;
wire [23:0] AA4  = (New4<=ain2) ? (AA3|24'h80000) : AA3 ;
wire [47:0] What5 = 48'h1000000000;
wire [47:0] wire_New5 = AxA4 + What5 + (AA4<<19);
wire [47:0] wire_AxA5 = (wire_New5<=ain2) ? wire_New5 : AxA4 ;
wire [23:0] wire_AA5  = (wire_New5<=ain2) ? (AA4|24'h40000) : AA4 ;
reg [47:0] AxA5,AA5; always @(posedge clk) begin AxA5<=wire_AxA5; AA5<=wire_AA5; end
reg [47:0] ain5;  always @(posedge clk) if (en) ain5 <= ain2;
reg vld5;  always @(posedge clk) if (en) vld5 <= vld2;

wire [47:0] What6 = 48'h400000000;
wire [47:0] New6 = AxA5 + What6 + (AA5<<18);
wire [47:0] AxA6 = (New6<=ain5) ? New6 : AxA5 ;
wire [23:0] AA6  = (New6<=ain5) ? (AA5|24'h20000) : AA5 ;
wire [47:0] What7 = 48'h100000000;
wire [47:0] New7 = AxA6 + What7 + (AA6<<17);
wire [47:0] AxA7 = (New7<=ain5) ? New7 : AxA6 ;
wire [23:0] AA7  = (New7<=ain5) ? (AA6|24'h10000) : AA6 ;
wire [47:0] What8 = 48'h40000000;
wire [47:0] wire_New8 = AxA7 + What8 + (AA7<<16);
wire [47:0] wire_AxA8 = (wire_New8<=ain5) ? wire_New8 : AxA7 ;
wire [23:0] wire_AA8  = (wire_New8<=ain5) ? (AA7|24'h8000) : AA7 ;
reg [47:0] AxA8,AA8; always @(posedge clk) begin AxA8<=wire_AxA8; AA8<=wire_AA8; end
reg [47:0] ain8;  always @(posedge clk) if (en) ain8 <= ain5;
reg vld8;  always @(posedge clk) if (en) vld8 <= vld5;

wire [47:0] What9 = 48'h10000000;
wire [47:0] New9 = AxA8 + What9 + (AA8<<15);
wire [47:0] AxA9 = (New9<=ain8) ? New9 : AxA8 ;
wire [23:0] AA9  = (New9<=ain8) ? (AA8|24'h4000) : AA8 ;
wire [47:0] What10 = 48'h4000000;
wire [47:0] New10 = AxA9 + What10 + (AA9<<14);
wire [47:0] AxA10 = (New10<=ain8) ? New10 : AxA9 ;
wire [23:0] AA10  = (New10<=ain8) ? (AA9|24'h2000) : AA9 ;
wire [47:0] What11 = 48'h1000000;
wire [47:0] wire_New11 = AxA10 + What11 + (AA10<<13);
wire [47:0] wire_AxA11 = (wire_New11<=ain8) ? wire_New11 : AxA10 ;
wire [23:0] wire_AA11  = (wire_New11<=ain8) ? (AA10|24'h1000) : AA10 ;
reg [47:0] AxA11,AA11; always @(posedge clk) begin AxA11<=wire_AxA11; AA11<=wire_AA11; end
reg [47:0] ain11;  always @(posedge clk) if (en) ain11 <= ain8;
reg vld11;  always @(posedge clk) if (en) vld11 <= vld8;

wire [47:0] What12 = 48'h400000;
wire [47:0] New12 = AxA11 + What12 + (AA11<<12);
wire [47:0] AxA12 = (New12<=ain11) ? New12 : AxA11 ;
wire [23:0] AA12  = (New12<=ain11) ? (AA11|24'h800) : AA11 ;
wire [47:0] What13 = 48'h100000;
wire [47:0] New13 = AxA12 + What13 + (AA12<<11);
wire [47:0] AxA13 = (New13<=ain11) ? New13 : AxA12 ;
wire [23:0] AA13  = (New13<=ain11) ? (AA12|24'h400) : AA12 ;
wire [47:0] What14 = 48'h40000;
wire [47:0] wire_New14 = AxA13 + What14 + (AA13<<10);
wire [47:0] wire_AxA14 = (wire_New14<=ain11) ? wire_New14 : AxA13 ;
wire [23:0] wire_AA14  = (wire_New14<=ain11) ? (AA13|24'h200) : AA13 ;
reg [47:0] AxA14,AA14; always @(posedge clk) begin AxA14<=wire_AxA14; AA14<=wire_AA14; end
reg [47:0] ain14;  always @(posedge clk) if (en) ain14 <= ain11;
reg vld14;  always @(posedge clk) if (en) vld14 <= vld11;

wire [47:0] What15 = 48'h10000;
wire [47:0] New15 = AxA14 + What15 + (AA14<<9);
wire [47:0] AxA15 = (New15<=ain14) ? New15 : AxA14 ;
wire [23:0] AA15  = (New15<=ain14) ? (AA14|24'h100) : AA14 ;
wire [47:0] What16 = 48'h4000;
wire [47:0] New16 = AxA15 + What16 + (AA15<<8);
wire [47:0] AxA16 = (New16<=ain14) ? New16 : AxA15 ;
wire [23:0] AA16  = (New16<=ain14) ? (AA15|24'h80) : AA15 ;
wire [47:0] What17 = 48'h1000;
wire [47:0] wire_New17 = AxA16 + What17 + (AA16<<7);
wire [47:0] wire_AxA17 = (wire_New17<=ain14) ? wire_New17 : AxA16 ;
wire [23:0] wire_AA17  = (wire_New17<=ain14) ? (AA16|24'h40) : AA16 ;
reg [47:0] AxA17,AA17; always @(posedge clk) begin AxA17<=wire_AxA17; AA17<=wire_AA17; end
reg [47:0] ain17;  always @(posedge clk) if (en) ain17 <= ain14;
reg vld17;  always @(posedge clk) if (en) vld17 <= vld14;

wire [47:0] What18 = 48'h400;
wire [47:0] New18 = AxA17 + What18 + (AA17<<6);
wire [47:0] AxA18 = (New18<=ain17) ? New18 : AxA17 ;
wire [23:0] AA18  = (New18<=ain17) ? (AA17|24'h20) : AA17 ;
wire [47:0] What19 = 48'h100;
wire [47:0] New19 = AxA18 + What19 + (AA18<<5);
wire [47:0] AxA19 = (New19<=ain17) ? New19 : AxA18 ;
wire [23:0] AA19  = (New19<=ain17) ? (AA18|24'h10) : AA18 ;
wire [47:0] What20 = 48'h40;
wire [47:0] wire_New20 = AxA19 + What20 + (AA19<<4);
wire [47:0] wire_AxA20 = (wire_New20<=ain17) ? wire_New20 : AxA19 ;
wire [23:0] wire_AA20  = (wire_New20<=ain17) ? (AA19|24'h8) : AA19 ;
reg [47:0] AxA20,AA20; always @(posedge clk) begin AxA20<=wire_AxA20; AA20<=wire_AA20; end
reg [47:0] ain20;  always @(posedge clk) if (en) ain20 <= ain17;
reg vld20;  always @(posedge clk) if (en) vld20 <= vld17;

wire [47:0] What21 = 48'h10;
wire [47:0] New21 = AxA20 + What21 + (AA20<<3);
wire [47:0] AxA21 = (New21<=ain20) ? New21 : AxA20 ;
wire [23:0] AA21  = (New21<=ain20) ? (AA20|24'h4) : AA20 ;
wire [47:0] What22 = 48'h4;
wire [47:0] New22 = AxA21 + What22 + (AA21<<2);
wire [47:0] AxA22 = (New22<=ain20) ? New22 : AxA21 ;
wire [23:0] AA22  = (New22<=ain20) ? (AA21|24'h2) : AA21 ;
wire [47:0] What23 = 48'h1;
wire [47:0] New23 = AxA22 + What23 + (AA22<<1);
wire [47:0] AxA23 = (New23<=ain20) ? New23 : AxA22 ;
wire [23:0] AA23  = (New23<=ain20) ? (AA22|24'h1) : AA22 ;

always @(posedge clk)  out <= AA23;
always @(posedge clk)  vldout <= vld20;
endmodule
