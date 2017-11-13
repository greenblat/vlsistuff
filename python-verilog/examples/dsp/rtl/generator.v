



module generator (
    input clk,input rst_n
    ,input [5:0] paddr
    ,input [1:0] psize
    ,input psel
    ,input pwrite
    ,input [31:0] pwdata
    ,output [31:0] prdata
    ,output reg [15:0] outmix
);

wire [15:0] enables;
wire work = enables[0];
wire [10:0] start0,start1,start2;
wire [10:0] jump0,jump1,jump2;

wire [15:0] sin0,sin1,sin2;
wire [15:0] gain0,gain1,gain2;
reg [10:0] addr0,addr1,addr2;
reg running;
wire start = work && !running;

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        addr0<=0;
        addr1<=0;
        addr2<=0;
        running <= 0;
    end else begin
        running <= work;
        if (start) begin
            addr0 <= start0;
            addr1 <= start1;
            addr2 <= start2;
        end else if (running) begin
            addr0 <= addr0 + jump0;
            addr1 <= addr1 + jump1;
            addr2 <= addr2 + jump2;
        end else begin
            addr0<=0;
            addr1<=0;
            addr2<=0;
        end
    end
end

sintab  sin0m(.addr(addr0),.out(sin0));
sintab  sin1m(.addr(addr1),.out(sin1));
sintab  sin2m(.addr(addr2),.out(sin2));

wire [31:0] total =  {{16{sin0[15]}},sin0}*{{16{gain0[15]}},gain0} 
                    +{{16{sin1[15]}},sin1}*{{16{gain1[15]}},gain1} 
                    +{{16{sin2[15]}},sin2}*{{16{gain2[15]}},gain2} 
                    ;
wire [15:0] outmix_wire = total[31:16];
reg [15:0] outmix2,offset;
always @(posedge clk) outmix <= outmix_wire;


regfile regfile (
     .clk(clk) ,.rst_n(rst_n)
    ,.paddr(paddr[5:0])
    ,.prdata(prdata[31:0])
    ,.psel(psel)
    ,.psize(psize[1:0])
    ,.pwdata(pwdata[31:0])
    ,.pwrite(pwrite)

    ,.enables(enables[15:0])
    ,.gain0(gain0[15:0])
    ,.gain1(gain1[15:0])
    ,.gain2(gain2[15:0])
    ,.jump0(jump0[10:0])
    ,.jump1(jump1[10:0])
    ,.jump2(jump2[10:0])
    ,.start0(start0[10:0])
    ,.start1(start1[10:0])
    ,.start2(start2[10:0])
);




endmodule

