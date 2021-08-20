module tb;
reg [31:0] cycles;   initial cycles=0;
reg [31:0] errors;   initial errors=0;
reg [31:0] wrongs;   initial wrongs=0;
reg [31:0] corrects; initial corrects=0;
reg [31:0] marker;   initial marker=0;
reg [31:0] marker2;   initial marker2=0;

reg [255:0] rxstate,txstate;
initial rxstate=0;
initial txstate=0;



reg [15:0] baudrate0,baudrate1;
reg  clk;
reg [7:0] control;
reg  rst_n;
wire  rxd;
wire  txd;

reg  read_rx0;
wire  rx_valid0;
wire [7:0] rxdata0;
wire  tx_empty0;
reg [7:0] txdata0;
reg  write_tx0;

reg  read_rx1;
wire  rx_valid1;
wire [7:0] rxdata1;
wire  tx_empty1;
reg [7:0] txdata1;
reg  write_tx1;

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
    baudrate0[15:0] = 0;
    baudrate1[15:0] = 0;
    control[7:0] = 8'h50;
    rst_n = 0;
    read_rx0 = 0;
    read_rx1 = 0;
    txdata0[7:0] = 0;
    write_tx0 = 0;
    #100;
    rst_n=1;
end
uartx2 uart0 (
     .baudrate(baudrate0[15:0])
    ,.clk(clk)
    ,.control(control[7:0])
    ,.rst_n(rst_n)
    ,.rxd(rxd)
    ,.txd(txd)

    ,.read_rx(read_rx0)
    ,.rx_valid(rx_valid0)
    ,.rxdata(rxdata0[7:0])
    ,.status()
    ,.tx_empty(tx_empty0)
    ,.txdata(txdata0[7:0])
    ,.write_tx(write_tx0)
);
wire txd_mod;
uartx2_modified uart_mod (
     .baudrate(baudrate0[15:0])
    ,.clk(clk)
    ,.control(control[7:0])
    ,.rst_n(rst_n)
    ,.rxd(rxd)
    ,.txd(txd)

    ,.read_rx(read_rx0)
    ,.rx_valid(rx_valid0)
    ,.rxdata(rxdata0[7:0])
    ,.status()
    ,.tx_empty(tx_empty0)
    ,.txdata(txdata0[7:0])
    ,.write_tx(write_tx0)
);

uartx2 uart1 (
     .baudrate(baudrate1[15:0])
    ,.clk(clk)
    ,.control(control[7:0])
    ,.rst_n(rst_n)
    ,.rxd(txd) ,.txd(rxd)

    ,.read_rx(read_rx1)
    ,.rx_valid(rx_valid1)
    ,.rxdata(rxdata1[7:0])
    ,.status()
    ,.tx_empty(tx_empty1)
    ,.txdata(txdata1[7:0])
    ,.write_tx(write_tx1)
);


endmodule
