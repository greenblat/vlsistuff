
//sourced from:   https://github.com/greenblat/vlsistuff.git   ::: rtl_library/fifos/rtl
// MIT license: do whatever

module syncfifo_shared_4 #(parameter WID=32, parameter DEPTH=8) (
     input clk, input rst_n, input softreset
    ,input vldin, input [WID-1:0] din, input [1:0] destination
    ,input [3:0] readout, output [3:0] [WID-1:0] dout
    ,output full
    ,output [3:0] empty
    ,output [15:0] count
    ,output overflow

);

localparam AWID = $clog2(DEPTH);
reg [DEPTH-1:0] [WID-1:0] bufs ;

reg [DEPTH-1:0] occupied;
wire [AWID:0] first_free;
find_first_zero #(.WID(DEPTH)) zero (.din(occupied),.dout(first_free));
assign full = &occupied;

assign overflow = full && vldin;

wire [3:0] [AWID-1:0] ptr;

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        occupied <= 0;
    end else begin
        if (vldin && !full)   occupied[first_free] <= 1;

        if (readout[0] && !empty[0]) occupied[ptr[0]] <= 0; 
        if (readout[1] && !empty[1]) occupied[ptr[1]] <= 0; 
        if (readout[2] && !empty[2]) occupied[ptr[2]] <= 0; 
        if (readout[3] && !empty[3]) occupied[ptr[3]] <= 0; 
    end
end

always @(posedge clk) begin
    if (vldin && !full)   bufs[first_free] <= din;
end 

assign dout[0] = empty[0] ? 0 :bufs[ptr[0]];
assign dout[1] = empty[1] ? 0 :bufs[ptr[1]];
assign dout[2] = empty[2] ? 0 :bufs[ptr[2]];
assign dout[3] = empty[3] ? 0 :bufs[ptr[3]];




wire [3:0] int_full;

wire [3:0] count0,count1,count2,count3;
syncfifo #(AWID,DEPTH) ptr_0_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(vldin && !full && (destination==0)) ,.din(first_free[AWID-1:0])
    ,.empty(empty[0]),.full(int_full[0])
    ,.readout(readout[0] && !empty[0])
    ,.dout(ptr[0])
    ,.softreset(softreset)
    ,.count(count0)
);

syncfifo #(AWID,DEPTH) ptr_1_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(vldin && !full && (destination==1)) ,.din(first_free[AWID-1:0])
    ,.empty(empty[1]),.full(int_full[1])
    ,.readout(readout[1] && !empty[1])
    ,.dout(ptr[1])
    ,.softreset(softreset)
    ,.count(count1)
);

syncfifo #(AWID,DEPTH) ptr_2_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(vldin && !full && (destination==2)) ,.din(first_free[AWID-1:0])
    ,.empty(empty[2]),.full(int_full[2])
    ,.readout(readout[2] && !empty[2])
    ,.dout(ptr[2])
    ,.softreset(softreset)
    ,.count(count2)
);

syncfifo #(AWID,DEPTH) ptr_3_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(vldin && !full && (destination==3)) ,.din(first_free[AWID-1:0])
    ,.empty(empty[3]),.full(int_full[3])
    ,.readout(readout[3] && !empty[3])
    ,.dout(ptr[3])
    ,.softreset(softreset)
    ,.count(count3)
);

assign count = 0+count0+count1+count2+count3;

wire [63:0]  sign_version = 64'h0003064409250424 ;
endmodule

