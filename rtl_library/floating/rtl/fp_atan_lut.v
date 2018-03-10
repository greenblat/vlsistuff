module fp_atan_lut ( input do_atan,input [31:0] ain,output reg [31:0] out,output reg vldout, input clk,input rst_n,input en);
wire [31:0] two = 32'h3fffffff;
wire [31:0] ten = 32'h411fffff;
wire gt2,gt10;
wire isneg = ain[31];
fp_gt i_gt2 (.bin(two),.ain({1'b0,ain[30:0]}),.out(gt2));
fp_gt i_gt10 (.bin(ten),.ain({1'b0,ain[30:0]}),.out(gt10));
wire [5:0] shift6 = gt10 ? 15 : gt2 ? 17 : 19;
wire [31:0] ain0;
fp_float2int fint0(.ain({1'b0,ain[30:0]}),.bin(shift6),.out(ain0));
reg [31:0] ain1;
reg d1_gt2,d1_gt10,d1_isneg,d1_do_atan;
always @(posedge clk) if (en && do_atan) ain1 <= ain0 - (gt10 ? 327680 : gt2 ? 262144 : 0);
always @(posedge clk) if (en && do_atan) d1_gt2 <= gt2;
always @(posedge clk) if (en && do_atan) d1_gt10 <= gt10;
always @(posedge clk) if (en && do_atan) d1_isneg <= isneg;
always @(posedge clk) if (en) d1_do_atan <= do_atan;
wire [31:0] ain2 = d1_gt10 ? (ain1) : d1_gt2 ? ain1 : ain1;
wire [9:0] diff = ain2[9:0];
wire [10:0] addr0 = ain2[20:10];
wire take_last = (addr0==1023);
wire [10:0] addr1 = take_last ? addr0 : (addr0+1);
wire [24:0] res0,res1,res2,res3,res4,res5;
wire [24:0] last1,last3,last5;
atan_table_till_2 atan0 (.addr(addr0[9:0]),.result(res0[24:0]),.lastone());
atan_table_till_2 atan1 (.addr(addr1[9:0]),.result(res1[24:0]),.lastone(last1));
atan_table_till_10 atan10 (.addr(addr0[9:0]),.result(res2[24:0]),.lastone());
atan_table_till_10 atan11 (.addr(addr1[9:0]),.result(res3[24:0]),.lastone(last3));
atan_table_till_32k atan320(.addr(addr0[9:0]),.result(res4[24:0]),.lastone());
atan_table_till_32k atan321 (.addr(addr1[9:0]),.result(res5[24:0]),.lastone(last5));
wire [24:0] result0 =  d1_gt10 ? res4 : d1_gt2 ? res2 : res0;
wire [24:0] result1 =  
       take_last  
    ? (d1_gt10 ? last5 : d1_gt2 ? last3 : last1) 
    : (d1_gt10 ? res5 : d1_gt2 ? res3 : res1)
    ;
wire [10:0] less = 11'h400 - diff;
wire [35:0] result2 = result0*less + result1*diff; 
wire [24:0] result3 = result2[35:11];
wire [5:0] backShift = 64-23;
wire [31:0] genericresult;
fp_int2float intf0(.ain({7'b0,result3}),.bin(backShift),.out(genericresult),.is_signed(1'b0));
wire [31:0] out_wire = {d1_isneg,genericresult[30:0]};
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        vldout <=  d1_do_atan;
    end else begin
        if (d1_do_atan) out <=  out_wire;
        vldout <=  d1_do_atan;
    end
end
endmodule
