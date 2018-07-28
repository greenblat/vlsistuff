#! /usr/bin/python

import os,sys,string,types
try:
    import xls2csv
    XLS_PRESENT = True
except:
    XLS_PRESENT = False
import csvPageClass
import logs

mustParams = {}
listedParams = {}
mustParams['reg'] = string.split('access wid')
listedParams['reg'] = mustParams['reg'] + string.split('desc latch reset')

helpSTRING = '''
    regfile.py ny.xlsx> | <reg.csv> | <test1.regfile> 
    accepts either xls or csv or text format.


regfile newone

reg control access=rw  
    field interpolate_G wid=1
    field use_external wid=1
    field use_pattern wid=2

reg thres access=rw wid=16
reg extern_std access=rw wid=32

reg max_sat access=ro wid=32


array cucu access=ro wid=20 amount=128 desc="what the world"

ram holder access=rw wid=32 amount=2048






'''

def helpString():
    print helpSTRING

txt=False
def main():
    global txt
    Csvs=[]
    Regfiles=[]
    Frenames={}
    Args = sys.argv[1:]
    if len(Args)==0:
        help_string()
    for Ind,Fname in enumerate(Args):
        if '.xls' in Fname:
            if not os.path.exists(Fname):
                print 'cannot open xls file "%s"'%Fname
                sys.exit()
            CsvName = produce_csv_from_xls(Fname)
            Csvs.append((CsvName,Fname))
            Frenames[CsvName]=Fname
        elif '.csv' in Fname:
            Csvs.append((Fname,Fname))
            Frenames[Fname]=Fname
        elif '.regfile' in Fname:
            Regfiles.append(Fname)
        if '-h' in Fname:
            help_string()
    Reset = 'async'
    if Csvs!=[]:
        Csv = csvPageClass.csvPageClass(Csvs,produce_csv_from_xls)
        Chip = 'regff'
    elif (Regfiles!=[]):
        txt = txtRegClass()
        for Regfile in Regfiles:
            buildRegfile(txt,Regfile) 
        txt.assignRegWidByFields()
        txt.createCsvFile()
        Csv = csvPageClass.csvPageClass([(txt.csvFileName,txt.csvFileName)],produce_csv_from_xls)
        Chip = txt.Chip
        dumpRdl(txt)
        Reset = txt.Reset
        print 'reset',Reset
    else:
        logs.log_error('need eother xls or csv or regfile extension file')

#    if txt:
#        txt.dump()
#        return


    FFF = {}
    Addrs = []
    for Reg in Csv.regs:
        Wid = Csv.regs[Reg][1]
        Addr = Csv.regs[Reg][3]
        Addrs.append((Addr,Reg))
        Fields = Csv.fields[Reg]
        Pos=0
        if Fields!=[]:
            for Widf,Def,Field,Desc in Fields:
                if Widf==1:
                    FFF[(Reg,Field)]=Pos
                    Pos += 1
                else: 
                    FFF[(Reg,Field)]=Widf+Pos-1,Pos
                    Pos += Widf
        if Wid=='':
           Csv.regs[Reg][1]=Pos 
    dumpAdaCsv(FFF,Addrs,Csv,Chip)
    dumpApbVerilog(FFF,Addrs,Csv,Reset)
    dumpRamVerilog(FFF,Addrs,Csv,Reset)
    dumpAxi4LiteVerilog(FFF,Addrs,Csv,Reset)

def dumpApbVerilog(FFF,Addrs,Csv,Reset):
    hasFields={}
    for (Reg,_) in FFF:
        hasFields[Reg]=True
    File = open('%s.v'%Csv.Module,'w')
    W1 = len(bin(Csv.runAddr))-3
    File.write('module %s (input clk,input rst_n,input pwrite, input psel, input penable, input [1:0] psize, input [31:0] pwdata, output reg [31:0] prdata, input [%d:0] paddr ,output reg [%d:0] waddr\n'%(Csv.Module,W1,W1))
    LL = writeInputsOutputsAndWires(Csv,File)
#    LL = []
#    for Reg in Csv.regs:
#        ST = Csv.regs[Reg]
#        LL.append((int(ST[3]),Reg))
#    LL.sort()
#    Wires = ''
#    for Add,Reg in LL:
#        ST = Csv.regs[Reg]
#        Wid = int(ST[1])
#        Acc = ST[0]
#        if writable(Acc):
#            Dir = 'output reg'
#        else:
#            Dir = 'input    '
#        if Wid>1:
#            WW = '[%2d:0]'%(Wid-1)
#        else:
#            WW = '       '
#        if Acc in ['ram']:
#            File.write('   ,input %s %s_rdata\n'%(WW,Reg))
#        elif  writable(Acc)or (Reg not in hasFields):
#            File.write('   ,%s %s %s\n'%(Dir,WW,Reg))
#        elif  not writable(Acc)and (Reg in hasFields):
#            Wires += 'wire %s %s;\n'%(WW,Reg)
#
#        if 'pulse' in Acc:
#            File.write('   ,output %s_pulse\n'%(Reg))
#        if Acc in ['external','ram']:
#            File.write('   ,output %s_wr_pulse\n'%(Reg))
#            File.write('   ,output %s_rd_pulse\n'%(Reg))
#            if (Wid>32)or(Acc=='ram'):
#                File.write('   ,output reg [15:0] %s_addr\n'%(Reg))
#            
#
##    for (Reg,Field) in FFF:
##        Pos = FFF[(Reg,Field)]
##        ST = Csv.regs[Reg]
##        Acc = ST[0]
##        if writable(Acc):
##            Dir = 'output '
##        else:
##            Dir = 'input  '
##        if type(Pos)==types.TupleType:
##            (H,L) = Pos
##            WW = int(H)-int(L)
##            File.write('   ,%s [%d:0] %s\n'%(Dir,WW,Field))
##        else:
##            File.write('   ,%s        %s\n'%(Dir,Field))
#
#    File.write(');\n')
#    File.write(Wires)
    X = (1<<(W1+1))-1
    X = X & 0xfffffffc
    File.write('wire [%d:0] mpaddr = paddr[%d:0] & %d\'h%x;\n'%(W1,W1,W1+1,X))
    File.write('wire [31:0] rdata_wire = \n')
    for Add,Reg in LL:
        ST = Csv.regs[Reg]
        if ST[0]=='ram':
            Reg = '%s_rdata'%Reg
        Wid = int(ST[1])
        Addr = int(ST[3])& 0xfffc
        if (Wid<=32):
            if (Wid<32):
                RR = "{%d'b0,%s}"%(32-Wid,Reg)
            else:
                RR = Reg
            if ST[0]=='ram':
                lastAddr = Addr + ST[2] * bytesPerWord(ST[1])
                File.write('    ((mpaddr[%d:0]>=\'h%x) && (mpaddr[%d:0]<\'h%x)) ? %s :\n'%(W1,Addr,W1,lastAddr,RR))
            else:
                File.write('    (mpaddr[%d:0]==\'h%x) ? %s :\n'%(W1,Addr,RR))
        else:
            Many,Add = Wid/32,Wid%32
            Many += (Add>0)
            for X in range(Many):
                File.write('    (mpaddr[%d:0]==\'h%x) ? %s[%d:%d] :\n'%(W1,Addr+4*X,Reg,31+32*X,32*X))
    File.write("    32'b0;\n")

    
    createFieldAssigns(FFF,Csv)


    File.write('always @(posedge clk) prdata <= rdata_wire;\n')

#    for (Reg,Field) in FFF:
#        Pos = FFF[(Reg,Field)]
#        ST = Csv.regs[Reg]
#        Acc = ST[0]
#        if writable(Acc):
#            Dir = 'output '
#        else:
#            Dir = 'input  '
#        Pos = FFF[(Reg,Field)]
#        if 'output' in Dir:
#            if type(Pos)==types.TupleType:
#                (H,L) = Pos
#                File.write('assign %s = %s[%s:%s];\n'%(Field,Reg,H,L))
#            else:
#                File.write('assign %s = %s[%s];\n'%(Field,Reg,Pos))
#        else:
#            if type(Pos)==types.TupleType:
#                (H,L) = Pos
#                File.write('assign %s[%s:%s] = %s;\n'%(Reg,H,L,Field))
#            else:
#                File.write('assign %s[%s] = %s;\n'%(Reg,Pos,Field))

    Str = string.replace(STRING0,'W1',str(W1))
    Str = string.replace(Str,'or negedge rst_n',Reset)
    File.write(Str)
    
    File.write('always @(posedge clk %s) begin\n    if (!rst_n) begin\n'%Reset)
    for Add,Reg in LL:
        ST = Csv.regs[Reg]
        Wid = int(ST[1])
        Acc = ST[0]
        if type(ST[2])==types.IntType:
           Def = ST[2]
        else:
           Def = eval(ST[2])
        if writable(Acc):
            File.write('        %s <= %d\'h%x;\n'%(Reg,Wid,Def))
    File.write('    end else if (apb_write && penable)  begin\n')
    for Add,Reg in LL:
        ST = Csv.regs[Reg]
        Wid = int(ST[1])
        Acc = ST[0]
        Addr = int(ST[3])& 0xfffc
        if writable(Acc):
            if (Wid<2):
                File.write('        if (mpaddr[%d:0]==\'h%x) %s <= wdata[0];\n'%(W1,Addr,Reg))
            elif (Wid<=8):
                File.write('        if (mpaddr[%d:0]==\'h%x) %s <= wdata[7:0];\n'%(W1,Addr,Reg))
            elif (Wid<=32):
                Wdata = '(%s[%d:0] & ~mask[%d:0]) | (wdata[%d:0] &mask[%d:0])'%(Reg,Wid-1,Wid-1,Wid-1,Wid-1) 
                File.write('        if (mpaddr[%d:0]==\'h%x) %s <= %s;\n'%(W1,Addr,Reg,Wdata))
            else:

                Many,Add = Wid/32,Wid%32
                Many += (Add>0)
                for X in range(Many):
                    Wdata = '(%s[%d:%d] & ~mask[31:0]) | (wdata &mask)'%(Reg,X*32+31,X*32) 
                    File.write('        if (mpaddr[%d:0]==\'h%x) %s[%d:%d] <= %s;\n'%(W1,Addr+4*X,Reg,X*32+31,X*32,Wdata))

    File.write('    end \n')
    File.write('end \n')


    for Add,Reg in LL:
        ST = Csv.regs[Reg]
        Wid = int(ST[1])
        Acc = ST[0]
        Addr = int(ST[3])& 0xfffc
        if 'ram' in Acc:
            lastAddr = Addr + ST[2] * bytesPerWord(ST[1])
            File.write('wire %s_ram_sel = psel &&  (mpaddr[%d:0]>=\'h%x) && (mpaddr[%d:0]<\'h%x);\n'%(Reg,W1,Addr,W1,lastAddr))
            File.write('reg %s_wr_pulse_reg; always @(posedge clk)  %s_wr_pulse_reg <= pwrite &&  %s_ram_sel;\n'%(Reg,Reg,Reg))
            File.write('assign %s_wr_pulse = penable &&  %s_wr_pulse_reg;\n'%(Reg,Reg))
            File.write('assign %s_rd_pulse = !pwrite &&  %s_ram_sel;\n'%(Reg,Reg))
            File.write('always @(posedge clk)  %s_addr <= mpaddr-\'h%x;\n'%(Reg,Addr))
        if 'external' in Acc:
            lastAddr = Addr + Wid/8
            if Wid>32:
                File.write('wire %s_wr_sel = pwrite && psel &&  (mpaddr[%d:0]>=\'h%x) && (mpaddr[%d:0]<\'h%x);\n'%(Reg,W1,Addr,W1,lastAddr))
                File.write('wire %s_rd_sel = !pwrite && psel &&  (mpaddr[%d:0]>=\'h%x) && (mpaddr[%d:0]<\'h%x);\n'%(Reg,W1,Addr,W1,lastAddr))
            else:
                File.write('wire %s_wr_sel = pwrite && psel &&  (mpaddr[%d:0]==\'h%x);\n'%(Reg,W1,Addr))
                File.write('wire %s_rd_sel = !pwrite && psel &&  (mpaddr[%d:0]==\'h%x);\n'%(Reg,W1,Addr))
            File.write('reg %s_wr_pulse_reg; always @(posedge clk)  %s_wr_pulse_reg <= %s_wr_sel;\n'%(Reg,Reg,Reg))
            File.write('reg %s_rd_pulse_reg; always @(posedge clk)  %s_rd_pulse_reg <= %s_rd_sel;\n'%(Reg,Reg,Reg))
            File.write('assign %s_wr_pulse = %s_wr_pulse_reg  && penable;\n'%(Reg,Reg))
            File.write('assign %s_rd_pulse = %s_rd_pulse_reg  && penable;\n'%(Reg,Reg))
            if Wid>32:
                File.write('always @(posedge clk)  %s_addr <= mpaddr-\'h%x;\n'%(Reg,Addr))
        if 'pulse' in Acc:
            if writable(Acc):
                File.write('reg %s_wr_pulse_reg; always @(posedge clk)  %s_wr_pulse_reg <= pwrite && psel &&  (mpaddr[%d:0]==\'h%x);\n'%(Reg,Reg,W1,Addr))
                File.write('reg %s_pulse_reg; always @(posedge clk) %s_pulse_reg <=  penable && %s_wr_pulse_reg ;\n'%(Reg,Reg,Reg))
                File.write('assign %s_pulse = %s_pulse_reg ;\n'%(Reg,Reg))
            else:    
                File.write('reg %s_rd_pulse_reg; always @(posedge clk)  %s_rd_pulse_reg <= !pwrite && psel &&  (mpaddr[%d:0]==\'h%x);\n'%(Reg,Reg,W1,Addr))
                File.write('assign %s_pulse =  penable && %s_rd_pulse_reg ;\n'%(Reg,Reg))
#                File.write('assign %s_pulse = !pwrite &&  psel &&  (mpaddr[%d:0]==\'h%x);\n'%(Reg,W1,Addr))

    File.write('endmodule\n')

AXISTRING = '''
module MODULE (input clk, input rst_n
    ,input awvalid,output awready, input [31:0] awaddr
    ,input wvalid, output wready, input [31:0] wdata, input [3:0] wstrb
    ,output bvalid, output [1:0] bresp, input bready

    ,input arvalid, output arready, input [31:0] araddr
    ,output rvalid, input rready, output [31:0] rdata, output [1:0] rresp
'''

def writeInputsOutputsAndWires(Csv,File):
    LL = []
    for Reg in Csv.regs:
        ST = Csv.regs[Reg]
        LL.append((int(ST[3]),Reg))
    LL.sort()
    Wires = ''
    for Add,Reg in LL:
        ST = Csv.regs[Reg]
        Wid = int(ST[1])
        Acc = ST[0]
        if writable(Acc):
            Dir = 'output reg'
        else:
            Dir = 'input    '
        if Wid>1:
            WW = '[%2d:0]'%(Wid-1)
        else:
            WW = '       '
        if Acc in ['ram']:
            File.write('   ,input %s %s_rdata\n'%(WW,Reg))
        else:
            File.write('   ,%s %s %s\n'%(Dir,WW,Reg))

        if 'pulse' in Acc:
            File.write('   ,output %s_pulse\n'%(Reg))
        if Acc in ['external','ram']:
            File.write('   ,output %s_wr_pulse\n'%(Reg))
            File.write('   ,output %s_rd_pulse\n'%(Reg))
            if (Wid>32)or(Acc=='ram'):
                File.write('   ,output reg [15:0] %s_addr\n'%(Reg))
    File.write(');\n')
    File.write(Wires)
    return LL

AXISTRING2 = '''
wire adfull,adempty,dafull,daempty;
wire arfull,arempty,drfull,drempty;
assign awready = !adfull;
assign wready = !dafull;
assign rvalid = !drempty;
assign rresp = 2'b0;
assign bresp = 2'b0;

wire [WW-1:0] iwaddr,iraddr;
wire do_write = !adempty && !daempty;
syncfifo #(WW,2) adfifo(.clk(clk),.rst_n(rst_n)
    ,.validin(awvalid),.datain(awaddr[WW-1:0])
    ,.readout(do_write),.dataout(iwaddr[WW-1:0])
    ,.full(adfull),.empty(adempty),.count(),.overflow(),.softreset(1'b0)
);
wire [31:0] iwdata,irdata;
wire [3:0] iwstrb;
wire do_read  = !arempty && !drfull;
syncfifo #(32+4,2) dafifo(.clk(clk),.rst_n(rst_n)
    ,.validin(wvalid),.datain({wdata,wstrb})
    ,.readout(do_write),.dataout({iwdata,iwstrb})
    ,.full(dafull),.empty(daempty),.count(),.overflow(),.softreset(1'b0)
);
reg was_do_write;
assign bvalid = (do_write || was_do_write);
always @(posedge clk) begin
    if (!rst_n) begin
        was_do_write <= 1'b0;
    end else begin
        if (do_write && !bready) begin
            was_do_write <= 1'b1;
        end else if (bready) begin
            was_do_write <= 1'b0;
        end
    end
end
syncfifo #(WW,2) arfifo(.clk(clk),.rst_n(rst_n)
    ,.validin(arvalid),.datain(araddr[WW-1:0])
    ,.readout(do_read),.dataout(iraddr[WW-1:0])
    ,.full(arfull),.empty(arempty),.count(),.overflow(),.softreset(1'b0)
);
assign arready = !arfull;
syncfifo #(32,2) drfifo(.clk(clk),.rst_n(rst_n)
    ,.validin(do_read),.datain(irdata)
    ,.readout(rready),.dataout(rdata)
    ,.full(drfull),.empty(drempty),.count(),.overflow(),.softreset(1'b0)
);
wire [31:0] mask = {  {8{iwstrb[3]}},{8{iwstrb[2]}},{8{iwstrb[1]}},{8{iwstrb[0]}} };

'''
    

def dumpAxi4LiteVerilog(FFF,Addrs,Csv,Reset):
    hasFields={}
    for (Reg,_) in FFF:
        hasFields[Reg]=True
    File = open('%s.axiv'%Csv.Module,'w')
    W1 = len(bin(Csv.runAddr))-2
#    print '>>>',Csv.runAddr,Csv.runAddr,bin(Csv.runAddr),len(bin(Csv.runAddr))

    File.write(string.replace(AXISTRING,"MODULE",Csv.Module))
    LL = writeInputsOutputsAndWires(Csv,File)

    File.write(string.replace(AXISTRING2,"WW",str(W1)))

    X = (1<<(W1+1))-1
    X = X & 0xfffffffc
    File.write('assign irdata = \n')
    for Add,Reg in LL:
        ST = Csv.regs[Reg]
        if ST[0]=='ram':
            Reg = '%s_rdata'%Reg
        Wid = int(ST[1])
        Addr = int(ST[3])& 0xfffc
        if (Wid<=32):
            if (Wid<32):
                RR = "{%d'b0,%s}"%(32-Wid,Reg)
            else:
                RR = Reg
            if ST[0]=='ram':
                lastAddr = Addr + ST[2] * bytesPerWord(ST[1])
                File.write('    ((iraddr[%d:0]>=\'h%x) && (iraddr[%d:0]<\'h%x)) ? %s :\n'%(W1-1,Addr,W1-1,lastAddr,RR))
            else:
                File.write('    (iraddr[%d:0]==\'h%x) ? %s :\n'%(W1-1,Addr,RR))
        else:
            Many,Add = Wid/32,Wid%32
#            Many += (Add>0)
            for X in range(Many):
                File.write('    (iraddr[%d:0]==\'h%x) ? %s[%d:%d] :\n'%(W1-1,Addr+4*X,Reg,31+32*X,32*X))
            if Add>0:
                X += 1
                File.write('    (iraddr[%d:0]==\'h%x) ? {%d\'b0,%s[%d:%d]} :\n'%(W1-1,Addr+4*X,32-Add,Reg,Add+32*X-1,32*X))

    File.write("    32'b0;\n")

    
    createFieldAssigns(FFF,Csv)


    
    File.write('always @(posedge clk %s) begin\n    if (!rst_n) begin\n'%Reset)
    for Add,Reg in LL:
        ST = Csv.regs[Reg]
        Wid = int(ST[1])
        Acc = ST[0]
        if type(ST[2])==types.IntType:
           Def = ST[2]
        else:
           Def = eval(ST[2])
        if writable(Acc):
            File.write('        %s <= %d\'h%x;\n'%(Reg,Wid,Def))
    File.write('    end else if (do_write)  begin\n')
    for Add,Reg in LL:
        ST = Csv.regs[Reg]
        Wid = int(ST[1])
        Acc = ST[0]
        Addr = int(ST[3])& 0xfffc
        if writable(Acc):
            if (Wid<2):
                File.write('        if (iwaddr[%d:0]==\'h%x) %s <= iwdata[0];\n'%(W1-1,Addr,Reg))
            elif (Wid<=8):
                File.write('        if (iwaddr[%d:0]==\'h%x) %s <= iwdata[7:0];\n'%(W1-1,Addr,Reg))
            elif (Wid<=32):
                Wdata = '(%s[%d:0] & ~mask[%d:0]) | (iwdata &mask)'%(Reg,Wid-1,Wid-1) 
                File.write('        if (iwaddr[%d:0]==\'h%x) %s <= %s;\n'%(W1-1,Addr,Reg,Wdata))
            else:

                Many,Add = Wid/32,Wid%32
                Many += (Add>0)
                for X in range(Many):
                    Wdata = '(%s[%d:%d] & ~mask[31:0]) | (iwdata &mask)'%(Reg,X*32+31,X*32) 
                    File.write('        if (iwaddr[%d:0]==\'h%x) %s[%d:%d] <= %s;\n'%(W1-1,Addr+4*X,Reg,X*32+31,X*32,Wdata))

    File.write('    end \n')
    File.write('end \n')


    for Add,Reg in LL:
        ST = Csv.regs[Reg]
        Wid = int(ST[1])
        Acc = ST[0]
        Addr = int(ST[3])& 0xfffc
        if 'ram' in Acc:
            lastAddr = Addr + ST[2] * bytesPerWord(ST[1])
            File.write('wire %s_wr_ram_sel = do_write &&  (iwaddr[%d:0]>=\'h%x) && (iwaddr[%d:0]<\'h%x);\n'%(Reg,W1-1,Addr,W1-1,lastAddr))
            File.write('wire %s_rd_ram_sel = do_read &&  (iraddr[%d:0]>=\'h%x) && (iraddr[%d:0]<\'h%x);\n'%(Reg,W1-1,Addr,W1-1,lastAddr))
            File.write('reg %s_wr_pulse_reg; always @(posedge clk)  %s_wr_pulse_reg <= %s_wr_ram_sel;\n'%(Reg,Reg,Reg))
            File.write('assign %s_wr_pulse = %s_wr_pulse_reg;\n'%(Reg,Reg))
            File.write('assign %s_rd_pulse = %s_rd_ram_sel;\n'%(Reg,Reg))
            File.write('always @(posedge clk)  %s_addr <= (do_write ? iwaddr :iraddr)-\'h%x;\n'%(Reg,Addr))
        if 'external' in Acc:
            lastAddr = Addr + Wid/8
            if Wid>32:
                File.write('wire %s_wr_sel = do_write &&  (iwaddr[%d:0]>=\'h%x) && (iwaddr[%d:0]<\'h%x);\n'%(Reg,W1-1,Addr,W1-1,lastAddr))
                File.write('wire %s_rd_sel = do_read  &&  (iraddr[%d:0]>=\'h%x) && (iraddr[%d:0]<\'h%x);\n'%(Reg,W1-1,Addr,W1-1,lastAddr))
            else:
                File.write('wire %s_wr_sel = do_write &&  (iwaddr[%d:0]==\'h%x);\n'%(Reg,W1-1,Addr))
                File.write('wire %s_rd_sel = do_read  &&  (iraddr[%d:0]==\'h%x);\n'%(Reg,W1-1,Addr))
            File.write('reg %s_wr_pulse_reg; always @(posedge clk)  %s_wr_pulse_reg <= %s_wr_sel;\n'%(Reg,Reg,Reg))
            File.write('reg %s_rd_pulse_reg; always @(posedge clk)  %s_rd_pulse_reg <= %s_rd_sel;\n'%(Reg,Reg,Reg))
            File.write('assign %s_wr_pulse = %s_wr_pulse_reg;\n'%(Reg,Reg))
            File.write('assign %s_rd_pulse = %s_rd_pulse_reg;\n'%(Reg,Reg))
            if Wid>32:
                File.write('always @(posedge clk)  %s_addr <= (do_write ? iwaddr :iraddr)-\'h%x;\n'%(Reg,Addr))
        if 'pulse' in Acc:
            if writable(Acc):
                File.write('reg %s_pulse_reg; always @(posedge clk)  %s_pulse_reg <= do_write  &&  (iwaddr[%d:0]==\'h%x);\n'%(Reg,Reg,W1-1,Addr))
                File.write('assign %s_pulse = %s_pulse_reg ;\n'%(Reg,Reg))
            else:    
                File.write('reg %s_rd_pulse_reg; always @(posedge clk)  %s_rd_pulse_reg <= do_read &&  (iraddr[%d:0]==\'h%x);\n'%(Reg,Reg,W1-1,Addr))
                File.write('assign %s_pulse = %s_rd_pulse_reg;\n'%(Reg,Reg))

    File.write('endmodule\n')






def createFieldAssigns(FFF,Csv):
    File = open('%s.fields'%Csv.Module,'w')
    for (Reg,Field) in FFF:
        Pos = FFF[(Reg,Field)]
        ST = Csv.regs[Reg]
        Acc = ST[0]
        if writable(Acc):
            Dir = 'output '
        else:
            Dir = 'input  '
        Pos = FFF[(Reg,Field)]
        if 'output' in Dir:
            if type(Pos)==types.TupleType:
                (H,L) = Pos
                File.write('wire [%s:0]  %s = %s[%s:%s];\n'%(H-L,Field,Reg,H,L))
            else:
                File.write('wire %s = %s[%s];\n'%(Field,Reg,Pos))
        else:
            if type(Pos)==types.TupleType:
                (H,L) = Pos
                File.write('assign %s[%s:%s] = %s;\n'%(Reg,H,L,Field))
            else:
                File.write('assign %s[%s] = %s;\n'%(Reg,Pos,Field))


STRING0 = '''            
reg apb_write;
reg [1:0] wsize;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        apb_write <= 1'b0;
        waddr <= 0;
        wsize <= 0;
    end else begin
        apb_write <= psel && pwrite;
        waddr <= mpaddr;
        wsize <= psize;
    end
end
wire [31:0] mask = (wsize==1) ? 32'hff : (wsize==2) ? 32'hffff :  32'hffffffff;
wire [31:0] wdata = (wsize==1) ? {4{pwdata[7:0]}} : (wsize==2) ? {2{pwdata[15:0]}} :  pwdata;
'''




def dumpRamVerilog(FFF,Addrs,Csv,Reset):
    hasFields={}
    for (Reg,_) in FFF:
        hasFields[Reg]=True
    File = open('%s.vram'%Csv.Module,'w')
    W1 = len(bin(Csv.runAddr))-3
    File.write('module %s (input clk,input rst_n,input rwrite, input rsel, input [1:0] rsize, input [31:0] wdata, output [31:0] rdata, input [%d:0] addr ,output reg [%d:0] waddr\n'%(Csv.Module,W1,W1))
    LL = []
    for Reg in Csv.regs:
        ST = Csv.regs[Reg]
        LL.append((int(ST[3]),Reg))
    LL.sort()
    Wires = ''
    for Add,Reg in LL:
        ST = Csv.regs[Reg]
        Wid = int(ST[1])
        Acc = ST[0]
        if writable(Acc):
            Dir = 'output reg'
        else:
            Dir = 'input    '
        if Wid>1:
            WW = '[%2d:0]'%(Wid-1)
        else:
            WW = '       '
        if Acc in ['ram']:
            File.write('   ,input %s %s_rdata\n'%(WW,Reg))
        elif  writable(Acc)or (Reg not in hasFields):
            File.write('   ,%s %s %s\n'%(Dir,WW,Reg))
        elif  not writable(Acc)and (Reg in hasFields):
            Wires += 'wire %s %s;\n'%(WW,Reg)

        if 'pulse' in Acc:
            File.write('   ,output %s_pulse\n'%(Reg))
        if Acc in ['external','ram']:
            File.write('   ,output %s_wr_pulse\n'%(Reg))
            File.write('   ,output %s_rd_pulse\n'%(Reg))
            if (Wid>32)or(Acc=='ram'):
                File.write('   ,output reg [15:0] %s_addr\n'%(Reg))
            

    for (Reg,Field) in FFF:
        Pos = FFF[(Reg,Field)]
        ST = Csv.regs[Reg]
        Acc = ST[0]
        if writable(Acc):
            Dir = 'output '
        else:
            Dir = 'input  '
        if type(Pos)==types.TupleType:
            (H,L) = Pos
            WW = int(H)-int(L)
            File.write('   ,%s [%d:0] %s\n'%(Dir,WW,Field))
        else:
            File.write('   ,%s        %s\n'%(Dir,Field))
    File.write(');\n')
    File.write(Wires)
    File.write('wire [31:0] mask = (rsize==1) ? 32\'hff : (rsize==2) ? 32\'hffff :  32\'hffffffff;\n')
    File.write('wire [31:0] wdata = (rsize==1) ? {4{wdata[7:0]}} : (rsize==2) ? {2{wdata[15:0]}} :  wdata;\n')

    X = (1<<(W1+1))-1
    X = X & 0xfffffffc
    File.write('wire [%d:0] mpaddr = addr[%d:0] & %d\'h%x;\n'%(W1,W1,W1+1,X))
    File.write('assign rdata = \n')
    for Add,Reg in LL:
        ST = Csv.regs[Reg]
        if ST[0]=='ram':
            Reg = '%s_rdata'%Reg
        Wid = int(ST[1])
        Addr = int(ST[3])& 0xfffc

        if (Wid<=32):
            if (Wid<32):
                RR = "{%d'b0,%s}"%(32-Wid,Reg)
            else:
                RR = Reg 
            if ST[0]=='ram':
                lastAddr = Addr + ST[2] * bytesPerWord(ST[1])
                File.write('    ((mpaddr[%d:0]>=\'h%x) && (mpaddr[%d:0]<\'h%x)) : %s :\n'%(W1,Addr,W1,lastAddr,RR))
            else:
                File.write('    (mpaddr[%d:0]==\'h%x) ? %s :\n'%(W1,Addr,RR))
        else:
            Many,Add = Wid/32,Wid%32
            Many += (Add>0)
            for X in range(Many):
                File.write('    (mpaddr[%d:0]==\'h%x) ? %s[%d:%d] :\n'%(W1,Addr+4*X,Reg,31+32*X,32*X))
    File.write("    32'b0;\n")

    



    for (Reg,Field) in FFF:
        Pos = FFF[(Reg,Field)]
        ST = Csv.regs[Reg]
        Acc = ST[0]
        if writable(Acc):
            Dir = 'output '
        else:
            Dir = 'input  '
        Pos = FFF[(Reg,Field)]
        if 'output' in Dir:
            if type(Pos)==types.TupleType:
                (H,L) = Pos
                File.write('assign %s = %s[%s:%s];\n'%(Field,Reg,H,L))
            else:
                File.write('assign %s = %s[%s];\n'%(Field,Reg,Pos))
        else:
            if type(Pos)==types.TupleType:
                (H,L) = Pos
                File.write('assign %s[%s:%s] = %s;\n'%(Reg,H,L,Field))
            else:
                File.write('assign %s[%s] = %s;\n'%(Reg,Pos,Field))

    
    writeLatches(File,Reset,LL,Csv,W1)
    writeFlops(File,Reset,LL,Csv,W1)


    for Add,Reg in LL:
        ST = Csv.regs[Reg]
        Wid = int(ST[1])
        Acc = ST[0]
        Addr = int(ST[3])& 0xfffc
        if 'ram' in Acc:
            lastAddr = Addr + ST[2] * bytesPerWord(ST[1])
            File.write('wire %s_ram_sel = rsel &&  (mpaddr[%d:0]>=\'h%x) && (mpaddr[%d:0]<\'h%x);\n'%(Reg,W1,Addr,W1,lastAddr))
            File.write('reg %s_wr_pulse_reg; always @(posedge clk)  %s_wr_pulse_reg <= rwrite &&  %s_ram_sel;\n'%(Reg,Reg,Reg))
            File.write('assign %s_wr_pulse = %s_wr_pulse_reg;\n'%(Reg,Reg))
            File.write('assign %s_rd_pulse = !write &&  %s_ram_sel;\n'%(Reg,Reg))
            File.write('always @(posedge clk)  %s_addr <= mpaddr-\'h%x;\n'%(Reg,Addr))
        if 'external' in Acc:
            lastAddr = Addr + Wid/8
            if Wid>32:
                File.write('wire %s_wr_sel = rwrite && rsel &&  (mpaddr[%d:0]>=\'h%x) && (mpaddr[%d:0]<\'h%x);\n'%(Reg,W1,Addr,W1,lastAddr))
            else:
                File.write('wire %s_wr_sel = rwrite && rsel &&  (mpaddr[%d:0]==\'h%x);\n'%(Reg,W1,Addr))
            File.write('reg %s_wr_pulse_reg; assign %s_wr_pulse = %s_wr_pulse_reg;\n'%(Reg,Reg,Reg))
            File.write('always @(posedge clk)  %s_wr_pulse_reg <= %s_wr_sel;\n'%(Reg,Reg))
            if Wid>32:
                File.write('always @(posedge clk)  %s_addr <= mpaddr-\'h%x;\n'%(Reg,Addr))
        if 'pulse' in Acc:
            if writable(Acc):
                File.write('reg %s_wr_pulse_reg; always @(posedge clk)  %s_wr_pulse_reg <= rwrite && rsel &&  (mpaddr[%d:0]==\'h%x);\n'%(Reg,Reg,W1,Addr))
                File.write('reg %s_pulse_reg; always @(posedge clk) %s_pulse_reg <=  %s_wr_pulse_reg ;\n'%(Reg,Reg,Reg))
                File.write('assign %s_pulse = %s_pulse_reg ;\n'%(Reg,Reg))
            else:    
                File.write('reg %s_rd_pulse_reg; always @(posedge clk)  %s_rd_pulse_reg <= !rwrite && rsel &&  (mpaddr[%d:0]==\'h%x);\n'%(Reg,Reg,W1,Addr))
                File.write('assign %s_pulse =  penable && %s_rd_pulse_reg ;\n'%(Reg,Reg))
#                File.write('assign %s_pulse = !pwrite &&  psel &&  (mpaddr[%d:0]==\'h%x);\n'%(Reg,W1,Addr))

    File.write('endmodule\n')

def writeFlops(File,Reset,LL,Csv,W1):
    File.write('always @(posedge clk %s) begin\n    if (!rst_n) begin\n'%Reset)
    for Add,Reg in LL:
        ST = Csv.regs[Reg]
        
        Wid = int(ST[1])
        Acc = ST[0]
        if type(ST[2])==types.IntType:
           Def = ST[2]
        else:
           Def = eval(ST[2])
        if writable(Acc) and (ST[5]=='false'):
            File.write('        %s <= %d\'h%x;\n'%(Reg,Wid,Def))
    File.write('    end else if (rwrite && rsel)  begin\n')
    for Add,Reg in LL:
        ST = Csv.regs[Reg]
        Wid = int(ST[1])
        Acc = ST[0]
        Addr = int(ST[3])& 0xfffc
        if writable(Acc) and  (ST[5]=='false'):
            if (Wid<2):
                File.write('        if (mpaddr[%d:0]==\'h%x) %s <= wdata[0];\n'%(W1,Addr,Reg))
            elif (Wid<=8):
                File.write('        if (mpaddr[%d:0]==\'h%x) %s <= wdata[7:0];\n'%(W1,Addr,Reg))
            elif (Wid<=32):
                Wdata = '(%s[%d:0] & ~mask[%d:0]) | (wdata &mask)'%(Reg,Wid-1,Wid-1) 
                File.write('        if (mpaddr[%d:0]==\'h%x) %s <= %s;\n'%(W1,Addr,Reg,Wdata))
            else:

                Many,Add = Wid/32,Wid%32
                Many += (Add>0)
                for X in range(Many):
                    Wdata = '(%s[%d:%d] & ~mask[31:0]) | (wdata &mask)'%(Reg,X*32+31,X*32) 
                    File.write('        if (mpaddr[%d:0]==\'h%x) %s[%d:%d] <= %s;\n'%(W1,Addr+4*X,Reg,X*32+31,X*32,Wdata))

    File.write('    end \n')
    File.write('end \n')

def writeLatches(File,Reset,LL,Csv,W1):    
    File.write('always @(*) begin\n    if (!rst_n) begin\n')
    for Add,Reg in LL:
        ST = Csv.regs[Reg]
        
        Wid = int(ST[1])
        Acc = ST[0]
        if type(ST[2])==types.IntType:
           Def = ST[2]
        else:
           Def = eval(ST[2])
        if writable(Acc) and (ST[5]=='true'):
            File.write('        %s = %d\'h%x;\n'%(Reg,Wid,Def))
    File.write('    end else if (rwrite && rsel)  begin\n')
    for Add,Reg in LL:
        ST = Csv.regs[Reg]
        Wid = int(ST[1])
        Acc = ST[0]
        Addr = int(ST[3])& 0xfffc
        if writable(Acc) and  (ST[5]=='true'):
            if (Wid<2):
                File.write('        if (mpaddr[%d:0]==\'h%x) %s = wdata[0];\n'%(W1,Addr,Reg))
            elif (Wid<=8):
                File.write('        if (mpaddr[%d:0]==\'h%x) %s = wdata[7:0];\n'%(W1,Addr,Reg))
            elif (Wid<=32):
                Wdata = '(%s[%d:0] & ~mask[%d:0]) | (wdata &mask)'%(Reg,Wid-1,Wid-1) 
                File.write('        if (mpaddr[%d:0]==\'h%x) %s = %s;\n'%(W1,Addr,Reg,Wdata))
            else:

                Many,Add = Wid/32,Wid%32
                Many += (Add>0)
                for X in range(Many):
                    Wdata = '(%s[%d:%d] & ~mask[31:0]) | (wdata &mask)'%(Reg,X*32+31,X*32) 
                    File.write('        if (mpaddr[%d:0]==\'h%x) %s[%d:%d] = %s;\n'%(W1,Addr+4*X,Reg,X*32+31,X*32,Wdata))

    File.write('    end \n')
    File.write('end \n')



STRING0 = '''            
reg apb_write;
reg [1:0] wsize;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        apb_write <= 1'b0;
        waddr <= 0;
        wsize <= 0;
    end else begin
        apb_write <= psel && pwrite;
        waddr <= mpaddr;
        wsize <= psize;
    end
end
wire [31:0] mask = (wsize==1) ? 32'hff : (wsize==2) ? 32'hffff :  32'hffffffff;
wire [31:0] wdata = (wsize==1) ? {4{pwdata[7:0]}} : (wsize==2) ? {2{pwdata[15:0]}} :  pwdata;
'''










def writable(Acc):
    if 'w' in Acc: return True
    if 'W' in Acc: return True
    return False

def dumpAdaCsv(FFF,Addrs,Csv,Chip='result'):
    Fout = open('%s.csv'%Chip,'w')
    Fdef = open('%s.defines'%Chip,'w')
    Fincv = open('%s.vh'%Chip,'w')
    Fccc = open('%s.h'%Chip,'w')
    Fout.write('NAME,ADDRESS,BITS,DEFAULT,FIELD NAME,,ACCESS,DESCRIPTION\n')
    Addrs.sort()
    for Addr,Reg in Addrs:
        Acc = Csv.regs[Reg][0]
        Fout.write('%s,%s'%(Reg,hex(Addr)))
        Fdef.write('define %s 0x%x\n'%(Reg,Addr))
        Fincv.write('parameter %s  = \'h%x;\n'%(Reg,Addr))
        Fccc.write('#define  ADDR_%s  0x%x\n'%(string.upper(Reg),Addr))
        if Csv.fields[Reg]==[]:
            Wid = int(Csv.regs[Reg][1])
            Def = Csv.regs[Reg][2]
            if len(Csv.regs[Reg])>=5:
                Desc = Csv.regs[Reg][4]
            else:
                Desc = ''
            Fout.write(',%s,%s,%s,,%s,"%s"\n'%(widi(Wid-1,0),defi(Def),Reg,Acc,string.replace(string.replace(Desc,'.',' '),'"','')))
            if Wid<32:
                Fout.write(',,%s,%s,%s,,RO\n'%(widi(31,Wid),0,'RSRVD'))
        else:
            Pref=''
            High=0
            for Wid,Def,Field,Desc in Csv.fields[Reg]:
                HiLo = FFF[(Reg,Field)]
                if type(HiLo)==types.TupleType:
                    WW = '[%s:%s]'%(HiLo)
                    High = HiLo[0]+1 
                else:
                    WW = '[%s]'%HiLo
                    High = HiLo+1 
                Desc = string.replace(string.replace(Desc,'.',' '),'"','')
                Fout.write('%s,%s,%s,%s,,%s,%s\n'%(Pref,WW,Def,Field,Acc,Desc))
                Pref=','
            if High<32:
                Fout.write(',,[%s:%s],%s,%s,,RO\n'%(31,High,0,'RSRVD'))

    Fout.close()
    Fdef.close()
    Fincv.close()


def widi(Wid,From):
    if Wid==1:
        return '[%s]'%From
    return '[%s:%s]'%(Wid,From)

def defi(Def):
    if Def=='': return 0
    return Def

def ensure_dir(Dir):
    if not os.path.exists(Dir):
        os.system('mkdir %s'%Dir)

def extract_base_name(Fname):
    ww = string.split(Fname,'/')
    Fname1 = ww[-1]
    ww = string.split(Fname1,'.')
    return ww[0]

def produce_csv_from_xls(Fname):
    if not XLS_PRESENT:
        print 'no xls parser found, call ilia'
        return
    
    xls2csv.workOnAll([Fname])
    ensure_dir('misc')
    Cell = extract_base_name(Fname)
    Foutnamne = 'misc/mid_%s.csv'%(Cell)
    os.system('/bin/mv %s.csv %s'%(Cell,Foutnamne))
    return Foutnamne

def starts_with(Str,Pattern):
    Len = len(Pattern)
    if len(Str)<Len:
        return False
    return Str[:Len]==Pattern

def ensure_is_int(Param,Wid):
    if type(Wid)==types.IntType:
        return
    print 'strange parameter for %s. expecting int got %s "%s"'%(Param,type(Wid),Wid)
    traceback.print_stack()
    sys.exit()

def buildRegfile(txt,Regfile):
    File = open(Regfile)
    lines = File.readlines()
    File.close()
    state='idle'
    for line in lines:
        wrds = string.split(line)
        if wrds==[]:
            pass
        elif wrds[0]=='reg':
            txt.addReg(wrds[1:])
        elif wrds[0]=='field':
            txt.addField(wrds[1:])
        elif wrds[0]=='array':
            txt.addArray(wrds[1:])
        elif wrds[0]=='ram':
            txt.addRam(wrds[1:])
        elif wrds[0]=='end':
            pass
        elif wrds[0]=='chip':
            txt.Chip = wrds[1]
            if len(wrds)>2: 
                txt.ResetMode = wrds[2]
            else:
                txt.ResetMode=='async'
            if txt.ResetMode=='async':
                txt.Reset = 'or negedge rst_n'
            else:
                txt.Reset = ''
                

        elif wrds[0][0]=='#':
            pass
        elif wrds[0][0]=='/':
            pass
        else:
            logs.log_error('keyword not used "%s"'%(wrds[0]))

class itemClass:
    def __init__(self,Name,Kind,Params):
        self.Name=Name
        self.Kind=Kind
        self.Params=Params
        if 'reset' not in Params:
            self.Params['reset']='0'
        if 'desc' not in Params:
            self.Params['desc']=' '
        if 'latch' not in Params:
            self.Params['latch']='false'
        self.addr=0
    def getParam(self,Param):
        if Param in self.Params: return self.Params[Param]
        print '>>>param %s is not in Params=%s'%(Param,self.Params)
        return '0'
    def csv(self,Fout):
        if self.Kind=='reg':
            self.checkParams()
            Fout.write('reg,%s,,%s,,%s,%s,,"%s",%s\n'%(self.Name,self.Params['access'],self.getParam('wid'),self.Params['reset'],self.Params['desc'],self.Params['latch']))
        elif self.Kind=='field':
            Fout.write(',,%s,%s,,%s,%s,,"%s"\n'%(self.Name,'',self.Params['wid'],self.Params['reset'],self.Params['desc']))
        elif self.Kind=='ram':
            Fout.write('ram,%s,%s,,,%s,,%s"%s"\n'%(self.Name,'',self.Params['wid'],self.Params['amount'],self.Params['desc']))
        elif self.Kind=='array':
            Fout.write('array,%s,%s,,,%s,,%s"%s"\n'%(self.Name,'',self.Params['wid'],self.Params['amount'],self.Params['desc']))
        else:
            logs.log_error('untreated kind "%s"'%self.Kind)

    def checkParams(self):
        if (self.Kind not in mustParams)or(self.Kind not in listedParams):
            logs.log_error('untreated kind "%s"'%self.Kind)
            return
            
        for Prm in mustParams[self.Kind]:
            if Prm not in self.Params: 
                logs.log_error('missing param "%s" in  "%s" %s '%(Prm,self.Name,self.Kind))
        for Prm in self.Params:
            if Prm not in listedParams[self.Kind]:
                logs.log_error('extra param "%s" in  "%s" %s '%(Prm,self.Name,self.Kind))

    def dump(self):
        logs.log_info('item %s addr=%x %s %s'%(self.Name,self.addr,self.Kind,self.Params))
    def nextAddr(self):
        if self.Kind=='reg':
            if self.Params['wid']<=32: return self.addr+4
            Many = Item.Params['wid'] / 32
            Residue = Item.Params['wid'] % 32
            if Residue!=0: Many += 1
            if self.Params['wid']<=64: return self.addr+Many*4
        if self.Kind=='array':
            if self.Params['wid']>32:
                logs.log_error('width of array %s = %d'%(self.Name,self.Params['wid']))
            Many = self.Params['amount']
            return Many*4 + self.addr
        if self.Kind=='ram':
            if self.Params['wid']<=32:
                Many = self.Params['amount']
                return Many*4 + self.addr
        logs.log_error('cannot determine address of %s %s %s'%(self.Name,self.Kind,self.Params))            
        return 4 + self.addr

class txtRegClass:
    def __init__(self):
        self.items=[]
        self.Chip = 'regfile'
        self.ResetMode = 'async'

    def assignRegWidByFields(self):
        curReg = False
        Wid=0
        Reset = 0
        for Item in self.items:
#            print '>>>',curReg,Item.Kind,Item.Params
#            if (Item.Kind=='reg')and('wid' not in Item.Params):
#                if curReg: logs.log_error('widthless register %s'%curReg.Name)
#                curReg = Item
#                print '>>xxxx>',curReg,Item.Kind,Item.Params
            if (Item.Kind=='reg')and('wid' in Item.Params):
                curReg = Item
                Wid = curReg.Params['wid']
                if curReg and (Wid==0): logs.log_error('widhless register %s'%curReg.Name)
                elif (curReg):
                    curReg.Params['wid']=Wid
                    curReg.Params['reset']=Reset
            elif (Item.Kind=='field'):
                if not curReg: logs.log_error('field without register %s'%Item.Name)
                if 'reset' in Item.Params:
                    Rst = Item.Params['reset']
                    if Rst=='': Rst=0
                else:
                    Rst = 0
                Incr = Item.Params['wid']
#                print 'reset %x wid=%d rst=%x  %s'%(Reset,Wid,Rst,type(Rst))
#                Reset = Reset + (eval(Rst)<<Wid)
#                print 'reset2 %x wid=%d rst=%x  %s'%(Reset,Wid,Rst,type(Rst))
                Wid += Incr


        if curReg:
            curReg.Params['wid']=Wid
            curReg.Params['reset']=Reset

    def createCsvFile(self):
#        print 'len',len(self.items)
        Fout = open('temp_%s.csv'%self.Chip,'w')
        Fout.write('kind,name,field,access,addr,wid,reset,amount,description,\n')
        Fout.write('module,%s,,,,,,\n'%self.Chip)
        for Item in self.items:
            Item.csv(Fout)
        Fout.close()
        self.csvFileName = 'temp_%s.csv'%self.Chip

    def assignAddrs(self):
        Addr=0
        for Item in self.items:
            Item.addr=Addr
            Addr = Item.nextAddr()
        self.lastAddr=Addr

    def dump(self):
        self.assignAddrs()
        logs.log_info('txtregsclass dump')
        for Item in self.items:
            Item.dump()

    def addField(self,wrds):
        Name = wrds[0]
        Params = getParams(wrds[1:])
        item = itemClass(wrds[0],'field',Params)
        self.items.append(item)
    def addReg(self,wrds):
        Name = wrds[0]
        Params = getParams(wrds[1:])
        item = itemClass(wrds[0],'reg',Params)
        self.items.append(item)

    def addRam(self,wrds):
        Name = wrds[0]
        Params = getParams(wrds[1:])
        item = itemClass(wrds[0],'ram',Params)
        self.items.append(item)

    def addArray(self,wrds):
        Name = wrds[0]
        Params = getParams(wrds[1:])
        item = itemClass(wrds[0],'array',Params)
        self.items.append(item)








def getParams(wrds):
    Params={}
    for wrd in wrds:
        ww = string.split(wrd,'=')
        if len(ww)==2:
            Var = ww[0]
            try:
                Val = eval(ww[1])
            except:
                Val = ww[1]
            Params[Var]=Val
        else:
            logs.log_error('strange param "%s"'%(wrd))
    return Params


def dumpRdl(txt):
    File = open('%s.rdl'%txt.Chip,'w')
    File.write('addrmap %s {\n'%(txt.Chip))
    Fields={}
    Curreg = False
    for Item in txt.items:
        if Item.Kind=='reg':
            Fields[Item.Name]=[]
            Curreg = Item.Name
        if Item.Kind=='field':
            Fields[Curreg].append(Item)
            
    for Item in txt.items:
        if Item.Kind=='ram':
            File.write('reg %s_ram {\n'%Item.Name)
            File.write('    name = "%s ram ";\n'%Item.Name)
            File.write('    desc = "%s   %s x %d ";\n'%(getPrm(Item.Params,'desc','---'),getPrm(Item.Params,'wid',32),getPrm(Item.Params,'amount',32)))
            File.write('    field {sw=rw; hw=rw; } nn[%d:0];\n'%(Item.Params['wid']-1))
            File.write('};\n')
            File.write('external %s_ram %s[%d] ;\n'%(Item.Name,Item.Name,Item.Params['amount']))
        elif (Item.Kind=='reg')and(Fields[Item.Name]!=[]):
            File.write('reg %s_reg {\n'%Item.Name)
            File.write('    name = "%s register";\n'%Item.Name)
            File.write('    desc = "%s";\n'%getPrm(Item.Params,'desc','---'))
            FF = Fields[Item.Name]
            Pos=0
            for Fil in FF:
                Last = Pos + Fil.Params['wid'] 
                File.write('    field {sw=%s; hw=%s; %s } %s[%d:%d] = %s;\n'%(swAcc(Item.Params),hwAcc(Item.Params),specials(Item.Params),Fil.Name,Last-1,Pos,getPrm(Fil.Params,'reset',0)))
                Pos = Last
            File.write('};\n')
                
        elif (Item.Kind=='reg')and(Item.Params['wid']>64):
            File.write('reg %s_reg {\n'%Item.Name)
            File.write('    name = "%s register";\n'%Item.Name)
            File.write('    desc = "%s";\n'%getPrm(Item.Params,'desc','---'))
            File.write('    field {sw=%s; hw=%s; %s } nn[%d:0] = %s;\n'%(swAcc(Item.Params),hwAcc(Item.Params),specials(Item.Params),31,getPrm(Item.Params,'reset',0)))
            File.write('};\n')
            Many = Item.Params['wid'] / 32
            Residue = Item.Params['wid'] % 32
            if Residue!=0: Many += 1
            File.write('%s_reg %s[%d];\n'%(Item.Name,Item.Name,Many))
        elif (Item.Kind=='reg')and(Item.Params['wid']>32):
            File.write('reg %s_reg {\n'%Item.Name)
            File.write('    name = "%s register";\n'%Item.Name)
            File.write('    desc = "%s";\n'%getPrm(Item.Params,'desc','---'))
            File.write('    field {sw=%s; hw=%s; %s } nn[%d:0] = %s;\n'%(swAcc(Item.Params),hwAcc(Item.Params),specials(Item.Params),31,getPrm(Item.Params,'reset',0)))
            File.write('};\n')
            File.write('%s_reg %s_lo;\n'%(Item.Name,Item.Name))
            File.write('%s_reg %s_hi;\n'%(Item.Name,Item.Name))
        elif (Item.Kind=='reg')and(Item.Params['wid']<=32):
            File.write('reg %s_reg {\n'%Item.Name)
            File.write('    name = "%s register";\n'%Item.Name)
            File.write('    desc = "%s";\n'%getPrm(Item.Params,'desc','---'))
            File.write('    field {sw=%s; hw=%s; %s } nn[%d:0] = %s;\n'%(swAcc(Item.Params),hwAcc(Item.Params),specials(Item.Params),Item.Params['wid']-1,getPrm(Item.Params,'reset',0)))
            File.write('};\n')
            File.write('%s_reg %s;\n'%(Item.Name,Item.Name))
        elif Item.Kind=='field':
            pass
        elif Item.Kind=='array':
            pass
        else:
            logs.log_error('strange item %s %s'%(Item.Name,Item.Kind))





    File.write('};\n')
    File.close()

def specials(Params):
    if ('w' in Params['access']) and('pulse' in Params['access']): return 'singlepulse;'
    if 'pulse' in Params['access']: return 'software_access;'
    return ''

def swAcc(Params):
    if 'w' in Params['access']: return 'wr'
    return 'r'

def hwAcc(Params):
    if 'w' in Params['access']: return 'r'
    return 'w'

def getPrm(Params,Prm,Def):
    if Prm in Params: return Params[Prm]
    return Def

def bytesPerWord(Bits):
    if Bits<=8: return 1
    if Bits<=16: return 2
    if Bits<=32: return 4

main()



