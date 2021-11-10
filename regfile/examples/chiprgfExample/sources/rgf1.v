
module rgf1 (input pclk, input presetn,
    input psel, input penable, input pwrite, input [4-1:0] pstrb, input [16-1:0] paddr, input [32-1:0] pwdata, output [32-1:0] prdata,output [32-1:0] prdata_wire
    ,output pready, output pslverr
    ,input [31:0] ronly
    ,output ronly_pulse
    ,input ronly_ready
    ,input [15:0] ronly2
    ,output ronly2_pulse
    ,input ronly2_ready
    ,output [15:0] wonly
    ,output wonly_pulse
    ,input wonly_ready
    ,output  one
    ,output [31:0] rega
    ,output [31:0] control0
    ,output regb_pulse
    ,input [31:0] w1cc
    ,output [31:0] w1cc_out_reg
    ,input [16:0] ramx_rdata
    ,output [16:0] ramx_wdata
    ,output [7:0] ramx_addr
    ,output ramx_rd_pulse
    ,output ramx_wr_pulse
    ,input ramx_ready
    ,output [31:0] rega
    ,output [31:0] control0
    ,output regb_pulse
    ,input [31:0] extern
    ,output  extern_rd_pulse
    ,output  extern_wr_pulse
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
    ,output [127:0] wider
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
    ,input [31:0] ronly
    ,output ronly_pulse
    ,input ronly_ready
    ,input [15:0] ronly2
    ,output ronly2_pulse
    ,input ronly2_ready
    ,output [15:0] wonly
    ,output wonly_pulse
    ,input wonly_ready
    ,output  one
    ,output [31:0] rega
    ,output [31:0] control0
    ,output regb_pulse
    ,input [31:0] w1cc
    ,output [31:0] w1cc_out_reg
    ,input [16:0] ramx_rdata
    ,output [16:0] ramx_wdata
    ,output [7:0] ramx_addr
    ,output ramx_rd_pulse
    ,output ramx_wr_pulse
    ,input ramx_ready
    ,input  [1:0] dma0
    ,input  [7:0] cpu1
    ,input  [2:0] spi0
    ,output [1:0] odma
    ,output [7:0] ocpu
    ,output [2:0] ospi
    ,output  badfwr_flag
    ,input   badfro_flag
    ,input  [1:0] dma0
    ,input  [7:0] cpu1
    ,input  [2:0] spi0
    ,output [1:0] odma
    ,output [7:0] ocpu
    ,output [2:0] ospi
    ,input  [1:0] dma0
    ,input  [7:0] cpu1
    ,input  [2:0] spi0
    ,output [1:0] odma
    ,output [7:0] ocpu
    ,output [2:0] ospi
    ,output  badfwr_flag
    ,input   badfro_flag
);
    wire [23:0] statusa; // hhh
    wire [23:0] regb; // hhh
    wire  badfwr; // hhh
    wire  badfro; // hhh
    wire [23:0] statusa; // hhh
    wire [23:0] regb; // hhh
    wire [23:0] statusa; // hhh
    wire [23:0] regb; // hhh
    wire  badfwr; // hhh
    wire  badfro; // hhh

wire i_pread = psel && !pwrite;
wire i_pwrite = psel && pwrite && penable;
assign pslverr = 0;
assign pready = 
    ronly_pulse ? ronly_ready :
    ronly2_pulse ? ronly2_ready :
    wonly_pulse ? wonly_ready :
    (ramx_wr_pulse || ramx_rd_pulse) ? ramx_ready :
    ronly_pulse ? ronly_ready :
    ronly2_pulse ? ronly2_ready :
    ronly_pulse ? ronly_ready :
    ronly2_pulse ? ronly2_ready :
    wonly_pulse ? wonly_ready :
    (ramx_wr_pulse || ramx_rd_pulse) ? ramx_ready :
    1;
wire [31:0] last_wdata;

wire [1023:0] ZEROES = 1024'b0;
// wire [31:0] last_wdata;
rgf1_ram rgf (.pclk(pclk),.presetn(presetn),.pwrite(i_pwrite),.pread(i_pread),.paddr(paddr)
    ,.pwdata(pwdata),.prdata(prdata),.prdata_wire(prdata_wire)
    ,.pstrb(pstrb),.last_wdata(last_wdata)
    ,.penable(penable)
    ,.ronly(ronly)
    ,.ronly_pulse(ronly_pulse)
    ,.ronly_ready(ronly_ready)
    ,.ronly2(ronly2)
    ,.ronly2_pulse(ronly2_pulse)
    ,.ronly2_ready(ronly2_ready)
    ,.wonly(wonly)
    ,.wonly_pulse(wonly_pulse)
    ,.wonly_ready(wonly_ready)
    ,.one(one)
    ,.rega(rega)
    ,.control0(control0)
    ,.statusa(ZEROES[23:0] | statusa)
    ,.regb(regb)
    ,.regb_pulse(regb_pulse)
    ,.w1cc(w1cc)
    ,.w1cc_out_reg(w1cc_out_reg)
    ,.badfwr(badfwr)
    ,.badfro(badfro)
    ,.ramx_rdata(ramx_rdata)
    ,.ramx_wdata(ramx_wdata)
    ,.ramx_addr(ramx_addr)
    ,.ramx_rd_pulse(ramx_rd_pulse)
    ,.ramx_wr_pulse(ramx_wr_pulse)
    ,.ramx_ready(ramx_ready)
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
    ,.ronly(ronly)
    ,.ronly_pulse(ronly_pulse)
    ,.ronly_ready(ronly_ready)
    ,.ronly2(ronly2)
    ,.ronly2_pulse(ronly2_pulse)
    ,.ronly2_ready(ronly2_ready)
    ,.wonly(wonly)
    ,.wonly_pulse(wonly_pulse)
    ,.wonly_ready(wonly_ready)
    ,.one(one)
    ,.rega(rega)
    ,.control0(control0)
    ,.statusa(ZEROES[23:0] | statusa)
    ,.regb(regb)
    ,.regb_pulse(regb_pulse)
    ,.w1cc(w1cc)
    ,.w1cc_out_reg(w1cc_out_reg)
    ,.badfwr(badfwr)
    ,.badfro(badfro)
    ,.ramx_rdata(ramx_rdata)
    ,.ramx_wdata(ramx_wdata)
    ,.ramx_addr(ramx_addr)
    ,.ramx_rd_pulse(ramx_rd_pulse)
    ,.ramx_wr_pulse(ramx_wr_pulse)
    ,.ramx_ready(ramx_ready)
);
assign statusa[1:0] = dma0;
assign statusa[15:8] = cpu1;
assign statusa[18:16] = spi0;
assign statusa[7:2] = 0;
assign statusa[23:19] = 0;
assign odma = regb[1:0];
assign ocpu = regb[15:8];
assign ospi = regb[18:16];
assign badfwr_flag = badfwr;
assign badfro = badfro_flag;
assign statusa[1:0] = dma0;
assign statusa[15:8] = cpu1;
assign statusa[18:16] = spi0;
assign statusa[7:2] = 0;
assign statusa[23:19] = 0;
assign odma = regb[1:0];
assign ocpu = regb[15:8];
assign ospi = regb[18:16];
assign statusa[1:0] = dma0;
assign statusa[15:8] = cpu1;
assign statusa[18:16] = spi0;
assign statusa[7:2] = 0;
assign statusa[23:19] = 0;
assign odma = regb[1:0];
assign ocpu = regb[15:8];
assign ospi = regb[18:16];
assign badfwr_flag = badfwr;
assign badfro = badfro_flag;
endmodule
module rgf1_ram (
    input pclk,input presetn,input pwrite, input pread, input penable
    ,input [32-1:0] pwdata, output [32-1:0] prdata, output [32-1:0] prdata_wire
    ,input [4-1:0] pstrb
    ,input [16-1:0] paddr ,output reg [32-1:0] last_wdata
    ,input [31:0] ronly
    ,output ronly_pulse
    ,input ronly_ready
    ,input [15:0] ronly2
    ,output ronly2_pulse
    ,input ronly2_ready
    ,output reg [15:0] wonly
    ,output wonly_pulse
    ,input wonly_ready
    ,output reg  one
    ,output reg [31:0] rega
    ,output reg [31:0] control0
    ,input [23:0] statusa
    ,output reg [23:0] regb
    ,output regb_pulse
    ,input [31:0] w1cc
    ,output [31:0] w1cc_out_reg
    ,output reg  badfwr
    ,input  badfro
    ,input [16:0] ramx_rdata
    ,output [16:0] ramx_wdata
    ,output [7:0] ramx_addr
    ,output ramx_rd_pulse
    ,output ramx_wr_pulse
    ,input ramx_ready
    ,output reg [31:0] rega
    ,output reg [31:0] control0
    ,input [23:0] statusa
    ,output reg [23:0] regb
    ,output regb_pulse
    ,input [31:0] extern
    ,output  extern_rd_pulse
    ,output  extern_wr_pulse
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
    ,input [31:0] ronly
    ,output ronly_pulse
    ,input ronly_ready
    ,input [15:0] ronly2
    ,output ronly2_pulse
    ,input ronly2_ready
    ,output reg [15:0] wonly
    ,output wonly_pulse
    ,input wonly_ready
    ,output reg  one
    ,output reg [31:0] rega
    ,output reg [31:0] control0
    ,input [23:0] statusa
    ,output reg [23:0] regb
    ,output regb_pulse
    ,input [31:0] w1cc
    ,output [31:0] w1cc_out_reg
    ,output reg  badfwr
    ,input  badfro
    ,input [16:0] ramx_rdata
    ,output [16:0] ramx_wdata
    ,output [7:0] ramx_addr
    ,output ramx_rd_pulse
    ,output ramx_wr_pulse
    ,input ramx_ready
);
wire [32-1:0] wdata = pwdata;
    reg [31:0] w1cc_int;
assign w1cc_out_reg = w1cc_int;

wire w1cc_wr_sel;
always @(posedge pclk or negedge presetn) begin
    if (!presetn) begin 
        w1cc_int <= 0;
    end else begin
        w1cc_int <= (w1cc_wr_sel ? (w1cc_int & ~ wdata[31:0]) : w1cc_int) | w1cc;
    end
end

    reg [31:0] w1cc_int;
assign w1cc_out_reg = w1cc_int;

wire w1cc_wr_sel;
always @(posedge pclk or negedge presetn) begin
    if (!presetn) begin 
        w1cc_int <= 0;
    end else begin
        w1cc_int <= (w1cc_wr_sel ? (w1cc_int & ~ wdata[31:0]) : w1cc_int) | w1cc;
    end
end


wire [16-1:0] mpaddr0 =  16'hfffc & (paddr - 'h0);
wire [16-1:0] mpaddr = (pread||pwrite) ? mpaddr0  : 0;
assign prdata_wire =

    (mpaddr == 'h10000) ? ronly[31:0] :
    (mpaddr == 'h10004) ? {16'b0,ronly2} :
    (mpaddr == 'h10008) ? {16'b0,wonly} :
    (mpaddr == 'h1000c) ? {31'b0,one} :
    (mpaddr == 'h10010) ? rega[31:0] :
    (mpaddr == 'h10014) ? control0[31:0] :
    (mpaddr == 'h10018) ? {8'b0,statusa} :
    (mpaddr == 'h1001c) ? {8'b0,regb} :
    (mpaddr == 'h10020) ? w1cc_int[31:0] :
    (mpaddr == 'h10024) ? {31'b0,badfwr} :
    (mpaddr == 'h10028) ? {31'b0,badfro} :
    (mpaddr == 'h20000) ? rega[31:0] :
    (mpaddr == 'h20004) ? control0[31:0] :
    (mpaddr == 'h20008) ? {8'b0,statusa} :
    (mpaddr == 'h2000c) ? {8'b0,regb} :
    (mpaddr == 'h20010) ? extern[31:0] :
    (mpaddr == 'h20100) ? eth0tmp0[31:0] :
    (mpaddr == 'h20104) ? {8'b0,eth0tmp1} :
    (mpaddr == 'h20108) ? {16'b0,eth0tmp2} :
    (mpaddr == 'h20200) ? eth1tmp0[31:0] :
    (mpaddr == 'h20204) ? {8'b0,eth1tmp1} :
    (mpaddr == 'h20208) ? {16'b0,eth1tmp2} :
    (mpaddr == 'h20300) ? eth2tmp0[31:0] :
    (mpaddr == 'h20304) ? {8'b0,eth2tmp1} :
    (mpaddr == 'h20308) ? {16'b0,eth2tmp2} :
    (mpaddr == 'h20400) ? eth3tmp0[31:0] :
    (mpaddr == 'h20404) ? {8'b0,eth3tmp1} :
    (mpaddr == 'h20408) ? {16'b0,eth3tmp2} :
    (mpaddr == 'h2040c) ? wider[31:0] :
    (mpaddr == 'h20410) ? wider[63:32] :
    (mpaddr == 'h20414) ? wider[95:64] :
    (mpaddr == 'h20418) ? wider[127:96] :
    (mpaddr == 'h2041c) ? longer[31:0] :
    (mpaddr == 'h20420) ? longer[63:32] :
    (mpaddr == 'h20424) ? longer[95:64] :
    (mpaddr == 'h20428) ? longer[127:96] :
    (mpaddr == 'h2042c) ? ronly[31:0] :
    (mpaddr == 'h20430) ? {16'b0,ronly2} :
    (mpaddr == 'h30000) ? ronly[31:0] :
    (mpaddr == 'h30004) ? {16'b0,ronly2} :
    (mpaddr == 'h30008) ? {16'b0,wonly} :
    (mpaddr == 'h3000c) ? {31'b0,one} :
    (mpaddr == 'h30010) ? rega[31:0] :
    (mpaddr == 'h30014) ? control0[31:0] :
    (mpaddr == 'h30018) ? {8'b0,statusa} :
    (mpaddr == 'h3001c) ? {8'b0,regb} :
    (mpaddr == 'h30020) ? w1cc_int[31:0] :
    (mpaddr == 'h30024) ? {31'b0,badfwr} :
    (mpaddr == 'h30028) ? {31'b0,badfro} :
    32'hdeadbeaf;
wire ramx_rd_data_valid;


reg [32-1:0] prdata_reg;
always @(posedge pclk) prdata_reg <=  prdata_wire;
assign prdata =       ramx_rd_data_valid ? ramx_rdata :

    prdata_reg;

wire [32-1:0] mask = { {{8{pstrb[3]}},{8{pstrb[2]}},{8{pstrb[1]}},{8{pstrb[0]}}} };
always @(posedge pclk) if (pwrite) last_wdata <= wdata & mask;
always @(posedge pclk or negedge presetn) begin
    if (!presetn) begin 
        wonly <= 16'h0;
        one <= 1'h1;
        rega <= 32'h123456;
        control0 <= 32'hcc00;
        regb <= 24'h0;
        badfwr <= 1'h0;
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
        wonly <= 16'h0;
        one <= 1'h1;
        rega <= 32'h123456;
        control0 <= 32'hcc00;
        regb <= 24'h0;
        badfwr <= 1'h0;
    end else if (pwrite)  begin
        if (mpaddr == 'h10008) wonly <= (wonly & ~mask[15:0]) | (wdata[15:0] & mask[15:0]);
        if (mpaddr == 'h1000c) one <= (one & ~mask[0:0]) | (wdata[0:0] & mask[0:0]);
        if (mpaddr == 'h10010) rega <= (rega & ~mask) | (wdata & mask);
        if (mpaddr == 'h10014) control0 <= (control0 & ~mask) | (wdata & mask);
        if (mpaddr == 'h1001c) regb <= 24'h7ff03 & ((regb & ~mask[23:0]) | (wdata[23:0] & mask[23:0]));
        if (mpaddr == 'h10024) badfwr <= (badfwr & ~mask[0:0]) | (wdata[0:0] & mask[0:0]);
        if (mpaddr == 'h20000) rega <= (rega & ~mask) | (wdata & mask);
        if (mpaddr == 'h20004) control0 <= (control0 & ~mask) | (wdata & mask);
        if (mpaddr == 'h2000c) regb <= 24'h607ff & ((regb & ~mask[23:0]) | (wdata[23:0] & mask[23:0]));
        if (mpaddr == 'h20100) eth0tmp0 <= (eth0tmp0 & ~mask) | (wdata & mask);
        if (mpaddr == 'h20104) eth0tmp1 <= (eth0tmp1 & ~mask[23:0]) | (wdata[23:0] & mask[23:0]);
        if (mpaddr == 'h20108) eth0tmp2 <= (eth0tmp2 & ~mask[15:0]) | (wdata[15:0] & mask[15:0]);
        if (mpaddr == 'h20200) eth1tmp0 <= (eth1tmp0 & ~mask) | (wdata & mask);
        if (mpaddr == 'h20204) eth1tmp1 <= (eth1tmp1 & ~mask[23:0]) | (wdata[23:0] & mask[23:0]);
        if (mpaddr == 'h20208) eth1tmp2 <= (eth1tmp2 & ~mask[15:0]) | (wdata[15:0] & mask[15:0]);
        if (mpaddr == 'h20300) eth2tmp0 <= (eth2tmp0 & ~mask) | (wdata & mask);
        if (mpaddr == 'h20304) eth2tmp1 <= (eth2tmp1 & ~mask[23:0]) | (wdata[23:0] & mask[23:0]);
        if (mpaddr == 'h20308) eth2tmp2 <= (eth2tmp2 & ~mask[15:0]) | (wdata[15:0] & mask[15:0]);
        if (mpaddr == 'h20400) eth3tmp0 <= (eth3tmp0 & ~mask) | (wdata & mask);
        if (mpaddr == 'h20404) eth3tmp1 <= (eth3tmp1 & ~mask[23:0]) | (wdata[23:0] & mask[23:0]);
        if (mpaddr == 'h20408) eth3tmp2 <= (eth3tmp2 & ~mask[15:0]) | (wdata[15:0] & mask[15:0]);
        if (mpaddr == 'h2040c) wider[31:0] <= (wider[31:0] & ~mask) | (wdata & mask);
        if (mpaddr == 'h20410) wider[63:32] <= (wider[63:32] & ~mask) | (wdata & mask);
        if (mpaddr == 'h20414) wider[95:64] <= (wider[95:64] & ~mask) | (wdata & mask);
        if (mpaddr == 'h20418) wider[127:96] <= (wider[127:96] & ~mask) | (wdata & mask);
        if (mpaddr == 'h30008) wonly <= (wonly & ~mask[15:0]) | (wdata[15:0] & mask[15:0]);
        if (mpaddr == 'h3000c) one <= (one & ~mask[0:0]) | (wdata[0:0] & mask[0:0]);
        if (mpaddr == 'h30010) rega <= (rega & ~mask) | (wdata & mask);
        if (mpaddr == 'h30014) control0 <= (control0 & ~mask) | (wdata & mask);
        if (mpaddr == 'h3001c) regb <= 24'h7ff03 & ((regb & ~mask[23:0]) | (wdata[23:0] & mask[23:0]));
        if (mpaddr == 'h30024) badfwr <= (badfwr & ~mask[0:0]) | (wdata[0:0] & mask[0:0]);
    end
end

wire ronly_rd_sel = pread && (mpaddr=='h10000);
reg ronly_rd_pulse_reg; always @(posedge pclk)  ronly_rd_pulse_reg <= ronly_rd_sel;
assign ronly_pulse = ronly_rd_pulse_reg && penable;


wire ronly2_rd_sel = pread && (mpaddr=='h10004);
reg ronly2_rd_pulse_reg; always @(posedge pclk)  ronly2_rd_pulse_reg <= ronly2_rd_sel;
assign ronly2_pulse = ronly2_rd_pulse_reg && penable;


wire wonly_wr_sel = pwrite && (mpaddr=='h10008);
reg wonly_wr_pulse_reg; always @(posedge pclk)  wonly_wr_pulse_reg <= wonly_wr_sel;
assign wonly_pulse = wonly_wr_pulse_reg;


wire regb_wr_sel = pwrite && (mpaddr=='h1001c);
reg regb_wr_pulse_reg; always @(posedge pclk)  regb_wr_pulse_reg <= regb_wr_sel;
assign regb_pulse = regb_wr_pulse_reg;


assign w1cc_wr_sel = pwrite && (mpaddr=='h10020);

wire [2:0] ExtraBytesramx  =  pstrb[0] ? 0 : pstrb[1] ? 1 : pstrb[2] ? 2 : pstrb[3] ? 3 : 0;
assign ramx_addr = ((mpaddr - 'h10100)>>2);
assign ramx_wdata = wdata[16:0];

assign ramx_rd_pulse = pread && (mpaddr>='h10100) && (mpaddr < 'h10500);
reg ramx_rd_pulse_dly; always @(posedge pclk)  ramx_rd_pulse_dly <= ramx_rd_pulse;
assign ramx_rd_data_valid = ramx_rd_pulse_dly;


assign ramx_wr_pulse = pwrite && (mpaddr>='h10100) && (mpaddr < 'h10500);


wire regb_wr_sel = pwrite && (mpaddr=='h2000c);
reg regb_wr_pulse_reg; always @(posedge pclk)  regb_wr_pulse_reg <= regb_wr_sel;
assign regb_pulse = regb_wr_pulse_reg;


wire extern_rd_sel = pread && (mpaddr=='h20010);
reg extern_rd_pulse_reg; always @(posedge pclk)  extern_rd_pulse_reg <= extern_rd_sel;
assign extern_rd_pulse = extern_rd_pulse_reg && penable;


wire extern_wr_sel = pwrite && (mpaddr=='h20010);
reg extern_wr_pulse_reg; always @(posedge pclk)  extern_wr_pulse_reg <= extern_wr_sel;
assign extern_wr_pulse = extern_wr_pulse_reg;


wire ronly_rd_sel = pread && (mpaddr=='h2042c);
reg ronly_rd_pulse_reg; always @(posedge pclk)  ronly_rd_pulse_reg <= ronly_rd_sel;
assign ronly_pulse = ronly_rd_pulse_reg && penable;


wire ronly2_rd_sel = pread && (mpaddr=='h20430);
reg ronly2_rd_pulse_reg; always @(posedge pclk)  ronly2_rd_pulse_reg <= ronly2_rd_sel;
assign ronly2_pulse = ronly2_rd_pulse_reg && penable;

wire [2:0] ExtraBytesldst_ram  =  pstrb[0] ? 0 : pstrb[1] ? 1 : pstrb[2] ? 2 : pstrb[3] ? 3 : 0;
assign ldst_ram_addr = ((mpaddr - 'h20800)>>2);
assign ldst_ram_wdata = wdata;

assign ldst_ram_rd_pulse = pread && (mpaddr>='h20800) && (mpaddr < 'h20a00);
reg ldst_ram_rd_pulse_dly; always @(posedge pclk)  ldst_ram_rd_pulse_dly <= ldst_ram_rd_pulse;
assign ldst_ram_rd_data_valid = ldst_ram_rd_pulse_dly;


assign ldst_ram_wr_pulse = pwrite && (mpaddr>='h20800) && (mpaddr < 'h20a00);


wire ronly_rd_sel = pread && (mpaddr=='h30000);
reg ronly_rd_pulse_reg; always @(posedge pclk)  ronly_rd_pulse_reg <= ronly_rd_sel;
assign ronly_pulse = ronly_rd_pulse_reg && penable;


wire ronly2_rd_sel = pread && (mpaddr=='h30004);
reg ronly2_rd_pulse_reg; always @(posedge pclk)  ronly2_rd_pulse_reg <= ronly2_rd_sel;
assign ronly2_pulse = ronly2_rd_pulse_reg && penable;


wire wonly_wr_sel = pwrite && (mpaddr=='h30008);
reg wonly_wr_pulse_reg; always @(posedge pclk)  wonly_wr_pulse_reg <= wonly_wr_sel;
assign wonly_pulse = wonly_wr_pulse_reg;


wire regb_wr_sel = pwrite && (mpaddr=='h3001c);
reg regb_wr_pulse_reg; always @(posedge pclk)  regb_wr_pulse_reg <= regb_wr_sel;
assign regb_pulse = regb_wr_pulse_reg;


assign w1cc_wr_sel = pwrite && (mpaddr=='h30020);

wire [2:0] ExtraBytesramx  =  pstrb[0] ? 0 : pstrb[1] ? 1 : pstrb[2] ? 2 : pstrb[3] ? 3 : 0;
assign ramx_addr = ((mpaddr - 'h30100)>>2);
assign ramx_wdata = wdata[16:0];

assign ramx_rd_pulse = pread && (mpaddr>='h30100) && (mpaddr < 'h30500);
reg ramx_rd_pulse_dly; always @(posedge pclk)  ramx_rd_pulse_dly <= ramx_rd_pulse;
assign ramx_rd_data_valid = ramx_rd_pulse_dly;


assign ramx_wr_pulse = pwrite && (mpaddr>='h30100) && (mpaddr < 'h30500);

endmodule
