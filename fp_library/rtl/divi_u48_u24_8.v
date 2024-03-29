
module divi_u48_u24_8 ( input clk,input rst_n,input en, input vldin,output reg vldout, input [47:0] ain, input [23:0] bin, output reg  [47:0] out,output reg [22:0] remainder);
// stages=8 places=[41, 34, 27, 20, 13, 6]
reg vld1;
always @(posedge clk) if (en) vld1 <= vldin;
reg [71:0] ain1;
always @(posedge clk) if (en) ain1 <= {24'b0,ain};
reg [24:0] bin1;
always @(posedge clk) if (en) bin1 <= {1'b0,bin};


wire bit1 = (bin1 <= ain1[71:47]);
wire [24:0] xhigh1 = ain1[71:47]-bin1;
wire [23:0] high1 = bit1 ? xhigh1[23:0] : ain1[70:47] ;
wire [70:0]  ain2 = {high1,ain1[46:0]};
wire res2 = bit1;
wire [24:0] bin2 = bin1;
wire vld2 = vld1;


wire bit2 = (bin2 <= ain2[70:46]);
wire [24:0] xhigh2 = ain2[70:46]-bin2;
wire [23:0] high2 = bit2 ? xhigh2[23:0] : ain2[69:46] ;
wire [69:0]  ain3 = {high2,ain2[45:0]};
wire [1:0]  res3 = {res2,bit2};
wire [24:0] bin3 = bin2;
wire vld3 = vld2;


wire bit3 = (bin3 <= ain3[69:45]);
wire [24:0] xhigh3 = ain3[69:45]-bin3;
wire [23:0] high3 = bit3 ? xhigh3[23:0] : ain3[68:45] ;
wire [68:0]  ain4 = {high3,ain3[44:0]};
wire [2:0]  res4 = {res3,bit3};
wire [24:0] bin4 = bin3;
wire vld4 = vld3;


wire bit4 = (bin4 <= ain4[68:44]);
wire [24:0] xhigh4 = ain4[68:44]-bin4;
wire [23:0] high4 = bit4 ? xhigh4[23:0] : ain4[67:44] ;
wire [67:0]  ain5 = {high4,ain4[43:0]};
wire [3:0]  res5 = {res4,bit4};
wire [24:0] bin5 = bin4;
wire vld5 = vld4;


wire bit5 = (bin5 <= ain5[67:43]);
wire [24:0] xhigh5 = ain5[67:43]-bin5;
wire [23:0] high5 = bit5 ? xhigh5[23:0] : ain5[66:43] ;
wire [66:0]  ain6 = {high5,ain5[42:0]};
wire [4:0]  res6 = {res5,bit5};
wire [24:0] bin6 = bin5;
wire vld6 = vld5;


wire bit6 = (bin6 <= ain6[66:42]);
wire [24:0] xhigh6 = ain6[66:42]-bin6;
wire [23:0] high6 = bit6 ? xhigh6[23:0] : ain6[65:42] ;
wire [65:0]  pre_ain7 = {high6,ain6[41:0]};
wire [5:0]  pre_res7 = {res6,bit6};

reg [65:0] ain7;
always @(posedge clk) if (en) ain7 <= pre_ain7;
reg [24:0] bin7;
always @(posedge clk) if (en) bin7 <= bin6;
reg [5:0] res7;
always @(posedge clk) if (en) res7 <= pre_res7;
reg vld7;
always @(posedge clk) if (en) vld7 <= vld6;


wire bit7 = (bin7 <= ain7[65:41]);
wire [24:0] xhigh7 = ain7[65:41]-bin7;
wire [23:0] high7 = bit7 ? xhigh7[23:0] : ain7[64:41] ;
wire [64:0]  ain8 = {high7,ain7[40:0]};
wire [6:0]  res8 = {res7,bit7};
wire [24:0] bin8 = bin7;
wire vld8 = vld7;


wire bit8 = (bin8 <= ain8[64:40]);
wire [24:0] xhigh8 = ain8[64:40]-bin8;
wire [23:0] high8 = bit8 ? xhigh8[23:0] : ain8[63:40] ;
wire [63:0]  ain9 = {high8,ain8[39:0]};
wire [7:0]  res9 = {res8,bit8};
wire [24:0] bin9 = bin8;
wire vld9 = vld8;


wire bit9 = (bin9 <= ain9[63:39]);
wire [24:0] xhigh9 = ain9[63:39]-bin9;
wire [23:0] high9 = bit9 ? xhigh9[23:0] : ain9[62:39] ;
wire [62:0]  ain10 = {high9,ain9[38:0]};
wire [8:0]  res10 = {res9,bit9};
wire [24:0] bin10 = bin9;
wire vld10 = vld9;


wire bit10 = (bin10 <= ain10[62:38]);
wire [24:0] xhigh10 = ain10[62:38]-bin10;
wire [23:0] high10 = bit10 ? xhigh10[23:0] : ain10[61:38] ;
wire [61:0]  ain11 = {high10,ain10[37:0]};
wire [9:0]  res11 = {res10,bit10};
wire [24:0] bin11 = bin10;
wire vld11 = vld10;


wire bit11 = (bin11 <= ain11[61:37]);
wire [24:0] xhigh11 = ain11[61:37]-bin11;
wire [23:0] high11 = bit11 ? xhigh11[23:0] : ain11[60:37] ;
wire [60:0]  ain12 = {high11,ain11[36:0]};
wire [10:0]  res12 = {res11,bit11};
wire [24:0] bin12 = bin11;
wire vld12 = vld11;


wire bit12 = (bin12 <= ain12[60:36]);
wire [24:0] xhigh12 = ain12[60:36]-bin12;
wire [23:0] high12 = bit12 ? xhigh12[23:0] : ain12[59:36] ;
wire [59:0]  ain13 = {high12,ain12[35:0]};
wire [11:0]  res13 = {res12,bit12};
wire [24:0] bin13 = bin12;
wire vld13 = vld12;


wire bit13 = (bin13 <= ain13[59:35]);
wire [24:0] xhigh13 = ain13[59:35]-bin13;
wire [23:0] high13 = bit13 ? xhigh13[23:0] : ain13[58:35] ;
wire [58:0]  pre_ain14 = {high13,ain13[34:0]};
wire [12:0]  pre_res14 = {res13,bit13};

reg [58:0] ain14;
always @(posedge clk) if (en) ain14 <= pre_ain14;
reg [24:0] bin14;
always @(posedge clk) if (en) bin14 <= bin13;
reg [12:0] res14;
always @(posedge clk) if (en) res14 <= pre_res14;
reg vld14;
always @(posedge clk) if (en) vld14 <= vld13;


wire bit14 = (bin14 <= ain14[58:34]);
wire [24:0] xhigh14 = ain14[58:34]-bin14;
wire [23:0] high14 = bit14 ? xhigh14[23:0] : ain14[57:34] ;
wire [57:0]  ain15 = {high14,ain14[33:0]};
wire [13:0]  res15 = {res14,bit14};
wire [24:0] bin15 = bin14;
wire vld15 = vld14;


wire bit15 = (bin15 <= ain15[57:33]);
wire [24:0] xhigh15 = ain15[57:33]-bin15;
wire [23:0] high15 = bit15 ? xhigh15[23:0] : ain15[56:33] ;
wire [56:0]  ain16 = {high15,ain15[32:0]};
wire [14:0]  res16 = {res15,bit15};
wire [24:0] bin16 = bin15;
wire vld16 = vld15;


wire bit16 = (bin16 <= ain16[56:32]);
wire [24:0] xhigh16 = ain16[56:32]-bin16;
wire [23:0] high16 = bit16 ? xhigh16[23:0] : ain16[55:32] ;
wire [55:0]  ain17 = {high16,ain16[31:0]};
wire [15:0]  res17 = {res16,bit16};
wire [24:0] bin17 = bin16;
wire vld17 = vld16;


wire bit17 = (bin17 <= ain17[55:31]);
wire [24:0] xhigh17 = ain17[55:31]-bin17;
wire [23:0] high17 = bit17 ? xhigh17[23:0] : ain17[54:31] ;
wire [54:0]  ain18 = {high17,ain17[30:0]};
wire [16:0]  res18 = {res17,bit17};
wire [24:0] bin18 = bin17;
wire vld18 = vld17;


wire bit18 = (bin18 <= ain18[54:30]);
wire [24:0] xhigh18 = ain18[54:30]-bin18;
wire [23:0] high18 = bit18 ? xhigh18[23:0] : ain18[53:30] ;
wire [53:0]  ain19 = {high18,ain18[29:0]};
wire [17:0]  res19 = {res18,bit18};
wire [24:0] bin19 = bin18;
wire vld19 = vld18;


wire bit19 = (bin19 <= ain19[53:29]);
wire [24:0] xhigh19 = ain19[53:29]-bin19;
wire [23:0] high19 = bit19 ? xhigh19[23:0] : ain19[52:29] ;
wire [52:0]  ain20 = {high19,ain19[28:0]};
wire [18:0]  res20 = {res19,bit19};
wire [24:0] bin20 = bin19;
wire vld20 = vld19;


wire bit20 = (bin20 <= ain20[52:28]);
wire [24:0] xhigh20 = ain20[52:28]-bin20;
wire [23:0] high20 = bit20 ? xhigh20[23:0] : ain20[51:28] ;
wire [51:0]  pre_ain21 = {high20,ain20[27:0]};
wire [19:0]  pre_res21 = {res20,bit20};

reg [51:0] ain21;
always @(posedge clk) if (en) ain21 <= pre_ain21;
reg [24:0] bin21;
always @(posedge clk) if (en) bin21 <= bin20;
reg [19:0] res21;
always @(posedge clk) if (en) res21 <= pre_res21;
reg vld21;
always @(posedge clk) if (en) vld21 <= vld20;


wire bit21 = (bin21 <= ain21[51:27]);
wire [24:0] xhigh21 = ain21[51:27]-bin21;
wire [23:0] high21 = bit21 ? xhigh21[23:0] : ain21[50:27] ;
wire [50:0]  ain22 = {high21,ain21[26:0]};
wire [20:0]  res22 = {res21,bit21};
wire [24:0] bin22 = bin21;
wire vld22 = vld21;


wire bit22 = (bin22 <= ain22[50:26]);
wire [24:0] xhigh22 = ain22[50:26]-bin22;
wire [23:0] high22 = bit22 ? xhigh22[23:0] : ain22[49:26] ;
wire [49:0]  ain23 = {high22,ain22[25:0]};
wire [21:0]  res23 = {res22,bit22};
wire [24:0] bin23 = bin22;
wire vld23 = vld22;


wire bit23 = (bin23 <= ain23[49:25]);
wire [24:0] xhigh23 = ain23[49:25]-bin23;
wire [23:0] high23 = bit23 ? xhigh23[23:0] : ain23[48:25] ;
wire [48:0]  ain24 = {high23,ain23[24:0]};
wire [22:0]  res24 = {res23,bit23};
wire [24:0] bin24 = bin23;
wire vld24 = vld23;


wire bit24 = (bin24 <= ain24[48:24]);
wire [24:0] xhigh24 = ain24[48:24]-bin24;
wire [23:0] high24 = bit24 ? xhigh24[23:0] : ain24[47:24] ;
wire [47:0]  ain25 = {high24,ain24[23:0]};
wire [23:0]  res25 = {res24,bit24};
wire [24:0] bin25 = bin24;
wire vld25 = vld24;


wire bit25 = (bin25 <= ain25[47:23]);
wire [24:0] xhigh25 = ain25[47:23]-bin25;
wire [23:0] high25 = bit25 ? xhigh25[23:0] : ain25[46:23] ;
wire [46:0]  ain26 = {high25,ain25[22:0]};
wire [24:0]  res26 = {res25,bit25};
wire [24:0] bin26 = bin25;
wire vld26 = vld25;


wire bit26 = (bin26 <= ain26[46:22]);
wire [24:0] xhigh26 = ain26[46:22]-bin26;
wire [23:0] high26 = bit26 ? xhigh26[23:0] : ain26[45:22] ;
wire [45:0]  ain27 = {high26,ain26[21:0]};
wire [25:0]  res27 = {res26,bit26};
wire [24:0] bin27 = bin26;
wire vld27 = vld26;


wire bit27 = (bin27 <= ain27[45:21]);
wire [24:0] xhigh27 = ain27[45:21]-bin27;
wire [23:0] high27 = bit27 ? xhigh27[23:0] : ain27[44:21] ;
wire [44:0]  pre_ain28 = {high27,ain27[20:0]};
wire [26:0]  pre_res28 = {res27,bit27};

reg [44:0] ain28;
always @(posedge clk) if (en) ain28 <= pre_ain28;
reg [24:0] bin28;
always @(posedge clk) if (en) bin28 <= bin27;
reg [26:0] res28;
always @(posedge clk) if (en) res28 <= pre_res28;
reg vld28;
always @(posedge clk) if (en) vld28 <= vld27;


wire bit28 = (bin28 <= ain28[44:20]);
wire [24:0] xhigh28 = ain28[44:20]-bin28;
wire [23:0] high28 = bit28 ? xhigh28[23:0] : ain28[43:20] ;
wire [43:0]  ain29 = {high28,ain28[19:0]};
wire [27:0]  res29 = {res28,bit28};
wire [24:0] bin29 = bin28;
wire vld29 = vld28;


wire bit29 = (bin29 <= ain29[43:19]);
wire [24:0] xhigh29 = ain29[43:19]-bin29;
wire [23:0] high29 = bit29 ? xhigh29[23:0] : ain29[42:19] ;
wire [42:0]  ain30 = {high29,ain29[18:0]};
wire [28:0]  res30 = {res29,bit29};
wire [24:0] bin30 = bin29;
wire vld30 = vld29;


wire bit30 = (bin30 <= ain30[42:18]);
wire [24:0] xhigh30 = ain30[42:18]-bin30;
wire [23:0] high30 = bit30 ? xhigh30[23:0] : ain30[41:18] ;
wire [41:0]  ain31 = {high30,ain30[17:0]};
wire [29:0]  res31 = {res30,bit30};
wire [24:0] bin31 = bin30;
wire vld31 = vld30;


wire bit31 = (bin31 <= ain31[41:17]);
wire [24:0] xhigh31 = ain31[41:17]-bin31;
wire [23:0] high31 = bit31 ? xhigh31[23:0] : ain31[40:17] ;
wire [40:0]  ain32 = {high31,ain31[16:0]};
wire [30:0]  res32 = {res31,bit31};
wire [24:0] bin32 = bin31;
wire vld32 = vld31;


wire bit32 = (bin32 <= ain32[40:16]);
wire [24:0] xhigh32 = ain32[40:16]-bin32;
wire [23:0] high32 = bit32 ? xhigh32[23:0] : ain32[39:16] ;
wire [39:0]  ain33 = {high32,ain32[15:0]};
wire [31:0]  res33 = {res32,bit32};
wire [24:0] bin33 = bin32;
wire vld33 = vld32;


wire bit33 = (bin33 <= ain33[39:15]);
wire [24:0] xhigh33 = ain33[39:15]-bin33;
wire [23:0] high33 = bit33 ? xhigh33[23:0] : ain33[38:15] ;
wire [38:0]  ain34 = {high33,ain33[14:0]};
wire [32:0]  res34 = {res33,bit33};
wire [24:0] bin34 = bin33;
wire vld34 = vld33;


wire bit34 = (bin34 <= ain34[38:14]);
wire [24:0] xhigh34 = ain34[38:14]-bin34;
wire [23:0] high34 = bit34 ? xhigh34[23:0] : ain34[37:14] ;
wire [37:0]  pre_ain35 = {high34,ain34[13:0]};
wire [33:0]  pre_res35 = {res34,bit34};

reg [37:0] ain35;
always @(posedge clk) if (en) ain35 <= pre_ain35;
reg [24:0] bin35;
always @(posedge clk) if (en) bin35 <= bin34;
reg [33:0] res35;
always @(posedge clk) if (en) res35 <= pre_res35;
reg vld35;
always @(posedge clk) if (en) vld35 <= vld34;


wire bit35 = (bin35 <= ain35[37:13]);
wire [24:0] xhigh35 = ain35[37:13]-bin35;
wire [23:0] high35 = bit35 ? xhigh35[23:0] : ain35[36:13] ;
wire [36:0]  ain36 = {high35,ain35[12:0]};
wire [34:0]  res36 = {res35,bit35};
wire [24:0] bin36 = bin35;
wire vld36 = vld35;


wire bit36 = (bin36 <= ain36[36:12]);
wire [24:0] xhigh36 = ain36[36:12]-bin36;
wire [23:0] high36 = bit36 ? xhigh36[23:0] : ain36[35:12] ;
wire [35:0]  ain37 = {high36,ain36[11:0]};
wire [35:0]  res37 = {res36,bit36};
wire [24:0] bin37 = bin36;
wire vld37 = vld36;


wire bit37 = (bin37 <= ain37[35:11]);
wire [24:0] xhigh37 = ain37[35:11]-bin37;
wire [23:0] high37 = bit37 ? xhigh37[23:0] : ain37[34:11] ;
wire [34:0]  ain38 = {high37,ain37[10:0]};
wire [36:0]  res38 = {res37,bit37};
wire [24:0] bin38 = bin37;
wire vld38 = vld37;


wire bit38 = (bin38 <= ain38[34:10]);
wire [24:0] xhigh38 = ain38[34:10]-bin38;
wire [23:0] high38 = bit38 ? xhigh38[23:0] : ain38[33:10] ;
wire [33:0]  ain39 = {high38,ain38[9:0]};
wire [37:0]  res39 = {res38,bit38};
wire [24:0] bin39 = bin38;
wire vld39 = vld38;


wire bit39 = (bin39 <= ain39[33:9]);
wire [24:0] xhigh39 = ain39[33:9]-bin39;
wire [23:0] high39 = bit39 ? xhigh39[23:0] : ain39[32:9] ;
wire [32:0]  ain40 = {high39,ain39[8:0]};
wire [38:0]  res40 = {res39,bit39};
wire [24:0] bin40 = bin39;
wire vld40 = vld39;


wire bit40 = (bin40 <= ain40[32:8]);
wire [24:0] xhigh40 = ain40[32:8]-bin40;
wire [23:0] high40 = bit40 ? xhigh40[23:0] : ain40[31:8] ;
wire [31:0]  ain41 = {high40,ain40[7:0]};
wire [39:0]  res41 = {res40,bit40};
wire [24:0] bin41 = bin40;
wire vld41 = vld40;


wire bit41 = (bin41 <= ain41[31:7]);
wire [24:0] xhigh41 = ain41[31:7]-bin41;
wire [23:0] high41 = bit41 ? xhigh41[23:0] : ain41[30:7] ;
wire [30:0]  pre_ain42 = {high41,ain41[6:0]};
wire [40:0]  pre_res42 = {res41,bit41};

reg [30:0] ain42;
always @(posedge clk) if (en) ain42 <= pre_ain42;
reg [24:0] bin42;
always @(posedge clk) if (en) bin42 <= bin41;
reg [40:0] res42;
always @(posedge clk) if (en) res42 <= pre_res42;
reg vld42;
always @(posedge clk) if (en) vld42 <= vld41;


wire bit42 = (bin42 <= ain42[30:6]);
wire [24:0] xhigh42 = ain42[30:6]-bin42;
wire [23:0] high42 = bit42 ? xhigh42[23:0] : ain42[29:6] ;
wire [29:0]  ain43 = {high42,ain42[5:0]};
wire [41:0]  res43 = {res42,bit42};
wire [24:0] bin43 = bin42;
wire vld43 = vld42;


wire bit43 = (bin43 <= ain43[29:5]);
wire [24:0] xhigh43 = ain43[29:5]-bin43;
wire [23:0] high43 = bit43 ? xhigh43[23:0] : ain43[28:5] ;
wire [28:0]  ain44 = {high43,ain43[4:0]};
wire [42:0]  res44 = {res43,bit43};
wire [24:0] bin44 = bin43;
wire vld44 = vld43;


wire bit44 = (bin44 <= ain44[28:4]);
wire [24:0] xhigh44 = ain44[28:4]-bin44;
wire [23:0] high44 = bit44 ? xhigh44[23:0] : ain44[27:4] ;
wire [27:0]  ain45 = {high44,ain44[3:0]};
wire [43:0]  res45 = {res44,bit44};
wire [24:0] bin45 = bin44;
wire vld45 = vld44;


wire bit45 = (bin45 <= ain45[27:3]);
wire [24:0] xhigh45 = ain45[27:3]-bin45;
wire [23:0] high45 = bit45 ? xhigh45[23:0] : ain45[26:3] ;
wire [26:0]  ain46 = {high45,ain45[2:0]};
wire [44:0]  res46 = {res45,bit45};
wire [24:0] bin46 = bin45;
wire vld46 = vld45;


wire bit46 = (bin46 <= ain46[26:2]);
wire [24:0] xhigh46 = ain46[26:2]-bin46;
wire [23:0] high46 = bit46 ? xhigh46[23:0] : ain46[25:2] ;
wire [25:0]  ain47 = {high46,ain46[1:0]};
wire [45:0]  res47 = {res46,bit46};
wire [24:0] bin47 = bin46;
wire vld47 = vld46;


wire bit47 = (bin47 <= ain47[25:1]);
wire [24:0] xhigh47 = ain47[25:1]-bin47;
wire [23:0] high47 = bit47 ? xhigh47[23:0] : ain47[24:1] ;
wire [24:0]  ain48 = {high47,ain47[0]};
wire [46:0]  res48 = {res47,bit47};
wire [24:0] bin48 = bin47;
wire vld48 = vld47;


wire bit48 = (bin48 <= ain48[24:0]);
wire [24:0] xhigh48 = ain48[24:0]-bin48;
wire [23:0] high48 = bit48 ? xhigh48[23:0] : ain48[23:0] ;
wire [23:0]  ain49 = high48;
wire [47:0]  res49 = {res48,bit48};
wire [24:0] bin49 = bin48;
wire vld49 = vld48;
wire [47:0] res000 = (bin49==0) ? 48'b0 : res49 ;
always @(posedge clk) if (en) out <= res000;
always @(posedge clk) if (en) remainder <= ain49;
always @(posedge clk) if (en) vldout <= vld49;
endmodule
