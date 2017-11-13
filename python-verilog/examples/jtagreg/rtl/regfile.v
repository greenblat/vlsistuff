module regfile (input clk,input rst_n,input pwrite, input psel, input [1:0] psize, input [31:0] pwdata, output reg [31:0] prdata, input [6:0] paddr
   ,output reg [31:0] enables
   ,output reg [31:0] control_stream1
   ,output reg [31:0] control_stream2
   ,output reg [31:0] input_select
   ,output reg [15:0] config0
   ,output reg [23:0] config1
   ,output reg [ 7:0] config2
   ,output reg [ 9:0] port0
   ,output reg [ 9:0] port1
   ,output  [2:0] num_octaves0
   ,output         lens_invariant0
   ,output  [2:0] num_octaves1
   ,output  [5:0] pattern_scale0
   ,output         lens_invariant1
   ,output  [5:0] pattern_scale1
);
wire [31:0] rdata_wire = 
    (paddr[6:2]==0) ? enables :
    (paddr[6:2]==1) ? control_stream1 :
    (paddr[6:2]==2) ? control_stream2 :
    (paddr[6:2]==3) ? input_select :
    (paddr[6:2]==4) ? {16'b0,config0} :
    (paddr[6:2]==5) ? {8'b0,config1} :
    (paddr[6:2]==6) ? {24'b0,config2} :
    (paddr[6:2]==7) ? {22'b0,port0} :
    (paddr[6:2]==8) ? {22'b0,port1} :
    32'b0;
always @(posedge clk) prdata <= rdata_wire;
assign num_octaves1 = port1[2:0];
assign lens_invariant0 = port0[9];
assign num_octaves0 = port0[2:0];
assign pattern_scale1 = port1[8:3];
assign lens_invariant1 = port1[9];
assign pattern_scale0 = port0[8:3];
wire [31:0] mask = (psize==1) ? 32'hff : (psize==2) ? 32'hffff :  32'hffffffff;
wire [31:0] wdata = (psize==1) ? {4{pwdata[7:0]}} : (psize==2) ? {2{pwdata[15:0]}} :  pwdata;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        enables <= 32'h0;
        control_stream1 <= 32'h0;
        control_stream2 <= 32'h0;
        input_select <= 32'h0;
        config0 <= 16'h234;
        config1 <= 24'hfff;
        config2 <= 8'h55;
        port0 <= 10'h0;
        port1 <= 10'h0;
    end else if (pwrite && psel)  begin
        if (paddr[6:2]==0) enables <= (enables[31:0] & ~mask[31:0]) | (wdata &mask);
        if (paddr[6:2]==1) control_stream1 <= (control_stream1[31:0] & ~mask[31:0]) | (wdata &mask);
        if (paddr[6:2]==2) control_stream2 <= (control_stream2[31:0] & ~mask[31:0]) | (wdata &mask);
        if (paddr[6:2]==3) input_select <= (input_select[31:0] & ~mask[31:0]) | (wdata &mask);
        if (paddr[6:2]==4) config0 <= (config0[15:0] & ~mask[15:0]) | (wdata &mask);
        if (paddr[6:2]==5) config1 <= (config1[23:0] & ~mask[23:0]) | (wdata &mask);
        if (paddr[6:2]==6) config2 <= (config2[7:0] & ~mask[7:0]) | (wdata &mask);
        if (paddr[6:2]==7) port0 <= (port0[9:0] & ~mask[9:0]) | (wdata &mask);
        if (paddr[6:2]==8) port1 <= (port1[9:0] & ~mask[9:0]) | (wdata &mask);
    end 
end 
endmodule
