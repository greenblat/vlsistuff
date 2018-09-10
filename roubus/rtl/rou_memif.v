

module rou_memif #(
     parameter DWID = 128
    ,parameter AWID = 32
    ,parameter TWID = 5
    ,parameter BWID =
        (DWID==512)  ? 6 :
        (DWID==256)  ? 5 :
        (DWID==128) ? 4 :
        (DWID==64)  ? 3 : 2
    ,parameter WID = 2+DWID+AWID+BWID+TWID
    ,parameter DEPTH=1024
    ,parameter WSTRB = DWID/8
) (
    input clk, input rst_n


    ,output [WID-1:0] msg_out
    ,input msg_out_ack

    ,input [WID-1:0] msg_in
    ,output msg_in_ack

    ,input [AWID-1:0] base_address
 // local memory interface
    ,output local_wr ,output local_rd
    ,output [31:0] local_addr
    ,output [DWID-1:0] local_wr_data
    ,output [WSTRB-1:0] local_wstrb
    ,output [DWID-1:0] local_bwen
    ,input  local_wr_ok
    ,input  local_wr_error

    ,input [127:0] local_rd_data
    ,input  local_rd_addr_ok
    ,input  local_rd_data_ok
    ,input  local_rd_error

);


wire [127:0] msg_in_data;
wire [1:0] msg_in_cmd;
wire [3:0] msg_in_bytes;
wire [4:0] msg_in_tags;
wire [31:0] msg_in_addr;

wire wr_data_fifo_full,wr_data_fifo_empty;
assign msg_in_ack = !wr_data_fifo_full;

rou_msg_fields msg_in_fields(.msg(msg_in), .addr(msg_in_addr) ,.tags(msg_in_tags) ,.bytes(msg_in_bytes) ,.cmd(msg_in_cmd) ,.data(msg_in_data));

reg second_valid;
wire rd_busy;
wire rd_cmd = !wr_data_fifo_empty && !wr_cmd;
wire  readout = (wr_cmd && local_wr_ok && !second_valid) || rd_cmd && !rd_busy;

wire [31:0] wr_addr;
wire [127:0] wr_data;
wire [3:0] wr_bytes;
wire [31:0] effective_addr = msg_in_addr - base_address;
wire [TWID-1:0] wr_tags;
wire wr_cmd;
syncfifo #(1+DWID+BWID+TWID+32,4) wr_data_fifo (.clk(clk),.rst_n(rst_n),.softreset(1'b0)
    ,.validin(msg_in_cmd!=0),.datain({(msg_in_cmd==2),msg_in_tags,msg_in_data,msg_in_bytes,effective_addr})
    ,.full(wr_data_fifo_full),.empty(wr_data_fifo_empty),.overflow(),.count()
    ,.readout(readout),.dataout({wr_cmd,wr_tags,wr_data,wr_bytes,wr_addr})
);


wire [3:0] wr_offset = wr_addr[3:0];

reg [31:0] second_addr;
reg [WSTRB-1:0] second_wstrb;
reg [DWID-1:0] second_data;

wire  [2*WSTRB-1:0] twowstrb  = ((1<<wr_bytes)-1)<<wr_offset; 
wire [DWID*2-1:0] twodata = {{DWID{1'b0}},wr_data} << (8*wr_offset);
wire valid_second_serving = twowstrb[2*WSTRB-1:WSTRB]!=0;

wire [WSTRB-1:0] first_wstrb = twowstrb[WSTRB-1:0];
wire [DWID-1:0] first_data = twodata[DWID-1:0];
wire [AWID-1:0] first_addr = {wr_addr[31:4],4'b0};

wire merge_valid = second_valid && (second_addr[31:4]==wr_addr[31:4])&&((first_wstrb & second_wstrb)==0) && (wr_cmd && !wr_data_fifo_empty);

wire [WSTRB-1:0] merged_wstrb = first_wstrb|second_wstrb;
wire [DWID-1:0] merged_data   = {
     (first_wstrb[15] ? first_data[127:120] : second_data[127:120])
    ,(first_wstrb[14] ? first_data[119:112] : second_data[119:112])
    ,(first_wstrb[13] ? first_data[111:104] : second_data[111:104])
    ,(first_wstrb[12] ? first_data[103:96] : second_data[103:96])
    ,(first_wstrb[11] ? first_data[95:88] : second_data[95:88])
    ,(first_wstrb[10] ? first_data[87:80] : second_data[87:80])
    ,(first_wstrb[9] ? first_data[79:72] : second_data[79:72])
    ,(first_wstrb[8] ? first_data[71:64] : second_data[71:64])
    ,(first_wstrb[7] ? first_data[63:56] : second_data[63:56])
    ,(first_wstrb[6] ? first_data[55:48] : second_data[55:48])
    ,(first_wstrb[5] ? first_data[47:40] : second_data[47:40])
    ,(first_wstrb[4] ? first_data[39:32] : second_data[39:32])
    ,(first_wstrb[3] ? first_data[31:24] : second_data[31:24])
    ,(first_wstrb[2] ? first_data[23:16] : second_data[23:16])
    ,(first_wstrb[1] ? first_data[15:8] : second_data[15:8])
    ,(first_wstrb[0] ? first_data[7:0] : second_data[7:0])
};

assign local_bwen = ~{
     {8{local_wstrb[15]}}
    ,{8{local_wstrb[14]}}
    ,{8{local_wstrb[13]}}
    ,{8{local_wstrb[12]}}
    ,{8{local_wstrb[11]}}
    ,{8{local_wstrb[10]}}
    ,{8{local_wstrb[9]}}
    ,{8{local_wstrb[8]}}
    ,{8{local_wstrb[7]}}
    ,{8{local_wstrb[6]}}
    ,{8{local_wstrb[5]}}
    ,{8{local_wstrb[4]}}
    ,{8{local_wstrb[3]}}
    ,{8{local_wstrb[2]}}
    ,{8{local_wstrb[1]}}
    ,{8{local_wstrb[0]}}
};


wire [31:0] local_rd_addr;

assign local_wr = (wr_cmd && !wr_data_fifo_empty) || second_valid;
assign local_addr = local_rd ? local_rd_addr : merge_valid ? first_addr : second_valid ? second_addr : first_addr;
assign local_wr_data  = merge_valid ? merged_data : second_valid ? second_data : first_data;
assign local_wstrb = merge_valid ? merged_wstrb : second_valid ? second_wstrb : twowstrb[WSTRB-1:0];


always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        second_valid <= 1'b0;
        second_addr <= 0;
        second_wstrb <= 0;
        second_data <= 0;
    end else if (!second_valid && valid_second_serving) begin
        second_valid <= 1'b1;
        second_addr <= {wr_addr[31:4]+1'b1,4'b0};;
        second_wstrb <= twowstrb[2*WSTRB-1:WSTRB];;
        second_data <= twodata[2*DWID-1:DWID];
    end else if (second_valid && local_wr_ok) begin
        second_valid <= 1'b0;
   end
end
        
reg [AWID-1:0] back_addr;
wire [4:0] obytes;
wire [DWID-1:0] odata;
wire ovalid,pulse_last;
wire otaken = msg_out_ack;
reg incr_back_addr;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        back_addr <= 0;
        incr_back_addr <= 0;
    end else begin
        if (!rd_busy && rd_cmd) begin
            back_addr <= wr_data[AWID-1:0];
            incr_back_addr <= wr_tags[0];
        end else if (ovalid && otaken && incr_back_addr) begin
            back_addr <= back_addr +obytes;
        end
    end
end

wire [16+BWID-1:0] byte_counts = {wr_data[AWID+16-1:AWID],wr_bytes}+1'b1;

rou_multireader rou_multireader (
     .clk(clk) ,.rst_n(rst_n)
    ,.busy(rd_busy)
    ,.memsize(3'd4)

    ,.valid(rd_cmd)
    ,.incr_addr(wr_tags[1])
    ,.start_addr(wr_addr)
    ,.bytes(byte_counts)

    ,.local_rd(local_rd)
    ,.local_rd_addr(local_rd_addr[31:0])
    ,.local_rd_addr_ok(local_rd_addr_ok)
    ,.local_rd_data(local_rd_data[127:0])
    ,.local_rd_data_ok(local_rd_data_ok)
    ,.local_rd_roffset()

    ,.obytes(obytes[4:0])
    ,.odata(odata[127:0])
    ,.otaken(msg_out_ack)
    ,.ovalid(ovalid)
    ,.pulse_last(pulse_last)
);

wire [BWID-1:0] msg_out_bytes = obytes-1;
rou_msg_build  msg_out_build  (.msg(msg_out),.data(odata),.addr(back_addr),.tags({4'b0000,pulse_last}) ,.bytes(msg_out_bytes) ,.cmd({ovalid,1'b0}));





endmodule


