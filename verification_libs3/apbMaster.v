

module apbMaster ( input clk, input rst_n

    ,input xread, input xwrite, input [31:0] xaddr, input [31:0] xwdata
    ,output reg [31:0] xrdata, output reg xvalid
    ,output xidle


    ,output reg psel, output reg penable, output reg pwrite
    , output reg [31:0] paddr
    , output reg [31:0] pwdata, output reg [3:0] pstrb
    ,input pready, input pslverr, input [31:0] prdata
);
reg [3:0] state;
assign xidle = state==0;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        state <= 0;
        xvalid <= 0;
        xrdata <= 0;
        psel <= 0;
        penable <= 0;
        pwrite <= 0;
        paddr <= 0;
        pwdata <= 0;
        pstrb <= 15;
    end else begin
        if (state == 0) begin
            xvalid <= 0;
            if (xwrite) begin
                paddr <= xaddr;
                pwdata <= xwdata;
                psel <= 1;
                penable <= 0;
                pstrb <= 15;
                state <= 10;
                pwrite <= 1;
            end else if (xread) begin
                paddr <= xaddr;
                psel <= 1;
                penable <= 0;
                state <= 1;
            end
        end else if (state == 1) begin
            if (pready) begin
                state <= 2;
                penable <= 1;
            end
        end else if (state == 2) begin
            if (pready) begin
                xrdata <= prdata;
                state <= 0;
                xvalid <= 1;
                penable <= 0;
                psel <= 0;
            end
        end else if (state == 10) begin
            if (pready) begin
                state <= 11;
                penable <= 1;
            end
        end else if (state == 11) begin
            if (pready) begin
                state <= 0;
                penable <= 0;
                pwrite <= 0;
                psel <= 0;
            end
        end
    end
end




endmodule

