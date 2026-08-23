// APB arbiter: 2 masters -> 1 slave, round-robin.
//
// The slave-side SETUP/ACCESS phasing is generated entirely by this arbiter's
// own FSM, never by passing a master's PENABLE straight through. A master
// that is requesting but not yet granted advances its own SETUP->ACCESS
// transition unconditionally (it has no visibility into arbitration), so by
// the time it is finally granted its own PENABLE may already be high. If we
// muxed PENABLE directly, the slave would see PSEL and PENABLE both go high
// in the same cycle -- skipping SETUP entirely. Instead every grant always
// gets exactly one explicit PENABLE=0 cycle to the slave (S_SETUP) before
// PENABLE=1 (S_ACCESS), and the granted master is held at PREADY=0 until
// S_ACCESS so it can't mistake the forced SETUP cycle for a completion.
module apb_arbiter #(
    parameter ADDR_WIDTH = 32,
    parameter DATA_WIDTH = 32,
    parameter STRB_WIDTH = DATA_WIDTH/8
) (
    input  wire                    clk,
    input  wire                    rst_n,

    // ---------------- Master 0 (slave-side interface presented to master 0) ----------------
    input  wire                    m0_psel,
    input  wire                    m0_penable,
    input  wire                    m0_pwrite,
    input  wire [ADDR_WIDTH-1:0]   m0_paddr,
    input  wire [DATA_WIDTH-1:0]   m0_pwdata,
    input  wire [STRB_WIDTH-1:0]   m0_pstrb,
    output wire [DATA_WIDTH-1:0]   m0_prdata,
    output wire                    m0_pready,
    output wire                    m0_pslverr,

    // ---------------- Master 1 (slave-side interface presented to master 1) ----------------
    input  wire                    m1_psel,
    input  wire                    m1_penable,
    input  wire                    m1_pwrite,
    input  wire [ADDR_WIDTH-1:0]   m1_paddr,
    input  wire [DATA_WIDTH-1:0]   m1_pwdata,
    input  wire [STRB_WIDTH-1:0]   m1_pstrb,
    output wire [DATA_WIDTH-1:0]   m1_prdata,
    output wire                    m1_pready,
    output wire                    m1_pslverr,

    // ---------------- Slave port (master-side interface driven to the shared slave) --------
    output wire                    s_psel,
    output wire                    s_penable,
    output wire                    s_pwrite,
    output wire [ADDR_WIDTH-1:0]   s_paddr,
    output wire [DATA_WIDTH-1:0]   s_pwdata,
    output wire [STRB_WIDTH-1:0]   s_pstrb,
    input  wire [DATA_WIDTH-1:0]   s_prdata,
    input  wire                    s_pready,
    input  wire                    s_pslverr
);

    localparam S_IDLE   = 2'd0;
    localparam S_SETUP  = 2'd1;
    localparam S_ACCESS = 2'd2;

    reg [1:0] state;
    reg       grant;   // 0 = master 0 owns the bus, 1 = master 1 owns the bus

    wire req0 = m0_psel;
    wire req1 = m1_psel;

    // Round-robin pick: if both request, alternate off the master currently/just
    // holding `grant`; if only one requests, it wins outright.
    wire next_grant = (req0 && req1) ? ~grant : req0 ? 1'b0 : 1'b1;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            state <= S_IDLE;
            grant <= 1'b0;
        end else begin
            case (state)
                S_IDLE: begin
                    if (req0 || req1) begin
                        grant <= next_grant;
                        state <= S_SETUP;
                    end
                end

                S_SETUP: begin
                    // exactly one cycle, unconditionally
                    state <= S_ACCESS;
                end

                S_ACCESS: begin
                    if (s_pready) begin
                        if (req0 || req1) begin
                            grant <= next_grant;
                            state <= S_SETUP;
                        end else begin
                            state <= S_IDLE;
                        end
                    end
                end

                default: state <= S_IDLE;
            endcase
        end
    end

    // `grant` is stable for the entire SETUP+ACCESS of a transfer, so the
    // address/data mux can key off it directly.
    assign s_psel    = (state != S_IDLE);
    assign s_penable = (state == S_ACCESS);
    assign s_pwrite  = grant ? m1_pwrite : m0_pwrite;
    assign s_paddr   = grant ? m1_paddr  : m0_paddr;
    assign s_pwdata  = grant ? m1_pwdata : m0_pwdata;
    assign s_pstrb   = grant ? m1_pstrb  : m0_pstrb;

    // PREADY/PRDATA/PSLVERR only reach the granted master, and only once the
    // arbiter itself is actually in ACCESS (never during the forced SETUP
    // cycle, even if that master's own PENABLE was already high).
    wire in_access0 = (state == S_ACCESS) && (grant == 1'b0);
    wire in_access1 = (state == S_ACCESS) && (grant == 1'b1);

    assign m0_prdata  = s_prdata;
    assign m0_pready  = in_access0 ? s_pready  : 1'b0;
    assign m0_pslverr = in_access0 ? s_pslverr : 1'b0;

    assign m1_prdata  = s_prdata;
    assign m1_pready  = in_access1 ? s_pready  : 1'b0;
    assign m1_pslverr = in_access1 ? s_pslverr : 1'b0;

endmodule
