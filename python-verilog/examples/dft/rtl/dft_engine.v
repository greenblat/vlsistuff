

module dft_engine (
    input clk, input rst_n

    ,input start
    ,output sample_read
    ,output [7:0] sample_addr
    ,input  [15:0] sample_data

    ,output [7:0] result_addr
    ,output [15:0]  result_data
    ,output result_write
    ,output finished
);

reg [11:0] runaddr;

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        runaddr<=0;
        step<=0;
    end else begin
        if (active==0) begin
            if (start) active<=1;
        end else if (active) begin
        end
    end
end


sintable sintable(.ain(runaddr),.out(

endmodule

