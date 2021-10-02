
module axi_wr_4_splitter #(parameter EXTRAS = 8, parameter IDWID=4, parameter DWID=64, parameter WSTRB=DWID/8) (
    input clk, input rst_n


// A port
    ,output [IDWID-1:0] a_awid
    ,output [31:0] a_awaddr
    ,output [7:0] a_awlen
    ,output [1:0] a_awburst
    ,output [EXTRAS-1:0] a_awextras
    ,output a_awvalid
    ,input a_awready

    ,output [DWID-1:0] a_wdata
    ,output [WSTRB-1:0] a_wstrb
    ,output a_wlast
    ,output a_wvalid
    ,input a_wready

    ,input [IDWID-1:0] a_bid
    ,input [1:0] a_bresp
    ,input a_bvalid
    ,output a_bready

// B port
    ,output [IDWID-1:0] b_awid
    ,output [31:0] b_awaddr
    ,output [7:0] b_awlen
    ,output [EXTRAS-1:0] b_awextras
    ,output [1:0] b_awburst
    ,output b_awvalid
    ,input b_awready

    ,output [DWID-1:0] b_wdata
    ,output [WSTRB-1:0] b_wstrb
    ,output b_wlast
    ,output b_wvalid
    ,input b_wready
    ,input [IDWID-1:0] b_bid
    ,input [1:0] b_bresp
    ,input b_bvalid
    ,output b_bready

// C port
    ,output [IDWID-1:0] c_awid
    ,output [31:0] c_awaddr
    ,output [7:0] c_awlen
    ,output [EXTRAS-1:0] c_awextras
    ,output [1:0] c_awburst
    ,output c_awvalid
    ,input c_awready
    ,output [DWID-1:0] c_wdata
    ,output [WSTRB-1:0] c_wstrb
    ,output c_wlast
    ,output c_wvalid
    ,input c_wready
    ,input [IDWID-1:0] c_bid
    ,input [1:0] c_bresp
    ,input c_bvalid
    ,output c_bready


// D port
    ,output [IDWID-1:0] d_awid
    ,output [31:0] d_awaddr
    ,output [7:0] d_awlen
    ,output [EXTRAS-1:0] d_awextras
    ,output [1:0] d_awburst
    ,output d_awvalid
    ,input d_awready
    ,output [DWID-1:0] d_wdata
    ,output [WSTRB-1:0] d_wstrb
    ,output d_wlast
    ,output d_wvalid
    ,input d_wready
    ,input [IDWID-1:0] d_bid
    ,input [1:0] d_bresp
    ,input d_bvalid
    ,output d_bready




    ,input [3:0] awid
    ,input [31:0] awaddr
    ,input [7:0] awlen
    ,input [EXTRAS-1:0] awextras
    ,input [1:0] awburst
    ,input awvalid
    ,output awready
    ,input [DWID-1:0] wdata
    ,input [WSTRB-1:0] wstrb
    ,input wlast
    ,input wvalid
    ,output wready
    ,output [IDWID-1:0] bid
    ,output [1:0] bresp
    ,output bvalid
    ,input bready

);

localparam AWIDE = IDWID + 32 + 8 + EXTRAS + 2;
wire [AWIDE-1:0] new_aw_entry =   { awid ,awaddr ,awlen ,awextras ,awburst };
wire aw_empty,aw_full;
wire [AWIDE-1:0] active_aw_entry;
wire readout_aw_fifo;
syncfifo_sampled #(AWIDE,4) aw_fifo (.clk(clk),.rst_n(rst_n),.vldin(awvalid && awready)
    ,.din(new_aw_entry)
    ,.empty(aw_empty),.full(aw_full)
    ,.readout(readout_aw_fifo)
    ,.dout(active_aw_entry)
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_aw_fifo)
);
assign awready = !aw_full;

wire readout_w_fifo = (a_wvalid && a_wready) || (b_wvalid && b_wready) || (c_wvalid && c_wready) || (d_wvalid && d_wready) ;

wire [DWID-1:0] work_wdata;
wire [WSTRB-1:0] work_wstrb;
wire work_wlast;
syncfifo_sampled #(DWID+WSTRB+1,8) w_fifo (.clk(clk),.rst_n(rst_n),.vldin(wvalid && wready)
    ,.din({wdata,wstrb,wlast})
    ,.empty(w_empty),.full(w_full)
    ,.readout(readout_w_fifo)
    ,.dout({work_wdata,work_wstrb,work_wlast})
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_w_fifo)
);
assign wready = !w_full;


wire [2:0] whosnext = 
    a_start ? 1 :
    b_start ? 2 :
    c_start ? 3 :
    d_start ? 4 :
    0;
wire [2:0] whosnow;
wire finished_transaction = readout_w_fifo && work_wlast;
wire order_fifo_empty,order_fifo_full;
syncfifo_sampled #(3,8) order_fifo (.clk(clk),.rst_n(rst_n),.vldin(readout_aw_fifo)
    ,.din(whosnext)
    ,.empty(order_fifo_empty),.full(order_fifo_full)
    ,.readout(finished_transaction && !order_fifo_empty)
    ,.dout(whosnow)
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_order_fifo)
);
assign wready = !w_full;


wire [3:0] work_awid;
wire [31:0] work_awaddr;
wire [7:0] work_awlen;
wire [EXTRAS-1:0] work_awextras;
wire [1:0] work_awburst;
assign {work_awid ,work_awaddr ,work_awlen ,work_awextras ,work_awburst} = active_aw_entry ;

wire a_start = !aw_empty && (work_awaddr[31:30] == 0);
wire b_start = !aw_empty && (work_awaddr[31:30] == 1);
wire c_start = !aw_empty && (work_awaddr[31:30] == 2);
wire d_start = !aw_empty && (work_awaddr[31:30] == 3);

assign readout_aw_fifo = !order_fifo_full && !aw_empty && (
    (a_start && a_awready) || 
    (b_start && b_awready) || 
    (c_start && c_awready) ||
    (d_start && d_awready)  
);
assign a_awvalid = a_start;
assign b_awvalid = b_start;
assign c_awvalid = c_start;
assign d_awvalid = d_start;

assign a_wvalid = (whosnow==1) && !w_empty ;
assign b_wvalid = (whosnow==2) && !w_empty ;
assign c_wvalid = (whosnow==3) && !w_empty ;
assign d_wvalid = (whosnow==4) && !w_empty ;

assign a_wdata = a_wvalid ? work_wdata : 0;
assign b_wdata = b_wvalid ? work_wdata : 0;
assign c_wdata = c_wvalid ? work_wdata : 0;
assign d_wdata = d_wvalid ? work_wdata : 0;

assign a_wlast = work_wlast;
assign b_wlast = work_wlast;
assign c_wlast = work_wlast;
assign d_wlast = work_wlast;
assign a_wstrb = work_wstrb;
assign b_wstrb = work_wstrb;
assign c_wstrb = work_wstrb;
assign d_wstrb = work_wstrb;


wire back_bid_a_fifo_empty,back_bid_a_fifo_full;
wire [IDWID-1:0] x_a_bid;
wire [1:0] x_a_bresp;
syncfifo #(IDWID+2,2) back_bid_a_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(a_bvalid && !back_bid_a_fifo_full)
    ,.din({a_bid,a_bresp})
    ,.empty(back_bid_a_fifo_empty),.full(back_bid_a_fifo_full)
    ,.readout(readout_back_bid_a_fifo) ,.dout({x_a_bid,x_a_bresp})
    ,.count() ,.softreset(1'b0)
    ,.overflow()
);

wire back_bid_b_fifo_empty,back_bid_b_fifo_full;
wire [IDWID-1:0] x_b_bid;
wire [1:0] x_b_bresp;
syncfifo #(IDWID+2,2) back_bid_b_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(b_bvalid && !back_bid_b_fifo_full)
    ,.din({b_bid,b_bresp})
    ,.empty(back_bid_b_fifo_empty),.full(back_bid_b_fifo_full)
    ,.readout(readout_back_bid_b_fifo) ,.dout({x_b_bid,x_b_bresp})
    ,.count() ,.softreset(1'b0)
    ,.overflow()
);


wire back_bid_c_fifo_empty,back_bid_c_fifo_full;
wire [IDWID-1:0] x_c_bid;
wire [1:0] x_c_bresp;
syncfifo #(IDWID+2,2) back_bid_c_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(c_bvalid && !back_bid_c_fifo_full)
    ,.din({c_bid,c_bresp})
    ,.empty(back_bid_c_fifo_empty),.full(back_bid_c_fifo_full)
    ,.readout(readout_back_bid_c_fifo) ,.dout({x_c_bid,x_c_bresp})
    ,.count() ,.softreset(1'b0)
    ,.overflow()
);

wire back_bid_d_fifo_empty,back_bid_d_fifo_full;
wire [IDWID-1:0] x_d_bid;
wire [1:0] x_d_bresp;
syncfifo #(IDWID+2,2) back_bid_d_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(d_bvalid && !back_bid_d_fifo_full)
    ,.din({d_bid,d_bresp})
    ,.empty(back_bid_d_fifo_empty),.full(back_bid_d_fifo_full)
    ,.readout(readout_back_bid_d_fifo) ,.dout({x_d_bid,x_d_bresp})
    ,.count() ,.softreset(1'b0)
    ,.overflow()
);
assign a_bready = !back_bid_a_fifo_full;
assign b_bready = !back_bid_b_fifo_full;
assign c_bready = !back_bid_c_fifo_full;
assign d_bready = !back_bid_d_fifo_full;


assign readout_back_bid_a_fifo =  b_vldin && !back_bid_a_fifo_empty;
assign readout_back_bid_b_fifo =  b_vldin && !back_bid_b_fifo_empty && back_bid_a_fifo_empty;
assign readout_back_bid_c_fifo =  b_vldin && !back_bid_c_fifo_empty && back_bid_a_fifo_empty && back_bid_b_fifo_empty;
assign readout_back_bid_d_fifo =  b_vldin && !back_bid_d_fifo_empty && back_bid_a_fifo_empty && back_bid_b_fifo_empty && back_bid_c_fifo_empty;




wire b_vldin = !b_full && (!back_bid_a_fifo_empty || !back_bid_b_fifo_empty || !back_bid_c_fifo_empty || !back_bid_d_fifo_empty);

wire [IDWID+2+2-1:0] b_entry = 
    !back_bid_a_fifo_empty  ? {x_a_bid,x_a_bresp,2'b00} :
    !back_bid_b_fifo_empty  ? {x_b_bid,x_b_bresp,2'b01} :
    !back_bid_c_fifo_empty  ? {x_c_bid,x_c_bresp,2'b10} :
    !back_bid_d_fifo_empty  ? {x_d_bid,x_d_bresp,2'b11} :
    0;
    
wire [1:0] bowner;
syncfifo_sampled #(IDWID+2+2,4) b_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(b_vldin)
    ,.din(b_entry)
    ,.empty(b_empty),.full(b_full)
    ,.readout(bready && !b_empty) ,.dout({bid,bresp,bowner})
    ,.count() ,.softreset(1'b0)
    ,.overflow(panic_b_fifo)
);
assign bvalid = !b_empty;

assign a_awaddr = {work_awaddr[29:0],2'b0};
assign b_awaddr = {work_awaddr[29:0],2'b0};
assign c_awaddr = {work_awaddr[29:0],2'b0};
assign d_awaddr = {work_awaddr[29:0],2'b0};

assign a_awlen = work_awlen;
assign b_awlen = work_awlen;
assign c_awlen = work_awlen;
assign d_awlen = work_awlen;

assign a_awextras = work_awextras;
assign b_awextras = work_awextras;
assign c_awextras = work_awextras;
assign d_awextras = work_awextras;

assign a_awburst = work_awburst;
assign b_awburst = work_awburst;
assign c_awburst = work_awburst;
assign d_awburst = work_awburst;

assign a_awid = work_awid;
assign b_awid = work_awid;
assign c_awid = work_awid;
assign d_awid = work_awid;


reg [7:0] a_bcount,b_bcount,c_bcount,d_bcount;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        a_bcount <= 0;b_bcount <= 0;c_bcount <= 0;d_bcount <= 0;
    end else begin
        if (a_awvalid && a_awready && !((bowner==0)&&bvalid&&bready)) a_bcount <= a_bcount+1;
        else if (!(a_awvalid && a_awready) && ((bowner==0)&&bvalid&&bready)) a_bcount <= a_bcount-1;

        if (b_awvalid && b_awready && !((bowner==1)&&bvalid&&bready)) b_bcount <= b_bcount+1;
        else if (!(b_awvalid && b_awready) && ((bowner==1)&&bvalid&&bready)) b_bcount <= b_bcount-1;

        if (c_awvalid && c_awready && !((bowner==2)&&bvalid&&bready)) c_bcount <= c_bcount+1;
        else if (!(c_awvalid && c_awready) && ((bowner==2)&&bvalid&&bready)) c_bcount <= c_bcount-1;

        if (d_awvalid && d_awready && !((bowner==3)&&bvalid&&bready)) d_bcount <= d_bcount+1;
        else if (!(d_awvalid && d_awready) && ((bowner==3)&&bvalid&&bready)) d_bcount <= d_bcount-1;
    end
end



endmodule


