


module read_axi_depot #(parameter IDWID=4, parameter BWID=4) (
    input clk, input rst_n
    ,output active
    ,input [IDWID-1:0] arid
    ,input [15:0] arbytes
    ,input arvalid
    ,output taken
    ,output reg [IDWID-1:0] activeid

    ,input rvalid
    ,input rready
    ,input [IDWID-1:0] rid
    ,input [BWID-1:0] backbytes

    ,output rlast
);


reg [1:0] state;
reg [15:0] runbytes;
wire [15:0] newbytes;

assign active = state!=0;

wire fifo_empty,fifo_full;
wire use_data =  rvalid && rready && (rid==activeid) && active;
wire readout = use_data && !fifo_empty;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        state <= 0;
        activeid <= 0;
        runbytes <= 0;
    end else begin
        if (state==0) begin
            if (arvalid) begin
                state<= 1;
                activeid <= arid;
                runbytes <= arbytes;
            end
         end else if (state==1) begin
            if (use_data) begin
                if (rlast) begin
                    if (fifo_empty) begin
                        state<=0;
                    end else begin
                        runbytes <= newbytes;
                    end
                end else begin
                    runbytes <= runbytes - backbytes-1;
                end
            end
         end
    end
end

wire push_to_fifo = (rid==activeid) && active && rvalid;
syncfifo #(16,8) record_fifo (.clk(clk),.rst_n(rst_n),.softreset(1'b0)
    ,.validin(push_to_fifo),.datain(arbytes)
    ,.full(fifo_full),.empty(fifo_empty),.overflow(),.count()
    ,.readout(readout),.dataout(newbytes)
);

assign taken = !fifo_full;

assign rlast = (backbytes>=runbytes)&&(rid==activeid)&& active;

endmodule

