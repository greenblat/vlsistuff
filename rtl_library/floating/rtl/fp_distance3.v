module fp_distance3 (input clk,input rst_n,input [31:0] ain,input [31:0] bin,input [31:0] cin
    ,input en,input vldin,output vldout,output [31:0] out);
wire [31:0] tmpa,tmpb,tmpc,tmpd;
fp_multiplier    muli0 (.ain(ain),.bin(ain),.out(tmpa));
fp_multiplier    muli1 (.ain(bin),.bin(bin),.out(tmpb));
fp_multiplier    muli2 (.ain(cin),.bin(cin),.out(tmpc));
fp_adder3         add0 (.in0(tmpa),.in1(tmpb),.in2(tmpc),.out(tmpd));
reg [31:0] tmpe;
reg vld1;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        vld1 <= 0;
        tmpe <= 0 ;
    end else if (en) begin
        vld1 <= vldin;
        if (vldin) tmpe <= tmpd;
    end  
end
fp_sqrt sqrt_dist(.clk(clk),.rst_n(rst_n),.en(en),.vldin(vld1),.vldout(vldout),.ain(tmpe),.out(out));
endmodule
