

module uartx2frac(
    input rxd,
    output txd,
    output [7:0] status,
    input [7:0] txdata,
    output [7:0] rxdata,
    output rx_valid,
    output tx_empty,
    input read_rx,
    input write_tx,
    input clk,
    input rst_n,
    input [7:0] control,
    input [15:0] baudrate,
    input [7:0] fractional
);

//control bits
/*control register
    control[1:0]  = 00 uart eight bits
                    01 ninth bit is odd parity 
                    10 ninth bit is even parity 
                    11 ninth bit is coming from control[7]  
    control[2] = ninth bit value received
    control[3] = discard bad characters
    control[4] = enable the RX part of the uart 
    control[5] = hunt for ninth_bit equal to control[2]
    control[6] = enable the TX part of the uart
    control[7] = ninth bit to transmit
*/

/* status register
    status[0]     = rx queue has data
    status[1]     = tx queue has place available
    status[2]     = current entry in rx queue had noise error
    status[3]     = current entry in rx queue had framing error
    status[4]     = current entry in rx queue had parity error
    status[5]     = current entry in rx queue was overrun 
    status[6]     = current entry in rx queue bit nine  
*/

    
wire control_eight_bits = !control[0] && !control[1]; 
wire control_nine_bits =  !control_eight_bits; 
wire control_parity_even =  !control[0] && control[1]; 
wire control_parity_odd =  control[0] && !control[1]; 
wire control_ninth_data =  control[0] && control[1]; 

// status bits
reg rx_bufa_valid;
reg rx_bufb_valid;
reg tx_bufa_valid;
reg [4:0] rxstatusb;

assign status[0] =  rx_bufb_valid;
assign status[1] =  !tx_bufa_valid;
assign status[2] =  rxstatusb[0];
assign status[3] =  rxstatusb[1];
assign status[4] =  rxstatusb[2];
assign status[5] =  rxstatusb[3];
assign status[6] =  rxstatusb[4];
assign status[7] = 1'b0;

wire txfixer;
wire [15:0] effectivetxbaudrate = baudrate + txfixer;

// rxd sync
reg rxd1,rxd_raw;
always @(posedge clk or negedge rst_n) begin
    rxd1 <= rxd;
    rxd_raw <= rxd1;
end

wire [15:0] bit_place = 8'b1 + {1'b0,baudrate[15:1]};
reg last_rxd;
reg rxd_filt;
reg was_bit_noise;
reg [15:0] rxinbit;
reg rx_active;
reg [10:0] rxsr;
reg rx_noise;
reg rx_overrun;
wire rx_framing_error;
wire rxnewdata = (rxsr[0]==1'b0)&&rx_active;
wire rx_midbit = (rxinbit==bit_place) && rx_active;
wire rx_midbit1 = (rxinbit==(bit_place+1)) && rx_active;
wire rx_shift = rx_active && rx_midbit1;

wire  is_one = last_rxd && rxd_raw;
wire  is_zero = !last_rxd && !rxd_raw;
wire  is_noise = !is_one && !is_zero;
wire negedge_rxd = control[4] && !rx_active && is_zero && !rx_framing_error;

always @(posedge clk  or negedge rst_n) begin
    if (!rst_n) begin
        rxd_filt <= 1'b1;
        last_rxd <= 1;
        was_bit_noise <= 1'b0;
    end else begin
        last_rxd <=  rxd_raw;
        if (rx_midbit) begin
            rxd_filt <= (is_one) ? 1'b1 : (is_zero ? 1'b0 : rxd_filt); 
            was_bit_noise <= is_noise;
        end
    end
end



always @(posedge clk  or negedge rst_n) begin
    if (!rst_n) begin
        rx_overrun <= 1'b0;
    end else begin
        if (rxnewdata && rx_bufa_valid) 
            rx_overrun <= 1'b1;
        else if (rxnewdata && !rx_bufa_valid) 
            rx_overrun <= 1'b0;
    end
end

wire rffixer;
wire [15:0] effectiverxbaudrate = baudrate + rxfixer;
reg [8:0] rxaddition;
assign rxfixer = rxaddition[8];

always @(posedge clk  or negedge rst_n) begin
    if (!rst_n) begin
        rxinbit <= 15'b0;
        rx_active <= 1'b0;
        rxaddition <= 0;
    end else begin
        rxaddition <= 
            negedge_rxd ? 0 : 
            !rx_active ? 0 :
            (rxinbit<effectiverxbaudrate) ?  rxaddition :
            (0 + rxaddition[7:0]  + fractional);


        rxinbit <= 
            negedge_rxd ? 0 :
            !rx_active ? 0 :
            (rxinbit<effectiverxbaudrate) ?  (rxinbit+1) : 0 ;

        if (negedge_rxd) 
            rx_active <= 1;
        else if (rxnewdata) 
            rx_active <= 0;
    end
end

reg first;

always @(posedge clk  or negedge rst_n) begin
    if (!rst_n) begin
        rxsr <= 11'b11111111111;
        rx_noise <= 1'b0;
        first <= 1'b1;
    end else begin
        if (negedge_rxd)  begin
            rxsr <= 11'b11111111111;
            rx_noise <= 1'b0;
            first <= 1'b1;
        end else if (rxnewdata) begin
            rxsr <= 11'b11111111111;
            first <= 1'b1;
        end else if (rx_shift) begin
            rxsr <= {(first ? 1'b0 : rxd_filt),(control_eight_bits?rxd_filt:rxsr[10]),rxsr[9:1]}; 
            rx_noise <= rx_noise | was_bit_noise || (first && rxd_filt);
            first <= 1'b0;
        end
    end
end

reg [8:0] rx_bufa;
reg [7:0] rx_bufb;
assign rxdata = rx_bufb;
reg [2:0] rxstatusa;
wire rx_xor = ^rx_bufa;
assign rx_framing_error = control_eight_bits ? !rxsr[9] : !rxsr[10];
wire compute_rx_parity_error = 
      (!rx_xor && control_parity_odd)
    ||(rx_xor && control_parity_even)
    ||(rx_bufa[8] && control_ninth_data);


wire rx_parity_error = 
    (compute_rx_parity_error&&(control_parity_odd||control_parity_even));

wire byte_is_acceptable = 
      (!control[3])  // we pass errors
    ||(!(rx_parity_error)&& !rxstatusb[2] && !rxstatusa[1] &&!rxstatusa[0]);

// this byte is ok by address filter,we check control[2] is equal to the ninth bit
wire filtered_ok_byte = 
    (!control[5]) || (control[1:0]!=2'b11) ||(rx_bufa[8]==control[2]);
always @(posedge clk  or negedge rst_n) begin
    if (!rst_n) begin
        rx_bufa <= 9'b0;
        rx_bufb <= 8'b0;
        rx_bufa_valid <= 1'b0;
        rx_bufb_valid <= 1'b0;
        rxstatusa <= 3'b0;
        rxstatusb <= 5'b0;
    end else begin
        if (rx_bufa_valid && !rx_bufb_valid) begin
            rx_bufb <= rx_bufa[7:0];
            rxstatusb <= {rx_bufa[8],rxstatusa[2],rx_parity_error,rxstatusa[1:0]};
            rx_bufb_valid <= filtered_ok_byte && byte_is_acceptable;
            // synthesis translate_off
//            if (!(filtered_ok_byte && byte_is_acceptable)) $display(">>byte rejected %b ",rx_bufa,$stime,"  %b",rxstatusa,rx_parity_error);
            // synthesis translate_on
            rx_bufa_valid <= 1'b0;
        end
        if (read_rx) 
            rx_bufb_valid <= 1'b0;

        if (rxnewdata) begin
            rx_bufa <= rxsr[9:1];
            rxstatusa <= {rx_overrun,rx_framing_error,rx_noise};
            rx_bufa_valid <= 1'b1;
        end
    end
end
assign rx_valid = rx_bufb_valid;


// transmitter
reg [7:0] tx_bufa;
reg [8:0] tx_bufb;
reg tx_bufb_valid;
reg tx_active;
reg [15:0] txinbit;
wire tx_start = tx_bufb_valid && !tx_active && (txinbit==1);
wire tx_shift = tx_active && (txinbit==1);
wire txbit_nine = 
    control_eight_bits 
    || (control_parity_even && (^tx_bufa))
    || (control_parity_odd && !(^tx_bufa))
    || (control_ninth_data && control[7])
    ;

always @(posedge clk  or negedge rst_n) begin
    if (!rst_n) begin
        tx_bufa <= 8'b0;
        tx_bufa_valid <= 1'b0;
        tx_bufb <= 8'b0;
        tx_bufb_valid <= 1'b0;
    end else begin
        if (write_tx && !tx_bufa_valid) begin
            tx_bufa_valid <= 1'b1;
            tx_bufa <= txdata;
        end
        if (!tx_bufb_valid && tx_bufa_valid) begin
            tx_bufa_valid <= 1'b0;
            tx_bufb_valid <= 1'b1;
            tx_bufb <= {txbit_nine,tx_bufa};
        end
        if (tx_start) begin
            tx_bufb_valid <= 1'b0;
        end
    end
end

reg [8:0] txaddition;
assign txfixer = txaddition[8];
always @(posedge clk  or negedge rst_n) begin
    if (!rst_n) begin
        txinbit <= 16'b0;
        txaddition <= 0;
    end else begin
        if (txinbit<effectivetxbaudrate) begin
            txinbit <= txinbit +1;
        end else begin
            txinbit<=0;
            txaddition <= 0 + txaddition[7:0]  + fractional;
        end
    end
end


reg [10:0] txsr;
always @(posedge clk  or negedge rst_n) begin
    if (!rst_n) begin
        txsr <= 11'h7ff;
    end else begin
        if (tx_start)
            txsr <= {control_nine_bits,tx_bufb,1'b0};
        else if (tx_shift)
            txsr <= {1'b0,txsr[10:1]};
        else if (!tx_active)
            txsr <= 11'h7ff;
    end
end
assign txd = txsr[0] || (txsr==0);
assign tx_empty =  control[6] && !tx_bufa_valid;

always @(posedge clk or negedge rst_n ) begin
    if (!rst_n) begin
        tx_active <= 1'b0;
    end else begin
        if (tx_start)
            tx_active <= 1'b1;
        else if (txsr==11'b0)
            tx_active <= 1'b0;
    end
end

endmodule



