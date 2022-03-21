


module axi_rd_4_splitter #(parameter AWID=32,parameter EXTRAS=8, parameter IDWID=4, parameter DWID=64)(

    input clk, input rst_n


    ,output [IDWID-1:0] a_arid
    ,output [AWID-1:0] a_araddr
    ,output [7:0] a_arlen
    ,output [2:0] a_arsize
    ,output [EXTRAS-1:0] a_arextras
    ,output [1:0] a_arburst
    ,output a_arvalid
    ,input a_arready
    ,input [IDWID-1:0] a_rid
    ,input [DWID-1:0] a_rdata
    ,input [1:0] a_rresp
    ,input a_rlast
    ,input a_rvalid
    ,output a_rready



    ,output [IDWID-1:0] b_arid
    ,output [AWID-1:0] b_araddr
    ,output [7:0] b_arlen
    ,output [2:0] b_arsize
    ,output [EXTRAS-1:0] b_arextras
    ,output [1:0] b_arburst
    ,output b_arvalid
    ,input b_arready
    ,input [IDWID-1:0] b_rid
    ,input [DWID-1:0] b_rdata
    ,input [1:0] b_rresp
    ,input b_rlast
    ,input b_rvalid
    ,output b_rready


    ,output [IDWID-1:0] c_arid
    ,output [AWID-1:0] c_araddr
    ,output [7:0] c_arlen
    ,output [2:0] c_arsize
    ,output [EXTRAS-1:0] c_arextras
    ,output [1:0] c_arburst
    ,output c_arvalid
    ,input c_arready
    ,input [IDWID-1:0] c_rid
    ,input [DWID-1:0] c_rdata
    ,input [1:0] c_rresp
    ,input c_rlast
    ,input c_rvalid
    ,output c_rready

    ,output [IDWID-1:0] d_arid
    ,output [AWID-1:0] d_araddr
    ,output [7:0] d_arlen
    ,output [2:0] d_arsize
    ,output [EXTRAS-1:0] d_arextras
    ,output [1:0] d_arburst
    ,output d_arvalid
    ,input d_arready
    ,input [IDWID-1:0] d_rid
    ,input [DWID-1:0] d_rdata
    ,input [1:0] d_rresp
    ,input d_rlast
    ,input d_rvalid
    ,output d_rready



    ,input [IDWID-1:0] arid
    ,input [AWID-1:0] araddr
    ,input [7:0] arlen
    ,input [2:0] arsize
    ,input [EXTRAS-1:0] arextras
    ,input [1:0] arburst
    ,input arvalid
    ,output arready
    ,output [IDWID-1:0] rid
    ,output [DWID-1:0] rdata
    ,output [1:0] rresp
    ,output rlast
    ,output rvalid
    ,input rready
);


localparam ARIDE = 3 + IDWID + AWID + 8 + EXTRAS + 2;
wire [ARIDE-1:0] new_ar_entry =   { arsize, arid ,araddr ,arlen ,arextras ,arburst };
wire ar_empty,ar_full,r_full,a_r_full,b_r_full,c_r_full,d_r_full;
wire [ARIDE-1:0] active_ar_entry;
wire readout_ar_fifo;
syncfifo_sampled #(ARIDE,4) ar_fifo (.clk(clk),.rst_n(rst_n),.vldin(arvalid && arready)
    ,.din(new_ar_entry)
    ,.empty(ar_empty),.full(ar_full)
    ,.readout(readout_ar_fifo)
    ,.dout(active_ar_entry)
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_ar_fifo)
);
assign arready = !ar_full;



wire [3:0] work_arid;
wire [AWID-1:0] work_araddr;
wire [7:0] work_arlen;
wire [EXTRAS-1:0] work_arextras;
wire [1:0] work_arburst;
wire [3:0] work_arsize;
assign {work_arsize, work_arid ,work_araddr ,work_arlen ,work_arextras ,work_arburst} = ar_empty ? 0 : active_ar_entry ;

wire a_start = work_araddr[AWID-1:AWID-2] == 0;
wire b_start = work_araddr[AWID-1:AWID-2] == 1;
wire c_start = work_araddr[AWID-1:AWID-2] == 2;
wire d_start = work_araddr[AWID-1:AWID-2] == 3;

assign readout_ar_fifo = !ar_empty && (
    (a_start && a_arready) ||
    (b_start && b_arready) ||
    (c_start && c_arready) ||
    (d_start && d_arready)
);
assign a_arvalid = a_start && !ar_empty ;
assign b_arvalid = b_start && !ar_empty ;
assign c_arvalid = c_start && !ar_empty ;
assign d_arvalid = d_start && !ar_empty ;


assign a_araddr = {work_araddr[AWID-3:0],2'b0};
assign b_araddr = {work_araddr[AWID-3:0],2'b0};
assign c_araddr = {work_araddr[AWID-3:0],2'b0};
assign d_araddr = {work_araddr[AWID-3:0],2'b0};

assign a_arlen = work_arlen;
assign b_arlen = work_arlen;
assign c_arlen = work_arlen;
assign d_arlen = work_arlen;

assign a_arsize = work_arsize;
assign b_arsize = work_arsize;
assign c_arsize = work_arsize;
assign d_arsize = work_arsize;

assign a_arextras = work_arextras;
assign b_arextras = work_arextras;
assign c_arextras = work_arextras;
assign d_arextras = work_arextras;

assign a_arburst = work_arburst;
assign b_arburst = work_arburst;
assign c_arburst = work_arburst;
assign d_arburst = work_arburst;

assign a_arid = work_arid;
assign b_arid = work_arid;
assign c_arid = work_arid;
assign d_arid = work_arid;

wire back_r_empty,back_r_full;
wire [1:0] back_r;
wire back_rtaken;
syncfifo #(2,6) back_r_fifo (.clk(clk),.rst_n(rst_n),.vldin(readout_ar_fifo)
    ,.din(work_araddr[AWID-1:AWID-2])
    ,.empty(back_r_empty),.full(back_r_full)
    ,.readout(back_rtaken)
    ,.dout(back_r)
    ,.count() ,.softreset(1'b0) ,.overflow()
);


wire [DWID+4+2+1 - 1:0] a_r_new_entry,b_r_new_entry,c_r_new_entry,d_r_new_entry;
wire a_rtaken,b_rtaken,c_rtaken,d_rtaken;
syncfifo #(DWID+4+2+1,2) a_r_fifo (.clk(clk),.rst_n(rst_n),.vldin(a_rvalid && a_rready)
    ,.din({a_rlast,a_rresp,a_rid,a_rdata})
    ,.empty(a_r_empty),.full(a_r_full)
    ,.readout(a_rtaken)
    ,.dout(a_r_new_entry)
    ,.count() ,.softreset(1'b0) ,.overflow()
);
syncfifo #(DWID+4+2+1,2) b_r_fifo (.clk(clk),.rst_n(rst_n),.vldin(b_rvalid && b_rready)
    ,.din({b_rlast,b_rresp,b_rid,b_rdata})
    ,.empty(b_r_empty),.full(b_r_full)
    ,.readout(b_rtaken)
    ,.dout(b_r_new_entry)
    ,.count() ,.softreset(1'b0) ,.overflow()
);
syncfifo #(DWID+4+2+1,2) c_r_fifo (.clk(clk),.rst_n(rst_n),.vldin(c_rvalid && c_rready)
    ,.din({c_rlast,c_rresp,c_rid,c_rdata})
    ,.empty(c_r_empty),.full(c_r_full)
    ,.readout(c_rtaken)
    ,.dout(c_r_new_entry)
    ,.count() ,.softreset(1'b0) ,.overflow()
);
syncfifo #(DWID+4+2+1,2) d_r_fifo (.clk(clk),.rst_n(rst_n),.vldin(d_rvalid && d_rready)
    ,.din({d_rlast,d_rresp,d_rid,d_rdata})
    ,.empty(d_r_empty),.full(d_r_full)
    ,.readout(d_rtaken)
    ,.dout(d_r_new_entry)
    ,.count() ,.softreset(1'b0) ,.overflow()
);

assign a_rready = !a_r_full;
assign b_rready = !b_r_full;
assign c_rready = !c_r_full;
assign d_rready = !d_r_full;






wire r_vldin = !a_r_empty || !b_r_empty || !c_r_empty || !d_r_empty;


wire [DWID+4+2+1 -1 : 0] r_new_entry = 
    ((back_r == 0) && !a_r_empty) ? a_r_new_entry :
    ((back_r == 1) && !b_r_empty) ? b_r_new_entry :
    ((back_r == 2) && !c_r_empty) ? c_r_new_entry :
    ((back_r == 3) && !d_r_empty) ? d_r_new_entry :
    0;

assign a_rtaken = (back_r == 0) && !r_full && !a_r_empty;
assign b_rtaken = (back_r == 1) && !r_full && !b_r_empty;
assign c_rtaken = (back_r == 2) && !r_full && !c_r_empty;
assign d_rtaken = (back_r == 3) && !r_full && !d_r_empty;

assign back_rtaken = r_vldin && r_new_entry[DWID+4+2+1-1] && !r_full;
syncfifo #(DWID+4+2+1,4) r_fifo (.clk(clk),.rst_n(rst_n),.vldin(r_vldin)
    ,.din(r_new_entry)
    ,.empty(r_empty),.full(r_full)
    ,.readout(rready && !r_empty)
    ,.dout({rlast,rresp,rid,rdata})
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_r_fifo)
);

assign rvalid = !r_empty;


endmodule




