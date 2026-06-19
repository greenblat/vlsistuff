`timescale 1ns / 1ps
module cpu_ram ( input clk
    ,input ram_rd
    ,input ram_wr
    ,input ram_fetch
    ,input [15:0] addr
    ,input [31:0] wdata
    ,output reg [31:0] rdata
    ,output ready

);

localparam SIZE = 1<<14;
reg [31:0] pram [0:SIZE-1];
reg [31:0] dram [0:SIZE-1];
integer ii;
initial begin
    #1;
    $readmemh("pram.hex",pram);
    $readmemh("dram.hex",dram);
end

wire [31:0] ram0 = pram[0];


wire panic0 = ram_rd && ram_wr;


always @(posedge clk) begin
    if (ram_rd && ram_fetch) begin
        rdata <= pram[addr[14:2]];
    end else if (ram_rd && !ram_fetch) begin
        rdata <= dram[addr[14:2]];
    end  else 
        rdata <= 0;

    if (ram_wr) begin
        dram[addr[14:2]] <=  wdata;
    end
end
assign ready = 1;

wire [31:0] dbg0 = dram[0];
wire [31:0] dbg4 = dram[1];
wire [31:0] dbg8 = dram[2];
wire [31:0] dbgc = dram[3];
wire [31:0] dbg10 = dram[4];
wire [31:0] dbg14 = dram[5];
wire [31:0] dbg18 = dram[6];
wire [31:0] dbg1c = dram[7];
wire [31:0] dbg20 = dram[8];
wire [31:0] dbg24 = dram[9];
wire [31:0] dbg28 = dram[10];
wire [31:0] dbg2c = dram[11];
wire [31:0] dbg30 = dram[12];

wire [63:0]  sign_version = 64'h0000f79f020326 ;
endmodule

