module axi_write_slave #(parameter IDWID=8)(
     input clk, input rst_n
 // axi write address channel
    ,input [IDWID-1:0] awid            // address write id
    ,input [31:0] awaddr
    ,input [7:0] awlen
    ,input [2:0] awsize
    ,input [1:0] awburst
    ,input [3:0] awcache
    ,input [2:0] awprot
    ,input awvalid
    ,output awready
 // axi write data channel
    ,input [127:0] wdata
    ,input [15:0] wstrb
    ,input wlast
    ,input wvalid
    ,output wready
 // axi write responce channel
    ,output [IDWID-1:0] bid 
    ,output [1:0] bresp
    ,output bvalid
    ,input bready
 // local memory interface
    ,output local_wr
    ,output local_last
    ,output [31:0] local_addr
    ,output [127:0] local_wr_data
    ,output [15:0] local_wstrb
    ,input  local_wr_ok
    ,input  local_wr_error

    ,output [IDWID-1:0] local_wid

    ,output active // used to monitor in simulation
);
wire [31:0] xawaddr;
wire [2:0] xawsize;
wire [1:0] xawburst;
wire [IDWID-1:0] xawid;
wire [7:0] xawlen;
wire ad_full,ad_empty;
wire read_ad_fifo;
syncfifo #(32+3+2+IDWID+8,4) ad_fifo (.clk(clk),.rst_n(rst_n),.softreset(1'b0)
    ,.validin(awvalid&& awready),.datain({awaddr,awsize,awburst,awid,awlen})
    ,.full(ad_full),.empty(ad_empty),.overflow(),.count()
    ,.readout(read_ad_fifo),.dataout({xawaddr,xawsize,xawburst,xawid,xawlen})
);
assign awready = !ad_full;
wire da_full,da_empty;
wire [127:0] xwdata;
wire [15:0] xwstrb;
wire ywlast;
wire read_da_fifo;
syncfifo #(128+16+1,4) da_fifo (.clk(clk),.rst_n(rst_n),.softreset(1'b0)
    ,.validin(wvalid&& wready),.datain({wdata,wstrb,wlast})
    ,.full(da_full),.empty(da_empty),.overflow(),.count()
    ,.readout(read_da_fifo),.dataout({xwdata,xwstrb,ywlast})
);
assign xwlast = da_empty ? 1'b0 : ywlast;
assign wready = !da_full;
wire br_full,br_empty;
wire bpanic = br_full && wvalid;

reg accumulate_error;
always @(posedge clk) begin
    if (!rst_n) begin
        accumulate_error <=1'b0;
    end else begin
        if (read_da_fifo) begin
            if (ywlast) accumulate_error <= 1'b0;
            else accumulate_error <= accumulate_error | bpanic |  local_wr_error;
        end
    end
end


wire [1:0] xbresp = {1'b0,(accumulate_error | bpanic |  local_wr_error)};
syncfifo #(IDWID+2,4) bresp_fifo (.clk(clk),.rst_n(rst_n),.softreset(1'b0)
    ,.validin(read_da_fifo && xwlast),.datain({xawid,xbresp})
    ,.full(br_full),.empty(br_empty),.overflow(),.count()
    ,.readout(bvalid && bready),.dataout({bid,bresp})
);
assign bvalid = !br_empty;
assign read_ad_fifo = !da_empty && !ad_empty && xwlast && local_wr_ok;
assign read_da_fifo = !da_empty && !ad_empty && local_wr_ok;
reg [31:0] waddr;
reg first;


wire [31:0] mask0 = (1<<xawsize)-1;
wire [31:0] addr0 = xawaddr & ~mask0;

wire [IDWID-1:0] wraparound = 
         (xawlen==1) ? 4'd1 :
         (xawlen==3) ? 4'd2 :
         (xawlen==7) ? 4'd3 :
         (xawlen==15) ? 4'd4 :
         4'd0;
wire [4:0] wincr = (xawburst==0) ? 5'b0 : (5'b1<<xawsize); 
wire [31:0] burst_mask =  (wraparound==0) ? 32'hffffffff : (1<<(xawsize+wraparound))-1;
wire [31:0] mask1 = (xawburst==2'd2) ? burst_mask  : 32'hffffffff;
wire [31:0] next_waddr = (~mask1 & waddr)|(mask1 & (waddr + wincr));
wire [31:0] next_xawaddr = (~mask1 & xawaddr)|(mask1 & (xawaddr + wincr));





always @(posedge clk ) begin
    if (!rst_n) begin
        waddr<=0;
        first <= 1;
    end else begin
        if (first && !da_empty && !ad_empty && !xwlast && local_wr_ok) begin
            first <= 0;
            waddr <= next_xawaddr;
        end else if (!first && !da_empty && !ad_empty && !xwlast && local_wr_ok) begin
            waddr <= next_waddr;
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
assign local_last = xwlast;
assign local_wid = xawid;


assign active = !first || !br_empty || !ad_empty;
endmodule

