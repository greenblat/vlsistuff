module tb;
reg [31:0] iid; initial iid=1;
reg [31:0] cycles;   initial cycles=0;
reg [31:0] errors;   initial errors=0;
reg [31:0] wrongs;   initial wrongs=0;
reg [31:0] panics;   initial panics=0;
reg [31:0] corrects; initial corrects=0;
reg [31:0] marker;   initial marker=0;
reg  clk,clka;
reg [2:0] req_addr;
wire [7:0] req_count;
reg [63:0] req_data;
reg [0:0] req_write;
reg [2:0] resp_addr;
wire [7:0] resp_count;
wire [63:0] resp_data;
reg [0:0] resp_read;
reg  rst_n;

always begin
    clk=0;
    #10;
    clk=1;
    #3;
    $python("negedge()");
    #7;
end


always begin
    clka=0;
    #10;
    clka=1;
    #3;
    $python("negedgea()");
    #7;
end

 wire [3:0] rid;
 wire [1:0] rresp;
 reg [31:0] araddr;
 reg [1:0] arburst;
 reg [3:0] arcache;
 reg [3:0] arid;
 reg [7:0] arlen;
 reg [2:0] arprot;
 wire  arready;
 reg rready;
 reg [2:0] arsize;
 reg  arvalid;
 reg [31:0] awaddr;
 reg [1:0] awburst;
 reg [3:0] awcache;
 reg [3:0] awid;
 reg [7:0] awlen;
 reg [2:0] awprot;
 wire  awready;
 reg [2:0] awsize;
 reg  awvalid;
 wire [3:0] bid;
 reg  bready;
 wire [1:0] bresp;
 wire  bvalid;
 wire [127:0] rdata;
 wire  rvalid;
 reg  rxd;
 wire  txd;
 reg [127:0] wdata;
 reg  wlast;
 wire  wready;
 reg [15:0] wstrb;
 reg  wvalid;



initial begin
    $dumpvars(0,tb);
    clk = 0;
    req_addr[2:0] = 0;
    req_data[63:0] = 0;
    req_write[0:0] = 0;
    resp_addr[2:0] = 0;
    resp_read[0:0] = 0;
    rst_n = 0;

     araddr[31:0] = 0;
     arburst[1:0] = 0;
     arcache[3:0] = 0;
     arid[3:0] = 0;
     arlen[7:0] = 0;
     arprot[2:0] = 0;
     arsize[2:0] = 0;
     arvalid = 0;
     awaddr[31:0] = 0;
     awburst[1:0] = 0;
     awcache[3:0] = 0;
     awid[3:0] = 0;
     awlen[7:0] = 0;
     awprot[2:0] = 0;
     awsize[2:0] = 0;
     awvalid = 0;
     wvalid = 0;
     bready = 0;
     rready = 0;





    #100;
    rst_n=1;
end
noc3 dut (
     .araddr(araddr[31:0])
    ,.arburst(arburst[1:0])
    ,.arcache(arcache[3:0])
    ,.arid(arid[3:0])
    ,.arlen(arlen[7:0])
    ,.arprot(arprot[2:0])
    ,.arready(arready)
    ,.arsize(arsize[2:0])
    ,.arvalid(arvalid)
    ,.awaddr(awaddr[31:0])
    ,.awburst(awburst[1:0])
    ,.awcache(awcache[3:0])
    ,.awid(awid[3:0])
    ,.awlen(awlen[7:0])
    ,.awprot(awprot[2:0])
    ,.awready(awready)
    ,.awsize(awsize[2:0])
    ,.awvalid(awvalid)
    ,.bid(bid[3:0])
    ,.bready(bready)
    ,.bresp(bresp[1:0])
    ,.bvalid(bvalid)
    ,.clk(clk)
    ,.clka(clka)
    ,.rdata(rdata[127:0])
    ,.req_addr(req_addr[2:0])
    ,.req_count(req_count[7:0])
    ,.req_data(req_data[63:0])
    ,.req_write(req_write)
    ,.resp_addr(resp_addr[2:0])
    ,.resp_count(resp_count[7:0])
    ,.resp_data(resp_data[63:0])
    ,.resp_read(resp_read)
    ,.rid(rid[3:0])
    ,.rlast(rlast)
    ,.rready(rready)
    ,.rresp(rresp[1:0])
    ,.rst_n(rst_n)
    ,.rvalid(rvalid)
    ,.rxd(rxd)
    ,.txd(txd)
    ,.wdata(wdata[127:0])
    ,.wlast(wlast)
    ,.wready(wready)
    ,.wstrb(wstrb[15:0])
    ,.wvalid(wvalid)
);

endmodule
