
module rou_axi_master #(
     parameter DWID = 128 
    ,parameter AWID = 32
    ,parameter ADWID = 32
    ,parameter TWID = 5 
    ,parameter BWID = 
        (DWID==512)  ? 6 : 
        (DWID==256)  ? 5 : 
        (DWID==128) ? 4 : 
        (DWID==64)  ? 3 : 2 
    ,parameter WID = 2+DWID+AWID+BWID+TWID
) (
    input clk, input rst_n
    ,input rou_in_seen, output rou_out_seen
    ,input [WID-1:0] rou_in, output [2:0] ack_in 
    ,output [WID-1:0] rou_out, input [2:0] ack_out
    ,input [31:0] pages, input [31:0] whoami



// axi write addr channel
    ,output [3:0] awid           // addr write id
    ,output [ADWID-1:0] awaddr
    ,output [7:0] awlen
    ,output [2:0] awsize
    ,output [1:0] awburst
    ,output awvalid
    ,input awready

// axi write data channel
    ,output [127:0] wdata
    ,output [15:0] wstrb
    ,output wlast
    ,output wvalid
    ,input wready

// axi write responce channel
    ,input [3:0] bid 
    ,input [1:0] bresp
    ,input bvalid
    ,output bready

// axi read addr channel
    ,output [3:0] arid
    ,output [ADWID-1:0] araddr
    ,output [7:0] arlen
    ,output [2:0] arsize
    ,output [1:0] arburst
    ,output arvalid
    ,input arready
    
// axi read data channel
    ,input [3:0] rid 
    ,input [127:0] rdata
    ,input [1:0] rresp
    ,input rlast
    ,input rvalid
    ,output rready




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

wire wr_data_fifo_full,wr_data_fifo_empty;
wire wr_addr_fifo_full,wr_addr_fifo_empty;
wire rd_fifo_full,rd_fifo_empty;
assign msg_in_ack = !wr_data_fifo_full && !wr_addr_fifo_full && !rd_fifo_full;
wire [127:0] msg_in_data;
wire [1:0] msg_in_cmd;
wire [3:0] msg_in_bytes;
wire [4:0] msg_in_tags;
wire [31:0] msg_in_addr;


rou_msg_fields msg_in_fields(.msg(msg_in), .addr(msg_in_addr) ,.tags(msg_in_tags) ,.bytes(msg_in_bytes) ,.cmd(msg_in_cmd) ,.data(msg_in_data));


wire [3:0] wr_offset;
wire [BWID-1:0] wr_bytes;
wire [DWID-1:0] wr_wdata;
wire [AWID-1:0] wr_waddr;



syncfifo #(DWID+BWID+4,4) wr_data_fifo (.clk(clk),.rst_n(rst_n),.softreset(1'b0)
    ,.validin(msg_in_cmd==2),.datain({msg_in_data,msg_in_bytes,msg_in_addr[3:0]})
    ,.full(wr_data_fifo_full),.empty(wr_data_fifo_empty),.overflow(),.count()
    ,.readout(wready),.dataout({wr_wdata,wr_bytes,wr_offset})
);
syncfifo #(AWID,4) wr_addr_fifo (.clk(clk),.rst_n(rst_n),.softreset(1'b0)
    ,.validin(msg_in_cmd==2),.datain(msg_in_addr)
    ,.full(wr_addr_fifo_full),.empty(wr_addr_fifo_empty),.overflow(),.count()
    ,.readout(awready),.dataout(wr_waddr)
);




assign awvalid = !wr_addr_fifo_empty;
assign awlen = 0;
assign awid = 3;
assign awaddr = wr_waddr-base_address;
assign awburst = 1;
assign awsize = 4;


assign wvalid = !wr_data_fifo_empty;
assign wdata  = wr_wdata << (8*wr_offset);
assign wstrb  = ((1<<wr_bytes)-1)<<wr_offset;  // NOT TREATED SPLIT TO TWO!!!!
assign wlast = wvalid;



wire [4:0] rd_tags;
wire [47:0] rd_rdata;
wire [31:0] rd_raddr;

wire [BWID-1:0] rd_bytes0;
syncfifo #(48+BWID+TWID+AWID,4) rd_data_fifo (.clk(clk),.rst_n(rst_n),.softreset(1'b0)
    ,.validin(msg_in_cmd==1),.datain({msg_in_data[47:0],msg_in_tags,msg_in_bytes,msg_in_addr})
    ,.full(rd_fifo_full),.empty(rd_fifo_empty),.overflow(),.count()
    ,.readout(rd_readout),.dataout({rd_rdata,rd_tags,rd_bytes0,rd_raddr})
);

wire [19:0] rd_bytes = {rd_rdata[47:32],rd_bytes0}+1;
wire [31:0] rd_return = rd_rdata[31:0];

reg [2:0] rdstate;
reg [31:0] return_addr;
reg increment_return;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        rdstate<=0;
        return_addr<=0;
        increment_return <= 0;
    end else begin
        if (rdstate==0) begin
            if (!rd_fifo_empty && arready) begin
                rdstate<= 1;
                return_addr <= rd_return;
                increment_return <= rd_tags[1];
            end
        end else if (rdstate==1) begin
            if (rvalid && rlast && rready) begin
                rdstate<= 0;
            end
            return_addr <= (rvalid && rready && increment_return) ? return_addr + 16 : return_addr;
        end
    end
end

assign arvalid = (rdstate==0)&&!rd_fifo_empty;
assign arburst = rd_tags[0];  // NEEDS VALIDATION, ILIA. Look at read message.
assign araddr = rd_raddr;
assign arlen = (rd_bytes>>4)+(rd_bytes[3:0]!=0)-1;   // NEEDS SPLITTER logic. ILIA
assign arsize = 4;
assign arid = 3;
assign rd_readout = (rdstate==0)&&!rd_fifo_empty && arready;

assign rready = !rd_data_fifo_full;
wire rd_data_readout = msg_out_ack;
wire [DWID-1:0] backdata;
syncfifo #(DWID,4) rd_back_fifo (.clk(clk),.rst_n(rst_n),.softreset(1'b0)
    ,.validin(rvalid),.datain(rdata)
    ,.full(rd_data_fifo_full),.empty(rd_data_fifo_empty),.overflow(),.count()
    ,.readout(rd_data_readout),.dataout(backdata)
);

rou_msg_build  msg_out_build  (.msg(msg_out),.data(backdata),.addr(return_addr),.tags(5'd0) ,.bytes(4'hf) ,.cmd(rd_data_fifo_empty ? 2'd0 : 2'd2));



endmodule

