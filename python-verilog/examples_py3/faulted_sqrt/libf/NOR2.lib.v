module NOR2 (input A, output Y, input B);
`ifdef REGISTER
initial begin
   $display("register  %m.stuck_0_A input");
   $display("register  %m.stuck_1_A input");
   $display("register  %m.stuck_0_Y output");
   $display("register  %m.stuck_1_Y output");
   $display("register  %m.stuck_0_B input");
   $display("register  %m.stuck_1_B input");
end
`endif
reg stuck_0_A; initial stuck_0_A=0;
reg stuck_1_A; initial stuck_1_A=0;
wire d_A = stuck_1_A ? 1 : stuck_0_A ? 0 : A;
reg stuck_0_Y; initial stuck_0_Y=0;
reg stuck_1_Y; initial stuck_1_Y=0;
wire d_Y;
assign Y = stuck_1_Y ? 1 : stuck_0_Y ? 0 : d_Y;
reg stuck_0_B; initial stuck_0_B=0;
reg stuck_1_B; initial stuck_1_B=0;
wire d_B = stuck_1_B ? 1 : stuck_0_B ? 0 : B;
assign d_Y = ! ( d_A || d_B );
endmodule
