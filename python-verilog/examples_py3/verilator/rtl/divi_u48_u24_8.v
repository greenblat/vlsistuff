
module divi_u48_u24_8 ( input clk,input rst_n,input en, input vldin,output reg vldout, input [47:0] src0, input [23:0] src1, output reg  [47:0] out,output reg [22:0] remsrc0der);
// stages=8 places=[41, 34, 27, 20, 13, 6]
reg vld1;
always @(posedge clk) if (en) vld1 <= vldin;
reg [71:0] src01;
always @(posedge clk) if (en) src01 <= {24'b0,src0};
reg [24:0] src11;
always @(posedge clk) if (en) src11 <= {1'b0,src1};


wire bit1 = (src11 <= src01[71:47]);
wire [24:0] xhigh1 = src01[71:47]-src11;
wire [23:0] high1 = bit1 ? xhigh1[23:0] : src01[70:47] ;
wire [70:0]  src02 = {high1,src01[46:0]};
wire res2 = bit1;
wire [24:0] src12 = src11;
wire vld2 = vld1;


wire bit2 = (src12 <= src02[70:46]);
wire [24:0] xhigh2 = src02[70:46]-src12;
wire [23:0] high2 = bit2 ? xhigh2[23:0] : src02[69:46] ;
wire [69:0]  src03 = {high2,src02[45:0]};
wire [1:0]  res3 = {res2,bit2};
wire [24:0] src13 = src12;
wire vld3 = vld2;


wire bit3 = (src13 <= src03[69:45]);
wire [24:0] xhigh3 = src03[69:45]-src13;
wire [23:0] high3 = bit3 ? xhigh3[23:0] : src03[68:45] ;
wire [68:0]  src04 = {high3,src03[44:0]};
wire [2:0]  res4 = {res3,bit3};
wire [24:0] src14 = src13;
wire vld4 = vld3;


wire bit4 = (src14 <= src04[68:44]);
wire [24:0] xhigh4 = src04[68:44]-src14;
wire [23:0] high4 = bit4 ? xhigh4[23:0] : src04[67:44] ;
wire [67:0]  src05 = {high4,src04[43:0]};
wire [3:0]  res5 = {res4,bit4};
wire [24:0] src15 = src14;
wire vld5 = vld4;


wire bit5 = (src15 <= src05[67:43]);
wire [24:0] xhigh5 = src05[67:43]-src15;
wire [23:0] high5 = bit5 ? xhigh5[23:0] : src05[66:43] ;
wire [66:0]  src06 = {high5,src05[42:0]};
wire [4:0]  res6 = {res5,bit5};
wire [24:0] src16 = src15;
wire vld6 = vld5;


wire bit6 = (src16 <= src06[66:42]);
wire [24:0] xhigh6 = src06[66:42]-src16;
wire [23:0] high6 = bit6 ? xhigh6[23:0] : src06[65:42] ;
wire [65:0]  pre_src07 = {high6,src06[41:0]};
wire [5:0]  pre_res7 = {res6,bit6};

reg [65:0] src07;
always @(posedge clk) if (en) src07 <= pre_src07;
reg [24:0] src17;
always @(posedge clk) if (en) src17 <= src16;
reg [5:0] res7;
always @(posedge clk) if (en) res7 <= pre_res7;
reg vld7;
always @(posedge clk) if (en) vld7 <= vld6;


wire bit7 = (src17 <= src07[65:41]);
wire [24:0] xhigh7 = src07[65:41]-src17;
wire [23:0] high7 = bit7 ? xhigh7[23:0] : src07[64:41] ;
wire [64:0]  src08 = {high7,src07[40:0]};
wire [6:0]  res8 = {res7,bit7};
wire [24:0] src18 = src17;
wire vld8 = vld7;


wire bit8 = (src18 <= src08[64:40]);
wire [24:0] xhigh8 = src08[64:40]-src18;
wire [23:0] high8 = bit8 ? xhigh8[23:0] : src08[63:40] ;
wire [63:0]  src09 = {high8,src08[39:0]};
wire [7:0]  res9 = {res8,bit8};
wire [24:0] src19 = src18;
wire vld9 = vld8;


wire bit9 = (src19 <= src09[63:39]);
wire [24:0] xhigh9 = src09[63:39]-src19;
wire [23:0] high9 = bit9 ? xhigh9[23:0] : src09[62:39] ;
wire [62:0]  src010 = {high9,src09[38:0]};
wire [8:0]  res10 = {res9,bit9};
wire [24:0] src110 = src19;
wire vld10 = vld9;


wire bit10 = (src110 <= src010[62:38]);
wire [24:0] xhigh10 = src010[62:38]-src110;
wire [23:0] high10 = bit10 ? xhigh10[23:0] : src010[61:38] ;
wire [61:0]  src011 = {high10,src010[37:0]};
wire [9:0]  res11 = {res10,bit10};
wire [24:0] src111 = src110;
wire vld11 = vld10;


wire bit11 = (src111 <= src011[61:37]);
wire [24:0] xhigh11 = src011[61:37]-src111;
wire [23:0] high11 = bit11 ? xhigh11[23:0] : src011[60:37] ;
wire [60:0]  src012 = {high11,src011[36:0]};
wire [10:0]  res12 = {res11,bit11};
wire [24:0] src112 = src111;
wire vld12 = vld11;


wire bit12 = (src112 <= src012[60:36]);
wire [24:0] xhigh12 = src012[60:36]-src112;
wire [23:0] high12 = bit12 ? xhigh12[23:0] : src012[59:36] ;
wire [59:0]  src013 = {high12,src012[35:0]};
wire [11:0]  res13 = {res12,bit12};
wire [24:0] src113 = src112;
wire vld13 = vld12;


wire bit13 = (src113 <= src013[59:35]);
wire [24:0] xhigh13 = src013[59:35]-src113;
wire [23:0] high13 = bit13 ? xhigh13[23:0] : src013[58:35] ;
wire [58:0]  pre_src014 = {high13,src013[34:0]};
wire [12:0]  pre_res14 = {res13,bit13};

reg [58:0] src014;
always @(posedge clk) if (en) src014 <= pre_src014;
reg [24:0] src114;
always @(posedge clk) if (en) src114 <= src113;
reg [12:0] res14;
always @(posedge clk) if (en) res14 <= pre_res14;
reg vld14;
always @(posedge clk) if (en) vld14 <= vld13;


wire bit14 = (src114 <= src014[58:34]);
wire [24:0] xhigh14 = src014[58:34]-src114;
wire [23:0] high14 = bit14 ? xhigh14[23:0] : src014[57:34] ;
wire [57:0]  src015 = {high14,src014[33:0]};
wire [13:0]  res15 = {res14,bit14};
wire [24:0] src115 = src114;
wire vld15 = vld14;


wire bit15 = (src115 <= src015[57:33]);
wire [24:0] xhigh15 = src015[57:33]-src115;
wire [23:0] high15 = bit15 ? xhigh15[23:0] : src015[56:33] ;
wire [56:0]  src016 = {high15,src015[32:0]};
wire [14:0]  res16 = {res15,bit15};
wire [24:0] src116 = src115;
wire vld16 = vld15;


wire bit16 = (src116 <= src016[56:32]);
wire [24:0] xhigh16 = src016[56:32]-src116;
wire [23:0] high16 = bit16 ? xhigh16[23:0] : src016[55:32] ;
wire [55:0]  src017 = {high16,src016[31:0]};
wire [15:0]  res17 = {res16,bit16};
wire [24:0] src117 = src116;
wire vld17 = vld16;


wire bit17 = (src117 <= src017[55:31]);
wire [24:0] xhigh17 = src017[55:31]-src117;
wire [23:0] high17 = bit17 ? xhigh17[23:0] : src017[54:31] ;
wire [54:0]  src018 = {high17,src017[30:0]};
wire [16:0]  res18 = {res17,bit17};
wire [24:0] src118 = src117;
wire vld18 = vld17;


wire bit18 = (src118 <= src018[54:30]);
wire [24:0] xhigh18 = src018[54:30]-src118;
wire [23:0] high18 = bit18 ? xhigh18[23:0] : src018[53:30] ;
wire [53:0]  src019 = {high18,src018[29:0]};
wire [17:0]  res19 = {res18,bit18};
wire [24:0] src119 = src118;
wire vld19 = vld18;


wire bit19 = (src119 <= src019[53:29]);
wire [24:0] xhigh19 = src019[53:29]-src119;
wire [23:0] high19 = bit19 ? xhigh19[23:0] : src019[52:29] ;
wire [52:0]  src020 = {high19,src019[28:0]};
wire [18:0]  res20 = {res19,bit19};
wire [24:0] src120 = src119;
wire vld20 = vld19;


wire bit20 = (src120 <= src020[52:28]);
wire [24:0] xhigh20 = src020[52:28]-src120;
wire [23:0] high20 = bit20 ? xhigh20[23:0] : src020[51:28] ;
wire [51:0]  pre_src021 = {high20,src020[27:0]};
wire [19:0]  pre_res21 = {res20,bit20};

reg [51:0] src021;
always @(posedge clk) if (en) src021 <= pre_src021;
reg [24:0] src121;
always @(posedge clk) if (en) src121 <= src120;
reg [19:0] res21;
always @(posedge clk) if (en) res21 <= pre_res21;
reg vld21;
always @(posedge clk) if (en) vld21 <= vld20;


wire bit21 = (src121 <= src021[51:27]);
wire [24:0] xhigh21 = src021[51:27]-src121;
wire [23:0] high21 = bit21 ? xhigh21[23:0] : src021[50:27] ;
wire [50:0]  src022 = {high21,src021[26:0]};
wire [20:0]  res22 = {res21,bit21};
wire [24:0] src122 = src121;
wire vld22 = vld21;


wire bit22 = (src122 <= src022[50:26]);
wire [24:0] xhigh22 = src022[50:26]-src122;
wire [23:0] high22 = bit22 ? xhigh22[23:0] : src022[49:26] ;
wire [49:0]  src023 = {high22,src022[25:0]};
wire [21:0]  res23 = {res22,bit22};
wire [24:0] src123 = src122;
wire vld23 = vld22;


wire bit23 = (src123 <= src023[49:25]);
wire [24:0] xhigh23 = src023[49:25]-src123;
wire [23:0] high23 = bit23 ? xhigh23[23:0] : src023[48:25] ;
wire [48:0]  src024 = {high23,src023[24:0]};
wire [22:0]  res24 = {res23,bit23};
wire [24:0] src124 = src123;
wire vld24 = vld23;


wire bit24 = (src124 <= src024[48:24]);
wire [24:0] xhigh24 = src024[48:24]-src124;
wire [23:0] high24 = bit24 ? xhigh24[23:0] : src024[47:24] ;
wire [47:0]  src025 = {high24,src024[23:0]};
wire [23:0]  res25 = {res24,bit24};
wire [24:0] src125 = src124;
wire vld25 = vld24;


wire bit25 = (src125 <= src025[47:23]);
wire [24:0] xhigh25 = src025[47:23]-src125;
wire [23:0] high25 = bit25 ? xhigh25[23:0] : src025[46:23] ;
wire [46:0]  src026 = {high25,src025[22:0]};
wire [24:0]  res26 = {res25,bit25};
wire [24:0] src126 = src125;
wire vld26 = vld25;


wire bit26 = (src126 <= src026[46:22]);
wire [24:0] xhigh26 = src026[46:22]-src126;
wire [23:0] high26 = bit26 ? xhigh26[23:0] : src026[45:22] ;
wire [45:0]  src027 = {high26,src026[21:0]};
wire [25:0]  res27 = {res26,bit26};
wire [24:0] src127 = src126;
wire vld27 = vld26;


wire bit27 = (src127 <= src027[45:21]);
wire [24:0] xhigh27 = src027[45:21]-src127;
wire [23:0] high27 = bit27 ? xhigh27[23:0] : src027[44:21] ;
wire [44:0]  pre_src028 = {high27,src027[20:0]};
wire [26:0]  pre_res28 = {res27,bit27};

reg [44:0] src028;
always @(posedge clk) if (en) src028 <= pre_src028;
reg [24:0] src128;
always @(posedge clk) if (en) src128 <= src127;
reg [26:0] res28;
always @(posedge clk) if (en) res28 <= pre_res28;
reg vld28;
always @(posedge clk) if (en) vld28 <= vld27;


wire bit28 = (src128 <= src028[44:20]);
wire [24:0] xhigh28 = src028[44:20]-src128;
wire [23:0] high28 = bit28 ? xhigh28[23:0] : src028[43:20] ;
wire [43:0]  src029 = {high28,src028[19:0]};
wire [27:0]  res29 = {res28,bit28};
wire [24:0] src129 = src128;
wire vld29 = vld28;


wire bit29 = (src129 <= src029[43:19]);
wire [24:0] xhigh29 = src029[43:19]-src129;
wire [23:0] high29 = bit29 ? xhigh29[23:0] : src029[42:19] ;
wire [42:0]  src030 = {high29,src029[18:0]};
wire [28:0]  res30 = {res29,bit29};
wire [24:0] src130 = src129;
wire vld30 = vld29;


wire bit30 = (src130 <= src030[42:18]);
wire [24:0] xhigh30 = src030[42:18]-src130;
wire [23:0] high30 = bit30 ? xhigh30[23:0] : src030[41:18] ;
wire [41:0]  src031 = {high30,src030[17:0]};
wire [29:0]  res31 = {res30,bit30};
wire [24:0] src131 = src130;
wire vld31 = vld30;


wire bit31 = (src131 <= src031[41:17]);
wire [24:0] xhigh31 = src031[41:17]-src131;
wire [23:0] high31 = bit31 ? xhigh31[23:0] : src031[40:17] ;
wire [40:0]  src032 = {high31,src031[16:0]};
wire [30:0]  res32 = {res31,bit31};
wire [24:0] src132 = src131;
wire vld32 = vld31;


wire bit32 = (src132 <= src032[40:16]);
wire [24:0] xhigh32 = src032[40:16]-src132;
wire [23:0] high32 = bit32 ? xhigh32[23:0] : src032[39:16] ;
wire [39:0]  src033 = {high32,src032[15:0]};
wire [31:0]  res33 = {res32,bit32};
wire [24:0] src133 = src132;
wire vld33 = vld32;


wire bit33 = (src133 <= src033[39:15]);
wire [24:0] xhigh33 = src033[39:15]-src133;
wire [23:0] high33 = bit33 ? xhigh33[23:0] : src033[38:15] ;
wire [38:0]  src034 = {high33,src033[14:0]};
wire [32:0]  res34 = {res33,bit33};
wire [24:0] src134 = src133;
wire vld34 = vld33;


wire bit34 = (src134 <= src034[38:14]);
wire [24:0] xhigh34 = src034[38:14]-src134;
wire [23:0] high34 = bit34 ? xhigh34[23:0] : src034[37:14] ;
wire [37:0]  pre_src035 = {high34,src034[13:0]};
wire [33:0]  pre_res35 = {res34,bit34};

reg [37:0] src035;
always @(posedge clk) if (en) src035 <= pre_src035;
reg [24:0] src135;
always @(posedge clk) if (en) src135 <= src134;
reg [33:0] res35;
always @(posedge clk) if (en) res35 <= pre_res35;
reg vld35;
always @(posedge clk) if (en) vld35 <= vld34;


wire bit35 = (src135 <= src035[37:13]);
wire [24:0] xhigh35 = src035[37:13]-src135;
wire [23:0] high35 = bit35 ? xhigh35[23:0] : src035[36:13] ;
wire [36:0]  src036 = {high35,src035[12:0]};
wire [34:0]  res36 = {res35,bit35};
wire [24:0] src136 = src135;
wire vld36 = vld35;


wire bit36 = (src136 <= src036[36:12]);
wire [24:0] xhigh36 = src036[36:12]-src136;
wire [23:0] high36 = bit36 ? xhigh36[23:0] : src036[35:12] ;
wire [35:0]  src037 = {high36,src036[11:0]};
wire [35:0]  res37 = {res36,bit36};
wire [24:0] src137 = src136;
wire vld37 = vld36;


wire bit37 = (src137 <= src037[35:11]);
wire [24:0] xhigh37 = src037[35:11]-src137;
wire [23:0] high37 = bit37 ? xhigh37[23:0] : src037[34:11] ;
wire [34:0]  src038 = {high37,src037[10:0]};
wire [36:0]  res38 = {res37,bit37};
wire [24:0] src138 = src137;
wire vld38 = vld37;


wire bit38 = (src138 <= src038[34:10]);
wire [24:0] xhigh38 = src038[34:10]-src138;
wire [23:0] high38 = bit38 ? xhigh38[23:0] : src038[33:10] ;
wire [33:0]  src039 = {high38,src038[9:0]};
wire [37:0]  res39 = {res38,bit38};
wire [24:0] src139 = src138;
wire vld39 = vld38;


wire bit39 = (src139 <= src039[33:9]);
wire [24:0] xhigh39 = src039[33:9]-src139;
wire [23:0] high39 = bit39 ? xhigh39[23:0] : src039[32:9] ;
wire [32:0]  src040 = {high39,src039[8:0]};
wire [38:0]  res40 = {res39,bit39};
wire [24:0] src140 = src139;
wire vld40 = vld39;


wire bit40 = (src140 <= src040[32:8]);
wire [24:0] xhigh40 = src040[32:8]-src140;
wire [23:0] high40 = bit40 ? xhigh40[23:0] : src040[31:8] ;
wire [31:0]  src041 = {high40,src040[7:0]};
wire [39:0]  res41 = {res40,bit40};
wire [24:0] src141 = src140;
wire vld41 = vld40;


wire bit41 = (src141 <= src041[31:7]);
wire [24:0] xhigh41 = src041[31:7]-src141;
wire [23:0] high41 = bit41 ? xhigh41[23:0] : src041[30:7] ;
wire [30:0]  pre_src042 = {high41,src041[6:0]};
wire [40:0]  pre_res42 = {res41,bit41};

reg [30:0] src042;
always @(posedge clk) if (en) src042 <= pre_src042;
reg [24:0] src142;
always @(posedge clk) if (en) src142 <= src141;
reg [40:0] res42;
always @(posedge clk) if (en) res42 <= pre_res42;
reg vld42;
always @(posedge clk) if (en) vld42 <= vld41;


wire bit42 = (src142 <= src042[30:6]);
wire [24:0] xhigh42 = src042[30:6]-src142;
wire [23:0] high42 = bit42 ? xhigh42[23:0] : src042[29:6] ;
wire [29:0]  src043 = {high42,src042[5:0]};
wire [41:0]  res43 = {res42,bit42};
wire [24:0] src143 = src142;
wire vld43 = vld42;


wire bit43 = (src143 <= src043[29:5]);
wire [24:0] xhigh43 = src043[29:5]-src143;
wire [23:0] high43 = bit43 ? xhigh43[23:0] : src043[28:5] ;
wire [28:0]  src044 = {high43,src043[4:0]};
wire [42:0]  res44 = {res43,bit43};
wire [24:0] src144 = src143;
wire vld44 = vld43;


wire bit44 = (src144 <= src044[28:4]);
wire [24:0] xhigh44 = src044[28:4]-src144;
wire [23:0] high44 = bit44 ? xhigh44[23:0] : src044[27:4] ;
wire [27:0]  src045 = {high44,src044[3:0]};
wire [43:0]  res45 = {res44,bit44};
wire [24:0] src145 = src144;
wire vld45 = vld44;


wire bit45 = (src145 <= src045[27:3]);
wire [24:0] xhigh45 = src045[27:3]-src145;
wire [23:0] high45 = bit45 ? xhigh45[23:0] : src045[26:3] ;
wire [26:0]  src046 = {high45,src045[2:0]};
wire [44:0]  res46 = {res45,bit45};
wire [24:0] src146 = src145;
wire vld46 = vld45;


wire bit46 = (src146 <= src046[26:2]);
wire [24:0] xhigh46 = src046[26:2]-src146;
wire [23:0] high46 = bit46 ? xhigh46[23:0] : src046[25:2] ;
wire [25:0]  src047 = {high46,src046[1:0]};
wire [45:0]  res47 = {res46,bit46};
wire [24:0] src147 = src146;
wire vld47 = vld46;


wire bit47 = (src147 <= src047[25:1]);
wire [24:0] xhigh47 = src047[25:1]-src147;
wire [23:0] high47 = bit47 ? xhigh47[23:0] : src047[24:1] ;
wire [24:0]  src048 = {high47,src047[0]};
wire [46:0]  res48 = {res47,bit47};
wire [24:0] src148 = src147;
wire vld48 = vld47;


wire bit48 = (src148 <= src048[24:0]);
wire [24:0] xhigh48 = src048[24:0]-src148;
wire [23:0] high48 = bit48 ? xhigh48[23:0] : src048[23:0] ;
wire [23:0]  src049 = high48;
wire [47:0]  res49 = {res48,bit48};
wire [24:0] src149 = src148;
wire vld49 = vld48;
wire [47:0] res000 = (src149==0) ? 48'b0 : res49 ;
always @(posedge clk) if (en) out <= res000;
always @(posedge clk) if (en) remsrc0der <= src049;
always @(posedge clk) if (en) vldout <= vld49;
endmodule
