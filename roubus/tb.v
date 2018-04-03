

module tb;

reg [31:0] cycles;   initial cycles=0;
reg [31:0] errors;   initial errors=0;
reg [31:0] wrongs;   initial wrongs=0;
reg [31:0] panics;   initial panics=0;
reg [31:0] corrects; initial corrects=0;
reg [31:0] marker;   initial marker=0;


reg [15:0] idindex;

reg [255:0] paths [0:127];
initial idindex=0;

wire [7:0] resp_count;
wire [63:0] resp_data;
reg resp_read; initial resp_read=0;

reg [169:0] admin_msg_in; initial admin_msg_in = 0;
wire admin_msg_in_ack;

reg clk;
reg rst_n;

initial begin
    $dumpvars(0,tb);
    rst_n=0;
    #100;
    rst_n=1;
end
always begin
    clk=0;
    #5;
    clk=1;
    #5;
    $python("negedge()");
end
noc0 noc0 (.clk(clk),.rst_n(rst_n)
   ,.admin_msg_in(admin_msg_in)
   ,.admin_msg_in_ack(admin_msg_in_ack)
   ,.resp_count(resp_count)
   ,.resp_data(resp_data)
   ,.resp_read(resp_read)
);





endmodule

