
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
wire [AWIDE-1:0] new_a_aw_entry =   { a_awid ,a_awaddr ,a_awlen ,a_awextras ,a_awburst };
wire [AWIDE-1:0] new_b_aw_entry =   { b_awid ,b_awaddr ,b_awlen ,b_awextras ,b_awburst };
wire [AWIDE-1:0] new_c_aw_entry =   { c_awid ,c_awaddr ,c_awlen ,c_awextras ,c_awburst };
wire [AWIDE-1:0] new_d_aw_entry =   { d_awid ,d_awaddr ,d_awlen ,d_awextras ,d_awburst };

wire [AWIDE-1:0] a_active_aw_entry;
wire [AWIDE-1:0] b_active_aw_entry;
wire [AWIDE-1:0] c_active_aw_entry;
wire [AWIDE-1:0] d_active_aw_entry;

wire readout_a_aw_fifo,readout_b_aw_fifo,readout_c_aw_fifo,readout_d_aw_fifo;

reg [7:0] a_b_count,b_b_count,c_b_count,d_b_count;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        a_b_count <= 0;
        b_b_count <= 0;
        c_b_count <= 0;
        d_b_count <= 0;
    end else begin

        if (a_awvalid && a_awready && !(a_bvalid && a_bready)) a_b_count <= a_b_count + 1;
        else if (a_bvalid && a_bready && !(a_awvalid && a_awready)) a_b_count <= a_b_count - 1;

        if (awready && readout_b_aw_fifo && !(b_bvalid && b_bready)) b_b_count <= b_b_count + 1;
        else if (b_bvalid && b_bready && !(awready && readout_b_aw_fifo)) b_b_count <= b_b_count - 1;

        if (awready && readout_c_aw_fifo && !(c_bvalid && c_bready)) c_b_count <= c_b_count + 1;
        else if (c_bvalid && c_bready && !(awready && readout_c_aw_fifo)) c_b_count <= c_b_count - 1;

        if (awready && readout_d_aw_fifo && !(d_bvalid && d_bready)) d_b_count <= d_b_count + 1;
        else if (d_bvalid && d_bready && !(awready && readout_d_aw_fifo)) d_b_count <= d_b_count - 1;

    end
end


syncfifo_sampled #(AWIDE,4) a_aw_fifo (.clk(clk),.rst_n(rst_n),.vldin(a_awvalid && a_awready)
    ,.din(new_a_aw_entry)
    ,.empty(a_aw_empty),.full(a_aw_full)
    ,.readout(readout_a_aw_fifo)
    ,.dout(a_active_aw_entry)
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_a_aw_fifo)
);

syncfifo #(AWIDE,2) b_aw_fifo (.clk(clk),.rst_n(rst_n),.vldin(b_awvalid && b_awready)
    ,.din(new_b_aw_entry)
    ,.empty(b_aw_empty),.full(b_aw_full)
    ,.readout(readout_b_aw_fifo)
    ,.dout(b_active_aw_entry)
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_b_aw_fifo)
);
syncfifo #(AWIDE,2) c_aw_fifo (.clk(clk),.rst_n(rst_n),.vldin(c_awvalid && c_awready)
    ,.din(new_c_aw_entry)
    ,.empty(c_aw_empty),.full(c_aw_full)
    ,.readout(readout_c_aw_fifo)
    ,.dout(c_active_aw_entry)
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_c_aw_fifo)
);
syncfifo #(AWIDE,2) d_aw_fifo (.clk(clk),.rst_n(rst_n),.vldin(d_awvalid && d_awready)
    ,.din(new_d_aw_entry)
    ,.empty(d_aw_empty),.full(d_aw_full)
    ,.readout(readout_d_aw_fifo)
    ,.dout(d_active_aw_entry)
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_d_aw_fifo)
);

wire working_a,working_b,working_c,working_d;
wire [3:0] workings;
syncfifo #(4,4) work_aw_fifo (.clk(clk),.rst_n(rst_n),.vldin(awvalid && awready)
    ,.din({readout_d_aw_fifo,readout_c_aw_fifo,readout_b_aw_fifo,readout_a_aw_fifo})
    ,.empty(work_aw_empty),.full(work_aw_full)
    ,.readout(wvalid && wready && wlast)
    ,.dout(workings[3:0])
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_work_aw_fifo)
);
assign {working_d,working_c,working_b,working_a} = work_aw_empty ? 0 : workings;




// wire finished_transaction;
//wire idling =  !working_a && !working_b && !working_c && !working_d;
//always @(posedge clk or negedge rst_n) begin
//    if (!rst_n) begin
//        working_a <= 0;
//        working_b <= 0;
//        working_c <= 0;
//        working_d <= 0;
//    end else begin
//        if (!a_aw_empty && idling) begin
//            working_a <= 1;
//        end else if (!b_aw_empty && idling) begin
//            working_b <= 1;
//        end else if (!c_aw_empty && idling) begin
//            working_c <= 1;
//        end else if (!d_aw_empty && idling) begin
//            working_d <= 1;
//        end else if (working_a) begin
//            if (finished_transaction) begin
//                working_a <= 0;
//            end
//        end else if (working_b) begin
//            if (finished_transaction) begin
//                working_b <= 0;
//            end
//        end else if (working_c) begin
//            if (finished_transaction) begin
//                working_c <= 0;
//            end
//        end else if (working_d) begin
//            if (finished_transaction) begin
//                working_d <= 0;
//            end
//        end
//    end
//end

wire [3:0] orig_wid;
assign {orig_wid ,awaddr ,awlen ,awextras ,awburst} = 
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


//wire bs_are_full = a_b_full || b_b_full || c_b_full || d_b_full;
wire bs_are_full = (a_b_count>=8) || b_b_full || c_b_full || d_b_full;
assign readout_a_aw_fifo = !work_aw_full && awready && (a_b_count<8) && !a_aw_empty;
assign readout_b_aw_fifo = !work_aw_full && awready && (b_b_count<8) && a_aw_empty && !b_aw_empty;
assign readout_c_aw_fifo = !work_aw_full && awready && (c_b_count<8) && a_aw_empty && b_aw_empty && !c_aw_empty;
assign readout_d_aw_fifo = !work_aw_full && awready && (d_b_count<8) && a_aw_empty && b_aw_empty && c_aw_empty && !d_aw_empty;

wire working = working_a || working_b || working_c || working_d;
// assign finished_transaction = wready && wvalid && wlast && working;

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
    (inbid==1) ? a_bready :
    (inbid==2) ? b_bready :
    (inbid==3) ? c_bready :
    (inbid==4) ? d_bready :
    0;




wire [DWID-1:0] x_wdata   = working_a ? a_wdata   : working_b ? b_wdata : working_c ? c_wdata : d_wdata ;
wire [WSTRB-1:0] x_wstrb   = working_a ? a_wstrb   : working_b ? b_wstrb : working_c ? c_wstrb : d_wstrb ;
wire x_wlast   = 
      working_a ? a_wlast
    : working_b ? b_wlast
    : working_c ? c_wlast
    : working_d ? d_wlast : 0 ;

wire x_wvalid  = ( 
       (working_a && a_wvalid)  
    || (working_b && b_wvalid) 
    || (working_c && c_wvalid)
    || (working_d && d_wvalid)
);

wire d_out_empty,d_out_full;
wire x_wready = !d_out_full; 
assign a_wready  = working_a ? x_wready :  0;
assign b_wready  = working_b ? x_wready :  0;
assign c_wready  = working_c ? x_wready :  0;
assign d_wready  = working_d ? x_wready :  0;

assign awvalid = readout_a_aw_fifo || readout_b_aw_fifo || readout_c_aw_fifo || readout_d_aw_fifo;


syncfifo_sampled #(DWID+WSTRB+1,2) d_out_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(x_wvalid && !d_out_full)
    ,.din({x_wdata,x_wlast,x_wstrb})
    ,.empty(d_out_empty),.full(d_out_full)
    ,.readout(wready) ,.dout({wdata,wlast,wstrb})
    ,.count() ,.softreset(1'b0)
    ,.overflow(panic_d_out_fifo)
);

assign wvalid = !d_out_empty; 

reg [4:0] outstanding_ws;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        outstanding_ws <= 16;
    end  else begin
        if (awvalid && awready && !(wvalid && wlast && wready))
            outstanding_ws <= outstanding_ws - 1;
        else if (!(awvalid && awready) && (wvalid && wlast && wready))
            outstanding_ws <= outstanding_ws + 1;
    end
end

endmodule


