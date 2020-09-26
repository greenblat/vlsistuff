
module reducedCordic(input atan, input sin,input cos, input [31:0] src0,output [31:0] out, input clk,output reg done,input rst_n);

parameter SHIFTY = 20;


wire [5:0] atanShift = 20; 
wire [31:0] flt1241 = 32'h449b2000;

wire atanOverLimit;
fp_gt gtatan (.src0(src0),.src1(flt1241),.out(atanOverLimit));


wire [31:0] src00;

wire [31:0] I24 = (1<<atanShift);
wire isneg = src0[31];
reg isnegST0,isnegST1;
wire [31:0] recipK_sc = 636751;
wire [5:0] shift6 = atan ? atanShift : 24;
fp_float2int fint0(.src0({1'b0,src0[30:0]}),.src1(shift6),.out(src00));

wire [31:0] atanlimit = 1241;

wire [31:0] limitatan20 = atanlimit<<atanShift;


wire [31:0] src02 = (atan && atanOverLimit) ? limitatan20 : src00;


wire [31:0] X0     = atan ? I24   : (sin||cos) ? recipK_sc  :  0;
wire [31:0] Y0     = atan ? src02  : (sin||cos) ? 0          :  0;
wire [31:0] Angle0 = atan ? 0     : (sin||cos) ? src02       :  0;
wire [4:0] work0 = {atan,sin,cos,2'b00};
wire start = work0!=0;
wire [31:0] angle1,x1,y1;
oneStep stepx0 (.Angle(Angle0),.X0(X0),.Y0(Y0),.step(5'd0),.X1(x1),.Y1(y1),.Angle1(angle1),.work(work0),.target(src02));
wire [31:0] angle2,x2,y2;
oneStep stepx1 (.Angle(angle1),.X0(x1),.Y0(y1),.step(5'd1),.X1(x2),.Y1(y2),.Angle1(angle2),.work(work0),.target(src02));
wire [31:0] angle3,x3,y3;
oneStep stepx2 (.Angle(angle2),.X0(x2),.Y0(y2),.step(5'd2),.X1(x3),.Y1(y3),.Angle1(angle3),.work(work0),.target(src02));
wire [31:0] angle4,x4,y4;
oneStep stepx3 (.Angle(angle3),.X0(x3),.Y0(y3),.step(5'd3),.X1(x4),.Y1(y4),.Angle1(angle4),.work(work0),.target(src02));
wire [31:0] angle5,x5,y5;
oneStep stepx4 (.Angle(angle4),.X0(x4),.Y0(y4),.step(5'd4),.X1(x5),.Y1(y5),.Angle1(angle5),.work(work0),.target(src02));
wire [31:0] angle6,x6,y6;
oneStep stepx5 (.Angle(angle5),.X0(x5),.Y0(y5),.step(5'd5),.X1(x6),.Y1(y6),.Angle1(angle6),.work(work0),.target(src02));
wire [31:0] angle7,x7,y7;
oneStep stepx6 (.Angle(angle6),.X0(x6),.Y0(y6),.step(5'd6),.X1(x7),.Y1(y7),.Angle1(angle7),.work(work0),.target(src02));
wire [31:0] angle8,x8,y8;
oneStep stepx7 (.Angle(angle7),.X0(x7),.Y0(y7),.step(5'd7),.X1(x8),.Y1(y8),.Angle1(angle8),.work(work0),.target(src02));

reg [31:0] angleST0,xST0,yST0;
reg [31:0] target1;
reg vldST0;
reg [4:0] workST0,workST1;
always @(posedge clk or negedge rst_n) if (!rst_n) angleST0<=0; else if (start)  angleST0 <= angle8;
always @(posedge clk or negedge rst_n) if (!rst_n) xST0<=0; else if (start)  xST0 <= x8;
always @(posedge clk or negedge rst_n) if (!rst_n) yST0<=0; else if (start)  yST0 <= y8;
always @(posedge clk or negedge rst_n) if (!rst_n) vldST0<=0; else vldST0 <= start;
always @(posedge clk or negedge rst_n) if (!rst_n) isnegST0<=0; else if (start) isnegST0 <= isneg;
always @(posedge clk or negedge rst_n) if (!rst_n) workST0<=0; else if (start) workST0 <= work0;
always @(posedge clk or negedge rst_n) if (!rst_n) target1<=0; else if (start) target1 <= src02;

wire [31:0] angle9,x9,y9;
oneStep stepx8 (.Angle(angleST0),.X0(xST0),.Y0(yST0),.step(5'd8),.X1(x9),.Y1(y9),.Angle1(angle9),.work(workST0),.target(target1));
wire [31:0] angle10,x10,y10;
oneStep stepx9 (.Angle(angle9),.X0(x9),.Y0(y9),.step(5'd9),.X1(x10),.Y1(y10),.Angle1(angle10),.work(workST0),.target(target1));
wire [31:0] angle11,x11,y11;
oneStep stepx10 (.Angle(angle10),.X0(x10),.Y0(y10),.step(5'd10),.X1(x11),.Y1(y11),.Angle1(angle11),.work(workST0),.target(target1));
wire [31:0] angle12,x12,y12;
oneStep stepx11 (.Angle(angle11),.X0(x11),.Y0(y11),.step(5'd11),.X1(x12),.Y1(y12),.Angle1(angle12),.work(workST0),.target(target1));
wire [31:0] angle13,x13,y13;
oneStep stepx12 (.Angle(angle12),.X0(x12),.Y0(y12),.step(5'd12),.X1(x13),.Y1(y13),.Angle1(angle13),.work(workST0),.target(target1));
wire [31:0] angle14,x14,y14;
oneStep stepx13 (.Angle(angle13),.X0(x13),.Y0(y13),.step(5'd13),.X1(x14),.Y1(y14),.Angle1(angle14),.work(workST0),.target(target1));
wire [31:0] angle15,x15,y15;
oneStep stepx14 (.Angle(angle14),.X0(x14),.Y0(y14),.step(5'd14),.X1(x15),.Y1(y15),.Angle1(angle15),.work(workST0),.target(target1));
wire [31:0] angle16,x16,y16;
oneStep stepx15 (.Angle(angle15),.X0(x15),.Y0(y15),.step(5'd15),.X1(x16),.Y1(y16),.Angle1(angle16),.work(workST0),.target(target1));

reg [31:0] angleST1,xST1,yST1;
reg [31:0] target2;
reg vldST1;
always @(posedge clk or negedge rst_n) if (!rst_n) angleST1<=0; else if (vldST0)  angleST1 <= angle16;
always @(posedge clk or negedge rst_n) if (!rst_n) xST1<=0; else if (vldST0)  xST1 <= x16;
always @(posedge clk or negedge rst_n) if (!rst_n) yST1<=0; else if (vldST0)  yST1 <= y16;
always @(posedge clk or negedge rst_n) if (!rst_n) vldST1<=0; else vldST1 <= vldST0;
always @(posedge clk or negedge rst_n) if (!rst_n) isnegST1<=0; else if (vldST0) isnegST1 <= isnegST0;
always @(posedge clk or negedge rst_n) if (!rst_n) workST1<=0; else if (vldST0) workST1 <= workST0;
always @(posedge clk or negedge rst_n) if (!rst_n) target2<=0; else if (vldST0) target2 <= target1;

wire [31:0] angle17,x17,y17;
oneStep stepx16 (.Angle(angleST1),.X0(xST1),.Y0(yST1),.step(5'd16),.X1(x17),.Y1(y17),.Angle1(angle17),.work(workST1),.target(target2));
wire [31:0] angle18,x18,y18;
oneStep stepx17 (.Angle(angle17),.X0(x17),.Y0(y17),.step(5'd17),.X1(x18),.Y1(y18),.Angle1(angle18),.work(workST1),.target(target2));
wire [31:0] angle19,x19,y19;
oneStep stepx18 (.Angle(angle18),.X0(x18),.Y0(y18),.step(5'd18),.X1(x19),.Y1(y19),.Angle1(angle19),.work(workST1),.target(target2));
wire [31:0] angle20,x20,y20;
oneStep stepx19 (.Angle(angle19),.X0(x19),.Y0(y19),.step(5'd19),.X1(x20),.Y1(y20),.Angle1(angle20),.work(workST1),.target(target2));
wire [31:0] angle21,x21,y21;
oneStep stepx20 (.Angle(angle20),.X0(x20),.Y0(y20),.step(5'd20),.X1(x21),.Y1(y21),.Angle1(angle21),.work(workST1),.target(target2));
wire [31:0] angle22,x22,y22;
oneStep stepx21 (.Angle(angle21),.X0(x21),.Y0(y21),.step(5'd21),.X1(x22),.Y1(y22),.Angle1(angle22),.work(workST1),.target(target2));
wire [31:0] angle23,x23,y23;
oneStep stepx22 (.Angle(angle22),.X0(x22),.Y0(y22),.step(5'd22),.X1(x23),.Y1(y23),.Angle1(angle23),.work(workST1),.target(target2));
wire [31:0] angle24,x24,y24;
oneStep stepx23 (.Angle(angle23),.X0(x23),.Y0(y23),.step(5'd23),.X1(x24),.Y1(y24),.Angle1(angle24),.work(workST1),.target(target2));

reg [4:0] work24;
reg [31:0] outhold,xfinal,yfinal;
reg isneg24;
always @(posedge clk or negedge rst_n) if (!rst_n) outhold<=0; else if (vldST1)  outhold <= angle24;
always @(posedge clk or negedge rst_n) if (!rst_n) done<=0; else done<= vldST1;
always @(posedge clk or negedge rst_n) if (!rst_n) isneg24<=0; else if (vldST1) isneg24<= isnegST1;
always @(posedge clk or negedge rst_n) if (!rst_n) work24<=0; else if (vldST1) work24 <= workST1;
always @(posedge clk or negedge rst_n) if (!rst_n) xfinal<=0; else if (vldST1) xfinal <= x24;
always @(posedge clk or negedge rst_n) if (!rst_n) yfinal<=0; else if (vldST1) yfinal <= y24;
wire [31:0] outhold2;
wire atan24,sin24,cos24,nc24,nc25;  assign {atan24,sin24,cos24,nc24,nc25} = work24;
wire [31:0] forout = (atan24) ? outhold : sin24 ? yfinal : cos24 ? xfinal : 0;
wire [5:0] backShift = (atan24) ? 64-24 : 64-SHIFTY;
fp_int2float intf0(.src0(forout),.src1(backShift),.out(outhold2),.is_signed(1'b1));
wire [31:0] outhold3;
fp_int2float_was intf0_was(.src0(forout),.src1(backShift),.out(outhold3));
assign out = {(isneg24 && !cos24),outhold2[30:0]};
endmodule

module oneStep(
    input [31:0] Angle,input [31:0] X0, input [31:0] Y0
    ,input [4:0] step,
    output [31:0] X1,output [31:0] Y1, output [31:0] Angle1
    ,input [4:0] work
    ,input [31:0] target
);
wire atan,sin,cos,nc0,nc1;
assign {atan,sin,cos,nc1,nc0} = work;
wire Dir = atan ? Y0[31] : (sin||cos) ?  Angle[31] : 0 ;
// Dir==0 increas angle, Dir==1 decrease angle :: DIR==1 means Y0>0
wire [31:0] Mask0 = (1<<(32-step))-1;
wire [31:0] Mask1 = ~Mask0;
wire [31:0] YY = {32{Y0[31]}} & Mask1;
wire [31:0] XX = {32{X0[31]}} & Mask1;
wire [31:0] DY = (Y0>>step)|YY;
wire [31:0] DX = (X0>>step)|XX;
assign X1 = (atan && (Y0==0)) ? X0 : (X0 - (Dir ?  DY : -DY)); 
assign Y1 = (atan && (Y0==0)) ? Y0 : (Y0  + (Dir ? DX : -DX));
wire [31:0] Addit,Tmp;
fixangles angles0(.step(step),.angle(Addit));
assign Tmp = Angle + (Dir ? Addit : -Addit);
assign Angle1 = ((atan)&&(Y0==0)) ? Angle : Tmp;
endmodule
module fixangles(input [4:0] step,output reg [31:0] angle);
always @(step) begin
    case (step)
         0 : angle = 32'h00c90fda;
         1 : angle = 32'h0076b19c;
         2 : angle = 32'h003eb6eb;
         3 : angle = 32'h001fd5ba;
         4 : angle = 32'h000ffaad;
         5 : angle = 32'h0007ff55;
         6 : angle = 32'h0003ffea;
         7 : angle = 32'h0001fffd;
         8 : angle = 32'h0000ffff;
         9 : angle = 32'h00007fff;
        10 : angle = 32'h00003fff;
        11 : angle = 32'h00001fff;
        12 : angle = 32'h00000fff;
        13 : angle = 32'h000007ff;
        14 : angle = 32'h000003ff;
        15 : angle = 32'h000001ff;
        16 : angle = 32'h000000ff;
        17 : angle = 32'h0000007f;
        18 : angle = 32'h0000003f;
        19 : angle = 32'h0000001f;
        20 : angle = 32'h0000000f;
        21 : angle = 32'h00000007;
        22 : angle = 32'h00000003;
        23 : angle = 32'h00000001;
        default: angle = 0;
    endcase
end
endmodule

