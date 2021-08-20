


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
        stage0 <= datain ^ CONST;
        vlds[0] <= vldin;
    end
end


wire [31:0] tmp1 = (stage0 ^ key[63:32]) + (stage0[0] ? CONST : 0);
reg [31:0] stage1;    
always @(posedge clk) begin
    stage1 <=  {tmp1[1:0],tmp1[31:2]};
    vlds[1] <= vlds[0];
end 

wire [31:0] tmp2 = (stage1 ^ key[95:64]) + (stage1[0] ? CONST : 0);
reg [31:0] stage2;    
always @(posedge clk) begin
    stage2 <=  {tmp2[2:0],tmp2[31:3]};
    vlds[2] <= vlds[1];
end 

wire [31:0] tmp3 = (stage2 ^ key[127:96]) + (stage2[0] ? CONST : 0);
reg [31:0] stage3;    
always @(posedge clk) begin
    stage3 <=  {tmp3[3:0],tmp3[31:4]};
    vlds[3] <= vlds[2];
end 

wire [31:0] tmp4 = (stage3 ^ key[31:0]) + (stage3[0] ? CONST : 0);
reg [31:0] stage4;    
always @(posedge clk) begin
    stage4 <=  {tmp4[4:0],tmp4[31:5]};
    vlds[4] <= vlds[3];
end 

wire [31:0] tmp5 = (stage4 ^ key[63:32]) + (stage4[0] ? CONST : 0);
reg [31:0] stage5;    
always @(posedge clk) begin
    stage5 <=  {tmp5[5:0],tmp5[31:6]};
    vlds[5] <= vlds[4];
end 

wire [31:0] tmp6 = (stage5 ^ key[95:64]) + (stage5[0] ? CONST : 0);
reg [31:0] stage6;    
always @(posedge clk) begin
    stage6 <=  {tmp6[6:0],tmp6[31:7]};
    vlds[6] <= vlds[5];
end 

wire [31:0] tmp7 = (stage6 ^ key[127:96]) + (stage6[0] ? CONST : 0);
reg [31:0] stage7;    
always @(posedge clk) begin
    stage7 <=  {tmp7[7:0],tmp7[31:8]};
    vlds[7] <= vlds[6];
end 

wire [31:0] tmp8 = (stage7 ^ key[31:0]) + (stage7[0] ? CONST : 0);
reg [31:0] stage8;    
always @(posedge clk) begin
    stage8 <=  {tmp8[8:0],tmp8[31:9]};
    vlds[8] <= vlds[7];
end 

wire [31:0] tmp9 = (stage8 ^ key[63:32]) + (stage8[0] ? CONST : 0);
reg [31:0] stage9;    
always @(posedge clk) begin
    stage9 <=  {tmp9[9:0],tmp9[31:10]};
    vlds[9] <= vlds[8];
end 

wire [31:0] tmp10 = (stage9 ^ key[95:64]) + (stage9[0] ? CONST : 0);
reg [31:0] stage10;    
always @(posedge clk) begin
    stage10 <=  {tmp10[10:0],tmp10[31:11]};
    vlds[10] <= vlds[9];
end 

wire [31:0] tmp11 = (stage10 ^ key[127:96]) + (stage10[0] ? CONST : 0);
reg [31:0] stage11;    
always @(posedge clk) begin
    stage11 <=  {tmp11[11:0],tmp11[31:12]};
    vlds[11] <= vlds[10];
end 

wire [31:0] tmp12 = (stage11 ^ key[31:0]) + (stage11[0] ? CONST : 0);
reg [31:0] stage12;    
always @(posedge clk) begin
    stage12 <=  {tmp12[12:0],tmp12[31:13]};
    vlds[12] <= vlds[11];
end 

assign vldout = vlds[12];
assign encrypted = stage12;

endmodule


