


module ahblite_slave (
     input hclk
    ,input hresetn

    ,input [1:0] htrans
    ,input [2:0] hburst
    ,input hsel
    ,input hwrite
    ,input [2:0] hsize
    ,input [3:0] hprot
    ,input [31:0] haddr
    ,input [31:0] hwdata

    ,output [31:0] hrdata
    ,output hreadyout
    ,output hresp


    ,output [31:0] paddr
    ,output [31:0] pwdata
    ,output        pwrite
    ,output [3:0]  pstrb
    ,output        pread
    ,input  [31:0] prdata
    ,input         pready




);

localparam IDLE = 0;
localparam BUSY  = 1;
localparam NONSEQ = 2;
localparam SEQ = 3;

reg [31:0] addr0,addr1;
reg writing0,writing1;
reg valid0,valid1;
reg [2:0] wsize0;

wire relevant_trans = (htrans==2)||(htrans==3);
wire relevant_hsel = hsel && relevant_trans;

always @(posedge hclk or negedge hresetn) begin
    if (!hresetn) begin
        addr0    <= 0;
        writing0 <= 0;
        addr1    <= 0;
        writing1 <= 0;
        valid0 <= 0;
        valid1 <= 0;
        wsize0 <= 0;
    end else begin
        if (relevant_hsel && hreadyout) begin
            addr0 <= haddr;
            writing0 <= hwrite;
            valid0 <= 1;
            wsize0 <= hsize;
        end else if (!hsel) begin
            addr0 <= 0;
            writing0 <= 0;
            valid0 <= 0;
        end

        addr1 <= addr0;
        writing1 <= writing0;
        valid1 <= valid0;
    end
end
reg [31:0] wdata0;
always @(posedge hclk or negedge hresetn) begin
    if (!hresetn) begin
        wdata0 <= 0;
    end else begin
        wdata0 <= hwdata;
    end
end

assign pwrite = writing0 && valid0;

assign hreadyout = (!hsel) ? 1
    : (writing0 && valid0) ? pready
    : (!writing0 && valid0) ?  pready
    : 1;

assign pread = relevant_hsel && !pwrite;

assign hresp = (!relevant_hsel) ? 0 :  (hsize>2);

assign pstrb = 
    (wsize0==0) ?  (1<<addr0[1:0]) : 
    (wsize0==1) ?  (3<<addr0[1])    :
    (wsize0==2) ?   4'hf    :
    0;

assign paddr = addr0;
assign pwdata = hwdata;
assign hrdata = prdata;
endmodule




