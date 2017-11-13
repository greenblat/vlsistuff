module tb;
reg [31:0] cycles;   initial cycles=0;
reg [31:0] errors;   initial errors=0;
reg [31:0] wrongs;   initial wrongs=0;
reg [31:0] corrects; initial corrects=0;
reg [31:0] marker;   initial marker=0;
reg [31:0] marker2;   initial marker2=0;
reg [7:0] rxstate,txstate; initial rxstate=0; initial txstate=0;
reg  clk;
wire [13:0] ram_addr;
reg [31:0] ram_rdata;
wire  ram_read;
wire [31:0] ram_wdata;
wire  ram_write;
reg  rst_n;
wire  rxd;
wire  txd;

always begin
    clk=0;
    #10;
    clk=1;
    #3;
    $python("negedge()");
    #7;
end
initial begin
    $dumpvars(0,tb);
    clk = 0;
    ram_rdata[31:0] = 0;
    rst_n = 0;
    #100;
    rst_n=1;
end
dbguart dbguart (
     .clk(clk)
    ,.ram_addr(ram_addr[13:0])
    ,.ram_rdata(ram_rdata[31:0])
    ,.ram_read(ram_read)
    ,.ram_wdata(ram_wdata[31:0])
    ,.ram_write(ram_write)
    ,.rst_n(rst_n)
    ,.rxd(rxd)
    ,.txd(txd)
);

reg [15:0] baudrate; initial baudrate=16'h100;
wire [7:0] control  = 8'h50;
wire [7:0] rxdata0;
reg [7:0] txdata0;
reg write_tx0;
py_uartx2 uartmodel (
     .baudrate(baudrate[15:0])
    ,.clk(clk)
    ,.control(control[7:0])
    ,.rst_n(rst_n)
    ,.rxd(txd)
    ,.txd(rxd)

    ,.read_rx(rx_valid0)
    ,.rx_valid(rx_valid0)
    ,.rxdata(rxdata0[7:0])
    ,.status()
    ,.tx_empty(tx_empty0)
    ,.txdata(txdata0[7:0])
    ,.write_tx(write_tx0)
);





endmodule
