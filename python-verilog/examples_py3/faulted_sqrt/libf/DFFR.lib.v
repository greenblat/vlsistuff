module DFFR (input CK, output Q, input RN, input D);
`ifdef REGISTER
initial begin
   $display("register  %m.stuck_0_Q output");
   $display("register  %m.stuck_1_Q output");
   $display("register  %m.stuck_0_D input");
   $display("register  %m.stuck_1_D input");
end
`endif
reg stuck_0_Q; initial stuck_0_Q=0;
reg stuck_1_Q; initial stuck_1_Q=0;
wire d_Q;
assign Q = stuck_1_Q ? 1 : stuck_0_Q ? 0 : d_Q;
reg stuck_0_D; initial stuck_0_D=0;
reg stuck_1_D; initial stuck_1_D=0;
wire d_D = stuck_1_D ? 1 : stuck_0_D ? 0 : D;
reg IQ;
always @(posedge tb.forceX) IQ <= 1'bx;
always @(posedge tb.checkX) if (IQ===1'bx) $display(" %m is x");
wire IQN = !IQ;
always @(posedge CK or negedge RN) if (! RN) IQ<=0; else IQ<= d_D;
assign d_Q = IQ;
endmodule
