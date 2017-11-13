module tb;
reg [31:0] cycles;   initial cycles=0;
reg [31:0] errors;   initial errors=0;
reg [31:0] wrongs;   initial wrongs=0;
reg [31:0] corrects; initial corrects=0;
reg [31:0] marker;   initial marker=0;
reg  clk;
wire [15:0] outmix;
reg [5:0] paddr;
wire [31:0] prdata;
reg  psel;
reg [1:0] psize;
reg [31:0] pwdata;
reg  pwrite;
reg penable;
reg  rst_n;
reg run_slowly;

always begin
    clk=0;
    #10;
    clk=1;
    #3;
    $python("negedge()");
    #7;
    wait(run_slowly==0);
end
initial begin
    $dumpvars(0,tb);
    run_slowly=0;
    paddr[5:0] = 0;
    penable=0;
    psel = 0;
    psize[1:0] = 0;
    pwdata[31:0] = 0;
    pwrite = 0;
    rst_n = 0;
    #100;
    rst_n=1;
end
generator generator (
     .clk(clk)
    ,.outmix(outmix[15:0])
    ,.paddr(paddr[5:0])
    ,.prdata(prdata[31:0])
    ,.psel(psel)
    ,.psize(psize[1:0])
    ,.pwdata(pwdata[31:0])
    ,.pwrite(pwrite)
    ,.rst_n(rst_n)
);

wire [15:0] firout;
fir fir (.clk(clk),.din(outmix),.dout(firout));



endmodule
