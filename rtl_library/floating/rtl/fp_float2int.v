module fp_float2int #(parameter WID=32) ( input [31:0] ain ,input [5:0] bin,output [31:0] out);
wire [30:0] ZERO = 31'b0;
wire [31:0] mant = {1'b1,ain[22:0],8'b0};
wire sign        = ain[31];
wire [7:0]  exp0  = ain[30:23];
wire [7:0]  exp  = exp0-7'd127+{bin[5],bin[5],bin};
wire special1 = exp0==8'hff;
wire special2 = sign && !exp[7] && (exp>31);
wire special3 = !sign && !exp[7] && (exp>31);
wire [7:0] shift_wire = 8'd31-exp;
wire [5:0] shift = (shift_wire>31) ? 6'd32 : shift_wire[5:0];
wire special0 = (ZERO==ain[30:0]) ||(shift>31);
wire [31:0] mant2 = mant>>shift;
wire [31:0] mant3 = sign ? -mant2 : mant2;
assign out = 
      special3 ? 32'h7fffffff 
    : special2 ? 32'h80000000 
    :(special0||special1) ? 0 
    : mant3;
wire [31:0] mask0 = (1<<(WID-1))-1;
wire [31:0] mask1 = ~mask0;
wire [31:0] data0 = out & mask1;
wire [31:0] data1 = data0 | mask0;
wire all_good =  (data0==0)||(data1==32'hffffffff);
wire panic = !all_good;
endmodule
