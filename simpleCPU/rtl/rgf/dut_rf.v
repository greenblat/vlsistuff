
`timescale 1ns / 1ps
module dut_rf (input pclk, input presetn, input softreset
    ,input psel, input penable, input pwrite, input [4-1:0] pstrb, input [16-1:0] paddr, input [32-1:0] pwdata, output [32-1:0] prdata,output [32-1:0] prdata_wire
    ,output pready, output pslverr
    ,input [31:0] version
    ,output [95:0] reg0
    ,input [31:0] status
    ,output [31:0] counter_start
    ,output counter_start_pulse
    ,input [31:0] interrupts
    ,output [31:0] interrupts_out_reg
    ,output [4:0] set_interrupt
    ,output set_interrupt_pulse
);

wire i_pread = psel && !pwrite;
wire i_pwrite = psel && pwrite && penable;
assign pslverr = 0;
assign pready = 1;
wire [31:0] last_wdata;

wire [1023:0] ZEROES = 1024'b0;
dut_rf_ram rgf (.pclk(pclk),.presetn(presetn),.softreset(softreset),.pwrite(i_pwrite),.pread(i_pread),.paddr(paddr)
    ,.pwdata(pwdata),.prdata(prdata),.prdata_wire(prdata_wire)
    ,.pstrb(pstrb),.last_wdata(last_wdata)
    ,.penable(penable),.pready()
    ,.version(version)
    ,.reg0(reg0)
    ,.status(status)
    ,.counter_start(counter_start)
    ,.counter_start_pulse(counter_start_pulse)
    ,.interrupts(interrupts)
    ,.interrupts_out_reg(interrupts_out_reg)
    ,.set_interrupt(set_interrupt)
    ,.set_interrupt_pulse(set_interrupt_pulse)
);
endmodule
`timescale 1ns / 1ps
module dut_rf_ram (
    input pclk,input presetn, input softreset, input pwrite, input pread, input penable
    ,input [32-1:0] pwdata, output [32-1:0] prdata, output [32-1:0] prdata_wire
    ,input [4-1:0] pstrb
    ,input [16-1:0] paddr ,output reg [32-1:0] last_wdata
    ,output pready
    ,input [31:0] version
    ,output reg [95:0] reg0
    ,input [31:0] status
    ,output reg [31:0] counter_start
    ,output counter_start_pulse
    ,input [31:0] interrupts
    ,output [31:0] interrupts_out_reg
    ,output reg [4:0] set_interrupt
    ,output set_interrupt_pulse
);
wire [32-1:0] wdata = pwdata;
    reg [31:0] interrupts_int;
assign interrupts_out_reg = interrupts_int;

wire interrupts_wr_sel;
always @(posedge pclk or negedge presetn) begin
    if (!presetn) begin 
        interrupts_int <= 0;
    end else begin
        interrupts_int <= (interrupts_wr_sel ? (interrupts_int & ~ wdata[31:0]) : interrupts_int) | interrupts;
    end
end


wire [16-1:0] mpaddr0 =  16'hfffc & (paddr - 'h0);
wire [16-1:0] mpaddr = (pread||pwrite) ? mpaddr0  : 0;
assign prdata_wire =

    (mpaddr == 'h0) ? version[31:0] :
    (mpaddr == 'h4) ? reg0[31:0] :
    (mpaddr == 'h8) ? reg0[63:32] :
    (mpaddr == 'hc) ? reg0[95:64] :
    (mpaddr == 'h10) ? status[31:0] :
    (mpaddr == 'h14) ? counter_start[31:0] :
    (mpaddr == 'h18) ? interrupts_int[31:0] :
    (mpaddr == 'h1c) ? {27'b0,set_interrupt} :
    32'hdeadbeef;



reg [32-1:0] prdata_reg;
always @(posedge pclk) prdata_reg <=  prdata_wire;
assign pready = 1;

assign prdata =   
    prdata_reg;

wire [32-1:0] mask = { {{8{pstrb[3]}},{8{pstrb[2]}},{8{pstrb[1]}},{8{pstrb[0]}}} };
always @(posedge pclk) if (pwrite) last_wdata <= wdata & mask;
always @(posedge pclk or negedge presetn) begin
    if (!presetn) begin 
        reg0 <= 96'h0;
        counter_start <= 32'h0;
        set_interrupt <= 5'h0;
    end else if (softreset)  begin
        reg0 <= 96'h0;
        counter_start <= 32'h0;
        set_interrupt <= 5'h0;
    end else if (pwrite)  begin
        if (mpaddr == 'h4) reg0[31:0] <= (reg0[31:0] & ~mask[31:0]) | (wdata[31:0] & mask[31:0]);
        if (mpaddr == 'h8) reg0[63:32] <= (reg0[63:32] & ~mask[31:0]) | (wdata[31:0] & mask[31:0]);
        if (mpaddr == 'hc) reg0[95:64] <= (reg0[95:64] & ~mask[31:0]) | (wdata[31:0] & mask[31:0]);
        if (mpaddr == 'h14) counter_start <= (counter_start & ~mask) | (wdata & mask);
        if (mpaddr == 'h1c) set_interrupt <= (set_interrupt & ~mask[4:0]) | (wdata[4:0] & mask[4:0]);
    end
end

wire counter_start_wr_sel = pwrite && (mpaddr=='h14);
reg counter_start_wr_pulse_reg; always @(posedge pclk or negedge presetn)  if (!presetn) counter_start_wr_pulse_reg<=0; else counter_start_wr_pulse_reg <= counter_start_wr_sel;
assign counter_start_pulse = counter_start_wr_pulse_reg;


assign interrupts_wr_sel = pwrite && (mpaddr=='h18);


wire set_interrupt_wr_sel = pwrite && (mpaddr=='h1c);
reg set_interrupt_wr_pulse_reg; always @(posedge pclk or negedge presetn)  if (!presetn) set_interrupt_wr_pulse_reg<=0; else set_interrupt_wr_pulse_reg <= set_interrupt_wr_sel;
assign set_interrupt_pulse = set_interrupt_wr_pulse_reg;

endmodule
