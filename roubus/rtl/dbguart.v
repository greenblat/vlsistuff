module dbguart (
     input clk
    ,input rst_n
    ,input rxd
    ,output txd

    ,output [13:0] ram_addr
    ,input [31:0]  ram_rdata
    ,output [31:0]  ram_wdata
    ,output ram_read
    ,output ram_write

);


parameter DOTS_CHAR = 58;
parameter CRLF = 10;
parameter DOT_CHAR = 8'h2e;
parameter EQ_CHAR = 8'h3d;
parameter GT_CHAR = 8'h3e;
parameter PLUS_CHAR = 8'h2b;
parameter QUESTION_CHAR = 8'h3f;

parameter D_CHAR = 8'h44;
parameter B_CHAR = 8'h42;
parameter G_CHAR = 8'h31;
parameter ZERO_CHAR = 8'h30;


reg write_tx;
wire rx_valid;
wire tx_empty;


wire [7:0] txdata,rxdata,status,control;
wire [15:0] baudrate;

uartx2 uartx2 (
   .clk(clk)
  ,.nreset(rst_n)
  ,.txd(txd)
  ,.rxd(rxd)

  ,.control(control[7:0])
  ,.write_tx(write_tx)
  ,.read_rx(rx_valid)
  ,.rxdata(rxdata[7:0])
  ,.txdata(txdata[7:0])
  ,.tx_empty(tx_empty)
  ,.status(status[7:0])
  ,.baudrate(baudrate[15:0])
  ,.rx_valid(rx_valid)
);

// rxfifo
reg [7:0] rxfifo [0:17];
wire [7:0] rxfifo0 = rxfifo[0];
wire [7:0] rxfifo1 = rxfifo[1];
wire [7:0] rxfifo2 = rxfifo[2];
wire [7:0] rxfifo3 = rxfifo[3];
reg command_pulse;
always @(posedge clk) begin
    command_pulse <= rx_valid;
    if (rx_valid) begin
        rxfifo[0]<=rxdata;
        rxfifo[1]<=rxfifo[0];
        rxfifo[2]<=rxfifo[1];
        rxfifo[3]<=rxfifo[2];
        rxfifo[4]<=rxfifo[3];
        rxfifo[5]<=rxfifo[4];
        rxfifo[6]<=rxfifo[5];
        rxfifo[7]<=rxfifo[6];
        rxfifo[8]<=rxfifo[7];
        rxfifo[9]<=rxfifo[8];
        rxfifo[10]<=rxfifo[9];
        rxfifo[11]<=rxfifo[10];
        rxfifo[12]<=rxfifo[11];
        rxfifo[13]<=rxfifo[12];
        rxfifo[14]<=rxfifo[13];
        rxfifo[15]<=rxfifo[14];
        rxfifo[16]<=rxfifo[15];
        rxfifo[17]<=rxfifo[16];
    end
end


wire question_valid = (rxfifo[1]==QUESTION_CHAR)&&(rxfifo[0]==DOT_CHAR) && command_pulse;
wire read_command_valid = (rxfifo[5]==DOTS_CHAR)&&(rxfifo[0]==DOT_CHAR) && command_pulse
    &&hexchar(rxfifo[1])
    &&hexchar(rxfifo[2])
    &&hexchar(rxfifo[3])
    &&hexchar(rxfifo[4])
    ;

wire long_read_command_valid = (rxfifo[7]==DOTS_CHAR)&&(rxfifo[0]==DOT_CHAR) && command_pulse
    &&hexchar(rxfifo[1])
    &&hexchar(rxfifo[2])
    &&hexchar(rxfifo[3])
    &&hexchar(rxfifo[4])
    &&hexchar(rxfifo[5])
    &&hexchar(rxfifo[6])
    ;



wire write_regs_command_valid = (rxfifo[13]==EQ_CHAR)&&(rxfifo[0]==DOT_CHAR) && command_pulse
    &&hexchar(rxfifo[1])
    &&hexchar(rxfifo[2])
    &&hexchar(rxfifo[3])
    &&hexchar(rxfifo[4])
    &&hexchar(rxfifo[5])
    &&hexchar(rxfifo[6])
    &&hexchar(rxfifo[7])
    &&hexchar(rxfifo[8])
    &&hexchar(rxfifo[9])
    &&hexchar(rxfifo[10])
    &&hexchar(rxfifo[11])
    &&hexchar(rxfifo[12])
    ;


wire write_mem_command_valid = (rxfifo[17]==GT_CHAR)&&(rxfifo[0]==DOT_CHAR) && command_pulse
    &&hexchar(rxfifo[1])
    &&hexchar(rxfifo[2])
    &&hexchar(rxfifo[3])
    &&hexchar(rxfifo[4])
    &&hexchar(rxfifo[5])
    &&hexchar(rxfifo[6])
    &&hexchar(rxfifo[7])
    &&hexchar(rxfifo[8])
    &&hexchar(rxfifo[9])
    &&hexchar(rxfifo[10])
    &&hexchar(rxfifo[11])
    &&hexchar(rxfifo[12])
    &&hexchar(rxfifo[13])
    &&hexchar(rxfifo[14])
    &&hexchar(rxfifo[15])
    &&hexchar(rxfifo[16])
    ;





wire [15:0] helper0 ={ hexval(rxfifo[7]),hexval(rxfifo[6]),hexval(rxfifo[5]),hexval(rxfifo[4])};
wire [15:0] read_addr ={ hexval(rxfifo[4]),hexval(rxfifo[3]),hexval(rxfifo[2]),hexval(rxfifo[1])};
wire [15:0] long_read_addr ={ hexval(rxfifo[6]),hexval(rxfifo[5]),hexval(rxfifo[4]),hexval(rxfifo[3])};
wire [7:0] long_count_read =  { hexval(rxfifo[2]),hexval(rxfifo[1])};
wire [15:0] regs_wr_addr = { hexval(rxfifo[12]),hexval(rxfifo[11]),hexval(rxfifo[10]),hexval(rxfifo[9])};
wire [15:0] mem_wr_addr = { hexval(rxfifo[16]),hexval(rxfifo[15]),hexval(rxfifo[14]),hexval(rxfifo[13])};
wire [31:0] pwdata = 
         { 
           hexval(rxfifo[8]),hexval(rxfifo[7]),hexval(rxfifo[6]),hexval(rxfifo[5])
           ,hexval(rxfifo[4]),hexval(rxfifo[3]),hexval(rxfifo[2]),hexval(rxfifo[1])
         };
assign ram_wdata = 
         { 
           hexval(rxfifo[8]),hexval(rxfifo[7]),hexval(rxfifo[6]),hexval(rxfifo[5])
           ,hexval(rxfifo[4]),hexval(rxfifo[3]),hexval(rxfifo[2]),hexval(rxfifo[1])
         };

wire [15:0] enables;
reg [11:0] keep_alive_count;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        keep_alive_count<=1;
    end else if (!enables[0]) begin
        keep_alive_count<=keep_alive_count+1;
    end else begin
        keep_alive_count<=1;
    end
end
wire keep_alive = keep_alive_count==0;


// tx fifo. loaded in one go.
reg [7:0] txfifo [0:17];
reg [4:0] txptr;
reg txactive;
reg add_crlf;
assign txdata = (!txactive && write_tx) ? rxfifo[0] : add_crlf ? CRLF : txfifo[txptr];
wire txstart_pread;

reg txactive0;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        txptr<=0;
        txactive<=0;
        txactive0<=0;
        write_tx<=0;
      add_crlf<=0;
    end else begin
        txactive <= txactive0;
        if (!txactive) begin
            write_tx<=command_pulse;
            if (txstart_pread) begin
                txptr<=0;
                txactive0<=1;
            end
        end else begin
            if (write_tx) begin
                write_tx<=0;
                txptr<=txptr+1;
                if (add_crlf) begin
                    add_crlf<=0;
                    txactive0<=0;
                end
            end else if ((txptr==18)||(txfifo[txptr]==0)) begin
                add_crlf<=1;
                txptr<=0;
            end else if (tx_empty) begin
                write_tx<=1;
            end  
        end
    end
end

wire [31:0] prdata;
wire penable=1;
wire psel,pwrite;
reg [15:0] paddr;

reg [3:0] reading_sm;
reg [3:0] long_reading_sm;
reg [3:0] writing_sm;
reg [7:0] long_count;
assign pwrite = (writing_sm==1);
assign ram_write = (writing_sm==3);
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        reading_sm<=0;        
        writing_sm<=0;        
        paddr<=0;
    end else begin
        if (write_regs_command_valid) begin
            paddr <= regs_wr_addr;
            writing_sm <= 1;
        end else if (writing_sm==1) begin
            writing_sm <= 0;
        end
        if (write_mem_command_valid) begin
            paddr <= mem_wr_addr;
            writing_sm <= 3;
         end else if (writing_sm==3) begin
            writing_sm <= 0;
         end

        if (long_read_command_valid) begin
            paddr <= long_read_addr;
            long_count <= long_count_read;
            long_reading_sm <=1;
        end else if (long_reading_sm==1) begin
            if (long_count==0) begin
                long_reading_sm<=0;
            end else if (reading_sm==0) begin
                reading_sm <=1;
                long_reading_sm <=2;
                long_count<= long_count-1;
            end
        end else if (long_reading_sm==2) begin
            if (reading_sm==0) begin
                long_reading_sm <=1;
                if (paddr[15])
                    paddr <= paddr+8;
                else
                    paddr <= paddr+4;
            end
        end

        if (read_command_valid) begin
            paddr <= read_addr;
            reading_sm <=1;
        end else if (reading_sm==1) begin
            if (paddr[15]==0)
                reading_sm<=2;
            else
                reading_sm<=4;
        end else if (reading_sm==2) begin
            reading_sm<=3;
        end else if (reading_sm==3) begin
            if (!txactive) begin
                reading_sm<=0;
            end
        end else if (reading_sm==4) begin
            reading_sm<=5;
        end else if (reading_sm==5) begin
            if (!txactive) begin
                reading_sm<=0;
            end
        end
    end
end

assign psel = ((reading_sm==1) && (paddr[15]==0))||(writing_sm==1);
assign txstart_pread = (!txactive) && 
    ((reading_sm==2)||(reading_sm==4)||keep_alive||question_valid);
assign ram_read = (reading_sm==1)&&(paddr[15]==1);
assign ram_addr = paddr[13:0];




always @(posedge clk) if (!txactive) begin
    if (reading_sm==2) begin
        txfifo[0]<=DOTS_CHAR;
        txfifo[1]<=xnibble(paddr[15:12]);
        txfifo[2]<=xnibble(paddr[11:8]);
        txfifo[3]<=xnibble(paddr[7:4]);
        txfifo[4]<=xnibble(paddr[3:0]);
        txfifo[5]<=xnibble(prdata[31:28]);
        txfifo[6]<=xnibble(prdata[27:24]);
        txfifo[7]<=xnibble(prdata[23:20]);
        txfifo[8]<=xnibble(prdata[19:16]);
        txfifo[9]<=xnibble(prdata[15:12]);
        txfifo[10]<=xnibble(prdata[11:8]);
        txfifo[11]<=xnibble(prdata[7:4]);
        txfifo[12]<=xnibble(prdata[3:0]);
        txfifo[13]<=DOT_CHAR;
        txfifo[14]<=0;
    end else if ((reading_sm==1)&&paddr[15]) begin
        txfifo[0]<=PLUS_CHAR;
        txfifo[1]<=xnibble(paddr[15:12]);
        txfifo[2]<=xnibble(paddr[11:8]);
        txfifo[3]<=xnibble(paddr[7:4]);
        txfifo[4]<=xnibble(paddr[3:0]);
        txfifo[5]<=xnibble(8'b0);
        txfifo[6]<=xnibble(8'b0);
        txfifo[7]<=xnibble(ram_rdata[39:36]);
        txfifo[8]<=xnibble(ram_rdata[35:32]);
        txfifo[9]<=xnibble(ram_rdata[31:28]);
        txfifo[10]<=xnibble(ram_rdata[27:24]);
        txfifo[11]<=xnibble(ram_rdata[23:20]);
        txfifo[12]<=xnibble(ram_rdata[19:16]);
        txfifo[13]<=xnibble(ram_rdata[15:12]);
        txfifo[14]<=xnibble(ram_rdata[11:8]);
        txfifo[15]<=xnibble(ram_rdata[7:4]);
        txfifo[16]<=xnibble(ram_rdata[3:0]);
        txfifo[17]<=DOT_CHAR;
    end else if (keep_alive||question_valid) begin
        txfifo[0]<=D_CHAR;
        txfifo[1]<=B_CHAR;
        txfifo[2]<=G_CHAR;
        txfifo[3]<=ZERO_CHAR;
        txfifo[4]<=xnibble(helper0[15:12]);
        txfifo[5]<=xnibble(helper0[11:8]);
        txfifo[6]<=xnibble(helper0[7:4]);
        txfifo[7]<=xnibble(helper0[3:0]);
        txfifo[8]<=0;
    end
end

function [7:0] xnibble (input [3:0] nib);
begin
    if (nib<10) xnibble = nib + 8'h30;
    else xnibble = nib - 10 + 8'h41;
end
endfunction

function [3:0] hexval (input [7:0] nib);
begin
    if ((nib>=8'h30)&&(nib<=8'h39)) 
        hexval = nib-8'h30;
    else if ((nib>=8'h41)&&(nib<=8'h46)) 
        hexval = nib-8'h41+10;
    else if ((nib>=8'h61)&&(nib<=8'h66)) 
        hexval = nib-8'h61+10;
    else 
        hexval=0;
end
endfunction

function hexchar(input [7:0] nib);
begin
    if ((nib>=8'h30)&&(nib<=8'h39)) 
        hexchar = 1'b1;
    else if ((nib>=8'h41)&&(nib<=8'h46)) 
        hexchar = 1'b1;
    else if ((nib>=8'h61)&&(nib<=8'h66)) 
        hexchar = 1'b1;
    else 
        hexchar=1'b0;
    
end
endfunction

wire prst_n = rst_n;
wire pclk = clk;

wire [7:0] nc8;
regfile regfile (
     .clk(clk) ,.rst_n(rst_n)
    ,.paddr(paddr[5:0])
    ,.prdata(prdata[31:0])
    ,.psel(psel)
    ,.psize(2'b11)
    ,.pwdata(pwdata[31:0])
    ,.pwrite(pwrite)

    ,.enables(enables[15:0])
    ,.baudrate(baudrate) ,.control({nc8,control}) ,.gain2()
    ,.jump0() ,.jump1() ,.jump2()
    ,.start0() ,.start1() ,.start2()
);






endmodule


