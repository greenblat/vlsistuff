

module rou_admin # (
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
    ,input rou_in_seen, output rou_out_seen
    ,input  [WID-1:0] rou_in, output [2:0] ack_in
    ,output [WID-1:0] rou_out, input [2:0] ack_out

    ,output [7:0]  req_count
    ,input [63:0]  req_data
    ,input [2:0]   req_addr
    ,input         req_write


    ,output  [7:0] resp_count
    ,output [63:0] resp_data
    ,input   [2:0] resp_addr
    ,input         resp_read

    ,input [31:0] pages, input [31:0] whoami
    ,input seen_monitor
);


reg [195:0] request_msg;
reg req_fifo_write;

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        req_fifo_write <= 0;
    end else begin
        req_fifo_write <= req_write && (req_addr==2);
    end
end
always @(posedge clk) begin
    if (req_write) begin
        case (req_addr)
        0: request_msg[63:0] <= req_data;
        1: request_msg[127:64] <= req_data;
        2: request_msg[195:128] <= req_data;
        endcase
    end
end

wire softreset=0;
wire [WID-1:0] msg_out_bef;
wire request_fifo_empty;
wire msg_out_ack;
syncfifo #(WID,4) request_fifo (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(req_fifo_write),.datain(request_msg[WID-1:0])
    ,.full(),.empty(request_fifo_empty),.overflow(),.count(req_count[2:0])
    ,.readout(msg_out_ack),.dataout(msg_out_bef)
);
assign req_count[7:3] = 0;

wire [WID-1:0] msg_out =  request_fifo_empty ? {WID{1'b0}} : msg_out_bef;



wire [WID-1:0] msg_in;
wire resp_fifo_full,resp_fifo_empty;
wire resp_fifo_write =  msg_in[1:0] != 0;
wire resp_readout = resp_read && (resp_addr==3);
assign msg_in_ack = !resp_fifo_full && resp_fifo_write;
rou_nif nif (
     .clk(clk) ,.rst_n(rst_n)
    ,.ack_in(ack_in[2:0])
    ,.ack_out(ack_out[2:0])
    ,.msg_in(msg_in[(WID - 1):0])
    ,.msg_in_ack(msg_in_ack)
    ,.msg_out(msg_out[(WID - 1):0])
    ,.msg_out_ack(msg_out_ack)
    ,.rou_in_seen(rou_in_seen) ,.rou_out_seen(rou_out_seen)
    ,.rou_in(rou_in[(WID - 1):0])
    ,.rou_out(rou_out[(WID - 1):0])
    ,.uses_pages(pages[15:0])
    ,.whoami(whoami[15:0])
    ,.seen_monitor(seen_monitor)
);
wire [WID-1:0] resp_whole_data;
syncfifo #(WID,4) resp_fifo (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(resp_fifo_write),.datain(msg_in)
    ,.full(resp_fifo_full),.empty(resp_fifo_empty),.overflow(),.count(resp_count[2:0])
    ,.readout(resp_readout),.dataout(resp_whole_data)
);
assign resp_count[7:3] = 0;

wire [195:0] msg_extend = 196'b0 | resp_whole_data;
assign resp_data = 
    (resp_addr==0) ?  msg_extend[63:0] :
    (resp_addr==1) ?  msg_extend[127:64] :
    (resp_addr==2)  ? msg_extend[195:128] :
    196'b0;


endmodule




