
// THIS IS NOT A WORKING CODE, JUST ATTEMPT TO BUILD ONE

module syncfifo_shared_4 #(parameter WID=32, parameter DEPTH=8) (
    ,input clk, input rst_n, input softreset
    ,input vldin[3:0], input [3:0] [WID-1:0] din
    ,input [3:0] readout, output [3:0] [WID-1:0] dout
    ,output [3:0] full
    ,output [3:0] empty
    ,output [15:0] count

);

reg [DEPTH-1:0] bufs [WID-1:0];

localpram AWID = $clog2(DEPTH); 

wire [3:0] [AWID-1:0] ptr;

wire [2:0] writes = 0+readout[0]+readout[1]+readout[2]+readout[3];
localparam INIT = 0;
multififo_w4_r4 #(.WIDTH(AWID),.DEPTH(DEPTH),.INIT(0)) (
    .clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.writes(writes),.din()
    ,.reads(reads) ,.dout()
    ,.taken()
    ,.count(count)
    ,.frees(frees)
);









integer ii;
reg nonfree;
always @* begin
    ii = 0;
    while ((ii<DEPTH) && (occupied[ii])) ii = ii+1;
end
wire nofrees = &occupied;

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        occupied <= 0;
    end else begin
        if (written && !nofrees) occupied[ii] <= 1; 
        if (readout[0] && !empty[0]) occupied[ptr[0]] <= 0; 
        if (readout[1] && !empty[1]) occupied[ptr[1]] <= 0; 
        if (readout[2] && !empty[2]) occupied[ptr[2]] <= 0; 
        if (readout[3] && !empty[3]) occupied[ptr[3]] <= 0; 
    end
end


wire [3:0] int_full;

syncfifo #(AWID,DEPTH) ptr_0_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(vldin[0] && !full[0]) ,.din(din[0])
    ,.empty(empty[0]),.full(int_full[0])
    ,.readout(readout[0] && !empty[0])
    ,.dout(ptr[0])
    ,.softreset(softreset)
    ,.count() ,.overflow()
);

syncfifo #(AWID,DEPTH) ptr_1_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(vldin[1] && !full[1]) ,.din(din[1])
    ,.empty(empty[1]),.full(int_full[1])
    ,.readout(readout[1] && !empty[1])
    ,.dout(ptr[1])
    ,.softreset(softreset)
    ,.count() ,.overflow()
);

syncfifo #(AWID,DEPTH) ptr_2_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(vldin[2] && !full[2]) ,.din(din[2])
    ,.empty(empty[2]),.full(int_full[2])
    ,.readout(readout[2] && !empty[2])
    ,.dout(ptr[2])
    ,.softreset(softreset)
    ,.count() ,.overflow()
);

syncfifo #(AWID,DEPTH) ptr_3_fifo (.clk(clk),.rst_n(rst_n)
    ,.vldin(vldin[3] && !full[3]) ,.din(din[3])
    ,.empty(empty[3]),.full(int_full[3])
    ,.readout(readout[3] && !empty[3])
    ,.dout(ptr[3])
    ,.softreset(softreset)
    ,.count() ,.overflow()
);





endmodule

