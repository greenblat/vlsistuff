

module nif_manager #(
     parameter DWID = 128 
    ,parameter AWID = 32
    ,parameter TWID = 5 
    ,parameter BWID = 
        (DWID==512)  ? 6 : 
        (DWID==256)  ? 5 : 
        (DWID==128) ? 4 : 
        (DWID==64)  ? 3 : 2 
    ,parameter WID = 2+DWID+AWID+BWID+TWID
    ,parameter WBUFS = 6
) (
    input clk, input rst_n, input seen_monitor

    ,input [WID-1:0] rou_in, input rou_in_seen, output [1:0] splitter0_sel
    ,input [WID-1:0] msg5,   output [1:0] splitter1_sel


    ,input [WID-1:0] msg4, input [WBUFS-1:0] msg4index, output msg4_ack
    ,input [1:0] msg4src

    ,output reg use2free
    ,output reg [WBUFS-1:0] msg8index ,input [WBUFS-1:0] free2indx
    ,input msg8_ack
    ,output reg [WID-1:0] msg8
    ,output [WBUFS-1:0] retiredindx


    ,input [15:0] uses_pages
    ,input [15:0] whoami
    ,output reg [31:0] control_bits
    ,output reg [AWID-1:0] base_address

);

parameter NOTLEGAL= (1<<WBUFS)-1;
wire [1:0] rou_in_cmd;
wire [AWID-1:0] rou_in_addr;
wire [DWID-1:0] rou_in_data;
wire [TWID-1:0] rou_in_tags;
wire [BWID-1:0] rou_in_bytes;

reg [AWID-1:0] last_address;
wire rou_in_mngresponce,rou_in_mngrequest;
rou_msg_fields rou_in_fields(.msg(rou_in), .addr(rou_in_addr) ,.tags(rou_in_tags) ,.bytes(rou_in_bytes) ,.cmd(rou_in_cmd) ,.data(rou_in_data));
rou_msg_parser  rou_in_parser (.msg(rou_in),.msg_reset(),.msg_enumerate(),.msg_controls()
    ,.msg_mngrequest(rou_in_mngrequest)
    ,.msg_mngresponce(rou_in_mngresponce)
);

wire our_address = (rou_in_addr>=base_address)&&(rou_in_addr<last_address)&&(base_address!=last_address); 
wire our_data_incoming = ((rou_in_cmd!=0) && our_address) && (rou_in_cmd!=2'b11);
wire our_mng_incoming = (rou_in_cmd==2'b11);
wire transfer_incoming = (rou_in_cmd!=0) && !our_address && !(rou_in_cmd==2'b11);
wire seen_already = is_active_admin && rou_in_seen && seen_monitor;

wire msg4_controls,msg4_mngresponce;
// 1 = down, 2 =  out,  3 = manager.
assign splitter0_sel = 
    seen_already ? 2'd1 :
    (our_data_incoming||((rou_in_mngrequest||rou_in_mngresponce) && is_active_admin)) ? 2'd1 : 
    (transfer_incoming||(rou_in_mngresponce && !is_active_admin)) ? 2'd2 : 
    our_mng_incoming ? 2'd3 : 
    2'd0;

wire [1:0] msg5_cmd;
wire [AWID-1:0] msg5_addr;
wire [DWID-1:0] msg5_data;
wire [TWID-1:0] msg5_tags;
wire [BWID-1:0] msg5_bytes;
rou_msg_fields msg5_fields(.msg(msg5), .addr(msg5_addr) ,.tags(msg5_tags) ,.bytes(msg5_bytes) ,.cmd(msg5_cmd) ,.data(msg5_data));

assign splitter1_sel = 
    (msg5_cmd==2'd3) ? 2'd2 : 
    (msg5_cmd!=2'd0) ? 2'd1 : 
    2'd0;

wire msg4_mngrequest,msg4_report,msg4_bad;
rou_msg_parser  msg4_parser (.msg(msg4),.msg_reset(msg4_reset),.msg_enumerate(msg4_enumerate),.msg_controls(msg4_controls),.msg_mngresponce(msg4_mngresponce)
    ,.msg_report(msg4_report)
    ,.msg_mngrequest(msg4_mngrequest)
    ,.msg_bad(msg4_bad)
);

reg is_active_admin;
reg cannot_be_active_admin;

wire [7:0] panics;
assign panics[0] = msg4_mngresponce && (msg4src==1);
assign panics[1] = msg4_mngrequest && (msg4src==1) && cannot_be_active_admin;
assign panics[7:2] = 0;

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        is_active_admin <= 1'b0;
        cannot_be_active_admin <= 1'b0;
    end else begin
        if (msg4_reset && (!is_active_admin || cannot_be_active_admin)) begin
            is_active_admin <= 1'b0;
            cannot_be_active_admin <= 1'b0;
        end else if (!cannot_be_active_admin && msg4_mngrequest && !msg4_bad) begin
            is_active_admin <= msg4src==1;
            cannot_be_active_admin <= msg4src==2;
        end 
    end 
end

wire [1:0] msg4_cmd;
wire [AWID-1:0] msg4_addr;
wire [DWID-1:0] msg4_data;
wire [TWID-1:0] msg4_tags;
wire [BWID-1:0] msg4_bytes;
wire [WID-1:0] msg8_wire;
reg send_last_address,send_report;
reg [WBUFS-1:0] retired1indx;
reg [WBUFS-1:0] retired2indx;
assign msg4_ack = !send_last_address && !use2free;
wire [31:0] last_address_wire = {msg4_addr[AWID-1:10],10'b0} + {uses_pages,10'b0} + {(msg4_addr[9:0]!=0),10'b0};
wire [WID-1:0] msg8report_wire;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        base_address<=0;
        last_address<=0;
        send_last_address<=1'b0;
        send_report <= 1'b0;
        msg8 <= {WID{1'b0}};
        retired1indx <= NOTLEGAL;
        msg8index <= NOTLEGAL;
        use2free <= 1'b0;
    end else begin
        if (msg4_enumerate) begin
            base_address <= msg4_addr;
            last_address <= last_address_wire;
            send_last_address <= 1'b1;
            msg8 <= msg8_wire;
        end else if (msg4_reset) begin
            base_address <= 0;
            last_address <= 0;
            msg8 <= {WID{1'b0}};
            send_last_address <= 1'b1;
            retired1indx <=msg4index;
        end else if (msg4_report && !send_report) begin
            send_report <= 1'b1;
            msg8index <= msg4index;
            msg8 <= msg8report_wire;
        end else if (send_report &&  (free2indx!=NOTLEGAL)) begin
            send_report <= 1'b1;
            use2free <= 1'b1;
            msg8index <= free2indx;
        end else if (send_last_address && (free2indx!=NOTLEGAL)) begin
            send_last_address <= 1'b0;
            use2free <= 1'b1;
            retired1indx <=NOTLEGAL;
            msg8index <= free2indx;
        end else if (((msg4_addr != base_address)||(msg4_addr ==0)) && msg4_controls) begin
            msg8index <= msg4index;
        end else if (msg4_bad) begin
            retired1indx <=msg4index;
        end else if (msg8_ack) begin
            msg8 <= {WID{1'b0}};
            use2free <= 1'b0;
            msg8index <= NOTLEGAL;
            retired1indx <=NOTLEGAL;
        end
    end
end
rou_msg_fields msg4_fields(.msg(msg4), .addr(msg4_addr) ,.tags(msg4_tags) ,.bytes(msg4_bytes) ,.cmd(msg4_cmd) ,.data(msg4_data));
rou_msg_build  msg8build  (.msg(msg8_wire),.data(msg4_data),.addr(last_address_wire),.tags(msg4_tags) ,.bytes(msg4_bytes) ,.cmd(msg4_cmd));
rou_msg_build  msg8build_report  (.msg(msg8report_wire),.data({DWID{1'b0}}|whoami|{control_bits,16'b0}),.addr(last_address_wire),.tags((msg4_tags|1'b1)) ,.bytes(msg4_bytes) ,.cmd(msg4_cmd));

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        control_bits <= 32'b0;
        retired2indx <= NOTLEGAL;
    end else begin
        if (((msg4_addr == base_address)||(msg4_addr ==0)) && msg4_controls) begin
            control_bits <= msg4_data[31:0];
            if (msg4_addr !=0) retired2indx <= msg4index;
        end else if ((retired2indx!=NOTLEGAL)&&(retired1indx==NOTLEGAL)) begin
            retired2indx <= NOTLEGAL;
        end
    end
end
assign retiredindx =  (retired1indx!=NOTLEGAL)  ? retired1indx : retired2indx;

endmodule

