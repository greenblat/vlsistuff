module fp_maxmin (input max_cmd, input [31:0] ain,input [31:0] bin, output [31:0] out);
wire isgt;
fp_gt gt (.ain(ain),.bin(bin),.out(isgt));
assign out = (isgt ^ max_cmd) ? bin : ain; 
endmodule
