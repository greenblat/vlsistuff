
module jtag_tap (
     input    jtck_clock
    ,input    jtdi_out
    ,output   jtdo_in
    ,input    jtms_out
    ,input    por_n


    ,output reg ram_read
    ,output reg ram_write
    ,output reg [15:0] ram_addr
    ,output reg [31:0] ram_wr_data
    ,input [31:0] ram_rd_data
    ,input ram_ready
    ,input [7:0] version
    ,output reg [31:0] control
    ,input [31:0] status

);


wire xir_tck;
wire  xdr_tck;

reg [7:0] ireg;
reg [3:0] tap ;
reg [31:0] sreg ;



parameter READ_ADDR                =    8'h41;
parameter READ_MEM_32B             =    8'h42;
parameter READ_MEM_INCR_ADDR       =    8'h43;
parameter WRITE_ADDR               =    8'h44;
parameter WRITE_MEM_32B            =    8'h45;
parameter WRITE_MEM_32B_INCRADDR   =    8'h46;
parameter WRITE_CONTROL            =    8'h47;
parameter READ_STATUS              =    8'h48;


parameter RESET      = 4'd0;
parameter IDLE       = 4'd1;
parameter DR_SCAN    = 4'd2;
parameter IR_SCAN    = 4'd3;
parameter CAPTURE_DR = 4'd4;
parameter SHIFT_DR   = 4'd5;
parameter EXIT1_DR   = 4'd6;
parameter PAUSE_DR   = 4'd7;
parameter EXIT2_DR   = 4'd8;
parameter UPDATE_DR  = 4'd9;

parameter CAPTURE_IR = 4'd10;
parameter SHIFT_IR   = 4'd11;
parameter EXIT1_IR   = 4'd12;
parameter PAUSE_IR   = 4'd13;
parameter EXIT2_IR   = 4'd14;
parameter UPDATE_IR  = 4'd15;


reg [2:0] incr_addr;


wire do_incr = (ireg == WRITE_MEM_32B_INCRADDR);

always @(posedge jtck_clock or negedge por_n)  begin
    if(!por_n) begin
        ram_write <= 1'b0;
        ram_read <= 1'b0;
        incr_addr <= 3'b0;
    end else begin
        if (!ram_write) begin
            if (xdr_tck &&((ireg ==WRITE_MEM_32B)||(ireg ==WRITE_MEM_32B_INCRADDR))) begin
                ram_write <= 1'b1;
            end
        end else if (ram_ready) begin
            ram_write <= 1'b0;
        end
        if (ram_read) begin
            if (ram_ready) begin
                ram_read <= 1'b0;
            end
        end else begin
            if (xir_tck) begin
                if ((ireg ==READ_MEM_32B)||(ireg ==READ_MEM_INCR_ADDR)) begin
                    ram_read <= 1'b1;
                end
            end
        end

        if (ram_write && ram_ready) begin
            if (do_incr) begin
                incr_addr <= 3'd4;
            end
        end else if (ram_read && ram_ready) begin
            if (ireg ==READ_MEM_INCR_ADDR) incr_addr <= 3'd4;
        end else incr_addr <= 3'b0;
    end
end

always @(posedge jtck_clock or negedge por_n)  begin
     if(!por_n) begin
         tap <= RESET;
     end else begin
         case(tap)
             RESET:
                 tap <= (jtms_out?RESET:IDLE);
             IDLE:
                 tap <= (jtms_out?DR_SCAN:IDLE);
             DR_SCAN:
                 tap <= (jtms_out?IR_SCAN:CAPTURE_DR);
             IR_SCAN:
                 tap <= (jtms_out?RESET:CAPTURE_IR);
             CAPTURE_DR:
                 tap <= (jtms_out?EXIT1_DR:SHIFT_DR);
             SHIFT_DR:
                 tap <= (jtms_out?EXIT1_DR:SHIFT_DR);
             EXIT1_DR:
                 tap <= (jtms_out?UPDATE_DR:PAUSE_DR);
             PAUSE_DR:
                 tap <= (jtms_out?EXIT2_DR:PAUSE_DR);
             EXIT2_DR:
                 tap <= (jtms_out?UPDATE_DR:SHIFT_DR);
             UPDATE_DR:
                 tap <= (jtms_out?DR_SCAN:IDLE);
             CAPTURE_IR:
                 tap <= (jtms_out?EXIT1_IR:SHIFT_IR);
             SHIFT_IR:
                 tap <= (jtms_out?EXIT1_IR:SHIFT_IR);
             EXIT1_IR:
                 tap <= (jtms_out?UPDATE_IR:PAUSE_IR);
             PAUSE_IR:
                 tap <= (jtms_out?EXIT2_IR:PAUSE_IR);
             EXIT2_IR:
                 tap <= (jtms_out?UPDATE_IR:SHIFT_IR);
             UPDATE_IR:
                 tap <= (jtms_out?DR_SCAN:IDLE);
         endcase
     end
end



always @(posedge jtck_clock or negedge por_n) begin
    if(!por_n) begin
        ireg <= 8'b00000010;
        sreg <= 0;
    end else begin
        case(tap)
            RESET:
                ireg <= 8'b00000010;
            CAPTURE_IR:
                sreg[7:0] <= ireg[7:0];
            SHIFT_IR:begin
                sreg[31:0] <= {jtdi_out,sreg[31:1]};
            end
            EXIT1_IR,EXIT2_IR:
                if(jtms_out) ireg[7:0] <= sreg[31:24];
            UPDATE_IR : begin
            end
            CAPTURE_DR:
                case(ireg[7:0])
                    8'h00,8'h20:  sreg[7:0] <= version;
                    READ_MEM_INCR_ADDR,READ_MEM_32B:  begin
                        sreg[31:0] <=  ram_rd_data;
                    end
                    READ_STATUS:
                        sreg[31:0] <=  status;
                    READ_ADDR:          sreg[31:0] <=  {ram_addr,ram_addr};
              //      8'hff: sreg[0] <= jtdi_out; // full bypass
		    8'hff: sreg[0] <= 0;
		  
                endcase
            SHIFT_DR:begin
	            if (ireg[7:0] == 8'hff)begin
		            sreg[0] <= jtdi_out;
	            end else
                 sreg[31:0] <= {jtdi_out,sreg[31:1]};//was only in shifr dr
            end
        endcase
    end
end


always @(posedge jtck_clock or negedge por_n) begin
     if(!por_n) begin
         ram_addr <= 16'b0;
         ram_wr_data <= 32'b0;
         control <= 32'b0;
     end else begin
         if (xdr_tck) begin
            $display("IREG %x %x",ireg,sreg);
             case (ireg)
                  WRITE_MEM_32B_INCRADDR,WRITE_MEM_32B :  ram_wr_data <= sreg[31:0];
                  WRITE_ADDR :  ram_addr <= sreg[31:16];
                  WRITE_CONTROL :  control <= sreg[31:16];
            endcase
        end else begin
            ram_addr <= ram_addr + incr_addr;
        end
     end
end




jtag_neg_module jtag_neg_module (
    .jtck_clock(jtck_clock),
    .por_n(por_n),
    .tap(tap),
    .tdo(jtdo_in),
    .xir_tck(xir_tck),
    .xdr_tck(xdr_tck),
    .sr0(sreg[0])
);

endmodule

module jtag_neg_module(
    input jtck_clock,
    input por_n,
    output reg tdo,
    output reg xir_tck,
    output reg xdr_tck,
    input sr0,
    input [3:0] tap

);

parameter UPDATE_DR = 9;
parameter UPDATE_IR = 15;
    always @(negedge jtck_clock or negedge por_n)
         if(!por_n) begin
             tdo <= 1'b0;
             xir_tck <= 1'b0;
             xdr_tck <= 1'b0;
         end else begin
             tdo <= sr0;
             case(tap)
                 UPDATE_IR:
                     xir_tck <= 1'b1;
                 UPDATE_DR:
                     xdr_tck <= 1'b1;
                 default : begin
                     xir_tck <= 1'b0;
                     xdr_tck <= 1'b0;
                 end
             endcase
         end
endmodule

