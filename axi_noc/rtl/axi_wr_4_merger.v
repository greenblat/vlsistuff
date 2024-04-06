
module axi_wr_4_merger #(parameter AWID=32,parameter IDWID=4, parameter DWID=32, parameter WSTRB=DWID/8, parameter EXTRAS=8) (
    input clk, input rst_n

    ,input [3:0] a_awmst
    ,input [3:0] b_awmst
    ,input [3:0] c_awmst
    ,input [3:0] d_awmst
    ,output [3:0] a_bmst
    ,output [3:0] b_bmst
    ,output [3:0] c_bmst
    ,output [3:0] d_bmst

    ,output [3:0] awmst
    ,input [3:0] bmst

    ,input [15:0] from_a
    ,input [15:0] from_b
    ,input [15:0] from_c
    ,input [15:0] from_d

    ,input [IDWID-1:0] a_awid
    ,input [AWID-1:0] a_awaddr
    ,input [7:0] a_awlen
    ,input [2:0] a_awsize
    ,input [EXTRAS-1:0] a_awextras
    ,input [1:0] a_awburst
    ,input a_awvalid
    ,output a_awready
    ,input [DWID-1:0] a_wdata
    ,input [WSTRB-1:0] a_wstrb
    ,input a_wlast
    ,input a_wvalid
    ,output a_wready
    ,output [IDWID-1:0] a_bid
    ,output [1:0] a_bresp
    ,output a_bvalid
    ,input a_bready

    ,input [IDWID-1:0] b_awid
    ,input [AWID-1:0] b_awaddr
    ,input [7:0] b_awlen
    ,input [2:0] b_awsize
    ,input [EXTRAS-1:0] b_awextras
    ,input [1:0] b_awburst
    ,input b_awvalid
    ,output b_awready
    ,input [DWID-1:0] b_wdata
    ,input [WSTRB-1:0] b_wstrb
    ,input b_wlast
    ,input b_wvalid
    ,output b_wready
    ,output [IDWID-1:0] b_bid
    ,output [1:0] b_bresp
    ,output b_bvalid
    ,input b_bready


    ,input [IDWID-1:0] c_awid
    ,input [AWID-1:0] c_awaddr
    ,input [7:0] c_awlen
    ,input [2:0] c_awsize
    ,input [EXTRAS-1:0] c_awextras
    ,input [1:0] c_awburst
    ,input c_awvalid
    ,output c_awready
    ,input [DWID-1:0] c_wdata
    ,input [WSTRB-1:0] c_wstrb
    ,input c_wlast
    ,input c_wvalid
    ,output c_wready
    ,output [IDWID-1:0] c_bid
    ,output [1:0] c_bresp
    ,output c_bvalid
    ,input c_bready

    ,input [IDWID-1:0] d_awid
    ,input [AWID-1:0] d_awaddr
    ,input [7:0] d_awlen
    ,input [2:0] d_awsize
    ,input [EXTRAS-1:0] d_awextras
    ,input [1:0] d_awburst
    ,input d_awvalid
    ,output d_awready
    ,input [DWID-1:0] d_wdata
    ,input [WSTRB-1:0] d_wstrb
    ,input d_wlast
    ,input d_wvalid
    ,output d_wready
    ,output [IDWID-1:0] d_bid
    ,output [1:0] d_bresp
    ,output d_bvalid
    ,input d_bready



    ,output [3:0] awid
    ,output [AWID-1:0] awaddr
    ,output [7:0] awlen
    ,output [2:0] awsize
    ,output [EXTRAS-1:0] awextras
    ,output [1:0] awburst
    ,output awvalid
    ,input awready
    ,output [DWID-1:0] wdata
    ,output [WSTRB-1:0] wstrb
    ,output wlast
    ,output wvalid
    ,input wready
    ,input [IDWID-1:0] bid
    ,input [1:0] bresp
    ,input bvalid
    ,output bready

);

wire a_aw_full,a_aw_empty;
assign a_awready = !a_aw_full;
wire b_aw_full,b_aw_empty;
assign b_awready = !b_aw_full;
wire c_aw_full,c_aw_empty;
assign c_awready = !c_aw_full;
wire d_aw_full,d_aw_empty;
assign d_awready = !d_aw_full;

localparam AWIDE = 4 + 3 + IDWID + AWID + 8 + EXTRAS + 2 ;
wire [AWIDE-1:0] new_a_aw_entry =   { a_awmst, a_awsize, a_awextras ,a_awid, a_awburst, a_awlen, a_awaddr };
wire [AWIDE-1:0] new_b_aw_entry =   { b_awmst, b_awsize, b_awextras ,b_awid, b_awburst, b_awlen, b_awaddr };
wire [AWIDE-1:0] new_c_aw_entry =   { c_awmst, c_awsize, c_awextras ,c_awid, c_awburst, c_awlen, c_awaddr };
wire [AWIDE-1:0] new_d_aw_entry =   { d_awmst, d_awsize, d_awextras ,d_awid, d_awburst, d_awlen, d_awaddr };

wire [AWIDE-1:0] a_active_aw_entry;
wire [AWIDE-1:0] b_active_aw_entry;
wire [AWIDE-1:0] c_active_aw_entry;
wire [AWIDE-1:0] d_active_aw_entry;


reg [7:0] a_bcount,b_bcount,c_bcount,d_bcount;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        a_bcount <= 0; b_bcount <= 0; c_bcount <= 0; d_bcount <= 0;
    end else begin
        if (a_awvalid && a_awready && !(a_bvalid && a_bready)) a_bcount <= a_bcount + 1;
        else if (a_bvalid && a_bready && !(a_awvalid && a_awready)) a_bcount <= a_bcount - 1;

        if (b_awvalid && b_awready && !(b_bvalid && b_bready)) b_bcount <= b_bcount + 1;
        else if (b_bvalid && b_bready && !(b_awvalid && b_awready)) b_bcount <= b_bcount - 1;

        if (c_awvalid && c_awready && !(c_bvalid && c_bready)) c_bcount <= c_bcount + 1;
        else if (c_bvalid && c_bready && !(c_awvalid && c_awready)) c_bcount <= c_bcount - 1;

        if (d_awvalid && d_awready && !(d_bvalid && d_bready)) d_bcount <= d_bcount + 1;
        else if (d_bvalid && d_bready && !(d_awvalid && d_awready)) d_bcount <= d_bcount - 1;
    end
end

wire panic_a_aw_fifo,panic_b_aw_fifo,panic_c_aw_fifo,panic_d_aw_fifo;
wire start_d,start_c,start_b,start_a;
syncfifo #(AWIDE,2) a_aw_fifo (.clk(clk),.rst_n(rst_n),.vldin(a_awvalid && a_awready && !a_aw_full)
    ,.din(new_a_aw_entry)
    ,.empty(a_aw_empty),.full(a_aw_full)
    ,.readout(start_a)
    ,.dout(a_active_aw_entry)
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_a_aw_fifo)
);

syncfifo #(AWIDE,2) b_aw_fifo (.clk(clk),.rst_n(rst_n),.vldin(b_awvalid && b_awready && !b_aw_full)
    ,.din(new_b_aw_entry)
    ,.empty(b_aw_empty),.full(b_aw_full)
    ,.readout(start_b)
    ,.dout(b_active_aw_entry)
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_b_aw_fifo)
);

syncfifo #(AWIDE,2) c_aw_fifo (.clk(clk),.rst_n(rst_n),.vldin(c_awvalid && c_awready && !c_aw_full)
    ,.din(new_c_aw_entry)
    ,.empty(c_aw_empty),.full(c_aw_full)
    ,.readout(start_c)
    ,.dout(c_active_aw_entry)
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_c_aw_fifo)
);
syncfifo #(AWIDE,2) d_aw_fifo (.clk(clk),.rst_n(rst_n),.vldin(d_awvalid && d_awready && !d_aw_full)
    ,.din(new_d_aw_entry)
    ,.empty(d_aw_empty),.full(d_aw_full)
    ,.readout(start_d)
    ,.dout(d_active_aw_entry)
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_d_aw_fifo)
);






wire a_win_fifo_empty,a_win_fifo_full;
wire b_win_fifo_empty,b_win_fifo_full;
wire c_win_fifo_empty,c_win_fifo_full;
wire d_win_fifo_empty,d_win_fifo_full;

wire burst_end = wvalid && wready && wlast;


wire request_a = !a_aw_empty && !a_win_fifo_empty && (a_bcount<8) ;
wire request_b = !b_aw_empty && !b_win_fifo_empty && (b_bcount<8) ;
wire request_c = !c_aw_empty && !c_win_fifo_empty && (c_bcount<8) ;
wire request_d = !d_aw_empty && !d_win_fifo_empty && (d_bcount<8) ;
wire any_start = start_d|| start_c|| start_b|| start_a;

wire [AWIDE+2-1:0] aw_in_entry = 
    start_a ? {2'b00,a_active_aw_entry} :
    start_b ? {2'b01,b_active_aw_entry} :
    start_c ? {2'b10,c_active_aw_entry} :
    start_d ? {2'b11,d_active_aw_entry} :
    0;

wire [AWIDE-1:0] active_aw_entry;
wire aw_fifo_empty,aw_fifo_full;
wire readout_aw_fifo;



wire eligible_a = request_a && !aw_fifo_full ;
wire eligible_b = request_b && !aw_fifo_full ;
wire eligible_c = request_c && !aw_fifo_full ;
wire eligible_d = request_d && !aw_fifo_full ;

// awready && wready : might cause glitches. if changed in the middle of arbitration.

axi_round_robin #(4) rr0 (.clk(clk),.rst_n(rst_n)
    ,.requests({eligible_d,eligible_c,eligible_b,eligible_a})
    ,.grants({start_d,start_c,start_b,start_a})
    ,.pos()
);

wire [1:0] origin;
syncfifo #(AWIDE+2,2) aw_fifo (.clk(clk),.rst_n(rst_n),.vldin(any_start)
    ,.din(aw_in_entry)
    ,.empty(aw_fifo_empty),.full(aw_fifo_full)
    ,.readout(readout_aw_fifo)
    ,.dout({origin,active_aw_entry})
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_aw_fifo)
);

assign awvalid = !aw_fifo_empty;
assign readout_aw_fifo  = awvalid && awready;
assign {awmst, awsize, awextras ,awid,awburst,awlen,awaddr} = active_aw_entry;


wire [1:0] take_from; 
syncfifo #(2,16) rw_fifo (.clk(clk),.rst_n(rst_n),.vldin(readout_aw_fifo)
    ,.din(origin)
    ,.empty(rw_fifo_empty),.full(rw_fifo_full)
    ,.readout(wvalid && wready && wlast)
    ,.dout(take_from)
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_rw_fifo)
);







wire b_out_empty,b_out_full;
assign bready  =  !b_out_full;
wire [IDWID-1:0] inbid;
wire [1:0] inbresp;
wire y_bready;

wire [3:0] inbmst;
wire panic_b_out_fifo;
syncfifo_sampled #(4+IDWID+2,2) b_out_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(bvalid)
    ,.din({bmst,bid,bresp})
    ,.empty(b_out_empty),.full(b_out_full)
    ,.readout(y_bready) ,.dout({inbmst,inbid,inbresp})
    ,.count() ,.softreset(1'b0)
    ,.overflow(panic_b_out_fifo)
);

assign a_bid = inbid;
assign b_bid = inbid;
assign c_bid = inbid;
assign d_bid = inbid;
assign a_bmst = inbmst;
assign b_bmst = inbmst;
assign c_bmst = inbmst;
assign d_bmst = inbmst;

assign a_bresp = inbresp;
assign b_bresp = inbresp;
assign c_bresp = inbresp;
assign d_bresp = inbresp;

assign a_bvalid = !b_out_empty && from_a[inbmst];
assign b_bvalid = !b_out_empty && from_b[inbmst];
assign c_bvalid = !b_out_empty && from_c[inbmst];
assign d_bvalid = !b_out_empty && from_d[inbmst];

assign y_bready = 
    b_out_empty ? 0 :
    a_bvalid ? a_bready :
    b_bvalid ? b_bready :
    c_bvalid ? c_bready :
    d_bvalid ? d_bready :
    0;

wire readout_a_win_fifo = wready && !rw_fifo_empty && (take_from==0) && !a_win_fifo_empty;
wire readout_b_win_fifo = wready && !rw_fifo_empty && (take_from==1) && !b_win_fifo_empty;
wire readout_c_win_fifo = wready && !rw_fifo_empty && (take_from==2) && !c_win_fifo_empty;
wire readout_d_win_fifo = wready && !rw_fifo_empty && (take_from==3) && !d_win_fifo_empty;

wire [DWID+WSTRB+1-1:0] a_wentry;
assign a_wready = !a_win_fifo_full;
syncfifo #(DWID+WSTRB+1,2) a_win_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(a_wvalid && !a_win_fifo_full)
    ,.din({a_wlast,a_wstrb,a_wdata})
    ,.empty(a_win_fifo_empty),.full(a_win_fifo_full)
    ,.readout(readout_a_win_fifo & wready) ,.dout(a_wentry)
    ,.count() ,.softreset(1'b0) ,.overflow()
);

wire [DWID+WSTRB+1-1:0] b_wentry;
assign b_wready = !b_win_fifo_full;
syncfifo #(DWID+WSTRB+1,2) b_win_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(b_wvalid && !b_win_fifo_full)
    ,.din({b_wlast,b_wstrb,b_wdata})
    ,.empty(b_win_fifo_empty),.full(b_win_fifo_full)
    ,.readout(readout_b_win_fifo & wready) ,.dout(b_wentry)
    ,.count() ,.softreset(1'b0) ,.overflow()
);

wire [DWID+WSTRB+1-1:0] c_wentry;
assign c_wready = !c_win_fifo_full;
syncfifo #(DWID+WSTRB+1,2) c_win_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(c_wvalid && !c_win_fifo_full)
    ,.din({c_wlast,c_wstrb,c_wdata})
    ,.empty(c_win_fifo_empty),.full(c_win_fifo_full)
    ,.readout(readout_c_win_fifo & wready) ,.dout(c_wentry)
    ,.count() ,.softreset(1'b0) ,.overflow()
);

wire [DWID+WSTRB+1-1:0] d_wentry;
assign d_wready = !d_win_fifo_full;
syncfifo #(DWID+WSTRB+1,2) d_win_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(d_wvalid && !d_win_fifo_full)
    ,.din({d_wlast,d_wstrb,d_wdata})
    ,.empty(d_win_fifo_empty),.full(d_win_fifo_full)
    ,.readout(readout_d_win_fifo & wready) ,.dout(d_wentry)
    ,.count() ,.softreset(1'b0) ,.overflow()
);


assign {wlast,wstrb,wdata} = 
    readout_a_win_fifo ? a_wentry :
    readout_b_win_fifo ? b_wentry :
    readout_c_win_fifo ? c_wentry :
    readout_d_win_fifo ? d_wentry :
    0;

assign wvalid = readout_a_win_fifo || readout_b_win_fifo || readout_c_win_fifo || readout_d_win_fifo ;




wire panic_acount = (a_bcount==0) && (a_bvalid && a_bready);
wire panic_bcount = (b_bcount==0) && (b_bvalid && b_bready);
wire panic_ccount = (c_bcount==0) && (c_bvalid && c_bready);
wire panic_dcount = (d_bcount==0) && (d_bvalid && d_bready);



wire [63:0]  sign_version = 64'h000d55bd21060424 ;
endmodule


