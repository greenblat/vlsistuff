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
