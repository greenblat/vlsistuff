


module axi_rd_4_splitter #(parameter EXTRAS=8, parameter IDWID=4, parameter DWID=64)(

    input clk, input rst_n


    ,output [IDWID-1:0] a_arid
    ,output [31:0] a_araddr
    ,output [7:0] a_arlen
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
    ,output [31:0] b_araddr
    ,output [7:0] b_arlen
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
    ,output [31:0] c_araddr
    ,output [7:0] c_arlen
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
    ,output [31:0] d_araddr
    ,output [7:0] d_arlen
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
    ,input [31:0] araddr
    ,input [7:0] arlen
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


localparam ARIDE = IDWID + 32 + 8 + EXTRAS + 2;
wire [ARIDE-1:0] new_ar_entry =   { arid ,araddr ,arlen ,arextras ,arburst };
wire ar_empty,ar_full;
wire [ARIDE-1:0] active_ar_entry;
wire readout_ar_fifo;
syncfifo_sampled #(ARIDE,4) ar_fifo (.clk(clk),.rst_n(rst_n),.vldin(arvalid && arready)
    ,.din(new_ar_entry)
    ,.empty(ar_empty),.full(ar_full)
    ,.readout(readout_ar_fifo)
    ,.dout(active_ar_entry)
    ,.count()
    ,.softreset(1'b0)
);
assign arready = !ar_full;



wire [3:0] work_arid;
wire [31:0] work_araddr;
wire [7:0] work_arlen;
wire [EXTRAS-1:0] work_arextras;
wire [1:0] work_arburst;
assign {work_arid ,work_araddr ,work_arlen ,work_arextras ,work_arburst} = ar_empty ? 0 : active_ar_entry ;
reg working_a,working_b,working_c,working_d;

wire a_start = work_araddr[31:30] == 0;
wire b_start = work_araddr[31:30] == 1;
wire c_start = work_araddr[31:30] == 2;
wire d_start = work_araddr[31:30] == 3;

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


assign a_araddr = {work_araddr[29:0],2'b0};
assign b_araddr = {work_araddr[29:0],2'b0};
assign c_araddr = {work_araddr[29:0],2'b0};
assign d_araddr = {work_araddr[29:0],2'b0};

assign a_arlen = work_arlen;
assign b_arlen = work_arlen;
assign c_arlen = work_arlen;
assign d_arlen = work_arlen;

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



wire r_vldin = a_rvalid || b_rvalid || c_rvalid || d_rvalid;

wire [DWID+4+2+1 -1 : 0] r_new_entry = 
    a_rvalid ? {a_rlast,a_rresp,a_rid,a_rdata} :
    b_rvalid ? {b_rlast,b_rresp,b_rid,b_rdata} :
    c_rvalid ? {c_rlast,c_rresp,c_rid,c_rdata} :
    d_rvalid ? {d_rlast,d_rresp,d_rid,d_rdata} :
    0;

assign a_rready = !r_full;
assign b_rready = !r_full && !a_rvalid;
assign c_rready = !r_full && !a_rvalid && !b_rvalid;
assign d_rready = !r_full && !a_rvalid && !b_rvalid && !c_rvalid ;

syncfifo_sampled #(DWID+4+2+1,8) w_fifo (.clk(clk),.rst_n(rst_n),.vldin(r_vldin)
    ,.din(r_new_entry)
    ,.empty(r_empty),.full(r_full)
    ,.readout(rready)
    ,.dout({rlast,rresp,rid,rdata})
    ,.count()
    ,.softreset(1'b0)
);
assign rvalid = !r_empty;


endmodule




