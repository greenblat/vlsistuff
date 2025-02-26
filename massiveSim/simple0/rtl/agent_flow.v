


module agent (input [7:0] localid,input clk, input rst_n, input en, input [159:0] msgin, output okin,  output [159:0] msgout, input okout, output busy);

wire [159:0] msgentry;
wire emptyientrn,emptyientry,readoutientry;
wire msg_vld = msgin[31:0]!=0;
syncfifo fifoentry (.clk(clk),.rst_n(rst_n)
    ,.din(msgin),.vldin(msg_vld)
    ,.dout(msgentry),.empty(emptyentry),.full(fullentry),.readout(startin)
    ,.softreset(1'b0),.count(),.overflow(panicentry)
);
assign okin =  !fullentry;

wire [31:0] id,idout;
wire [63:0] aa,bb;

assign {bb,aa,id} = msgentry;
wire math_busy;
wire startin = !emptyentry;
wire [63:0] result;
math_subsys subsys (
     .clk(clk)
    ,.rst_n(rst_n)
    ,.en(en)
    ,.startin(startin)
    ,.idin(id[31:0]) ,.aa(aa[63:0]) ,.bb(bb[63:0])

    ,.busy(math_busy)

    ,.idout(idout[31:0])
    ,.result(result[63:0])
    ,.vldout(vldout)
);


assign busy = math_busy || !emptyentry || !emptyout;


wire panic0 = vldout && fullout;

assign vldinout = vldout && !fullout;
wire readoutout = !emptyout && okout;
syncfifo  fifoout (.clk(clk),.rst_n(rst_n)
    ,.din({~result,result,idout}),.vldin(vldinout)
    ,.dout(msgout),.empty(emptyout),.full(fullout),.readout(readoutout)
    ,.softreset(1'b0),.count(),.overflow(panicout)
);



endmodule

