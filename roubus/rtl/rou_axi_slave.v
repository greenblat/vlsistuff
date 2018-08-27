module rou_axi_slave #(
     parameter DWID = 128 
    ,parameter AWID = 32
    ,parameter TWID = 5 
    ,parameter BWID = 
        (DWID==512)  ? 6 : 
        (DWID==256)  ? 5 : 
        (DWID==128) ? 4 : 
        (DWID==64)  ? 3 : 2 
    ,parameter WID = 2+DWID+AWID+BWID+TWID
    ,parameter IDWID = 4
) (
    input clk, input rst_n
    ,input rou_in_seen, output rou_out_seen
    ,input [WID-1:0] rou_in, output [2:0] ack_in 
    ,output [WID-1:0] rou_out, input [2:0] ack_out
    ,input [31:0] pages, input [31:0] whoami



     // axi write address channel
    ,input [IDWID-1:0] awid            // address write id
    ,input [31:0] awaddr
    ,input [7:0] awlen
    ,input [2:0] awsize
    ,input [1:0] awburst
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
 // axi read address channel
    ,input [IDWID-1:0] arid
    ,input [31:0] araddr
    ,input [7:0] arlen
    ,input [2:0] arsize
    ,input [1:0] arburst
    ,input arvalid
    ,output arready
 // axi read data channel
    ,output [IDWID-1:0] rid
    ,output [127:0] rdata
    ,output [1:0] rresp
    ,output rlast
    ,output rvalid
    ,input rready


);

wire [31:0] control;
wire [WID-1:0] msg_in,msg_out;
wire msg_in_ack,msg_out_ack;

wire [AWID-1:0] base_address;

rou_nif nif (
     .ack_in(ack_in[2:0])
    ,.ack_out(ack_out[2:0])
    ,.clk(clk)
    ,.control(control[31:0])
    ,.base_address(base_address)
    ,.msg_in(msg_in[(WID - 1):0])
    ,.msg_in_ack(msg_in_ack)
    ,.msg_out(msg_out[(WID - 1):0])
    ,.msg_out_ack(msg_out_ack)

    ,.rou_in_seen(rou_in_seen)
    ,.rou_out_seen(rou_out_seen)

    ,.rou_in(rou_in[(WID - 1):0])
    ,.rou_out(rou_out[(WID - 1):0])
    ,.rst_n(rst_n)
    ,.uses_pages(pages[15:0])
    ,.whoami(whoami[15:0])
    ,.seen_monitor(1'b0)
);

wire local_wr,local_last;
wire [IDWID-1:0] local_wid;
wire [31:0] local_wr_addr;
wire [15:0] local_wstrb;
wire [127:0] local_wr_data;
wire  local_wr_ok;
wire  local_wr_error = 1'b0;



wire  [IDWID-1:0] bidd;
wire  [1:0] brespp;
wire  bvalidd;
assign rresp = 0;

axi_write_slave  #(.IDWID(IDWID))  axi_write_slave (
     .awaddr(awaddr[31:0])
    ,.awburst(awburst[1:0])
    ,.awcache(4'b0)
    ,.awid(awid)
    ,.awlen(awlen[7:0])
    ,.awprot(3'b0)
    ,.awready(awready)
    ,.awsize(awsize[2:0])
    ,.awvalid(awvalid)
    ,.bid(bid)
    ,.bready(bready)
    ,.bresp(bresp[1:0])
    ,.bvalid(bvalid)
    ,.clk(clk)
    ,.local_addr(local_wr_addr[31:0])
    ,.local_wr_data(local_wr_data[127:0])
    ,.local_wr(local_wr)
    ,.local_last(local_last)
    ,.local_wid(local_wid)
    ,.local_wstrb(local_wstrb[15:0])
    ,.local_wr_ok(local_wr_ok)
    ,.local_wr_error(local_wr_error)
    ,.rst_n(rst_n)
    ,.wdata(wdata[127:0])
    ,.wlast(wlast)
    ,.wready(wready)
    ,.wstrb(wstrb[15:0])
    ,.wvalid(wvalid)
    ,.active(write_active)
);



wire [4:0] modify_wr_address  = 
    local_wstrb[0] ? 0 : local_wstrb[1] ? 1 : local_wstrb[2] ? 2 : local_wstrb[3] ? 3 :
    local_wstrb[4] ? 4 : local_wstrb[5] ? 5 : local_wstrb[6] ? 6 : local_wstrb[7] ? 7 :
    local_wstrb[8] ? 8 : local_wstrb[9] ? 9 : local_wstrb[10] ? 10 : local_wstrb[11] ? 11 :
    local_wstrb[12] ? 12 : local_wstrb[13] ? 13 : local_wstrb[14] ? 14 : local_wstrb[15] ? 15 : 0;


wire [15:0] modify_wstrb = local_wstrb >>modify_wr_address;
wire [3:0]  modify_bytes = 
    modify_wstrb[15] ? 15 : modify_wstrb[14] ? 14 : modify_wstrb[13] ? 13 : modify_wstrb[12] ? 12 :
    modify_wstrb[11] ? 11 : modify_wstrb[10] ? 10 : modify_wstrb[9] ? 9 : modify_wstrb[8] ? 8 :
    modify_wstrb[7] ? 7 : modify_wstrb[6] ? 6 : modify_wstrb[5] ? 5 : modify_wstrb[4] ? 4 :
    modify_wstrb[3] ? 3 : modify_wstrb[2] ? 2 : modify_wstrb[1] ? 1 : 0;


wire [31:0] mod_wr_addr =  local_wr_addr + modify_wr_address;
wire [127:0] mod_wr_data = local_wr_data >> (modify_wr_address*8);

wire [WID-1:0] msg_wr_out,msg_rd_out;
rou_msg_build  msg_out_build  (.msg(msg_wr_out),.data(mod_wr_data),.addr(mod_wr_addr),.tags(5'b00011) ,.bytes(modify_bytes) ,.cmd(local_wr ? 2'd2 : 2'd0));

assign local_wr_ok =  msg_out_ack && (msg_rd_out[1:0]==2'b00);
assign bresp = 2'b0;

syncfifo #(IDWID,4) ad_fifo (.clk(clk),.rst_n(rst_n),.softreset(1'b0)
    ,.validin(local_last&& local_wr),.datain(local_wid)
    ,.full(),.empty(bfifo_empty),.overflow(),.count()
    ,.readout(bready && local_wr_ok),.dataout(bid)
);
assign bvalid =  !bfifo_empty;




wire [15:0] rd_bytes =(1+arlen)*(1<<arsize);
wire rdfull;
assign arready = !rdfull && depot_taken && !no_place;

wire [15:0] xrbytes;
wire [31:0] xraddr;
wire [IDWID-1:0] xrid;

syncfifo #(32+16+IDWID,4) read_rq_fifo (.clk(clk),.rst_n(rst_n),.softreset(1'b0)
    ,.validin(arvalid&&arready),.datain({araddr,rd_bytes,arid})
    ,.full(rdfull),.empty(rdempty),.overflow(),.count()
    ,.readout(msg_out_ack),.dataout({xraddr,xrbytes,xrid})
);

wire [127:0] msg_rd_addr = 128'b0 | {xrbytes[15:4],base_address[AWID-1:IDWID+4],xrid,4'b0} ;
rou_msg_build  msg_out_rd_build  (.msg(msg_rd_out),.data(msg_rd_addr),.addr(xraddr),.tags(5'd0) ,.bytes(xrbytes[3:0]) ,.cmd(rdempty ? 2'b00 : 2'b01));
assign msg_out = !rdempty ? msg_rd_out : local_wr ? msg_wr_out : 0;


wire rd_fifo_full,rd_fifo_empty;
assign msg_in_ack = !rd_fifo_full;
wire [127:0] msg_in_data;
wire [1:0] msg_in_cmd;
wire [3:0] msg_in_bytes;
wire [4:0] msg_in_tags;
wire [31:0] msg_in_addr;
rou_msg_fields msg_in_fields(.msg(msg_in), .addr(msg_in_addr) ,.tags(msg_in_tags) ,.bytes(msg_in_bytes) ,.cmd(msg_in_cmd) ,.data(msg_in_data));

wire [BWID-1:0] backbytes;
wire [DWID-1:0] rdata;
syncfifo #(DWID+BWID+IDWID,4) rd_data_fifo (.clk(clk),.rst_n(rst_n),.softreset(1'b0)
    ,.validin(msg_in_cmd==2),.datain({msg_in_data,msg_in_bytes,msg_in_addr[IDWID+4-1:4]})
    ,.full(rd_fifo_full),.empty(rd_fifo_empty),.overflow(),.count()
    ,.readout(rready),.dataout({rdata,backbytes,rid})
);

assign rvalid = !rd_fifo_empty;

wire [4-1:0] actives,rlasts,takens,depot_arvalid,matches;
wire [IDWID-1:0] activeid0,activeid1,activeid2,activeid3;



assign no_place = arvalid && (depot_arvalid==0);

wire ok0 = !actives[0];
wire ok1 = actives[1:0] == 2'b01;
wire ok2 = actives[2:0] == 3'b011;
wire ok3 = actives[3:0] == 4'b0111;

read_axi_depot depot0 (
    .clk(clk) ,.rst_n(rst_n)
    ,.active(actives[0]) ,.activeid(activeid0)
    ,.arbytes(rd_bytes) ,.arid(arid) ,.arvalid(depot_arvalid[0])
    ,.backbytes(rd_fifo_empty? {BWID{1'b0}} : backbytes) ,.rid(rid) ,.rready(rready) ,.rvalid(rvalid)
    ,.rlast(rlasts[0]) ,.taken(takens[0])
);
assign matches[0] = arvalid && actives[0] && (activeid0==arid);
assign depot_arvalid[0] =  (takens[0] && matches[0]) || (arvalid && (matches==0) && ok0);

read_axi_depot depot1 (
    .clk(clk) ,.rst_n(rst_n)
    ,.active(actives[1]) ,.activeid(activeid1)
    ,.arbytes(rd_bytes) ,.arid(arid) ,.arvalid(depot_arvalid[1])
    ,.backbytes(rd_fifo_empty? {BWID{1'b0}} : backbytes) ,.rid(rid) ,.rready(rready) ,.rvalid(rvalid)
    ,.rlast(rlasts[1]) ,.taken(takens[1])
);
assign matches[1] = arvalid && actives[1] && (activeid1==arid);
assign depot_arvalid[1] =  (takens[1] && matches[1]) || (arvalid && (matches==0) && ok1);

read_axi_depot depot2 (
    .clk(clk) ,.rst_n(rst_n)
    ,.active(actives[2]) ,.activeid(activeid2)
    ,.arbytes(rd_bytes) ,.arid(arid) ,.arvalid(depot_arvalid[2])
    ,.backbytes(rd_fifo_empty? {BWID{1'b0}} : backbytes) ,.rid(rid) ,.rready(rready) ,.rvalid(rvalid)
    ,.rlast(rlasts[2]) ,.taken(takens[2])
);
assign matches[2] = arvalid && actives[2] && (activeid2==arid);
assign depot_arvalid[2] =  (takens[2] && matches[2]) || (arvalid && (matches==0) && ok2);

read_axi_depot depot3 (
    .clk(clk) ,.rst_n(rst_n)
    ,.active(actives[3]) ,.activeid(activeid3)
    ,.arbytes(rd_bytes) ,.arid(arid) ,.arvalid(depot_arvalid[3])
    ,.backbytes(rd_fifo_empty? {BWID{1'b0}} : backbytes) ,.rid(rid) ,.rready(rready) ,.rvalid(rvalid)
    ,.rlast(rlasts[3]) ,.taken(takens[3])
);
assign matches[3] = arvalid && actives[3] && (activeid3==arid);
assign depot_arvalid[3] =  (takens[3] && matches[3]) || (arvalid && (matches==0) && ok3);


assign depot_taken = |takens;


assign rlast  = 
       (actives[0] && (activeid0==rid) && rlasts[0])
    || (actives[1] && (activeid1==rid) && rlasts[1])
    || (actives[2] && (activeid2==rid) && rlasts[2])
    || (actives[3] && (activeid3==rid) && rlasts[3])
    ;




endmodule

