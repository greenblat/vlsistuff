
module divider_u128_u128_64 ( input clk,input rst_n,input en, input vldin,output reg vldout, input [127:0] ain, input [127:0] bin, output reg  [127:0] out,output reg [126:0] remainder);
// stages=64 places=[126, 124, 122, 120, 118, 116, 114, 112, 110, 108, 106, 104, 102, 100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 3]
reg vld1;
always @(posedge clk) if (en) vld1 <= vldin; else vld1 <= 0;
reg [255:0] ain1;
always @(posedge clk) if (en) ain1 <= {128'b0,ain};
reg [128:0] bin1;
always @(posedge clk) if (en) bin1 <= {1'b0,bin};


wire bit1 = (bin1 <= ain1[255:127]);
wire [128:0] xhigh1 = ain1[255:127]-bin1;
wire [127:0] high1 = bit1 ? xhigh1[127:0] : ain1[254:127] ;
wire [254:0]  ain2 = {high1,ain1[126:0]};
wire res2 = bit1;
wire [128:0] bin2 = bin1;
wire vld2 = vld1;


wire bit2 = (bin2 <= ain2[254:126]);
wire [128:0] xhigh2 = ain2[254:126]-bin2;
wire [127:0] high2 = bit2 ? xhigh2[127:0] : ain2[253:126] ;
wire [253:0]  ain3 = {high2,ain2[125:0]};
wire [1:0]  res3 = {res2,bit2};
wire [128:0] bin3 = bin2;
wire vld3 = vld2;


wire bit3 = (bin3 <= ain3[253:125]);
wire [128:0] xhigh3 = ain3[253:125]-bin3;
wire [127:0] high3 = bit3 ? xhigh3[127:0] : ain3[252:125] ;
wire [252:0]  pre_ain4 = {high3,ain3[124:0]};
wire [2:0]  pre_res4 = {res3,bit3};

reg [252:0] ain4;
always @(posedge clk) if (en) ain4 <= pre_ain4;
reg [128:0] bin4;
always @(posedge clk) if (en) bin4 <= bin3;
reg [2:0] res4;
always @(posedge clk) if (en) res4 <= pre_res4;
reg vld4;
always @(posedge clk) if (en) vld4 <= vld3; else vld4 <= 0;


wire bit4 = (bin4 <= ain4[252:124]);
wire [128:0] xhigh4 = ain4[252:124]-bin4;
wire [127:0] high4 = bit4 ? xhigh4[127:0] : ain4[251:124] ;
wire [251:0]  ain5 = {high4,ain4[123:0]};
wire [3:0]  res5 = {res4,bit4};
wire [128:0] bin5 = bin4;
wire vld5 = vld4;


wire bit5 = (bin5 <= ain5[251:123]);
wire [128:0] xhigh5 = ain5[251:123]-bin5;
wire [127:0] high5 = bit5 ? xhigh5[127:0] : ain5[250:123] ;
wire [250:0]  ain6 = {high5,ain5[122:0]};
wire [4:0]  res6 = {res5,bit5};
wire [128:0] bin6 = bin5;
wire vld6 = vld5;


wire bit6 = (bin6 <= ain6[250:122]);
wire [128:0] xhigh6 = ain6[250:122]-bin6;
wire [127:0] high6 = bit6 ? xhigh6[127:0] : ain6[249:122] ;
wire [249:0]  pre_ain7 = {high6,ain6[121:0]};
wire [5:0]  pre_res7 = {res6,bit6};

reg [249:0] ain7;
always @(posedge clk) if (en) ain7 <= pre_ain7;
reg [128:0] bin7;
always @(posedge clk) if (en) bin7 <= bin6;
reg [5:0] res7;
always @(posedge clk) if (en) res7 <= pre_res7;
reg vld7;
always @(posedge clk) if (en) vld7 <= vld6; else vld7 <= 0;


wire bit7 = (bin7 <= ain7[249:121]);
wire [128:0] xhigh7 = ain7[249:121]-bin7;
wire [127:0] high7 = bit7 ? xhigh7[127:0] : ain7[248:121] ;
wire [248:0]  ain8 = {high7,ain7[120:0]};
wire [6:0]  res8 = {res7,bit7};
wire [128:0] bin8 = bin7;
wire vld8 = vld7;


wire bit8 = (bin8 <= ain8[248:120]);
wire [128:0] xhigh8 = ain8[248:120]-bin8;
wire [127:0] high8 = bit8 ? xhigh8[127:0] : ain8[247:120] ;
wire [247:0]  pre_ain9 = {high8,ain8[119:0]};
wire [7:0]  pre_res9 = {res8,bit8};

reg [247:0] ain9;
always @(posedge clk) if (en) ain9 <= pre_ain9;
reg [128:0] bin9;
always @(posedge clk) if (en) bin9 <= bin8;
reg [7:0] res9;
always @(posedge clk) if (en) res9 <= pre_res9;
reg vld9;
always @(posedge clk) if (en) vld9 <= vld8; else vld9 <= 0;


wire bit9 = (bin9 <= ain9[247:119]);
wire [128:0] xhigh9 = ain9[247:119]-bin9;
wire [127:0] high9 = bit9 ? xhigh9[127:0] : ain9[246:119] ;
wire [246:0]  ain10 = {high9,ain9[118:0]};
wire [8:0]  res10 = {res9,bit9};
wire [128:0] bin10 = bin9;
wire vld10 = vld9;


wire bit10 = (bin10 <= ain10[246:118]);
wire [128:0] xhigh10 = ain10[246:118]-bin10;
wire [127:0] high10 = bit10 ? xhigh10[127:0] : ain10[245:118] ;
wire [245:0]  pre_ain11 = {high10,ain10[117:0]};
wire [9:0]  pre_res11 = {res10,bit10};

reg [245:0] ain11;
always @(posedge clk) if (en) ain11 <= pre_ain11;
reg [128:0] bin11;
always @(posedge clk) if (en) bin11 <= bin10;
reg [9:0] res11;
always @(posedge clk) if (en) res11 <= pre_res11;
reg vld11;
always @(posedge clk) if (en) vld11 <= vld10; else vld11 <= 0;


wire bit11 = (bin11 <= ain11[245:117]);
wire [128:0] xhigh11 = ain11[245:117]-bin11;
wire [127:0] high11 = bit11 ? xhigh11[127:0] : ain11[244:117] ;
wire [244:0]  ain12 = {high11,ain11[116:0]};
wire [10:0]  res12 = {res11,bit11};
wire [128:0] bin12 = bin11;
wire vld12 = vld11;


wire bit12 = (bin12 <= ain12[244:116]);
wire [128:0] xhigh12 = ain12[244:116]-bin12;
wire [127:0] high12 = bit12 ? xhigh12[127:0] : ain12[243:116] ;
wire [243:0]  pre_ain13 = {high12,ain12[115:0]};
wire [11:0]  pre_res13 = {res12,bit12};

reg [243:0] ain13;
always @(posedge clk) if (en) ain13 <= pre_ain13;
reg [128:0] bin13;
always @(posedge clk) if (en) bin13 <= bin12;
reg [11:0] res13;
always @(posedge clk) if (en) res13 <= pre_res13;
reg vld13;
always @(posedge clk) if (en) vld13 <= vld12; else vld13 <= 0;


wire bit13 = (bin13 <= ain13[243:115]);
wire [128:0] xhigh13 = ain13[243:115]-bin13;
wire [127:0] high13 = bit13 ? xhigh13[127:0] : ain13[242:115] ;
wire [242:0]  ain14 = {high13,ain13[114:0]};
wire [12:0]  res14 = {res13,bit13};
wire [128:0] bin14 = bin13;
wire vld14 = vld13;


wire bit14 = (bin14 <= ain14[242:114]);
wire [128:0] xhigh14 = ain14[242:114]-bin14;
wire [127:0] high14 = bit14 ? xhigh14[127:0] : ain14[241:114] ;
wire [241:0]  pre_ain15 = {high14,ain14[113:0]};
wire [13:0]  pre_res15 = {res14,bit14};

reg [241:0] ain15;
always @(posedge clk) if (en) ain15 <= pre_ain15;
reg [128:0] bin15;
always @(posedge clk) if (en) bin15 <= bin14;
reg [13:0] res15;
always @(posedge clk) if (en) res15 <= pre_res15;
reg vld15;
always @(posedge clk) if (en) vld15 <= vld14; else vld15 <= 0;


wire bit15 = (bin15 <= ain15[241:113]);
wire [128:0] xhigh15 = ain15[241:113]-bin15;
wire [127:0] high15 = bit15 ? xhigh15[127:0] : ain15[240:113] ;
wire [240:0]  ain16 = {high15,ain15[112:0]};
wire [14:0]  res16 = {res15,bit15};
wire [128:0] bin16 = bin15;
wire vld16 = vld15;


wire bit16 = (bin16 <= ain16[240:112]);
wire [128:0] xhigh16 = ain16[240:112]-bin16;
wire [127:0] high16 = bit16 ? xhigh16[127:0] : ain16[239:112] ;
wire [239:0]  pre_ain17 = {high16,ain16[111:0]};
wire [15:0]  pre_res17 = {res16,bit16};

reg [239:0] ain17;
always @(posedge clk) if (en) ain17 <= pre_ain17;
reg [128:0] bin17;
always @(posedge clk) if (en) bin17 <= bin16;
reg [15:0] res17;
always @(posedge clk) if (en) res17 <= pre_res17;
reg vld17;
always @(posedge clk) if (en) vld17 <= vld16; else vld17 <= 0;


wire bit17 = (bin17 <= ain17[239:111]);
wire [128:0] xhigh17 = ain17[239:111]-bin17;
wire [127:0] high17 = bit17 ? xhigh17[127:0] : ain17[238:111] ;
wire [238:0]  ain18 = {high17,ain17[110:0]};
wire [16:0]  res18 = {res17,bit17};
wire [128:0] bin18 = bin17;
wire vld18 = vld17;


wire bit18 = (bin18 <= ain18[238:110]);
wire [128:0] xhigh18 = ain18[238:110]-bin18;
wire [127:0] high18 = bit18 ? xhigh18[127:0] : ain18[237:110] ;
wire [237:0]  pre_ain19 = {high18,ain18[109:0]};
wire [17:0]  pre_res19 = {res18,bit18};

reg [237:0] ain19;
always @(posedge clk) if (en) ain19 <= pre_ain19;
reg [128:0] bin19;
always @(posedge clk) if (en) bin19 <= bin18;
reg [17:0] res19;
always @(posedge clk) if (en) res19 <= pre_res19;
reg vld19;
always @(posedge clk) if (en) vld19 <= vld18; else vld19 <= 0;


wire bit19 = (bin19 <= ain19[237:109]);
wire [128:0] xhigh19 = ain19[237:109]-bin19;
wire [127:0] high19 = bit19 ? xhigh19[127:0] : ain19[236:109] ;
wire [236:0]  ain20 = {high19,ain19[108:0]};
wire [18:0]  res20 = {res19,bit19};
wire [128:0] bin20 = bin19;
wire vld20 = vld19;


wire bit20 = (bin20 <= ain20[236:108]);
wire [128:0] xhigh20 = ain20[236:108]-bin20;
wire [127:0] high20 = bit20 ? xhigh20[127:0] : ain20[235:108] ;
wire [235:0]  pre_ain21 = {high20,ain20[107:0]};
wire [19:0]  pre_res21 = {res20,bit20};

reg [235:0] ain21;
always @(posedge clk) if (en) ain21 <= pre_ain21;
reg [128:0] bin21;
always @(posedge clk) if (en) bin21 <= bin20;
reg [19:0] res21;
always @(posedge clk) if (en) res21 <= pre_res21;
reg vld21;
always @(posedge clk) if (en) vld21 <= vld20; else vld21 <= 0;


wire bit21 = (bin21 <= ain21[235:107]);
wire [128:0] xhigh21 = ain21[235:107]-bin21;
wire [127:0] high21 = bit21 ? xhigh21[127:0] : ain21[234:107] ;
wire [234:0]  ain22 = {high21,ain21[106:0]};
wire [20:0]  res22 = {res21,bit21};
wire [128:0] bin22 = bin21;
wire vld22 = vld21;


wire bit22 = (bin22 <= ain22[234:106]);
wire [128:0] xhigh22 = ain22[234:106]-bin22;
wire [127:0] high22 = bit22 ? xhigh22[127:0] : ain22[233:106] ;
wire [233:0]  pre_ain23 = {high22,ain22[105:0]};
wire [21:0]  pre_res23 = {res22,bit22};

reg [233:0] ain23;
always @(posedge clk) if (en) ain23 <= pre_ain23;
reg [128:0] bin23;
always @(posedge clk) if (en) bin23 <= bin22;
reg [21:0] res23;
always @(posedge clk) if (en) res23 <= pre_res23;
reg vld23;
always @(posedge clk) if (en) vld23 <= vld22; else vld23 <= 0;


wire bit23 = (bin23 <= ain23[233:105]);
wire [128:0] xhigh23 = ain23[233:105]-bin23;
wire [127:0] high23 = bit23 ? xhigh23[127:0] : ain23[232:105] ;
wire [232:0]  ain24 = {high23,ain23[104:0]};
wire [22:0]  res24 = {res23,bit23};
wire [128:0] bin24 = bin23;
wire vld24 = vld23;


wire bit24 = (bin24 <= ain24[232:104]);
wire [128:0] xhigh24 = ain24[232:104]-bin24;
wire [127:0] high24 = bit24 ? xhigh24[127:0] : ain24[231:104] ;
wire [231:0]  pre_ain25 = {high24,ain24[103:0]};
wire [23:0]  pre_res25 = {res24,bit24};

reg [231:0] ain25;
always @(posedge clk) if (en) ain25 <= pre_ain25;
reg [128:0] bin25;
always @(posedge clk) if (en) bin25 <= bin24;
reg [23:0] res25;
always @(posedge clk) if (en) res25 <= pre_res25;
reg vld25;
always @(posedge clk) if (en) vld25 <= vld24; else vld25 <= 0;


wire bit25 = (bin25 <= ain25[231:103]);
wire [128:0] xhigh25 = ain25[231:103]-bin25;
wire [127:0] high25 = bit25 ? xhigh25[127:0] : ain25[230:103] ;
wire [230:0]  ain26 = {high25,ain25[102:0]};
wire [24:0]  res26 = {res25,bit25};
wire [128:0] bin26 = bin25;
wire vld26 = vld25;


wire bit26 = (bin26 <= ain26[230:102]);
wire [128:0] xhigh26 = ain26[230:102]-bin26;
wire [127:0] high26 = bit26 ? xhigh26[127:0] : ain26[229:102] ;
wire [229:0]  pre_ain27 = {high26,ain26[101:0]};
wire [25:0]  pre_res27 = {res26,bit26};

reg [229:0] ain27;
always @(posedge clk) if (en) ain27 <= pre_ain27;
reg [128:0] bin27;
always @(posedge clk) if (en) bin27 <= bin26;
reg [25:0] res27;
always @(posedge clk) if (en) res27 <= pre_res27;
reg vld27;
always @(posedge clk) if (en) vld27 <= vld26; else vld27 <= 0;


wire bit27 = (bin27 <= ain27[229:101]);
wire [128:0] xhigh27 = ain27[229:101]-bin27;
wire [127:0] high27 = bit27 ? xhigh27[127:0] : ain27[228:101] ;
wire [228:0]  ain28 = {high27,ain27[100:0]};
wire [26:0]  res28 = {res27,bit27};
wire [128:0] bin28 = bin27;
wire vld28 = vld27;


wire bit28 = (bin28 <= ain28[228:100]);
wire [128:0] xhigh28 = ain28[228:100]-bin28;
wire [127:0] high28 = bit28 ? xhigh28[127:0] : ain28[227:100] ;
wire [227:0]  pre_ain29 = {high28,ain28[99:0]};
wire [27:0]  pre_res29 = {res28,bit28};

reg [227:0] ain29;
always @(posedge clk) if (en) ain29 <= pre_ain29;
reg [128:0] bin29;
always @(posedge clk) if (en) bin29 <= bin28;
reg [27:0] res29;
always @(posedge clk) if (en) res29 <= pre_res29;
reg vld29;
always @(posedge clk) if (en) vld29 <= vld28; else vld29 <= 0;


wire bit29 = (bin29 <= ain29[227:99]);
wire [128:0] xhigh29 = ain29[227:99]-bin29;
wire [127:0] high29 = bit29 ? xhigh29[127:0] : ain29[226:99] ;
wire [226:0]  ain30 = {high29,ain29[98:0]};
wire [28:0]  res30 = {res29,bit29};
wire [128:0] bin30 = bin29;
wire vld30 = vld29;


wire bit30 = (bin30 <= ain30[226:98]);
wire [128:0] xhigh30 = ain30[226:98]-bin30;
wire [127:0] high30 = bit30 ? xhigh30[127:0] : ain30[225:98] ;
wire [225:0]  pre_ain31 = {high30,ain30[97:0]};
wire [29:0]  pre_res31 = {res30,bit30};

reg [225:0] ain31;
always @(posedge clk) if (en) ain31 <= pre_ain31;
reg [128:0] bin31;
always @(posedge clk) if (en) bin31 <= bin30;
reg [29:0] res31;
always @(posedge clk) if (en) res31 <= pre_res31;
reg vld31;
always @(posedge clk) if (en) vld31 <= vld30; else vld31 <= 0;


wire bit31 = (bin31 <= ain31[225:97]);
wire [128:0] xhigh31 = ain31[225:97]-bin31;
wire [127:0] high31 = bit31 ? xhigh31[127:0] : ain31[224:97] ;
wire [224:0]  ain32 = {high31,ain31[96:0]};
wire [30:0]  res32 = {res31,bit31};
wire [128:0] bin32 = bin31;
wire vld32 = vld31;


wire bit32 = (bin32 <= ain32[224:96]);
wire [128:0] xhigh32 = ain32[224:96]-bin32;
wire [127:0] high32 = bit32 ? xhigh32[127:0] : ain32[223:96] ;
wire [223:0]  pre_ain33 = {high32,ain32[95:0]};
wire [31:0]  pre_res33 = {res32,bit32};

reg [223:0] ain33;
always @(posedge clk) if (en) ain33 <= pre_ain33;
reg [128:0] bin33;
always @(posedge clk) if (en) bin33 <= bin32;
reg [31:0] res33;
always @(posedge clk) if (en) res33 <= pre_res33;
reg vld33;
always @(posedge clk) if (en) vld33 <= vld32; else vld33 <= 0;


wire bit33 = (bin33 <= ain33[223:95]);
wire [128:0] xhigh33 = ain33[223:95]-bin33;
wire [127:0] high33 = bit33 ? xhigh33[127:0] : ain33[222:95] ;
wire [222:0]  ain34 = {high33,ain33[94:0]};
wire [32:0]  res34 = {res33,bit33};
wire [128:0] bin34 = bin33;
wire vld34 = vld33;


wire bit34 = (bin34 <= ain34[222:94]);
wire [128:0] xhigh34 = ain34[222:94]-bin34;
wire [127:0] high34 = bit34 ? xhigh34[127:0] : ain34[221:94] ;
wire [221:0]  pre_ain35 = {high34,ain34[93:0]};
wire [33:0]  pre_res35 = {res34,bit34};

reg [221:0] ain35;
always @(posedge clk) if (en) ain35 <= pre_ain35;
reg [128:0] bin35;
always @(posedge clk) if (en) bin35 <= bin34;
reg [33:0] res35;
always @(posedge clk) if (en) res35 <= pre_res35;
reg vld35;
always @(posedge clk) if (en) vld35 <= vld34; else vld35 <= 0;


wire bit35 = (bin35 <= ain35[221:93]);
wire [128:0] xhigh35 = ain35[221:93]-bin35;
wire [127:0] high35 = bit35 ? xhigh35[127:0] : ain35[220:93] ;
wire [220:0]  ain36 = {high35,ain35[92:0]};
wire [34:0]  res36 = {res35,bit35};
wire [128:0] bin36 = bin35;
wire vld36 = vld35;


wire bit36 = (bin36 <= ain36[220:92]);
wire [128:0] xhigh36 = ain36[220:92]-bin36;
wire [127:0] high36 = bit36 ? xhigh36[127:0] : ain36[219:92] ;
wire [219:0]  pre_ain37 = {high36,ain36[91:0]};
wire [35:0]  pre_res37 = {res36,bit36};

reg [219:0] ain37;
always @(posedge clk) if (en) ain37 <= pre_ain37;
reg [128:0] bin37;
always @(posedge clk) if (en) bin37 <= bin36;
reg [35:0] res37;
always @(posedge clk) if (en) res37 <= pre_res37;
reg vld37;
always @(posedge clk) if (en) vld37 <= vld36; else vld37 <= 0;


wire bit37 = (bin37 <= ain37[219:91]);
wire [128:0] xhigh37 = ain37[219:91]-bin37;
wire [127:0] high37 = bit37 ? xhigh37[127:0] : ain37[218:91] ;
wire [218:0]  ain38 = {high37,ain37[90:0]};
wire [36:0]  res38 = {res37,bit37};
wire [128:0] bin38 = bin37;
wire vld38 = vld37;


wire bit38 = (bin38 <= ain38[218:90]);
wire [128:0] xhigh38 = ain38[218:90]-bin38;
wire [127:0] high38 = bit38 ? xhigh38[127:0] : ain38[217:90] ;
wire [217:0]  pre_ain39 = {high38,ain38[89:0]};
wire [37:0]  pre_res39 = {res38,bit38};

reg [217:0] ain39;
always @(posedge clk) if (en) ain39 <= pre_ain39;
reg [128:0] bin39;
always @(posedge clk) if (en) bin39 <= bin38;
reg [37:0] res39;
always @(posedge clk) if (en) res39 <= pre_res39;
reg vld39;
always @(posedge clk) if (en) vld39 <= vld38; else vld39 <= 0;


wire bit39 = (bin39 <= ain39[217:89]);
wire [128:0] xhigh39 = ain39[217:89]-bin39;
wire [127:0] high39 = bit39 ? xhigh39[127:0] : ain39[216:89] ;
wire [216:0]  ain40 = {high39,ain39[88:0]};
wire [38:0]  res40 = {res39,bit39};
wire [128:0] bin40 = bin39;
wire vld40 = vld39;


wire bit40 = (bin40 <= ain40[216:88]);
wire [128:0] xhigh40 = ain40[216:88]-bin40;
wire [127:0] high40 = bit40 ? xhigh40[127:0] : ain40[215:88] ;
wire [215:0]  pre_ain41 = {high40,ain40[87:0]};
wire [39:0]  pre_res41 = {res40,bit40};

reg [215:0] ain41;
always @(posedge clk) if (en) ain41 <= pre_ain41;
reg [128:0] bin41;
always @(posedge clk) if (en) bin41 <= bin40;
reg [39:0] res41;
always @(posedge clk) if (en) res41 <= pre_res41;
reg vld41;
always @(posedge clk) if (en) vld41 <= vld40; else vld41 <= 0;


wire bit41 = (bin41 <= ain41[215:87]);
wire [128:0] xhigh41 = ain41[215:87]-bin41;
wire [127:0] high41 = bit41 ? xhigh41[127:0] : ain41[214:87] ;
wire [214:0]  ain42 = {high41,ain41[86:0]};
wire [40:0]  res42 = {res41,bit41};
wire [128:0] bin42 = bin41;
wire vld42 = vld41;


wire bit42 = (bin42 <= ain42[214:86]);
wire [128:0] xhigh42 = ain42[214:86]-bin42;
wire [127:0] high42 = bit42 ? xhigh42[127:0] : ain42[213:86] ;
wire [213:0]  pre_ain43 = {high42,ain42[85:0]};
wire [41:0]  pre_res43 = {res42,bit42};

reg [213:0] ain43;
always @(posedge clk) if (en) ain43 <= pre_ain43;
reg [128:0] bin43;
always @(posedge clk) if (en) bin43 <= bin42;
reg [41:0] res43;
always @(posedge clk) if (en) res43 <= pre_res43;
reg vld43;
always @(posedge clk) if (en) vld43 <= vld42; else vld43 <= 0;


wire bit43 = (bin43 <= ain43[213:85]);
wire [128:0] xhigh43 = ain43[213:85]-bin43;
wire [127:0] high43 = bit43 ? xhigh43[127:0] : ain43[212:85] ;
wire [212:0]  ain44 = {high43,ain43[84:0]};
wire [42:0]  res44 = {res43,bit43};
wire [128:0] bin44 = bin43;
wire vld44 = vld43;


wire bit44 = (bin44 <= ain44[212:84]);
wire [128:0] xhigh44 = ain44[212:84]-bin44;
wire [127:0] high44 = bit44 ? xhigh44[127:0] : ain44[211:84] ;
wire [211:0]  pre_ain45 = {high44,ain44[83:0]};
wire [43:0]  pre_res45 = {res44,bit44};

reg [211:0] ain45;
always @(posedge clk) if (en) ain45 <= pre_ain45;
reg [128:0] bin45;
always @(posedge clk) if (en) bin45 <= bin44;
reg [43:0] res45;
always @(posedge clk) if (en) res45 <= pre_res45;
reg vld45;
always @(posedge clk) if (en) vld45 <= vld44; else vld45 <= 0;


wire bit45 = (bin45 <= ain45[211:83]);
wire [128:0] xhigh45 = ain45[211:83]-bin45;
wire [127:0] high45 = bit45 ? xhigh45[127:0] : ain45[210:83] ;
wire [210:0]  ain46 = {high45,ain45[82:0]};
wire [44:0]  res46 = {res45,bit45};
wire [128:0] bin46 = bin45;
wire vld46 = vld45;


wire bit46 = (bin46 <= ain46[210:82]);
wire [128:0] xhigh46 = ain46[210:82]-bin46;
wire [127:0] high46 = bit46 ? xhigh46[127:0] : ain46[209:82] ;
wire [209:0]  pre_ain47 = {high46,ain46[81:0]};
wire [45:0]  pre_res47 = {res46,bit46};

reg [209:0] ain47;
always @(posedge clk) if (en) ain47 <= pre_ain47;
reg [128:0] bin47;
always @(posedge clk) if (en) bin47 <= bin46;
reg [45:0] res47;
always @(posedge clk) if (en) res47 <= pre_res47;
reg vld47;
always @(posedge clk) if (en) vld47 <= vld46; else vld47 <= 0;


wire bit47 = (bin47 <= ain47[209:81]);
wire [128:0] xhigh47 = ain47[209:81]-bin47;
wire [127:0] high47 = bit47 ? xhigh47[127:0] : ain47[208:81] ;
wire [208:0]  ain48 = {high47,ain47[80:0]};
wire [46:0]  res48 = {res47,bit47};
wire [128:0] bin48 = bin47;
wire vld48 = vld47;


wire bit48 = (bin48 <= ain48[208:80]);
wire [128:0] xhigh48 = ain48[208:80]-bin48;
wire [127:0] high48 = bit48 ? xhigh48[127:0] : ain48[207:80] ;
wire [207:0]  pre_ain49 = {high48,ain48[79:0]};
wire [47:0]  pre_res49 = {res48,bit48};

reg [207:0] ain49;
always @(posedge clk) if (en) ain49 <= pre_ain49;
reg [128:0] bin49;
always @(posedge clk) if (en) bin49 <= bin48;
reg [47:0] res49;
always @(posedge clk) if (en) res49 <= pre_res49;
reg vld49;
always @(posedge clk) if (en) vld49 <= vld48; else vld49 <= 0;


wire bit49 = (bin49 <= ain49[207:79]);
wire [128:0] xhigh49 = ain49[207:79]-bin49;
wire [127:0] high49 = bit49 ? xhigh49[127:0] : ain49[206:79] ;
wire [206:0]  ain50 = {high49,ain49[78:0]};
wire [48:0]  res50 = {res49,bit49};
wire [128:0] bin50 = bin49;
wire vld50 = vld49;


wire bit50 = (bin50 <= ain50[206:78]);
wire [128:0] xhigh50 = ain50[206:78]-bin50;
wire [127:0] high50 = bit50 ? xhigh50[127:0] : ain50[205:78] ;
wire [205:0]  pre_ain51 = {high50,ain50[77:0]};
wire [49:0]  pre_res51 = {res50,bit50};

reg [205:0] ain51;
always @(posedge clk) if (en) ain51 <= pre_ain51;
reg [128:0] bin51;
always @(posedge clk) if (en) bin51 <= bin50;
reg [49:0] res51;
always @(posedge clk) if (en) res51 <= pre_res51;
reg vld51;
always @(posedge clk) if (en) vld51 <= vld50; else vld51 <= 0;


wire bit51 = (bin51 <= ain51[205:77]);
wire [128:0] xhigh51 = ain51[205:77]-bin51;
wire [127:0] high51 = bit51 ? xhigh51[127:0] : ain51[204:77] ;
wire [204:0]  ain52 = {high51,ain51[76:0]};
wire [50:0]  res52 = {res51,bit51};
wire [128:0] bin52 = bin51;
wire vld52 = vld51;


wire bit52 = (bin52 <= ain52[204:76]);
wire [128:0] xhigh52 = ain52[204:76]-bin52;
wire [127:0] high52 = bit52 ? xhigh52[127:0] : ain52[203:76] ;
wire [203:0]  pre_ain53 = {high52,ain52[75:0]};
wire [51:0]  pre_res53 = {res52,bit52};

reg [203:0] ain53;
always @(posedge clk) if (en) ain53 <= pre_ain53;
reg [128:0] bin53;
always @(posedge clk) if (en) bin53 <= bin52;
reg [51:0] res53;
always @(posedge clk) if (en) res53 <= pre_res53;
reg vld53;
always @(posedge clk) if (en) vld53 <= vld52; else vld53 <= 0;


wire bit53 = (bin53 <= ain53[203:75]);
wire [128:0] xhigh53 = ain53[203:75]-bin53;
wire [127:0] high53 = bit53 ? xhigh53[127:0] : ain53[202:75] ;
wire [202:0]  ain54 = {high53,ain53[74:0]};
wire [52:0]  res54 = {res53,bit53};
wire [128:0] bin54 = bin53;
wire vld54 = vld53;


wire bit54 = (bin54 <= ain54[202:74]);
wire [128:0] xhigh54 = ain54[202:74]-bin54;
wire [127:0] high54 = bit54 ? xhigh54[127:0] : ain54[201:74] ;
wire [201:0]  pre_ain55 = {high54,ain54[73:0]};
wire [53:0]  pre_res55 = {res54,bit54};

reg [201:0] ain55;
always @(posedge clk) if (en) ain55 <= pre_ain55;
reg [128:0] bin55;
always @(posedge clk) if (en) bin55 <= bin54;
reg [53:0] res55;
always @(posedge clk) if (en) res55 <= pre_res55;
reg vld55;
always @(posedge clk) if (en) vld55 <= vld54; else vld55 <= 0;


wire bit55 = (bin55 <= ain55[201:73]);
wire [128:0] xhigh55 = ain55[201:73]-bin55;
wire [127:0] high55 = bit55 ? xhigh55[127:0] : ain55[200:73] ;
wire [200:0]  ain56 = {high55,ain55[72:0]};
wire [54:0]  res56 = {res55,bit55};
wire [128:0] bin56 = bin55;
wire vld56 = vld55;


wire bit56 = (bin56 <= ain56[200:72]);
wire [128:0] xhigh56 = ain56[200:72]-bin56;
wire [127:0] high56 = bit56 ? xhigh56[127:0] : ain56[199:72] ;
wire [199:0]  pre_ain57 = {high56,ain56[71:0]};
wire [55:0]  pre_res57 = {res56,bit56};

reg [199:0] ain57;
always @(posedge clk) if (en) ain57 <= pre_ain57;
reg [128:0] bin57;
always @(posedge clk) if (en) bin57 <= bin56;
reg [55:0] res57;
always @(posedge clk) if (en) res57 <= pre_res57;
reg vld57;
always @(posedge clk) if (en) vld57 <= vld56; else vld57 <= 0;


wire bit57 = (bin57 <= ain57[199:71]);
wire [128:0] xhigh57 = ain57[199:71]-bin57;
wire [127:0] high57 = bit57 ? xhigh57[127:0] : ain57[198:71] ;
wire [198:0]  ain58 = {high57,ain57[70:0]};
wire [56:0]  res58 = {res57,bit57};
wire [128:0] bin58 = bin57;
wire vld58 = vld57;


wire bit58 = (bin58 <= ain58[198:70]);
wire [128:0] xhigh58 = ain58[198:70]-bin58;
wire [127:0] high58 = bit58 ? xhigh58[127:0] : ain58[197:70] ;
wire [197:0]  pre_ain59 = {high58,ain58[69:0]};
wire [57:0]  pre_res59 = {res58,bit58};

reg [197:0] ain59;
always @(posedge clk) if (en) ain59 <= pre_ain59;
reg [128:0] bin59;
always @(posedge clk) if (en) bin59 <= bin58;
reg [57:0] res59;
always @(posedge clk) if (en) res59 <= pre_res59;
reg vld59;
always @(posedge clk) if (en) vld59 <= vld58; else vld59 <= 0;


wire bit59 = (bin59 <= ain59[197:69]);
wire [128:0] xhigh59 = ain59[197:69]-bin59;
wire [127:0] high59 = bit59 ? xhigh59[127:0] : ain59[196:69] ;
wire [196:0]  ain60 = {high59,ain59[68:0]};
wire [58:0]  res60 = {res59,bit59};
wire [128:0] bin60 = bin59;
wire vld60 = vld59;


wire bit60 = (bin60 <= ain60[196:68]);
wire [128:0] xhigh60 = ain60[196:68]-bin60;
wire [127:0] high60 = bit60 ? xhigh60[127:0] : ain60[195:68] ;
wire [195:0]  pre_ain61 = {high60,ain60[67:0]};
wire [59:0]  pre_res61 = {res60,bit60};

reg [195:0] ain61;
always @(posedge clk) if (en) ain61 <= pre_ain61;
reg [128:0] bin61;
always @(posedge clk) if (en) bin61 <= bin60;
reg [59:0] res61;
always @(posedge clk) if (en) res61 <= pre_res61;
reg vld61;
always @(posedge clk) if (en) vld61 <= vld60; else vld61 <= 0;


wire bit61 = (bin61 <= ain61[195:67]);
wire [128:0] xhigh61 = ain61[195:67]-bin61;
wire [127:0] high61 = bit61 ? xhigh61[127:0] : ain61[194:67] ;
wire [194:0]  ain62 = {high61,ain61[66:0]};
wire [60:0]  res62 = {res61,bit61};
wire [128:0] bin62 = bin61;
wire vld62 = vld61;


wire bit62 = (bin62 <= ain62[194:66]);
wire [128:0] xhigh62 = ain62[194:66]-bin62;
wire [127:0] high62 = bit62 ? xhigh62[127:0] : ain62[193:66] ;
wire [193:0]  pre_ain63 = {high62,ain62[65:0]};
wire [61:0]  pre_res63 = {res62,bit62};

reg [193:0] ain63;
always @(posedge clk) if (en) ain63 <= pre_ain63;
reg [128:0] bin63;
always @(posedge clk) if (en) bin63 <= bin62;
reg [61:0] res63;
always @(posedge clk) if (en) res63 <= pre_res63;
reg vld63;
always @(posedge clk) if (en) vld63 <= vld62; else vld63 <= 0;


wire bit63 = (bin63 <= ain63[193:65]);
wire [128:0] xhigh63 = ain63[193:65]-bin63;
wire [127:0] high63 = bit63 ? xhigh63[127:0] : ain63[192:65] ;
wire [192:0]  ain64 = {high63,ain63[64:0]};
wire [62:0]  res64 = {res63,bit63};
wire [128:0] bin64 = bin63;
wire vld64 = vld63;


wire bit64 = (bin64 <= ain64[192:64]);
wire [128:0] xhigh64 = ain64[192:64]-bin64;
wire [127:0] high64 = bit64 ? xhigh64[127:0] : ain64[191:64] ;
wire [191:0]  pre_ain65 = {high64,ain64[63:0]};
wire [63:0]  pre_res65 = {res64,bit64};

reg [191:0] ain65;
always @(posedge clk) if (en) ain65 <= pre_ain65;
reg [128:0] bin65;
always @(posedge clk) if (en) bin65 <= bin64;
reg [63:0] res65;
always @(posedge clk) if (en) res65 <= pre_res65;
reg vld65;
always @(posedge clk) if (en) vld65 <= vld64; else vld65 <= 0;


wire bit65 = (bin65 <= ain65[191:63]);
wire [128:0] xhigh65 = ain65[191:63]-bin65;
wire [127:0] high65 = bit65 ? xhigh65[127:0] : ain65[190:63] ;
wire [190:0]  ain66 = {high65,ain65[62:0]};
wire [64:0]  res66 = {res65,bit65};
wire [128:0] bin66 = bin65;
wire vld66 = vld65;


wire bit66 = (bin66 <= ain66[190:62]);
wire [128:0] xhigh66 = ain66[190:62]-bin66;
wire [127:0] high66 = bit66 ? xhigh66[127:0] : ain66[189:62] ;
wire [189:0]  pre_ain67 = {high66,ain66[61:0]};
wire [65:0]  pre_res67 = {res66,bit66};

reg [189:0] ain67;
always @(posedge clk) if (en) ain67 <= pre_ain67;
reg [128:0] bin67;
always @(posedge clk) if (en) bin67 <= bin66;
reg [65:0] res67;
always @(posedge clk) if (en) res67 <= pre_res67;
reg vld67;
always @(posedge clk) if (en) vld67 <= vld66; else vld67 <= 0;


wire bit67 = (bin67 <= ain67[189:61]);
wire [128:0] xhigh67 = ain67[189:61]-bin67;
wire [127:0] high67 = bit67 ? xhigh67[127:0] : ain67[188:61] ;
wire [188:0]  ain68 = {high67,ain67[60:0]};
wire [66:0]  res68 = {res67,bit67};
wire [128:0] bin68 = bin67;
wire vld68 = vld67;


wire bit68 = (bin68 <= ain68[188:60]);
wire [128:0] xhigh68 = ain68[188:60]-bin68;
wire [127:0] high68 = bit68 ? xhigh68[127:0] : ain68[187:60] ;
wire [187:0]  pre_ain69 = {high68,ain68[59:0]};
wire [67:0]  pre_res69 = {res68,bit68};

reg [187:0] ain69;
always @(posedge clk) if (en) ain69 <= pre_ain69;
reg [128:0] bin69;
always @(posedge clk) if (en) bin69 <= bin68;
reg [67:0] res69;
always @(posedge clk) if (en) res69 <= pre_res69;
reg vld69;
always @(posedge clk) if (en) vld69 <= vld68; else vld69 <= 0;


wire bit69 = (bin69 <= ain69[187:59]);
wire [128:0] xhigh69 = ain69[187:59]-bin69;
wire [127:0] high69 = bit69 ? xhigh69[127:0] : ain69[186:59] ;
wire [186:0]  ain70 = {high69,ain69[58:0]};
wire [68:0]  res70 = {res69,bit69};
wire [128:0] bin70 = bin69;
wire vld70 = vld69;


wire bit70 = (bin70 <= ain70[186:58]);
wire [128:0] xhigh70 = ain70[186:58]-bin70;
wire [127:0] high70 = bit70 ? xhigh70[127:0] : ain70[185:58] ;
wire [185:0]  pre_ain71 = {high70,ain70[57:0]};
wire [69:0]  pre_res71 = {res70,bit70};

reg [185:0] ain71;
always @(posedge clk) if (en) ain71 <= pre_ain71;
reg [128:0] bin71;
always @(posedge clk) if (en) bin71 <= bin70;
reg [69:0] res71;
always @(posedge clk) if (en) res71 <= pre_res71;
reg vld71;
always @(posedge clk) if (en) vld71 <= vld70; else vld71 <= 0;


wire bit71 = (bin71 <= ain71[185:57]);
wire [128:0] xhigh71 = ain71[185:57]-bin71;
wire [127:0] high71 = bit71 ? xhigh71[127:0] : ain71[184:57] ;
wire [184:0]  ain72 = {high71,ain71[56:0]};
wire [70:0]  res72 = {res71,bit71};
wire [128:0] bin72 = bin71;
wire vld72 = vld71;


wire bit72 = (bin72 <= ain72[184:56]);
wire [128:0] xhigh72 = ain72[184:56]-bin72;
wire [127:0] high72 = bit72 ? xhigh72[127:0] : ain72[183:56] ;
wire [183:0]  pre_ain73 = {high72,ain72[55:0]};
wire [71:0]  pre_res73 = {res72,bit72};

reg [183:0] ain73;
always @(posedge clk) if (en) ain73 <= pre_ain73;
reg [128:0] bin73;
always @(posedge clk) if (en) bin73 <= bin72;
reg [71:0] res73;
always @(posedge clk) if (en) res73 <= pre_res73;
reg vld73;
always @(posedge clk) if (en) vld73 <= vld72; else vld73 <= 0;


wire bit73 = (bin73 <= ain73[183:55]);
wire [128:0] xhigh73 = ain73[183:55]-bin73;
wire [127:0] high73 = bit73 ? xhigh73[127:0] : ain73[182:55] ;
wire [182:0]  ain74 = {high73,ain73[54:0]};
wire [72:0]  res74 = {res73,bit73};
wire [128:0] bin74 = bin73;
wire vld74 = vld73;


wire bit74 = (bin74 <= ain74[182:54]);
wire [128:0] xhigh74 = ain74[182:54]-bin74;
wire [127:0] high74 = bit74 ? xhigh74[127:0] : ain74[181:54] ;
wire [181:0]  pre_ain75 = {high74,ain74[53:0]};
wire [73:0]  pre_res75 = {res74,bit74};

reg [181:0] ain75;
always @(posedge clk) if (en) ain75 <= pre_ain75;
reg [128:0] bin75;
always @(posedge clk) if (en) bin75 <= bin74;
reg [73:0] res75;
always @(posedge clk) if (en) res75 <= pre_res75;
reg vld75;
always @(posedge clk) if (en) vld75 <= vld74; else vld75 <= 0;


wire bit75 = (bin75 <= ain75[181:53]);
wire [128:0] xhigh75 = ain75[181:53]-bin75;
wire [127:0] high75 = bit75 ? xhigh75[127:0] : ain75[180:53] ;
wire [180:0]  ain76 = {high75,ain75[52:0]};
wire [74:0]  res76 = {res75,bit75};
wire [128:0] bin76 = bin75;
wire vld76 = vld75;


wire bit76 = (bin76 <= ain76[180:52]);
wire [128:0] xhigh76 = ain76[180:52]-bin76;
wire [127:0] high76 = bit76 ? xhigh76[127:0] : ain76[179:52] ;
wire [179:0]  pre_ain77 = {high76,ain76[51:0]};
wire [75:0]  pre_res77 = {res76,bit76};

reg [179:0] ain77;
always @(posedge clk) if (en) ain77 <= pre_ain77;
reg [128:0] bin77;
always @(posedge clk) if (en) bin77 <= bin76;
reg [75:0] res77;
always @(posedge clk) if (en) res77 <= pre_res77;
reg vld77;
always @(posedge clk) if (en) vld77 <= vld76; else vld77 <= 0;


wire bit77 = (bin77 <= ain77[179:51]);
wire [128:0] xhigh77 = ain77[179:51]-bin77;
wire [127:0] high77 = bit77 ? xhigh77[127:0] : ain77[178:51] ;
wire [178:0]  ain78 = {high77,ain77[50:0]};
wire [76:0]  res78 = {res77,bit77};
wire [128:0] bin78 = bin77;
wire vld78 = vld77;


wire bit78 = (bin78 <= ain78[178:50]);
wire [128:0] xhigh78 = ain78[178:50]-bin78;
wire [127:0] high78 = bit78 ? xhigh78[127:0] : ain78[177:50] ;
wire [177:0]  pre_ain79 = {high78,ain78[49:0]};
wire [77:0]  pre_res79 = {res78,bit78};

reg [177:0] ain79;
always @(posedge clk) if (en) ain79 <= pre_ain79;
reg [128:0] bin79;
always @(posedge clk) if (en) bin79 <= bin78;
reg [77:0] res79;
always @(posedge clk) if (en) res79 <= pre_res79;
reg vld79;
always @(posedge clk) if (en) vld79 <= vld78; else vld79 <= 0;


wire bit79 = (bin79 <= ain79[177:49]);
wire [128:0] xhigh79 = ain79[177:49]-bin79;
wire [127:0] high79 = bit79 ? xhigh79[127:0] : ain79[176:49] ;
wire [176:0]  ain80 = {high79,ain79[48:0]};
wire [78:0]  res80 = {res79,bit79};
wire [128:0] bin80 = bin79;
wire vld80 = vld79;


wire bit80 = (bin80 <= ain80[176:48]);
wire [128:0] xhigh80 = ain80[176:48]-bin80;
wire [127:0] high80 = bit80 ? xhigh80[127:0] : ain80[175:48] ;
wire [175:0]  pre_ain81 = {high80,ain80[47:0]};
wire [79:0]  pre_res81 = {res80,bit80};

reg [175:0] ain81;
always @(posedge clk) if (en) ain81 <= pre_ain81;
reg [128:0] bin81;
always @(posedge clk) if (en) bin81 <= bin80;
reg [79:0] res81;
always @(posedge clk) if (en) res81 <= pre_res81;
reg vld81;
always @(posedge clk) if (en) vld81 <= vld80; else vld81 <= 0;


wire bit81 = (bin81 <= ain81[175:47]);
wire [128:0] xhigh81 = ain81[175:47]-bin81;
wire [127:0] high81 = bit81 ? xhigh81[127:0] : ain81[174:47] ;
wire [174:0]  ain82 = {high81,ain81[46:0]};
wire [80:0]  res82 = {res81,bit81};
wire [128:0] bin82 = bin81;
wire vld82 = vld81;


wire bit82 = (bin82 <= ain82[174:46]);
wire [128:0] xhigh82 = ain82[174:46]-bin82;
wire [127:0] high82 = bit82 ? xhigh82[127:0] : ain82[173:46] ;
wire [173:0]  pre_ain83 = {high82,ain82[45:0]};
wire [81:0]  pre_res83 = {res82,bit82};

reg [173:0] ain83;
always @(posedge clk) if (en) ain83 <= pre_ain83;
reg [128:0] bin83;
always @(posedge clk) if (en) bin83 <= bin82;
reg [81:0] res83;
always @(posedge clk) if (en) res83 <= pre_res83;
reg vld83;
always @(posedge clk) if (en) vld83 <= vld82; else vld83 <= 0;


wire bit83 = (bin83 <= ain83[173:45]);
wire [128:0] xhigh83 = ain83[173:45]-bin83;
wire [127:0] high83 = bit83 ? xhigh83[127:0] : ain83[172:45] ;
wire [172:0]  ain84 = {high83,ain83[44:0]};
wire [82:0]  res84 = {res83,bit83};
wire [128:0] bin84 = bin83;
wire vld84 = vld83;


wire bit84 = (bin84 <= ain84[172:44]);
wire [128:0] xhigh84 = ain84[172:44]-bin84;
wire [127:0] high84 = bit84 ? xhigh84[127:0] : ain84[171:44] ;
wire [171:0]  pre_ain85 = {high84,ain84[43:0]};
wire [83:0]  pre_res85 = {res84,bit84};

reg [171:0] ain85;
always @(posedge clk) if (en) ain85 <= pre_ain85;
reg [128:0] bin85;
always @(posedge clk) if (en) bin85 <= bin84;
reg [83:0] res85;
always @(posedge clk) if (en) res85 <= pre_res85;
reg vld85;
always @(posedge clk) if (en) vld85 <= vld84; else vld85 <= 0;


wire bit85 = (bin85 <= ain85[171:43]);
wire [128:0] xhigh85 = ain85[171:43]-bin85;
wire [127:0] high85 = bit85 ? xhigh85[127:0] : ain85[170:43] ;
wire [170:0]  ain86 = {high85,ain85[42:0]};
wire [84:0]  res86 = {res85,bit85};
wire [128:0] bin86 = bin85;
wire vld86 = vld85;


wire bit86 = (bin86 <= ain86[170:42]);
wire [128:0] xhigh86 = ain86[170:42]-bin86;
wire [127:0] high86 = bit86 ? xhigh86[127:0] : ain86[169:42] ;
wire [169:0]  pre_ain87 = {high86,ain86[41:0]};
wire [85:0]  pre_res87 = {res86,bit86};

reg [169:0] ain87;
always @(posedge clk) if (en) ain87 <= pre_ain87;
reg [128:0] bin87;
always @(posedge clk) if (en) bin87 <= bin86;
reg [85:0] res87;
always @(posedge clk) if (en) res87 <= pre_res87;
reg vld87;
always @(posedge clk) if (en) vld87 <= vld86; else vld87 <= 0;


wire bit87 = (bin87 <= ain87[169:41]);
wire [128:0] xhigh87 = ain87[169:41]-bin87;
wire [127:0] high87 = bit87 ? xhigh87[127:0] : ain87[168:41] ;
wire [168:0]  ain88 = {high87,ain87[40:0]};
wire [86:0]  res88 = {res87,bit87};
wire [128:0] bin88 = bin87;
wire vld88 = vld87;


wire bit88 = (bin88 <= ain88[168:40]);
wire [128:0] xhigh88 = ain88[168:40]-bin88;
wire [127:0] high88 = bit88 ? xhigh88[127:0] : ain88[167:40] ;
wire [167:0]  pre_ain89 = {high88,ain88[39:0]};
wire [87:0]  pre_res89 = {res88,bit88};

reg [167:0] ain89;
always @(posedge clk) if (en) ain89 <= pre_ain89;
reg [128:0] bin89;
always @(posedge clk) if (en) bin89 <= bin88;
reg [87:0] res89;
always @(posedge clk) if (en) res89 <= pre_res89;
reg vld89;
always @(posedge clk) if (en) vld89 <= vld88; else vld89 <= 0;


wire bit89 = (bin89 <= ain89[167:39]);
wire [128:0] xhigh89 = ain89[167:39]-bin89;
wire [127:0] high89 = bit89 ? xhigh89[127:0] : ain89[166:39] ;
wire [166:0]  ain90 = {high89,ain89[38:0]};
wire [88:0]  res90 = {res89,bit89};
wire [128:0] bin90 = bin89;
wire vld90 = vld89;


wire bit90 = (bin90 <= ain90[166:38]);
wire [128:0] xhigh90 = ain90[166:38]-bin90;
wire [127:0] high90 = bit90 ? xhigh90[127:0] : ain90[165:38] ;
wire [165:0]  pre_ain91 = {high90,ain90[37:0]};
wire [89:0]  pre_res91 = {res90,bit90};

reg [165:0] ain91;
always @(posedge clk) if (en) ain91 <= pre_ain91;
reg [128:0] bin91;
always @(posedge clk) if (en) bin91 <= bin90;
reg [89:0] res91;
always @(posedge clk) if (en) res91 <= pre_res91;
reg vld91;
always @(posedge clk) if (en) vld91 <= vld90; else vld91 <= 0;


wire bit91 = (bin91 <= ain91[165:37]);
wire [128:0] xhigh91 = ain91[165:37]-bin91;
wire [127:0] high91 = bit91 ? xhigh91[127:0] : ain91[164:37] ;
wire [164:0]  ain92 = {high91,ain91[36:0]};
wire [90:0]  res92 = {res91,bit91};
wire [128:0] bin92 = bin91;
wire vld92 = vld91;


wire bit92 = (bin92 <= ain92[164:36]);
wire [128:0] xhigh92 = ain92[164:36]-bin92;
wire [127:0] high92 = bit92 ? xhigh92[127:0] : ain92[163:36] ;
wire [163:0]  pre_ain93 = {high92,ain92[35:0]};
wire [91:0]  pre_res93 = {res92,bit92};

reg [163:0] ain93;
always @(posedge clk) if (en) ain93 <= pre_ain93;
reg [128:0] bin93;
always @(posedge clk) if (en) bin93 <= bin92;
reg [91:0] res93;
always @(posedge clk) if (en) res93 <= pre_res93;
reg vld93;
always @(posedge clk) if (en) vld93 <= vld92; else vld93 <= 0;


wire bit93 = (bin93 <= ain93[163:35]);
wire [128:0] xhigh93 = ain93[163:35]-bin93;
wire [127:0] high93 = bit93 ? xhigh93[127:0] : ain93[162:35] ;
wire [162:0]  ain94 = {high93,ain93[34:0]};
wire [92:0]  res94 = {res93,bit93};
wire [128:0] bin94 = bin93;
wire vld94 = vld93;


wire bit94 = (bin94 <= ain94[162:34]);
wire [128:0] xhigh94 = ain94[162:34]-bin94;
wire [127:0] high94 = bit94 ? xhigh94[127:0] : ain94[161:34] ;
wire [161:0]  pre_ain95 = {high94,ain94[33:0]};
wire [93:0]  pre_res95 = {res94,bit94};

reg [161:0] ain95;
always @(posedge clk) if (en) ain95 <= pre_ain95;
reg [128:0] bin95;
always @(posedge clk) if (en) bin95 <= bin94;
reg [93:0] res95;
always @(posedge clk) if (en) res95 <= pre_res95;
reg vld95;
always @(posedge clk) if (en) vld95 <= vld94; else vld95 <= 0;


wire bit95 = (bin95 <= ain95[161:33]);
wire [128:0] xhigh95 = ain95[161:33]-bin95;
wire [127:0] high95 = bit95 ? xhigh95[127:0] : ain95[160:33] ;
wire [160:0]  ain96 = {high95,ain95[32:0]};
wire [94:0]  res96 = {res95,bit95};
wire [128:0] bin96 = bin95;
wire vld96 = vld95;


wire bit96 = (bin96 <= ain96[160:32]);
wire [128:0] xhigh96 = ain96[160:32]-bin96;
wire [127:0] high96 = bit96 ? xhigh96[127:0] : ain96[159:32] ;
wire [159:0]  pre_ain97 = {high96,ain96[31:0]};
wire [95:0]  pre_res97 = {res96,bit96};

reg [159:0] ain97;
always @(posedge clk) if (en) ain97 <= pre_ain97;
reg [128:0] bin97;
always @(posedge clk) if (en) bin97 <= bin96;
reg [95:0] res97;
always @(posedge clk) if (en) res97 <= pre_res97;
reg vld97;
always @(posedge clk) if (en) vld97 <= vld96; else vld97 <= 0;


wire bit97 = (bin97 <= ain97[159:31]);
wire [128:0] xhigh97 = ain97[159:31]-bin97;
wire [127:0] high97 = bit97 ? xhigh97[127:0] : ain97[158:31] ;
wire [158:0]  ain98 = {high97,ain97[30:0]};
wire [96:0]  res98 = {res97,bit97};
wire [128:0] bin98 = bin97;
wire vld98 = vld97;


wire bit98 = (bin98 <= ain98[158:30]);
wire [128:0] xhigh98 = ain98[158:30]-bin98;
wire [127:0] high98 = bit98 ? xhigh98[127:0] : ain98[157:30] ;
wire [157:0]  pre_ain99 = {high98,ain98[29:0]};
wire [97:0]  pre_res99 = {res98,bit98};

reg [157:0] ain99;
always @(posedge clk) if (en) ain99 <= pre_ain99;
reg [128:0] bin99;
always @(posedge clk) if (en) bin99 <= bin98;
reg [97:0] res99;
always @(posedge clk) if (en) res99 <= pre_res99;
reg vld99;
always @(posedge clk) if (en) vld99 <= vld98; else vld99 <= 0;


wire bit99 = (bin99 <= ain99[157:29]);
wire [128:0] xhigh99 = ain99[157:29]-bin99;
wire [127:0] high99 = bit99 ? xhigh99[127:0] : ain99[156:29] ;
wire [156:0]  ain100 = {high99,ain99[28:0]};
wire [98:0]  res100 = {res99,bit99};
wire [128:0] bin100 = bin99;
wire vld100 = vld99;


wire bit100 = (bin100 <= ain100[156:28]);
wire [128:0] xhigh100 = ain100[156:28]-bin100;
wire [127:0] high100 = bit100 ? xhigh100[127:0] : ain100[155:28] ;
wire [155:0]  pre_ain101 = {high100,ain100[27:0]};
wire [99:0]  pre_res101 = {res100,bit100};

reg [155:0] ain101;
always @(posedge clk) if (en) ain101 <= pre_ain101;
reg [128:0] bin101;
always @(posedge clk) if (en) bin101 <= bin100;
reg [99:0] res101;
always @(posedge clk) if (en) res101 <= pre_res101;
reg vld101;
always @(posedge clk) if (en) vld101 <= vld100; else vld101 <= 0;


wire bit101 = (bin101 <= ain101[155:27]);
wire [128:0] xhigh101 = ain101[155:27]-bin101;
wire [127:0] high101 = bit101 ? xhigh101[127:0] : ain101[154:27] ;
wire [154:0]  ain102 = {high101,ain101[26:0]};
wire [100:0]  res102 = {res101,bit101};
wire [128:0] bin102 = bin101;
wire vld102 = vld101;


wire bit102 = (bin102 <= ain102[154:26]);
wire [128:0] xhigh102 = ain102[154:26]-bin102;
wire [127:0] high102 = bit102 ? xhigh102[127:0] : ain102[153:26] ;
wire [153:0]  pre_ain103 = {high102,ain102[25:0]};
wire [101:0]  pre_res103 = {res102,bit102};

reg [153:0] ain103;
always @(posedge clk) if (en) ain103 <= pre_ain103;
reg [128:0] bin103;
always @(posedge clk) if (en) bin103 <= bin102;
reg [101:0] res103;
always @(posedge clk) if (en) res103 <= pre_res103;
reg vld103;
always @(posedge clk) if (en) vld103 <= vld102; else vld103 <= 0;


wire bit103 = (bin103 <= ain103[153:25]);
wire [128:0] xhigh103 = ain103[153:25]-bin103;
wire [127:0] high103 = bit103 ? xhigh103[127:0] : ain103[152:25] ;
wire [152:0]  ain104 = {high103,ain103[24:0]};
wire [102:0]  res104 = {res103,bit103};
wire [128:0] bin104 = bin103;
wire vld104 = vld103;


wire bit104 = (bin104 <= ain104[152:24]);
wire [128:0] xhigh104 = ain104[152:24]-bin104;
wire [127:0] high104 = bit104 ? xhigh104[127:0] : ain104[151:24] ;
wire [151:0]  pre_ain105 = {high104,ain104[23:0]};
wire [103:0]  pre_res105 = {res104,bit104};

reg [151:0] ain105;
always @(posedge clk) if (en) ain105 <= pre_ain105;
reg [128:0] bin105;
always @(posedge clk) if (en) bin105 <= bin104;
reg [103:0] res105;
always @(posedge clk) if (en) res105 <= pre_res105;
reg vld105;
always @(posedge clk) if (en) vld105 <= vld104; else vld105 <= 0;


wire bit105 = (bin105 <= ain105[151:23]);
wire [128:0] xhigh105 = ain105[151:23]-bin105;
wire [127:0] high105 = bit105 ? xhigh105[127:0] : ain105[150:23] ;
wire [150:0]  ain106 = {high105,ain105[22:0]};
wire [104:0]  res106 = {res105,bit105};
wire [128:0] bin106 = bin105;
wire vld106 = vld105;


wire bit106 = (bin106 <= ain106[150:22]);
wire [128:0] xhigh106 = ain106[150:22]-bin106;
wire [127:0] high106 = bit106 ? xhigh106[127:0] : ain106[149:22] ;
wire [149:0]  pre_ain107 = {high106,ain106[21:0]};
wire [105:0]  pre_res107 = {res106,bit106};

reg [149:0] ain107;
always @(posedge clk) if (en) ain107 <= pre_ain107;
reg [128:0] bin107;
always @(posedge clk) if (en) bin107 <= bin106;
reg [105:0] res107;
always @(posedge clk) if (en) res107 <= pre_res107;
reg vld107;
always @(posedge clk) if (en) vld107 <= vld106; else vld107 <= 0;


wire bit107 = (bin107 <= ain107[149:21]);
wire [128:0] xhigh107 = ain107[149:21]-bin107;
wire [127:0] high107 = bit107 ? xhigh107[127:0] : ain107[148:21] ;
wire [148:0]  ain108 = {high107,ain107[20:0]};
wire [106:0]  res108 = {res107,bit107};
wire [128:0] bin108 = bin107;
wire vld108 = vld107;


wire bit108 = (bin108 <= ain108[148:20]);
wire [128:0] xhigh108 = ain108[148:20]-bin108;
wire [127:0] high108 = bit108 ? xhigh108[127:0] : ain108[147:20] ;
wire [147:0]  pre_ain109 = {high108,ain108[19:0]};
wire [107:0]  pre_res109 = {res108,bit108};

reg [147:0] ain109;
always @(posedge clk) if (en) ain109 <= pre_ain109;
reg [128:0] bin109;
always @(posedge clk) if (en) bin109 <= bin108;
reg [107:0] res109;
always @(posedge clk) if (en) res109 <= pre_res109;
reg vld109;
always @(posedge clk) if (en) vld109 <= vld108; else vld109 <= 0;


wire bit109 = (bin109 <= ain109[147:19]);
wire [128:0] xhigh109 = ain109[147:19]-bin109;
wire [127:0] high109 = bit109 ? xhigh109[127:0] : ain109[146:19] ;
wire [146:0]  ain110 = {high109,ain109[18:0]};
wire [108:0]  res110 = {res109,bit109};
wire [128:0] bin110 = bin109;
wire vld110 = vld109;


wire bit110 = (bin110 <= ain110[146:18]);
wire [128:0] xhigh110 = ain110[146:18]-bin110;
wire [127:0] high110 = bit110 ? xhigh110[127:0] : ain110[145:18] ;
wire [145:0]  pre_ain111 = {high110,ain110[17:0]};
wire [109:0]  pre_res111 = {res110,bit110};

reg [145:0] ain111;
always @(posedge clk) if (en) ain111 <= pre_ain111;
reg [128:0] bin111;
always @(posedge clk) if (en) bin111 <= bin110;
reg [109:0] res111;
always @(posedge clk) if (en) res111 <= pre_res111;
reg vld111;
always @(posedge clk) if (en) vld111 <= vld110; else vld111 <= 0;


wire bit111 = (bin111 <= ain111[145:17]);
wire [128:0] xhigh111 = ain111[145:17]-bin111;
wire [127:0] high111 = bit111 ? xhigh111[127:0] : ain111[144:17] ;
wire [144:0]  ain112 = {high111,ain111[16:0]};
wire [110:0]  res112 = {res111,bit111};
wire [128:0] bin112 = bin111;
wire vld112 = vld111;


wire bit112 = (bin112 <= ain112[144:16]);
wire [128:0] xhigh112 = ain112[144:16]-bin112;
wire [127:0] high112 = bit112 ? xhigh112[127:0] : ain112[143:16] ;
wire [143:0]  pre_ain113 = {high112,ain112[15:0]};
wire [111:0]  pre_res113 = {res112,bit112};

reg [143:0] ain113;
always @(posedge clk) if (en) ain113 <= pre_ain113;
reg [128:0] bin113;
always @(posedge clk) if (en) bin113 <= bin112;
reg [111:0] res113;
always @(posedge clk) if (en) res113 <= pre_res113;
reg vld113;
always @(posedge clk) if (en) vld113 <= vld112; else vld113 <= 0;


wire bit113 = (bin113 <= ain113[143:15]);
wire [128:0] xhigh113 = ain113[143:15]-bin113;
wire [127:0] high113 = bit113 ? xhigh113[127:0] : ain113[142:15] ;
wire [142:0]  ain114 = {high113,ain113[14:0]};
wire [112:0]  res114 = {res113,bit113};
wire [128:0] bin114 = bin113;
wire vld114 = vld113;


wire bit114 = (bin114 <= ain114[142:14]);
wire [128:0] xhigh114 = ain114[142:14]-bin114;
wire [127:0] high114 = bit114 ? xhigh114[127:0] : ain114[141:14] ;
wire [141:0]  pre_ain115 = {high114,ain114[13:0]};
wire [113:0]  pre_res115 = {res114,bit114};

reg [141:0] ain115;
always @(posedge clk) if (en) ain115 <= pre_ain115;
reg [128:0] bin115;
always @(posedge clk) if (en) bin115 <= bin114;
reg [113:0] res115;
always @(posedge clk) if (en) res115 <= pre_res115;
reg vld115;
always @(posedge clk) if (en) vld115 <= vld114; else vld115 <= 0;


wire bit115 = (bin115 <= ain115[141:13]);
wire [128:0] xhigh115 = ain115[141:13]-bin115;
wire [127:0] high115 = bit115 ? xhigh115[127:0] : ain115[140:13] ;
wire [140:0]  ain116 = {high115,ain115[12:0]};
wire [114:0]  res116 = {res115,bit115};
wire [128:0] bin116 = bin115;
wire vld116 = vld115;


wire bit116 = (bin116 <= ain116[140:12]);
wire [128:0] xhigh116 = ain116[140:12]-bin116;
wire [127:0] high116 = bit116 ? xhigh116[127:0] : ain116[139:12] ;
wire [139:0]  pre_ain117 = {high116,ain116[11:0]};
wire [115:0]  pre_res117 = {res116,bit116};

reg [139:0] ain117;
always @(posedge clk) if (en) ain117 <= pre_ain117;
reg [128:0] bin117;
always @(posedge clk) if (en) bin117 <= bin116;
reg [115:0] res117;
always @(posedge clk) if (en) res117 <= pre_res117;
reg vld117;
always @(posedge clk) if (en) vld117 <= vld116; else vld117 <= 0;


wire bit117 = (bin117 <= ain117[139:11]);
wire [128:0] xhigh117 = ain117[139:11]-bin117;
wire [127:0] high117 = bit117 ? xhigh117[127:0] : ain117[138:11] ;
wire [138:0]  ain118 = {high117,ain117[10:0]};
wire [116:0]  res118 = {res117,bit117};
wire [128:0] bin118 = bin117;
wire vld118 = vld117;


wire bit118 = (bin118 <= ain118[138:10]);
wire [128:0] xhigh118 = ain118[138:10]-bin118;
wire [127:0] high118 = bit118 ? xhigh118[127:0] : ain118[137:10] ;
wire [137:0]  pre_ain119 = {high118,ain118[9:0]};
wire [117:0]  pre_res119 = {res118,bit118};

reg [137:0] ain119;
always @(posedge clk) if (en) ain119 <= pre_ain119;
reg [128:0] bin119;
always @(posedge clk) if (en) bin119 <= bin118;
reg [117:0] res119;
always @(posedge clk) if (en) res119 <= pre_res119;
reg vld119;
always @(posedge clk) if (en) vld119 <= vld118; else vld119 <= 0;


wire bit119 = (bin119 <= ain119[137:9]);
wire [128:0] xhigh119 = ain119[137:9]-bin119;
wire [127:0] high119 = bit119 ? xhigh119[127:0] : ain119[136:9] ;
wire [136:0]  ain120 = {high119,ain119[8:0]};
wire [118:0]  res120 = {res119,bit119};
wire [128:0] bin120 = bin119;
wire vld120 = vld119;


wire bit120 = (bin120 <= ain120[136:8]);
wire [128:0] xhigh120 = ain120[136:8]-bin120;
wire [127:0] high120 = bit120 ? xhigh120[127:0] : ain120[135:8] ;
wire [135:0]  pre_ain121 = {high120,ain120[7:0]};
wire [119:0]  pre_res121 = {res120,bit120};

reg [135:0] ain121;
always @(posedge clk) if (en) ain121 <= pre_ain121;
reg [128:0] bin121;
always @(posedge clk) if (en) bin121 <= bin120;
reg [119:0] res121;
always @(posedge clk) if (en) res121 <= pre_res121;
reg vld121;
always @(posedge clk) if (en) vld121 <= vld120; else vld121 <= 0;


wire bit121 = (bin121 <= ain121[135:7]);
wire [128:0] xhigh121 = ain121[135:7]-bin121;
wire [127:0] high121 = bit121 ? xhigh121[127:0] : ain121[134:7] ;
wire [134:0]  ain122 = {high121,ain121[6:0]};
wire [120:0]  res122 = {res121,bit121};
wire [128:0] bin122 = bin121;
wire vld122 = vld121;


wire bit122 = (bin122 <= ain122[134:6]);
wire [128:0] xhigh122 = ain122[134:6]-bin122;
wire [127:0] high122 = bit122 ? xhigh122[127:0] : ain122[133:6] ;
wire [133:0]  pre_ain123 = {high122,ain122[5:0]};
wire [121:0]  pre_res123 = {res122,bit122};

reg [133:0] ain123;
always @(posedge clk) if (en) ain123 <= pre_ain123;
reg [128:0] bin123;
always @(posedge clk) if (en) bin123 <= bin122;
reg [121:0] res123;
always @(posedge clk) if (en) res123 <= pre_res123;
reg vld123;
always @(posedge clk) if (en) vld123 <= vld122; else vld123 <= 0;


wire bit123 = (bin123 <= ain123[133:5]);
wire [128:0] xhigh123 = ain123[133:5]-bin123;
wire [127:0] high123 = bit123 ? xhigh123[127:0] : ain123[132:5] ;
wire [132:0]  ain124 = {high123,ain123[4:0]};
wire [122:0]  res124 = {res123,bit123};
wire [128:0] bin124 = bin123;
wire vld124 = vld123;


wire bit124 = (bin124 <= ain124[132:4]);
wire [128:0] xhigh124 = ain124[132:4]-bin124;
wire [127:0] high124 = bit124 ? xhigh124[127:0] : ain124[131:4] ;
wire [131:0]  pre_ain125 = {high124,ain124[3:0]};
wire [123:0]  pre_res125 = {res124,bit124};

reg [131:0] ain125;
always @(posedge clk) if (en) ain125 <= pre_ain125;
reg [128:0] bin125;
always @(posedge clk) if (en) bin125 <= bin124;
reg [123:0] res125;
always @(posedge clk) if (en) res125 <= pre_res125;
reg vld125;
always @(posedge clk) if (en) vld125 <= vld124; else vld125 <= 0;


wire bit125 = (bin125 <= ain125[131:3]);
wire [128:0] xhigh125 = ain125[131:3]-bin125;
wire [127:0] high125 = bit125 ? xhigh125[127:0] : ain125[130:3] ;
wire [130:0]  ain126 = {high125,ain125[2:0]};
wire [124:0]  res126 = {res125,bit125};
wire [128:0] bin126 = bin125;
wire vld126 = vld125;


wire bit126 = (bin126 <= ain126[130:2]);
wire [128:0] xhigh126 = ain126[130:2]-bin126;
wire [127:0] high126 = bit126 ? xhigh126[127:0] : ain126[129:2] ;
wire [129:0]  pre_ain127 = {high126,ain126[1:0]};
wire [125:0]  pre_res127 = {res126,bit126};

reg [129:0] ain127;
always @(posedge clk) if (en) ain127 <= pre_ain127;
reg [128:0] bin127;
always @(posedge clk) if (en) bin127 <= bin126;
reg [125:0] res127;
always @(posedge clk) if (en) res127 <= pre_res127;
reg vld127;
always @(posedge clk) if (en) vld127 <= vld126; else vld127 <= 0;


wire bit127 = (bin127 <= ain127[129:1]);
wire [128:0] xhigh127 = ain127[129:1]-bin127;
wire [127:0] high127 = bit127 ? xhigh127[127:0] : ain127[128:1] ;
wire [128:0]  ain128 = {high127,ain127[0]};
wire [126:0]  res128 = {res127,bit127};
wire [128:0] bin128 = bin127;
wire vld128 = vld127;


wire bit128 = (bin128 <= ain128[128:0]);
wire [128:0] xhigh128 = ain128[128:0]-bin128;
wire [127:0] high128 = bit128 ? xhigh128[127:0] : ain128[127:0] ;
wire [127:0]  ain129 = high128;
wire [127:0]  res129 = {res128,bit128};
wire [128:0] bin129 = bin128;
wire vld129 = vld128;
wire [127:0] res000 = (bin129==0) ? 128'b0 : res129 ;
always @(posedge clk) if (en) out <= res000;
always @(posedge clk) if (en) remainder <= ain129;
always @(posedge clk) if (en) vldout <= vld129; else vldout <= 0;
endmodule
