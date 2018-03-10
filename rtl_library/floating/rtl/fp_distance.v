module fp_distance (input clk,input rst_n,input [31:0] ain,input [31:0] bin,input en,input vldin,output vldout,output [31:0] out);
wire [31:0] tmpa,tmpb,tmpc;
fp_multiplier    muli0 (.ain(ain),.bin(ain),.out(tmpa));
fp_multiplier    muli1 (.ain(bin),.bin(bin),.out(tmpb));
fp_adder         add0 (.ain(tmpa),.bin(tmpb),.out(tmpc));
reg [31:0] tmpd;
reg vld1;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        vld1 <= 0;
        tmpd <= 0 ;
    end else if (en) begin
        vld1 <= vldin;
        if (vldin) tmpd <= tmpc;
    end  
end
fp_sqrt sqrt_dist(.clk(clk),.rst_n(rst_n),.en(en),.vldin(vld1),.vldout(vldout),.ain(tmpd),.out(out));
endmodule
