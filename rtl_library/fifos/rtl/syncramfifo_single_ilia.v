
// this ram based fifo cannot continuously support concurrent reads and writes.
// because the width of the ram is single (==WID).

module syncramfifo_single_ilia #(parameter WID=32, parameter DEPTH=1024, parameter WCOUNT=$clog2(DEPTH)) (
     input clk,input rst_n,input softreset
    ,input [15:0] capacity
    ,input validin, input [WID-1:0] datain, output full
    ,input readout, output [WID-1:0] dataout, output empty
    ,output [15:0] count

    ,output wen
    ,output cen
    ,output [WCOUNT-1:0] addr
    ,output [WID-1:0] wdata
    ,input  [WID-1:0] rdata

    ,output panic
);

wire write_from_fifoin,write_to_ram,read_from_ram;
reg write_from_ram; 

reg [WID-1:0] fifoin [0:7];
reg [3:0] wptrin,rptrin;
wire [3:0] countin = (wptrin >= rptrin) ? (wptrin - rptrin) :  ((16-rptrin) + wptrin);
wire   emptyin = (countin == 0);
wire   fullin = (countin == 8);
wire [WID-1:0]  first = fifoin[rptrin[2:0]];

always @(posedge clk) begin
    if(validin && !fullin) begin
        fifoin[wptrin[2:0]] <= datain;
    end 
end

always @(posedge clk or negedge rst_n) begin
    if(!rst_n) begin
        wptrin <= 0; rptrin <= 0;
    end else if(softreset) begin
        wptrin <= 0; rptrin <= 0;
    end else begin
        if(validin && !fullin) begin
            wptrin <= (wptrin==15) ? 0 : (wptrin + 1);
        end 
        if(write_from_fifoin) begin
            rptrin <= (rptrin==15) ? 0 : (rptrin + 1);
        end else if(write_to_ram && !ram_full) begin
            rptrin <= (rptrin==15) ? 0 : (rptrin + 1);
        end
    end 
end


reg [WID-1:0] fifoout [0:3];
reg [2:0] wptrout,rptrout;
wire [2:0] countout = (wptrout >= rptrout) ? (wptrout - rptrout) :  ((8-rptrout) + wptrout);
assign   empty = countout == 0;
wire   fullout = countout == 4;
assign dataout = empty ? 0 : fifoout[rptrout[1:0]];

always @(posedge clk) begin
    if(write_from_fifoin) begin
        fifoout[wptrout[1:0]] <= first;
    end 
    if(write_from_ram) begin
        fifoout[wptrout[1:0]] <= rdata;
    end 
end
always @(posedge clk or negedge rst_n) begin
    if(!rst_n) begin
        wptrout <= 0; rptrout <= 0;
    end else if(softreset) begin
        wptrout <= 0; rptrout <= 0;
    end else begin
        if(write_from_ram) begin
            wptrout <= (wptrout==7) ? 0 : (wptrout + 1);
        end 
        if(write_from_fifoin) begin
            wptrout <= (wptrout==7) ? 0 : (wptrout + 1);
        end 
        if(readout && !empty) begin
            rptrout <= (rptrout==7) ? 0 : (rptrout + 1);
        end 
    end 
end


assign write_from_fifoin = (count==0) && (countin>0) && (!fullout) && !write_from_ram;
assign write_to_ram = (countin>=2) && (fullout||(count>0)) && !read_from_ram;
assign read_from_ram = (count!=0) && (countout<4) && !write_from_ram;

always @(posedge clk or negedge rst_n) begin
    if(!rst_n) begin
        write_from_ram <=0;
    end else begin
        write_from_ram <=read_from_ram;
    end
end

wire [WCOUNT:0] wcapacity = capacity;
wire panic0 = validin && fullin;
wire panic1 = (countout>2) && write_from_ram;
wire panic2 = write_from_ram && write_from_fifoin;
wire panic3 = count>=wcapacity;
wire panic4;
wire panic5 = write_from_fifoin && write_to_ram;
assign panic = panic0 || panic1 || panic2 || panic3 || panic4 || panic5;


reg [WCOUNT:0] wptr,rptr;
reg whalf,rhalf;
assign   count = 
    (whalf==rhalf) ? (wptr - rptr) :
    (whalf && !rhalf) ? (wcapacity - rptr + wptr) :
    (wcapacity-rptr+wptr);
wire   ram_empty = count == 0;
wire   ram_full = count >= (wcapacity-5);


always @(posedge clk or negedge rst_n) begin
    if(!rst_n) begin
        wptr <= 0; rptr <= 0;
        rhalf<=0; whalf<=0;
    end else if(softreset) begin
        wptr <= 0; rptr <= 0;
        rhalf<=0; whalf<=0;
    end else begin
        if(write_to_ram && !ram_full) begin
            wptr <= (wptr==(wcapacity-1)) ? 0 : (wptr + 1);
            whalf <= whalf ^ (wptr==(wcapacity-1));
        end 
        if(read_from_ram && !ram_empty) begin
            rptr <= (rptr==(wcapacity-1)) ? 0 : (rptr + 1);
            rhalf <= rhalf ^ (rptr==(wcapacity-1));
        end 
    end 
end

assign wen = !write_to_ram;
assign cen = !(read_from_ram || write_to_ram);
assign wdata =  first;
assign full = ram_full || fullin;
assign addr = write_to_ram ? wptr : rptr;


// debug
reg [19:0] dbgwr,dbgrd;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        dbgwr<=0; dbgrd<=0;
    end else if (softreset) begin
        dbgwr<=0; dbgrd<=0;
    end else begin
        if (validin && !full) dbgwr <= dbgwr+1;
        if (readout && !empty) dbgrd <= dbgrd+1;
    end
end
assign panic4 = dbgrd>dbgwr;


endmodule


//  syncramfifo_single #(32,1024)   fifo (
//      .clk(clk),.rst_n(rst_n),.capacity(capacity[15:0))
//      ,.validin(validin),.datain(datain[WID-1:0],.full(full)
//      ,.readout(readout),.dataout(dataout[WID-1:0]),.empty(empty)
//      ,.count(count[15:0])
//      ,.softreset(softreset)
//  
//      ,.wen(ram_wen)
//      ,.cen(ram_cen)
//      ,.addr(ram_addr[8:0])
//      ,.wdata(ram_wdata[WID-1:0])
//      ,.rdata(ram_rdata[WID-1:0])
//  
//  );


