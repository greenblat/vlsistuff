
// Ilia Greenblat : top level of the RTL design.
// includes uart, regfile and float unit


module fltserver (  input clk, input rst_n, input rxd, output txd);

reg [15:0] baudrate;
reg [7:0] fractional;
wire [15:0] txcount;
wire softreset = 0;
wire tx_empty;
wire write_tx = tx_empty && (txcount>0);

wire [7:0] control = 8'h50;
wire [7:0] rxdata,txdata;
wire [31:0] result;
wire vldout;
wire [7:0] status;
wire rx_valid;
reg [7:0] dst; 

uartx2frac uart (
     .clk(clk)
    ,.rst_n(rst_n)
    ,.baudrate(baudrate[15:0])
    ,.fractional(fractional[7:0])
    ,.control(control[7:0])
    ,.rxd(rxd)
    ,.txd(txd)

    ,.read_rx(rx_valid)
    ,.rx_valid(rx_valid)
    ,.rxdata(rxdata[7:0])
    ,.status(status)
    ,.tx_empty(tx_empty)
    ,.txdata(txdata[7:0])
    ,.write_tx(write_tx)
);


wire [7:0] letA =  97;
wire [7:0] letB =  98;
wire [7:0] letC =  99;
wire [7:0] letD =  100;
wire [7:0] letE =  101;
wire [7:0] letF =  102;
wire [7:0] letG =  103;
wire [7:0] letH =  104;
wire [7:0] letI =  105;
wire [7:0] letJ =  106;
wire [7:0] letK =  107;
wire [7:0] letL =  108;
wire [7:0] letM =  109;
wire [7:0] letN =  110;
wire [7:0] letO =  111;
wire [7:0] letP =  112;
wire [7:0] letQ =  113;
wire [7:0] letR =  114;
wire [7:0] letS =  115;
wire [7:0] letT =  116;
wire [7:0] letU =  117;
wire [7:0] letV =  118;
wire [7:0] letW =  119;
wire [7:0] letX =  120;
wire [7:0] letY =  121;
wire [7:0] letZ =  122;
wire [7:0] letCR =  10;

wire [7:0] let0 =  48;
wire [7:0] let1 =  49;
wire [7:0] let2 =  50;
wire [7:0] let3 =  51;
wire [7:0] let4 =  52;
wire [7:0] let5 =  53;
wire [7:0] let6 =  54;
wire [7:0] let7 =  55;
wire [7:0] let8 =  56;
wire [7:0] let9 =  57;


wire [3:0] reads;
wire writes;
wire [15:0] count,frees;
wire [10*8-1:0] dout;
wire taken;
multififo_w1_r10 #(.WIDTH(8),.DEPTH(32)) rxfifo (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.writes(rx_valid),.din(rxdata)
    ,.reads(reads),.dout(dout)
    ,.count(count)
    ,.frees(frees)
    ,.taken(taken)
);

wire wr_baudrate = (count>=6) && (dout[7:0] == letW) && (dout[15:8] == letB);
wire wr_fractional = (count>=4) && (dout[7:0] == letW) && (dout[15:8] == letF);
wire wr_reg = (count>=10) && (dout[7:0] == letW) && (dout[15:8] >= let0) && (dout[15:8] <= let7);
wire rd_reg = (count>=2) && (dout[7:0] == letR) && (dout[15:8] >= let0) && (dout[15:8] <= let7);
wire work = (count>=7) && (dout[7:0] == letO);
wire pop = (count>10);
wire clean = (count>0)&&(dout[7:0] == letCR);
assign reads = 
    wr_baudrate ? 6 : 
    wr_fractional ? 5 : 
    wr_reg ? 10 :
    rd_reg ? 2 :
    work ? 7 :
    pop ? 1 :
    clean ? count :
    0;

reg [31:0] reg0,reg1,reg2,reg3,reg4,reg5,reg6,reg7;
wire [31:0] fvalue = {
     dhex(dout[23:16]),dhex(dout[31:24]),dhex(dout[39:32]),dhex(dout[47:40])
    ,dhex(dout[55:48]),dhex(dout[63:56]),dhex(dout[71:64]),dhex(dout[79:72])
};
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        fractional <= 0;
        baudrate <= 100;
        reg0 <= 0; reg1 <= 0; reg2 <= 0; reg3 <= 0;
        reg4 <= 0; reg5 <= 0; reg6 <= 0; reg7 <= 0;
    end else begin
        if (wr_baudrate)  baudrate <= {dhex(dout[23:16]),dhex(dout[31:24]),dhex(dout[39:32]),dhex(dout[47:40])};
        if (wr_fractional)  fractional <= {dhex(dout[31:24]),dhex(dout[23:16])};
        if (wr_reg) begin
            if (dout[15:8] == let0) reg0 <= fvalue;
            if (dout[15:8] == let1) reg1 <= fvalue;
            if (dout[15:8] == let2) reg2 <= fvalue;
            if (dout[15:8] == let3) reg3 <= fvalue;
            if (dout[15:8] == let4) reg4 <= fvalue;
            if (dout[15:8] == let5) reg5 <= fvalue;
            if (dout[15:8] == let6) reg6 <= fvalue;
            if (dout[15:8] == let7) reg7 <= fvalue;
        end
        if (vldout) begin
            if (dst == 0) reg0 <= result;
            if (dst == 1) reg1 <= result;
            if (dst == 2) reg2 <= result;
            if (dst == 3) reg3 <= result;
            if (dst == 4) reg4 <= result;
            if (dst == 5) reg5 <= result;
            if (dst == 6) reg6 <= result;
            if (dst == 7) reg7 <= result;
        end
    end
end


wire [7:0] AA = dout[15:8];
wire [7:0] BB = dout[23:16];
wire [7:0] CC = dout[31:24];


wire [3:0] oper = (!work) ? 0 : 
    ((AA == letA)&&(BB==letD)&&(CC==letD)) ?  1 :
    ((AA == letS)&&(BB==letU)&&(CC==letB)) ?  2 :
    ((AA == letM)&&(BB==letU)&&(CC==letL)) ?  3 :
    ((AA == letF)&&(BB==letA)&&(CC==letB)) ?  4 :
    ((AA == letM)&&(BB==letA)&&(CC==letX)) ?  5 :
    ((AA == letM)&&(BB==letI)&&(CC==letN)) ?  6 :
    ((AA == letN)&&(BB==letE)&&(CC==letG)) ?  7 :
    ((AA == letD)&&(BB==letI)&&(CC==letV)) ?  8 :
    ((AA == letS)&&(BB==letQ)&&(CC==letR)) ?  9 :
    ((AA == letS)&&(BB==letI)&&(CC==letN)) ?  10 :
    ((AA == letC)&&(BB==letO)&&(CC==letS)) ?  11 :
    0;


wire [7:0] sel0 = dout[39:32];
wire [7:0] sel1 = dout[47:40];
wire [7:0] dst_wire = dout[51:48];
always @(posedge clk) if (work) dst <= dst_wire;
wire [31:0] src0 = 
    (sel0 == let0) ? reg0 :
    (sel0 == let1) ? reg1 :
    (sel0 == let2) ? reg2 :
    (sel0 == let3) ? reg3 :
    (sel0 == let4) ? reg4 :
    (sel0 == let5) ? reg5 :
    (sel0 == let6) ? reg6 :
    (sel0 == let7) ? reg7 :
    0 ;
wire [31:0] src1 = 
    (sel1 == let0) ? reg0 :
    (sel1 == let1) ? reg1 :
    (sel1 == let2) ? reg2 :
    (sel1 == let3) ? reg3 :
    (sel1 == let4) ? reg4 :
    (sel1 == let5) ? reg5 :
    (sel1 == let6) ? reg6 :
    (sel1 == let7) ? reg7 :
    0 ;



float_unit float_unit (.clk(clk),.rst_n(rst_n)
    ,.vldin(work),.oper(oper),.src0(src0),.src1(src1)
    ,.vldout(vldout),.result(result)
);

wire [8*8-1:0]  resultout = {24'b0,result[7:0],result[15:8],result[23:16],result[31:24],letR};

wire [15:0] txfrees;
wire txtaken;
wire [31:0] selected_reg = 
    (dout[15:8] == let0) ? reg0 :
    (dout[15:8] == let1) ? reg1 :
    (dout[15:8] == let2) ? reg2 :
    (dout[15:8] == let3) ? reg3 :
    (dout[15:8] == let4) ? reg4 :
    (dout[15:8] == let5) ? reg5 :
    (dout[15:8] == let6) ? reg6 :
    (dout[15:8] == let7) ? reg7 :
    0 ;

wire [63:0] selected_hex = {
     hexf(selected_reg[3:0])
    ,hexf(selected_reg[7:4])
    ,hexf(selected_reg[11:8])
    ,hexf(selected_reg[15:12])
    ,hexf(selected_reg[19:16])
    ,hexf(selected_reg[23:20])
    ,hexf(selected_reg[27:24])
    ,hexf(selected_reg[31:28])
};


wire [3:0] txwrites = rd_reg ? 9 : 0;
multififo_w10_r1 #(.WIDTH(8),.DEPTH(32)) txfifo (.clk(clk),.rst_n(rst_n),.softreset(softreset)
    ,.writes(txwrites),.din({8'b0,letCR,selected_hex})
    ,.reads(write_tx),.dout(txdata)
    ,.count(txcount)
    ,.frees(txfrees)
    ,.taken(txtaken)
);

function [7:0] hexf(input [3:0] inx );
begin
    if (inx<10) hexf = 8'h30+inx;
    else hexf = 8'h61 + inx - 10;
end
endfunction
function [3:0] dhex(input [7:0] inx);
begin
    if ((inx>=letA)&&(inx<=letF))
        dhex = 10+inx-letA;
    else if ((inx>=let0)&&(inx<=let9))
        dhex = inx-let0;
end
endfunction
endmodule

