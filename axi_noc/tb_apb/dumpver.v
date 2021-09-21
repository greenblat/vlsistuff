module axi2apb #( parameter IDWID = 4,parameter DWID = 64,parameter WSTRB = (DIWD / 8)) (
    input [31:0] araddr
    ,input [1:0] arburst
    ,input [3:0] arcache
    ,input [(IDWID - 1):0] arid
    ,input [7:0] arlen
    ,input [2:0] arprot
    ,input [3:0] arqos
    ,output  arready
    ,input [2:0] arsize
    ,input  arvalid
    ,input [31:0] awaddr
    ,input [1:0] awburst
    ,input [3:0] awcache
    ,input [3:0] awid
    ,input [7:0] awlen
    ,input [2:0] awprot
    ,input [3:0] awqos
    ,output  awready
    ,input [2:0] awsize
    ,input  awvalid
    ,output [(IDWID - 1):0] bid
    ,input  bready
    ,output [1:0] bresp
    ,output  bvalid
    ,input  clk
    ,output [31:0] paddr
    ,output reg  penable
    ,input [31:0] prdata
    ,input  pready
    ,input [1:0] presp
    ,output  psel
    ,output [3:0] pstrb
    ,output [31:0] pwdata
    ,output  pwrite
    ,output [(DWID - 1):0] rdata
    ,output [(IDWID - 1):0] rid
    ,output  rlast
    ,input  rready
    ,output [1:0] rresp
    ,input  rst_n
    ,output  rvalid
    ,input [(DWID - 1):0] wdata
    ,input  wlast
    ,output  wready
    ,input [(WSTRB - 1):0] wstrb
    ,input  wvalid
);
localparam AWIDE = (((IDWID + 32) + 8) + 2);
localparam ARIDE = (((IDWID + 2) + 8) + 32);
wire  ar_empty;
wire  aw_empty;
reg  working_r;
reg  working_w;
wire [7:0] work_awlen;
reg [31:0] run_addr;
reg [1:0] run_burst;
reg [8:0] run_len;
wire  run_last;
reg [(IDWID - 1):0] run_rid;
wire [(IDWID - 1):0] work_awid;
wire [7:0] work_arlen;
wire [31:0] work_awaddr;
wire [31:0] work_araddr;
wire [1:0] work_awburst;
wire [(IDWID - 1):0] work_arid;
reg [1:0] work_arburst;
wire  w_full;
wire  r_full;
wire  run_rlast;
wire  pread;
wire [31:0] wrapmask;
wire [31:0] next_addr;
wire [(AWIDE - 1):0] new_aw_entry;
wire  aw_full;
wire [(AWIDE - 1):0] active_aw_entry;
wire  readout_aw_fifo;
wire  b_empty;
wire  b_full;
wire  work_wlast;
wire [(DWID - 1):0] work_wdata;
wire [(WSTRB - 1):0] work_wstrb;
wire  w_empty;
wire  readout_ar_fifo;
wire [(ARIDE - 1):0] new_ar_entry;
wire [(ARIDE - 1):0] active_ar_entry;
wire  ar_full;
wire  pushr;
reg [63:0] lowrdata;
wire  r_empty;
reg [3:0] pstate;
assign   run_last = run_len == 1;
assign   run_rlast = (run_len == 0) && working_r;
assign   pread = (working_r && (!r_full)) && (run_len > 0);
assign   wrapmask = ((work_arlen == 3) ? 32'hffff_ffe0 :
     ((work_arlen == 7) ? 32'hffff_ffc0 :
     ((work_arlen == 15) ? 32'hffff_ff80 :
     ((work_arlen == 31) ? 32'hffff_ff00 : ((work_arlen == 63) ? 32'hffff_fe00 : 32'hffff_fc00)))));
assign   next_addr = ((run_burst == 0) ? run_addr :
     ((run_burst == 1) ? (run_addr 
    + 8) : ((run_burst == 2) ? ((run_addr & wrapmask) 
    + ((run_addr 
    + 8) & (~wrapmask))) : 0)));
assign   new_aw_entry = {awid, awaddr, awlen, awburst};
assign   {work_awid, work_awaddr, work_awlen, work_awburst} = active_aw_entry;
assign   awready = !aw_full;
assign   bresp = 0;
assign   wready = !w_full;
assign   bvalid = !b_empty;
assign   readout_aw_fifo = (pwrite && work_wlast) && working_w;
assign   readout_ar_fifo = (working_r && run_rlast) && pushr;
assign   new_ar_entry = {arid, arburst, arlen, araddr};
assign   arready = !ar_full;
assign   {work_arid, work_arburst, work_arlen, work_araddr} = active_ar_entry;
assign   pushr = (pstate == 3) && pready;
assign   rvalid = !r_empty;
assign   pwrite = ((!aw_empty) && (!w_empty)) && working_w;
assign   paddr = ((pstate == 0) ? run_addr :
     ((pstate == 2) ? (run_addr 
    + 4) :
     ((pstate == 3) ? (run_addr 
    + 4) : ((pstate == 9) ? (run_addr 
    + 4) : ((pstate == 10) ? (run_addr 
    + 4) : run_addr)))));
assign   pwdata = ((pstate == 8) ? work_wdata[31:0] : ((pstate == 10) ? work_wdata[63:32] : work_wdata[31:0]));
assign   pstrb = ((pstate == 8) ? work_wstrb[3:0] : ((pstate == 10) ? work_wstrb[7:4] : 0));
assign   psel = (pread || pwrite) || (pstate > 0);
assign   penable = (((pstate == 1) || (pstate == 3)) || (pstate == 8)) || (pstate == 10);
assign   rresp = presp;
syncfifo_sampled #(AWIDE, 4) aw_fifo (.clk(clk)
    ,.count()
    ,.din(new_aw_entry)
    ,.dout(active_aw_entry)
    ,.empty(aw_empty)
    ,.full(aw_full)
    ,.readout(readout_aw_fifo)
    ,.rst_n(rst_n)
    ,.softreset(1'b0)
    ,.vldin((awvalid && awready)));
syncfifo_sampled #(4, 4) b_fifo (.clk(clk)
    ,.count()
    ,.din(run_rid)
    ,.dout(bid)
    ,.empty(b_empty)
    ,.full(b_full)
    ,.readout(bready)
    ,.rst_n(rst_n)
    ,.softreset(1'b0)
    ,.vldin((run_last && working_w)));
syncfifo_sampled #(73, 4) w_fifo (.clk(clk)
    ,.count()
    ,.din({wlast, wstrb[7:0], wdata[63:0]})
    ,.dout({work_wlast, work_wstrb, work_wdata})
    ,.empty(w_empty)
    ,.full(w_full)
    ,.readout(pwrite)
    ,.rst_n(rst_n)
    ,.softreset(1'b0)
    ,.vldin((wvalid && wready)));
syncfifo_sampled #(ARIDE, 4) ar_fifo (.clk(clk)
    ,.count()
    ,.din(new_ar_entry)
    ,.dout(active_ar_entry)
    ,.empty(ar_empty)
    ,.full(ar_full)
    ,.readout(readout_ar_fifo)
    ,.rst_n(rst_n)
    ,.softreset(1'b0)
    ,.vldin((arvalid && arready)));
syncfifo_sampled #(69, 4) r_fifo (.clk(clk)
    ,.count()
    ,.din({prdata, lowrdata, run_rid, run_rlast})
    ,.dout({rdata, rid, rlast})
    ,.empty(r_empty)
    ,.full(r_full)
    ,.readout(rready)
    ,.rst_n(rst_n)
    ,.softreset(1'b0)
    ,.vldin(pushr));
always @(posedge clk or negedge rst_n) begin
    if(!rst_n) begin
        working_r <= 0;
        working_w <= 0;
        run_addr <= 0;
        run_burst <= 0;
        run_len <= 0;
        run_rid <= 0;
    end else begin
        if((!working_r) && (!working_w)) begin
            if(!ar_empty) begin
                working_r <= 1;
                run_addr <= work_araddr & 32'hffff_fff8;
                run_burst <= work_arburst;
                run_len <= work_arlen + 1;
                run_rid <= work_arid;
            end else if(!aw_empty) begin
                working_w <= 1;
                run_addr <= work_awaddr;
                run_burst <= work_awburst;
                run_len <= work_awlen + 1;
                run_rid <= work_awid;
            end
        end else if(working_r && (!r_full)) begin
            run_addr <= next_addr;
            run_len <= run_len - 1;
            if(pushr && run_rlast) begin
                working_r <= 0;
            end
        end else if(working_w) begin
            run_addr <= next_addr;
            run_len <= run_len - 1;
            if(run_last) begin
                working_w <= 0;
            end
        end
    end
end
always @(posedge clk) begin
    if(pready) begin
        if(pstate == 1) begin
            lowrdata[31:0] <= prdata;
        end
    end
end
always @(posedge clk or negedge rst_n) begin
    if(!rst_n) begin
        pstate <= 0;
    end else begin
        if(pstate == 0) begin
            if(pread) begin
                pstate <= 1;
            end else if(pwrite) begin
                pstate <= 8;
            end
        end else if(pstate == 1) begin
            if(pready) begin
                pstate <= 2;
            end
        end else if(pstate == 2) begin
            if(pready) begin
                pstate <= 3;
            end
        end else if(pstate == 3) begin
            if(pready) begin
                pstate <= 0;
            end
        end else if(pstate == 8) begin
            if(pready) begin
                pstate <= 9;
            end
        end else if(pstate == 9) begin
            if(pready) begin
                pstate <= 10;
            end
        end else if(pstate == 10) begin
            if(pready) begin
                pstate <= 0;
            end
        end
    end
end
endmodule

