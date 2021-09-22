
// add address generator;


module axi2apb #(parameter IDWID=4,parameter DWID=64, parameter WSTRB = DWID/8, parameter EXTRAS=8)(

    input clk, input rst_n


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




    ,output psel
    ,output [31:0] paddr
    ,output reg penable
    ,output pwrite
    ,output [31:0] pwdata
    ,input pready
    ,input [1:0] presp
    ,input [31:0] prdata
    ,output [3:0] pstrb
);
    



    
wire ar_empty,aw_empty;
reg working_r,working_w;

wire [7:0] work_awlen;
reg [31:0] run_addr;
reg [1:0] run_burst;
reg [8:0] run_len;
wire run_last = run_len == 1;
reg [IDWID-1:0] run_rid;
wire [IDWID-1:0] work_awid;
wire [7:0] work_arlen;
wire [31:0] work_awaddr,work_araddr;
wire [1:0] work_awburst;
wire [IDWID-1:0] work_arid;
reg [1:0] work_arburst;
wire w_full;
wire r_full;
wire run_rlast = (run_len == 1) && working_r;
wire pread = working_r && !r_full && (run_len>0);


wire [31:0] wrapmask = 
    (work_arlen == 3) ? 32'hffff_ffe0 :
    (work_arlen == 7) ? 32'hffff_ffc0 :
    (work_arlen ==15) ? 32'hffff_ff80 :
    (work_arlen ==31) ? 32'hffff_ff00 :
    (work_arlen ==63) ? 32'hffff_fe00 :
    32'hffff_fc00 ;


wire [31:0] next_addr = 
    (run_burst == 0) ? run_addr :
    (run_burst == 1) ? (run_addr+8) :
    (run_burst == 2) ? (run_addr & wrapmask) + ((run_addr + 8) & ~wrapmask) :
    0;


wire pushr;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        working_r <= 0;
        working_w <= 0;
        run_addr <= 0;
        run_burst <= 0;
        run_len <= 0;
        run_rid <= 0;
    end else begin
        if (!working_r && !working_w) begin
            if (!ar_empty) begin
                working_r <= 1;
                run_addr <= work_araddr & 32'hffff_fff8;
                run_burst <= work_arburst;
                run_len <= work_arlen+1;
                run_rid <= work_arid;
            end else if (!aw_empty) begin
                working_w <= 1;
                run_addr <= work_awaddr;
                run_burst <= work_awburst;
                run_len <= work_awlen+1;
                run_rid <= work_awid;
            end
        end else if (working_r && !r_full && pready && (pstate==3)) begin
            run_addr <= next_addr;
            run_len <= run_len - 1;

            if (pushr && run_rlast) begin
                working_r <= 0;
            end 
        end else if (working_w && (pstate==10) && pready) begin
            run_addr <= next_addr;
            run_len <= run_len -1 ;
            if (run_last) begin
                working_w <= 0;
            end
        end
    end
end


localparam AWIDE =  IDWID + 32 + 8  +2;
wire [AWIDE-1:0] new_aw_entry =   {   awid ,awaddr ,awlen , awburst };
wire aw_full;
wire [AWIDE-1:0] active_aw_entry;
assign {   work_awid ,work_awaddr ,work_awlen , work_awburst } = active_aw_entry;
wire readout_aw_fifo;
syncfifo_sampled #(AWIDE,4) aw_fifo (.clk(clk),.rst_n(rst_n),.vldin(awvalid && awready)
    ,.din(new_aw_entry)
    ,.empty(aw_empty),.full(aw_full)
    ,.readout(readout_aw_fifo)
    ,.dout(active_aw_entry)
    ,.count()
    ,.softreset(1'b0)
);
assign awready = !aw_full;

syncfifo_sampled #(4,4) b_fifo (.clk(clk),.rst_n(rst_n),.vldin(run_last && working_w)
    ,.din(run_rid)
    ,.empty(b_empty),.full(b_full)
    ,.readout(bready)
    ,.dout(bid)
    ,.count()
    ,.softreset(1'b0)
);
assign bresp = 0;
assign wready = !w_full;
assign bvalid = !b_empty;
wire work_wlast;
wire [DWID-1:0] work_wdata;
wire [WSTRB-1:0] work_wstrb;
syncfifo_sampled #(1+8+64,4) w_fifo (.clk(clk),.rst_n(rst_n),.vldin(wvalid && wready)
    ,.din({wlast,wstrb[7:0],wdata[63:0]})
    ,.empty(w_empty),.full(w_full)
    ,.readout((pstate==10) && pready)
    ,.dout({work_wlast,work_wstrb,work_wdata})
    ,.count()
    ,.softreset(1'b0)
);

assign readout_aw_fifo = ipwrite && work_wlast && working_w;
wire readout_ar_fifo = working_r && run_rlast &&  pushr;
localparam ARIDE = IDWID+2+8+32;
wire [ARIDE-1:0] new_ar_entry =  {arid,arburst,arlen,araddr};
 wire [ARIDE-1:0]  active_ar_entry;
syncfifo_sampled #(ARIDE,4) ar_fifo (.clk(clk),.rst_n(rst_n),.vldin(arvalid && arready)
    ,.din(new_ar_entry)
    ,.empty(ar_empty),.full(ar_full)
    ,.readout(readout_ar_fifo)
    ,.dout(active_ar_entry)
    ,.count()
    ,.softreset(1'b0)
);
assign arready = !ar_full;
assign {work_arid,work_arburst,work_arlen,work_araddr} = active_ar_entry;

reg [31:0] lowrdata;
syncfifo_sampled #(1+4+64,4) r_fifo (.clk(clk),.rst_n(rst_n),.vldin(pushr)
    ,.din({prdata,lowrdata,run_rid,run_rlast})
    ,.empty(r_empty),.full(r_full)
    ,.readout(rready)
    ,.dout({rdata,rid,rlast})
    ,.count()
    ,.softreset(1'b0)
);


reg [3:0] pstate;
assign pushr = (pstate==3) && pready; 
always @(posedge clk) begin
    if (pready) begin
        if (pstate==1) lowrdata[31:0] <= prdata;
    end
end

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        pstate <= 0;
     end else begin
        if (pstate == 0) begin
            if (pread) pstate <= 1;
            else if (ipwrite) pstate <= 8;
        end else if (pstate==1) begin
            if (pready) pstate <= 2;
        end else if (pstate==2) begin
            if (pready) pstate <= 3;
        end else if (pstate==3) begin
            if (pready) pstate <= 0;

        end else if (pstate==8) begin
            if (pready) pstate <= 9;
        end else if (pstate==9) begin
            if (pready) pstate <= 10;
        end else if (pstate==10) begin
            if (pready) pstate <= 0;
        end
    end
end
assign rvalid= !r_empty;

assign ipwrite = !aw_empty && !w_empty && working_w && (pstate==0);

assign paddr = 
    (pstate == 0) ? run_addr :
    (pstate == 2) ? (run_addr+4) :
    (pstate == 3) ? (run_addr+4) :
    (pstate == 9) ? (run_addr+4) :
    (pstate == 10) ? (run_addr+4) :
    run_addr;

assign pwdata =  
    (pstate==8) ? work_wdata[31:0] :
    (pstate==9) ? work_wdata[63:32] :
    (pstate==10) ? work_wdata[63:32] :
     work_wdata[31:0];

assign pstrb = 
    (pstate == 8) ? work_wstrb[3:0] :
    (pstate == 10) ? work_wstrb[7:4] :
    0;

assign psel = pread || ipwrite || (pstate>0) ;
assign penable = (pstate==1)||(pstate==3)||(pstate==8)||(pstate==10);
assign rresp = presp;
assign pwrite = (pstate==8) || (pstate==10);
endmodule

