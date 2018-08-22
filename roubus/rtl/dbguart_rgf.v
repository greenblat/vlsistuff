module dbguart_rgf (input clk,input rst_n,input rwrite, input rsel, input [1:0] rsize, input [31:0] wrdata, output [31:0] rdata, input [4:0] addr
   ,output reg [ 7:0] uart_control
   ,output reg [15:0] baudrate
   ,input     [31:0] control
   ,input     [31:0] base_address
);
wire [31:0] mask = (rsize==1) ? 32'hff : (rsize==2) ? 32'hffff :  32'hffffffff;
wire [31:0] wdata = (rsize==1) ? {4{wrdata[7:0]}} : (rsize==2) ? {2{wrdata[15:0]}} :  wrdata;
wire [4:0] mpaddr = addr[4:0] & 5'h1c;
assign rdata = 
    (mpaddr[4:0]=='h0) ? {24'b0,uart_control} :
    (mpaddr[4:0]=='h4) ? {16'b0,baudrate} :
    (mpaddr[4:0]=='h8) ? control :
    (mpaddr[4:0]=='hc) ? base_address :
    32'b0;
always @(posedge clk ) begin
    if (!rst_n) begin
        uart_control <= 8'h50;
        baudrate <= 16'h6;
    end else if (rwrite && rsel)  begin
        if (mpaddr[4:0]=='h0) uart_control <= wdata[7:0];
        if (mpaddr[4:0]=='h4) baudrate <= (baudrate[15:0] & ~mask[15:0]) | (wdata &mask);
    end 
end 
endmodule
