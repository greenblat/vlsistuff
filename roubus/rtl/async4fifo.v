module async4fifo #(parameter WID=32)(
     input wclk
    ,input rst_n
    ,input rclk
    ,input writex
    ,output wfull
    ,input [WID-1:0] wdata
    ,output [WID-1:0] rdata
    ,output rempty
    ,input  readx
);



wire [WID-1:0] rdata0,rdata1,rdata2,rdata3;
wire wfull0,wfull1,wfull2,wfull3;
wire rempty0,rempty1,rempty2,rempty3;

reg [1:0] wptr;
always @(posedge wclk or negedge rst_n) begin
    if (!rst_n) begin
        wptr<=0;
    end else if (writex && !wfull) begin
        wptr<=wptr+1;
    end
end

assign wfull = 
    ((wptr==0)&&wfull0)||
    ((wptr==1)&&wfull1)||
    ((wptr==2)&&wfull2)||
    ((wptr==3)&&wfull3);

wire writex0 = writex && (wptr==0)&&!wfull0;
wire writex1 = writex && (wptr==1)&&!wfull1;
wire writex2 = writex && (wptr==2)&&!wfull2;
wire writex3 = writex && (wptr==3)&&!wfull3;

reg [1:0] rptr;
always @(posedge rclk or negedge rst_n) begin
    if (!rst_n) begin
        rptr<=0;
    end else if (readx && !rempty) begin
        rptr<=rptr+1;
    end
end

assign rdata = 
    (rptr==0) ? rdata0 :
    (rptr==1) ? rdata1 :
    (rptr==2) ? rdata2 :
    (rptr==3) ? rdata3 :
    0;

assign rempty = 
    (rptr==0) ? rempty0 :
    (rptr==1) ? rempty1 :
    (rptr==2) ? rempty2 :
    (rptr==3) ? rempty3 :
    0;

assign readx0 = readx && (rptr==0);
assign readx1 = readx && (rptr==1);
assign readx2 = readx && (rptr==2);
assign readx3 = readx && (rptr==3);


async_stage #(WID) stage0 (
     .rclk(rclk) ,.rst_n(rst_n) ,.wclk(wclk)
    ,.rdata(rdata0) ,.readx(readx0) ,.rempty(rempty0)
    ,.wdata(wdata) ,.wfull(wfull0) ,.writex(writex0)
);
async_stage #(WID) stage1 (
     .rclk(rclk) ,.rst_n(rst_n) ,.wclk(wclk)
    ,.rdata(rdata1) ,.readx(readx1) ,.rempty(rempty1)
    ,.wdata(wdata) ,.wfull(wfull1) ,.writex(writex1)
);
async_stage #(WID) stage2 (
     .rclk(rclk) ,.rst_n(rst_n) ,.wclk(wclk)
    ,.rdata(rdata2) ,.readx(readx2) ,.rempty(rempty2)
    ,.wdata(wdata) ,.wfull(wfull2) ,.writex(writex2)
);
async_stage #(WID) stage3 (
     .rclk(rclk) ,.rst_n(rst_n) ,.wclk(wclk)
    ,.rdata(rdata3) ,.readx(readx3) ,.rempty(rempty3)
    ,.wdata(wdata) ,.wfull(wfull3) ,.writex(writex3)
);
endmodule


