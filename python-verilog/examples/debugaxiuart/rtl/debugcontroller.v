


module debugcontroller (
    input clk, input rst_n
    ,output softreset

    ,input rx_fifo_empty, input [7:0] rx_fifo_data, output rx_fifo_read
    ,input tx_fifo_full,  output [7:0] tx_fifo_data, output tx_fifo_write

    ,input lcl_empty
    ,input [32+4+2+1 -1:0] lcl_data
    ,output lcl_read

    ,input [6:0] bresp_bid
    ,output bresp_bid_pulse
    ,input bresp_empty



    ,output        rgf_sel
    ,output        rgf_wr
    ,output [31:0] rgf_wdata
    ,output [7:0]  rgf_addr
    ,input  [31:0] rgf_rdata



// direct commands port
    ,input arvalid
    ,input awvalid
    ,input arready
    ,input awready


    ,input lcl_rd_full





);



reg [15:0] stk_addr;
reg [31:0] stk_data;

wire [7:0] CHR0 = 8'h30;
wire [7:0] CHR9 = 8'h39;
wire [7:0] CHRA = 8'h41;
wire [7:0] CHRF = 8'h46;
wire [7:0] CHRa = 8'h61;
wire [7:0] CHRb = 8'h62;
wire [7:0] CHRf = 8'h66;
wire [7:0] CHRr = 8'h72;
wire [7:0] CHRdot = 8'h2e;
wire [7:0] CHRnewline = 8'ha;
wire [3:0] hexval = 
    ((rx_fifo_data>=CHR0)&&(rx_fifo_data<=CHR9)) ? (rx_fifo_data-CHR0) :
    ((rx_fifo_data>=CHRA)&&(rx_fifo_data<=CHRF)) ? (rx_fifo_data-CHRA+10) :
    ((rx_fifo_data>=CHRa)&&(rx_fifo_data<=CHRf)) ? (rx_fifo_data-CHRa+10) :
    0;

wire hexvalid = 
    ((rx_fifo_data>=CHR0)&&(rx_fifo_data<=CHR9)) ? 1 :
    ((rx_fifo_data>=CHRA)&&(rx_fifo_data<=CHRF)) ? 1 :
    ((rx_fifo_data>=CHRa)&&(rx_fifo_data<=CHRf)) ? 1 :
    0;

wire pusha_flag,pushd_flag,clear_flag,echo_flag;
wire write_flag0,read_flag0;
wire write_flag  = write_flag0;
wire read_flag  = read_flag0;
reg was_read_flag; always @(posedge clk) was_read_flag <= read_flag;
reg was_write_flag; always @(posedge clk) was_write_flag <= write_flag;
always @(posedge clk) begin
    if (clear_flag) begin
        stk_addr <= 0;
        stk_data <= 0;
    end else begin
        if (pusha_flag) begin
            stk_addr <= {stk_addr[11:0],hexval};
        end
        if (pushd_flag) begin
            stk_data <= {stk_data[27:0],hexval};
        end
    end
end
wire enable;
state_machine state_machine (.clk(clk),.rst_n(rst_n),.datain(rx_fifo_data),.validin(!rx_fifo_empty),.enable(enable)
    ,.pusha_flag(pusha_flag),.pushd_flag(pushd_flag),.clear_flag(clear_flag),.echo_flag(echo_flag),.write_flag(write_flag0),.read_flag(read_flag0)
    ,.idle_state(idle_state)
);


reg [3:0] lcl_pos,bresp;
assign enable = (lcl_pos==0)&&(bresp==0);
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        lcl_pos <= 0;
    end else begin
        if (lcl_pos==0) begin
            if (!lcl_empty && idle_state && (bresp==0)) begin
                lcl_pos <= 13;
            end 
        end else if (lcl_pos>0) begin
           lcl_pos <= lcl_pos -1;
        end
    end
end
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        bresp <= 0;
    end else begin
        if ((bresp==0) && !bresp_empty && idle_state && (lcl_pos==0) && lcl_empty) begin
            bresp <= 4'h8;
        end else if (bresp!=0) begin
            bresp <= bresp >> 1;
        end
    end
end

wire [7:0] lcl_byte = 
    bresp[3] ?  CHRb :
    bresp[2] ?  hexbyte(bresp_bid[6:4]) :
    bresp[1] ?  hexbyte(bresp_bid[3:0]) :
    bresp[0] ?  CHRnewline :
    (lcl_pos==13) ? CHRr :
    (lcl_pos==12) ? hexbyte(lcl_data[38:36]) :
    (lcl_pos==11) ? hexbyte(lcl_data[35:32]) :
    (lcl_pos==10) ? CHRdot :

    (lcl_pos==9) ? hexbyte(lcl_data[31:28]) :
    (lcl_pos==8) ? hexbyte(lcl_data[27:24]) :
    (lcl_pos==7) ? hexbyte(lcl_data[23:20]) :
    (lcl_pos==6) ? hexbyte(lcl_data[19:16]) :
    (lcl_pos==5) ? hexbyte(lcl_data[15:12]) :
    (lcl_pos==4) ? hexbyte(lcl_data[11:08]) :
    (lcl_pos==3) ? hexbyte(lcl_data[07:04]) :
    (lcl_pos==2) ? hexbyte(lcl_data[03:00]) :
    (lcl_pos==1) ?  CHRnewline : 0;

assign rx_fifo_read = echo_flag;
assign tx_fifo_data = echo_flag ?  rx_fifo_data : lcl_byte;
assign tx_fifo_write = (echo_flag || (lcl_pos>0) || (bresp!=0));
assign lcl_read = (lcl_pos==1);
assign bresp_bid_pulse = bresp[0];
assign rgf_sel = was_read_flag || was_write_flag;
assign rgf_wr = was_write_flag;
assign rgf_wdata = stk_data;
assign rgf_addr = stk_addr;
assign softreset = 0;

function [7:0] hexbyte (input [3:0] nibble);
begin
    if (nibble<10) hexbyte = 8'h30 + nibble;
    else           hexbyte = 8'h41 + nibble - 10;
end
endfunction




endmodule

