

module bridge2_manager #(
     parameter DWID = 128 
    ,parameter AWID = 32
    ,parameter TWID = 5 
    ,parameter BWID = 
        (DWID==512)  ? 6 : 
        (DWID==256)  ? 5 : 
        (DWID==128) ? 4 : 
        (DWID==64)  ? 3 : 2 
    ,parameter WID = 2+DWID+AWID+BWID+TWID
    ,parameter WBUFS = 6
) (
    input clk, input rst_n

    ,input [WID-1:0] rou_in0, input rou_in0_seen, output [1:0] splitter0_sel
    ,input [WID-1:0] rou_in1, input rou_in1_seen, output [1:0] splitter1_sel

    ,output softreset
);

parameter NOTLEGAL= (1<<WBUFS)-1;
assign softreset = 0;
reg [AWID-1:0] lo_address;
reg [AWID-1:0] hi_address;

wire [AWID-1:0] rou_in0_addr,rou_in1_addr;
reg side0close,side1close;


wire rou_in0_mngresponce,rou_in0_mngrequest;
rou_msg_fields rou_in0_fields(.msg(rou_in0), .addr(rou_in0_addr) ,.tags() ,.bytes() ,.cmd() ,.data());
rou_msg_parser  rou_in0_parser (.msg(rou_in0),.msg_reset(rou_in0_reset),.msg_enumerate(rou_in0_enumerate),.msg_controls()
    ,.msg_mngrequest(rou_in0_mngrequest)
    ,.msg_mngresponce(rou_in0_mngresponce)
);


wire rou_in1_mngresponce,rou_in1_mngrequest;
rou_msg_fields rou_in1_fields(.msg(rou_in1), .addr(rou_in1_addr) ,.tags() ,.bytes() ,.cmd() ,.data());
rou_msg_parser  rou_in1_parser (.msg(rou_in1),.msg_reset(rou_in1_reset),.msg_enumerate(rou_in1_enumerate),.msg_controls()
    ,.msg_mngrequest(rou_in1_mngrequest)
    ,.msg_mngresponce(rou_in1_mngresponce)
);

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        lo_address <= 0;
        hi_address <= 0;
        side0close <= 0;
        side1close <= 0;
    end else begin
        if (rou_in0_mngrequest && !side0close && !side1close) begin
            side0close <= 1'b1;
        end else if (rou_in0_reset) begin
            side0close <= 1'b0;
        end

        if (rou_in1_mngrequest && !side0close && !side1close) begin
            side1close <= 1'b1;
        end else if (rou_in1_reset) begin
            side1close <= 1'b0;
        end

        if (rou_in0_enumerate && !side1close) begin
            lo_address <= rou_in0_addr;
        end
        if (rou_in0_enumerate && side1close) begin
            hi_address <= rou_in0_addr;
        end

        if (rou_in1_enumerate && !side0close) begin
            lo_address <= rou_in1_addr;
        end
        if (rou_in1_enumerate && side0close) begin
            hi_address <= rou_in1_addr;
        end
    end
end
            
assign splitter0_sel = 
    (rou_in0_mngresponce && side0close) ? 2'd1 :  
    (rou_in0_mngresponce && side1close) ? 2'd2 :  
    rou_in0_mngrequest? 2'd2 : 
    (rou_in0_addr<lo_address) ?  2'd1 : 
    (rou_in0_addr>=hi_address) ?  2'd1 : 
    2'd2;

assign splitter1_sel = 
    (rou_in1_mngresponce && side1close) ? 2'd2 :  
    (rou_in1_mngresponce && side0close) ? 2'd1 :  
    rou_in1_mngrequest? 2'd1 : 
    (rou_in1_addr<lo_address) ?  2'd1 : 
    (rou_in1_addr>=hi_address) ?  2'd1 : 
    2'd2;


endmodule

