


module faultifizer #(parameter WID=8) ( 
    input [WID-1:0] inx, output [WID-1:0] outx
);

reg [WID-1:0] stuck0,stuck1;
initial stuck0 = {WID{1'b0}};
initial stuck1 =  {WID{1'b0}};
initial flip =  {WID{1'b0}};

integer kk;
always @(posedge tb.makeStuckList) begin
    if ((WID)<2) begin
        $display("register  %m.stuck0 1 1");
        $display("register  %m.stuck1 1 1");
        $display("register  %m.flip 1 1");
    end else begin
        for (kk=0;kk<WID;kk=kk+1) begin 
            $display("register  %m.stuck0 %d %d ",WID,kk);
            $display("register  %m.stuck1 %d %d ",WID,kk);
            $display("register  %m.flip %d %d ",WID,kk);
        end 
    end
end
assign outx = (~stuck0) & ((flip^inx)|stuck1);
endmodule

