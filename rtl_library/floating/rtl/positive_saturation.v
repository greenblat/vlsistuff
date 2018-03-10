module positive_saturation #(parameter WID=16) (input [31:0] inx, input[WID-1:0] maxval,output [WID-1:0] outx);
assign outx = inx[31] ? 0 : (inx>maxval) ? maxval : inx; 
endmodule
