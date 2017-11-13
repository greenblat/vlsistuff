


module fir (input clk
    ,input [15:0] din
    ,output reg [15:0] dout

);



reg [15:0] dlys [0:8];
reg [15:0] coefs [0:8];
initial begin
    coefs[0] = 2000;
    coefs[1] = 1000;
    coefs[2] = 1500;
    coefs[3] = 6000;
    coefs[4] = 9000;
    coefs[5] = 4000;
    coefs[6] = 2000;
    coefs[7] = 1000;
    coefs[8] = 0100;
end



always @(posedge clk) begin
    dlys[0] <= din;
    for (II=1;I<9;II=II+1) begin  
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
wire [35:0] denom = coeffs[0] + coeffs[1] + coeffs[2] + coeffs[3] + coeffs[4] + coeffs[5] + coeffs[6] + coeffs[7] + coeffs[8] ;

wire [35:0] result = nomin/denom;

always @(posedge clk)
    dout <= denom[15:0];
end 



endmodule

