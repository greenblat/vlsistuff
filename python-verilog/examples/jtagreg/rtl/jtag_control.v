
/*





*/



module jtag_control(
     input    jtck_clock
    ,input    jtdi_out
    ,output   jtdo_in
    ,input    jtms_out
    ,input    rst_n




    ,output reg mem_read
    ,output reg mem_write
    ,output reg [15:0] mem_addr
    ,output reg [31:0] mem_wr_data
    ,output reg [1:0] mem_wr_width
    ,input [31:0] mem_rd_data
    ,input mem_ready

);  



wire xir_tck;
wire  xdr_tck;





reg [7:0] ir;
reg [3:0] tap ;
reg [31:0] sr ;


reg [31:0] rddata;




parameter READ_ADDR                =    8'h41;
parameter READ_MEM_32B             =    8'h42;
parameter READ_MEM_INCR_ADDR       =    8'h43;
parameter WRITE_ADDR               =    8'h50;
parameter WRITE_MEM_16B            =    8'h60;
parameter WRITE_MEM_16B_INCRADDR   =    8'h61;
parameter WRITE_MEM_32B            =    8'h62;
parameter WRITE_MEM_32B_INCRADDR   =    8'h63;
parameter WRITE_MEM_8B             =    8'h64;
parameter WRITE_MEM_8B_INCRADDR    =    8'h65;


parameter RESET = 0;
parameter IDLE = 1;
parameter DR_SCAN = 2;
parameter IR_SCAN = 3;
parameter CAPTURE_DR = 4;
parameter SHIFT_DR = 5;
parameter EXIT1_DR = 6;
parameter PAUSE_DR = 7;
parameter EXIT2_DR = 8;
parameter UPDATE_DR = 9;

parameter CAPTURE_IR = 10;
parameter SHIFT_IR = 11;
parameter EXIT1_IR = 12;
parameter PAUSE_IR = 13;
parameter EXIT2_IR = 14;
parameter UPDATE_IR = 15;


reg [2:0] incr_addr;


wire do_incr = (ir==WRITE_MEM_8B_INCRADDR)||(ir==WRITE_MEM_16B_INCRADDR)||(ir==WRITE_MEM_32B_INCRADDR);

always @(posedge jtck_clock or negedge rst_n)  begin
    if(!rst_n) begin
        mem_write <= 0;
        mem_read <= 0;
        mem_wr_width <= 0;
        incr_addr<=0;
        rddata<=0;
    end else begin
        if (incr_addr) incr_addr<=0;
        if (xdr_tck) begin
            if ((ir==WRITE_MEM_8B)||(ir==WRITE_MEM_8B_INCRADDR)) begin
                mem_write <= 1;
                mem_wr_width <= 0;
            end else if ((ir==WRITE_MEM_16B)||(ir==WRITE_MEM_16B_INCRADDR)) begin
                mem_write <= 1;
                mem_wr_width <= 1;
            end else if ((ir==WRITE_MEM_32B)||(ir==WRITE_MEM_32B_INCRADDR)) begin
                mem_write <= 1;
                mem_wr_width <= 2;
            end
        end
        if (xir_tck) begin
            if (ir==READ_MEM_32B) begin
                mem_read <= 1;
            end
            if (ir==READ_MEM_INCR_ADDR) begin
                mem_read <= 1;
            end
        end
        if (mem_write && mem_ready) begin
            mem_write <= 0;
            mem_wr_width <= 0;
            if (do_incr) begin
                if (mem_wr_width==2) incr_addr<=4; 
                else if (mem_wr_width==1) incr_addr<=2; 
                else incr_addr<=1;
            end
        end else if (mem_read && mem_ready) begin
            mem_read <= 0;
            rddata <= mem_rd_data;
            if (ir==READ_MEM_INCR_ADDR) incr_addr<=4;
        end
    end
end

always @(posedge jtck_clock or negedge rst_n)  begin
     if(!rst_n) begin
         tap<=RESET;
     end else begin
         case(tap)
             RESET:
                 tap<=(jtms_out?RESET:IDLE);
             IDLE:
                 tap<=(jtms_out?DR_SCAN:IDLE);
             DR_SCAN:
                 tap<=(jtms_out?IR_SCAN:CAPTURE_DR);
             IR_SCAN:
                 tap<=(jtms_out?RESET:CAPTURE_IR);
             CAPTURE_DR:
                 tap<=(jtms_out?EXIT1_DR:SHIFT_DR);
             SHIFT_DR:
                 tap<=(jtms_out?EXIT1_DR:SHIFT_DR);
             EXIT1_DR:
                 tap<=(jtms_out?UPDATE_DR:PAUSE_DR);
             PAUSE_DR:
                 tap<=(jtms_out?EXIT2_DR:PAUSE_DR);
             EXIT2_DR:
                 tap<=(jtms_out?UPDATE_DR:SHIFT_DR);
             UPDATE_DR:
                 tap<=(jtms_out?DR_SCAN:IDLE);
             CAPTURE_IR:
                 tap<=(jtms_out?EXIT1_IR:SHIFT_IR);
             SHIFT_IR:
                 tap<=(jtms_out?EXIT1_IR:SHIFT_IR);
             EXIT1_IR:
                 tap<=(jtms_out?UPDATE_IR:PAUSE_IR);
             PAUSE_IR:
                 tap<=(jtms_out?EXIT2_IR:PAUSE_IR);
             EXIT2_IR:
                 tap<=(jtms_out?UPDATE_IR:SHIFT_IR);
             UPDATE_IR:
                 tap<=(jtms_out?DR_SCAN:IDLE);
         endcase
     end
end



always @(posedge jtck_clock or negedge rst_n) begin
    if(!rst_n) begin
        ir<=8'b00000010;
        sr[31:0]<=0;
    end else begin
        case(tap)
            RESET:
                ir<=8'b00000010;
            CAPTURE_IR:
                sr[7:0]<=ir[7:0];
            SHIFT_IR:begin
                sr[31:0]<={jtdi_out,sr[31:1]};
            end
            EXIT1_IR,EXIT2_IR:
                if(jtms_out) ir[7:0]<=sr[31:24];
            UPDATE_IR : begin
            end
            CAPTURE_DR:
                case(ir[7:0])
                    8'h00,8'h20:  sr[7:0]<=8'h6a; 
                    READ_MEM_INCR_ADDR,READ_MEM_32B:  begin
                        sr[31:0] <=  rddata;
                    end
                    READ_ADDR:          sr[31:0] <=  {mem_addr,mem_addr};
                    8'hff: sr[0]<=jtdi_out; // full bypass
                endcase
            SHIFT_DR:begin
                   sr[31:0]<={jtdi_out,sr[31:1]};
            end
        endcase
    end
end            


always @(posedge jtck_clock or negedge rst_n) begin
     if(!rst_n) begin
         mem_addr<=0;
         mem_wr_data<=0;
     end else begin
         if (incr_addr) mem_addr <= mem_addr +incr_addr;
         if (xdr_tck) begin
             case (ir)
                  WRITE_MEM_8B_INCRADDR,WRITE_MEM_8B :  mem_wr_data <= {sr[31:24],sr[31:24],sr[31:24],sr[31:24]};
                  WRITE_MEM_16B_INCRADDR,WRITE_MEM_16B :  mem_wr_data <= {sr[31:16],sr[31:16]};
                  WRITE_MEM_32B_INCRADDR,WRITE_MEM_32B :  mem_wr_data <= sr[31:0];
                  WRITE_ADDR :  mem_addr <= sr[31:16];
            endcase
         end 
     end 
end    








neg_jtag_tiny neg_jtag_tiny(
    .jtck_clock(jtck_clock),
    .rst_n(rst_n),
    .tap(tap),
    .tdo(jtdo_in),
    .xir_tck(xir_tck),
    .xdr_tck(xdr_tck),
    .sr0(sr[0])
);

endmodule


module neg_jtag_tiny(
    input jtck_clock,
    input rst_n,
    output reg tdo,
    output reg xir_tck,
    output reg xdr_tck,
    input sr0,
    input [3:0] tap

) /* synthesis syn_scan_enable=0 */ ;

parameter UPDATE_DR = 9;
parameter UPDATE_IR = 15;
    always @(negedge jtck_clock or negedge rst_n) 
         if(!rst_n) begin
             tdo<=0;
             xir_tck<=0;
             xdr_tck<=0;
         end else begin
             tdo<=sr0;
             xir_tck<=0;
             xdr_tck<=0;
             case(tap)
                 UPDATE_IR:
                     xir_tck<=1;
                 UPDATE_DR:
                     xdr_tck<=1;
             endcase
         end
endmodule



