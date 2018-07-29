
module example0 (
    input clk, input rst_n
    ,input [7:0] inx
    ,output reg [7:0] outx
);

wire [7:0] mid0 = inx + 1;
wire [7:0] mid1 = inx - outx;

wire [15:0] ram [0:100];

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        outx <= 0;
    end else begin
        outx <= ~inx;
    end
end

son0 i_son0 (.clk(clk),.res(res0));
son1 i_son1 (.clk(clk),.res(res1));
son2 i_son2 (.clk(clk),.res(res2));
son3 i_son3 (.clk(clk),.res(res3));


endmodule

