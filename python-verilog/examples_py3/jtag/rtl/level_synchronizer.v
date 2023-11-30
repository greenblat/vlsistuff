


module level_synchronizer #(parameter WID=1) (
    input clk, input [WID-1:0] din, input rst_n,output [WID-1:0] dout
);

reg [WID-1:0] sreg0,sreg1;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        sreg0 <= 0;
        sreg1 <= 0;
    end else begin
        sreg0 <= din;
        sreg1 <= sreg0;
    end
end
assign dout = sreg1;


endmodule

