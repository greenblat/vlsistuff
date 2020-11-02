module NAND3 (input A, output Y, input C, input B);
`ifdef REGISTER
initial begin
   $display("register  %m.stuck_1_A input");
   $display("register  %m.stuck_0_Y output");
   $display("register  %m.stuck_1_Y output");
   $display("register  %m.stuck_1_C input");
   $display("register  %m.stuck_1_B input");
end
`endif
reg stuck_1_A; initial stuck_1_A=0;
wire d_A = stuck_1_A ? 1 : A;
reg stuck_0_Y; initial stuck_0_Y=0;
reg stuck_1_Y; initial stuck_1_Y=0;
wire d_Y;
assign Y = stuck_1_Y ? 1 : stuck_0_Y ? 0 : d_Y;
reg stuck_1_C; initial stuck_1_C=0;
wire d_C = stuck_1_C ? 1 : C;
reg stuck_1_B; initial stuck_1_B=0;
wire d_B = stuck_1_B ? 1 : B;
assign d_Y = ! ( d_A && d_B && d_C );
endmodule
