
module ram_16_512 (input clk,input cen,input wen
   ,input      [15:0] din
   ,output     [15:0] dout
   ,input     [8:0] addr
);
reg [15:0] mem [0:511];
reg [15:0] tmp;

wire addr_ok = ((^addr)!==1'bx);

wire inps_ok = (^{cen,wen}!==1'bx)&&addr_ok;
assign #1 dout = tmp;
always @(posedge clk) if (inps_ok && ~cen && ~wen) begin
    mem[addr]<=din;
end
always @(posedge clk) begin
    if (inps_ok && ~cen && wen) tmp <= mem[addr];
    else tmp <= 16'bx;
end
endmodule
