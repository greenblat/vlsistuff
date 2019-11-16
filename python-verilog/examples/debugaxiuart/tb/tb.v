module tb;
reg [31:0] cycles;   initial cycles=0;
reg [31:0] errors;   initial errors=0;
reg [31:0] wrongs;   initial wrongs=0;
reg [31:0] panics;   initial panics=0;
reg [31:0] corrects; initial corrects=0;
reg [31:0] marker;   initial marker=0;
wire [31:0] araddr;
wire [1:0] arburst;
wire [3:0] arid;
wire [7:0] arlen;
reg  arready;
wire [2:0] arsize;
wire  arvalid;
wire [31:0] awaddr;
wire [1:0] awburst;
wire [3:0] awid;
wire [7:0] awlen;
reg  awready;
wire [2:0] awsize;
wire  awvalid;
reg [3:0] bid;
wire  bready;
reg [1:0] bresp;
reg  bvalid;
reg  clk;
reg [31:0] rdata;
reg [3:0] rid;
reg  rlast;
wire  rready;
reg [1:0] rresp;
reg  rst_n;
reg  rvalid;
reg  rxd;
wire  txd;
wire [31:0] wdata;
wire  wlast;
reg  wready;
wire [3:0] wstrb;
wire  wvalid;

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
    arready = 0;
    awready = 0;
    bid = 0;
    bresp = 0;
    bvalid = 0;
    clk = 0;
    rdata = 0;
    rid = 0;
    rlast = 0;
    rresp = 0;
    rst_n = 0;
    rvalid = 0;
    rxd = 0;
    wready = 0;
    #100;
    rst_n=1;
end
debugaxiuart dut (
     .araddr(araddr[31:0])
    ,.arburst(arburst[1:0])
    ,.arid(arid[3:0])
    ,.arlen(arlen[7:0])
    ,.arready(arready)
    ,.arsize(arsize[2:0])
    ,.arvalid(arvalid)
    ,.awaddr(awaddr[31:0])
    ,.awburst(awburst[1:0])
    ,.awid(awid[3:0])
    ,.awlen(awlen[7:0])
    ,.awready(awready)
    ,.awsize(awsize[2:0])
    ,.awvalid(awvalid)
    ,.bid(bid[3:0])
    ,.bready(bready)
    ,.bresp(bresp[1:0])
    ,.bvalid(bvalid)
    ,.clk(clk)
    ,.rdata(rdata[31:0])
    ,.rid(rid[3:0])
    ,.rlast(rlast)
    ,.rready(rready)
    ,.rresp(rresp[1:0])
    ,.rst_n(rst_n)
    ,.rvalid(rvalid)
    ,.rxd(rxd)
    ,.txd(txd)
    ,.wdata(wdata[31:0])
    ,.wlast(wlast)
    ,.wready(wready)
    ,.wstrb(wstrb[3:0])
    ,.wvalid(wvalid)
);

reg [1023:0] testname;
initial begin
    if ($value$plusargs("SEQ=%s",testname)) begin 
         $display(" Running SEQ= %s.",testname); 
    end else begin
        testname = 0;
        $display(" default test");
    end 
    #10;
    if (testname!=0) $python("sequence()",testname);
end 
endmodule
