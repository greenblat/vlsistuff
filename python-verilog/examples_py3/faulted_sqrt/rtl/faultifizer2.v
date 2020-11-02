


module faultifizer #(parameter WID=8) ( 
    input [WID-1:0] inx, output [WID-1:0] outx
);


reg [WID-1:0] stuck0,stuck1,flip;
reg [31:0] myindex; initial myindex=-1;

reg [15:0] ptr;
always @(tb.fault_index) 
    if ((tb.fault_index>=myindex)&&(tb.fault_index<(myindex+2*WID))) begin
        if (tb.fault_index[0])
            stuck1 =  ((1<<(tb.fault_index-myindex))>>1);
        else
            stuck0 =  ((1<<(tb.fault_index-myindex))>>1);
    end else begin
        stuck0 = 0;
        stuck1 = 0;
        flip = 0;
    end

reg [WID-1:0] stuck0,stuck1;
initial stuck0 = {WID{1'b0}};
initial stuck1 =  {WID{1'b0}};
initial flip =  {WID{1'b0}};

integer kk;
always @(posedge tb.makeStuckList) begin
    myindex = tb.fault_index;
    tb.fault_index  = tb.fault_index + 3*WID;
    if ((WID)<2) begin
        $display("register  %m.stuck0 1 1 %d",myindex);
        $display("register  %m.stuck1 1 1 %d",myindex+1);
        $display("register  %m.flip 1 1 %d",myindex+2);
    end else begin
        for (kk=0;kk<WID;kk=kk+1) begin 
            $display("register  %m.stuck0 %d %d %d ",WID,kk,myindex + 2*kk);
            $display("register  %m.stuck1 %d %d %d ",WID,kk,myindex + 2*kk+1);
            $display("register  %m.flip %d %d %d ",WID,kk,myindex + 2*kk+2);
        end 
    end
end
assign outx = (~stuck0) & ((flip^inx)|stuck1);
endmodule

