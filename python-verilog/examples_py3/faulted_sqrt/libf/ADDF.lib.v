module ADDF (input A, input CI, input B, output CO, output S);
`ifdef REGISTER
initial begin
   $display("register  %m.stuck_0_A input");
   $display("register  %m.stuck_1_A input");
   $display("register  %m.stuck_0_CI input");
   $display("register  %m.stuck_1_CI input");
   $display("register  %m.stuck_0_B input");
   $display("register  %m.stuck_1_B input");
   $display("register  %m.stuck_0_CO output");
   $display("register  %m.stuck_1_CO output");
   $display("register  %m.stuck_0_S output");
   $display("register  %m.stuck_1_S output");
end
`endif
reg stuck_0_A; initial stuck_0_A=0;
reg stuck_1_A; initial stuck_1_A=0;
wire d_A = stuck_1_A ? 1 : stuck_0_A ? 0 : A;
reg stuck_0_CI; initial stuck_0_CI=0;
reg stuck_1_CI; initial stuck_1_CI=0;
wire d_CI = stuck_1_CI ? 1 : stuck_0_CI ? 0 : CI;
reg stuck_0_B; initial stuck_0_B=0;
reg stuck_1_B; initial stuck_1_B=0;
wire d_B = stuck_1_B ? 1 : stuck_0_B ? 0 : B;
reg stuck_0_CO; initial stuck_0_CO=0;
reg stuck_1_CO; initial stuck_1_CO=0;
wire d_CO;
assign CO = stuck_1_CO ? 1 : stuck_0_CO ? 0 : d_CO;
reg stuck_0_S; initial stuck_0_S=0;
reg stuck_1_S; initial stuck_1_S=0;
wire d_S;
assign S = stuck_1_S ? 1 : stuck_0_S ? 0 : d_S;
assign d_CO = ( ( d_A ^ d_B ) && d_CI ) || ( d_A && d_B );
assign d_S = d_A ^ d_B ^ d_CI;
endmodule
