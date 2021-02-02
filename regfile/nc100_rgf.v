
module nc100_rgf (input pclk, input presetn,
    input psel, input penable, input pwrite, input [4-1:0] pstrb, input [16-1:0] paddr, input [32-1:0] pwdata, output [32-1:0] prdata
    ,output pready, output pslverr
    ,output [31:0] rega
    ,output [31:0] control0
    ,output regb_pulse
    ,input [31:0] extern
    ,output extern_rd_pulse
    ,output extern_wr_pulse
    ,output [31:0] eth0tmp0
    ,output [23:0] eth0tmp1
    ,output [15:0] eth0tmp2
    ,output [31:0] eth1tmp0
    ,output [23:0] eth1tmp1
    ,output [15:0] eth1tmp2
    ,output [31:0] eth2tmp0
    ,output [23:0] eth2tmp1
    ,output [15:0] eth2tmp2
    ,output [31:0] eth3tmp0
    ,output [23:0] eth3tmp1
    ,output [15:0] eth3tmp2
    ,input [31:0] ronly
    ,output ronly_pulse
    ,input ronly_ready
    ,input [15:0] ronly2
    ,output ronly2_pulse
    ,input ronly2_ready
    ,input [31:0] ldst_ram_rdata
    ,output [31:0] ldst_ram_wdata
    ,output [6:0] ldst_ram_addr
    ,output ldst_ram_rd_pulse
    ,output ldst_ram_wr_pulse
    ,input  [1:0] dma0
    ,input  [7:0] cpu1
    ,input  [2:0] spi0
    ,output [1:0] odma
    ,output [7:0] ocpu
    ,output [2:0] ospi
    ,output [127:0] wider
    ,output [127:0] longer
);
    wire [23:0] statusa;
    wire [23:0] regb;
    wire [127:0] wider;
    wire [127:0] longer;

wire i_pread = psel && !pwrite;
wire i_pwrite = psel && pwrite && penable;
assign pslverr = 0;
assign pready = 1;

wire [1023:0] ZEROES = 1024'b0;
nc100_rgf_ram rgf (.pclk(pclk),.presetn(presetn),.pwrite(i_pwrite),.pread(i_pread),.paddr(paddr)
    ,.pwdata(pwdata),.prdata(prdata)
    ,.pstrb(pstrb)
    ,.rega(rega)
    ,.control0(control0)
    ,.statusa(ZEROES[23:0] | statusa)
    ,.regb(regb)
    ,.regb_pulse(regb_pulse)
    ,.extern(extern)
    ,.extern_rd_pulse(extern_rd_pulse)
    ,.extern_wr_pulse(extern_wr_pulse)
    ,.eth0tmp0(eth0tmp0)
    ,.eth0tmp1(eth0tmp1)
    ,.eth0tmp2(eth0tmp2)
    ,.eth1tmp0(eth1tmp0)
    ,.eth1tmp1(eth1tmp1)
    ,.eth1tmp2(eth1tmp2)
    ,.eth2tmp0(eth2tmp0)
    ,.eth2tmp1(eth2tmp1)
    ,.eth2tmp2(eth2tmp2)
    ,.eth3tmp0(eth3tmp0)
    ,.eth3tmp1(eth3tmp1)
    ,.eth3tmp2(eth3tmp2)
    ,.wider(wider)
    ,.longer(longer)
    ,.ronly(ronly)
    ,.ronly_pulse(ronly_pulse)
    ,.ronly_ready(ronly_ready)
    ,.ronly2(ronly2)
    ,.ronly2_pulse(ronly2_pulse)
    ,.ronly2_ready(ronly2_ready)
    ,.ldst_ram_rdata(ldst_ram_rdata)
    ,.ldst_ram_wdata(ldst_ram_wdata)
    ,.ldst_ram_addr(ldst_ram_addr)
    ,.ldst_ram_rd_pulse(ldst_ram_rd_pulse)
    ,.ldst_ram_wr_pulse(ldst_ram_wr_pulse)
);
assign statusa[1:0] = dma0;
assign statusa[15:8] = cpu1;
assign statusa[18:16] = spi0;
assign odma = regb[1:0];
assign ocpu = regb[15:8];
assign ospi = regb[18:16];
endmodule
module nc100_rgf_ram (
    input pclk,input presetn,input pwrite, input pread
    ,input [32-1:0] pwdata, output [32-1:0] prdata
    ,input [4-1:0] pstrb
    ,input [16-1:0] paddr ,output reg [32-1:0] last_wdata
    ,output reg [31:0] rega
    ,output reg [31:0] control0
    ,input [23:0] statusa
    ,output reg [23:0] regb
    ,output regb_pulse
    ,input [31:0] extern
    ,output extern_rd_pulse
    ,output extern_wr_pulse
    ,output reg [31:0] eth0tmp0
    ,output reg [23:0] eth0tmp1
    ,output reg [15:0] eth0tmp2
    ,output reg [31:0] eth1tmp0
    ,output reg [23:0] eth1tmp1
    ,output reg [15:0] eth1tmp2
    ,output reg [31:0] eth2tmp0
    ,output reg [23:0] eth2tmp1
    ,output reg [15:0] eth2tmp2
    ,output reg [31:0] eth3tmp0
    ,output reg [23:0] eth3tmp1
    ,output reg [15:0] eth3tmp2
    ,output reg [127:0] wider
    ,input [127:0] longer
    ,input [31:0] ronly
    ,output ronly_pulse
    ,input ronly_ready
    ,input [15:0] ronly2
    ,output ronly2_pulse
    ,input ronly2_ready
    ,input [31:0] ldst_ram_rdata
    ,output [31:0] ldst_ram_wdata
    ,output [6:0] ldst_ram_addr
    ,output ldst_ram_rd_pulse
    ,output ldst_ram_wr_pulse

);
wire [16-1:0] mpaddr = (pread||pwrite) ? (paddr - 'h0)  : 0;
wire [32-1:0] prdata_wire =

    (mpaddr == 'h0) ? rega[31:0] :
    (mpaddr == 'h4) ? control0[31:0] :
    (mpaddr == 'h8) ? {8'b0,statusa} :
    (mpaddr == 'hc) ? {8'b0,regb} :
    (mpaddr == 'h10) ? extern[31:0] :
    (mpaddr == 'h100) ? eth0tmp0[31:0] :
    (mpaddr == 'h104) ? {8'b0,eth0tmp1} :
    (mpaddr == 'h108) ? {16'b0,eth0tmp2} :
    (mpaddr == 'h200) ? eth1tmp0[31:0] :
    (mpaddr == 'h204) ? {8'b0,eth1tmp1} :
    (mpaddr == 'h208) ? {16'b0,eth1tmp2} :
    (mpaddr == 'h300) ? eth2tmp0[31:0] :
    (mpaddr == 'h304) ? {8'b0,eth2tmp1} :
    (mpaddr == 'h308) ? {16'b0,eth2tmp2} :
    (mpaddr == 'h400) ? eth3tmp0[31:0] :
    (mpaddr == 'h404) ? {8'b0,eth3tmp1} :
    (mpaddr == 'h408) ? {16'b0,eth3tmp2} :
    (mpaddr == 'h40c) ? wider[31:0] :
    (mpaddr == 'h410) ? wider[63:32] :
    (mpaddr == 'h414) ? wider[95:64] :
    (mpaddr == 'h418) ? wider[127:96] :
    (mpaddr == 'h41c) ? longer[31:0] :
    (mpaddr == 'h420) ? longer[63:32] :
    (mpaddr == 'h424) ? longer[95:64] :
    (mpaddr == 'h428) ? longer[127:96] :
    (mpaddr == 'h42c) ? ronly[31:0] :
    (mpaddr == 'h430) ? {16'b0,ronly2} :
    32'hdeadbeaf;
wire ldst_ram_rd_data_valid;


reg [32-1:0] prdata_reg;
always @(posedge pclk) prdata_reg <=  prdata_wire;
assign prdata =       ldst_ram_rd_data_valid ? ldst_ram_rdata :

    prdata_reg;

wire [32-1:0] mask = { {{8{pstrb[3]}},{8{pstrb[2]}},{8{pstrb[1]}},{8{pstrb[0]}}} };
wire [32-1:0] wdata = pwdata;
always @(posedge pclk) if (pwrite) last_wdata <= wdata & mask;
always @(posedge pclk or negedge presetn) begin
    if (!presetn) begin 
        rega <= 32'h123456;
        control0 <= 32'hcc00;
        regb <= 24'h0;
        eth0tmp0 <= 32'h0;
        eth0tmp1 <= 24'h0;
        eth0tmp2 <= 16'h0;
        eth1tmp0 <= 32'h0;
        eth1tmp1 <= 24'h0;
        eth1tmp2 <= 16'h0;
        eth2tmp0 <= 32'h0;
        eth2tmp1 <= 24'h0;
        eth2tmp2 <= 16'h0;
        eth3tmp0 <= 32'h0;
        eth3tmp1 <= 24'h0;
        eth3tmp2 <= 16'h0;
        wider <= 128'h0;
    end else if (pwrite)  begin
        if (mpaddr == 'h0) rega <= (rega & ~mask) | (wdata & mask);
        if (mpaddr == 'h4) control0 <= (control0 & ~mask) | (wdata & mask);
        if (mpaddr == 'hc) regb <= 24'h7ff03 & ((regb & ~mask) | (wdata & mask));
        if (mpaddr == 'h100) eth0tmp0 <= (eth0tmp0 & ~mask) | (wdata & mask);
        if (mpaddr == 'h104) eth0tmp1 <= (eth0tmp1 & ~mask) | (wdata & mask);
        if (mpaddr == 'h108) eth0tmp2 <= (eth0tmp2 & ~mask) | (wdata & mask);
        if (mpaddr == 'h200) eth1tmp0 <= (eth1tmp0 & ~mask) | (wdata & mask);
        if (mpaddr == 'h204) eth1tmp1 <= (eth1tmp1 & ~mask) | (wdata & mask);
        if (mpaddr == 'h208) eth1tmp2 <= (eth1tmp2 & ~mask) | (wdata & mask);
        if (mpaddr == 'h300) eth2tmp0 <= (eth2tmp0 & ~mask) | (wdata & mask);
        if (mpaddr == 'h304) eth2tmp1 <= (eth2tmp1 & ~mask) | (wdata & mask);
        if (mpaddr == 'h308) eth2tmp2 <= (eth2tmp2 & ~mask) | (wdata & mask);
        if (mpaddr == 'h400) eth3tmp0 <= (eth3tmp0 & ~mask) | (wdata & mask);
        if (mpaddr == 'h404) eth3tmp1 <= (eth3tmp1 & ~mask) | (wdata & mask);
        if (mpaddr == 'h408) eth3tmp2 <= (eth3tmp2 & ~mask) | (wdata & mask);
        if (mpaddr == 'h40c) wider[31:0] <= (wider[31:0] & ~mask) | (wdata & mask);
        if (mpaddr == 'h410) wider[63:32] <= (wider[63:32] & ~mask) | (wdata & mask);
        if (mpaddr == 'h414) wider[95:64] <= (wider[95:64] & ~mask) | (wdata & mask);
        if (mpaddr == 'h418) wider[127:96] <= (wider[127:96] & ~mask) | (wdata & mask);
    end
end

wire regb_wr_sel = pwrite && (mpaddr=='hc);
reg regb_wr_pulse_reg; always @(posedge pclk)  regb_wr_pulse_reg <= regb_wr_sel;
assign regb_pulse = regb_wr_pulse_reg;


wire extern_rd_sel = pread && (mpaddr=='h10);
reg extern_rd_pulse_reg; always @(posedge pclk)  extern_rd_pulse_reg <= extern_rd_sel;
assign extern_rd_pulse = extern_rd_pulse_reg;


wire extern_wr_sel = pwrite && (mpaddr=='h10);
reg extern_wr_pulse_reg; always @(posedge pclk)  extern_wr_pulse_reg <= extern_wr_sel;
assign extern_wr_pulse = extern_wr_pulse_reg;


wire ronly_rd_sel = pread && (mpaddr=='h42c);
reg ronly_rd_pulse_reg; always @(posedge pclk)  ronly_rd_pulse_reg <= ronly_rd_sel;
assign ronly_pulse = ronly_rd_pulse_reg;


wire ronly2_rd_sel = pread && (mpaddr=='h430);
reg ronly2_rd_pulse_reg; always @(posedge pclk)  ronly2_rd_pulse_reg <= ronly2_rd_sel;
assign ronly2_pulse = ronly2_rd_pulse_reg;

wire [2:0] ExtraBytesldst_ram  =  pstrb[0] ? 0 : pstrb[1] ? 1 : pstrb[2] ? 2 : pstrb[3] ? 3 : 0;
assign ldst_ram_addr = ((mpaddr - 'h800)>>2);
assign ldst_ram_wdata = wdata;

assign ldst_ram_rd_pulse = pread && (mpaddr>='h800) && (mpaddr < 'ha00);
reg ldst_ram_rd_pulse_dly; always @(posedge pclk)  ldst_ram_rd_pulse_dly <= ldst_ram_rd_pulse;
assign ldst_ram_rd_data_valid = ldst_ram_rd_pulse_dly;


assign ldst_ram_wr_pulse = pwrite && (mpaddr>='h800) && (mpaddr < 'ha00);

endmodule
