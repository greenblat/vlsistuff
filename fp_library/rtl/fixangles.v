module fixangles(input [4:0] step,output reg [31:0] angle);
always @(step) begin
    case (step)
         0 : angle = 32'h00c90fda;
         1 : angle = 32'h0076b19c;
         2 : angle = 32'h003eb6eb;
         3 : angle = 32'h001fd5ba;
         4 : angle = 32'h000ffaad;
         5 : angle = 32'h0007ff55;
         6 : angle = 32'h0003ffea;
         7 : angle = 32'h0001fffd;
         8 : angle = 32'h0000ffff;
         9 : angle = 32'h00007fff;
        10 : angle = 32'h00003fff;
        11 : angle = 32'h00001fff;
        12 : angle = 32'h00000fff;
        13 : angle = 32'h000007ff;
        14 : angle = 32'h000003ff;
        15 : angle = 32'h000001ff;
        16 : angle = 32'h000000ff;
        17 : angle = 32'h0000007f;
        18 : angle = 32'h0000003f;
        19 : angle = 32'h0000001f;
        20 : angle = 32'h0000000f;
        21 : angle = 32'h00000007;
        22 : angle = 32'h00000003;
        23 : angle = 32'h00000001;
        default: angle = 0;
    endcase
end
endmodule
