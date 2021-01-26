module nc100_rgf_ram (
    input clk,input rst_n,input pwrite, input pread
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
    32'hdeadbeaf;
wire ldst_ram_rd_data_valid;


reg [32-1:0] prdata_reg;
always @(posedge clk) prdata_reg <=  prdata_wire;
assign prdata =       ldst_ram_rd_data_valid ? ldst_ram_rdata :

    prdata_reg;

wire [32-1:0] mask = { {{8{pstrb[3]}},{8{pstrb[2]}},{8{pstrb[1]}},{8{pstrb[0]}}} };
wire [32-1:0] wdata = pwdata;
always @(posedge clk) if (pwrite) last_wdata <= wdata & mask;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin 
        rega <= 32'h123456;
        control0 <= 32'hcc00;
        regb <= 24'h0;
    end else if (pwrite)  begin
        if (mpaddr == 'h0) rega <= (rega & ~mask) | (wdata & mask);
        if (mpaddr == 'h4) control0 <= (control0 & ~mask) | (wdata & mask);
        if (mpaddr == 'hc) regb <= (regb & ~mask) | (wdata & mask);
    end
end

wire regb_wr_sel = pwrite && (mpaddr=='hc);
reg regb_wr_pulse_reg; always @(posedge clk)  regb_wr_pulse_reg <= regb_wr_sel;
assign regb_pulse = regb_wr_pulse_reg;


wire extern_rd_sel = pread && (mpaddr=='h10);
reg extern_rd_pulse_reg; always @(posedge clk)  extern_rd_pulse_reg <= extern_rd_sel;
assign extern_rd_pulse = extern_rd_pulse_reg;


wire extern_wr_sel = pwrite && (mpaddr=='h10);
reg extern_wr_pulse_reg; always @(posedge clk)  extern_wr_pulse_reg <= extern_wr_sel;
assign extern_wr_pulse = extern_wr_pulse_reg;

wire [2:0] ExtraBytesldst_ram  =  pstrb[0] ? 0 : pstrb[1] ? 1 : pstrb[2] ? 2 : pstrb[3] ? 3 : 0;
assign ldst_ram_addr = ((mpaddr - 'h800)>>2);
assign ldst_ram_wdata = wdata;

assign ldst_ram_rd_pulse = pread && (mpaddr>='h800) && (mpaddr < 'ha00);
reg ldst_ram_rd_pulse_dly; always @(posedge clk)  ldst_ram_rd_pulse_dly <= ldst_ram_rd_pulse;
assign ldst_ram_rd_data_valid = ldst_ram_rd_pulse_dly;


assign ldst_ram_wr_pulse = pwrite && (mpaddr>='h800) && (mpaddr < 'ha00);

endmodule

module nc100_rgf (input clk, input rst_n,
    input psel, input penable, input pwrite, input [4-1:0] pstrb, input [16-1:0] paddr, input [32-1:0] pwdata, output [32-1:0] prdata
    ,output pready, output pslverr
    ,output [31:0] rega
    ,output [31:0] control0
    ,output regb_pulse
    ,input [31:0] extern
    ,output extern_rd_pulse
    ,output extern_wr_pulse
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
);

wire i_pread = psel && !pwrite;
wire i_pwrite = psel && pwrite && penable;
assign pslverr = 0;
    wire [23:0] statusa;
    wire [23:0] regb;

nc100_rgf_ram rgf (.clk(clk),.rst_n(rst_n),.pwrite(i_pwrite),.pread(i_pread),.paddr(paddr)
    ,.pwdata(pwdata),.prdata(prdata)
    ,.pstrb(pstrb)
    ,.rega(rega)
    ,.control0(control0)
    ,.statusa(statusa)
    ,.regb(regb)
    ,.regb_pulse(regb_pulse)
    ,.extern(extern)
    ,.extern_rd_pulse(extern_rd_pulse)
    ,.extern_wr_pulse(extern_wr_pulse)
    ,.ldst_ram_rdata(ldst_ram_rdata)
    ,.ldst_ram_wdata(ldst_ram_wdata)
    ,.ldst_ram_addr(ldst_ram_addr)
    ,.ldst_ram_rd_pulse(ldst_ram_rd_pulse)
    ,.ldst_ram_wr_pulse(ldst_ram_wr_pulse)
);
assign statusa = { spi0 ,cpu1 ,dma0 };
assign { ospi ,ocpu ,odma } = regb;
endmodule
