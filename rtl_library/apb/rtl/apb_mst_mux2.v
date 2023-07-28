
module apb_mst_mux2 (
     input clk, input rst_n

// master side
    ,output [31:0] m_paddr
    ,output [31:0] m_pwdata
    ,output        m_psel
    ,output        m_penable
    ,output        m_pwrite
    ,output [3:0]  m_pstrb
    ,input         m_pready
    ,input         m_pslverr
    ,input [31:0]  m_prdata


// slave 1 and 2  side
    ,input [31:0]  s1_paddr
    ,input [31:0]  s1_pwdata
    ,input         s1_psel
    ,input         s1_penable
    ,input         s1_pwrite
    ,input [3:0]   s1_pstrb
    ,output        s1_pready
    ,output        s1_pslverr
    ,output [31:0] s1_prdata

    ,input [31:0]  s2_paddr
    ,input [31:0]  s2_pwdata
    ,input         s2_psel
    ,input         s2_penable
    ,input         s2_pwrite
    ,input [3:0]   s2_pstrb
    ,output        s2_pready
    ,output        s2_pslverr
    ,output [31:0] s2_prdata

);

reg work1,work2;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        work1 <= 0;
        work2 <= 0;
    end else begin
        if (!work1 && !work2) begin
            if (s1_psel) begin
                work1 <= 1;
            end else if (s2_psel) begin
                work2 <= 1;
            end
       end else if (work1) begin
            if (s1_pready) begin
                work1 <= 0;
            end
       end else if (work2) begin
            if (s2_pready) begin
                work2 <= 0;
            end
       end
    end
end

wire do1 = (!work1 && !work2) ? s1_psel : work1;
wire do2 = (!work1 && !work2) ? s2_psel : work2;
assign m_psel = s1_psel || s2_psel;
assign m_penable = (do1 && s1_penable )  || (do2 && s2_penable);
assign m_pwdata = do1  ? s1_pwdata : do2 ? s2_pwdata : 0;
assign m_pstrb = do1  ? s1_pstrb : do2 ? s2_pstrb : 0;
assign m_pwrite = do1  ? s1_pwrite : do2 ? s2_pwrite : 0;
assign m_paddr = do1  ? s1_paddr : do2 ? s2_paddr : 0;


assign s1_prdata  = do1 ? m_prdata : 0;
assign s2_prdata  = do2 ? m_prdata : 0;
assign s1_pslverr  = do1 ? m_pslverr : 0;
assign s2_pslverr  = do2 ? m_pslverr : 0;
assign s1_pready =  work1 || !s2_psel;
assign s2_pready =  work2 || !s1_psel;


endmodule


