
import string
import logs






AXIHEADER = '''
module MODULE (input clk, input rst_n
    ,input awvalid,output awready, input [31:0] awaddr
    ,input wvalid, output wready, input [31:0] wdata, input [3:0] wstrb
    ,output bvalid, output [1:0] bresp, input bready

    ,input arvalid, output arready, input [31:0] araddr
    ,output rvalid, input rready, output [31:0] rdata, output [1:0] rresp
'''



AXISTRING2 = '''
wire adfull,adempty,dafull,daempty;
wire arfull,arempty,drfull,drempty;
assign awready = !adfull;
assign wready = !dafull;
assign rvalid = !drempty;
assign rresp = 2'b0;
assign bresp = 2'b0;

wire i_pread;
wire [15:0] iwaddr,iraddr;
wire i_pwrite = !adempty && !daempty && !i_pread;
syncfifo #(16,2) adfifo(.clk(clk),.rst_n(rst_n)
    ,.validin(awvalid),.datain(awaddr[15:0])
    ,.readout(i_pwrite),.dataout(iwaddr[15:0])
    ,.full(adfull),.empty(adempty),.count(),.overflow(),.softreset(1'b0)
);
wire [31:0] pwdata,prdata;
wire [3:0] pstrb;
wire pread  = !arempty && !drfull;
syncfifo #(32+4,2) dafifo(.clk(clk),.rst_n(rst_n)
    ,.validin(wvalid),.datain({wdata,wstrb})
    ,.readout(i_pwrite),.dataout({pwdata,pstrb})
    ,.full(dafull),.empty(daempty),.count(),.overflow(),.softreset(1'b0)
);
reg was_i_pwrite;
assign bvalid = (i_pwrite || was_i_pwrite);
always @(posedge clk) begin
    if (!rst_n) begin
        was_i_pwrite <= 1'b0;
    end else begin
        if (i_pwrite && !bready) begin
            was_i_pwrite <= 1'b1;
        end else if (bready) begin
            was_i_pwrite <= 1'b0;
        end
    end
end
syncfifo #(16,2) arfifo(.clk(clk),.rst_n(rst_n)
    ,.validin(arvalid),.datain(araddr[15:0])
    ,.readout(i_pread),.dataout(iraddr[15:0])
    ,.full(arfull),.empty(arempty),.count(),.overflow(),.softreset(1'b0)
);
assign arready = !arfull;
reg was_i_pread; always @(posedge clk) was_i_pread <= i_pread;
syncfifo #(32,2) drfifo(.clk(clk),.rst_n(rst_n)
    ,.validin(was_i_pread),.datain(prdata)
    ,.readout(rready),.dataout(rdata)
    ,.full(drfull),.empty(drempty),.count(),.overflow(),.softreset(1'b0)
);

wire [15:0] paddr = i_pwrite ? iwaddr : iraddr;

// ------------------
'''
    




APBHead = ''' 
module MODULE (input clk, input rst_n,
    input psel, input pwrite, input [3:0] pstrb, input [15:0] paddr, input [31:0] pwdata, output [31:0] prdata
    ,output pready, output pslverr
'''
APBInst = ''' 
MODULE rgf (.clk(clk),.rst_n(rst_n),.pwrite(i_pwrite),.pread(i_pread),.paddr(paddr)
    ,.pwdata(pwdata),.prdata(prdata)
    ,.pstrb(pstrb)
'''




