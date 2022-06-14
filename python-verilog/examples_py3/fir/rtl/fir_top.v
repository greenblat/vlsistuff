
module fir_top (
    input clk, input rst_n,
    input psel
    ,input [31:0] paddr
    ,input penable
    ,input pwrite
    ,input [31:0] pwdata
    ,output pready
    ,output [31:0] prdata
    ,input [7:0] sample
    ,input vldin
    ,output [7:0] result
    ,output vldout
);
wire [63:0] coeffs;
wire [3:0] scalefactor;
wire enable;
fir fir ( .clk(clk),.sample(sample),.vldin(vldin)
    ,.coeffs(coeffs),.vldout(vldout),.result(result),.scalefactor(scalefactor)
    ,.saturation(saturation)
);

fir_rgf rgf (.pclk(clk),.presetn(rst_n),.psel(psel),.penable(penable),.pwdata(pwdata),.prdata(prdata),.pwrite(pwrite),.pready(pready)
    ,.pstrb(4'hf)
    ,.paddr(paddr)
    ,.coeffs(coeffs),.scalefactor(scalefactor)
    ,.goods(goods)
    ,.bads(bads)
    ,.enable(enable)
);

reg [31:0] goods,bads;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        goods <= 0;
        bads <= 0;
    end else if (!enable) begin
        goods <= 0;
        bads <= 0;
    end else begin
        goods <= goods + !saturation;
        bads <= bads + saturation;
    end
end


endmodule

