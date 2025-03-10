// add address generator;


module axi2ram #(parameter AWID=32,parameter IDWID=4,parameter DWID=64, parameter WSTRB=DWID/8, parameter RAMSIZE=16)(

    input clk, input rst_n


    ,input [IDWID-1:0] arid
    ,input [AWID-1:0] araddr
    ,input [7:0] arlen
    ,input [2:0] arsize
    ,input [1:0] arburst
    ,input arvalid
    ,output arready
    ,output [IDWID-1:0] rid
    ,output [DWID-1:0] rdata
    ,output [1:0] rresp
    ,output rlast
    ,output rvalid
    ,input rready

    ,input [3:0] awid
    ,input [AWID-1:0] awaddr
    ,input [7:0] awlen
    ,input [2:0] awsize
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


    
wire ar_empty,aw_empty;
reg working_r,working_w;

wire [7:0] work_awlen;
wire [2:0] work_awsize;
reg [AWID-1:0] run_addr;
reg [1:0] run_burst;
reg [8:0] run_len;
reg [2:0] run_size;
wire run_last = run_len == 1;
reg [IDWID-1:0] run_id;
wire [IDWID-1:0] work_awid;
wire [7:0] work_arlen;
wire [2:0] work_arsize;
wire [AWID-1:0] work_awaddr,work_araddr;
wire [1:0] work_awburst;
wire [IDWID-1:0] work_arid;
reg [1:0] work_arburst;
wire w_full;
wire r_full;
wire run_rlast = (run_len == 0) && working_r;
wire pread = working_r && !r_full && (run_len>0);


wire [31:0] wrapmask = 
    (work_arlen == 3) ? 32'hffff_ffe0 :
    (work_arlen == 7) ? 32'hffff_ffc0 :
    (work_arlen ==15) ? 32'hffff_ff80 :
    (work_arlen ==31) ? 32'hffff_ff00 :
    (work_arlen ==63) ? 32'hffff_fe00 :
    32'hffff_fc00 ;

wire [3:0] addr_jump = 
    (run_size == 0) ? 1 :
    (run_size == 1) ? 2 :
    (run_size == 2) ? 4 :
    (run_size == 3) ? 8 : 0;

wire [AWID-1:0] next_addr = 
    (run_burst == 0) ? run_addr :
    (run_burst == 1) ? (run_addr+8) :
    (run_burst == 2) ? (run_addr & wrapmask) + ((run_addr + 8) & ~wrapmask) :
    0;


always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        working_r <= 0;
        working_w <= 0;
        run_addr <= 0;
        run_burst <= 0;
        run_len <= 0;
        run_size <= 0;
        run_id <= 0;
    end else begin
        if (!working_r && !working_w) begin
            if (!ar_empty) begin
                working_r <= 1;
                run_addr <= work_araddr & 32'hffff_fff8;
                run_burst <= work_arburst;
                run_len <= work_arlen+1;
                run_size <= work_arsize;
                run_id <= work_arid;
            end else if (!aw_empty) begin
                working_w <= 1;
                run_addr <= work_awaddr;
                run_burst <= work_awburst;
                run_len <= work_awlen+1;
                run_size <= work_awsize;
                run_id <= work_awid;
            end
        end else if (working_r && !r_full) begin
            run_addr <= next_addr;
            run_len <= run_len - 1;

            if (pread_dly && run_rlast) begin
                working_r <= 0;
            end 
        end else if (working_w) begin
            run_addr <= next_addr;
            run_len <= run_len -1 ;
            if (run_last) begin
                working_w <= 0;
            end
        end
    end
end


localparam AWIDE =  3 + IDWID + AWID + 8  +2;
wire [AWIDE-1:0] new_aw_entry =   {awsize, awid ,awaddr ,awlen , awburst };
wire aw_full;
wire [AWIDE-1:0] active_aw_entry;
assign {work_awsize,  work_awid ,work_awaddr ,work_awlen , work_awburst } = active_aw_entry;
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
wire [IDWID-1:0] x_bid;
syncfifo_sampled #(4,4) b_fifo (.clk(clk),.rst_n(rst_n),.vldin(run_last && working_w)
    ,.din(run_id)
    ,.empty(b_empty),.full(b_full)
    ,.readout(bready)
    ,.dout(x_bid)
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_b_fifo)
);
assign bid = x_bid;
assign bresp = 0;
assign wready = !w_full;
assign bvalid = !b_empty;
wire work_wlast;
wire [DWID-1:0] work_wdata;
wire [WSTRB-1:0] work_wstrb;
syncfifo_sampled #(1+WSTRB+DWID,4) w_fifo (.clk(clk),.rst_n(rst_n),.vldin(wvalid && wready)
    ,.din({wlast,wstrb[WSTRB-1:0],wdata[DWID-1:0]})
    ,.empty(w_empty),.full(w_full)
    ,.readout(pwrite)
    ,.dout({work_wlast,work_wstrb,work_wdata})
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_w_fifo)
);

assign readout_aw_fifo = pwrite && work_wlast && working_w;
wire readout_ar_fifo = working_r && run_rlast &&  pread_dly;
localparam ARIDE = 3+IDWID+2+8+AWID;
wire [ARIDE-1:0] new_ar_entry =  {arsize,arid,arburst,arlen,araddr};
 wire [ARIDE-1:0]  active_ar_entry;
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
assign {work_arsize,work_arid,work_arburst,work_arlen,work_araddr} = active_ar_entry;

reg [DWID-1:0] prdata; 
reg pread_dly; always @(posedge clk) pread_dly <= pread;
syncfifo_sampled #(1+4+DWID,4) r_fifo (.clk(clk),.rst_n(rst_n),.vldin(pread_dly)
    ,.din({prdata,run_id,run_rlast})
    ,.empty(r_empty),.full(r_full)
    ,.readout(rready)
    ,.dout({rdata,rid,rlast})
    ,.count()
    ,.softreset(1'b0)
    ,.overflow(panic_r_fifo)
);

assign rvalid= !r_empty;

assign pwrite = !aw_empty && !w_empty && working_w;


reg [DWID-1:0] ram [0:(1<<RAMSIZE)-1];
wire [DWID-1:0] was_data = ram[run_addr>>3];
wire [DWID-1:0] wmask;
assign wmask[7+0*8:0*8] = {8{work_wstrb[0]}};
assign wmask[7+1*8:1*8] = {8{work_wstrb[1]}};
assign wmask[7+2*8:2*8] = {8{work_wstrb[2]}};
assign wmask[7+3*8:3*8] = {8{work_wstrb[3]}};
assign wmask[7+4*8:4*8] = {8{work_wstrb[4]}};
assign wmask[7+5*8:5*8] = {8{work_wstrb[5]}};
assign wmask[7+6*8:6*8] = {8{work_wstrb[6]}};
assign wmask[7+7*8:7*8] = {8{work_wstrb[7]}};

wire [DWID-1:0] new_wdata  = (was_data & ~ wmask)|(work_wdata & wmask);
always @(posedge clk) begin
    if (pwrite) begin
        ram[(run_addr>>3)] <=  new_wdata;
        $display("RAM WRITE addr=%h data=%h  wstrb=%h", run_addr,new_wdata,work_wstrb);
    end
end
always @(posedge clk) if (pread) begin
    prdata <= ram[run_addr>>3];
    $display("RAM READ addr=%h data=%h", run_addr,ram[run_addr>>3]);
end
assign rresp = (run_size>3) || ((run_addr>>3)>=(1<<RAMSIZE));




wire [63:0]  sign_version = 64'h000742ff22060424 ;
endmodule

