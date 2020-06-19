import string
import logs



LINES = {0:[],1:[],2:[],3:[],4:[],5:[]}
def dumpApb(Db):
    from regfile3 import getPrm,expandBits
    Module = Db['chip'].Params['names'][0] 
    Str = string.replace(HEADER,'MODULE',Module)
    File = open('%s.v'%Module,'w')
    File.write(Str)
    Db['module']=Module

    for Reg in Db['regs']:
        if Reg.Kind=='reg':
            treatReg(Reg)
        elif Reg.Kind=='array':
            treatArray(Reg)
        elif Reg.Kind=='ram':
            treatRam(Reg)
        elif Reg.Kind=='gap': 
            pass
        else:
            logs.log_error('wrong kind %s'%(Reg.Kind,Reg.Params.Names))
    
    for Line in LINES[0]:
        File.write('%s\n'%Line)

    Base = getPrm(Db['chip'],'base',0)
    X = logs.neededBits(Db['chip'].Addr-Base)
    Mask = ((1<<X)-1) & 0xfffc
    Str = string.replace(STRING0,'MASK',hex(Mask)[2:])
    Str = string.replace(Str,'BASE',hex(Base)[2:])
    File.write('%s\n'%Str)

    for Line in LINES[1]:
        File.write('%s\n'%Line)
    File.write("    32'hx;\n")
    Str = Db['chip'].RAMS_WIRES + '\n' + string.replace(STRING1,'RAMS',Db['chip'].RAMS)
    RST = getPrm(Db['chip'],'reset','async')
    if RST=='async':
        Str = string.replace(Str,'ASYNCRST','or negedge rst_n')
    else:
        Str = string.replace(Str,'ASYNCRST','')
    File.write('%s\n'%Str)
    for Line in LINES[2]:
        File.write('%s\n'%Line)

    File.write('    end else if (apb_write && penable)  begin\n')
    for Line in LINES[3]:
        File.write('%s\n'%Line)

    File.write('    end\n')
    File.write('end\n')

    for Line in LINES[4]:
        File.write('%s\n'%Line)


    File.write('endmodule\n')
    File.close()

ROPULSE = '''
wire REG_rd_sel = !pwrite && psel &&  (mpaddr=='hADDR);
reg REG_rd_pulse_reg; always @(posedge clk)  REG_rd_pulse_reg <= REG_rd_sel;
assign REG_pulse = REG_rd_pulse_reg  && penable;
'''
RWPULSE = '''
wire REG_wr_sel = pwrite && psel &&  (mpaddr=='hADDR);
reg REG_wr_pulse_reg; always @(posedge clk)  REG_wr_pulse_reg <= REG_wr_sel;
assign REG_pulse = REG_wr_pulse_reg  && penable;
'''

RAM_ROPULSE_RANGE = '''
assign REG_rd_pulse = !pwrite && psel &&  (mpaddr>='hLADDR) && (mpaddr < 'hHADDR);
reg REG_rd_pulse_dly; always @(posedge clk)  REG_rd_pulse_dly <= REG_rd_pulse;
assign REG_rd_data_valid = REG_rd_pulse_dly && penable;
'''

ROPULSE_RANGE = '''
wire REG_rd_sel = !pwrite && psel &&  (mpaddr>='hLADDR) && (mpaddr < 'hHADDR);
reg REG_rd_pulse_reg; always @(posedge clk)  REG_rd_pulse_reg <= REG_rd_sel;
assign REG_rd_pulse = REG_rd_pulse_reg  && penable;
'''

RWPULSE_RANGE = '''
wire REG_wr_sel = pwrite && psel &&  (mpaddr>='hLADDR) && (mpaddr < 'hHADDR);
reg REG_wr_pulse_reg; always @(posedge clk)  REG_wr_pulse_reg <= REG_wr_sel;
assign REG_wr_pulse = REG_wr_pulse_reg  && penable;
'''



def treatReg(Reg):
    from regfile3 import getPrm,expandBits
    Access= getPrm(Reg,'access','rw')
    Wid= getPrm(Reg,'width',32)
    Reset= getPrm(Reg,'reset',0)
    Name= getPrm(Reg,'names',['err'])[0]
    if 'ro' in Access:
        Line = '    ,input [%d:0] %s'%(Wid-1,Name)
        LINES[0].append(Line)
        if 'pulse' in Access:
            lastAddr = Reg.Addr
            Wid2 = Wid
            while Wid2>32:
                lastAddr += 4
                Wid2 -= 32
            Line = '    ,output %s_pulse'%(Name)
            LINES[0].append(Line)
            Str = string.replace(ROPULSE,'REG',Name)
            Str = string.replace(Str,'ADDR',hex(lastAddr)[2:])
            LINES[4].append(Str)

        if (Wid<32):
            Line = '    (mpaddr == \'h%x) ? %s :'%(Reg.Addr,expandBits(Name,Wid,32))
            LINES[1].append(Line)
        else:
            Wid1 = Wid
            Ad = Reg.Addr
            Hi,Lo = 31,0
            while Wid1>0:
                Line = '    (mpaddr == \'h%x) ? %s[%d:%d] :'%(Ad,expandBits(Name,min(Wid1,32),32),Hi,Lo)
                Wid1 -= 32
                Ad += 4
                Lo += 32
                Hi = min(Wid-1,Hi+32)
                LINES[1].append(Line)

            
    elif 'rw' in Access:
        Line = '    ,output reg [%d:0] %s'%(Wid-1,Name)
        LINES[0].append(Line)
        lastAddr = Reg.Addr
        Wid2 = Wid
        while Wid2>32:
            lastAddr += 4
            Wid2 -= 32
        if 'pulse' in Access:
            Line = '    ,output %s_pulse'%(Name)
            LINES[0].append(Line)
            Str = string.replace(RWPULSE,'REG',Name)
            Str = string.replace(Str,'ADDR',hex(lastAddr)[2:])
            LINES[4].append(Str)
        if Wid<=32:
            Line = '    (mpaddr == \'h%x) ? %s :'%(Reg.Addr,expandBits(Name,Wid,32))
            LINES[1].append(Line)
            Line = '        if (waddr == \'h%x) %s <= (%s & ~mask) | (wdata & mask);'%(Reg.Addr,Name,Name)
            LINES[3].append(Line)
        else:
            Wid1 = Wid
            Ad = Reg.Addr
            Hi,Lo = 31,0
            while Wid1>0:
                Line = '    (mpaddr == \'h%x) ? %s[%d:%d] :'%(Ad,expandBits(Name,min(Wid1,32),32),Hi,Lo)
                LINES[1].append(Line)
                Line = '        if (waddr == \'h%x) %s[%d:%d] <= (%s[%d:%d] & ~mask) | (wdata & mask);'%(Ad,Name,Hi,Lo,Name,Hi,Lo)
                LINES[3].append(Line)
                Ad += 4
                Lo += 32
                Wid1 -= 32
                Hi = min(Wid-1,Hi+32)


        Line = '        %s <= %d\'h%x;'%(Name,Wid,Reset)
        LINES[2].append(Line)

    elif 'external' in Access:
        Line = '    ,input [%d:0] %s'%(Wid-1,Name)
        LINES[0].append(Line)
        Line = '    ,output %s_rd_pulse'%(Name)
        LINES[0].append(Line)
        Line = '    ,output %s_wr_pulse'%(Name)
        LINES[0].append(Line)
        Str = string.replace(ROPULSE,'assign REG','assign %s_rd'%Name)
        Str = string.replace(Str,'REG',Name)
        Str = string.replace(Str,'ADDR',hex(Reg.Addr)[2:])
        LINES[4].append(Str)
        Str = string.replace(RWPULSE,'assign REG','assign %s_rd'%Name)
        Str = string.replace(Str,'REG',Name)
        Str = string.replace(Str,'ADDR',hex(Reg.Addr)[2:])
        LINES[4].append(Str)

def treatArray(Reg):
    Access = getPrm(Reg,'access','rw')
    Wid = getPrm(Reg,'width',32)
    Dep = getPrm(Reg,'depth',32)
    Name= getPrm(Reg,'names',['err'])[0]
    if 'external' in Access:
        Line = '    ,input [%d:0] [%d:0] %s'%(Dep-1,Wid-1,Name)
        LINES[0].append(Line)
        Line = '    ,output %s_rd_pulse'%(Name)
        LINES[0].append(Line)
        Line = '    ,output %s_wr_pulse'%(Name)
        LINES[0].append(Line)
        Line = '    ,output [%d:0] %s_addr'%(logs.neededBits(Dep)-1,Name)
        LINES[0].append(Line)

        Str = string.replace(ROPULSE_RANGE,'REG',Name)
        Str = string.replace(Str,'LADDR',hex(Reg.Addr)[2:])
        Str = string.replace(Str,'HADDR',hex(Reg.HADDR)[2:])
        LINES[4].append(Str)
        Str = string.replace(RWPULSE_RANGE,'REG',Name)
        Str = string.replace(Str,'LADDR',hex(Reg.Addr)[2:])
        Str = string.replace(Str,'HADDR',hex(Reg.HADDR)[2:])
        LINES[4].append(Str)

    elif ('wr' in Access)or('rw' in Access):
        Line = '    ,output reg [%d:0] [%d:0] %s'%(Dep-1,Wid-1,Name)
        LINES[0].append(Line)
        Ad = Reg.Addr
        for Ind in range(Dep):
            Line = '    (mpaddr == \'h%x) ? %s :'%(Ad,expandBits(Name+'[%d]'%Ind,Wid,32))
            Ad += 4
            LINES[1].append(Line)


        Line = '        %s <= %d\'h%x;'%(Name,Wid,Reset)
        LINES[2].append(Line)

    elif ('ro' in Access):
        Line = '    ,input [%d:0] [%d:0] %s'%(Dep-1,Wid-1,Name)
        LINES[0].append(Line)
        Ad = Reg.Addr
        for Ind in range(Dep):
            Line = '    (mpaddr == \'h%x) ? %s :'%(Ad,expandBits(Name+'[%d]'%Ind,Wid,32))
            Ad += 4
            LINES[1].append(Line)
    return

def treatRam(Reg):
    Access = getPrm(Reg,'access','rw')
    Wid = getPrm(Reg,'width',32)
    Dep = getPrm(Reg,'depth',32)
    Name= getPrm(Reg,'names',['err'])[0]
    Line = '    ,input [%d:0] %s_rdata'%(Wid-1,Name)
    LINES[0].append(Line)
    Line = '    ,output [%d:0] %s_addr'%(logs.neededBits(Dep-1),Name)
    LINES[0].append(Line)
    Line = '    ,output %s_rd_pulse'%(Name)
    LINES[0].append(Line)
    Line = '    ,output %s_wr_pulse'%(Name)
    LINES[0].append(Line)

    Line = 'assign %s_addr = (mpaddr - \'h%x)>>2;'%(Name,Reg.Addr)
    LINES[4].append(Line)
    Str = string.replace(RAM_ROPULSE_RANGE,'REG',Name)
    Str = string.replace(Str,'LADDR',hex(Reg.Addr)[2:])
    Str = string.replace(Str,'HADDR',hex(Reg.HADDR)[2:])
    LINES[4].append(Str)
    Str = string.replace(RWPULSE_RANGE,'REG',Name)
    Str = string.replace(Str,'LADDR',hex(Reg.Addr)[2:])
    Str = string.replace(Str,'HADDR',hex(Reg.HADDR)[2:])
    LINES[4].append(Str)

    Line = '%s_rd_data_valid ? %s_rdata :'%(Name,Name)
    Db['chip'].RAMS += Line
    Db['chip'].RAMS_WIRES += 'wire %s_rd_data_valid;'%Name



HEADER = '''module MODULE (
    input clk,input rst_n,input pwrite, input psel, input [3:0] pstrb, output pready,input penable
    ,output reg pslverr, input [1:0] psize, input [31:0] pwdata, output [31:0] prdata
    ,input [15:0] paddr ,output reg [15:0] waddr,output reg [31:0] last_wdata
'''

STRING0 = ''' 
);
wire [15:0] mpaddr = (paddr - 16'hBASE) & 16'hMASK;
assign pready = 1;
wire [31:0] prdata_wire =
'''

STRING1 = ''' 

reg [31:0] prdata_reg;
always @(posedge clk) prdata_reg <=  prdata_wire;
assign prdata =   RAMS
   prdata_reg;

reg apb_write;
reg [1:0] wsize;
always @(posedge clk ASYNCRST) begin
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
always @(posedge clk) if (apb_write && penable) last_wdata <= pwdata;
always @(posedge clk ASYNCRST) begin
    if (!rst_n) begin ''' 


