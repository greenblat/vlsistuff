
module sqrt_u40_5 ( input clk,input rst_n,input en,input vldin, input [39:0] ain, output reg [19:0] out,output reg vldout);
// stages=5 places=[15, 10, 5]
reg vld20;
always @(posedge clk) if (en) vld20 <= vldin;
reg [39:0] datain20;
always @(posedge clk) if (en) datain20 <= ain;
wire [39:0] Y20 = 0;
wire [39:0] YY20 = 0;
wire [39:0] Decra19 = (40'b1<<(2*19));
wire [39:0] Decrb19 = (Y20<<(19+1));
wire [39:0] Decr19 = Decra19+Decrb19;
wire [39:0] YY19_1 = YY20+Decr19;
wire [39:0] Base19 =  40'b1<<19;
wire smaller19 =  (YY19_1<=datain20);
wire [39:0] YY19 = smaller19 ? YY19_1 : ~YY20;
wire [19:0] Y19 = smaller19 ? Y20+Base19 : Y20;
wire [39:0] datain19 = datain20;
wire vld19 = vld20;

wire [39:0] Decra18 = (40'b1<<(2*18));
wire [39:0] Decrb18 = (Y19<<(18+1));
wire [39:0] Decr18 = Decra18+Decrb18;
wire [39:0] YY18_1 = YY19+Decr18;
wire [39:0] Base18 =  40'b1<<18;
wire smaller18 =  (YY18_1<=datain19);
wire [39:0] YY18 = smaller18 ? YY18_1 : YY19;
wire [19:0] Y18 = smaller18 ? Y19+Base18 : Y19;
wire [39:0] datain18 = datain19;
wire vld18 = vld19;

wire [39:0] Decra17 = (40'b1<<(2*17));
wire [39:0] Decrb17 = (Y18<<(17+1));
wire [39:0] Decr17 = Decra17+Decrb17;
wire [39:0] YY17_1 = YY18+Decr17;
wire [39:0] Base17 =  40'b1<<17;
wire smaller17 =  (YY17_1<=datain18);
wire [39:0] YY17 = smaller17 ? YY17_1 : YY18;
wire [19:0] Y17 = smaller17 ? Y18+Base17 : Y18;
wire [39:0] datain17 = datain18;
wire vld17 = vld18;

wire [39:0] Decra16 = (40'b1<<(2*16));
wire [39:0] Decrb16 = (Y17<<(16+1));
wire [39:0] Decr16 = Decra16+Decrb16;
wire [39:0] YY16_1 = YY17+Decr16;
wire [39:0] Base16 =  40'b1<<16;
wire smaller16 =  (YY16_1<=datain17);
wire [39:0] YY16 = smaller16 ? YY16_1 : YY17;
wire [19:0] Y16 = smaller16 ? Y17+Base16 : Y17;
wire [39:0] datain16 = datain17;
wire vld16 = vld17;

wire [39:0] Decra15 = (40'b1<<(2*15));
wire [39:0] Decrb15 = (Y16<<(15+1));
wire [39:0] Decr15 = Decra15+Decrb15;
wire [39:0] YY15_1 = YY16+Decr15;
wire [39:0] Base15 =  40'b1<<15;
wire smaller15 =  (YY15_1<=datain16);
wire [39:0] pre_YY15 = smaller15 ? YY15_1 : YY16;
wire [19:0] pre_Y15 = smaller15 ? Y16+Base15 : Y16;
reg [39:0] YY15;
always @(posedge clk) if (en) YY15 <= pre_YY15;
reg [39:0] Y15;
always @(posedge clk) if (en) Y15 <= pre_Y15;
reg [39:0] datain15;
always @(posedge clk) if (en) datain15 <= datain16;
reg vld15;
always @(posedge clk) if (en) vld15 <= vld16;

wire [39:0] Decra14 = (40'b1<<(2*14));
wire [39:0] Decrb14 = (Y15<<(14+1));
wire [39:0] Decr14 = Decra14+Decrb14;
wire [39:0] YY14_1 = YY15+Decr14;
wire [39:0] Base14 =  40'b1<<14;
wire smaller14 =  (YY14_1<=datain15);
wire [39:0] YY14 = smaller14 ? YY14_1 : YY15;
wire [19:0] Y14 = smaller14 ? Y15+Base14 : Y15;
wire [39:0] datain14 = datain15;
wire vld14 = vld15;

wire [39:0] Decra13 = (40'b1<<(2*13));
wire [39:0] Decrb13 = (Y14<<(13+1));
wire [39:0] Decr13 = Decra13+Decrb13;
wire [39:0] YY13_1 = YY14+Decr13;
wire [39:0] Base13 =  40'b1<<13;
wire smaller13 =  (YY13_1<=datain14);
wire [39:0] YY13 = smaller13 ? YY13_1 : YY14;
wire [19:0] Y13 = smaller13 ? Y14+Base13 : Y14;
wire [39:0] datain13 = datain14;
wire vld13 = vld14;

wire [39:0] Decra12 = (40'b1<<(2*12));
wire [39:0] Decrb12 = (Y13<<(12+1));
wire [39:0] Decr12 = Decra12+Decrb12;
wire [39:0] YY12_1 = YY13+Decr12;
wire [39:0] Base12 =  40'b1<<12;
wire smaller12 =  (YY12_1<=datain13);
wire [39:0] YY12 = smaller12 ? YY12_1 : YY13;
wire [19:0] Y12 = smaller12 ? Y13+Base12 : Y13;
wire [39:0] datain12 = datain13;
wire vld12 = vld13;

wire [39:0] Decra11 = (40'b1<<(2*11));
wire [39:0] Decrb11 = (Y12<<(11+1));
wire [39:0] Decr11 = Decra11+Decrb11;
wire [39:0] YY11_1 = YY12+Decr11;
wire [39:0] Base11 =  40'b1<<11;
wire smaller11 =  (YY11_1<=datain12);
wire [39:0] YY11 = smaller11 ? YY11_1 : YY12;
wire [19:0] Y11 = smaller11 ? Y12+Base11 : Y12;
wire [39:0] datain11 = datain12;
wire vld11 = vld12;

wire [39:0] Decra10 = (40'b1<<(2*10));
wire [39:0] Decrb10 = (Y11<<(10+1));
wire [39:0] Decr10 = Decra10+Decrb10;
wire [39:0] YY10_1 = YY11+Decr10;
wire [39:0] Base10 =  40'b1<<10;
wire smaller10 =  (YY10_1<=datain11);
wire [39:0] pre_YY10 = smaller10 ? YY10_1 : YY11;
wire [19:0] pre_Y10 = smaller10 ? Y11+Base10 : Y11;
reg [39:0] YY10;
always @(posedge clk) if (en) YY10 <= pre_YY10;
reg [39:0] Y10;
always @(posedge clk) if (en) Y10 <= pre_Y10;
reg [39:0] datain10;
always @(posedge clk) if (en) datain10 <= datain11;
reg vld10;
always @(posedge clk) if (en) vld10 <= vld11;

wire [39:0] Decra9 = (40'b1<<(2*9));
wire [39:0] Decrb9 = (Y10<<(9+1));
wire [39:0] Decr9 = Decra9+Decrb9;
wire [39:0] YY9_1 = YY10+Decr9;
wire [39:0] Base9 =  40'b1<<9;
wire smaller9 =  (YY9_1<=datain10);
wire [39:0] YY9 = smaller9 ? YY9_1 : YY10;
wire [19:0] Y9 = smaller9 ? Y10+Base9 : Y10;
wire [39:0] datain9 = datain10;
wire vld9 = vld10;

wire [39:0] Decra8 = (40'b1<<(2*8));
wire [39:0] Decrb8 = (Y9<<(8+1));
wire [39:0] Decr8 = Decra8+Decrb8;
wire [39:0] YY8_1 = YY9+Decr8;
wire [39:0] Base8 =  40'b1<<8;
wire smaller8 =  (YY8_1<=datain9);
wire [39:0] YY8 = smaller8 ? YY8_1 : YY9;
wire [19:0] Y8 = smaller8 ? Y9+Base8 : Y9;
wire [39:0] datain8 = datain9;
wire vld8 = vld9;

wire [39:0] Decra7 = (40'b1<<(2*7));
wire [39:0] Decrb7 = (Y8<<(7+1));
wire [39:0] Decr7 = Decra7+Decrb7;
wire [39:0] YY7_1 = YY8+Decr7;
wire [39:0] Base7 =  40'b1<<7;
wire smaller7 =  (YY7_1<=datain8);
wire [39:0] YY7 = smaller7 ? YY7_1 : YY8;
wire [19:0] Y7 = smaller7 ? Y8+Base7 : Y8;
wire [39:0] datain7 = datain8;
wire vld7 = vld8;

wire [39:0] Decra6 = (40'b1<<(2*6));
wire [39:0] Decrb6 = (Y7<<(6+1));
wire [39:0] Decr6 = Decra6+Decrb6;
wire [39:0] YY6_1 = YY7+Decr6;
wire [39:0] Base6 =  40'b1<<6;
wire smaller6 =  (YY6_1<=datain7);
wire [39:0] YY6 = smaller6 ? YY6_1 : YY7;
wire [19:0] Y6 = smaller6 ? Y7+Base6 : Y7;
wire [39:0] datain6 = datain7;
wire vld6 = vld7;

wire [39:0] Decra5 = (40'b1<<(2*5));
wire [39:0] Decrb5 = (Y6<<(5+1));
wire [39:0] Decr5 = Decra5+Decrb5;
wire [39:0] YY5_1 = YY6+Decr5;
wire [39:0] Base5 =  40'b1<<5;
wire smaller5 =  (YY5_1<=datain6);
wire [39:0] pre_YY5 = smaller5 ? YY5_1 : YY6;
wire [19:0] pre_Y5 = smaller5 ? Y6+Base5 : Y6;
reg [39:0] YY5;
always @(posedge clk) if (en) YY5 <= pre_YY5;
reg [39:0] Y5;
always @(posedge clk) if (en) Y5 <= pre_Y5;
reg [39:0] datain5;
always @(posedge clk) if (en) datain5 <= datain6;
reg vld5;
always @(posedge clk) if (en) vld5 <= vld6;

wire [39:0] Decra4 = (40'b1<<(2*4));
wire [39:0] Decrb4 = (Y5<<(4+1));
wire [39:0] Decr4 = Decra4+Decrb4;
wire [39:0] YY4_1 = YY5+Decr4;
wire [39:0] Base4 =  40'b1<<4;
wire smaller4 =  (YY4_1<=datain5);
wire [39:0] YY4 = smaller4 ? YY4_1 : YY5;
wire [19:0] Y4 = smaller4 ? Y5+Base4 : Y5;
wire [39:0] datain4 = datain5;
wire vld4 = vld5;

wire [39:0] Decra3 = (40'b1<<(2*3));
wire [39:0] Decrb3 = (Y4<<(3+1));
wire [39:0] Decr3 = Decra3+Decrb3;
wire [39:0] YY3_1 = YY4+Decr3;
wire [39:0] Base3 =  40'b1<<3;
wire smaller3 =  (YY3_1<=datain4);
wire [39:0] YY3 = smaller3 ? YY3_1 : YY4;
wire [19:0] Y3 = smaller3 ? Y4+Base3 : Y4;
wire [39:0] datain3 = datain4;
wire vld3 = vld4;

wire [39:0] Decra2 = (40'b1<<(2*2));
wire [39:0] Decrb2 = (Y3<<(2+1));
wire [39:0] Decr2 = Decra2+Decrb2;
wire [39:0] YY2_1 = YY3+Decr2;
wire [39:0] Base2 =  40'b1<<2;
wire smaller2 =  (YY2_1<=datain3);
wire [39:0] YY2 = smaller2 ? YY2_1 : YY3;
wire [19:0] Y2 = smaller2 ? Y3+Base2 : Y3;
wire [39:0] datain2 = datain3;
wire vld2 = vld3;

wire [39:0] Decra1 = (40'b1<<(2*1));
wire [39:0] Decrb1 = (Y2<<(1+1));
wire [39:0] Decr1 = Decra1+Decrb1;
wire [39:0] YY1_1 = YY2+Decr1;
wire [39:0] Base1 =  40'b1<<1;
wire smaller1 =  (YY1_1<=datain2);
wire [39:0] YY1 = smaller1 ? YY1_1 : YY2;
wire [19:0] Y1 = smaller1 ? Y2+Base1 : Y2;
wire [39:0] datain1 = datain2;
wire vld1 = vld2;

wire [39:0] Decra0 = (40'b1<<(2*0));
wire [39:0] Decrb0 = (Y1<<(0+1));
wire [39:0] Decr0 = Decra0+Decrb0;
wire [39:0] YY0_1 = YY1+Decr0;
wire [39:0] Base0 =  40'b1<<0;
wire smaller0 =  (YY0_1<=datain1);
wire [39:0] YY0 = smaller0 ? YY0_1 : YY1;
wire [19:0] Y0 = smaller0 ? Y1+Base0 : Y1;
wire [39:0] datain0 = datain1;
wire vld0 = vld1;

always @(posedge clk) if (en) out <= Y0;
always @(posedge clk) if (en) vldout <= vld0;
endmodule
