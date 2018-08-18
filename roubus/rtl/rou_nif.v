

module rou_nif #(
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
    input clk, input rst_n, input seen_monitor
    ,input  [WID-1:0] rou_in, input rou_in_seen, output [2:0] ack_in
    ,output [WID-1:0] rou_out, output rou_out_seen,  input [2:0] ack_out

    ,input [15:0] uses_pages
    ,input [15:0] whoami

    ,output [WID-1:0] msg_in
    ,input msg_in_ack

    ,input [WID-1:0] msg_out
    ,output  msg_out_ack


    ,output [31:0] control
    ,output [AWID-1:0] base_address
);

wire softreset = control[0];
parameter BUFS = 8;
reg [WID-1:0] bufs [0:BUFS-1];
reg [BUFS-1:0] seens;
parameter WBUFS = 3+$clog2(BUFS);
parameter NOTLEGAL= (1<<WBUFS)-1;
wire [WBUFS-1:0] free0indx,free1indx,free2indx,queue0index,queue1index,queue2index,queue3index,queue5index,queue6index,queue7index,queue8index,queue9index;

wire [WID-1:0] msg6,msg7,msg1a,msg6a;

wire [1:0] splitter0_sel;
wire [WID-1:0] msg0,msg1,msg2;
wire msg0_ack,msg1_ack,msg2_ack;
assign ack_in[2:1] = 0;
msg_splitter3 #(WID) splitter0 (.msgin(rou_in),.msginack(ack_in[0]),.msga(msg2),.msgb(msg1),.msgc(msg0),.sel(splitter0_sel)
    ,.acka(msg2_ack), .ackb(msg1_ack), .ackc(msg0_ack)
    ,.default_option({WID{1'b0}})
);

wire queue2_full,queue2_empty;
wire writemsg2 = msgValid(msg2);
wire [WBUFS-1:0] queue2index_raw;
syncfifo #(WBUFS,4) queue2 (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(writemsg2),.datain(free0indx)
    ,.full(queue2_full),.empty(queue2_empty),.overflow(),.count()
    ,.readout(msg_in_ack),.dataout(queue2index_raw)
);

assign queue2index = queue2_empty ? NOTLEGAL : queue2index_raw;
assign msg2_ack = !queue2_full;
assign msg_in = (queue2index==NOTLEGAL) ? {WID{1'b0}} : bufs[queue2index];


wire queue0_full,queue0_empty;
wire writemsg0 = msgValid(msg0);
wire [WBUFS-1:0] queue3index_raw;
syncfifo #(WBUFS,4) queue0 (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(writemsg0),.datain(free0indx)
    ,.full(queue0_full),.empty(queue0_empty),.overflow(),.count()
    ,.readout(msg3_ack),.dataout(queue3index_raw)
);
assign queue3index = queue0_empty ? NOTLEGAL : queue3index_raw;
assign msg0_ack = !queue0_full;


wire queue1_full,queue1_empty;
wire writemsg1 = msgValid(msg1);
assign msg1_ack = !queue1_full;
wire [WBUFS-1:0] queue1index_raw;
syncfifo #(WBUFS,4) queue1 (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(writemsg1),.datain(free0indx)
    ,.full(queue1_full),.empty(queue1_empty),.overflow(),.count()
    ,.readout(msg1a_ack),.dataout(queue1index_raw)
);

assign queue1index = queue1_empty ? NOTLEGAL : queue1index_raw;

wire queue8_full,queue8_empty;
wire [WBUFS-1:0] msg8index,queue8index_raw;
syncfifo #(WBUFS,4) queue8 (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(msg8index!=NOTLEGAL),.datain(msg8index)
    ,.full(queue8_full),.empty(queue8_empty),.overflow(),.count()
    ,.readout(msg8a_ack),.dataout(queue8index_raw)
);
wire msg8_ack = !queue8_full;

assign queue8index = queue8_empty ? NOTLEGAL : queue8index_raw;


wire [WBUFS-1:0] queue7aindex,msg9index;
msg_joiner3_narrow #(WBUFS) joiner1 (.msga(queue1index),.msgb(queue8index),.msgc(queue7aindex),.msgout(msg9index),.msgout_ack(msg9_ack)
    ,.msga_ack(msg1a_ack)
    ,.msgb_ack(msg8a_ack)
    ,.msgc_ack(msg7a_ack)
);

wire queue9_full,queue9_empty;
wire [WBUFS-1:0] queue9index_raw;
syncfifo #(WBUFS,4) queue9 (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(msg9index!=NOTLEGAL),.datain(msg9index)
    ,.full(queue9_full),.empty(queue9_empty),.overflow(),.count()
    ,.readout(ack_out!=0),.dataout(queue9index_raw)
);
assign queue9index = queue9_empty ? NOTLEGAL : queue9index_raw;
assign msg9_ack = !queue9_full;
assign rou_out = (queue9index==NOTLEGAL) ? {WID{1'b0}} : bufs[queue9index];
assign rou_out_seen = (queue9index==NOTLEGAL) ? 1'b0 : (seen_monitor ^ seens[queue9index]);


wire queue5_full,queue5_empty,msg5_ack;

wire writemsgout = msgValid(msg_out);
wire [WBUFS-1:0] queue5index_raw;
syncfifo #(WBUFS,4) queue5 (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(writemsgout),.datain(free1indx)
    ,.full(queue5_full),.empty(queue5_empty),.overflow(),.count()
    ,.readout(msg5_ack),.dataout(queue5index_raw)
);

assign queue5index = queue5_empty ? NOTLEGAL : queue5index_raw;


assign msg_out_ack = !queue5_full;

wire msg6_ack;
wire [1:0] splitter1_sel;
wire [WBUFS-1:0] notlegal = NOTLEGAL;
msg_splitter2 #(WBUFS) splitter1 (.msgin(queue5index),.msginack(msg5_ack)
    ,.msga(queue7index) , .acka(msg7_ack)
    ,.msgb(queue6index) ,.ackb(msg6_ack)
    ,.sel(splitter1_sel) ,.default_option(notlegal)
);

wire [WBUFS-1:0] queue6aindex;
wire queue6_full,queue6_empty;
assign msg6_ack = !queue6_full;
wire [WBUFS-1:0] queue6aindex_raw;
syncfifo #(WBUFS,4) queue6 (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(queue6index!=NOTLEGAL),.datain(queue6index)
    ,.full(queue6_full),.empty(queue6_empty),.overflow(),.count()
    ,.readout(msg6a_ack),.dataout(queue6aindex_raw)
);

assign queue6aindex = queue6_empty ? NOTLEGAL : queue6aindex_raw;

wire queue7_full,queue7_empty;
wire [WBUFS-1:0] queue7aindex_raw;
syncfifo #(WBUFS,4) queue7 (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(queue7index!=NOTLEGAL),.datain(queue7index)
    ,.full(queue7_full),.empty(queue7_empty),.overflow(),.count()
    ,.readout(msg7a_ack),.dataout(queue7aindex_raw)
);

assign queue7aindex = queue7_empty ? NOTLEGAL : queue7aindex_raw;
assign msg7_ack = !queue7_full;



wire [WBUFS-1:0] msg4index;

wire [1:0] msg4src;
msg_joiner2_narrow #(WBUFS) joiner0 (.msga(queue6aindex),.msgb(queue3index),.msgout(msg4index),.msgsrc(msg4src),.msgout_ack(msg4_ack)
    ,.msga_ack(msg6a_ack)
    ,.msgb_ack(msg3_ack)
);

wire [WID-1:0] msg4 = (msg4index==NOTLEGAL) ? {WID{1'b0}} : bufs[msg4index];

wire [WID-1:0] msg8;
wire use2free;
wire [WBUFS-1:0] retiredindx;
wire [WID-1:0] msg5 = (queue5index==NOTLEGAL) ? {WID{1'b0}} : bufs[queue5index];
nif_manager nif_manager(.clk(clk),.rst_n(rst_n)
    ,.msg4(msg4),.msg4index(msg4index),.msg4_ack(msg4_ack)
    ,.msg4src(msg4src)
    ,.msg8index(msg8index),.msg8_ack(msg8_ack)
    ,.msg8(msg8)
    ,.use2free(use2free),.free2indx(free2indx)
    ,.retiredindx(retiredindx)


    ,.rou_in(rou_in),.rou_in_seen(rou_in_seen),.splitter0_sel(splitter0_sel)
    ,.msg5(msg5),.splitter1_sel(splitter1_sel)

    ,.control_bits(control)
    ,.base_address(base_address)
    ,.uses_pages(uses_pages)
    ,.whoami(whoami)
    ,.seen_monitor(seen_monitor)
);


reg [BUFS-1:0] occupied;
wire [5:0] availables;

rou_availables #(BUFS,WBUFS) rou_availables (
    .occupied(occupied),.availables(availables)
    ,.free0indx(free0indx)
    ,.free1indx(free1indx)
    ,.free2indx(free2indx)
);


wire use0free = writemsg2 || writemsg1 || writemsg0 ;
wire use1free = writemsgout ;

wire [WBUFS-1:0] zeroes = 0;
wire [BUFS-1:0] clear_occupied = 
        ((msg_in_ack && !queue2_empty) ?  (1<<queue2index) : zeroes)
      | ((retiredindx!=NOTLEGAL) ? (1<<retiredindx) : zeroes )
      | ((msg_out_ack && !queue9_empty) ? (1<<queue9index) : zeroes)
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
            | (use2free ?  ( 1<<free2indx) : zeroes)
            ;   
    end 
end

always @(posedge clk) begin
    if (writemsg0||writemsg1||writemsg2) bufs[free0indx] <= rou_in;
    if (writemsgout) bufs[free1indx] <= msg_out;
    if (use2free)    bufs[free2indx] <= msg8;
end    
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        seens <= 0;
    end else begin
        if (writemsg1) seens[free0indx] <= rou_in_seen;
        else if (writemsg0||writemsg2) seens[free0indx] <= 1'b0;

        if (writemsgout) seens[free1indx] <= 1'b0;
        if (use2free) seens[free2indx] <= 1'b0;
    end
end








function msgValid(input [WID-1:0] msg);
begin
    msgValid = msg[1:0] !=0;
end
endfunction



endmodule



