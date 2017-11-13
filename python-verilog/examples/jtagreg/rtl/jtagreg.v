



module jtagreg(
    input jtck
    ,input jtdi
    ,input jtms
    ,output jtdo
    ,input rst_n
);

wire [15:0] mem_addr;
wire [31:0] mem_rd_data;
wire  mem_read;
wire  mem_ready = 1;
wire [31:0] mem_wr_data;
wire [1:0] mem_wr_width;
wire  mem_write;

jtag_control jtag_control (
     .jtck_clock(jtck)
    ,.jtdi_out(jtdi)
    ,.jtdo_in(jtdo)
    ,.jtms_out(jtms)
    ,.mem_addr(mem_addr[15:0])
    ,.mem_rd_data(mem_rd_data[31:0])
    ,.mem_read(mem_read)
    ,.mem_ready(mem_ready)
    ,.mem_wr_data(mem_wr_data[31:0])
    ,.mem_wr_width(mem_wr_width[1:0])
    ,.mem_write(mem_write)
    ,.rst_n(rst_n)
);



wire [15:0] config0;
wire [23:0] config1;
wire [7:0] config2;
wire [31:0] control_stream1;
wire [31:0] control_stream2;
wire [31:0] enables;
wire [31:0] input_select;
wire  lens_invariant0;
wire  lens_invariant1;
wire [2:0] num_octaves0;
wire [2:0] num_octaves1;
wire [5:0] pattern_scale0;
wire [5:0] pattern_scale1;
wire [9:0] port0;
wire [9:0] port1;

wire [31:0] prdata;
wire  psel = mem_read||mem_write;
wire [1:0] psize = mem_wr_width;
wire [31:0] pwdata = mem_wr_data;
wire  pwrite = mem_write;
wire [6:0] paddr = mem_addr;
assign mem_rd_data = prdata;

regfile regfile (
     .clk(jtck) ,.rst_n(rst_n)

    ,.prdata(prdata[31:0])
    ,.psel(psel)
    ,.psize(psize[1:0])
    ,.pwdata(pwdata[31:0])
    ,.pwrite(pwrite)

    ,.config0(config0[15:0])
    ,.config1(config1[23:0])
    ,.config2(config2[7:0])
    ,.control_stream1(control_stream1[31:0])
    ,.control_stream2(control_stream2[31:0])
    ,.enables(enables[31:0])
    ,.input_select(input_select[31:0])
    ,.lens_invariant0(lens_invariant0)
    ,.lens_invariant1(lens_invariant1)
    ,.num_octaves0(num_octaves0[2:0])
    ,.num_octaves1(num_octaves1[2:0])
    ,.paddr(paddr[6:0])
    ,.pattern_scale0(pattern_scale0[5:0])
    ,.pattern_scale1(pattern_scale1[5:0])
    ,.port0(port0[9:0])
    ,.port1(port1[9:0])
);

endmodule



