module syncramfifo #(parameter WID=32, parameter DEPTH=1024, parameter WCOUNT=$clog2(DEPTH)) (
     input clk,input rst_n,input softreset
    ,input [15:0] capacity
    ,input validin, input [WID-1:0] datain, output full
    ,input readout, output [WID-1:0] dataout, output empty
    ,output [15:0] count
    ,output wen
    ,output cen
    ,output [WCOUNT-1:0] addr
    ,output [(2*WID)-1:0] wdata
    ,input  [(2*WID)-1:0] rdata
    ,output panic
);
wire write_from_fifoin,write_to_ram,read_from_ram;
reg write_from_ram; 
wire [15:0] ram_count;
reg [WID-1:0] fifoin [0:7];
reg [3:0] wptrin,rptrin;
wire [3:0] countin = (wptrin >= rptrin) ? (wptrin - rptrin) :  ((16-rptrin) + wptrin);
wire   emptyin = (countin == 0);
wire   fullin = (countin == 8);
wire  [2:0] rptrin1 =  (rptrin==7) ? 3'd0 : (rptrin+1'b1);
wire [WID-1:0]  first = fifoin[rptrin[2:0]];
wire [WID-1:0]  second = fifoin[rptrin1[2:0]];
always @(posedge clk) begin
    if(validin && !full) begin
        fifoin[wptrin[2:0]] <= datain;
    end 
end
always @(posedge clk or negedge rst_n) begin
    if(!rst_n) begin
        wptrin <= 0; rptrin <= 0;
    end else if(softreset) begin
        wptrin <= 0; rptrin <= 0;
    end else begin
        if(validin && !full) begin
            wptrin <= (wptrin==15) ? 0 : (wptrin + 1);
        end 
        if(write_from_fifoin) begin
            rptrin <= (rptrin==15) ? 0 : (rptrin + 1);
        end else if(write_to_ram) begin
            rptrin <= (rptrin==14) ? 0 : (rptrin==15) ? 1 : (rptrin + 2);
        end
    end 
end
reg [WID-1:0] fifoout [0:3];
reg [2:0] wptrout,rptrout;
wire [2:0] countout = (wptrout >= rptrout) ? (wptrout - rptrout) :  ((8-rptrout) + wptrout);
assign   empty = countout == 0;
wire   fullout = countout == 4;
assign dataout = empty ? 0 : fifoout[rptrout[1:0]];
wire [1:0] wptrout1 = (wptrout[1:0]==3) ? 0 : (wptrout[1:0]+1);
wire [1:0] wptrout0 = wptrout[1:0];
always @(posedge clk) begin
    if(write_from_fifoin) begin
        fifoout[wptrout[1:0]] <= first;
    end 
    if(write_from_ram) begin
        fifoout[wptrout1] <= rdata[(2*WID)-1:WID];
        fifoout[wptrout0] <= rdata[WID-1:0];
    end 
end
always @(posedge clk or negedge rst_n) begin
    if(!rst_n) begin
        wptrout <= 0; rptrout <= 0;
    end else if(softreset) begin
        wptrout <= 0; rptrout <= 0;
    end else begin
        if(write_from_ram) begin
            wptrout <= (wptrout==6) ? 0 :(wptrout==7) ? 1 : (wptrout + 2);
        end 
        if(write_from_fifoin) begin
            wptrout <= (wptrout==7) ? 0 : (wptrout + 1);
        end 
        if(readout && !empty) begin
            rptrout <= (rptrout==7) ? 0 : (rptrout + 1);
        end 
    end 
end
wire [WCOUNT:0] wcapacity = (capacity>>1)+capacity[0];
wire   ram_empty = ram_count == 0;
wire   ram_full = ram_count >= wcapacity;
assign write_from_fifoin = (ram_count==0) && (countin>0) && (!fullout) && !write_from_ram;
assign write_to_ram = !ram_full && (countin>=2) && (fullout||(ram_count>0)) && !read_from_ram;
assign read_from_ram = (ram_count!=0) && (countout<3) && !write_from_ram;
always @(posedge clk or negedge rst_n) begin
    if(!rst_n) begin
        write_from_ram <=0;
    end else begin
        write_from_ram <=read_from_ram;
    end
end
wire panic0 = validin && fullin && !full;
wire panic1 = (countout>2) && write_from_ram;
wire panic2 = write_from_ram && write_from_fifoin;
wire panic3 = (ram_count>=wcapacity) && write_to_ram;
wire panic4;
wire panic5 = write_from_fifoin && write_to_ram;
assign panic = panic0 || panic1 || panic2 || panic3 || panic4 || panic5;
reg [WCOUNT:0] wptr,rptr;
reg whalf,rhalf;
assign ram_count = 
    (whalf==rhalf) ? (wptr - rptr) :
    (whalf && !rhalf) ? (wcapacity - rptr + wptr) :
    (wcapacity-rptr+wptr);
assign count = ram_count*2 + countin + countout;
always @(posedge clk or negedge rst_n) begin
    if(!rst_n) begin
        wptr <= 0; rptr <= 0;
        rhalf<=0; whalf<=0;
    end else if(softreset) begin
        wptr <= 0; rptr <= 0;
        rhalf<=0; whalf<=0;
    end else begin
        if(write_to_ram) begin
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
assign wdata =  {second,first};
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
