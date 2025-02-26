
module math_subsys ( input clk, input rst_n, input startin, input [63:0] aa, input [63:0] bb
    ,input [31:0] idin
    ,output vldout
    ,output [63:0] result
    ,output [31:0] idout
    ,output busy
    ,input en
);

syncfifo32x100 fifoid (.clk(clk),.rst_n(rst_n)
    ,.din(idin),.vldin(startin)
    ,.dout(idout),.empty(fifoidempty),.full(),.readout(vldout)
    ,.softreset(1'b0),.count(),.overflow()
);
assign busy = !fifoidempty;

wire panic0 = fifoidempty && vldout ;


wire [31:0] dout0,dout1,dout2,dout3;
wire [31:0] dout4,dout5,dout6,dout7;
wire [31:0] dout8,dout9,douta,doutb;
wire [31:0] doutc,doutd,doute,doutf;
wire vld0;
mul16x16 mul0 ( .clk(clk),.rst_n(rst_n),.ain(aa[15:0]),.bin(bb[15:0]),.vldin(startin),.vldout(vld0),.dout(dout0));
mul16x16 mul1 ( .clk(clk),.rst_n(rst_n),.ain(aa[15:0]),.bin(bb[31:16]),.vldin(startin),.vldout(),.dout(dout1));
mul16x16 mul2 ( .clk(clk),.rst_n(rst_n),.ain(aa[15:0]),.bin(bb[47:32]),.vldin(startin),.vldout(),.dout(dout2));
mul16x16 mul3 ( .clk(clk),.rst_n(rst_n),.ain(aa[15:0]),.bin(bb[63:48]),.vldin(startin),.vldout(),.dout(dout3));

mul16x16 mul4 ( .clk(clk),.rst_n(rst_n),.ain(aa[31:16]),.bin(bb[15:0]),.vldin(startin),.vldout(),.dout(dout4));
mul16x16 mul5 ( .clk(clk),.rst_n(rst_n),.ain(aa[31:16]),.bin(bb[31:16]),.vldin(startin),.vldout(),.dout(dout5));
mul16x16 mul6 ( .clk(clk),.rst_n(rst_n),.ain(aa[31:16]),.bin(bb[47:32]),.vldin(startin),.vldout(),.dout(dout6));
mul16x16 mul7 ( .clk(clk),.rst_n(rst_n),.ain(aa[31:16]),.bin(bb[63:48]),.vldin(startin),.vldout(),.dout(dout7));

mul16x16 mul8 ( .clk(clk),.rst_n(rst_n),.ain(aa[47:32]),.bin(bb[15:0]),.vldin(startin),.vldout(),.dout(dout8));
mul16x16 mul9 ( .clk(clk),.rst_n(rst_n),.ain(aa[47:32]),.bin(bb[31:16]),.vldin(startin),.vldout(),.dout(dout9));
mul16x16 mula ( .clk(clk),.rst_n(rst_n),.ain(aa[47:32]),.bin(bb[47:32]),.vldin(startin),.vldout(),.dout(douta));
mul16x16 mulb ( .clk(clk),.rst_n(rst_n),.ain(aa[47:32]),.bin(bb[63:48]),.vldin(startin),.vldout(),.dout(doutb));

mul16x16 mulc ( .clk(clk),.rst_n(rst_n),.ain(aa[63:48]),.bin(bb[15:0]),.vldin(startin),.vldout(),.dout(doutc));
mul16x16 muld ( .clk(clk),.rst_n(rst_n),.ain(aa[63:48]),.bin(bb[31:16]),.vldin(startin),.vldout(),.dout(doutd));
mul16x16 mule ( .clk(clk),.rst_n(rst_n),.ain(aa[63:48]),.bin(bb[47:32]),.vldin(startin),.vldout(),.dout(doute));
mul16x16 mulf ( .clk(clk),.rst_n(rst_n),.ain(aa[63:48]),.bin(bb[63:48]),.vldin(startin),.vldout(),.dout(doutf));


wire [127:0] dmid_wire = 
       dout0
    + {dout1,16'b0}
    + {dout2,32'b0}
    + {dout3,48'b0}

    + {dout4,16'b0}
    + {dout5,32'b0}
    + {dout6,48'b0}
    + {dout7,64'b0}

    + {dout8,32'b0}
    + {dout9,48'b0}
    + {douta,64'b0}
    + {doutb,80'b0}

    + {doutc,48'b0}
    + {doutd,64'b0}
    + {doute,80'b0}
    + {doutf,96'b0}
;

reg [127:0] dmid; always @(posedge clk) dmid <= dmid_wire;

reg vld1; always @(posedge clk) vld1 <= vld0;


wire [127:0] PR = 17640718939615885909;


wire [126:0] remainder;
divider_u128_u128_64 divi (
     .ain(dmid)
    ,.bin(PR)
    ,.clk(clk)
    ,.en(en)
    ,.out()
    ,.remainder(remainder)
    ,.rst_n(rst_n)
    ,.vldin(vld1)
    ,.vldout(vldout)
);

assign result = remainder[63:0];

endmodule

