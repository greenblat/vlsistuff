module async_stage #(parameter WID=32)(
     input wclk
    ,input rst_nw
    ,input rclk
    ,input rst_nr
    ,input writex
    ,output wfull
    ,input [WID-1:0] wdata
    ,output reg  [WID-1:0] rdata
    ,output rempty
    ,input  readx
);
reg wtoken,rtoken;
level_sync syncr (.clk(rclk),.rst_n(rst_nr),.din(wtoken),.dout(wtoken_sync));
level_sync syncw (.clk(wclk),.rst_n(rst_nw),.din(rtoken),.dout(rtoken_sync));
assign wfull  =  wtoken!=rtoken_sync;
assign rempty  =  wtoken_sync==rtoken;
always @(posedge wclk or negedge rst_nw) begin
    if (!rst_nw) begin
        wtoken<=0;
        rdata <= 0;
    end else begin
        if (!wfull && writex) begin
            rdata <= wdata;
            wtoken <= !wtoken;
        end
    end
end
always @(posedge rclk or negedge rst_nr) begin
    if (!rst_nr) begin
        rtoken<=0;
    end else begin
        if (!rempty && readx) begin
            rtoken<=~rtoken;
        end
    end
end
endmodule


