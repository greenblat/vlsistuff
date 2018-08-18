
module ram_single_port #(  parameter DWID=128, parameter WORDS = 1024, parameter AWID= $clog2(WORDS)
)( 
    input clk, input rst_n
    ,input cen
    ,input wen
    ,input [AWID-1:0] addr
    ,input [DWID-1:0] bwen
    ,input [DWID-1:0] wdata
    ,output [DWID-1:0] rdata
);


reg [255:0] path;
reg [15:0] myid;
initial begin
    #1; 
    $swrite(path,"%m");
    myid = tb.idindex;
    tb.idindex = tb.idindex+1;
    tb.paths[myid] = path;
    $python("initial()",myid);
end

always @(negedge clk) begin
    if (rst_n==1) $python("work_ram_single_port()",myid,"ram");
end










endmodule

