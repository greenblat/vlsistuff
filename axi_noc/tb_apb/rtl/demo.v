
module demo (input pclk, input presetn,
    input psel, input penable, input pwrite, input [4-1:0] pstrb, input [20-1:0] paddr, input [32-1:0] pwdata, output [32-1:0] prdata,output [32-1:0] prdata_wire
    ,output pready, output pslverr
    ,output [127:0] key0
    ,output [127:0] key1
    ,output [7:0] [19:0] limits0
    ,output [7:0] [19:0] limits1
);

wire i_pread = psel && !pwrite;
wire i_pwrite = psel && pwrite && penable;
assign pslverr = 0;
assign pready = 1;
wire [31:0] last_wdata;

wire [1023:0] ZEROES = 1024'b0;
// wire [31:0] last_wdata;
demo_ram rgf (.pclk(pclk),.presetn(presetn),.pwrite(i_pwrite),.pread(i_pread),.paddr(paddr)
    ,.pwdata(pwdata),.prdata(prdata),.prdata_wire(prdata_wire)
    ,.pstrb(pstrb),.last_wdata(last_wdata)
    ,.penable(penable)
    ,.key0(key0)
    ,.key1(key1)
    ,.limits0(limits0)
    ,.limits1(limits1)
);
endmodule
module demo_ram (
    input pclk,input presetn,input pwrite, input pread, input penable
    ,input [32-1:0] pwdata, output [32-1:0] prdata, output [32-1:0] prdata_wire
    ,input [4-1:0] pstrb
    ,input [20-1:0] paddr ,output reg [32-1:0] last_wdata
    ,output reg [127:0] key0
    ,output reg [127:0] key1
    ,output reg [7:0] [19:0] limits0
    ,output reg [7:0] [19:0] limits1
);
wire [32-1:0] wdata = pwdata;

wire [20-1:0] mpaddr0 =  20'h7c & (paddr - 'h0);
wire [20-1:0] mpaddr = (pread||pwrite) ? mpaddr0  : 0;
assign prdata_wire =

    (mpaddr == 'h0) ? key0[31:0] :
    (mpaddr == 'h4) ? key0[63:32] :
    (mpaddr == 'h8) ? key0[95:64] :
    (mpaddr == 'hc) ? key0[127:96] :
    (mpaddr == 'h10) ? key1[31:0] :
    (mpaddr == 'h14) ? key1[63:32] :
    (mpaddr == 'h18) ? key1[95:64] :
    (mpaddr == 'h1c) ? key1[127:96] :
    (mpaddr == 'h20) ? {12'b0,limits0[0]} :
    (mpaddr == 'h24) ? {12'b0,limits0[1]} :
    (mpaddr == 'h28) ? {12'b0,limits0[2]} :
    (mpaddr == 'h2c) ? {12'b0,limits0[3]} :
    (mpaddr == 'h30) ? {12'b0,limits0[4]} :
    (mpaddr == 'h34) ? {12'b0,limits0[5]} :
    (mpaddr == 'h38) ? {12'b0,limits0[6]} :
    (mpaddr == 'h3c) ? {12'b0,limits0[7]} :
    (mpaddr == 'h40) ? {12'b0,limits1[0]} :
    (mpaddr == 'h44) ? {12'b0,limits1[1]} :
    (mpaddr == 'h48) ? {12'b0,limits1[2]} :
    (mpaddr == 'h4c) ? {12'b0,limits1[3]} :
    (mpaddr == 'h50) ? {12'b0,limits1[4]} :
    (mpaddr == 'h54) ? {12'b0,limits1[5]} :
    (mpaddr == 'h58) ? {12'b0,limits1[6]} :
    (mpaddr == 'h5c) ? {12'b0,limits1[7]} :
    32'hdeadbeaf;



reg [32-1:0] prdata_reg;
always @(posedge pclk) prdata_reg <=  prdata_wire;
assign prdata =   
    prdata_reg;

wire [32-1:0] mask = { {{8{pstrb[3]}},{8{pstrb[2]}},{8{pstrb[1]}},{8{pstrb[0]}}} };
always @(posedge pclk) if (pwrite) last_wdata <= wdata & mask;
always @(posedge pclk or negedge presetn) begin
    if (!presetn) begin 
        key0 <= 128'h0;
        key1 <= 128'h0;
        limits0 <= 160'h0;
        limits1 <= 160'h0;
    end else if (pwrite)  begin
        if (mpaddr == 'h0) key0[31:0] <= (key0[31:0] & ~mask) | (wdata & mask);
        if (mpaddr == 'h4) key0[63:32] <= (key0[63:32] & ~mask) | (wdata & mask);
        if (mpaddr == 'h8) key0[95:64] <= (key0[95:64] & ~mask) | (wdata & mask);
        if (mpaddr == 'hc) key0[127:96] <= (key0[127:96] & ~mask) | (wdata & mask);
        if (mpaddr == 'h10) key1[31:0] <= (key1[31:0] & ~mask) | (wdata & mask);
        if (mpaddr == 'h14) key1[63:32] <= (key1[63:32] & ~mask) | (wdata & mask);
        if (mpaddr == 'h18) key1[95:64] <= (key1[95:64] & ~mask) | (wdata & mask);
        if (mpaddr == 'h1c) key1[127:96] <= (key1[127:96] & ~mask) | (wdata & mask);
        if (mpaddr == 'h20) limits0[0] <= (limits0[0] & ~mask) | (wdata & mask);
        if (mpaddr == 'h24) limits0[1] <= (limits0[1] & ~mask) | (wdata & mask);
        if (mpaddr == 'h28) limits0[2] <= (limits0[2] & ~mask) | (wdata & mask);
        if (mpaddr == 'h2c) limits0[3] <= (limits0[3] & ~mask) | (wdata & mask);
        if (mpaddr == 'h30) limits0[4] <= (limits0[4] & ~mask) | (wdata & mask);
        if (mpaddr == 'h34) limits0[5] <= (limits0[5] & ~mask) | (wdata & mask);
        if (mpaddr == 'h38) limits0[6] <= (limits0[6] & ~mask) | (wdata & mask);
        if (mpaddr == 'h3c) limits0[7] <= (limits0[7] & ~mask) | (wdata & mask);
        if (mpaddr == 'h40) limits1[0] <= (limits1[0] & ~mask) | (wdata & mask);
        if (mpaddr == 'h44) limits1[1] <= (limits1[1] & ~mask) | (wdata & mask);
        if (mpaddr == 'h48) limits1[2] <= (limits1[2] & ~mask) | (wdata & mask);
        if (mpaddr == 'h4c) limits1[3] <= (limits1[3] & ~mask) | (wdata & mask);
        if (mpaddr == 'h50) limits1[4] <= (limits1[4] & ~mask) | (wdata & mask);
        if (mpaddr == 'h54) limits1[5] <= (limits1[5] & ~mask) | (wdata & mask);
        if (mpaddr == 'h58) limits1[6] <= (limits1[6] & ~mask) | (wdata & mask);
        if (mpaddr == 'h5c) limits1[7] <= (limits1[7] & ~mask) | (wdata & mask);
    end
end
endmodule
