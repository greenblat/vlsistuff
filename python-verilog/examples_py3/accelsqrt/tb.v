module tb;
reg [31:0] cycles;   initial cycles=0;
reg [31:0] errors;   initial errors=0;
reg [31:0] wrongs;   initial wrongs=0;
reg [31:0] panics;   initial panics=0;
reg [31:0] corrects; initial corrects=0;
reg [31:0] marker;   initial marker=0;
reg [31:0] Index;   initial Index=0;
reg [31:0] awaddr;
reg [1:0] awburst;
reg [3:0] awid;
reg [7:0] awlen;
wire  awready;
reg [3:0] awsize;
reg  awvalid;
reg  axi_clk;
wire [3:0] bid;
reg  bready;
wire [1:0] bresp;
wire  bvalid;
reg [15:0] paddr;
reg  pclk;
reg  penable;
wire [31:0] prdata;
wire  pready;
reg  psel;
reg  rst_n;
reg  sys_clk;
reg [31:0] wdata;
wire  wready;
reg [3:0] wstrb;
reg  wvalid;
reg wlast; initial wlast=0;

wire arvalid = 0;
wire rvalid = 0;
wire rready = 0;




always begin
    sys_clk=0;
    #10;
    sys_clk=1;
    #3;
    $python("sys_clk()");
    #7;
end
always begin
    axi_clk=0;
    #10;
    axi_clk=1;
    #3;
    $python("axi_clk()");
    #7;
end

always begin
    pclk=0;
    #10;
    pclk=1;
    #3;
    $python("pclk()");
    #7;
end


initial begin
    $dumpvars(0,tb);
    awaddr = 0;
    awburst = 0;
    awid = 0;
    awlen = 0;
    awsize = 0;
    awvalid = 0;
    axi_clk = 0;
    bready = 0;
    paddr = 0;
    pclk = 0;
    penable = 0;
    psel = 0;
    rst_n = 0;
    sys_clk = 0;
    wdata = 0;
    wstrb = 0;
    wvalid = 0;
    #100;
    rst_n=1;
end
accel_sqrt dut (
     .awaddr(awaddr[31:0])
    ,.awburst(awburst[1:0])
    ,.awid(awid[3:0])
    ,.awlen(awlen[7:0])
    ,.awready(awready)
    ,.awsize(awsize[3:0])
    ,.awvalid(awvalid)
    ,.axi_clk(axi_clk)
    ,.bid(bid[3:0])
    ,.bready(bready)
    ,.bresp(bresp[1:0])
    ,.bvalid(bvalid)
    ,.paddr(paddr[15:0])
    ,.pclk(pclk)
    ,.penable(penable)
    ,.prdata(prdata[31:0])
    ,.pready(pready)
    ,.psel(psel)
    ,.rst_n(rst_n)
    ,.sys_clk(sys_clk)
    ,.wdata(wdata[31:0])
    ,.wready(wready)
    ,.wstrb(wstrb[3:0])
    ,.wvalid(wvalid)
    ,.wlast(wlast)
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


module inout_driver ( inout io , input dflt );

reg val; initial val=0;
reg drive; initial drive=0;
assign io = drive ? val : 1'bz;
assign (pull1,pull0) io = dflt;

endmodule
