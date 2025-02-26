
module mul16x16 ( input clk, input rst_n, input [15:0] ain, input [15:0] bin, input vldin, output vldout, output reg [31:0] dout);


reg [15:0] aar,bbr;
reg [2:0] vlsr;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        vlsr <= 0;
        aar <= 0;
        bbr <= 0;
        dout <= 0;
    end else begin
        vlsr <= {vlsr[1:0],vldin};
        if (vldin) begin
            aar <= ain;
            bbr <= bin;
         end 
        if (vlsr[0]) begin
            dout <= aar*bbr;
        end 
    end
end
assign vldout = vlsr[1];

endmodule


