module flow_image_float (
    input [31:0] ain
    ,input [31:0] bin
    ,input sel
    ,output [31:0] out
);
assign out = sel ? ain : bin ;
endmodule
