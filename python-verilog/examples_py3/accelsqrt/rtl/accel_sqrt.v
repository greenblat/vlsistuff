


module accel_sqrt (
    input axi_clk
    ,input pclk
    ,input sys_clk
    ,input rst_n     // for all clocks. in real design, better sync them.
    
    ,input awvalid
    ,input [31:0] awaddr
    ,input [1:0] awburst
    ,input [7:0] awlen
    ,input [3:0] awid
    ,input [3:0] awsize
    ,output awready

    ,input wvalid
    ,input wlast
    ,input [3:0] wstrb
    ,input [31:0] wdata
    ,output wready

    ,output bvalid
    ,output [1:0] bresp
    ,output [3:0] bid
    ,input bready



    ,input [15:0] paddr
    ,input psel
    ,input penable
    ,output pready
    ,output [31:0] prdata

);

wire [31:0] axi_wdata;
wire axi_wlast,axi_write;
wire wfull;

axi_write_slave axi_write_slave (
     .clk(axi_clk) ,.rst_n(rst_n)
    ,.awaddr(awaddr[31:0])
    ,.awburst(awburst[1:0])
    ,.awcache(4'b0)
    ,.awid(awid[3:0])
    ,.awlen(awlen[7:0])
    ,.awlock(1'b0)
    ,.awprot(3'b0)
    ,.awready(awready)
    ,.awsize(awsize[2:0])
    ,.awvalid(awvalid)
    ,.bid(bid[3:0])
    ,.bready(bready)
    ,.bresp(bresp[1:0])
    ,.bvalid(bvalid)

    ,.wdata(wdata[31:0])
    ,.wlast(wlast)
    ,.wready(wready)
    ,.wstrb(wstrb[3:0])
    ,.wvalid(wvalid)

    ,.local_addr()
    ,.local_wr_data(axi_wdata)
    ,.local_wr(axi_write)
    ,.local_wr_last(axi_wlast)
    ,.local_wstrb()
    ,.local_wr_ok(!wfull)
);

wire [32:0] sys_data;
wire sys_read;
wire rempty;
wire infull;
async16fifo #(.WID(33)) infifoasync (
     .wclk(axi_clk) ,.rst_n(rst_n)
    ,.rclk(sys_clk)
    ,.writex(axi_write)
    ,.wdata({axi_wlast,axi_wdata})
    ,.rdata(sys_data)
    ,.readx(!infull)
    ,.rempty(rempty)
    ,.wfull(wfull)
    ,.rst_nr() ,.rst_nw()
);


wire [32:0] indata;
syncfifo #(.WID(33),.DEPTH(32)) insyncfifo (.clk(sys_clk),.rst_n(rst_n),.validin(!rempty),.datain(sys_data)
    ,.softreset(1'b0),.full(infull)
    ,.readout(!inempty),.dataout(indata),.empty(inempty)
    ,.count(),.overflow()
);

wire [19:0] sqrtout;
sqrt_u40_5 sqrt_u40_5 (
     .clk(sys_clk) ,.rst_n(rst_n) ,.en(1'b1)
    ,.ain({8'b0,indata[31:0]}) ,.vldin(!inempty)
    ,.out(sqrtout[19:0]) ,.vldout(vldout)
);

syncfifo #(.WID(1),.DEPTH(8)) passfifo (.clk(sys_clk),.rst_n(rst_n),.validin(!inempty),.datain(indata[32])
    ,.softreset(1'b0),.full()
    ,.readout(vldout),.dataout(islast),.empty()
    ,.count(),.overflow()
);

reg [31:0] sumx,computed_data;
reg computed_valid;

always @(posedge sys_clk or negedge rst_n) begin
    if (!rst_n) begin
        sumx <= 0;
        computed_data <= 0;
        computed_valid <= 0;
    end else begin
        if (vldout) sumx <= islast ? 0 : (sumx + sqrtout);
        if (vldout && islast) begin
            computed_data <= (sumx + sqrtout);
            computed_valid <= 1;
        end else 
            computed_valid <= 0;
    end
 end

wire [31:0] pcomputed_data;
wire pcomputed_read,prempty,pwfull;

async16fifo #(.WID(32)) outfifoasync (
     .wclk(sys_clk) ,.rst_n(rst_n)
    ,.rclk(pclk)
    ,.writex(computed_valid)
    ,.wdata(computed_data)
    ,.rdata(pcomputed_data)
    ,.readx(pcomputed_read)
    ,.rempty(prempty)
    ,.wfull(pwfull)
    ,.rst_nr() ,.rst_nw()
);


assign pcomputed_read = !prempty && !pfull;

syncfifo #(.WID(32),.DEPTH(8)) outfifo (.clk(pclk),.rst_n(rst_n),.validin(!prempty),.datain(pcomputed_data)
    ,.softreset(1'b0),.full(pfull)
    ,.readout(psel && penable),.dataout(prdata),.empty(pempty)
    ,.count(),.overflow()
);

assign pready = !pempty;


endmodule

