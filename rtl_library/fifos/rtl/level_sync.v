
module level_sync (input clk, input rst_n, input din, output dout);

reg [1:0] sr;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        sr <= 0;
    end else begin
        sr <= {sr[0],din};
    end
end

assign dout = sr[1];

endmodule

