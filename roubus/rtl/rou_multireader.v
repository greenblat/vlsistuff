


module rou_multireader (
    input clk, input rst_n

// command input
    ,input [31:0] start_addr
    ,input [2:0]  memsize
    ,input [19:0] bytes
    ,input incr_addr
    ,input valid
    ,output busy

//
    ,output [127:0] odata
    ,output [4:0] obytes
    ,output ovalid
    ,output pulse_last
    ,input otaken


// local memory interface
    ,output local_rd
    ,output reg [31:0] local_rd_addr
    ,output reg [3:0] local_rd_roffset
    ,input [127:0] local_rd_data
    ,input  local_rd_addr_ok
    ,input  local_rd_data_ok


    
);

reg [19:0] local_bytes;
wire [2:0] effective_memsize = memsize;
wire [31:0] mask1 =  ((1<<effective_memsize)-1);
wire [31:0] mask0 =  ~mask1;
wire [7:0] bytesInOneAccess = 1<<effective_memsize;
wire [4:0] first_bytes0 =  bytesInOneAccess -(start_addr & mask1);
wire [4:0] first_bytes  = (first_bytes0>bytes) ? bytes : first_bytes0;

wire bhasplace;

reg active0,active1;


wire [4:0] sent_bytes =  
    !active1 ? first_bytes
    : (local_bytes<bytesInOneAccess) ? local_bytes
    : bytesInOneAccess;

wire fw_full;
wire int_local_rd = active0 && bhasplace && !fw_full;
assign local_rd = int_local_rd; // &&  local_rd_addr_ok;

reg [3:0] local_offset;
reg local_incr;
always @(posedge clk ) begin
    if (!rst_n) begin
        active0 <= 0; active1 <= 0;
        local_rd_addr <= 0;
        local_bytes <= 0;
        local_incr <= 0;
        local_offset <= 0;
        local_rd_roffset<=0;
    end else begin
        if (!busy &&  valid) begin
            active0 <= (bytes!=0);
            active1 <= 0;
            local_rd_addr <=  mask0 & start_addr;
            local_rd_roffset <= start_addr & mask1;
            local_bytes <= bytes;
            local_incr  <= incr_addr;
            local_offset <= (start_addr & mask1); 
        end else if (int_local_rd && local_rd_addr_ok) begin
            local_offset <= 0;
            if (local_bytes<=bytesInOneAccess) begin
                active0 <= 0; active1 <= 0; local_rd_addr<=0; local_bytes<=0; 
            end else begin
                active1 <= 1;
                local_rd_addr <= local_rd_addr + (local_incr ? bytesInOneAccess : 0);
                local_bytes <= local_bytes  - sent_bytes;
            end
        end
    end
end


wire [4:0] use_bytes;
wire [3:0] use_offset;
wire use_last;

wire fw_empty;
wire read_fw_fifo  = !fw_empty &&  local_rd_data_ok;
wire [2:0] fw_count;
wire write_fw_fifo = int_local_rd && local_rd_addr_ok;
syncfifo #(5+4+1,4) forward_fifo (.clk(clk),.rst_n(rst_n),.softreset(1'b0)
    ,.validin(write_fw_fifo),.datain({sent_bytes,local_offset,1'b0})
    ,.full(fw_full),.empty(fw_empty),.overflow(),.count(fw_count)
    ,.readout(read_fw_fifo),.dataout({use_bytes,use_offset,use_last})
);


wire [3:0] bw_count;
wire [127:0] use_data = (local_rd_data>>{use_offset,3'b000});



parameter BACKWID = 128 + 1 + 5;



wire [BACKWID-1:0] back_indata = {use_last,use_bytes,use_data};

wire [BACKWID-1:0] back_outdata;
wire bw_empty;
syncfifo #(BACKWID,6) back_fifo (.clk(clk),.rst_n(rst_n),.softreset(1'b0)
    ,.validin(read_fw_fifo),.datain(back_indata)
    ,.full(),.empty(bw_empty),.overflow(),.count(bw_count)
    ,.readout(otaken),.dataout(back_outdata)
);

assign bhasplace = bw_count<4;

assign ovalid = !bw_empty;
assign {pulse_last,obytes,odata} = bw_empty ? {BACKWID{1'b0}} : back_outdata;

wire early_fw_empty = (fw_count==1) && read_fw_fifo;
assign busy = active0 || !fw_empty && !early_fw_empty;




endmodule


