
// result = a**b;
// table based mplementation of A to the power of B, where A&B are floating point numbers.
// 10 bit wide input is used for both tables.




module fp_exponent(
    input clk, input rst_n
    ,input [31:0] ain, input [31:0] bin, input validin
    ,output reg [31:0] result, output validout
    ,output busy
);

reg [3:0] step;
reg [31:0] aa,bb,temp,aatag;
reg [31:0] temp2,temp3;

wire [31:0] addout;


reg invert_result;


wire [31:0] flt_exp;
wire [7:0] dbgx = aa[30:23];
wire [7:0] dbg1a = (dbgx>=127) ? (dbgx-127) : (127-dbgx);
wire [7:0] dbgy = aatag[30:23];
wire [7:0] dbg1b = (dbgy>=127) ? (dbgy-127) : (127-dbgy);
wire [7:0] dbg1 = invert_result ? dbg1b : dbg1a;
fp_int2float #(.WIDE(8)) int2float(.ain(dbg1),.bin(6'b0),.is_signed(1'b1),.out(flt_exp));


wire [31:0] mulout;
wire [31:0] logtabresult;
wire [31:0] exptabresult;
wire [31:0] smltabresult;
reg [7:0] count;
assign validout = step==5;
assign busy = step!=0;
wire [31:0] ONE = 32'h3f800000;

wire [31:0] overout;
wire [7:0] dbg2 = temp2[30:23];
always @(posedge clk) begin
    if (!rst_n) begin
        step <= 0;
        aa <=0;
        bb <=0;
        temp <=0;
        temp2 <=0;
        temp3 <=0;
        count <= 0;
        result <= 0;
        invert_result <= 0;
        aatag <= 0;
    end else begin
        if (validin && (step==0)) begin
            step <= 1;
            aa <= ain;
            bb <= bin;
            aatag <= overout;
            invert_result <= ain[30:23]<127;
        end else if (step==1) begin
            temp <= addout;
            step <= 2;
        end else if (step==2) begin
            temp2 <= mulout;
            step <= 3;
        end else if (step==3) begin
            if (dbg2>=127) begin
                count <= temp2[30:23]-127;
                temp3 <= exptabresult;
                step <= 4;
             end else begin
                step <= 10;
                temp3 <= smltabresult;
             end
        end else if ((step==4)&&(count==0)) begin
            result <= (bb==0) ? aa : (aa==0) ? ONE : invert_result ? overout : temp3;
            step <= 5;
        end else if (step==4) begin
            temp3 <= mulout;
            count <= count -1;
        end else if (step==5) begin
            step <= 0;
        end else if (step==10) begin
            result <= (bb==0) ? ONE : (aa==0) ? 0 : invert_result ? overout : temp3;
            step <= 5;
        end
    end
end


wire [9:0] logtabindex = invert_result ? (aatag[22:13]+aatag[12]) : (aa[22:13]+aa[12]);
logtab logtab (.index(logtabindex),.result(logtabresult));

wire [9:0] exptabindex = temp2[22:13]+temp2[12];
exptab exptab (.index(exptabindex),.result(exptabresult));


wire [31:0] mula = 
    (step==2) ? temp : temp3;
wire [31:0] mulb = 
     (step==2)  ? bb : temp3;
fp_multiplier fmul (.ain(mula),.bin(mulb),.out(mulout));
fp_adder fadd (.ain(logtabresult),.bin(flt_exp),.out(addout));

wire [31:0] smlindex;
wire [5:0] shiftsml = 10;
fp_float2int #(.WID(10)) float2int (.ain(temp2),.bin(shiftsml),.out(smlindex));
smalltab smalltab (.ain(smlindex[9:0]),.out(smltabresult));

wire [31:0] overin = (step==0) ? ain : temp3;
fp_over fp_over (.ain(overin),.out(overout));

endmodule


