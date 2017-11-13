


module fir (input clk
    ,input [15:0] din
    ,output reg [15:0] dout

);



reg [15:0] dlys [0:8];
reg [15:0] coeffs [0:8];
initial begin
    coeffs[0] = 1000;
    coeffs[1] = 3000;
    coeffs[2] = 1500;
    coeffs[3] = 13000;
    coeffs[4] = 20000;
    coeffs[5] = 13000;
    coeffs[6] = 1500;
    coeffs[7] = 3000;
    coeffs[8] = 1000;
end


integer II;
always @(posedge clk) begin
    dlys[0] <= din;
    for (II=1;II<9;II=II+1) begin  
        dlys[II] <= dlys[II-1];
    end
end

wire [35:0] nomin = 
      coeffs[0]*dlys[0]
    + coeffs[1]*dlys[1]
    + coeffs[2]*dlys[2]
    + coeffs[3]*dlys[3]
    + coeffs[4]*dlys[4]
    + coeffs[5]*dlys[5]
    + coeffs[6]*dlys[6]
    + coeffs[7]*dlys[7]
    + coeffs[8]*dlys[8]
    ;

reg [5:0] bug; initial bug=0;

wire [35:0] denom = coeffs[0] + coeffs[1] + coeffs[2] + coeffs[3] + coeffs[4] + coeffs[5] + coeffs[6] + coeffs[7] + coeffs[8] ;

wire [35:0] result = bug + nomin/denom;

always @(posedge clk) dout <= result[15:0];



endmodule

