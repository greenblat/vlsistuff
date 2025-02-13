


module agent (input [7:0] localid,input last_one,input clk, input rst_n, input en, input [135:0] msgin, output okin,  output [135:0] msgout, input okout);

wire emptyin ;
reg startin ;
wire vldout ;
wire fullout ;
wire fulltransfer ;
wire emptytransfer ;
wire emptyout ;


reg busy;
reg [63:0] aa,bb;
reg [7:0] id;
wire start_wire = (!busy && !emptyin) ;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        id <= 0; aa<=0; bb<=0; busy <= 0;
        startin <= 0;
    end else begin
        startin <=  start_wire;
        if (start_wire)  begin
            {aa,bb,id} = msg;
            busy <= 1;
        end else if (busy) begin
            if (vldout) busy <= 0;
        end
    end
end

wire [135:0] msgentry;
wire emptyientrn,emptyientry,readoutientry;
syncfifo #(.WID(64+64+8),.DEPTH(2))  fifoentry (.clk(clk),.rst_n(rst_n)
    ,.din(msgin),.vldin(msgin[7:0]!=0)
    ,.dout(msgentry),.empty(emptyentry),.full(fullentry),.readout(readoutentry)
    ,.softreset(1'b0),.count(),.overflow(panicentry)
);
assign okin =  !fullentry;


wire [64+64+8-1:0] msg,msgtransfer;
wire takein = !fullin && !emptyentry  && !msgentry[7];
wire move_forward = !emptyentry  &&  ( (!last_one && fullin) || msgentry[7]) && !fulltransfer;
assign readoutentry = takein || move_forward;

syncfifo #(.WID(64+64+8),.DEPTH(2))  fifoin (.clk(clk),.rst_n(rst_n)
    ,.din(msgentry),.vldin(takein)
    ,.dout(msg),.empty(emptyin),.full(fullin),.readout(start_wire)
    ,.softreset(1'b0),.count(),.overflow(panicin)
);


wire readouttransfer = !emptytransfer && okout;
wire readoutout = okout && !emptyout && emptytransfer;

syncfifo #(.WID(64+64+8),.DEPTH(2))  fifotransfer (.clk(clk),.rst_n(rst_n)
    ,.din(msgentry),.vldin(move_forward)
    ,.dout(msgtransfer),.empty(emptytransfer),.full(fulltransfer),.readout(readouttransfer)
    ,.softreset(1'b0),.count(),.overflow(panictransfer)
);
wire [135:0] msgout0;
syncfifo #(.WID(64+64+8),.DEPTH(4))  fifoout (.clk(clk),.rst_n(rst_n)
    ,.din({localid,56'b0,result,(8'h80|id)}),.vldin(vldout)
    ,.dout(msgout0),.empty(emptyout),.full(fullout),.readout(readoutout)
    ,.softreset(1'b0),.count(),.overflow(panicout)
);

assign msgout = !emptytransfer ? {msgtransfer} : !emptyout ? msgout0 : 0;


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

wire [63:0] result = remainder[63:0];

endmodule

