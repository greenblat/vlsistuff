


module delay_reg(
    input clk,input rst_n,input en
    ,input src0,output out
    ,input [2:0] tap
);
reg [7:0] shifter;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        shifter <=0;
    end else if (en) begin
        shifter <= {shifter[6:0],src0};
    end
end

assign out = shifter[tap];

endmodule

