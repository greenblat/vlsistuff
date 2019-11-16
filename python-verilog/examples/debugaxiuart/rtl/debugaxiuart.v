
// this module is axi master controlled by commands coming from uart.
// uart character sequences can produce various transactions on AXI.


module debugaxiuart #(parameter BYTES=4, parameter WID=BYTES*8 (
    input clk ,input rst_n
    ,input rxd, output txd


// axi write addr channel
    ,output [3:0] awid           // addr write id
    ,output [31:0] awaddr
    ,output [7:0] awlen
    ,output [2:0] awsize
    ,output [1:0] awburst
    ,output awvalid
    ,input awready

// axi write data channel
    ,output [WID-1:0] wdata
    ,output [BYTES-1:0] wstrb
    ,output wlast
    ,output wvalid
    ,input wready

// axi write responce channel
    ,input [3:0] bid 
    ,input [1:0] bresp
    ,input bvalid
    ,output bready

// axi read addr channel
    ,output [3:0] arid
    ,output [31:0] araddr
    ,output [7:0] arlen
    ,output [2:0] arsize
    ,output [1:0] arburst
    ,output arvalid
    ,input arready
    
// axi read data channel
    ,input [3:0] rid 
    ,input [WID-1:0] rdata
    ,input [1:0] rresp
    ,input rlast
    ,input rvalid
    ,output rready



);



wire [31:0] local_wr_addr;
wire [WID-1:0] local_wr_data;
wire [BYTES-1:0] local_wstrb;
wire [31:0] status;
wire [6:0] rx_fifo_addr;
wire [8:0] tx_fifo_addr;

wire local_wr;
wire local_wr_last;
wire lcl_empty;
wire [WID+BYTES+4+2+1 -1:0] lcl_data;
wire lcl_read;
wire [15:0] lcl_count;
wire [15:0] uart_baudrate;

wire [15:0] tx_fifo_count;
wire [15:0] rx_fifo_count;
wire [31:0] local_rd_data;
wire [31:0] local_rd_addr;

wire [77:0] lcl_wdata;
wire [77:0] lcl_rdata;
wire [4:0] lcl_addr;

wire  [ 3:0] wr_wstrb;
wire [3:0] wdata_mode;

axi_master_32 axi_master (
     .clk(clk) ,.rst_n(rst_n) ,.softreset(softreset)

    ,.araddr(araddr) ,.arburst(arburst) ,.arid(arid) ,.arlen(arlen) ,.arready(arready)
    ,.arsize(arsize) ,.arvalid(arvalid)
    ,.awaddr(awaddr) ,.awburst(awburst) ,.awid(awid) ,.awlen(awlen) ,.awready(awready) ,.awsize(awsize) ,.awvalid(awvalid)
    ,.bid(bid) ,.bready(bready) ,.bresp(bresp) ,.bvalid(bvalid)
    ,.rdata(rdata) ,.rid(rid) ,.rlast(rlast) ,.rready(rready) ,.rresp(rresp) ,.rvalid(rvalid)
    ,.wdata(wdata) ,.wlast(wlast) ,.wready(wready) ,.wstrb(wstrb) ,.wvalid(wvalid)

    ,.local_rd(local_rd),.local_rd_data(local_rd_data),.wr_wstrb(wr_wstrb)
    ,.wdata_mode(wdata_mode)

);

wire [7:0] uart_control,uart_status;
wire [7:0] rxdata,txdata;
wire write_tx,tx_empty,rx_valid,read_rx;

uartx2 uartx2 (
   .clk(clk)
  ,.rst_n(rst_n)

  ,.txd(txd) ,.rxd(rxd)

  ,.control(uart_control[7:0])
  ,.status(uart_status[7:0])
  ,.baudrate(uart_baudrate[15:0])

  ,.write_tx(write_tx)
  ,.read_rx(!rx_fifo_full && rx_valid)
  ,.rxdata(rxdata[7:0])
  ,.txdata(txdata[7:0])
  ,.tx_empty(tx_empty)
  ,.rx_valid(rx_valid)
);

wire [15:0] rx_fifo_wdata,rx_ram_rdata;
wire [15:0] tx_fifo_wdata,tx_ram_rdata;
wire tx_fifo_wen,tx_fifo_cen,rx_fifo_wen,rx_fifo_cen;
wire [7:0] rx_fifo_data,tx_fifo_data;

syncramfifo #(8,256/2)   rx_fifo (
    .clk(clk),.rst_n(rst_n),.capacity(16'd256)
    ,.validin(rx_valid),.datain(rxdata),.full(rx_fifo_full)
    ,.readout(rx_fifo_read),.dataout(rx_fifo_data),.empty(rx_fifo_empty)
    ,.count(rx_fifo_count)
    ,.softreset(softreset)
    ,.wen(rx_fifo_wen) ,.cen(rx_fifo_cen) ,.addr(rx_fifo_addr) ,.wdata(rx_fifo_wdata) ,.rdata(rx_ram_rdata)
    ,.panic(rx_fifo_panic)
);  

syncramfifo #(8,1024/2)   tx_fifo (
    .clk(clk),.rst_n(rst_n),.capacity(16'd1024)
    ,.validin(tx_fifo_write),.datain(tx_fifo_data),.full(tx_fifo_full)
    ,.readout(tx_empty),.dataout(txdata),.empty(tx_fifo_empty)
    ,.count(tx_fifo_count)
    ,.softreset(softreset)
    ,.wen(tx_fifo_wen) ,.cen(tx_fifo_cen) ,.addr(tx_fifo_addr) ,.wdata(tx_fifo_wdata) ,.rdata(tx_ram_rdata)
    ,.panic(tx_fifo_panic)
);  

assign write_tx = !tx_fifo_empty && tx_empty;


syncramfifo #(32+4+2+1,64/2)   lcl_ram_fifo (
    .clk(clk),.rst_n(rst_n),.capacity(16'd64) ,.softreset(softreset)

    ,.validin(rvalid && rready),.datain({rlast,rresp,rid,rdata}),.full(lcl_full)
    ,.readout(lcl_read),.dataout(lcl_data),.empty(lcl_empty)
    ,.count(lcl_count)
    ,.wen(lcl_wen) ,.cen(lcl_cen) ,.addr(lcl_addr) ,.wdata(lcl_wdata) ,.rdata(lcl_rdata)
    ,.panic(lcl_panic)
);  

wire [63:0] lcl_rd_wdata,lcl_rd_rdata;
wire [4:0] lcl_rd_addr;
wire lcl_rd_wen,lcl_rd_cen;
wire [15:0] lcl_rd_count;
wire [31:0] push_wdata; wire push_wdata_pulse;
syncramfifo #(32,64/2)   lcl_rd_ram_fifo (
    .clk(clk),.rst_n(rst_n),.capacity(16'd64) ,.softreset(softreset)

    ,.validin(push_wdata_pulse),.datain(push_wdata),.full(lcl_rd_full)
    ,.readout(local_rd),.dataout(local_rd_data),.empty(lcl_rd_empty)
    ,.count(lcl_rd_count)
    ,.wen(lcl_rd_wen) ,.cen(lcl_rd_cen) ,.addr(lcl_rd_addr) ,.wdata(lcl_rd_wdata) ,.rdata(lcl_rd_rdata)
    ,.panic(lcl_rd_panic)
);  



ram_16_128 rx_fifo_ram (.clk(clk)
    ,.addr(rx_fifo_addr[6:0])
    ,.wen(rx_fifo_wen)
    ,.cen(rx_fifo_cen)
    ,.din(rx_fifo_wdata)
    ,.dout(rx_ram_rdata)
);
ram_16_512 tx_fifo_ram (.clk(clk)
    ,.addr(tx_fifo_addr)
    ,.wen(tx_fifo_wen)
    ,.cen(tx_fifo_cen)
    ,.din(tx_fifo_wdata)
    ,.dout(tx_ram_rdata)
);

ram_78_32 lcl_fifo_ram (.clk(clk)
    ,.addr(lcl_addr)
    ,.wen(lcl_wen)
    ,.cen(lcl_cen)
    ,.din(lcl_wdata)
    ,.dout(lcl_rdata)
);

ram_64_32 lcl_rd_fifo_ram (.clk(clk)
    ,.addr(lcl_rd_addr)
    ,.wen(lcl_rd_wen)
    ,.cen(lcl_rd_cen)
    ,.din(lcl_rd_wdata)
    ,.dout(lcl_rd_rdata)
);


wire        rgf_rsel;
wire        rgf_wr;
wire [31:0] rgf_wdata,rgf_rdata;
wire [7:0]  rgf_addr;


wire [5:0] bresp_bid_data;
wire [6:0] bresp_bid;
wire bresp_empty;
wire bresp_bid_pulse;

assign bresp_bid = {!bresp_empty,bresp_bid_data};

debugaxirgf debugaxirgf (
    .clk(clk),.rst_n(rst_n)
    ,.uart_control(uart_control)
    ,.uart_status(uart_status)
    ,.uart_baudrate(uart_baudrate)
    ,.rd_valid(),.rd_valid_pulse(arvalid)
    ,.wr_valid(),.wr_valid_pulse(awvalid)

    ,.rready(rready)
    ,.bready(bready)

    ,.rd_id(arid)
    ,.rd_size(arsize)
    ,.rd_addr(araddr)
    ,.rd_burst(arburst)
    ,.rd_len(arlen)

    ,.wr_id(awid)
    ,.wr_size(awsize)
    ,.wr_addr(awaddr)
    ,.wr_burst(awburst)
    ,.wr_len(awlen)
    ,.wr_wstrb(wr_wstrb)
    ,.wdata_mode(wdata_mode)


    ,.bresp_bid(bresp_bid)
    ,.bresp_bid_pulse()

    ,.push_wdata_pulse(push_wdata_pulse)
    ,.push_wdata(push_wdata)

    ,.rwrite(rgf_wr)
    ,.wrdata(rgf_wdata)
    ,.rdata(rgf_rdata)
    ,.addr(rgf_addr[6:0])
    ,.rsel(rgf_sel)
    ,.rsize(2'd2)
);

debugcontroller debugcontroller (
    .clk(clk),.rst_n(rst_n) ,.softreset(softreset)

    ,.tx_fifo_write(tx_fifo_write)
    ,.tx_fifo_data(tx_fifo_data)
    ,.tx_fifo_full(tx_fifo_full)

    ,.rx_fifo_read(rx_fifo_read)
    ,.rx_fifo_data(rx_fifo_data)
    ,.rx_fifo_empty(rx_fifo_empty)

    ,.lcl_empty(lcl_empty),.lcl_data(lcl_data), .lcl_read(lcl_read)
    ,.lcl_rd_full(lcl_rd_full)

    ,.bresp_bid(bresp_bid)
    ,.bresp_bid_pulse(bresp_bid_pulse)
    ,.bresp_empty(bresp_empty)

    ,.rgf_wr(rgf_wr)
    ,.rgf_wdata(rgf_wdata)
    ,.rgf_rdata(rgf_rdata)
    ,.rgf_addr(rgf_addr)
    ,.rgf_sel(rgf_sel)

    ,.arvalid(arvalid)
    ,.arready(arready)

    ,.awvalid(awvalid)
    ,.awready(awready)

);

syncfifo #(2+4,16) bresp_fifo (.clk(clk),.rst_n(rst_n),.softreset(1'b0)
    ,.validin(bvalid && bready),.datain({bresp,bid})
    ,.full(),.empty(bresp_empty),.overflow(),.count()
    ,.readout(bresp_bid_pulse),.dataout(bresp_bid_data)
);





endmodule

