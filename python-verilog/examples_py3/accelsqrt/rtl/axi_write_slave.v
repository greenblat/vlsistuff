
module axi_write_slave #(parameter DWID=32, parameter BYTES = DWID/8 )(
     input clk, input rst_n

// axi write address channel
    ,input [3:0] awid           // address write id
    ,input [31:0] awaddr
    ,input [7:0] awlen
    ,input [2:0] awsize
    ,input [1:0] awburst
    ,input       awlock
    ,input [3:0] awcache
    ,input [2:0] awprot
    ,input awvalid
    ,output awready

// axi write data channel
    ,input [DWID-1:0] wdata
    ,input [BYTES-1:0] wstrb
    ,input wlast
    ,input wvalid
    ,output wready

// axi write responce channel
    ,output [3:0] bid 
    ,output [1:0] bresp
    ,output bvalid
    ,input bready



// local memory interface
    ,output local_wr
    ,output [31:0] local_addr
    ,output [DWID-1:0] local_wr_data
    ,output [BYTES-1:0] local_wstrb
    ,output  local_wr_last
    ,input  local_wr_ok

);


wire [31:0] xawaddr;
wire [2:0] xawsize;
wire [1:0] xawburst;
wire [3:0] xawid;
wire ad_full,ad_empty;
wire read_ad_fifo;
syncfifo #(32+3+2+4) ad_fifo (.clk(clk),.rst_n(rst_n),.softreset(1'b0)
    ,.validin(awvalid&& awready),.datain({awaddr,awsize,awburst,awid})
    ,.full(ad_full),.empty(ad_empty),.overflow(),.count()
    ,.readout(read_ad_fifo),.dataout({xawaddr,xawsize,xawburst,xawid})
);


assign awready = !ad_full;
wire da_full,da_empty;
wire [DWID-1:0] xwdata;
wire [BYTES-1:0] xwstrb;
wire ywlast;
wire read_da_fifo;
syncfifo #(DWID+BYTES+1) da_fifo (.clk(clk),.rst_n(rst_n),.softreset(1'b0)
    ,.validin(wvalid&& wready),.datain({wdata,wstrb,wlast})
    ,.full(da_full),.empty(da_empty),.overflow(),.count()
    ,.readout(read_da_fifo),.dataout({xwdata,xwstrb,ywlast})
);

assign xwlast = da_empty ? 1'b0 : ywlast;

assign wready = !da_full;

wire br_full,br_empty;
wire bpanic = br_full && wvalid;
wire [1:0] xbresp = {1'b0,bpanic};

syncfifo #(4+2) bresp_fifo (.clk(clk),.rst_n(rst_n),.softreset(1'b0)
    ,.validin(read_da_fifo && xwlast),.datain({xawid,xbresp})
    ,.full(br_full),.empty(br_empty),.overflow(),.count()
    ,.readout(bvalid && bready),.dataout({bid,bresp})
);


assign bvalid = !br_empty;

assign read_ad_fifo = !da_empty && !ad_empty && xwlast && local_wr_ok;
assign read_da_fifo = !da_empty && !ad_empty && local_wr_ok;

reg [31:0] waddr;
reg first;
always @(posedge clk ) begin
    if (!rst_n) begin
        waddr<=0;
        first <= 1;
    end else begin
        if (first && !da_empty && !ad_empty && !xwlast && local_wr_ok) begin
            first <= 0;
            waddr <= xawaddr + ((xawburst==0) ? 0 : (1<<xawsize));
        end else if (!first && !da_empty && !ad_empty && !xwlast && local_wr_ok) begin
            waddr <= waddr + ((xawburst==0) ? 0 : (1<<xawsize));
        end else if (!first && !da_empty && !ad_empty && xwlast && local_wr_ok) begin
            waddr <= 0;
            first <= 1;
        end
    end
end


assign local_wr = !ad_empty && !da_empty;
assign local_addr = first ? xawaddr : waddr;
assign local_wstrb = xwstrb;
assign local_wr_data = xwdata;
assign local_wr_last = xwlast;

endmodule

