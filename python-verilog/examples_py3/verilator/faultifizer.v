


module faultifizer #(parameter WID=8) ( 
    input [WID-1:0] inx, output [WID-1:0] outx
);

reg [31:0] base;

initial begin
   base = tb.BASE;
   tb.BASE = tb.BASE + 2*WID;
end

wire [WID-1:0] stuck0,stuck1;
genvar II;
generate begin
    for (II=0;II<WID;II=II+1) begin
        assign stuck0[2*II]   =   (tb.STUCK == base+(2*II)); 
        assign stuck1[2*II+1] =   (tb.STUCK == base+(2*II+1));
    end
end

integer kk;
always @(posedge tb.makeStuckList) begin
    if ((WID)<2) begin
        $display("register  %m.stuck0 1 1 %d",base);
        $display("register  %m.stuck1 1 1 %d",base+1);
    end else begin
        for (kk=0;kk<WID;kk=kk+1) begin 
            $display("register  %m.stuck0 %d %d %d ",WID,kk,base+(kk*2));
            $display("register  %m.stuck1 %d %d %d ",WID,kk,base+(kk*2)+1);
        end 
    end
end
assign outx = (~stuck0) & (inx|stuck1);
endmodule

