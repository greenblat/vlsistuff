
module dut (input clk, input rst_n,input irq, output finish_good, output finish_bad);




wire [31:0] version = 32'h19062026;
wire [95:0] reg0;
wire [31:0] status;
wire [31:0] counter_start;
wire counter_start_pulse;
wire [4:0] set_interrupt;
wire set_interrupt_pulse;
wire counter_interrupt;
wire [31:0] interrupts =  set_interrupt_pulse ? (1 << set_interrupt) : {irq,counter_interrupt};
wire [31:0] interrupts_out_reg;

wire pwrite; 
wire [31:0] paddr;
wire psel;
wire penable;
wire [31:0] prdata,pwdata;
wire pready;

reg [31:0] counter;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        counter <= 0;
    end else begin
        if (counter>0) begin
            counter <= counter - 1;
        end else if (counter_start_pulse) begin
            counter <= counter_start;
        end
    end
end
assign counter_interrupt = counter==1;
assign status = counter;

dut_rf dut_rf (.pclk(clk),.presetn(rst_n)
    ,.pwrite(pwrite),.paddr(paddr[15:0]),.psel(psel),.penable(penable)
    ,.prdata(prdata),.prdata_wire(),.pwdata(pwdata),.pstrb(4'hf)
    ,.pready(pready),.pslverr()
    ,.softreset(1'b0)

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

wire external_access;
cpu_compound cpu_compound (
    .clk(clk) ,.rst_n(rst_n)
    ,.irq(interrupts_out_reg)

    ,.m_paddr(paddr[31:0])
    ,.m_penable(penable)
    ,.m_prdata(prdata[31:0])
    ,.m_pready(pready)
    ,.m_psel(psel)
    ,.m_pslverr(1'b0)
    ,.m_pstrb()
    ,.m_pwdata(pwdata[31:0])
    ,.m_pwrite(pwrite)

    ,.finish_good(finish_good)
    ,.finish_bad(finish_bad)
    ,.external_access(external_access)

);  







endmodule

