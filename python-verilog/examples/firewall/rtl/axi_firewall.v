module axi_firewall (
     input clk, input rst_n

// AXI MASTER
      // axi write address channel
    ,output [3:0] ms_awid           
    ,output [31:0] ms_awaddr
    ,output [7:0] ms_awlen
    ,output [2:0] ms_awsize
    ,output [1:0] ms_awburst
    ,output [3:0] ms_awcache
    ,output [3:0] ms_awqos
    ,output [2:0] ms_awprot
    ,output ms_awvalid
    ,input ms_awready
 // axi write data channel
    ,output [127:0] ms_wdata
    ,output [15:0] ms_wstrb
    ,output ms_wlast
    ,output ms_wvalid
    ,input ms_wready
 // axi write responce channel
    ,input [3:0] ms_bid
    ,input [1:0] ms_bresp
    ,input ms_bvalid
    ,output ms_bready
 // axi read address channel
    ,output [3:0] ms_arid
    ,output [31:0] ms_araddr
    ,output [7:0] ms_arlen
    ,output [2:0] ms_arsize
    ,output [1:0] ms_arburst
    ,output [3:0] ms_arcache
    ,output [3:0] ms_arqos
    ,output [2:0] ms_arprot
    ,output ms_arvalid
    ,input ms_arready
 // axi read data channel
    ,input [3:0] ms_rid
    ,input [127:0] ms_rdata
    ,input [1:0] ms_rresp
    ,input ms_rlast
    ,input ms_rvalid
    ,output ms_rready
 


// AXI SLAVE
      // axi write address channel
    ,input [3:0] sl_awid           
    ,input [31:0] sl_awaddr
    ,input [7:0] sl_awlen
    ,input [2:0] sl_awsize
    ,input [1:0] sl_awburst
    ,input [3:0] sl_awcache
    ,input [3:0] sl_awqos
    ,input [2:0] sl_awprot
    ,input sl_awvalid
    ,output sl_awready
 // axi write data channel
    ,input [127:0] sl_wdata
    ,input [15:0] sl_wstrb
    ,input sl_wlast
    ,input sl_wvalid
    ,output sl_wready
 // axi write responce channel
    ,output [3:0] sl_bid
    ,output [1:0] sl_bresp
    ,output sl_bvalid
    ,input sl_bready
 // axi read address channel
    ,input [3:0] sl_arid
    ,input [31:0] sl_araddr
    ,input [7:0] sl_arlen
    ,input [2:0] sl_arsize
    ,input [1:0] sl_arburst
    ,input [3:0] sl_arcache
    ,input [3:0] sl_arqos
    ,input [2:0] sl_arprot
    ,input sl_arvalid
    ,output sl_arready
 // axi read data channel
    ,output [3:0] sl_rid
    ,output [127:0] sl_rdata
    ,output [1:0] sl_rresp
    ,output sl_rlast
    ,output sl_rvalid
    ,input sl_rready
   
// secure APB slave
  ,input [15:0] paddr
  ,input       penable
  ,output [31:0] prdata
  ,output       pready
  ,input       psel
  ,output       pslverr
  ,input [31:0] pwdata
  ,input       pwrite

);
 
wire softreset= 1'b0;
wire wr_killout,rd_killout;
wire wr_validout,rd_validout;

parameter AWIDREC = 4+32+8+3+2+4+4+3;
wire [AWIDREC-1:0] sl_awfifo_in = { 
     sl_awid
    ,sl_awaddr
    ,sl_awlen
    ,sl_awsize
    ,sl_awburst
    ,sl_awcache
    ,sl_awqos
    ,sl_awprot
};



wire [AWIDREC-1:0] sl_awfifo_data,sl_awfifo_out_data;


assign {
     ms_awid
    ,ms_awaddr
    ,ms_awlen
    ,ms_awsize
    ,ms_awburst
    ,ms_awcache
    ,ms_awqos
    ,ms_awprot
} = sl_awfifo_out_data;


syncfifo #(AWIDREC,4) awfifo ( .clk(clk),.rst_n(rst_n) ,.softreset(softreset)
    ,.validin(sl_awvalid),.datain(sl_awfifo_in)
    ,.full(sl_awfifo_full),.empty(sl_awfifo_empty),.count()
    ,.readout(sl_awfifo_read),.dataout(sl_awfifo_data)
    ,.overflow()
);

syncfifo #(AWIDREC,4) awfifo_out ( .clk(clk),.rst_n(rst_n) ,.softreset(softreset)
    ,.validin(!sl_awfifo_empty && !wr_killout && wr_validout),.datain(sl_awfifo_data)
    ,.full(sl_awfifo_out_full),.empty(sl_awfifo_out_empty),.count()
    ,.readout(ms_awready),.dataout(sl_awfifo_out_data)
    ,.overflow()
);

assign ml_awvalid =  !sl_awfifo_out_empty;


wire [AWIDREC-1:0] sl_arfifo_in = { 
     sl_arid
    ,sl_araddr
    ,sl_arlen
    ,sl_arsize
    ,sl_arburst
    ,sl_arcache
    ,sl_arqos
    ,sl_arprot
};



wire [AWIDREC-1:0] sl_arfifo_data,sl_arfifo_data_out;

syncfifo #(AWIDREC,4) arfifo ( .clk(clk),.rst_n(rst_n) ,.softreset(softreset)
    ,.validin(sl_arvalid),.datain(sl_arfifo_in)
    ,.full(sl_arfifo_full),.empty(sl_arfifo_empty),.count()
    ,.readout(sl_arfifo_read),.dataout(sl_arfifo_data)
    ,.overflow()
);

syncfifo #(AWIDREC,4) arfifo_out ( .clk(clk),.rst_n(rst_n) ,.softreset(softreset)
    ,.validin(!sl_arfifo_empty && !rd_killout && rd_validout),.datain(sl_arfifo_data)
    ,.full(sl_arfifo_out_full),.empty(sl_arfifo_out_empty),.count()
    ,.readout(ms_arready),.dataout(sl_arfifo_out_data)
    ,.overflow()
);

assign {
     ms_arid
    ,ms_araddr
    ,ms_arlen
    ,ms_arsize
    ,ms_arburst
    ,ms_arcache
    ,ms_arqos
    ,ms_arprot
} = sl_arfifo_out_data;

assign ml_arvalid =  !sl_arfifo_out_empty;




wire wr_default_action ;
wire wr_validin ;
wire enable ;
wire rd_default_action ;
wire rd_validin ;





reg [7:0] rd_killed,wr_killed;
reg [1+1+8+8+32:0] rd_caught_data;
reg [1+1+8+8+32:0] wr_caught_data;
wire rd_caught_data_pulse,wr_caught_data_pulse;



wire [15:0] [31:0] addresses;

axi_firewall_rgf rgf (
     .clk(clk) ,.rst_n(rst_n)
    ,.paddr(paddr[9:0])
    ,.penable(penable)
    ,.prdata(prdata[31:0])
    ,.psel(psel)
    ,.pslverr(pslverr)
    ,.pwdata(pwdata[31:0])
    ,.pwrite(pwrite)



    ,.rd_caught_data_pulse(rd_caught_data_pulse)
    ,.rd_caught_data(rd_caught_data)
    ,.wr_caught_data_pulse(wr_caught_data_pulse)
    ,.wr_caught_data(wr_caught_data)

    ,.addresses(addresses)
);

wire [8-1:0] wr_validouts,rd_validouts;
wire [8-1:0] wr_killouts,rd_killouts;
parameter RULWID = 35;
wire [8-1:0] [RULWID-1:0] rules;

axi_firewall_rule wr_rule0 ( .clk(clk) ,.rst_n(rst_n)

    ,.killout(wr_killouts[0]) ,.validout(wr_validouts[0])
    ,.avalid(!sl_awfifo_empty)
    ,.fifo_data(sl_awfifo_data)

    ,.rulein(rules[0])


);

axi_firewall_rule rd_rule0 ( .clk(clk) ,.rst_n(rst_n)

    ,.killout(rd_killouts[0]) ,.validout(rd_validouts[0])
    ,.avalid(!sl_arfifo_empty)
    ,.fifo_data(sl_arfifo_data)


    ,.rulein(rules[0])

);
axi_firewall_rule wr_rule1 ( .clk(clk) ,.rst_n(rst_n)

    ,.killout(wr_killouts[1]) ,.validout(wr_validouts[1])
    ,.avalid(!sl_awfifo_empty)
    ,.fifo_data(sl_awfifo_data)

    ,.rulein(rules[1])


);

axi_firewall_rule rd_rule1 ( .clk(clk) ,.rst_n(rst_n)

    ,.killout(rd_killouts[1]) ,.validout(rd_validouts[1])
    ,.avalid(!sl_arfifo_empty)
    ,.fifo_data(sl_arfifo_data)


    ,.rulein(rules[1])

);
axi_firewall_rule wr_rule2 ( .clk(clk) ,.rst_n(rst_n)

    ,.killout(wr_killouts[2]) ,.validout(wr_validouts[2])
    ,.avalid(!sl_awfifo_empty)
    ,.fifo_data(sl_awfifo_data)

    ,.rulein(rules[2])


);

axi_firewall_rule rd_rule2 ( .clk(clk) ,.rst_n(rst_n)

    ,.killout(rd_killouts[2]) ,.validout(rd_validouts[2])
    ,.avalid(!sl_arfifo_empty)
    ,.fifo_data(sl_arfifo_data)


    ,.rulein(rules[2])

);
axi_firewall_rule wr_rule3 ( .clk(clk) ,.rst_n(rst_n)

    ,.killout(wr_killouts[3]) ,.validout(wr_validouts[3])
    ,.avalid(!sl_awfifo_empty)
    ,.fifo_data(sl_awfifo_data)

    ,.rulein(rules[3])


);

axi_firewall_rule rd_rule3 ( .clk(clk) ,.rst_n(rst_n)

    ,.killout(rd_killouts[3]) ,.validout(rd_validouts[3])
    ,.avalid(!sl_arfifo_empty)
    ,.fifo_data(sl_arfifo_data)


    ,.rulein(rules[3])

);
axi_firewall_rule wr_rule4 ( .clk(clk) ,.rst_n(rst_n)

    ,.killout(wr_killouts[4]) ,.validout(wr_validouts[4])
    ,.avalid(!sl_awfifo_empty)
    ,.fifo_data(sl_awfifo_data)

    ,.rulein(rules[4])


);

axi_firewall_rule rd_rule4 ( .clk(clk) ,.rst_n(rst_n)

    ,.killout(rd_killouts[4]) ,.validout(rd_validouts[4])
    ,.avalid(!sl_arfifo_empty)
    ,.fifo_data(sl_arfifo_data)


    ,.rulein(rules[4])

);
axi_firewall_rule wr_rule5 ( .clk(clk) ,.rst_n(rst_n)

    ,.killout(wr_killouts[5]) ,.validout(wr_validouts[5])
    ,.avalid(!sl_awfifo_empty)
    ,.fifo_data(sl_awfifo_data)

    ,.rulein(rules[5])


);

axi_firewall_rule rd_rule5 ( .clk(clk) ,.rst_n(rst_n)

    ,.killout(rd_killouts[5]) ,.validout(rd_validouts[5])
    ,.avalid(!sl_arfifo_empty)
    ,.fifo_data(sl_arfifo_data)


    ,.rulein(rules[5])

);
axi_firewall_rule wr_rule6 ( .clk(clk) ,.rst_n(rst_n)

    ,.killout(wr_killouts[6]) ,.validout(wr_validouts[6])
    ,.avalid(!sl_awfifo_empty)
    ,.fifo_data(sl_awfifo_data)

    ,.rulein(rules[6])


);

axi_firewall_rule rd_rule6 ( .clk(clk) ,.rst_n(rst_n)

    ,.killout(rd_killouts[6]) ,.validout(rd_validouts[6])
    ,.avalid(!sl_arfifo_empty)
    ,.fifo_data(sl_arfifo_data)


    ,.rulein(rules[6])

);
axi_firewall_rule wr_rule7 ( .clk(clk) ,.rst_n(rst_n)

    ,.killout(wr_killouts[7]) ,.validout(wr_validouts[7])
    ,.avalid(!sl_awfifo_empty)
    ,.fifo_data(sl_awfifo_data)

    ,.rulein(rules[7])


);

axi_firewall_rule rd_rule7 ( .clk(clk) ,.rst_n(rst_n)

    ,.killout(rd_killouts[7]) ,.validout(rd_validouts[7])
    ,.avalid(!sl_arfifo_empty)
    ,.fifo_data(sl_arfifo_data)


    ,.rulein(rules[7])

);

assign  wr_killout =
    wr_validouts[0] ? wr_killouts[0] :
    wr_validouts[1] ? wr_killouts[1] :
    wr_validouts[2] ? wr_killouts[2] :
    wr_validouts[3] ? wr_killouts[3] :
    wr_validouts[4] ? wr_killouts[4] :
    wr_validouts[5] ? wr_killouts[5] :
    wr_validouts[6] ? wr_killouts[6] :
    wr_validouts[7] ? wr_killouts[7] :
    wr_default_action;

assign wr_validout = wr_validin;

wire [3:0] wr_winner =  (!wr_validin || !enable) ? 4'bx :
    wr_validouts[0] ? 0 :
    wr_validouts[1] ? 1 :
    wr_validouts[2] ? 2 :
    wr_validouts[3] ? 3 :
    wr_validouts[4] ? 4 :
    wr_validouts[5] ? 5 :
    wr_validouts[6] ? 6 :
    wr_validouts[7] ? 7 :
    8;

assign  rd_killout =
    rd_validouts[0] ? rd_killouts[0] :
    rd_validouts[1] ? rd_killouts[1] :
    rd_validouts[2] ? rd_killouts[2] :
    rd_validouts[3] ? rd_killouts[3] :
    rd_validouts[4] ? rd_killouts[4] :
    rd_validouts[5] ? rd_killouts[5] :
    rd_validouts[6] ? rd_killouts[6] :
    rd_validouts[7] ? rd_killouts[7] :
    rd_default_action;

assign rd_validout = rd_validin;

wire [3:0] rd_winner =  (!rd_validin || !enable) ? 4'bx :
    rd_validouts[0] ? 0 :
    rd_validouts[1] ? 1 :
    rd_validouts[2] ? 2 :
    rd_validouts[3] ? 3 :
    rd_validouts[4] ? 4 :
    rd_validouts[5] ? 5 :
    rd_validouts[6] ? 6 :
    rd_validouts[7] ? 7 :
    8;

reg wr_caught;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        wr_caught <= 0;
        wr_caught_data <= 0;
    end else begin
        if (wr_caught_data_pulse) begin
            wr_caught <= 0;
            wr_caught_data <= 0;
        end else if (!wr_caught && wr_validout && enable && wr_killout)  begin
            wr_caught <= 1;
            wr_caught_data <= {
                1'b1
            };
        end
    end
end
reg rd_caught;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        rd_caught <= 0;
        rd_caught_data <= 0;
    end else begin
        if (rd_caught_data_pulse) begin
            rd_caught <= 0;
            rd_caught_data <= 0;
        end else if (!rd_caught && rd_validout && enable && rd_killout)  begin
            rd_caught <= 1;
            rd_caught_data <= {
                1'b1
            };
        end
    end
end

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) wr_killed <= 0;
    else if (enable && wr_validout && wr_killout && (wr_killed<255)) begin
        wr_killed <= wr_killed + 1;
    end
end

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) rd_killed <= 0;
    else if (enable && rd_validout && rd_killout && (rd_killed<255)) begin
        rd_killed <= rd_killed + 1;
    end
end



endmodule

