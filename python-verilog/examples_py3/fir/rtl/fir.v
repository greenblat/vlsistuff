


module fir (input clk, input [7:0][7:0] coeffs,input [7:0] sample,input vldin
    ,input [3:0] scalefactor
    ,output reg vldout
    ,output reg [7:0] result
    ,output saturation
);

reg [7:0] [7:0] samples;
reg vld0,vld1,vld2,vld3;
integer ii;
always @(posedge clk) begin
    if (vldin) begin
        for (ii=7;ii>0;ii = ii-1) begin
            samples[ii] <= samples[ii-1];
        end
        samples[0] <= sample;
    end
    vld0 <= vldin;
end
integer jj;
reg [7:0] [23:0] mid1;
always @(posedge clk) begin
    if (vld0) begin
        for (jj=0;jj<8;jj=jj+1) begin
            mid1[jj] <= 1 * samples[jj] * coeffs[jj];
//            $display("MUL jj=%d sample=%x coff=%x exp=%x ",jj,samples[jj],coeffs[jj],samples[jj] * coeffs[jj]);
        end
    end
    vld1 <= vld0;
end

reg [3:0] [23:0] mid2;
always @(posedge clk) begin
    if (vld1) begin
        mid2[0] <= mid1[0] + mid1[1];
        mid2[1] <= mid1[2] + mid1[3];
        mid2[2] <= mid1[4] + mid1[5];
        mid2[3] <= mid1[6] + mid1[7];
    end
    vld2 <= vld1;
end

reg [23:0] midresult;
always @(posedge clk) begin
    if (vld2) begin
       midresult <= mid2[0]+mid2[1]+mid2[2]+mid2[3]; 
    end
    vld3 <= vld2;
end

wire [23:0] tmp = midresult>>scalefactor;
assign saturation = tmp[23:8]!=0;
always @(posedge clk) begin
    if (vld3) begin
       result <= saturation ? 255 : tmp[7:0]; 
    end
    vldout <= vld3;
end

endmodule

