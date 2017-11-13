module regfile (input clk,input rst_n,input pwrite, input psel, input [1:0] psize, input [31:0] pwdata, output reg [31:0] prdata, input [5:0] paddr
   ,output reg [15:0] enables
   ,output reg [10:0] start0
   ,output reg [10:0] start1
   ,output reg [10:0] start2
   ,output reg [10:0] jump0
   ,output reg [10:0] jump1
   ,output reg [10:0] jump2
   ,output reg [15:0] baudrate
   ,output reg [15:0] control
   ,output reg [15:0] gain2
);
wire [31:0] rdata_wire = 
    (paddr[5:0]==0) ? {16'b0,enables} :
    (paddr[5:0]==4) ? {21'b0,start0} :
    (paddr[5:0]==8) ? {21'b0,start1} :
    (paddr[5:0]==12) ? {21'b0,start2} :
    (paddr[5:0]==16) ? {21'b0,jump0} :
    (paddr[5:0]==20) ? {21'b0,jump1} :
    (paddr[5:0]==24) ? {21'b0,jump2} :
    (paddr[5:0]==28) ? {16'b0,baudrate} :
    (paddr[5:0]==32) ? {16'b0,control} :
    (paddr[5:0]==36) ? {16'b0,gain2} :
    32'b0;
always @(posedge clk) prdata <= rdata_wire;
wire [31:0] mask = (psize==1) ? 32'hff : (psize==2) ? 32'hffff :  32'hffffffff;
wire [31:0] wdata = (psize==1) ? {4{pwdata[7:0]}} : (psize==2) ? {2{pwdata[15:0]}} :  pwdata;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        enables <= 16'h0;
        start0 <= 11'h0;
        start1 <= 11'h0;
        start2 <= 11'h0;
        jump0 <= 11'h0;
        jump1 <= 11'h0;
        jump2 <= 11'h0;
        baudrate <= 16'h100;
        control <= 16'h50;
        gain2 <= 16'h0;
    end else if (pwrite && psel)  begin
        if (paddr[5:0]==0) enables <= (enables[15:0] & ~mask[15:0]) | (wdata &mask);
        if (paddr[5:0]==4) start0 <= (start0[10:0] & ~mask[10:0]) | (wdata &mask);
        if (paddr[5:0]==8) start1 <= (start1[10:0] & ~mask[10:0]) | (wdata &mask);
        if (paddr[5:0]==12) start2 <= (start2[10:0] & ~mask[10:0]) | (wdata &mask);
        if (paddr[5:0]==16) jump0 <= (jump0[10:0] & ~mask[10:0]) | (wdata &mask);
        if (paddr[5:0]==20) jump1 <= (jump1[10:0] & ~mask[10:0]) | (wdata &mask);
        if (paddr[5:0]==24) jump2 <= (jump2[10:0] & ~mask[10:0]) | (wdata &mask);
        if (paddr[5:0]==28) baudrate <= (baudrate[15:0] & ~mask[15:0]) | (wdata &mask);
        if (paddr[5:0]==32) control <= (control[15:0] & ~mask[15:0]) | (wdata &mask);
        if (paddr[5:0]==36) gain2 <= (gain2[15:0] & ~mask[15:0]) | (wdata &mask);
    end 
end 
endmodule
