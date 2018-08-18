

module async_stage #(parameter WID=32)(
     input wclk
    ,input rst_n
    ,input rclk
    ,input writex
    ,output wfull
    ,input [WID-1:0] wdata
    ,output reg  [WID-1:0] rdata
    ,output rempty
    ,input  readx
);

reg wtoken,rtoken;
reg wtoken_mid,wtoken_sync;
reg rtoken_mid,rtoken_sync;

always @(posedge rclk) wtoken_mid <= wtoken;
always @(posedge rclk) wtoken_sync <= wtoken_mid;
always @(posedge wclk) rtoken_mid <= rtoken;
always @(posedge wclk) rtoken_sync <= rtoken_mid;

assign wfull  =  wtoken!=rtoken_sync;
assign rempty  =  wtoken_sync==rtoken;



always @(posedge wclk or rst_n) begin
    if (!rst_n) begin
        wtoken<=0;
        rdata <= 0;
    end else begin
        if (!wfull && writex) begin
            rdata <= wdata;
            wtoken <= !wtoken;
        end
    end
end

always @(posedge rclk or rst_n) begin
    if (!rst_n) begin
        rtoken<=0;
    end else begin
        if (!rempty && readx) begin
            rtoken<=~rtoken;
        end
    end
end

endmodule

