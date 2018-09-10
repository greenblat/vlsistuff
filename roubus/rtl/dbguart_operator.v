

module dbguart_operator #(
    parameter DWID = 128 
    ,parameter AWID = 32
    ,parameter TWID = 5 
    ,parameter BWID = 
        (DWID==512)  ? 6 : 
        (DWID==256)  ? 5 : 
        (DWID==128) ? 4 : 
        (DWID==64)  ? 3 : 2 
    ,parameter WID = 2+DWID+AWID+BWID+TWID
) (
     input clk, input rst_n , input softreset
    ,input [7:0] status
    ,output [7:0] txdata
    ,input [7:0] rxdata
    ,input rx_valid
    ,input tx_empty
    ,output read_rx
    ,output write_tx
    ,output [15:0] baudrate



    ,input [WID-1:0] msg_in
    ,output msg_in_ack

    ,output [WID-1:0] msg_out
    ,input  msg_out_ack


    ,output [7:0] uart_control
    ,input [31:0] control
    ,input [AWID-1:0] base_address

);

wire [7:0] addr;
wire rsel,rwrite;
wire [31:0] wrdata,rddata;
wire [1:0] rsize = 2;


dbguart_rgf dbguart_rgf (
     .clk(clk) ,.rst_n(rst_n)
    ,.addr(addr[4:0])
    ,.base_address(base_address[31:0])
    ,.baudrate(baudrate[15:0])
    ,.control(control[31:0])
    ,.rdata(rddata[31:0])
    ,.rsel(rsel)
    ,.rsize(rsize[1:0])
    ,.rwrite(rwrite)
    ,.uart_control(uart_control[7:0])
    ,.wrdata(wrdata[31:0])
);




assign read_rx = 0;


wire in_msg_fifo_full,in_msg_fifo_empty,take_msg_in;
wire [WID-1:0] msg_in_raw;
syncfifo #(WID,4) in_msg_fifo (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(msg_in[1:0]!=2'b00),.datain(msg_in)
    ,.full(in_msg_fifo_full),.empty(in_msg_fifo_empty),.overflow(),.count()
    ,.readout(take_msg_in),.dataout(msg_in_raw)
);

assign msg_in_ack = !in_msg_fifo_full;

wire [1:0] msg_in_cmd;
wire [AWID-1:0] msg_in_addr;
wire [DWID-1:0] msg_in_data;
wire [TWID-1:0] msg_in_tags;
wire [BWID-1:0] msg_in_bytes;

rou_msg_fields msg_in_fields(.msg(msg_in_raw), .addr(msg_in_addr) ,.tags(msg_in_tags) ,.bytes(msg_in_bytes) ,.cmd(msg_in_cmd) ,.data(msg_in_data));

wire [415:0] hcmd;
hexdigits #(2,1) hcmd_builder (.infield(msg_in_cmd),.outchar(hcmd[7:0]));
assign hcmd[15:8] = 8'h20;
hexdigits #(TWID,2) htags_builder (.infield(msg_in_tags),.outchar(hcmd[31:16]));
assign hcmd[39:32] = 8'h20;
hexdigits #(BWID,2) hbyts_builder (.infield(msg_in_bytes),.outchar(hcmd[55:40]));

assign hcmd[63:56] = 8'h20;
hexdigits #(AWID,8) haddr_builder (.infield(msg_in_addr),.outchar(hcmd[127:64]));
assign hcmd[135:128] = 8'h20;
hexdigits #(32,8) hdata0_builder (.infield(msg_in_data[127:96]),.outchar(hcmd[199:136]));
assign hcmd[207:200] = 8'h20;
hexdigits #(32,8) hdata1_builder (.infield(msg_in_data[95:64]),.outchar(hcmd[271:208]));
assign hcmd[279:272] = 8'h20;
hexdigits #(32,8) hdata2_builder (.infield(msg_in_data[63:32]),.outchar(hcmd[343:280]));
assign hcmd[351:344] = 8'h20;
hexdigits #(32,8) hdata3_builder (.infield(msg_in_data[31:0]),.outchar(hcmd[415:352]));


reg msg_in_active,rx_echo_active;
reg [5:0] msg_cnt;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        msg_in_active <= 1'b0;
        msg_cnt <= 0;
    end else begin
        if (!msg_in_active &&  !in_msg_fifo_empty && !rx_echo_active) begin
            msg_in_active<=1'b1;
            msg_cnt <= 1'b0;
        end else if (msg_in_active) begin
            if (!tx_fifo_full) begin
                if (msg_cnt==52) begin
                    msg_cnt <=0;
                    msg_in_active<=1'b0;
                end else msg_cnt <= msg_cnt + 1'b1;
            end
        end
    end
end

wire [7:0] generated_txdata;
reg generated_active;
assign take_msg_in = (msg_cnt==52) && !tx_fifo_full && msg_in_active;
wire [7:0] msg_in_txdata = (msg_cnt==52) ? 8'ha : (hcmd >> (msg_cnt*8));
wire [7:0] txdata_for_fifo = 
    msg_in_active ? msg_in_txdata : 
    rx_echo_active ? rxdata_raw : 
    generated_txdata;

wire txdata_write = msg_in_active || (rx_echo_active && !rx_fifo_empty) || generated_active;

wire tx_fifo_full,tx_fifo_empty;
syncfifo #(8,60) txdata_fifo (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(txdata_write),.datain(txdata_for_fifo)
    ,.full(tx_fifo_full),.empty(tx_fifo_empty),.overflow(),.count()
    ,.readout(tx_empty),.dataout(txdata)
);

assign write_tx = !tx_fifo_empty;

wire [7:0] rxdata_raw;
wire rxfifo_readout = rx_echo_active;

syncfifo #(8,8) rxdata_fifo (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.validin(rx_valid),.datain(rxdata)
    ,.full(rx_fifo_full),.empty(rx_fifo_empty),.overflow(),.count()
    ,.readout(rxfifo_readout),.dataout(rxdata_raw)
);

reg [7:0] rxmsg [0:59];
reg [5:0] rxptr;


wire start_rx_echo = (!rx_echo_active && !rx_fifo_empty && !msg_in_active && in_msg_fifo_empty && !generated_active);
wire start_rx_analysis = (rx_echo_active && !rx_fifo_empty && (rxdata==8'ha));
reg rx_msg_used;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        rx_echo_active <= 1'b0;
        rxptr <= 0;
        rx_msg_used<=1;
    end else begin
        if (start_rx_echo) begin
            rx_echo_active <= 1'b1;
        end else if (rx_echo_active && !rx_fifo_empty && (rxdata_raw==8'ha)) begin
            rx_echo_active <= 1'b0;
        end
        if (rx_echo_active && !rx_fifo_empty) begin
            rxptr <= rxptr+1;
        end else if (start_rx_echo) begin
            rxptr<= 0;
            rx_msg_used<=0;
        end else if (start_rx_analysis && msg_out_ack)  begin
            rx_msg_used<=1;
        end
    end
end
always @(posedge clk) begin
    if (rx_echo_active && !rx_fifo_empty) rxmsg[rxptr] <= rxdata_raw;
end

wire [7:0] LET_Question = 8'h3f; 
wire [7:0] LET_Exclamation = 8'h21;
wire [7:0] LET_w = 8'h77; 
wire [7:0] LET_r =  8'h72;
wire [7:0] LET_m = 8'h6d;
wire [7:0] LET_dot = 8'h2e;

wire make_rd_rgf = rxmsg[0]==LET_Question;
wire make_wr_rgf = rxmsg[0]==LET_Exclamation;

wire send_wr_msg = rxmsg[0]==LET_w;
wire send_rd_msg = rxmsg[0]==LET_r;
wire send_mn_msg = rxmsg[0]==LET_m;
wire send_msg = (send_wr_msg||send_rd_msg||send_mn_msg) &&  start_rx_analysis;


// rgf access
assign  rwrite = make_wr_rgf && start_rx_analysis;
assign  rsel = (make_wr_rgf || make_rd_rgf) && start_rx_analysis;
assign addr = hexvalue(rxmsg[1],rxmsg[2]);
assign wrdata[7:0]  = hexvalue(rxmsg[3],rxmsg[4]);
assign wrdata[15:8]  = hexvalue(rxmsg[5],rxmsg[6]);
assign wrdata[23:16]  = hexvalue(rxmsg[7],rxmsg[8]);
assign wrdata[31:24]  = hexvalue(rxmsg[9],rxmsg[10]);


wire [7:0] send_tags = hexvalue(rxmsg[1],rxmsg[2]);
wire [7:0] send_bytes = hexvalue(8'h0,rxmsg[3]);
wire [31:0] send_addr_raw;
assign send_addr_raw[31:24] = hexvalue(rxmsg[5],rxmsg[6]);
assign send_addr_raw[23:16] = hexvalue(rxmsg[7],rxmsg[8]);
assign send_addr_raw[15:8] = hexvalue(rxmsg[9],rxmsg[10]);
assign send_addr_raw[7:0] = hexvalue(rxmsg[12],rxmsg[11]);

wire [31:0] send_addr = 
    (rxmsg[12]==LET_dot) ? (send_addr_raw>>4) :
    (rxmsg[11]==LET_dot) ? (send_addr_raw>>8) :
    (rxmsg[10]==LET_dot) ? (send_addr_raw>>12) :
    (rxmsg[9]==LET_dot) ? (send_addr_raw>>16) :
    (rxmsg[8]==LET_dot) ? (send_addr_raw>>20) :
    (rxmsg[7]==LET_dot) ? (send_addr_raw>>24) :
    (rxmsg[6]==LET_dot) ? (send_addr_raw>>28) :
    0 ;

wire [5:0] sdp = 
    (rxmsg[5]==LET_dot) ?  6 :
    (rxmsg[6]==LET_dot) ?  7 :
    (rxmsg[7]==LET_dot) ?  8 :
    (rxmsg[8]==LET_dot) ?  9 :
    (rxmsg[9]==LET_dot) ?  10 :
    (rxmsg[10]==LET_dot) ?  11 :
    (rxmsg[11]==LET_dot) ?  12 :
    (rxmsg[12]==LET_dot) ?  13 :
    14 ;

wire [127:0] send_data_raw;
assign send_data_raw[127:120] = hexvalue(rxmsg[sdp],rxmsg[sdp+1]);
assign send_data_raw[119:112] = hexvalue(rxmsg[sdp+2],rxmsg[sdp+3]);
assign send_data_raw[111:104] = hexvalue(rxmsg[sdp+4],rxmsg[sdp+5]);
assign send_data_raw[103:96]  = hexvalue(rxmsg[sdp+6],rxmsg[sdp+7]);
assign send_data_raw[95:88]   = hexvalue(rxmsg[sdp+8],rxmsg[sdp+9]);
assign send_data_raw[87:80]   = hexvalue(rxmsg[sdp+10],rxmsg[sdp+11]);
assign send_data_raw[79:72]   = hexvalue(rxmsg[sdp+12],rxmsg[sdp+13]);
assign send_data_raw[71:64]   = hexvalue(rxmsg[sdp+14],rxmsg[sdp+15]);
assign send_data_raw[63:56]   = hexvalue(rxmsg[sdp+16],rxmsg[sdp+17]);
assign send_data_raw[55:48]   = hexvalue(rxmsg[sdp+18],rxmsg[sdp+19]);
assign send_data_raw[47:40]   = hexvalue(rxmsg[sdp+20],rxmsg[sdp+21]);
assign send_data_raw[39:32]   = hexvalue(rxmsg[sdp+22],rxmsg[sdp+23]);
assign send_data_raw[31:24]   = hexvalue(rxmsg[sdp+24],rxmsg[sdp+25]);
assign send_data_raw[23:16]   = hexvalue(rxmsg[sdp+26],rxmsg[sdp+27]);
assign send_data_raw[15:8]    = hexvalue(rxmsg[sdp+28],rxmsg[sdp+29]);
assign send_data_raw[7:0]     = hexvalue(rxmsg[sdp+30],rxmsg[sdp+31]);

wire [127:0] send_data = 
    (rxmsg[sdp]==LET_dot) ? 0 :
    (rxmsg[sdp+1]==LET_dot) ? send_data_raw[127:124] :
    (rxmsg[sdp+2]==LET_dot) ? send_data_raw[127:120] :
    (rxmsg[sdp+3]==LET_dot) ? send_data_raw[127:116] :
    (rxmsg[sdp+4]==LET_dot) ? send_data_raw[127:112] :
    (rxmsg[sdp+5]==LET_dot) ? send_data_raw[127:108] :
    (rxmsg[sdp+6]==LET_dot) ? send_data_raw[127:104] :
    (rxmsg[sdp+7]==LET_dot) ? send_data_raw[127:100] :
    (rxmsg[sdp+8]==LET_dot) ? send_data_raw[127:96] :
    (rxmsg[sdp+9]==LET_dot) ? send_data_raw[127:92] :
    (rxmsg[sdp+10]==LET_dot) ? send_data_raw[127:88] :
    (rxmsg[sdp+11]==LET_dot) ? send_data_raw[127:84] :
    (rxmsg[sdp+12]==LET_dot) ? send_data_raw[127:80] :
    (rxmsg[sdp+13]==LET_dot) ? send_data_raw[127:76] :
    (rxmsg[sdp+14]==LET_dot) ? send_data_raw[127:72] :
    (rxmsg[sdp+15]==LET_dot) ? send_data_raw[127:68] :
    (rxmsg[sdp+16]==LET_dot) ? send_data_raw[127:64] :
    (rxmsg[sdp+17]==LET_dot) ? send_data_raw[127:60] :
    (rxmsg[sdp+18]==LET_dot) ? send_data_raw[127:56] :
    (rxmsg[sdp+19]==LET_dot) ? send_data_raw[127:52] :
    (rxmsg[sdp+20]==LET_dot) ? send_data_raw[127:48] :
    (rxmsg[sdp+21]==LET_dot) ? send_data_raw[127:44] :
    (rxmsg[sdp+22]==LET_dot) ? send_data_raw[127:40] :
    (rxmsg[sdp+23]==LET_dot) ? send_data_raw[127:36] :
    (rxmsg[sdp+24]==LET_dot) ? send_data_raw[127:32] :
    (rxmsg[sdp+25]==LET_dot) ? send_data_raw[127:28] :
    (rxmsg[sdp+26]==LET_dot) ? send_data_raw[127:24] :
    (rxmsg[sdp+27]==LET_dot) ? send_data_raw[127:20] :
    (rxmsg[sdp+28]==LET_dot) ? send_data_raw[127:16] :
    (rxmsg[sdp+29]==LET_dot) ? send_data_raw[127:12] :
    (rxmsg[sdp+30]==LET_dot) ? send_data_raw[127:8] :
    (rxmsg[sdp+31]==LET_dot) ? send_data_raw[127:4] :
    send_data_raw;


wire [1:0] send_cmd_wire = 
    send_wr_msg ? 2'b10 : 
    send_rd_msg ? 2'b01 : 
    send_mn_msg ? 2'b11 : 
    2'b00;

reg [1:0] send_cmd;
assign msg_out = {send_data,send_addr,send_bytes[BWID-1:0],send_tags[TWID-1:0],send_cmd};

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        send_cmd <= 2'b0;
    end else begin
        if (send_cmd!=0) begin
            send_cmd <= 2'b00;
        end else if (!rx_msg_used && start_rx_analysis && msg_out_ack) begin
            send_cmd <= send_cmd_wire;
        end
    end
end

reg [5:0] gen_ptr;
wire [63:0] hexrdata;
assign generated_txdata = (gen_ptr==8) ? 8'ha : (hexrdata >> (gen_ptr*8));
hexdigits #(4,1) rdt0 (.infield(rrdata[3:0]),.outchar(hexrdata[63:56]));
hexdigits #(4,1) rdt1 (.infield(rrdata[7:4]),.outchar(hexrdata[55:48]));
hexdigits #(4,1) rdt2 (.infield(rrdata[11:8]),.outchar(hexrdata[47:40]));
hexdigits #(4,1) rdt3 (.infield(rrdata[15:12]),.outchar(hexrdata[39:32]));
hexdigits #(4,1) rdt4 (.infield(rrdata[19:16]),.outchar(hexrdata[31:24]));
hexdigits #(4,1) rdt5 (.infield(rrdata[23:20]),.outchar(hexrdata[23:16]));
hexdigits #(4,1) rdt6 (.infield(rrdata[27:24]),.outchar(hexrdata[15:8]));
hexdigits #(4,1) rdt7 (.infield(rrdata[31:28]),.outchar(hexrdata[7:0]));

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        generated_active <= 1'b0;
        gen_ptr <= 0;
    end else begin
        if (send_msg &&  !generated_active && !rx_echo_active &&  !msg_in_active)  begin
            generated_active <= 1'b1;
            gen_ptr <= 0;
        end else if (generated_active) begin
            if (!tx_fifo_full) begin
                if (gen_ptr==8)  begin
                   generated_active <= 1'b0; 
                   gen_ptr <= 0;
                end else begin
                    gen_ptr <= gen_ptr+1;
                end
            end                    
        end
    end
end

function [7:0] hexvalue (input [7:0] aa, input [7:0] bb);
begin
    hexvalue = {hexnibble(aa),hexnibble(bb)};
end
endfunction

function [3:0] hexnibble (input [7:0] aa);
begin
    if ((aa>=8'h30)&&(aa<=8'h39)) 
        hexnibble = aa[3:0];
    else if ((aa>=8'h61)&&(aa<=8'h66)) 
        hexnibble = aa[3:0]+9;
    else if ((aa>=8'h41)&&(aa<=8'h46)) 
        hexnibble = aa[3:0]+9;
    else
        hexnibble = 0;
end
endfunction


endmodule




