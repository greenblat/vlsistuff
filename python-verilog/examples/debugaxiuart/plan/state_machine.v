
module state_machine (input clk, input rst_n, input [7:0] datain, input validin, input enable, output idle_state
    ,output echo_flag
    ,output clear_flag
    ,output pusha_flag
    ,output pushd_flag
    ,output write_flag
    ,output read_flag
);
wire [7:0] ST_IDLE = 0;
wire [7:0] ST_WADDR0 = 1;
wire [7:0] ST_WADDR1 = 2;
wire [7:0] ST_WDATA0 = 3;
wire [7:0] ST_WDATA1 = 4;
wire [7:0] ST_WDATA2 = 5;
wire [7:0] ST_WDATA3 = 6;
wire [7:0] ST_WDATA4 = 7;
wire [7:0] ST_WDATA5 = 8;
wire [7:0] ST_WDATA6 = 9;
wire [7:0] ST_WDATA7 = 10;
wire [7:0] ST_RADDR0 = 11;
wire [7:0] ST_RADDR1 = 12;
wire [7:0] ST_RADDR2 = 13;
wire [7:0] CHRw = 8'h77;
wire [7:0] CHRr = 8'h72;

reg [7:0] state;
assign idle_state = (state==ST_IDLE);
wire [7:0] CHR0 = 8'h30;
wire [7:0] CHR9 = 8'h39;
wire [7:0] CHRA = 8'h41;
wire [7:0] CHRF = 8'h46;
wire [7:0] CHRa = 8'h61;
wire [7:0] CHRf = 8'h66;
wire hexvalid =
    ((datain>=CHR0)&&(datain<=CHR9)) ? 1 :
    ((datain>=CHRA)&&(datain<=CHRF)) ? 1 :
    ((datain>=CHRa)&&(datain<=CHRf)) ? 1 :
    0;

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        state <= ST_IDLE;
    end else begin
            if (validin && enable && (state==ST_IDLE)&& (datain==CHRw)) state <= ST_WADDR0;
        else if (validin && enable && (state==ST_WADDR0)&& hexvalid) state <= ST_WADDR1;
        else if (validin && enable && (state==ST_WADDR1)&& hexvalid) state <= ST_WDATA0;
        else if (validin && enable && (state==ST_WDATA0)&& hexvalid) state <= ST_WDATA1;
        else if (validin && enable && (state==ST_WDATA1)&& hexvalid) state <= ST_WDATA2;
        else if (validin && enable && (state==ST_WDATA2)&& hexvalid) state <= ST_WDATA3;
        else if (validin && enable && (state==ST_WDATA3)&& hexvalid) state <= ST_WDATA4;
        else if (validin && enable && (state==ST_WDATA4)&& hexvalid) state <= ST_WDATA5;
        else if (validin && enable && (state==ST_WDATA5)&& hexvalid) state <= ST_WDATA6;
        else if (validin && enable && (state==ST_WDATA6)&& hexvalid) state <= ST_WDATA7;
        else if (validin && enable && (state==ST_WDATA7)&& hexvalid) state <= ST_IDLE;
        else if (validin && enable && (state==ST_WADDR0)) state <= ST_IDLE;
        else if (validin && enable && (state==ST_WADDR1)&& !hexvalid) state <= ST_IDLE;
        else if (validin && enable && (state==ST_WDATA0)&& !hexvalid) state <= ST_IDLE;
        else if (validin && enable && (state==ST_WDATA1)&& !hexvalid) state <= ST_IDLE;
        else if (validin && enable && (state==ST_WDATA2)&& !hexvalid) state <= ST_IDLE;
        else if (validin && enable && (state==ST_WDATA3)&& !hexvalid) state <= ST_IDLE;
        else if (validin && enable && (state==ST_WDATA4)&& !hexvalid) state <= ST_IDLE;
        else if (validin && enable && (state==ST_WDATA5)&& !hexvalid) state <= ST_IDLE;
        else if (validin && enable && (state==ST_WDATA6)&& !hexvalid) state <= ST_IDLE;
        else if (validin && enable && (state==ST_WDATA7)&& !hexvalid) state <= ST_IDLE;
        else if (validin && enable && (state==ST_IDLE)&& (datain==CHRr)) state <= ST_RADDR0;
        else if (validin && enable && (state==ST_RADDR0)&& hexvalid) state <= ST_RADDR1;
        else if (validin && enable && (state==ST_RADDR1)&& hexvalid) state <= ST_IDLE;
        else if (validin && enable && (state==ST_RADDR0)) state <= ST_IDLE;
        else if (validin && enable && (state==ST_RADDR1)&& !hexvalid) state <= ST_IDLE;
        else if (validin && enable && (state==ST_RADDR2)&& !hexvalid) state <= ST_IDLE;
        else if (validin && enable && (state==ST_IDLE)) state <= ST_IDLE;

    end
end
assign echo_flag = validin && enable && ( 
      ((state==ST_IDLE)&& (datain==CHRw)) ? 1 : 
      ((state==ST_WADDR0)&& hexvalid) ? 1 : 
      ((state==ST_WADDR1)&& hexvalid) ? 1 : 
      ((state==ST_WDATA0)&& hexvalid) ? 1 : 
      ((state==ST_WDATA1)&& hexvalid) ? 1 : 
      ((state==ST_WDATA2)&& hexvalid) ? 1 : 
      ((state==ST_WDATA3)&& hexvalid) ? 1 : 
      ((state==ST_WDATA4)&& hexvalid) ? 1 : 
      ((state==ST_WDATA5)&& hexvalid) ? 1 : 
      ((state==ST_WDATA6)&& hexvalid) ? 1 : 
      ((state==ST_WDATA7)&& hexvalid) ? 1 : 
      ((state==ST_WADDR0)) ? 1 : 
      ((state==ST_WADDR1)&& !hexvalid) ? 1 : 
      ((state==ST_WDATA0)&& !hexvalid) ? 1 : 
      ((state==ST_WDATA1)&& !hexvalid) ? 1 : 
      ((state==ST_WDATA2)&& !hexvalid) ? 1 : 
      ((state==ST_WDATA3)&& !hexvalid) ? 1 : 
      ((state==ST_WDATA4)&& !hexvalid) ? 1 : 
      ((state==ST_WDATA5)&& !hexvalid) ? 1 : 
      ((state==ST_WDATA6)&& !hexvalid) ? 1 : 
      ((state==ST_WDATA7)&& !hexvalid) ? 1 : 
      ((state==ST_IDLE)&& (datain==CHRr)) ? 1 : 
      ((state==ST_RADDR0)&& hexvalid) ? 1 : 
      ((state==ST_RADDR1)&& hexvalid) ? 1 : 
      ((state==ST_RADDR0)) ? 1 : 
      ((state==ST_RADDR1)&& !hexvalid) ? 1 : 
      ((state==ST_RADDR2)&& !hexvalid) ? 1 : 
      ((state==ST_IDLE)) ? 1 : 
   0 );
assign clear_flag = validin && enable && ( 
      ((state==ST_IDLE)&& (datain==CHRw)) ? 1 : 
      ((state==ST_IDLE)) ? 1 : 
   0 );
assign pusha_flag = validin && enable && ( 
      ((state==ST_WADDR0)&& hexvalid) ? 1 : 
      ((state==ST_WADDR1)&& hexvalid) ? 1 : 
      ((state==ST_RADDR0)&& hexvalid) ? 1 : 
      ((state==ST_RADDR1)&& hexvalid) ? 1 : 
   0 );
assign pushd_flag = validin && enable && ( 
      ((state==ST_WDATA0)&& hexvalid) ? 1 : 
      ((state==ST_WDATA1)&& hexvalid) ? 1 : 
      ((state==ST_WDATA2)&& hexvalid) ? 1 : 
      ((state==ST_WDATA3)&& hexvalid) ? 1 : 
      ((state==ST_WDATA4)&& hexvalid) ? 1 : 
      ((state==ST_WDATA5)&& hexvalid) ? 1 : 
      ((state==ST_WDATA6)&& hexvalid) ? 1 : 
      ((state==ST_WDATA7)&& hexvalid) ? 1 : 
   0 );
assign write_flag = validin && enable && ( 
      ((state==ST_WDATA7)&& hexvalid) ? 1 : 
      ((state==ST_WADDR1)&& !hexvalid) ? 1 : 
      ((state==ST_WDATA0)&& !hexvalid) ? 1 : 
      ((state==ST_WDATA1)&& !hexvalid) ? 1 : 
      ((state==ST_WDATA2)&& !hexvalid) ? 1 : 
      ((state==ST_WDATA3)&& !hexvalid) ? 1 : 
      ((state==ST_WDATA4)&& !hexvalid) ? 1 : 
      ((state==ST_WDATA5)&& !hexvalid) ? 1 : 
      ((state==ST_WDATA6)&& !hexvalid) ? 1 : 
      ((state==ST_WDATA7)&& !hexvalid) ? 1 : 
   0 );
assign read_flag = validin && enable && ( 
      ((state==ST_RADDR1)&& hexvalid) ? 1 : 
      ((state==ST_RADDR1)&& !hexvalid) ? 1 : 
      ((state==ST_RADDR2)&& !hexvalid) ? 1 : 
   0 );
endmodule
