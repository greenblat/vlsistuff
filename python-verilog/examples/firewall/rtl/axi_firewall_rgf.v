module axi_firewall_rgf (input clk,input rst_n,input pwrite, input psel, input penable, output pslverr, input [1:0] psize, input [31:0] pwdata, output [31:0] prdata, input [6:0] paddr ,output reg [6:0] waddr,output reg [31:0] last_wdata
   ,output reg         enable
   ,input     [19:0] rd_caught_data
   ,output rd_caught_data_pulse
   ,input     [19:0] wr_caught_data
   ,output wr_caught_data_pulse
   ,output reg [511:0] addresses
);
assign pslverr = 0;
wire [6:0] mpaddr = paddr[6:0] & 7'h7c;
wire [31:0] prdata_wire = 
    (mpaddr[6:0]=='h0) ? {31'b0,enable} :
    (mpaddr[6:0]=='h4) ? {12'b0,rd_caught_data} :
    (mpaddr[6:0]=='h8) ? {12'b0,wr_caught_data} :
    (mpaddr[6:0]=='hc) ? addresses[31:0] :
    (mpaddr[6:0]=='h10) ? addresses[63:32] :
    (mpaddr[6:0]=='h14) ? addresses[95:64] :
    (mpaddr[6:0]=='h18) ? addresses[127:96] :
    (mpaddr[6:0]=='h1c) ? addresses[159:128] :
    (mpaddr[6:0]=='h20) ? addresses[191:160] :
    (mpaddr[6:0]=='h24) ? addresses[223:192] :
    (mpaddr[6:0]=='h28) ? addresses[255:224] :
    (mpaddr[6:0]=='h2c) ? addresses[287:256] :
    (mpaddr[6:0]=='h30) ? addresses[319:288] :
    (mpaddr[6:0]=='h34) ? addresses[351:320] :
    (mpaddr[6:0]=='h38) ? addresses[383:352] :
    (mpaddr[6:0]=='h3c) ? addresses[415:384] :
    (mpaddr[6:0]=='h40) ? addresses[447:416] :
    (mpaddr[6:0]=='h44) ? addresses[479:448] :
    (mpaddr[6:0]=='h48) ? addresses[511:480] :
    32'b0;
reg [31:0] prdata_reg;
always @(posedge clk) prdata_reg <=  prdata_wire;
assign prdata =  
   prdata_reg;
            
reg apb_write;
reg [1:0] wsize;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        apb_write <= 1'b0;
        waddr <= 0;
        wsize <= 0;
    end else begin
        apb_write <= psel && pwrite;
        waddr <= mpaddr;
        wsize <= psize;
    end
end
wire [31:0] mask = (wsize==1) ? 32'hff : (wsize==2) ? 32'hffff :  32'hffffffff;
wire [31:0] wdata = (wsize==1) ? {4{pwdata[7:0]}} : (wsize==2) ? {2{pwdata[15:0]}} :  pwdata;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        enable <= 1'h0;
        addresses <= 512'h0;
    end else if (apb_write && penable)  begin
        if (waddr[6:0]=='h0) enable <= (enable & ~mask[0]) | (wdata[0] &mask[0]);
        if (waddr[6:0]=='hc) addresses[31:0] <= (addresses[31:0] & ~mask[31:0]) | (wdata &mask);
        if (waddr[6:0]=='h10) addresses[63:32] <= (addresses[63:32] & ~mask[31:0]) | (wdata &mask);
        if (waddr[6:0]=='h14) addresses[95:64] <= (addresses[95:64] & ~mask[31:0]) | (wdata &mask);
        if (waddr[6:0]=='h18) addresses[127:96] <= (addresses[127:96] & ~mask[31:0]) | (wdata &mask);
        if (waddr[6:0]=='h1c) addresses[159:128] <= (addresses[159:128] & ~mask[31:0]) | (wdata &mask);
        if (waddr[6:0]=='h20) addresses[191:160] <= (addresses[191:160] & ~mask[31:0]) | (wdata &mask);
        if (waddr[6:0]=='h24) addresses[223:192] <= (addresses[223:192] & ~mask[31:0]) | (wdata &mask);
        if (waddr[6:0]=='h28) addresses[255:224] <= (addresses[255:224] & ~mask[31:0]) | (wdata &mask);
        if (waddr[6:0]=='h2c) addresses[287:256] <= (addresses[287:256] & ~mask[31:0]) | (wdata &mask);
        if (waddr[6:0]=='h30) addresses[319:288] <= (addresses[319:288] & ~mask[31:0]) | (wdata &mask);
        if (waddr[6:0]=='h34) addresses[351:320] <= (addresses[351:320] & ~mask[31:0]) | (wdata &mask);
        if (waddr[6:0]=='h38) addresses[383:352] <= (addresses[383:352] & ~mask[31:0]) | (wdata &mask);
        if (waddr[6:0]=='h3c) addresses[415:384] <= (addresses[415:384] & ~mask[31:0]) | (wdata &mask);
        if (waddr[6:0]=='h40) addresses[447:416] <= (addresses[447:416] & ~mask[31:0]) | (wdata &mask);
        if (waddr[6:0]=='h44) addresses[479:448] <= (addresses[479:448] & ~mask[31:0]) | (wdata &mask);
        if (waddr[6:0]=='h48) addresses[511:480] <= (addresses[511:480] & ~mask[31:0]) | (wdata &mask);
    end 
end 
always @(posedge clk) if (apb_write && penable) last_wdata <= pwdata; 
reg rd_caught_data_rd_pulse_reg; always @(posedge clk)  rd_caught_data_rd_pulse_reg <= !pwrite && psel &&  (mpaddr[6:0]=='h4);
assign rd_caught_data_pulse =  penable && rd_caught_data_rd_pulse_reg ;
reg wr_caught_data_rd_pulse_reg; always @(posedge clk)  wr_caught_data_rd_pulse_reg <= !pwrite && psel &&  (mpaddr[6:0]=='h8);
assign wr_caught_data_pulse =  penable && wr_caught_data_rd_pulse_reg ;
endmodule
