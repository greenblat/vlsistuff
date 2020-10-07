#! /usr/bin/env python3
import os,sys,string

HEADER = '''
module axi4light_switch(
     input  clk
    ,input  rst_n
'''

INTERFACE = '''
    ,IN [31:0]  PREF_araddr
    ,IN [2:0]   PREF_arprot
    ,OUT        PREF_arready
    ,IN         PREF_arvalid

    ,IN [31:0]  PREF_awaddr
    ,IN [2:0]   PREF_awprot
    ,OUT        PREF_awready
    ,IN         PREF_awvalid

    ,IN         PREF_bready
    ,OUT [1:0]  PREF_bresp
    ,OUT        PREF_bvalid

    ,OUT [31:0] PREF_rdata
    ,IN         PREF_rready
    ,OUT [1:0]  PREF_rresp
    ,OUT        PREF_rvalid

    ,IN [31:0]  PREF_wdata
    ,OUT        PREF_wready
    ,IN [3:0]   PREF_wstrb
    ,IN         PREF_wvalid
'''

WARBITER = '''


wire awempty,wdempty,awfull,wdfull;

assign IN_awready = !awfull;
assign IN_wready = !wdfull;
wire writing = !awempty && !wdempty;
wire [OUTS-1:0] wmatch;
wire wused = (wstate==5);
wire [31:0] awaddr;
wire bready = IN_bready;
wire [OUTS-1:0] wready,awready;

syncfifo #(.WID(32),.DEPTH(8)) waddrfifo (.clk(clk),.rst_n(rst_n),.validin(IN_awvalid),.datain(IN_awaddr)
    ,.softreset(1'b0),.full(awfull)
    ,.readout(wused),.dataout(awaddr),.empty(awempty)
    ,.count(),.overflow()
);

reg [2:0] wstate;
wire [31:0] wdata;
wire [3:0] wstrb;
syncfifo #(.WID(32+4),.DEPTH(8)) wdatafifo (.clk(clk),.rst_n(rst_n),.validin(IN_wvalid),.datain({IN_wdata,IN_wstrb})
    ,.softreset(1'b0),.full(wdfull)
    ,.readout(wused),.dataout({wdata,wstrb}),.empty(wdempty)
    ,.count(),.overflow()
);

wire arfull,rused,arempty;
wire [31:0] araddr;
syncfifo #(.WID(32),.DEPTH(8)) raddrfifo (.clk(clk),.rst_n(rst_n),.validin(IN_arvalid),.datain(IN_araddr)
    ,.softreset(1'b0),.full(arfull)
    ,.readout(rused),.dataout(araddr),.empty(arempty)
    ,.count(),.overflow()
);


assign IN_arready = !arfull;
wire [OUTS-1:0] bvalid;
wire wbad = writing && (wstate==0) & (wmatch==0);

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
          wstate <=0;
    end else begin
        if ((wstate==0)&&wbad) begin
            wstate <= 7;
        end else if (wstate==0) begin
            if (writing) wstate<=1;
        end else if (wstate==1) begin
            if (awready & wmatch) wstate<= 2;
        end else if (wstate==2) begin
            if (wready & wmatch) wstate <= 3;
        end else if (wstate==3) begin
            if (bvalid & wmatch) wstate <= 4;
        end else if (wstate==4) begin
            if (IN_bready) wstate <= 5;
        end else if (wstate==5) begin
            wstate <= 0;
        end else if (wstate==7) begin
            if (IN_bready) wstate <= 5;
        end
    end
end

wire [OUTS-1:0] awvalid = (writing && (wstate==1)) ? wmatch : 0 ;
wire [OUTS-1:0] wvalid = (writing && (wstate==2)) ? wmatch : 0 ;
assign IN_bvalid = (wstate==7) || (writing && (wstate==3) && |(bvalid & wmatch));
wire [OUTS-1:0] bresp;
assign IN_bresp = (|bresp) | wbad;



reg [3:0] rstate;
wire [OUTS-1:0] rmatch,arready,rready;
wire reading = !arempty;
wire [OUTS-1:0] arvalid = (reading && (rstate==0)) ? rmatch : 0 ;
wire [OUTS-1:0] rvalid;
assign IN_rvalid = (reading && (rstate==2)) ? |(rmatch & rvalid) : 0 ;
wire rbad = reading && (rstate==0) & (rmatch==0);

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
          rstate <=0;
    end else begin
        if ((rstate==0)&&rbad) begin
            rstate <= 7;
        end else if (rstate==0) begin
            if (reading) rstate<=1;
        end else if (rstate==1) begin
            if (arready) rstate<=2;
        end else if (rstate==2) begin
            if (IN_rready) rstate <= 0;
        end else if (rstate==7) begin
            rstate <= 0;
        end
    end
end
assign rused = (IN_rready && (rstate==2));
assign rready  =  (reading && IN_rready) ? rmatch : 0;



'''




def main():
    Spacing = eval(sys.argv[1])
    AxiIn = sys.argv[2]
    AxiOut = sys.argv[3:]

    Fout = open('axi4light_switch.v','w')
    Fout.write(HEADER)

    Str = INTERFACE.replace('PREF',AxiIn)
    Str = Str.replace('IN','input')
    Str = Str.replace('OUT','output')
    Fout.write(Str)
    Addressing = []
    while AxiOut != []:
        Bus = AxiOut.pop(0)
        Pages = int(AxiOut.pop(0))
        Addressing.append((Bus,Pages))
        Str = INTERFACE.replace('PREF',Bus)
        Str = Str.replace('IN','output')
        Str = Str.replace('OUT','input')
        Fout.write(Str)
        
    Fout.write(');\n')
    Bus,Pages = Addressing.pop(0)
    Len = len(Addressing)
    Prev = "32'h%x"%Spacing
    while (Addressing!=[]):
        Bus,Pages = Addressing.pop(0)
        Fout.write("wire [31:0]  BASE_%s = %s;\n"%(Bus,Prev))
        Fout.write("wire [31:0]  HIGH_%s = BASE_%s+16'h%x;\n"%(Bus,Bus,0x400 * Pages))
        Prev = 'HIGH_%s'%(Bus)
    Str = WARBITER.replace('IN',AxiIn)
    Str = Str.replace('OUTS',str(Len))
    Fout.write(Str)

    for ind,II in enumerate(AxiOut):
        Fout.write('assign  wmatch[%d] = (awaddr>=BASE_%s) && (awaddr<HIGH_%s);\n'%(ind,II,II))
        Fout.write('assign  rmatch[%d] = (araddr>=BASE_%s) && (araddr<HIGH_%s);\n'%(ind,II,II))
    for ind,II in enumerate(AxiOut):
        Fout.write('assign  %s_awvalid = awvalid[%s];\n'%(II,ind))
        Fout.write('assign  %s_wvalid = wvalid[%s];\n'%(II,ind))
        Fout.write('assign  %s_awaddr = awaddr-BASE_%s;\n'%(II,II))
        Fout.write('assign  %s_wdata = wdata;\n'%(II))
        Fout.write('assign  %s_wstrb = wstrb;\n'%(II))
        Fout.write('assign  %s_bready = bready;\n'%(II))
        Fout.write('assign  awready[%s]  = %s_awready;\n'%(ind,II))
        Fout.write('assign  wready[%s]  = %s_wready;\n'%(ind,II))
        Fout.write('assign  bresp[%s]  = (wstate==3) ? %s_bresp : 0;\n'%(ind,II))
        Fout.write('assign  bvalid[%s]  = (wstate==3) ? %s_bvalid : 0;\n'%(ind,II))

        Fout.write('assign  %s_araddr = araddr-BASE_%s;\n'%(II,II))
        Fout.write('assign  %s_arvalid = arvalid[%s];\n'%(II,ind))
        Fout.write('assign  rvalid[%s] = %s_rvalid;\n'%(ind,II))
        Fout.write('assign  arready[%s]  = (rstate==1) ? %s_arready : 0;\n'%(ind,II))
        Fout.write('assign  %s_rready  = (rstate==2) ? rready[%s] : 0;\n'%(II,ind))

    Fout.write('assign %s_rdata = \n'%(AxiIn))
    for ind,II in enumerate(AxiOut):
        Fout.write('    rmatch[%d] ? %s_rdata : \n'%(ind,II))
    Fout.write('   0;\n')
    Fout.write('assign %s_rresp = \n'%(AxiIn))
    for ind,II in enumerate(AxiOut):
        Fout.write('    rmatch[%d] ? %s_rresp : \n'%(ind,II))
    Fout.write('   0;\n')

    for II in AxiOut:
        for Sig in ['arprot','awprot']:
            Fout.write('assign %s_%s = %s_%s;\n'%(II,Sig,AxiIn,Sig))
    Fout.write('endmodule\n')
    Fout.close()

    createInstance(AxiIn,AxiOut)

def createInstance(AxiIn,AxiOut):
    Fout = open('axi4LiteSwitch.inst','w')

    Intrs = INTERFACE.split('\n')
    LL = []
    LW = []
    for line in Intrs:
        wrds = line.split()
        if 'PREF' in line:
            if len(wrds)==2:
                Wire = wrds[1]
                LW.append('wire %s;'%(Wire))
            elif len(wrds)==3:
                Wid = wrds[1]
                Wire = wrds[2]+wrds[1]
                LW.append('wire %s %s;'%(Wid,wrds[2]))
            LL.append(Wire)

    for Out in AxiOut:
        for Line in LW:
            Str = Line.replace('PREF',Out)
            Fout.write('%s\n'%Str)
    Fout.write('\n')

    Fout.write('axi4LiteSwitch axi4LiteSwitch (.clk(clk),.rst_n(rst_n)\n')

    for Line in LL:
        Str = Line.replace('PREF',AxiIn)
        if '[' in Str:
            Bus = Str[:Str.index('[')]
        else:
            Bus = Str
        Fout.write('    ,.%s(%s)\n'%(Bus,Str))
    Fout.write('\n')
    for Out in AxiOut:
        for Line in LL:
            Str = Line.replace('PREF',Out)
            if '[' in Str:
                Bus = Str[:Str.index('[')]
            else:
                Bus = Str
            Fout.write('    ,.%s(%s)\n'%(Bus,Str))
        Fout.write('\n')

    Fout.write(');\n')
    Fout.close()


if __name__ == '__main__': main()
