

module axi_master_32 (
// axi side clock and reset
     input clk
    ,input rst_n
    ,input softreset

// axi write addr channel
    ,input [3:0] awid           // addr write id
    ,input [31:0] awaddr
    ,input [7:0] awlen
    ,input [2:0] awsize
    ,input [1:0] awburst
    ,input awvalid
    ,input awready

// axi write data channel
    ,output [31:0] wdata
    ,output reg [3:0] wstrb
    ,output wlast
    ,output wvalid
    ,input wready

// axi write responce channel
    ,input [3:0] bid 
    ,input [1:0] bresp
    ,input bvalid
    ,output bready

// axi read addr channel
    ,output [3:0] arid
    ,output [31:0] araddr
    ,output [7:0] arlen
    ,output [2:0] arsize
    ,output [1:0] arburst
    ,output arvalid
    ,input arready
    
// axi read data channel
    ,input [3:0] rid 
    ,input [31:0] rdata
    ,input [1:0] rresp
    ,input rlast
    ,input rvalid
    ,output rready

    ,output local_rd
    ,input [31:0] local_rd_data
    ,input [3:0] wr_wstrb
    ,input [3:0] wdata_mode
);

wire [7:0] active_len;

syncfifo #(8,16) wdata_fifo (.clk(clk),.rst_n(rst_n),.softreset(1'b0)
    ,.validin(awvalid && awready),.datain(awlen)
    ,.full(),.empty(empty),.overflow(),.count()
    ,.readout(readout),.dataout(active_len)
);

reg [1:0] state;
reg [8:0] counter;

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        state<= 0;
        counter <= 0;
        wstrb <= 4'hf;
    end else begin
        if (state==0) begin
            if (!empty) begin
                counter <= active_len+1;
                wstrb <= wr_wstrb;
                state <= 1;
            end
        end else if (state==1) begin
            if (wready) begin
                wstrb <= 4'hf;
                counter <= counter -1;
                if (counter==1) begin
                    state<= 0;
                end
            end
        end
    end
end

assign wlast = (counter==1);
assign wvalid = (counter!=0);
assign wdata =  
    (wdata_mode==0) ? 0 :
    (wdata_mode==1) ? local_rd_data :
    (0 | counter) ;

assign local_rd =  (counter!=0) && wready && (wdata_mode==1);

endmodule

