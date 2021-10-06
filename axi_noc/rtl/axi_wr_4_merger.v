
module axi_wr_4_merger #(parameter IDWID=4, parameter DWID=64, parameter WSTRB=DWID/8, parameter EXTRAS=8) (
    input clk, input rst_n


    ,input [IDWID-1:0] a_awid
    ,input [31:0] a_awaddr
    ,input [7:0] a_awlen
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
    ,input [31:0] b_awaddr
    ,input [7:0] b_awlen
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
    ,input [31:0] c_awaddr
    ,input [7:0] c_awlen
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
    ,input [31:0] d_awaddr
    ,input [7:0] d_awlen
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
    ,output [31:0] awaddr
    ,output [7:0] awlen
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

localparam AWIDE = IDWID + 32 + 8 + EXTRAS + 2 ;
wire [AWIDE-1:0] new_a_aw_entry =   { a_awextras ,a_awid, a_awburst, a_awlen, a_awaddr };
wire [AWIDE-1:0] new_b_aw_entry =   { b_awextras ,b_awid, b_awburst, b_awlen, b_awaddr };
wire [AWIDE-1:0] new_c_aw_entry =   { c_awextras ,c_awid, c_awburst, c_awlen, c_awaddr };
wire [AWIDE-1:0] new_d_aw_entry =   { d_awextras ,d_awid, d_awburst, d_awlen, d_awaddr };

wire [AWIDE-1:0] a_active_aw_entry;
wire [AWIDE-1:0] b_active_aw_entry;
wire [AWIDE-1:0] c_active_aw_entry;
wire [AWIDE-1:0] d_active_aw_entry;

wire readout_a_aw_fifo,readout_b_aw_fifo,readout_c_aw_fifo,readout_d_aw_fifo;

reg [7:0] a_bcount,b_bcount,c_bcount,d_bcount;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        a_bcount <= 0;
        b_bcount <= 0;
        c_bcount <= 0;
        d_bcount <= 0;
    end else begin

        if (a_awvalid && a_awready && !(a_bvalid && a_bready)) a_bcount <= a_bcount + 1;
        else if (a_bvalid && a_bready && !(a_awvalid && a_awready)) a_bcount <= a_bcount - 1;

        if (awready && readout_b_aw_fifo && !(b_bvalid && b_bready)) b_bcount <= b_bcount + 1;
        else if (b_bvalid && b_bready && !(awready && readout_b_aw_fifo)) b_bcount <= b_bcount - 1;

        if (awready && readout_c_aw_fifo && !(c_bvalid && c_bready)) c_bcount <= c_bcount + 1;
        else if (c_bvalid && c_bready && !(awready && readout_c_aw_fifo)) c_bcount <= c_bcount - 1;

        if (awready && readout_d_aw_fifo && !(d_bvalid && d_bready)) d_bcount <= d_bcount + 1;
        else if (d_bvalid && d_bready && !(awready && readout_d_aw_fifo)) d_bcount <= d_bcount - 1;

    end
end


syncfifo #(AWIDE,2) a_aw_fifo (.clk(clk),.rst_n(rst_n),.vldin(a_awvalid && a_awready && !a_aw_full)
    ,.din(new_a_aw_entry)
    ,.empty(a_aw_empty),.full(a_aw_full)
    ,.readout(readout_a_aw_fifo)
    ,.dout(a_active_aw_entry)
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_a_aw_fifo)
);

syncfifo #(AWIDE,2) b_aw_fifo (.clk(clk),.rst_n(rst_n),.vldin(b_awvalid && b_awready && !b_aw_full)
    ,.din(new_b_aw_entry)
    ,.empty(b_aw_empty),.full(b_aw_full)
    ,.readout(readout_b_aw_fifo)
    ,.dout(b_active_aw_entry)
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_b_aw_fifo)
);
syncfifo #(AWIDE,2) c_aw_fifo (.clk(clk),.rst_n(rst_n),.vldin(c_awvalid && c_awready && !c_aw_full)
    ,.din(new_c_aw_entry)
    ,.empty(c_aw_empty),.full(c_aw_full)
    ,.readout(readout_c_aw_fifo)
    ,.dout(c_active_aw_entry)
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_c_aw_fifo)
);
syncfifo #(AWIDE,2) d_aw_fifo (.clk(clk),.rst_n(rst_n),.vldin(d_awvalid && d_awready && !d_aw_full)
    ,.din(new_d_aw_entry)
    ,.empty(d_aw_empty),.full(d_aw_full)
    ,.readout(readout_d_aw_fifo)
    ,.dout(d_active_aw_entry)
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_d_aw_fifo)
);

reg working_a,working_b,working_c,working_d;
wire burst_end = wvalid && wready && wlast;

wire eligible_a = !a_aw_empty && !a_win_fifo_empty;
wire eligible_b = !b_aw_empty && !b_win_fifo_empty;
wire eligible_c = !c_aw_empty && !c_win_fifo_empty;
wire eligible_d = !d_aw_empty && !d_win_fifo_empty;

wire all_idle = !working_a && !working_b && !working_c && !working_d;
wire a_winner,b_winner,c_winner,d_winner;
wire start_a = eligible_a && (all_idle) && awready && wready && (a_bcount<8) && a_winner;
wire start_b = eligible_b && (all_idle) && awready && wready && (b_bcount<8) && b_winner;
wire start_c = eligible_c && (all_idle) && awready && wready && (c_bcount<8) && c_winner;
wire start_d = eligible_d && (all_idle) && awready && wready && (d_bcount<8) && d_winner;

wire longer_a = a_active_aw_entry[7+32:32] != 0;
wire longer_b = b_active_aw_entry[7+32:32] != 0;
wire longer_c = c_active_aw_entry[7+32:32] != 0;
wire longer_d = d_active_aw_entry[7+32:32] != 0;


always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        working_a <=0; working_b <=0; working_c <=0; working_d <=0; 
    end else begin
        if (start_a) begin
            working_a <= longer_a; working_b <= 0; working_c <= 0; working_d <= 0;
        end else if (start_b) begin
            working_a <= 0; working_b <= longer_b; working_c <= 0; working_d <= 0;
        end else if (start_c) begin
            working_a <= 0; working_b <= 0; working_c <= longer_c; working_d <= 0;
        end else if (start_d) begin
            working_a <= 0; working_b <= 0; working_c <= 0; working_d <= longer_d;
        end else if (burst_end) begin
            working_a <= 0; working_b <= 0; working_c <= 0; working_d <= 0;
        end
    end
end
        



assign readout_a_aw_fifo =  start_a;
assign readout_b_aw_fifo =  start_b && !start_a;
assign readout_c_aw_fifo =  start_c && !start_b && !start_a;
assign readout_d_aw_fifo =  start_d && !start_c && !start_b && !start_a;


wire [7:0] a_pri_count,v_pri_count,c_pri_count,d_pri_count;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        a_pri_count <= 0;v_pri_count <= 0;c_pri_count <= 0;d_pri_count <= 0;
    end else begin
        if (readout_a_aw_fifo) 
            a_pri_count <= 0;
        else if (eligible_a) 
            a_pri_count <= a_pri_count + (a_pri_count<255);

        if (readout_b_aw_fifo) 
            b_pri_count <= 0;
        else if (eligible_a) 
            b_pri_count <= b_pri_count + (b_pri_count<255);

        if (readout_c_aw_fifo) 
            c_pri_count <= 0;
        else if (eligible_a) 
            c_pri_count <= c_pri_count + (c_pri_count<255);

        if (readout_d_aw_fifo) 
            d_pri_count <= 0;
        else if (eligible_a) 
            d_pri_count <= d_pri_count + (d_pri_count<255);
        else 
            d_pri_count <= 0;
    end
end

wire a_greater_than_b = a_pri_count >= b_pri_count;

wire a_greater_than_c = a_pri_count >= c_pri_count;
wire a_greater_than_d = a_pri_count >= d_pri_count;

wire b_greater_than_c = b_pri_count >= c_pri_count;
wire b_greater_than_d = b_pri_count >= d_pri_count;

wire c_greater_than_d = c_pri_count >= d_pri_count;

assign a_winner = (a_pri_count>0) && a_greater_than_b && a_greater_than_c && a_greater_than_d ;
assign b_winner = (b_pri_count>0) && !a_winner  && b_greater_than_c && b_greater_than_d ;
assign c_winner = (c_pri_count>0) && !a_winner && !b_winner && c_greater_than_d ;
assign d_winner = (d_pri_count>0) && !a_winner && !b_winner && !c_winner;


wire [3:0] orig_wid;
assign {awextras ,orig_wid,awburst,awlen,awaddr} = 
    (readout_a_aw_fifo) ? a_active_aw_entry :
    (readout_b_aw_fifo) ? b_active_aw_entry :
    (readout_c_aw_fifo) ? c_active_aw_entry :
    (readout_d_aw_fifo) ? d_active_aw_entry :
    0;

assign awid = 
    (readout_a_aw_fifo) ? 1 :
    (readout_b_aw_fifo) ? 2 :
    (readout_c_aw_fifo) ? 3 :
    (readout_d_aw_fifo) ? 4 :
    0;

wire a_win_fifo_empty,a_win_fifo_full;
wire b_win_fifo_empty,b_win_fifo_full;
wire c_win_fifo_empty,c_win_fifo_full;
wire d_win_fifo_empty,d_win_fifo_full;


wire panic_readout = (0+readout_a_aw_fifo+readout_b_aw_fifo+readout_c_aw_fifo+readout_d_aw_fifo)>1;

wire [IDWID-1:0] x_a_bid,x_b_bid,x_c_bid,x_d_bid;
syncfifo_sampled #(IDWID,8) a_b_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(readout_a_aw_fifo)
    ,.din(orig_wid)
    ,.empty(a_b_empty),.full(a_b_full)
    ,.readout(bvalid && (bid==1)) ,.dout(x_a_bid)
    ,.count() ,.softreset(1'b0)
    ,.overflow(panic_a_b_fifo)
);

syncfifo_sampled #(IDWID,8) b_b_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(readout_b_aw_fifo)
    ,.din(orig_wid)
    ,.empty(b_b_empty),.full(b_b_full)
    ,.readout(bvalid && (bid==2)) ,.dout(x_b_bid)
    ,.count() ,.softreset(1'b0)
    ,.overflow(panic_b_b_fifo)
);

syncfifo_sampled #(IDWID,8) c_b_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(readout_c_aw_fifo)
    ,.din(orig_wid)
    ,.empty(c_b_empty),.full(c_b_full)
    ,.readout(bvalid && (bid==3)) ,.dout(x_c_bid)
    ,.count() ,.softreset(1'b0)
    ,.overflow(panic_c_b_fifo)
);
syncfifo_sampled #(IDWID,8) d_b_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(readout_d_aw_fifo)
    ,.din(orig_wid)
    ,.empty(d_b_empty),.full(d_b_full)
    ,.readout(bvalid && (bid==4)) ,.dout(x_d_bid)
    ,.count() ,.softreset(1'b0)
    ,.overflow(panic_d_b_fifo)
);


wire b_out_empty,b_out_full;
assign bready  =  !b_out_full;
wire [IDWID-1:0] inbid;
wire [1:0] inbresp;
wire y_bready;
wire [IDWID-1:0] x_bid = 
    (bid==1) ? x_a_bid : 
    (bid==2) ? x_b_bid : 
    (bid==3) ? x_c_bid : 
    (bid==4) ? x_d_bid : 
    0;


wire [IDWID-1:0] y_bid;

syncfifo_sampled #(IDWID+IDWID+2,2) b_out_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(bvalid)
    ,.din({x_bid,bid,bresp})
    ,.empty(b_out_empty),.full(b_out_full)
    ,.readout(y_bready) ,.dout({y_bid,inbid,inbresp})
    ,.count() ,.softreset(1'b0)
    ,.overflow(panic_b_out_fifo)
);

assign a_bid = y_bid;
assign b_bid = y_bid;
assign c_bid = y_bid;
assign d_bid = y_bid;

assign a_bresp = inbresp;
assign b_bresp = inbresp;
assign c_bresp = inbresp;
assign d_bresp = inbresp;

assign a_bvalid = !b_out_empty && (inbid==1);
assign b_bvalid = !b_out_empty && (inbid==2);
assign c_bvalid = !b_out_empty && (inbid==3);
assign d_bvalid = !b_out_empty && (inbid==4);

assign y_bready = 
    b_out_empty ? 0 :
    (inbid==1) ? a_bready :
    (inbid==2) ? b_bready :
    (inbid==3) ? c_bready :
    (inbid==4) ? d_bready :
    0;

wire readout_a_win_fifo = wready && (readout_a_aw_fifo || working_a)  && !a_win_fifo_empty;
wire readout_b_win_fifo = wready && (readout_b_aw_fifo || working_b) && !b_win_fifo_empty;
wire readout_c_win_fifo = wready && (readout_c_aw_fifo || working_c) && !c_win_fifo_empty;
wire readout_d_win_fifo = wready && (readout_d_aw_fifo || working_d) && !d_win_fifo_empty;

wire [DWID+WSTRB+1-1:0] a_wentry;
assign a_wready = !a_win_fifo_full;
syncfifo #(DWID+WSTRB+1,2) a_win_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(a_wvalid && !a_win_fifo_full)
    ,.din({a_wlast,a_wstrb,a_wdata})
    ,.empty(a_win_fifo_empty),.full(a_win_fifo_full)
    ,.readout(readout_a_win_fifo) ,.dout(a_wentry)
    ,.count() ,.softreset(1'b0) ,.overflow()
);

wire [DWID+WSTRB+1-1:0] b_wentry;
assign b_wready = !b_win_fifo_full;
syncfifo #(DWID+WSTRB+1,2) b_win_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(b_wvalid && !b_win_fifo_full)
    ,.din({b_wlast,b_wstrb,b_wdata})
    ,.empty(b_win_fifo_empty),.full(b_win_fifo_full)
    ,.readout(readout_b_win_fifo) ,.dout(b_wentry)
    ,.count() ,.softreset(1'b0) ,.overflow()
);

wire [DWID+WSTRB+1-1:0] c_wentry;
assign c_wready = !c_win_fifo_full;
syncfifo #(DWID+WSTRB+1,2) c_win_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(c_wvalid && !c_win_fifo_full)
    ,.din({c_wlast,c_wstrb,c_wdata})
    ,.empty(c_win_fifo_empty),.full(c_win_fifo_full)
    ,.readout(readout_c_win_fifo) ,.dout(c_wentry)
    ,.count() ,.softreset(1'b0) ,.overflow()
);


wire [DWID+WSTRB+1-1:0] d_wentry;
assign d_wready = !d_win_fifo_full;
syncfifo #(DWID+WSTRB+1,2) d_win_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(d_wvalid && !d_win_fifo_full)
    ,.din({d_wlast,d_wstrb,d_wdata})
    ,.empty(d_win_fifo_empty),.full(d_win_fifo_full)
    ,.readout(readout_d_win_fifo) ,.dout(d_wentry)
    ,.count() ,.softreset(1'b0) ,.overflow()
);



assign {wlast,wstrb,wdata} = 
    readout_a_win_fifo ? a_wentry :
    readout_b_win_fifo ? b_wentry :
    readout_c_win_fifo ? c_wentry :
    readout_d_win_fifo ? d_wentry :
    0;

assign wvalid = readout_a_win_fifo || readout_b_win_fifo || readout_c_win_fifo || readout_d_win_fifo;

assign awvalid = readout_a_aw_fifo || readout_b_aw_fifo || readout_c_aw_fifo || readout_d_aw_fifo;



wire panic_acount = (a_bcount==0) && (a_bvalid && a_bready);
wire panic_bcount = (b_bcount==0) && (b_bvalid && b_bready);
wire panic_ccount = (c_bcount==0) && (c_bvalid && c_bready);
wire panic_dcount = (d_bcount==0) && (d_bvalid && d_bready);



endmodule


