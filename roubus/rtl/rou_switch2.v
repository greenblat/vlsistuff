
module rou_switch2 #(
     parameter DWID = 128 
    ,parameter AWID = 32
    ,parameter TWID = 5 
    ,parameter BWID = 
        (DWID==512)  ? 6 : 
        (DWID==256)  ? 5 : 
        (DWID==128) ? 4 : 
        (DWID==64)  ? 3 : 2 
    ,parameter WID = 2+DWID+AWID+BWID+TWID
)(
    input clk, input rst_n
    ,input  [WID-1:0] rou_in0, input rou_in0_seen, output [2:0] ack_in0
    ,output [WID-1:0] rou_out0, output rou_out0_seen,  input [2:0] ack_out0

    ,input  [WID-1:0] rou_in1, input rou_in1_seen, output [2:0] ack_in1
    ,output [WID-1:0] rou_out1, output rou_out1_seen,  input [2:0] ack_out1

);

parameter BUFS = 8;
reg [WID-1:0] bufs [0:BUFS-1];
reg [BUFS-1:0] seens;
parameter WBUFS = 3+$clog2(BUFS);
parameter NOTLEGAL= (1<<WBUFS)-1;
wire [WBUFS-1:0] free0indx,free1indx,free2indx;

wire [1:0] splitter0_sel;
wire [1:0] splitter1_sel;

wire [WID-1:0] msg_0_0,msg_0_1, msg_1_0,msg_1_1;
wire msg_0_0_ack,msg_0_1_ack,msg_1_0_ack,msg_1_1_ack;
wire queue_0_0_full,queue_0_0_empty;
wire queue_0_1_full,queue_0_1_empty;
wire queue_1_1_full,queue_1_1_empty;
wire queue_1_0_full,queue_1_0_empty;

wire [WBUFS-1:0] notlegal = NOTLEGAL;

assign ack_in0[2:1] = 0;
assign ack_in1[2:1] = 0;
msg_splitter2 #(WID) splitter0 (.msgin(rou_in0),.msginack(ack_in0[0])
    ,.msga(msg_0_0) , .acka(!queue_0_0_full)
    ,.msgb(msg_0_1) ,.ackb(!queue_0_1_full)
    ,.sel(splitter0_sel) ,.default_option({WID{1'b0}})
);

msg_splitter2 #(WID) splitter1 (.msgin(rou_in1),.msginack(ack_in1[0])
    ,.msga(msg_1_0) ,.acka(!queue_1_0_full)
    ,.msgb(msg_1_1) ,.ackb(!queue_1_1_full)
    ,.sel(splitter1_sel) ,.default_option({WID{1'b0}})
);

wire softreset;
wire writemsg_0_0 = msgValid(msg_0_0);
wire [WBUFS-1:0] queue_0_0_index_raw;
syncfifo #(WBUFS,4) queue_0_0 (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(writemsg_0_0),.datain(free0indx)
    ,.full(queue_0_0_full),.empty(queue_0_0_empty),.overflow(),.count()
    ,.readout(msg_0_0_ack),.dataout(queue_0_0_index_raw)
);

wire [WBUFS-1:0]  queue_0_0_index = queue_0_0_empty ? NOTLEGAL : queue_0_0_index_raw;



wire writemsg_0_1 = msgValid(msg_0_1);
wire [WBUFS-1:0] queue_0_1_index_raw;
syncfifo #(WBUFS,4) queue_0_1 (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(writemsg_0_1),.datain(free0indx)
    ,.full(queue_0_1_full),.empty(queue_0_1_empty),.overflow(),.count()
    ,.readout(msg_0_1_ack),.dataout(queue_0_1_index_raw)
);

wire [WBUFS-1:0]  queue_0_1_index = queue_0_1_empty ? NOTLEGAL : queue_0_1_index_raw;






wire writemsg_1_0 = msgValid(msg_1_0);
wire [WBUFS-1:0] queue_1_0_index_raw;
syncfifo #(WBUFS,4) queue_1_0 (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(writemsg_1_0),.datain(free1indx)
    ,.full(queue_1_0_full),.empty(queue_1_0_empty),.overflow(),.count()
    ,.readout(msg_1_0_ack),.dataout(queue_1_0_index_raw)
);

wire [WBUFS-1:0]  queue_1_0_index = queue_1_0_empty ? NOTLEGAL : queue_1_0_index_raw;



wire writemsg_1_1 = msgValid(msg_1_1);
wire [WBUFS-1:0] queue_1_1_index_raw;
syncfifo #(WBUFS,4) queue_1_1 (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(writemsg_1_1),.datain(free1indx)
    ,.full(queue_1_1_full),.empty(queue_1_1_empty),.overflow(),.count()
    ,.readout(msg_1_1_ack),.dataout(queue_1_1_index_raw)
);

wire [WBUFS-1:0]  queue_1_1_index = queue_1_1_empty ? NOTLEGAL : queue_1_1_index_raw;





wire [WBUFS-1:0] msgout0index,msgout1index;




msg_joiner2_narrow #(WBUFS) joiner0 (.msga(queue_0_0_index),.msgb(queue_1_0_index),.msgout(msgout0index),.msgsrc(),.msgout_ack(ack_out0[0])
    ,.msga_ack(msg_0_0_ack)
    ,.msgb_ack(msg_1_0_ack)
);

assign rou_out0 = (msgout0index==NOTLEGAL) ? {WID{1'b0}} : bufs[msgout0index];
assign rou_out1 = (msgout1index==NOTLEGAL) ? {WID{1'b0}} : bufs[msgout1index];

assign rou_out0_seen = (msgout0index==NOTLEGAL) ? 1'b0 : !seens[msgout0index];
assign rou_out1_seen = (msgout1index==NOTLEGAL) ? 1'b0 : !seens[msgout1index];



msg_joiner2_narrow #(WBUFS) joiner1 (.msga(queue_1_1_index),.msgb(queue_0_1_index),.msgout(msgout1index),.msgsrc(),.msgout_ack(ack_out1[0])
    ,.msga_ack(msg_1_1_ack)
    ,.msgb_ack(msg_0_1_ack)
);














reg [BUFS-1:0] occupied;
wire [5:0] availables;

rou_availables #(BUFS,WBUFS) rou_availables (
    .occupied(occupied),.availables(availables)
    ,.free0indx(free0indx)
    ,.free1indx(free1indx)
    ,.free2indx(free2indx)
);


wire use0free = writemsg_0_0 || writemsg_0_1 ;

wire [WBUFS-1:0] zeroes = 0;
wire [BUFS-1:0] clear_occupied = 
    ((msgout0index==NOTLEGAL) ? zeroes : msgout0index) 
    |((msgout1index==NOTLEGAL) ? zeroes : msgout1index) 
    ;   

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin 
        occupied <= 0;
    end else if (softreset) begin
        occupied <= 0;
    end else begin
        occupied <= (~clear_occupied & occupied)
            | (use0free ?  ( 1<<free0indx) : zeroes)
            | (use1free ?  ( 1<<free1indx) : zeroes)
            ;   
    end 
end

wire use1free = writemsg_1_0 || writemsg_1_1;
always @(posedge clk) begin
    if (use0free) bufs[free0indx] <= rou_in0;
    if (use1free) bufs[free1indx] <= rou_in1;
end    
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        seens <= 0;
    end else begin
        if (writemsg_0_0)      seens[free0indx] <= rou_in0_seen;
        else if (writemsg_0_1) seens[free0indx] <= 1'b0;

        if (writemsg_1_0)      seens[free1indx] <= rou_in1_seen;
        else if (writemsg_1_1) seens[free1indx] <= 1'b0;
    end
end


bridge2_manager bridge2_manager (.clk(clk),.rst_n(rst_n)
    ,.rou_in0(rou_in0),.rou_in0_seen(rou_in0_seen),.splitter0_sel(splitter0_sel)
    ,.rou_in1(rou_in1),.rou_in1_seen(rou_in1_seen),.splitter1_sel(splitter1_sel)
    ,.softreset(softreset)
);







function msgValid(input [WID-1:0] msg);
begin
    msgValid = msg[1:0] !=0;
end
endfunction



endmodule



