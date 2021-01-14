module async16fifo #(parameter WID=32)(
     input wclk
    ,input rst_n
    ,input rclk
    ,input writex
    ,output wfull
    ,input [WID-1:0] wdata
    ,output [WID-1:0] rdata
    ,output rempty
    ,input  readx
    ,output rst_nr
    ,output rst_nw
);
synchronizer_level syncrstr (.clk(rclk),.rst_n(rst_n),.din(1'b1),.dout(rst_nr));
synchronizer_level syncrstw (.clk(wclk),.rst_n(rst_n),.din(1'b1),.dout(rst_nw));
wire [16-1:0]  wfulls,remptys;
wire [WID-1:0] rdata0;
wire [WID-1:0] rdata1;
wire [WID-1:0] rdata2;
wire [WID-1:0] rdata3;
wire [WID-1:0] rdata4;
wire [WID-1:0] rdata5;
wire [WID-1:0] rdata6;
wire [WID-1:0] rdata7;
wire [WID-1:0] rdata8;
wire [WID-1:0] rdata9;
wire [WID-1:0] rdata10;
wire [WID-1:0] rdata11;
wire [WID-1:0] rdata12;
wire [WID-1:0] rdata13;
wire [WID-1:0] rdata14;
wire [WID-1:0] rdata15;
reg [4:0] wptr;
always @(posedge wclk or negedge rst_n) begin
    if (!rst_n) begin
        wptr<=0;
    end else if (writex && !wfull) begin
        wptr<=(wptr==15) ? 0 : (wptr+1);
    end
end
assign wfull = 0
    ||((wptr==0)&&wfulls[0])
    ||((wptr==1)&&wfulls[1])
    ||((wptr==2)&&wfulls[2])
    ||((wptr==3)&&wfulls[3])
    ||((wptr==4)&&wfulls[4])
    ||((wptr==5)&&wfulls[5])
    ||((wptr==6)&&wfulls[6])
    ||((wptr==7)&&wfulls[7])
    ||((wptr==8)&&wfulls[8])
    ||((wptr==9)&&wfulls[9])
    ||((wptr==10)&&wfulls[10])
    ||((wptr==11)&&wfulls[11])
    ||((wptr==12)&&wfulls[12])
    ||((wptr==13)&&wfulls[13])
    ||((wptr==14)&&wfulls[14])
    ||((wptr==15)&&wfulls[15])
;
wire writex0 = writex && (wptr==0)&&!wfulls[0];
wire writex1 = writex && (wptr==1)&&!wfulls[1];
wire writex2 = writex && (wptr==2)&&!wfulls[2];
wire writex3 = writex && (wptr==3)&&!wfulls[3];
wire writex4 = writex && (wptr==4)&&!wfulls[4];
wire writex5 = writex && (wptr==5)&&!wfulls[5];
wire writex6 = writex && (wptr==6)&&!wfulls[6];
wire writex7 = writex && (wptr==7)&&!wfulls[7];
wire writex8 = writex && (wptr==8)&&!wfulls[8];
wire writex9 = writex && (wptr==9)&&!wfulls[9];
wire writex10 = writex && (wptr==10)&&!wfulls[10];
wire writex11 = writex && (wptr==11)&&!wfulls[11];
wire writex12 = writex && (wptr==12)&&!wfulls[12];
wire writex13 = writex && (wptr==13)&&!wfulls[13];
wire writex14 = writex && (wptr==14)&&!wfulls[14];
wire writex15 = writex && (wptr==15)&&!wfulls[15];
reg [4:0] rptr;
always @(posedge rclk or negedge rst_n) begin
    if (!rst_n) begin
        rptr<=0;
    end else if (readx && !rempty) begin
        rptr<=(rptr==15) ? 0 : (rptr+1);
    end
end
assign rdata = 
    (rptr==0) ? rdata0 :
    (rptr==1) ? rdata1 :
    (rptr==2) ? rdata2 :
    (rptr==3) ? rdata3 :
    (rptr==4) ? rdata4 :
    (rptr==5) ? rdata5 :
    (rptr==6) ? rdata6 :
    (rptr==7) ? rdata7 :
    (rptr==8) ? rdata8 :
    (rptr==9) ? rdata9 :
    (rptr==10) ? rdata10 :
    (rptr==11) ? rdata11 :
    (rptr==12) ? rdata12 :
    (rptr==13) ? rdata13 :
    (rptr==14) ? rdata14 :
    (rptr==15) ? rdata15 :
    0;
assign rempty = 
    (rptr==0) ? remptys[0] :
    (rptr==1) ? remptys[1] :
    (rptr==2) ? remptys[2] :
    (rptr==3) ? remptys[3] :
    (rptr==4) ? remptys[4] :
    (rptr==5) ? remptys[5] :
    (rptr==6) ? remptys[6] :
    (rptr==7) ? remptys[7] :
    (rptr==8) ? remptys[8] :
    (rptr==9) ? remptys[9] :
    (rptr==10) ? remptys[10] :
    (rptr==11) ? remptys[11] :
    (rptr==12) ? remptys[12] :
    (rptr==13) ? remptys[13] :
    (rptr==14) ? remptys[14] :
    (rptr==15) ? remptys[15] :
    0;
wire readx0 = readx && (rptr==0);
wire readx1 = readx && (rptr==1);
wire readx2 = readx && (rptr==2);
wire readx3 = readx && (rptr==3);
wire readx4 = readx && (rptr==4);
wire readx5 = readx && (rptr==5);
wire readx6 = readx && (rptr==6);
wire readx7 = readx && (rptr==7);
wire readx8 = readx && (rptr==8);
wire readx9 = readx && (rptr==9);
wire readx10 = readx && (rptr==10);
wire readx11 = readx && (rptr==11);
wire readx12 = readx && (rptr==12);
wire readx13 = readx && (rptr==13);
wire readx14 = readx && (rptr==14);
wire readx15 = readx && (rptr==15);
async_stage #(WID) stage0 (
     .rclk(rclk) ,.rst_nr(rst_nr) ,.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata0) ,.readx(readx0) ,.rempty(remptys[0])
    ,.wdata(wdata) ,.wfull(wfulls[0]) ,.writex(writex0)
);
async_stage #(WID) stage1 (
     .rclk(rclk) ,.rst_nr(rst_nr) ,.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata1) ,.readx(readx1) ,.rempty(remptys[1])
    ,.wdata(wdata) ,.wfull(wfulls[1]) ,.writex(writex1)
);
async_stage #(WID) stage2 (
     .rclk(rclk) ,.rst_nr(rst_nr) ,.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata2) ,.readx(readx2) ,.rempty(remptys[2])
    ,.wdata(wdata) ,.wfull(wfulls[2]) ,.writex(writex2)
);
async_stage #(WID) stage3 (
     .rclk(rclk) ,.rst_nr(rst_nr) ,.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata3) ,.readx(readx3) ,.rempty(remptys[3])
    ,.wdata(wdata) ,.wfull(wfulls[3]) ,.writex(writex3)
);
async_stage #(WID) stage4 (
     .rclk(rclk) ,.rst_nr(rst_nr) ,.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata4) ,.readx(readx4) ,.rempty(remptys[4])
    ,.wdata(wdata) ,.wfull(wfulls[4]) ,.writex(writex4)
);
async_stage #(WID) stage5 (
     .rclk(rclk) ,.rst_nr(rst_nr) ,.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata5) ,.readx(readx5) ,.rempty(remptys[5])
    ,.wdata(wdata) ,.wfull(wfulls[5]) ,.writex(writex5)
);
async_stage #(WID) stage6 (
     .rclk(rclk) ,.rst_nr(rst_nr) ,.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata6) ,.readx(readx6) ,.rempty(remptys[6])
    ,.wdata(wdata) ,.wfull(wfulls[6]) ,.writex(writex6)
);
async_stage #(WID) stage7 (
     .rclk(rclk) ,.rst_nr(rst_nr) ,.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata7) ,.readx(readx7) ,.rempty(remptys[7])
    ,.wdata(wdata) ,.wfull(wfulls[7]) ,.writex(writex7)
);
async_stage #(WID) stage8 (
     .rclk(rclk) ,.rst_nr(rst_nr) ,.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata8) ,.readx(readx8) ,.rempty(remptys[8])
    ,.wdata(wdata) ,.wfull(wfulls[8]) ,.writex(writex8)
);
async_stage #(WID) stage9 (
     .rclk(rclk) ,.rst_nr(rst_nr) ,.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata9) ,.readx(readx9) ,.rempty(remptys[9])
    ,.wdata(wdata) ,.wfull(wfulls[9]) ,.writex(writex9)
);
async_stage #(WID) stage10 (
     .rclk(rclk) ,.rst_nr(rst_nr) ,.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata10) ,.readx(readx10) ,.rempty(remptys[10])
    ,.wdata(wdata) ,.wfull(wfulls[10]) ,.writex(writex10)
);
async_stage #(WID) stage11 (
     .rclk(rclk) ,.rst_nr(rst_nr) ,.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata11) ,.readx(readx11) ,.rempty(remptys[11])
    ,.wdata(wdata) ,.wfull(wfulls[11]) ,.writex(writex11)
);
async_stage #(WID) stage12 (
     .rclk(rclk) ,.rst_nr(rst_nr) ,.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata12) ,.readx(readx12) ,.rempty(remptys[12])
    ,.wdata(wdata) ,.wfull(wfulls[12]) ,.writex(writex12)
);
async_stage #(WID) stage13 (
     .rclk(rclk) ,.rst_nr(rst_nr) ,.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata13) ,.readx(readx13) ,.rempty(remptys[13])
    ,.wdata(wdata) ,.wfull(wfulls[13]) ,.writex(writex13)
);
async_stage #(WID) stage14 (
     .rclk(rclk) ,.rst_nr(rst_nr) ,.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata14) ,.readx(readx14) ,.rempty(remptys[14])
    ,.wdata(wdata) ,.wfull(wfulls[14]) ,.writex(writex14)
);
async_stage #(WID) stage15 (
     .rclk(rclk) ,.rst_nr(rst_nr) ,.rst_nw(rst_nw) ,.wclk(wclk)
    ,.rdata(rdata15) ,.readx(readx15) ,.rempty(remptys[15])
    ,.wdata(wdata) ,.wfull(wfulls[15]) ,.writex(writex15)
);
endmodule
