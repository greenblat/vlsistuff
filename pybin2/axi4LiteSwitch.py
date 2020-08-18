#! /usr/bin/python
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
    reg [2:0] wstate;
    reg [1:0] rstate;
    reg [31:0] awaddr,araddr;
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            wstate <=0;
            awaddr <= 0;
        end else begin
            if (wstate==0) begin
                if (IN_awvalid) begin
                    wstate <= 1;      
                    awaddr <= IN_awaddr;
                end
            end else if (wstate==1) begin
                if (awready) wstate <= 2;      
            end else if (wstate==2) begin
                if (wready) wstate <= 3;      
            end else if (wstate==3) begin
                if (IN_bvalid && IN_bready) wstate <= 0;
            end
        end
    end

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            rstate <=0;
            araddr <= 0;
        end else begin
            if (rstate==0) begin
                if (IN_arvalid) begin
                    rstate <= 1;      
                    araddr <= IN_araddr;
                end
            end else if (rstate==1) begin
                if (IN_arready) rstate <= 2;      
            end else if (rstate==2) begin
                if (IN_rvalid && IN_rready) rstate <= 3;      
            end else if (rstate==3) begin
                rstate <= 0;
            end
        end
    end



'''




def main():
    AxiIn = sys.argv[1]
    AxiOut = sys.argv[2:]

    Fout = open('axi4light_switch.v','w')
    Fout.write(HEADER)

    Str = INTERFACE.replace('PREF',AxiIn)
    Str = Str.replace('IN','input')
    Str = Str.replace('OUT','output')
    Fout.write(Str)

    for II in AxiOut:
        Str = INTERFACE.replace('PREF',II)
        Str = Str.replace('IN','output')
        Str = Str.replace('OUT','input')
        Fout.write(Str)
        
    Fout.write(');\n')
    Addr = AxiOut[0]
    Fout.write("wire [31:0]  BASE_%s = 32'h%x;\n"%(Addr,0))
    Fout.write("wire [31:0]  HIGH_%s = BASE_%s+16'h1000;\n"%(Addr,Addr))
    for II in AxiOut[1:]:
        Fout.write("wire [31:0]  BASE_%s = HIGH_%s;\n"%(II,Addr))
        Fout.write("wire [31:0]  HIGH_%s = BASE_%s+16'h1000;\n"%(II,II))
        Addr = II

    for II in AxiOut:
        Fout.write('wire %s_wr = (%s_awvalid && (%s_awaddr>=BASE_%s) && (%s_awaddr<HIGH_%s));\n'%(II,AxiIn,AxiIn,II,AxiIn,II))
        Fout.write('wire %s_rd = (%s_arvalid && (%s_araddr>=BASE_%s) && (%s_araddr<HIGH_%s));\n'%(II,AxiIn,AxiIn,II,AxiIn,II))
        Fout.write('reg %s_awvalid; always @(posedge clk) if (wstate==0) %s_awvalid <= %s_wr;\n'%(II,II,II))
        Fout.write('reg %s_arvalid; always @(posedge clk) if (rstate==0) %s_arvalid <= %s_rd;\n'%(II,II,II))
    for II in AxiOut:
        Fout.write('wire %s_wvalid = %s_wvalid && (wstate==2) && %s_awvalid;\n'%(II,AxiIn,II))

    Fout.write('wire awready = (wstate==1) && (0 \n')
    for II in AxiOut:
        Fout.write('    ||( %s_awvalid && %s_awready)\n'%(II,II))
    Fout.write(');\n')
    Fout.write('wire wready = (wstate==2) && (0 \n')
    for II in AxiOut:
        Fout.write('    ||( %s_awvalid && %s_wready)\n'%(II,II))
    Fout.write(');\n')
    Fout.write('wire bvalid = (wstate==3) && (0 \n')
    for II in AxiOut:
        Fout.write('    ||( %s_awvalid && %s_bvalid)\n'%(II,II))
    Fout.write(');\n')
    Fout.write('wire bresp = (wstate==3) && (0 \n')
    for II in AxiOut:
        Fout.write('    ||( %s_awvalid && %s_bresp)\n'%(II,II))
    Fout.write(');\n')


    Fout.write('wire arready = (rstate==1) && (0 \n')
    for II in AxiOut:
        Fout.write('    ||( %s_arvalid && %s_arready)\n'%(II,II))
    Fout.write(');\n')
    Fout.write('wire %s_rvalid = (rstate==2) && (0 \n'%AxiIn)
    for II in AxiOut:
        Fout.write('    ||( %s_arvalid && %s_rvalid)\n'%(II,II))
    Fout.write(');\n')
    Fout.write('wire %s_rdata = \n'%AxiIn)
    for II in AxiOut:
        Fout.write('     (%s_arvalid) ? %s_rdata :\n'%(II,II))
    Fout.write('0;\n')

#    Fout.write('wire %s_rready = \n'%AxiIn)
#    for II in AxiOut:
#        Fout.write('     (%s_arvalid) ? %s_rready :\n'%(II,II))
#    Fout.write('0;\n')

    Str = WARBITER.replace('IN',AxiIn)
    Fout.write(Str)



    for II in AxiOut:
        for Sig in ['bready','rready','araddr','arprot','awaddr','awprot','wstrb','wdata']:
            Fout.write('assign %s_%s = %s_%s;\n'%(II,Sig,AxiIn,Sig))


    Fout.write('endmodule\n')

if __name__ == '__main__': main()
