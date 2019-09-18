




module axi_firewall_rule #(parameter RULEWID=35,parameter AWIDREC = 4+32+8+3+2+4+4+3) (
    input clk, input rst_n
    ,output validout, output killout

    ,input [AWIDREC-1:0] fifo_data
    ,input avalid


    ,input [RULEWID-1:0] rulein



);

wire [3:0] aid;
wire [31:0] addr;
wire [7:0]  alen;
wire [2:0]  asize;
wire [1:0]  aburst;
wire [3:0]  acache;
wire [3:0]  aqos;
wire [2:0]  aprot;


assign {aid,addr,alen,asize,aburst,acache,aqos,aprot} = fifo_data;


endmodule

