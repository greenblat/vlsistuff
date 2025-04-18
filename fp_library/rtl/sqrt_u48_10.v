module sqrt_u48_10 (input clk, input rst_n,input [47:0] ain,output reg [23:0] out,input vldin,input en, output reg vldout);

wire [47:0] What0 = 48'h400000000000;
wire [47:0] AxA0 =  (What0<=ain) ? What0 : 0 ;
wire [23:0]  AA0  =  (What0<=ain) ? 24'h800000 : 0 ;

wire [47:0] What1 = 48'h100000000000;
wire [47:0] wire_New1 = AxA0 + What1 + (AA0<<23);
wire [47:0] wire_AxA1 = (wire_New1<=ain) ? wire_New1 : AxA0 ;
wire [23:0] wire_AA1  = (wire_New1<=ain) ? (AA0|24'h400000) : AA0 ;
reg [47:0] AxA1,AA1; always @(posedge clk) begin AxA1<=wire_AxA1; AA1<=wire_AA1; end
reg [47:0] ain1;  always @(posedge clk) if (en) ain1 <= ain;
reg vld1;  always @(posedge clk) if (en) vld1 <= vldin;

wire [47:0] What2 = 48'h40000000000;
wire [47:0] New2 = AxA1 + What2 + (AA1<<22);
wire [47:0] AxA2 = (New2<=ain1) ? New2 : AxA1 ;
wire [23:0] AA2  = (New2<=ain1) ? (AA1|24'h200000) : AA1 ;
wire [47:0] What3 = 48'h10000000000;
wire [47:0] wire_New3 = AxA2 + What3 + (AA2<<21);
wire [47:0] wire_AxA3 = (wire_New3<=ain1) ? wire_New3 : AxA2 ;
wire [23:0] wire_AA3  = (wire_New3<=ain1) ? (AA2|24'h100000) : AA2 ;
reg [47:0] AxA3,AA3; always @(posedge clk) begin AxA3<=wire_AxA3; AA3<=wire_AA3; end
reg [47:0] ain3;  always @(posedge clk) if (en) ain3 <= ain1;
reg vld3;  always @(posedge clk) if (en) vld3 <= vld1;

wire [47:0] What4 = 48'h4000000000;
wire [47:0] New4 = AxA3 + What4 + (AA3<<20);
wire [47:0] AxA4 = (New4<=ain3) ? New4 : AxA3 ;
wire [23:0] AA4  = (New4<=ain3) ? (AA3|24'h80000) : AA3 ;
wire [47:0] What5 = 48'h1000000000;
wire [47:0] wire_New5 = AxA4 + What5 + (AA4<<19);
wire [47:0] wire_AxA5 = (wire_New5<=ain3) ? wire_New5 : AxA4 ;
wire [23:0] wire_AA5  = (wire_New5<=ain3) ? (AA4|24'h40000) : AA4 ;
reg [47:0] AxA5,AA5; always @(posedge clk) begin AxA5<=wire_AxA5; AA5<=wire_AA5; end
reg [47:0] ain5;  always @(posedge clk) if (en) ain5 <= ain3;
reg vld5;  always @(posedge clk) if (en) vld5 <= vld3;

wire [47:0] What6 = 48'h400000000;
wire [47:0] New6 = AxA5 + What6 + (AA5<<18);
wire [47:0] AxA6 = (New6<=ain5) ? New6 : AxA5 ;
wire [23:0] AA6  = (New6<=ain5) ? (AA5|24'h20000) : AA5 ;
wire [47:0] What7 = 48'h100000000;
wire [47:0] wire_New7 = AxA6 + What7 + (AA6<<17);
wire [47:0] wire_AxA7 = (wire_New7<=ain5) ? wire_New7 : AxA6 ;
wire [23:0] wire_AA7  = (wire_New7<=ain5) ? (AA6|24'h10000) : AA6 ;
reg [47:0] AxA7,AA7; always @(posedge clk) begin AxA7<=wire_AxA7; AA7<=wire_AA7; end
reg [47:0] ain7;  always @(posedge clk) if (en) ain7 <= ain5;
reg vld7;  always @(posedge clk) if (en) vld7 <= vld5;

wire [47:0] What8 = 48'h40000000;
wire [47:0] New8 = AxA7 + What8 + (AA7<<16);
wire [47:0] AxA8 = (New8<=ain7) ? New8 : AxA7 ;
wire [23:0] AA8  = (New8<=ain7) ? (AA7|24'h8000) : AA7 ;
wire [47:0] What9 = 48'h10000000;
wire [47:0] wire_New9 = AxA8 + What9 + (AA8<<15);
wire [47:0] wire_AxA9 = (wire_New9<=ain7) ? wire_New9 : AxA8 ;
wire [23:0] wire_AA9  = (wire_New9<=ain7) ? (AA8|24'h4000) : AA8 ;
reg [47:0] AxA9,AA9; always @(posedge clk) begin AxA9<=wire_AxA9; AA9<=wire_AA9; end
reg [47:0] ain9;  always @(posedge clk) if (en) ain9 <= ain7;
reg vld9;  always @(posedge clk) if (en) vld9 <= vld7;

wire [47:0] What10 = 48'h4000000;
wire [47:0] New10 = AxA9 + What10 + (AA9<<14);
wire [47:0] AxA10 = (New10<=ain9) ? New10 : AxA9 ;
wire [23:0] AA10  = (New10<=ain9) ? (AA9|24'h2000) : AA9 ;
wire [47:0] What11 = 48'h1000000;
wire [47:0] wire_New11 = AxA10 + What11 + (AA10<<13);
wire [47:0] wire_AxA11 = (wire_New11<=ain9) ? wire_New11 : AxA10 ;
wire [23:0] wire_AA11  = (wire_New11<=ain9) ? (AA10|24'h1000) : AA10 ;
reg [47:0] AxA11,AA11; always @(posedge clk) begin AxA11<=wire_AxA11; AA11<=wire_AA11; end
reg [47:0] ain11;  always @(posedge clk) if (en) ain11 <= ain9;
reg vld11;  always @(posedge clk) if (en) vld11 <= vld9;

wire [47:0] What12 = 48'h400000;
wire [47:0] New12 = AxA11 + What12 + (AA11<<12);
wire [47:0] AxA12 = (New12<=ain11) ? New12 : AxA11 ;
wire [23:0] AA12  = (New12<=ain11) ? (AA11|24'h800) : AA11 ;
wire [47:0] What13 = 48'h100000;
wire [47:0] wire_New13 = AxA12 + What13 + (AA12<<11);
wire [47:0] wire_AxA13 = (wire_New13<=ain11) ? wire_New13 : AxA12 ;
wire [23:0] wire_AA13  = (wire_New13<=ain11) ? (AA12|24'h400) : AA12 ;
reg [47:0] AxA13,AA13; always @(posedge clk) begin AxA13<=wire_AxA13; AA13<=wire_AA13; end
reg [47:0] ain13;  always @(posedge clk) if (en) ain13 <= ain11;
reg vld13;  always @(posedge clk) if (en) vld13 <= vld11;

wire [47:0] What14 = 48'h40000;
wire [47:0] New14 = AxA13 + What14 + (AA13<<10);
wire [47:0] AxA14 = (New14<=ain13) ? New14 : AxA13 ;
wire [23:0] AA14  = (New14<=ain13) ? (AA13|24'h200) : AA13 ;
wire [47:0] What15 = 48'h10000;
wire [47:0] wire_New15 = AxA14 + What15 + (AA14<<9);
wire [47:0] wire_AxA15 = (wire_New15<=ain13) ? wire_New15 : AxA14 ;
wire [23:0] wire_AA15  = (wire_New15<=ain13) ? (AA14|24'h100) : AA14 ;
reg [47:0] AxA15,AA15; always @(posedge clk) begin AxA15<=wire_AxA15; AA15<=wire_AA15; end
reg [47:0] ain15;  always @(posedge clk) if (en) ain15 <= ain13;
reg vld15;  always @(posedge clk) if (en) vld15 <= vld13;

wire [47:0] What16 = 48'h4000;
wire [47:0] New16 = AxA15 + What16 + (AA15<<8);
wire [47:0] AxA16 = (New16<=ain15) ? New16 : AxA15 ;
wire [23:0] AA16  = (New16<=ain15) ? (AA15|24'h80) : AA15 ;
wire [47:0] What17 = 48'h1000;
wire [47:0] wire_New17 = AxA16 + What17 + (AA16<<7);
wire [47:0] wire_AxA17 = (wire_New17<=ain15) ? wire_New17 : AxA16 ;
wire [23:0] wire_AA17  = (wire_New17<=ain15) ? (AA16|24'h40) : AA16 ;
reg [47:0] AxA17,AA17; always @(posedge clk) begin AxA17<=wire_AxA17; AA17<=wire_AA17; end
reg [47:0] ain17;  always @(posedge clk) if (en) ain17 <= ain15;
reg vld17;  always @(posedge clk) if (en) vld17 <= vld15;

wire [47:0] What18 = 48'h400;
wire [47:0] New18 = AxA17 + What18 + (AA17<<6);
wire [47:0] AxA18 = (New18<=ain17) ? New18 : AxA17 ;
wire [23:0] AA18  = (New18<=ain17) ? (AA17|24'h20) : AA17 ;
wire [47:0] What19 = 48'h100;
wire [47:0] wire_New19 = AxA18 + What19 + (AA18<<5);
wire [47:0] wire_AxA19 = (wire_New19<=ain17) ? wire_New19 : AxA18 ;
wire [23:0] wire_AA19  = (wire_New19<=ain17) ? (AA18|24'h10) : AA18 ;
reg [47:0] AxA19,AA19; always @(posedge clk) begin AxA19<=wire_AxA19; AA19<=wire_AA19; end
reg [47:0] ain19;  always @(posedge clk) if (en) ain19 <= ain17;
reg vld19;  always @(posedge clk) if (en) vld19 <= vld17;

wire [47:0] What20 = 48'h40;
wire [47:0] New20 = AxA19 + What20 + (AA19<<4);
wire [47:0] AxA20 = (New20<=ain19) ? New20 : AxA19 ;
wire [23:0] AA20  = (New20<=ain19) ? (AA19|24'h8) : AA19 ;
wire [47:0] What21 = 48'h10;
wire [47:0] wire_New21 = AxA20 + What21 + (AA20<<3);
wire [47:0] wire_AxA21 = (wire_New21<=ain19) ? wire_New21 : AxA20 ;
wire [23:0] wire_AA21  = (wire_New21<=ain19) ? (AA20|24'h4) : AA20 ;
reg [47:0] AxA21,AA21; always @(posedge clk) begin AxA21<=wire_AxA21; AA21<=wire_AA21; end
reg [47:0] ain21;  always @(posedge clk) if (en) ain21 <= ain19;
reg vld21;  always @(posedge clk) if (en) vld21 <= vld19;

wire [47:0] What22 = 48'h4;
wire [47:0] New22 = AxA21 + What22 + (AA21<<2);
wire [47:0] AxA22 = (New22<=ain21) ? New22 : AxA21 ;
wire [23:0] AA22  = (New22<=ain21) ? (AA21|24'h2) : AA21 ;
wire [47:0] What23 = 48'h1;
wire [47:0] New23 = AxA22 + What23 + (AA22<<1);
wire [47:0] AxA23 = (New23<=ain21) ? New23 : AxA22 ;
wire [23:0] AA23  = (New23<=ain21) ? (AA22|24'h1) : AA22 ;

always @(posedge clk)  out <= AA23;
always @(posedge clk)  vldout <= vld21;
endmodule
