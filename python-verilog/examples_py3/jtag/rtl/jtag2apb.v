module jtag2apb(
    input jtck
    ,input jtdi
    ,input jtms
    ,output jtdo
    ,input rst_n
    ,input por_n
    ,input clk

    ,output psel
    ,output penable
    ,output reg pwrite
    ,output reg [31:0] pwdata
    ,output reg [15:0] paddr
    ,input [31:0] prdata
    ,input pready

    ,output [31:0] control
    ,input  [29:0] status
);

wire [15:0] ram_addr;
reg [31:0] ram_rd_data;
wire  ram_read;
wire  ram_ready;
wire [31:0] ram_wr_data;
wire  ram_write;
wire [7:0] version = 8'h57;

wire status1=1,status0=0;
wire [31:0] internal_status = { status1,status0,status};
jtag_tap jtag_tap (
     .jtck_clock(jtck)
    ,.jtdi_out(jtdi)
    ,.jtdo_in(jtdo)
    ,.jtms_out(jtms)
    ,.ram_addr(ram_addr[15:0])
    ,.ram_rd_data(ram_rd_data[31:0])
    ,.ram_read(ram_read)
    ,.ram_ready(ram_ready)
    ,.ram_wr_data(ram_wr_data[31:0])
    ,.ram_write(ram_write)
    ,.version(version)
    ,.por_n(por_n)
    ,.control(control)
    ,.status(internal_status)
);

wire ram_read_sync,ram_write_sync;
level_synchronizer level_synchronizer_1 (.clk(clk),.din(ram_read),.rst_n(rst_n),.dout(ram_read_sync));
level_synchronizer level_synchronizer_2 (.clk(clk),.din(ram_write),.rst_n(rst_n),.dout(ram_write_sync));

reg was;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        was<=1'b0;
    end else begin
        was <= ram_read_sync||ram_write_sync;
    end
end
wire pulse = !was && (ram_read_sync||ram_write_sync);

reg [1:0] state;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        state <= 0;
        pwrite <= 0;
    end else begin
        if (state==0) begin
            if (pulse) begin
                state <= 1;
                pwrite <= ram_write_sync;
            end
        end else if (state==1) begin
            if (pready)  begin
                state <= 0;
                pwrite <= 0;
            end
        end
    end
end



assign psel    = pulse || (state==1) ;
always @(posedge clk) if (pulse) paddr <= ram_addr;
always @(posedge clk)  if (pulse) pwdata <= ram_wr_data;
assign penable = state == 1;
assign ram_ready = 1;
always @(posedge clk) if (!pwrite && (state == 1)) ram_rd_data <= prdata;


endmodule



