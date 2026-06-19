`timescale 1ns / 1ps
module cpu_compound ( input clk, input rst_n

    ,input [31:0] irq
    ,output reg [31:0] eoi

    ,output reg [31:0]  m_paddr
    ,output reg [31:0]  m_pwdata
    ,output reg         m_psel
    ,output reg         m_penable
    ,output reg         m_pwrite
    ,output reg [3:0]   m_pstrb
    ,input        m_pready
    ,input        m_pslverr
    ,input [31:0] m_prdata

    ,output finish_good
    ,output finish_bad
    ,output external_access

);


wire  ready;

wire [31:0] rdata;
wire [31:0] mem_addr;
wire  mem_ready = (!m_psel || m_pready);
wire [31:0] mem_wdata;
wire mem_wr,mem_rd,mem_fetch;

localparam LOCAL_LIMIT = 32'h10000;

wire [31:0] mem_rdata = m_psel ? m_prdata : rdata ;



reg [31:0] irq_sticky;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        irq_sticky <= 0;
    end else begin
        irq_sticky <= (irq_sticky | irq) & ~eoi;
    end
end





wire mem_valid = mem_rd || mem_wr;
wire panic0 = mem_valid && external_access && mem_fetch;

reg [2:0] ext_state;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        m_psel <= 0;
        m_pwrite <= 0;
        m_pstrb <= 0;
        m_paddr <= 0;
        m_pwdata <= 0;
        m_penable <= 0;
        ext_state <= 0;
    end else begin
        if (ext_state == 1) begin
            m_penable <= 1;
            ext_state <= 2;
        end else if ((ext_state == 4) || (ext_state == 2)) begin
            m_penable <= 0;
            ext_state <= 0;
            m_psel <= 0;
            m_pwrite <= 0;
            m_pstrb <= 0;
            m_paddr <= 0;
            m_pwdata <= 0;
        end else if (ext_state == 3) begin
            m_penable <= 1;
            ext_state <= 4;
        end else if (mem_valid && !mem_fetch && external_access) begin
            m_psel <= 1;
            m_pwrite <= mem_wr;
            m_paddr <= (mem_addr<32'h20000) ? (mem_addr - 32'h10000) : mem_addr;
            m_pwdata <= mem_wdata;
            m_penable <= 0;
            m_pstrb <= 4'hf;
            ext_state <=  mem_wr ? 1 :3;
        end
    end
end
reg [15:0] irq_addr; initial irq_addr = 0;
wire [15:0] PC;
wire stop_code;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        irq_addr <= 0;
    end else begin
        if (stop_code) irq_addr <= PC+4;
    end
end
wire [7:0] nop_result;
wire sleeping;
simpleCPU simpleCPU (
     .clk(clk)
    ,.irq(irq_sticky!=0)
    ,.irq_addr(irq_addr)
    ,.mem_addr(mem_addr[31:0])
    ,.mem_rd(mem_rd)
    ,.mem_fetch(mem_fetch)
    ,.mem_rdata(mem_rdata[31:0])
    ,.mem_ready(mem_ready)
    ,.mem_wdata(mem_wdata[31:0])
    ,.mem_wr(mem_wr)
    ,.rst_n(rst_n)
    ,.running(running)
    ,.stop_code(stop_code)
    ,.PC(PC)
    ,.nop_result(nop_result)
    ,.finish_good(finish_good)
    ,.finish_bad(finish_bad)
    ,.sleeping(sleeping)
    ,.external_access(external_access)
);




cpu_ram ram(  
     .clk(clk)
    ,.ram_wr(mem_wr && !external_access)
    ,.ram_rd(mem_rd)
    ,.ram_fetch(mem_fetch)
    ,.addr(mem_addr[15:0])
    ,.wdata(mem_wdata)
    ,.rdata(rdata)
    ,.ready()
);

always @(posedge clk) begin
    if (running && (irq_sticky!=0)) begin
        eoi <= irq_sticky;
    end else begin
        eoi <= 0;
    end
end
wire [63:0]  sign_version = 64'h00048f4f020326 ;
endmodule

