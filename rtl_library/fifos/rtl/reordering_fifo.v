

module reordering_fifo #(parameter WID = 32, parameter DEPTH=8, parameter AWID = $clog2(DEPTH))(
     input clk,input rst_n, input softreset
    ,input vldin, input [WID-1:0] din, input [AWID:0] order, output full
    ,input readout, output [WID-1:0] dout, output empty
    ,output [15:0] count
);



parameter DEPTH1 = DEPTH-1;
parameter AWID1  = AWID-1;
reg [WID-1:0] fifos [0:DEPTH1];
reg [AWID:0] orders [0:DEPTH1];


wire [AWID:0] dbg0 = orders[0];
wire [AWID:0] dbg1 = orders[1];
wire [AWID:0] dbg2 = orders[2];
wire [AWID:0] dbg3 = orders[3];
wire [AWID:0] dbg4 = orders[4];
wire [AWID:0] dbg5 = orders[5];
wire [AWID:0] dbg6 = orders[6];
wire [AWID:0] dbg7 = orders[7];



reg [DEPTH1:0] valids ;
reg [AWID:0] int_count;
assign count = int_count;

reg [AWID1:0] wptr,rptr;
reg found;

reg [AWID:0] wcurrent,rcurrent;

always @* begin
    found = 0;
    rptr = 0;
    for (int ii=0;ii<DEPTH;ii=ii+1) begin
        if (valids[ii] && (rcurrent == orders[ii])) begin
            found = 1;
            rptr = ii;
        end
    end
end
        

wire   int_empty = int_count == 0;
assign empty = !found;
assign   full = int_count == DEPTH;
assign   dout = fifos[rptr];
wire overflow = vldin && full;

always @(posedge clk) begin
    if (vldin && !full) begin
        fifos[wptr] <= din;
        orders[wptr] <= order;
    end
end

always @(posedge clk or negedge rst_n) begin
    if(!rst_n) begin
       wptr <= 0; int_count<=0;
       valids <= 0;
       wcurrent <= 0;
       rcurrent <= 0;
    end else if(softreset) begin
        wptr <= 0; int_count<=0; valids <= 0; wcurrent <= 0;
    end else begin
        if(vldin && !full) begin
            wptr <= (wptr==(DEPTH1)) ? 0 : (wptr + 1'b1);
            valids[wptr] <= 1;
            wcurrent <= (wcurrent==(2*DEPTH - 1)) ? 0 :wcurrent + 1;
        end
        if (readout && found) begin
           rcurrent <= (rcurrent==(2*DEPTH-1)) ? 0 :rcurrent + 1;
            valids[rptr] <= 0;
        end

        int_count <=
            ((vldin && !full)&&(readout && !empty))  ? int_count :
            (vldin && !full)  ? (int_count+1'b1) :
            (readout && !empty)  ? (int_count-1'b1) :
            int_count;

    end
end


wire [63:0]  sign_version = 64'h000233c514240424 ;
endmodule




