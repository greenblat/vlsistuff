
module cntrl (input rst_n, input clk, output a0, output a1, output a2, output a3);



reg [3:0] aa;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) aa<= 0;
    else aa <= aa+1;
end

assign {a3,a2,a1,a0} = aa;

endmodule




