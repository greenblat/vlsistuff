module tb;
reg [31:0] cycles;   initial cycles=0;
reg [31:0] errors;   initial errors=0;
reg [31:0] wrongs;   initial wrongs=0;
reg [31:0] panics;   initial panics=0;
reg [31:0] corrects; initial corrects=0;
reg [31:0] marker;   initial marker=0;
reg  clk;
wire [31:0] ms_araddr;
wire [1:0] ms_arburst;
wire [3:0] ms_arcache;
wire [3:0] ms_arid;
wire [7:0] ms_arlen;
wire [2:0] ms_arprot;
wire [3:0] ms_arqos;
reg  ms_arready;
wire [2:0] ms_arsize;
wire  ms_arvalid;
wire [31:0] ms_awaddr;
wire [1:0] ms_awburst;
wire [3:0] ms_awcache;
wire [3:0] ms_awid;
wire [7:0] ms_awlen;
wire [2:0] ms_awprot;
wire [3:0] ms_awqos;
reg  ms_awready;
wire [2:0] ms_awsize;
wire  ms_awvalid;
reg [3:0] ms_bid;
wire  ms_bready;
reg [1:0] ms_bresp;
reg  ms_bvalid;
reg [127:0] ms_rdata;
reg [3:0] ms_rid;
reg  ms_rlast;
wire  ms_rready;
reg [1:0] ms_rresp;
reg  ms_rvalid;
wire [127:0] ms_wdata;
wire  ms_wlast;
reg  ms_wready;
wire [15:0] ms_wstrb;
wire  ms_wvalid;
reg [15:0] paddr;
reg  penable;
wire [31:0] prdata;
wire  pready;
reg  psel;
wire  pslverr;
reg [31:0] pwdata;
reg  pwrite;
reg  rst_n;
reg [31:0] sl_araddr;
reg [1:0] sl_arburst;
reg [3:0] sl_arcache;
reg [3:0] sl_arid;
reg [7:0] sl_arlen;
reg [2:0] sl_arprot;
reg [3:0] sl_arqos;
wire  sl_arready;
reg [2:0] sl_arsize;
reg  sl_arvalid;
reg [31:0] sl_awaddr;
reg [1:0] sl_awburst;
reg [3:0] sl_awcache;
reg [3:0] sl_awid;
reg [7:0] sl_awlen;
reg [2:0] sl_awprot;
reg [3:0] sl_awqos;
wire  sl_awready;
reg [2:0] sl_awsize;
reg  sl_awvalid;
wire [3:0] sl_bid;
reg  sl_bready;
wire [1:0] sl_bresp;
wire  sl_bvalid;
wire [127:0] sl_rdata;
wire [3:0] sl_rid;
wire  sl_rlast;
reg  sl_rready;
wire [1:0] sl_rresp;
wire  sl_rvalid;
reg [127:0] sl_wdata;
reg  sl_wlast;
wire  sl_wready;
reg [15:0] sl_wstrb;
reg  sl_wvalid;

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
    ms_arready = 0;
    ms_awready = 0;
    ms_bid = 0;
    ms_bresp = 0;
    ms_bvalid = 0;
    ms_rdata = 0;
    ms_rid = 0;
    ms_rlast = 0;
    ms_rresp = 0;
    ms_rvalid = 0;
    ms_wready = 0;
    paddr = 0;
    penable = 0;
    psel = 0;
    pwdata = 0;
    pwrite = 0;
    rst_n = 0;
    sl_araddr = 0;
    sl_arburst = 0;
    sl_arcache = 0;
    sl_arid = 0;
    sl_arlen = 0;
    sl_arprot = 0;
    sl_arqos = 0;
    sl_arsize = 0;
    sl_arvalid = 0;
    sl_awaddr = 0;
    sl_awburst = 0;
    sl_awcache = 0;
    sl_awid = 0;
    sl_awlen = 0;
    sl_awprot = 0;
    sl_awqos = 0;
    sl_awsize = 0;
    sl_awvalid = 0;
    sl_bready = 0;
    sl_rready = 0;
    sl_wdata = 0;
    sl_wlast = 0;
    sl_wstrb = 0;
    sl_wvalid = 0;
    #100;
    rst_n=1;
end
axi_firewall dut (
     .clk(clk)
    ,.ms_araddr(ms_araddr[31:0])
    ,.ms_arburst(ms_arburst[1:0])
    ,.ms_arcache(ms_arcache[3:0])
    ,.ms_arid(ms_arid[3:0])
    ,.ms_arlen(ms_arlen[7:0])
    ,.ms_arprot(ms_arprot[2:0])
    ,.ms_arqos(ms_arqos[3:0])
    ,.ms_arready(ms_arready)
    ,.ms_arsize(ms_arsize[2:0])
    ,.ms_arvalid(ms_arvalid)
    ,.ms_awaddr(ms_awaddr[31:0])
    ,.ms_awburst(ms_awburst[1:0])
    ,.ms_awcache(ms_awcache[3:0])
    ,.ms_awid(ms_awid[3:0])
    ,.ms_awlen(ms_awlen[7:0])
    ,.ms_awprot(ms_awprot[2:0])
    ,.ms_awqos(ms_awqos[3:0])
    ,.ms_awready(ms_awready)
    ,.ms_awsize(ms_awsize[2:0])
    ,.ms_awvalid(ms_awvalid)
    ,.ms_bid(ms_bid[3:0])
    ,.ms_bready(ms_bready)
    ,.ms_bresp(ms_bresp[1:0])
    ,.ms_bvalid(ms_bvalid)
    ,.ms_rdata(ms_rdata[127:0])
    ,.ms_rid(ms_rid[3:0])
    ,.ms_rlast(ms_rlast)
    ,.ms_rready(ms_rready)
    ,.ms_rresp(ms_rresp[1:0])
    ,.ms_rvalid(ms_rvalid)
    ,.ms_wdata(ms_wdata[127:0])
    ,.ms_wlast(ms_wlast)
    ,.ms_wready(ms_wready)
    ,.ms_wstrb(ms_wstrb[15:0])
    ,.ms_wvalid(ms_wvalid)
    ,.paddr(paddr[15:0])
    ,.penable(penable)
    ,.prdata(prdata[31:0])
    ,.pready(pready)
    ,.psel(psel)
    ,.pslverr(pslverr)
    ,.pwdata(pwdata[31:0])
    ,.pwrite(pwrite)
    ,.rst_n(rst_n)
    ,.sl_araddr(sl_araddr[31:0])
    ,.sl_arburst(sl_arburst[1:0])
    ,.sl_arcache(sl_arcache[3:0])
    ,.sl_arid(sl_arid[3:0])
    ,.sl_arlen(sl_arlen[7:0])
    ,.sl_arprot(sl_arprot[2:0])
    ,.sl_arqos(sl_arqos[3:0])
    ,.sl_arready(sl_arready)
    ,.sl_arsize(sl_arsize[2:0])
    ,.sl_arvalid(sl_arvalid)
    ,.sl_awaddr(sl_awaddr[31:0])
    ,.sl_awburst(sl_awburst[1:0])
    ,.sl_awcache(sl_awcache[3:0])
    ,.sl_awid(sl_awid[3:0])
    ,.sl_awlen(sl_awlen[7:0])
    ,.sl_awprot(sl_awprot[2:0])
    ,.sl_awqos(sl_awqos[3:0])
    ,.sl_awready(sl_awready)
    ,.sl_awsize(sl_awsize[2:0])
    ,.sl_awvalid(sl_awvalid)
    ,.sl_bid(sl_bid[3:0])
    ,.sl_bready(sl_bready)
    ,.sl_bresp(sl_bresp[1:0])
    ,.sl_bvalid(sl_bvalid)
    ,.sl_rdata(sl_rdata[127:0])
    ,.sl_rid(sl_rid[3:0])
    ,.sl_rlast(sl_rlast)
    ,.sl_rready(sl_rready)
    ,.sl_rresp(sl_rresp[1:0])
    ,.sl_rvalid(sl_rvalid)
    ,.sl_wdata(sl_wdata[127:0])
    ,.sl_wlast(sl_wlast)
    ,.sl_wready(sl_wready)
    ,.sl_wstrb(sl_wstrb[15:0])
    ,.sl_wvalid(sl_wvalid)
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
