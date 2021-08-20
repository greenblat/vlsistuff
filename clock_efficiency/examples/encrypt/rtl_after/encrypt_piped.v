


module encrypt_piped (input clk, input rst_n
    ,input [31:0] datain
    ,input [127:0] key
    ,input vldin

    ,output vldout
    ,output [31:0] encrypted
);

localparam CONST = 32'h4cfedf05;
reg [12:0] vlds;
reg [31:0] stage0;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        stage0 <= 0;
        vlds[0] <= 0;
    end else begin
        if (vldin) stage0 <= datain ^ CONST;
        vlds[0] <= vldin;
    end
end


wire [31:0] tmpa1 = (stage0 ^ key[63:32]) + (stage0[0] ? CONST : 0);
wire [31:0] tmpb1 = {tmpa1[1:0],tmpa1[31:2]};
reg [31:0] stage1;    
always @(posedge clk) begin
    if (vlds[0]) stage1 <=  tmpb1;
    vlds[1] <= vlds[0];
end 

wire [31:0] tmpa2 = (stage1 ^ key[95:64]) + (stage1[0] ? CONST : 0);
wire [31:0] tmpb2 = {tmpa2[2:0],tmpa2[31:3]};
reg [31:0] stage2;    
always @(posedge clk) begin
    if (vlds[1]) stage2 <=  tmpb2;
    vlds[2] <= vlds[1];
end 

wire [31:0] tmpa3 = (stage2 ^ key[127:96]) + (stage2[0] ? CONST : 0);
wire [31:0] tmpb3 = {tmpa3[3:0],tmpa3[31:4]};
reg [31:0] stage3;    
always @(posedge clk) begin
    if (vlds[2]) stage3 <=  tmpb3;
    vlds[3] <= vlds[2];
end 

wire [31:0] tmpa4 = (stage3 ^ key[31:0]) + (stage3[0] ? CONST : 0);
wire [31:0] tmpb4 = {tmpa4[4:0],tmpa4[31:5]};
reg [31:0] stage4;    
always @(posedge clk) begin
    if (vlds[3]) stage4 <=  tmpb4;
    vlds[4] <= vlds[3];
end 

wire [31:0] tmpa5 = (stage4 ^ key[63:32]) + (stage4[0] ? CONST : 0);
wire [31:0] tmpb5 = {tmpa5[5:0],tmpa5[31:6]};
reg [31:0] stage5;    
always @(posedge clk) begin
    if (vlds[4]) stage5 <=  tmpb5;
    vlds[5] <= vlds[4];
end 

wire [31:0] tmpa6 = (stage5 ^ key[95:64]) + (stage5[0] ? CONST : 0);
wire [31:0] tmpb6 = {tmpa6[6:0],tmpa6[31:7]};
reg [31:0] stage6;    
always @(posedge clk) begin
    if (vlds[5]) stage6 <=  tmpb6;
    vlds[6] <= vlds[5];
end 

wire [31:0] tmpa7 = (stage6 ^ key[127:96]) + (stage6[0] ? CONST : 0);
wire [31:0] tmpb7 = {tmpa7[7:0],tmpa7[31:8]};
reg [31:0] stage7;    
always @(posedge clk) begin
    if (vlds[6]) stage7 <=  tmpb7;
    vlds[7] <= vlds[6];
end 

wire [31:0] tmpa8 = (stage7 ^ key[31:0]) + (stage7[0] ? CONST : 0);
wire [31:0] tmpb8 = {tmpa8[8:0],tmpa8[31:9]};
reg [31:0] stage8;    
always @(posedge clk) begin
    if (vlds[7]) stage8 <=  tmpb8;
    vlds[8] <= vlds[7];
end 

wire [31:0] tmpa9 = (stage8 ^ key[63:32]) + (stage8[0] ? CONST : 0);
wire [31:0] tmpb9 = {tmpa9[9:0],tmpa9[31:10]};
reg [31:0] stage9;    
always @(posedge clk) begin
    if (vlds[8]) stage9 <=  tmpb9;
    vlds[9] <= vlds[8];
end 

wire [31:0] tmpa10 = (stage9 ^ key[95:64]) + (stage9[0] ? CONST : 0);
wire [31:0] tmpb10 = {tmpa10[10:0],tmpa10[31:11]};
reg [31:0] stage10;    
always @(posedge clk) begin
    if (vlds[9]) stage10 <=  tmpb10;
    vlds[10] <= vlds[9];
end 

wire [31:0] tmpa11 = (stage10 ^ key[127:96]) + (stage10[0] ? CONST : 0);
wire [31:0] tmpb11 = {tmpa11[11:0],tmpa11[31:12]};
reg [31:0] stage11;    
always @(posedge clk) begin
    if (vlds[10]) stage11 <=  tmpb11;
    vlds[11] <= vlds[10];
end 

wire [31:0] tmpa12 = (stage11 ^ key[31:0]) + (stage11[0] ? CONST : 0);
wire [31:0] tmpb12 = {tmpa12[12:0],tmpa12[31:13]};
reg [31:0] stage12;    
always @(posedge clk) begin
    if (vlds[11]) stage12 <=  tmpb12;
    vlds[12] <= vlds[11];
end 

assign vldout = vlds[12];
assign encrypted = stage12;

endmodule


