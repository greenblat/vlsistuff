module rrr (     input rst
    ,input clk
    ,output aout
);
nmos #(21,7) nmos_0 ( .o(wire1)
 ,.i(gnd)
 ,.g(wire15)
);
res #(.size(80)) res_0 ( .p(wire1)
 ,.n(aout)
);
res #(.size(75)) res_1 ( .p(aout)
 ,.n(vcc)
);
nmos #(14,7) nmos_1 ( .i(gnd)
 ,.o(wire10)
 ,.g(wire14)
);
res #(.size(40)) res_2 ( .n(aout)
 ,.p(wire10)
);
cap #(.size(_10pf)) cap_0 ( .n(aout)
 ,.p(gnd)
);
res #(.size(10)) res_3 ( .n(aout)
 ,.p(wire21)
);
res #(.size(20)) res_4 ( .n(aout)
 ,.p(wire20)
);
nmos #(7,6) nmos_2 ( .o(wire20)
 ,.i(gnd)
 ,.g(wire26)
);
nmos #(0,6) nmos_3 ( .o(wire21)
 ,.i(gnd)
 ,.g(wire25)
);
cntrl #(-11,22) cntrl_0 ( .a[0](wire29)
 ,.a[1](wire30)
 ,.a[2](wire31)
 ,.a[3](wire32)
 ,.rst(rst)
 ,.clk(clk)
);
endmodule
