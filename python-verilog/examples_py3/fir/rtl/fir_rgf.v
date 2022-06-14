
module fir_rgf (input pclk, input presetn,
    input psel, input penable, input pwrite, input [4-1:0] pstrb, input [32-1:0] paddr, input [32-1:0] pwdata, output [32-1:0] prdata,output [32-1:0] prdata_wire
    ,output pready, output pslverr
    ,output  enable
    ,output [3:0] scalefactor
    ,output [7:0] [7:0] coeffs
    ,input [31:0] goods
    ,input [31:0] bads
);

wire i_pread = psel && !pwrite;
wire i_pwrite = psel && pwrite && penable;
assign pslverr = 0;
assign pready = 1;
wire [31:0] last_wdata;

wire [1023:0] ZEROES = 1024'b0;
fir_rgf_ram rgf (.pclk(pclk),.presetn(presetn),.pwrite(i_pwrite),.pread(i_pread),.paddr(paddr)
    ,.pwdata(pwdata),.prdata(prdata),.prdata_wire(prdata_wire)
    ,.pstrb(pstrb),.last_wdata(last_wdata)
    ,.penable(penable)
    ,.enable(enable)
    ,.scalefactor(scalefactor)
    ,.coeffs(coeffs)
    ,.goods(goods)
    ,.bads(bads)
);
endmodule
module fir_rgf_ram (
    input pclk,input presetn,input pwrite, input pread, input penable
    ,input [32-1:0] pwdata, output [32-1:0] prdata, output [32-1:0] prdata_wire
    ,input [4-1:0] pstrb
    ,input [32-1:0] paddr ,output reg [32-1:0] last_wdata
    ,output pready
    ,output reg  enable
    ,output reg [3:0] scalefactor
    ,output reg [7:0] [7:0] coeffs
    ,input [31:0] goods
    ,input [31:0] bads
);
wire [32-1:0] wdata = pwdata;

wire [32-1:0] mpaddr0 =  32'hfffffffc & (paddr - 'h0);
wire [32-1:0] mpaddr = (pread||pwrite) ? mpaddr0  : 0;
assign prdata_wire =

    (mpaddr == 'h0) ? {31'b0,enable} :
    (mpaddr == 'h4) ? {28'b0,scalefactor} :
    (mpaddr == 'h8) ? {24'b0,coeffs[0]} :
    (mpaddr == 'hc) ? {24'b0,coeffs[1]} :
    (mpaddr == 'h10) ? {24'b0,coeffs[2]} :
    (mpaddr == 'h14) ? {24'b0,coeffs[3]} :
    (mpaddr == 'h18) ? {24'b0,coeffs[4]} :
    (mpaddr == 'h1c) ? {24'b0,coeffs[5]} :
    (mpaddr == 'h20) ? {24'b0,coeffs[6]} :
    (mpaddr == 'h24) ? {24'b0,coeffs[7]} :
    (mpaddr == 'h28) ? goods[31:0] :
    (mpaddr == 'h2c) ? bads[31:0] :
    32'hdeaddead;



reg [32-1:0] prdata_reg;
always @(posedge pclk) prdata_reg <=  prdata_wire;
assign pready = 1;

assign prdata =   
    prdata_reg;

wire [32-1:0] mask = { {{8{pstrb[3]}},{8{pstrb[2]}},{8{pstrb[1]}},{8{pstrb[0]}}} };
always @(posedge pclk) if (pwrite) last_wdata <= wdata & mask;
always @(posedge pclk or negedge presetn) begin
    if (!presetn) begin 
        enable <= 1'h0;
        scalefactor <= 4'h0;
        coeffs <= 64'h0;
    end else if (pwrite)  begin
        if (mpaddr == 'h0) enable <= (enable & ~mask[0:0]) | (wdata[0:0] & mask[0:0]);
        if (mpaddr == 'h4) scalefactor <= (scalefactor & ~mask[3:0]) | (wdata[3:0] & mask[3:0]);
        if (mpaddr == 'h8) coeffs[0] <= (coeffs[0] & ~mask) | (wdata & mask);
        if (mpaddr == 'hc) coeffs[1] <= (coeffs[1] & ~mask) | (wdata & mask);
        if (mpaddr == 'h10) coeffs[2] <= (coeffs[2] & ~mask) | (wdata & mask);
        if (mpaddr == 'h14) coeffs[3] <= (coeffs[3] & ~mask) | (wdata & mask);
        if (mpaddr == 'h18) coeffs[4] <= (coeffs[4] & ~mask) | (wdata & mask);
        if (mpaddr == 'h1c) coeffs[5] <= (coeffs[5] & ~mask) | (wdata & mask);
        if (mpaddr == 'h20) coeffs[6] <= (coeffs[6] & ~mask) | (wdata & mask);
        if (mpaddr == 'h24) coeffs[7] <= (coeffs[7] & ~mask) | (wdata & mask);
    end
end
endmodule
