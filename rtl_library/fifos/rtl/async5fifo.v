module async5fifo #(parameter WID=32)(
     input rst_n
    ,input wclk
    ,input writex
    ,output wfull
    ,input [WID-1:0] wdata

    ,input rclk
    ,output [WID-1:0] rdata
    ,output rempty
    ,input  readx
);

wire panic_overflow = wfull && writex;
wire panic_underflow = rempty && readx;
level_sync sync1 (.clk(rclk),.rst_n(rst_n),.din(1'b1),.dout(rst_nr));
level_sync  sync0 (.clk(wclk),.rst_n(rst_n),.din(1'b1),.dout(rst_nw));

wire [WID-1:0] rdata0;
wire wfull0,rempty0;
wire [WID-1:0] rdata1;
wire wfull1,rempty1;
wire [WID-1:0] rdata2;
wire wfull2,rempty2;
wire [WID-1:0] rdata3;
wire wfull3,rempty3;
wire [WID-1:0] rdata4;
wire wfull4,rempty4;


reg [2:0] wptr;
always @(posedge wclk or negedge rst_nw) begin
    if (!rst_nw) begin
        wptr<=0;
    end else if (writex && !wfull) begin
        wptr<= (wptr==4) ? 0 : (wptr+1);
    end
end

assign wfull = 0
    ||((wptr==0)&&wfull0)
    ||((wptr==1)&&wfull1)
    ||((wptr==2)&&wfull2)
    ||((wptr==3)&&wfull3)
    ||((wptr==4)&&wfull4)
;
wire writex0 = writex && (wptr==0)&&!wfull0;
wire writex1 = writex && (wptr==1)&&!wfull1;
wire writex2 = writex && (wptr==2)&&!wfull2;
wire writex3 = writex && (wptr==3)&&!wfull3;
wire writex4 = writex && (wptr==4)&&!wfull4;

reg [2:0] rptr;
always @(posedge rclk or negedge rst_nr) begin
    if (!rst_nr) begin
        rptr<=0;
    end else if (readx && !rempty) begin
        rptr<= (rptr==4) ? 0  : (rptr+1);
    end
end

assign rdata = 
    (rptr==0) ? rdata0 :
    (rptr==1) ? rdata1 :
    (rptr==2) ? rdata2 :
    (rptr==3) ? rdata3 :
    (rptr==4) ? rdata4 :
    0;

assign rempty = 
    (rptr==0) ? rempty0 :
    (rptr==1) ? rempty1 :
    (rptr==2) ? rempty2 :
    (rptr==3) ? rempty3 :
    (rptr==4) ? rempty4 :
    0;

wire readx0 = readx && (rptr==0);
wire readx1 = readx && (rptr==1);
wire readx2 = readx && (rptr==2);
wire readx3 = readx && (rptr==3);
wire readx4 = readx && (rptr==4);


async_stage #(WID) stage0 (
     .rclk(rclk) ,.rst_nr(rst_nr),.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata0) ,.readx(readx0) ,.rempty(rempty0)
    ,.wdata(wdata) ,.wfull(wfull0) ,.writex(writex0)
);
async_stage #(WID) stage1 (
     .rclk(rclk) ,.rst_nr(rst_nr),.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata1) ,.readx(readx1) ,.rempty(rempty1)
    ,.wdata(wdata) ,.wfull(wfull1) ,.writex(writex1)
);
async_stage #(WID) stage2 (
     .rclk(rclk) ,.rst_nr(rst_nr),.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata2) ,.readx(readx2) ,.rempty(rempty2)
    ,.wdata(wdata) ,.wfull(wfull2) ,.writex(writex2)
);
async_stage #(WID) stage3 (
     .rclk(rclk) ,.rst_nr(rst_nr),.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata3) ,.readx(readx3) ,.rempty(rempty3)
    ,.wdata(wdata) ,.wfull(wfull3) ,.writex(writex3)
);
async_stage #(WID) stage4 (
     .rclk(rclk) ,.rst_nr(rst_nr),.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata4) ,.readx(readx4) ,.rempty(rempty4)
    ,.wdata(wdata) ,.wfull(wfull4) ,.writex(writex4)
);
wire [63:0]  sign_version = 64'h0003418714240424 ;
endmodule


