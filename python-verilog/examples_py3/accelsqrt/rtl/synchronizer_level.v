module synchronizer_level ( input clk, input din, input rst_n,output dout);
reg [2:0] sreg;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        sreg <= 0;
    end else begin
        sreg <= {sreg[1:0],din};
    end
end
assign dout = sreg[2];
endmodule
