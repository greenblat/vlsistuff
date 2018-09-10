
module ram_single_port #(  parameter DWID=128, parameter WORDS = 1024, parameter AWID= $clog2(WORDS)
)( 
    input clk
    ,input cen
    ,input wen
    ,input [AWID-1:0] addr
    ,input [DWID-1:0] bwen
    ,input [DWID-1:0] wdata
    ,output reg [DWID-1:0] rdata
);

reg talk; initial talk=1;

reg [DWID-1:0] array [0:WORDS-1];
wire [DWID-1:0] prev_data =  array[addr];
integer ii;
initial begin
    for (ii=0;ii<WORDS;ii=ii+1) 
         array[ii]={DWID{1'b0}};
end

always @(posedge clk) if (!cen && wen) begin
    rdata<= prev_data;
    if (talk) $display("ram %m read ram[%h] => %h",addr,prev_data);
end


wire [DWID-1:0] new_value = (~bwen & wdata) | (bwen & prev_data);
always @(posedge clk) if (!cen && !wen) begin
    if (talk) $display("eam %m written ram[%h] <= %h",addr,new_value);
    array[addr] <= new_value;
end


endmodule

