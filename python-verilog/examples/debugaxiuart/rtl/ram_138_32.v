
module ram_138_32 (input clk,input cen,input wen
   ,input      [137:0] din
   ,output     [137:0] dout
   ,input     [4:0] addr
);
reg [137:0] mem [0:31];
reg [137:0] tmp;

wire addr_ok = ((^addr)!==1'bx);

wire inps_ok = (^{cen,wen}!==1'bx)&&addr_ok;
assign #1 dout = tmp;
always @(posedge clk) if (inps_ok && ~cen && ~wen) begin
    mem[addr]<=din;
end
always @(posedge clk) begin
    if (inps_ok && ~cen && wen) tmp <= mem[addr];
    else tmp <= 138'bx;
end
endmodule
