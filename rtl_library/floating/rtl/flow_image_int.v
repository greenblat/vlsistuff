module flow_image_int #(parameter WID=32) (
    input [WID-1:0] ain
    ,input [WID-1:0] bin
    ,input sel
    ,input [5:0] shift
    ,output [31:0] out
    ,input is_signed
);
wire [WID-1:0] selected = sel ? ain : bin; 
wire [5:0] nshift = -shift;
fp_int2float #(WID)  int2float3 (.ain(selected), .bin(nshift), .out(out),.is_signed(is_signed));
endmodule
