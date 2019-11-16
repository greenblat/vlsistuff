module debugaxirgf (input clk,input rst_n,input rwrite, input rsel, input [1:0] rsize, input [31:0] wrdata, output [31:0] rdata, input [6:0] addr
   ,output reg [15:0] uart_baudrate
   ,output reg [ 7:0] uart_control
   ,input     [ 7:0] uart_status
   ,output reg         rd_valid
   ,output reg rd_valid_pulse
   ,output reg [ 3:0] rd_id
   ,output reg [ 2:0] rd_size
   ,output reg [31:0] rd_addr
   ,output reg [ 1:0] rd_burst
   ,output reg [ 7:0] rd_len
   ,output reg         rready
   ,output reg         bready
   ,output reg         wr_valid
   ,output reg wr_valid_pulse
   ,output reg [ 3:0] wr_id
   ,output reg [ 2:0] wr_size
   ,output reg [31:0] wr_addr
   ,output reg [ 1:0] wr_burst
   ,output reg [ 7:0] wr_len
   ,output reg [ 3:0] wr_wstrb
   ,output reg [ 3:0] wdata_mode
   ,input     [ 6:0] bresp_bid
   ,output reg bresp_bid_pulse
   ,output reg [31:0] push_wdata
   ,output reg push_wdata_pulse
);
wire [31:0] mask = (rsize==0) ? 32'hff : (rsize==1) ? 32'hffff :  32'hffffffff;
wire [31:0] mpdata = (rsize==0) ? {4{wrdata[7:0]}} : (rsize==1) ? {2{wrdata[15:0]}} :  wrdata;
wire [6:0] mpaddr = addr[6:0] & 7'h7c;
assign rdata = 
    (mpaddr[6:0]=='h0) ? {16'b0,uart_baudrate} :
    (mpaddr[6:0]=='h4) ? {24'b0,uart_control} :
    (mpaddr[6:0]=='h8) ? {24'b0,uart_status} :
    (mpaddr[6:0]=='hc) ? {31'b0,rd_valid} :
    (mpaddr[6:0]=='h10) ? {28'b0,rd_id} :
    (mpaddr[6:0]=='h14) ? {29'b0,rd_size} :
    (mpaddr[6:0]=='h18) ? rd_addr :
    (mpaddr[6:0]=='h1c) ? {30'b0,rd_burst} :
    (mpaddr[6:0]=='h20) ? {24'b0,rd_len} :
    (mpaddr[6:0]=='h24) ? {31'b0,rready} :
    (mpaddr[6:0]=='h28) ? {31'b0,bready} :
    (mpaddr[6:0]=='h2c) ? {31'b0,wr_valid} :
    (mpaddr[6:0]=='h30) ? {28'b0,wr_id} :
    (mpaddr[6:0]=='h34) ? {29'b0,wr_size} :
    (mpaddr[6:0]=='h38) ? wr_addr :
    (mpaddr[6:0]=='h3c) ? {30'b0,wr_burst} :
    (mpaddr[6:0]=='h40) ? {24'b0,wr_len} :
    (mpaddr[6:0]=='h44) ? {28'b0,wr_wstrb} :
    (mpaddr[6:0]=='h48) ? {28'b0,wdata_mode} :
    (mpaddr[6:0]=='h4c) ? {25'b0,bresp_bid} :
    (mpaddr[6:0]=='h50) ? push_wdata :
    32'b0;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        uart_baudrate <= 16'h5;
        uart_control <= 8'h50;
        rd_valid <= 1'h0;
        rd_id <= 4'h0;
        rd_size <= 3'h2;
        rd_addr <= 32'h0;
        rd_burst <= 2'h1;
        rd_len <= 8'h0;
        rready <= 1'h1;
        bready <= 1'h1;
        wr_valid <= 1'h0;
        wr_id <= 4'h0;
        wr_size <= 3'h2;
        wr_addr <= 32'h0;
        wr_burst <= 2'h1;
        wr_len <= 8'h0;
        wr_wstrb <= 4'hf;
        wdata_mode <= 4'h0;
        push_wdata <= 32'h0;
    end else if (rwrite && rsel)  begin
        if (mpaddr[6:0]=='h0) uart_baudrate[15:0] <= (uart_baudrate[15:0] & ~mask[15:0]) | (mpdata[15:0] &mask[15:0]);
        if (mpaddr[6:0]=='h4) uart_control[7:0] <= (uart_control[7:0] & ~mask[7:0]) | (mpdata[7:0] &mask[7:0]);
        if (mpaddr[6:0]=='hc) rd_valid <= (rd_valid & ~mask[0]) | (mpdata[0] &mask[0]);
        if (mpaddr[6:0]=='h10) rd_id[3:0] <= (rd_id[3:0] & ~mask[3:0]) | (mpdata[3:0] &mask[3:0]);
        if (mpaddr[6:0]=='h14) rd_size[2:0] <= (rd_size[2:0] & ~mask[2:0]) | (mpdata[2:0] &mask[2:0]);
        if (mpaddr[6:0]=='h18) rd_addr[31:0] <= (rd_addr[31:0] & ~mask[31:0]) | (mpdata &mask);
        if (mpaddr[6:0]=='h1c) rd_burst[1:0] <= (rd_burst[1:0] & ~mask[1:0]) | (mpdata[1:0] &mask[1:0]);
        if (mpaddr[6:0]=='h20) rd_len[7:0] <= (rd_len[7:0] & ~mask[7:0]) | (mpdata[7:0] &mask[7:0]);
        if (mpaddr[6:0]=='h24) rready <= (rready & ~mask[0]) | (mpdata[0] &mask[0]);
        if (mpaddr[6:0]=='h28) bready <= (bready & ~mask[0]) | (mpdata[0] &mask[0]);
        if (mpaddr[6:0]=='h2c) wr_valid <= (wr_valid & ~mask[0]) | (mpdata[0] &mask[0]);
        if (mpaddr[6:0]=='h30) wr_id[3:0] <= (wr_id[3:0] & ~mask[3:0]) | (mpdata[3:0] &mask[3:0]);
        if (mpaddr[6:0]=='h34) wr_size[2:0] <= (wr_size[2:0] & ~mask[2:0]) | (mpdata[2:0] &mask[2:0]);
        if (mpaddr[6:0]=='h38) wr_addr[31:0] <= (wr_addr[31:0] & ~mask[31:0]) | (mpdata &mask);
        if (mpaddr[6:0]=='h3c) wr_burst[1:0] <= (wr_burst[1:0] & ~mask[1:0]) | (mpdata[1:0] &mask[1:0]);
        if (mpaddr[6:0]=='h40) wr_len[7:0] <= (wr_len[7:0] & ~mask[7:0]) | (mpdata[7:0] &mask[7:0]);
        if (mpaddr[6:0]=='h44) wr_wstrb[3:0] <= (wr_wstrb[3:0] & ~mask[3:0]) | (mpdata[3:0] &mask[3:0]);
        if (mpaddr[6:0]=='h48) wdata_mode[3:0] <= (wdata_mode[3:0] & ~mask[3:0]) | (mpdata[3:0] &mask[3:0]);
        if (mpaddr[6:0]=='h50) push_wdata[31:0] <= (push_wdata[31:0] & ~mask[31:0]) | (mpdata &mask);
    end 
end 
always @(posedge clk)  rd_valid_pulse <= rwrite && rsel &&  (mpaddr[6:0]=='hc);
always @(posedge clk)  wr_valid_pulse <= rwrite && rsel &&  (mpaddr[6:0]=='h2c);
always @(posedge clk)  bresp_bid_pulse <= !rwrite && rsel &&  (mpaddr[6:0]=='h4c);
always @(posedge clk)  push_wdata_pulse <= rwrite && rsel &&  (mpaddr[6:0]=='h50);
endmodule
