#! /usr/bin/env python3

import os,sys,string

import logs

import xml_regfile2_create
import regfile_html

def main():
    Fname = sys.argv[1]
    run(Fname)

def run(Fname,Dirx='.'):
    global Dir
    Dir = Dirx
    File = open(Dirx + '/' +Fname)
    readFile(File)
    
    computeWidthFromFields()
    treatFields()
    assignAddresses()
    Prmx = Db['chip'].Params
    Params = Db['chip'].Params['names']
    if 'bus' in Prmx:
        Params.append(Prmx['bus'])

    Module = Params[0] 
    Db['module']=Module
    Db['dir']=Dirx
    Db['lines'] = LINES
    if 'apb' in Params:
        dumpApb(Db)
    elif 'ram' in Params:
        Db['fout'].close()
    else:
        logs.log_error('need to specify output format:  apb ram')
    dumpDefines()
    runXml()
#    report()
#    report2(LINES)
    if LINES[8]!=[]:
        Fspl = open('%s.splits'%Module,'w')
        for Line in LINES[8]:
            Fspl.write(Line+'\n')
        Fspl.close()
    return Db['module']

def report2(LINES):
    for Key in LINES:
        LL = LINES[Key]
        for Li in LL:
            logs.log_info('%s: %s'%(Key,Li))

Db = {'items':[],'clocks':[],'regs':[],'fields':[]}

def createLines(File):
    Lines = File.readlines()
    Long = ''
    for line in Lines:
        if '//' in line: line = line[:line.index('//')]
        elif '#' in line: line = line[:line.index('#')]
        else:
            line = line[:-1]
        Long += line + ' ;;; '
    Wrds = Long.split()
    Res = []
    state = 'idle'
    for Wrd in Wrds:
        if state=='idle':
            if ('"' in Wrd)and(Wrd[-1]!='"'):
                Acc = Wrd
                state = 'work'
            else:
                Res.append(Wrd)
        elif state=='work':
            Acc += ' '+Wrd
            if Wrd.endswith('"'):
                state = 'idle'
                Acc = Acc.replace(';;;','\n')
                Res.append(Acc)
    Res2 = []
    while ';;;' in Res:
        X = Res.index(';;;')
        Head = Res[:X]
        Res = Res[X+1:]
        if Head!=[]:
            Res2.append(Head)
    return Res2        


checkNames = {}
def readFile(File):
    Lines = createLines(File)  
    Lines = treatTemplates(Lines)
    for wrds in Lines:
        if (wrds[0]=='end'):
            generate()
            return
        elif (wrds[0]=='chip'):
            Db['chip'] = itemClass(wrds)
        else:
            Item = itemClass(wrds)
            Db['items'].append(Item)
            Kind = Item.Kind
            if len(Item.Params['names'])>0:
                Name = Item.Params['names'][0]
                Item.Name = Name
                checkPair(Kind,Name)
            else:
                Item.Name = 'none'

def checkPair(Kind,Name):
    if Kind == 'field': return
    if Kind not in checkNames: 
        checkNames[Kind]=[Name]
        return
    if Name in checkNames[Kind]:
        logs.log_error('double defined item %s of kind %s . previous=%s'%((Name,Kind,checkNames[Kind])))
        return

    checkNames[Kind].append(Name)

def treatTemplates(Lines):
    Templates = {}
    Curr = []
    state = 'idle'
    Result = []
    for Line in Lines:
        if state=='idle':
            if Line[0]=='template':
                Name = Line[1]
                Curr = []
                state = 'work'
            elif Line[0]=='instance':
                Temp = Line[1]
                Inst = Line[2]
                for LL in Templates[Temp]:
                    LX = LL[:]
                    if LX[0]=='reg':
                        LX[1] = Inst+LX[1]
                    Result.append(LX)
            else:
                Result.append(Line)
        elif state=='work':
            if Line[0] == 'endtemplate':
                Templates[Name] = Curr[:]
                state='idle'
            else:
                Curr.append(Line)
    return Result


SYNONYMS = {'wid':'width','desc':'description','rw':'wr','rw_pulse':'wr_pulse'}

class itemClass:
    def __init__(self,Wrds):
        self.Kind = Wrds[0]
        self.Params = getParams(Wrds[1:])
        self.Synonyms()
        self.Addr = -1
        self.RAMS = ''
        self.RAMS_WIRES = ''
    def dump(self):
        print('%s : (%d 0x%x) %s'%(self.Kind,self.Addr,self.Addr,self.Params))
    def Synonyms(self):
        for Key in SYNONYMS:
            if Key in self.Params:
                Val = SYNONYMS[Key]
                if Val not in self.Params:
                    self.Params[Val] = self.Params[Key]

def expandBits(Name,Wid,Bits):
    if Wid==Bits: return Name
    if Wid<Bits:
        Line = '{%d\'b0,%s}'%(Bits-Wid,Name)
        return Line
    return 'ERROR%s'%Name

def getParams(wrds):
    Res = {}
    Nn = []
    for wrd in wrds:
        if '=' in wrd:
            ww = wrd.split('=')
            AA = examine(ww[1])
            Res[ww[0]] = AA
        else:
            Nn.append(wrd)
    Res['names']=Nn
    return Res 

def examine(Txt):
    if logs.startsWith(Txt,'0x'):
        X = Txt.replace('_','')
        return eval(X)
    elif logs.startsWith(Txt,'0b'):
        X = Txt.replace('_','')
        return eval(X)
    elif Txt[0] in '0123456789':
        try:
            return eval(Txt)
        except:
            logs.log_error('examine of "%s" failed'%Txt)
            return 0
    else:
        return Txt

def treatFields():
    DbFields = Db['fields']
    Nc = 0
    for Reg in DbFields:
        Split=True
        RegObj = findObj(Db['regs'],Reg)
        if 'fields' in RegObj.Params:
            Wid = getPrm(RegObj,'width',0)
            if Wid<=1:
                WW = ''
            else:
                WW = '[%s:0]'%(Wid-1)
            LINES[7].append('    ,output %s %s'%(WW,RegObj.Name))
            Split=False
            
        Fields = DbFields[Reg]
        Pos = 0
        Winaccess='gap'
        Access = Fields[0].Params['access']
        for Field in Fields:
            Wid = Field.Params['wid']
            Hi,Lo = Field.Params['position']
            Name = Field.Params['names'][0]
            if 'access' in Field.Params:
                Access = Field.Params['access']
                if Access!='gap':
                    Winaccess = Access

            if Wid<=1:
                WW = ''
            else:
                WW = '[%s:0]'%(Wid-1)

            if outAccess(Access):
                if Split:
                    LINES[7].append('    ,output %s %s'%(WW,Name))
                if ('fields' in RegObj.Params):
                    LINES[8].append('assign %s = %s[%d:%d];'%(Name,Reg,Hi,Lo))
                else:
                    LINES[6].append('assign %s = %s[%d:%d];'%(Name,Reg,Hi,Lo))
            elif inAccess(Access):
                if Split:
                    LINES[7].append('    ,input  %s %s'%(WW,Name))
                if ('fields' in RegObj.Params):
                    LINES[8].append('assign %s[%d:%d] = %s;'%(Reg,Hi,Lo,Name))
                else:
                    LINES[6].append('assign %s[%d:%d] = %s;'%(Reg,Hi,Lo,Name))
            else:
                logs.log_error('fields not legal access %s for %s'%(Access,Name))

def findObj(List,Name):
    for Obj in List:
        if Obj.Name==Name: return Obj
    return False


def generate():
    gatherFields()
    uniquifyFields()

FIELDED_REGS = []    

def uniquifyFields():
    Takens = {}
    for Reg in Db['regs']:
        Name = Reg.Name
        if Name in Db['fields']:
            List = Db['fields'][Name]
            for Field in List:
                Fname = Field.Name
                if Fname in Takens:
                    Takens[Fname].append((Field,Reg))
                else:
                    Takens[Fname] = [(Field,Reg)]
    for Fname in Takens:
        List = Takens[Fname]
        if len(List)>1:
            logs.log_info('duplicate fields %s. uniquifying'%Fname)
            for Field,Reg in List:
                if 'suffix' in Reg.Params:
                    Suff = Reg.Params['suffix']
                    Newname = Fname+Suff
                elif 'prefix' in Reg.Params:
                    Pref = Reg.Params['prefix']
                    Newname = Pref+Fname
                else:
                    Newname = Reg.Name+'_'+Fname
                Field.Name = Newname
                Field.Params['names'][0] = Newname
               
            
        


def gatherFields():
    Active = False
    Obj = False
    Db['fields'] = {}
    Db['regs'] = []
    for Reg in Db['items']:
        if Reg.Kind=='reg':
            Active = Reg.Params['names'][0]
            Obj = Reg
            Reg.Name = Active
            Db['regs'].append(Reg)
        elif Reg.Kind=='field':
            if Active:
                if ('access' not in Reg.Params) or ( Reg.Params['access']!='gap'):
                    Reg.Params['access'] = Obj.Params['access']
                Nreg = Obj.Params['names'][0]
                if Nreg not in FIELDED_REGS: FIELDED_REGS.append(Nreg)
                if Active not in Db['fields']:
                    Db['fields'][Active] = [Reg]
                else:
                    Db['fields'][Active].append(Reg)
                Reg.Name = Reg.Params['names'][0]
            else:
                logs.log_error('no reg for field %s'%(Reg.Params))
        else:
            Db['regs'].append(Reg)
            Active=False

def report():
    logs.mustKey(Db,'chip')
    logs.mustKey(Db,'regs')
    print(Db['chip'].Kind,Db['chip'].Params)
    for Reg in Db['regs']:
        Reg.dump()

ALIASES = {'empty':'default'}
def getPrm(Obj,Name,Default):
    if Name in Obj.Params: return Obj.Params[Name]
    if Name in ALIASES:
        return getPrm(Obj,ALIASES[Name],Default)
    return Default

def computeWidthFromFields():
    Db['splits'] = {}
    Db['splitsw'] = {}
    for Reg in Db['regs']:
        Name= Reg.Name
        if (Name!='none') and(Reg.Kind in ['reg','array','ram']):
            Name = Reg.Name

            OrigWid= getPrm(Reg,'width',0)
            Ptr = 0
            Wid = 0
            Map = []
            if Name in Db['fields']:
                List = Db['fields'][Name]
                for Obj in List:
                    Name= getPrm(Obj,'names',['err'])[0]
                    Obj.Name = Name
                    Add0 = getPrm(Obj,'width',0)
                    Add = getPrm(Obj,'width',0)
                    if Add==0:
                        logs.log_error('reg %s field %s has no width'%(Name,Obj.Name))
                    Align = getPrm(Obj,'align',0)
                    if (Align>0):
                       if (Align<=Add):
                          logs.log_error('field %s of reg %s has bith width and align. align is smaller.'%(Obj.Name,Name))
                       else:
                          Add = Align
                          Db['splits'][Reg.Name] = Reg
                    Obj.Params['position'] = (Wid+Add0-1,Wid)
                    while (len(Map)<(Wid+Add0)): Map.append('0')
                    for X in range(Wid+Add0-1,Wid-1,-1):
                        Map[X] = '1'
                        

                    Wid += Add
                if OrigWid==0:
                    Reg.Params['width']=Wid
                elif (OrigWid<Wid):
                    logs.log_error('fields of reg %s (wid=%d) take more bits (%d)'%(Reg.Name,OrigWid,Wid))
                if Reg.Name in Db['splits']:
                    Db['splitsw'][Reg.Name]=Map
            if (OrigWid==0)and( getPrm(Reg,'width',0)==0):
                logs.log_error('reg %s has no width and no fields (defined %s)'%(Name,list(Db['fields'].keys())))
            



def assignAddresses():
    Chip = Db['chip']
    Addr = getPrm(Chip,'base',0)
    Addr,HADDR = 0,0
    for Reg in Db['regs']:
        Reg.Addr = Addr
        if Reg.Kind in ['reg','array','ram']:
            Name= getPrm(Reg,'names',['err'])[0]
            LINES[5].append('%s = 0x%x'%(Name,Addr))
            LINES[5].append('ADDR_MAP["%s"] = 0x%x'%(Name,Addr))
        Addr += int(advanceAddr(Reg))
        Reg.HADDR = Addr
    Chip.Addr = Addr
    Chip.HADDR = Addr


def computeWid(Obj):
    Wid = Obj.Params['width']
    AA = Wid/32
    Rest = Wid-(AA*32)
    if Rest>0: AA += 1
    return AA

def bytes(Wid):
    A = Wid/8
    B= (Wid % 8)>0
    return A+B


def simpleAdvanceAddr(Obj):
    if 'width' in Db['chip'].Params:
        Bytes = Db['chip'].Params['width']/8
        busWid = Db['chip'].Params['width']
    else:
        Bytes = 4
        busWid = 32
    if 'width' in Obj.Params:
        Wid = Obj.Params['width']
        Bytes2 = bytes(Wid)
        if Wid<=busWid:
            Add = 1
        else:
            Add = int(round(1.0*Bytes2/Bytes + 0.5))
    return Add*Bytes


def advanceAddr(Obj):
            
    if 'width' in Db['chip'].Params:
        Bytes = Db['chip'].Params['width']/8
        busWid = Db['chip'].Params['width']
        Bytes2 = Bytes
    else:
        Bytes = 4
        busWid = 32
        Bytes2 = 4
    if 'width' in Obj.Params:
        Wid = Obj.Params['width']
        Bytes2 = bytes(Wid)
        if Wid<=busWid:
            Add = 1
        else:
            Add = int(round(1.0*Bytes2/Bytes + 0.5))
#            print('REG','add',Add,'bytes',Bytes,'bytes2',Bytes2,Add*Bytes,Wid,Obj.Params['names'])
    elif (Obj.Kind not in ['gap']):
        logs.log_error('advanceAddr: missing wid in %s %s  defs:%s'%(Obj.Kind,Obj.Name,Obj.Params))
        Add = 4


    if Obj.Kind in ['reg','external']:
        logs.mustKey(Obj.Params,'width')
        return Add*Bytes
    elif Obj.Kind in ('ram'):
        logs.mustKey(Obj.Params,'width')
        logs.mustKey(Obj.Params,'depth')
        if 'modifier' in Obj.Params:
            Modif = Obj.Params['modifier']
            if Modif not in ['internal','dpram','external']:
                logs.log_error('ram mode=%s of %s is not supported (external,internal,dpram) '%(Modif,Obj.Params['names'][0]))
                
        Dep = Obj.Params['depth']
        if (Bytes2<=Bytes):
            return Dep*Bytes
        else:
            logs.log_error('ram %s is not supported to  be wider than bus (%d>%d)'%(Obj.Params['names'][0],Bytes2,Bytes))
            return Bytes * 2 * Dep

            
    elif Obj.Kind in ('array'):
        logs.mustKey(Obj.Params,'width')
        Dep = Obj.Params['depth']
        Tot = Dep*Add*Bytes
        return Tot
    elif Obj.Kind=='gap':
        if 'align' in Obj.Params:
            Align = Obj.Params['align']
            X = int(Obj.Addr/Align)
            Diff = Obj.Addr -(X*Align)
            if Diff==0: return 0
            return (X+1)*Align - Obj.Addr
        elif 'abs' in Obj.Params:
            return Obj.Params['abs']
        else:
            logs.log_error('advanceAddr GAP got %s'%str(Obj.Params))
    else:
        logs.log_error('advanceAddr got %s'%(Obj.Kind))
        return Bytes

INSTANCE = '''
MODULE MODULE (.pclk(pclk),.present(present)
    .pwrite(pwrite),.paddr(paddr),.psel(psel),.penable(penable)
    ,.prdata(prdata),.pwdata(pwdata),.pstrb(pstrb)
    ,.pready(pready),.pslverr(pselverr)
'''




HEADER = '''module MODULE (
    input pclk,input presetn,input pwrite, input pread
    ,input [BUSWID-1:0] pwdata, output [BUSWID-1:0] prdata
    ,input [WSTRB-1:0] pstrb
    ,input [ADDWID-1:0] paddr ,output reg [BUSWID-1:0] last_wdata
'''

STRING0 = '''
);
wire [ADDWID-1:0] mpaddr = (pread||pwrite) ? (paddr - 'hBASE)  : 0;
wire [BUSWID-1:0] prdata_wire =
'''

PSTRB4 = '{{8{pstrb[3]}},{8{pstrb[2]}},{8{pstrb[1]}},{8{pstrb[0]}}}';
PSTRB8 = '{{8{pstrb[7]}},{8{pstrb[6]}},{8{pstrb[5]}},{8{pstrb[4]}},{8{pstrb[3]}},{8{pstrb[2]}},{8{pstrb[1]}},{8{pstrb[0]}}}';


STRING1 = '''

reg [BUSWID-1:0] prdata_reg;
always @(posedge pclk) prdata_reg <=  prdata_wire;
assign prdata =   RAMS
    prdata_reg;

wire [BUSWID-1:0] mask = { PSTRB };
wire [BUSWID-1:0] wdata = pwdata;
always @(posedge pclk) if (pwrite) last_wdata <= wdata & mask;
always @(posedge pclk ASYNCRST) begin
    if (!presetn) begin '''

LINES = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
def dumpRam(Postfix,File):
    Module = Db['chip'].Params['names'][0] 
    try:
        Buswid = Db['chip'].Params['width']
        Addwid = Db['chip'].Params['addrwid']
    except:
        logs.log_error('You need to have width and addrwid in chip line. it is buswidth')
        sys.exit()
    if Buswid==64: Wstrb=8
    if Buswid==32: Wstrb=4
    Str = HEADER.replace('MODULE',Module+Postfix)
    Str = Str.replace('BUSWID',str(Buswid))
    Str = Str.replace('ADDWID',str(Addwid))
    Str = Str.replace('WSTRB',str(Wstrb))
    File.write(Str)
    Db['module']=Module
#    bodyDump0(Db,File)
    for Line in LINES[0]:
        File.write('%s\n'%Line)
    bodyDump1(Db,File)
    return File
    


def bodyDump0(Db):
    for Reg in Db['regs']:
        if Reg.Kind in ['external','reg']:
            treatReg(Reg)
        elif Reg.Kind=='array':
            treatArray(Reg)
        elif Reg.Kind=='ram':
            treatRam(Reg)
        elif Reg.Kind=='gap': 
            pass
        else:
            logs.log_error('wrong kind %s %s'%(Reg.Kind,Reg.Params))
    

def bodyDump1(Db,File):
    Base = getPrm(Db['chip'],'base',0)
    X = logs.neededBits(Db['chip'].Addr-Base)
    Mask = ((1<<X)-1) & 0xfffc
    Buswid = Db['chip'].Params['width']
    Addwid = Db['chip'].Params['addrwid']
    if Buswid==64: Wstrb=8
    if Buswid==32: Wstrb=4
    Str = STRING0.replace('MASK',hex(Mask)[2:])
    Str = Str.replace('BASE',hex(Base)[2:])
    Str = Str.replace('BUSWID',str(Buswid))
    Str = Str.replace('ADDWID',str(Addwid))
    Str = Str.replace('WSTRB',str(Wstrb))
    File.write('%s\n'%Str)

    for Line in LINES[1]:
        File.write('%s\n'%Line)
    Default = getPrm(Db['chip'],'empty',"0xdeaddead")
    if (type(Default) is int):
        Default = hex(Default)[2:]
    elif (type(Default) is str):
        try:
            Default = eval(Default)
        except:
            logs.log_error('#empty of chip (default value for cases) is not a legal integer "%s"'%(Default))
            Default='0; // BAD DEFAULT %s'%Default
            
    File.write("    32'h%s;\n"%Default)
    Str = STRING1.replace('RAMS',Db['chip'].RAMS)
    Str = Str.replace('BUSWID',str(Buswid))
    Str = Str.replace('ADDWID',str(Addwid))
    Str = Str.replace('WSTRB',str(Wstrb))
    if Buswid==64:
        Str = Str.replace('PSTRB',PSTRB8)
    if Buswid==32:
        Str = Str.replace('PSTRB',PSTRB4)

    Str = Db['chip'].RAMS_WIRES + '\n' + Str
    RST = getPrm(Db['chip'],'reset','async')
    if RST=='async':
        Str = Str.replace('ASYNCRST','or negedge presetn')
    else:
        Str = Str.replace('ASYNCRST','')
    File.write('%s\n'%Str)
    for Line in LINES[2]:
        File.write('%s\n'%Line)

    File.write('    end else if (pwrite)  begin\n')
    for Line in LINES[3]:
        Reg = Line.split()[4]
        if Reg in Db['splitsw']:
            Obj = Db['splits'][Reg]
            Map = Db['splitsw'][Reg]
            Map.reverse()
            Bin = ''.join(Map)
            Int = int(Bin,2)
            MASK = "%d'h%x"%(Obj.Params['width'],Int)
            Line = Line.replace('<= ','<= %s & ('%MASK)
            Line = Line.replace(';',');')
        File.write('%s\n'%Line)

    File.write('    end\n')
    File.write('end\n')

    for Line in LINES[4]:
        File.write('%s\n'%Line)

    File.write('endmodule\n')

ROPULSE = '''
wire REG_rd_sel = pread && (mpaddr=='hADDR);
reg REG_rd_pulse_reg; always @(posedge pclk)  REG_rd_pulse_reg <= REG_rd_sel;
assign REG_pulse = REG_rd_pulse_reg;
'''


RWPULSE = '''
wire REG_wr_sel = pwrite && (mpaddr=='hADDR);
reg REG_wr_pulse_reg; always @(posedge pclk)  REG_wr_pulse_reg <= REG_wr_sel;
assign REG_pulse = REG_wr_pulse_reg;
'''

RAM_ROPULSE_RANGE = '''
assign REG_rd_pulse = pread && (mpaddr>='hLADDR) && (mpaddr < 'hHADDR);
reg REG_rd_pulse_dly; always @(posedge pclk)  REG_rd_pulse_dly <= REG_rd_pulse;
assign REG_rd_data_valid = REG_rd_pulse_dly;
'''

ROPULSE_RANGE = '''
wire REG_rd_sel = pread &&  (mpaddr>='hLADDR) && (mpaddr < 'hHADDR);
reg REG_rd_pulse_reg; always @(posedge pclk)  REG_rd_pulse_reg <= REG_rd_sel;
assign REG_rd_pulse = REG_rd_pulse_reg;
'''

RWPULSE_RANGE = '''
wire REG_wr_sel = pwrite && (mpaddr>='hLADDR) && (mpaddr < 'hHADDR);
reg REG_wr_pulse_reg; always @(posedge pclk)  REG_wr_pulse_reg <= REG_wr_sel;
assign REG_wr_pulse = REG_wr_pulse_reg;
'''
RAM_RWPULSE_RANGE = '''
assign REG_wr_pulse = pwrite && (mpaddr>='hLADDR) && (mpaddr < 'hHADDR);
'''


def treatPrdata(Reg,Wid,Name):
    if (Wid<32):
        Line = '    (mpaddr == \'h%x) ? %s :'%(Reg.Addr,expandBits(Name,Wid,32))
        LINES[1].append(Line)
    else:
        Wid1 = Wid
        Ad = Reg.Addr
        Hi,Lo = 31,0
        while Wid1>0:
            Line = '    (mpaddr == \'h%x) ? %s :'%(Ad,expandBits('%s[%d:%d]'%(Name,Hi,Lo),min(Wid1,32),32))
            Wid1 -= 32
            Ad += 4
            Lo += 32
            Hi = min(Wid-1,Hi+32)
            LINES[1].append(Line)

def treatReg(Reg):
    Access= getPrm(Reg,'access','rw')
    Wid= getPrm(Reg,'width',32)
    Reset= getPrm(Reg,'reset',0)
    Default= getPrm(Reg,'default',0)
    if (Reset==0)and(Default!=0): Reset=Default
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
            if 'ready' in Reg.Params:
                Line = '    ,input %s_ready'%(Name)
                LINES[0].append(Line)
#                LINES[9].append(Name)

            STR = ROPULSE
            if 'duration' in Reg.Params:
                STR = ROPULSE_DURATION
                STR = STR.replace('DURATION',str(Reg.Params['duration']))
            Str = STR.replace('REG',Name)
            Str = Str.replace('ADDR',hex(lastAddr)[2:])
            LINES[4].append(Str)

        treatPrdata(Reg,Wid,Name)
    elif ('rw' in Access)or('wr' in Access):
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
            STR = RWPULSE
            if 'duration' in Reg.Params:
                STR = RWPULSE_DURATION
                STR = STR.replace('DURATION',str(Reg.Params['duration']))
            Str = STR.replace('REG',Name)
            Str = Str.replace('ADDR',hex(lastAddr)[2:])
            LINES[4].append(Str)
        treatPrdata(Reg,Wid,Name)
        if Wid<=32:
            Line = '        if (mpaddr == \'h%x) %s <= (%s & ~mask) | (wdata & mask);'%(Reg.Addr,Name,Name)
            LINES[3].append(Line)
        else:
            Wid1 = Wid
            Ad = Reg.Addr
            Hi,Lo = 31,0
            while Wid1>0:
                Line = '        if (mpaddr == \'h%x) %s[%d:%d] <= (%s[%d:%d] & ~mask) | (wdata & mask);'%(Ad,Name,Hi,Lo,Name,Hi,Lo)
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
        treatPrdata(Reg,Wid,Name)
        Str = ROPULSE.replace('assign REG','assign %s_rd'%Name)
        Str = Str.replace('REG',Name)
        Str = Str.replace('ADDR',hex(Reg.Addr)[2:])
        LINES[4].append(Str)
        Str = RWPULSE.replace('assign REG','assign %s_wr'%Name)
        Str = Str.replace('REG',Name)
        Str = Str.replace('ADDR',hex(Reg.Addr)[2:])
        LINES[4].append(Str)

def treatArray(Reg):
    Access = getPrm(Reg,'access','rw')
    Wid = getPrm(Reg,'width',32)
    Reset = getPrm(Reg,'reset',0)
    Default = getPrm(Reg,'default',0)
    if (Reset==0)and(Default!=0): Reset=Default
    Dep = getPrm(Reg,'depth',32)
    Name= getPrm(Reg,'names',['err'])[0]
    if 'external' in Access:
        Line = '    ,input [%d:0] [%d:0] %s'%(Dep-1,Wid-1,Name)
        LINES[0].append(Line)
        Line = '    ,output %s_rd_pulse'%(Name)
        LINES[0].append(Line)
        Line = '    ,output %s_wr_pulse'%(Name)
        LINES[0].append(Line)
        Line = '    ,output [%d:0] %s_addr'%(logs.neededBits(Dep-1)-1,Name)
        LINES[0].append(Line)

        Str = ROPULSE_RANGE.replace('REG',Name)
        Str = Str.replace('LADDR',hex(Reg.Addr)[2:])
        Str = Str.replace('HADDR',hex(Reg.HADDR)[2:])
        LINES[4].append(Str)
        Str = RWPULSE_RANGE.replace('REG',Name)
        Str = Str.replace('LADDR',hex(Reg.Addr)[2:])
        Str = Str.replace('HADDR',hex(Reg.HADDR)[2:])
        LINES[4].append(Str)

    elif ('wr' in Access)or('rw' in Access):
        Line = '    ,output reg [%d:0] [%d:0] %s'%(Dep-1,Wid-1,Name)
        LINES[0].append(Line)
        Ad = Reg.Addr
        Line = '        %s <= %d\'h%x;'%(Name,Dep*Wid,Reset)
        LINES[2].append(Line)
        Ad = Reg.Addr
        for Ind in range(Dep):
            Line = '        if (mpaddr == \'h%x) %s[%d] <= (%s[%d] & ~mask) | (wdata & mask);'%(Ad,Name,Ind,Name,Ind)
            LINES[3].append(Line)
            Ad += simpleAdvanceAddr(Reg)

    elif ('ro' in Access):
        Line = '    ,input [%d:0] [%d:0] %s'%(Dep-1,Wid-1,Name)
        LINES[0].append(Line)
    Ad = Reg.Addr
    for Ind in range(Dep):
        Line = '    (mpaddr == \'h%x) ? %s :'%(Ad,expandBits(Name+'[%d]'%Ind,Wid,32))
        Ad += simpleAdvanceAddr(Reg)
        LINES[1].append(Line)
    return

def treatRam(Reg):
    Access = getPrm(Reg,'access','rw')
    Wid = getPrm(Reg,'width',32)
    Dep = getPrm(Reg,'depth',32)
    Name= getPrm(Reg,'names',['err'])[0]
    Line = '    ,input [%d:0] %s_rdata'%(Wid-1,Name)
    LINES[0].append(Line)
    Line = '    ,output [%d:0] %s_wdata'%(Wid-1,Name)
    LINES[0].append(Line)
    Line = '    ,output [%d:0] %s_addr'%(logs.neededBits(Dep-1)-1,Name)
    LINES[0].append(Line)
    Line = '    ,output %s_rd_pulse'%(Name)
    LINES[0].append(Line)
    Line = '    ,output %s_wr_pulse'%(Name)
    LINES[0].append(Line)

    BusWidth = Db['chip'].Params['width']
    BusBytes = BusWidth/8
    if BusBytes==8: AdShift = 3
    elif BusBytes==4: AdShift = 2
#    Bytes = (Wid/8)+((Wid%8)!=0);
#    if Bytes==1: AdShift=0
#    elif Bytes==2: AdShift=1
#    elif Bytes==4: AdShift=2

    Line = 'wire [2:0] ExtraBytes%s  =  pstrb[0] ? 0 : pstrb[1] ? 1 : pstrb[2] ? 2 : pstrb[3] ? 3 '%(Name)
    if (BusBytes==8):
        Line += ': pstrb[4] ? 4 : pstrb[5] ? 5 : pstrb[6] ? 6 : 7;'
    else:
        Line += ': 0;'
    LINES[4].append(Line)

    if (Wid==8): Adjust=0
    elif (Wid==16): Adjust=1
    elif (Wid==32): Adjust=2
    elif (Wid==64): Adjust=3

#    Line = 'wire [2:0] Extra%s = ExtraBytes%s>>%s;'%(Name,Name,Adjust)
#    LINES[4].append(Line)


    if (BusWidth==64):
        Line = 'assign %s_addr = ((mpaddr - \'h%x)>>%s);'%(Name,Reg.Addr,3)
    elif (BusWidth==32):
        Line = 'assign %s_addr = ((mpaddr - \'h%x)>>%s);'%(Name,Reg.Addr,2)
    LINES[4].append(Line)

    if BusWidth == Wid:
        Line = 'assign %s_wdata = wdata;'%(Name)
    elif (BusWidth>Wid):
        Line = 'assign %s_wdata = wdata[%d:0];'%(Name,Wid-1)
    LINES[4].append(Line)



    Str = RAM_ROPULSE_RANGE.replace('REG',Name)
    Str = Str.replace('LADDR',hex(Reg.Addr)[2:])
    Str = Str.replace('HADDR',hex(Reg.HADDR)[2:])
    LINES[4].append(Str)
    Str = RAM_RWPULSE_RANGE.replace('REG',Name)
    Str = Str.replace('LADDR',hex(Reg.Addr)[2:])
    Str = Str.replace('HADDR',hex(Reg.HADDR)[2:])
    LINES[4].append(Str)
    if (BusWidth==Wid):
        Line = '    %s_rd_data_valid ? %s_rdata :\n'%(Name,Name)
    elif (BusWidth==(2*Wid)):
        Line = '    %s_rd_data_valid ? {%s_rdata,%s_rdata} :\n'%(Name,Name,Name)
    elif (BusWidth==(4*Wid)):
        Line = '    %s_rd_data_valid ? {%s_rdata,%s_rdata,%s_rdata,%s_rdata} :\n'%(Name,Name,Name,Name,Name)
    elif (BusWidth==(8*Wid)):
        Line = '    %s_rd_data_valid ? {%s_rdata,%s_rdata,%s_rdata,%s_rdata,%s_rdata,%s_rdata,%s_rdata,%s_rdata} :\n'%(Name,Name,Name,Name,Name,Name,Name,Name,Name)
    else:
        Line = '    %s_rd_data_valid ? %s_rdata :\n'%(Name,Name)
    Db['chip'].RAMS += Line
    Db['chip'].RAMS_WIRES += 'wire %s_rd_data_valid;'%Name


def dumpDefines():
    Module = Db['chip'].Params['names'][0] 
    File = open('%s/%s_defs.py'%(Dir,Module),'w')
    File2 = open('%s/%s_inc.seq'%(Dir,Module),'w')
    File.write('ADDR_MAP = {}\n')
    for Line in LINES[5]:
        File.write('%s\n'%(Line))
    File.close()
    
    for Line in LINES[5]:
        if 'ADDR' not in Line:
            ww = Line.split()
            File2.write('define %s %s\n'%(ww[0],ww[2]))
    File2.close()

def runXml():
    Module = Db['chip'].Params['names'][0]
    xml_regfile2_create.createXml(Module,Db)
    regfile_html.produce_html(Module,Db)

APBHead = '''
module MODULE (input pclk, input presetn,
    input psel, input penable, input pwrite, input [WSTRB-1:0] pstrb, input [ADDWID-1:0] paddr, input [BUSWID-1:0] pwdata, output [BUSWID-1:0] prdata
    ,output pready, output pslverr
'''
APBInst = '''
wire [1023:0] ZEROES = 1024'b0;
MODULE rgf (.pclk(pclk),.presetn(presetn),.pwrite(i_pwrite),.pread(i_pread),.paddr(paddr)
    ,.pwdata(pwdata),.prdata(prdata)
    ,.pstrb(pstrb)
'''

APB2RAM = '''
wire i_pread = psel && !pwrite;
wire i_pwrite = psel && pwrite && penable;
assign pslverr = 0;
'''



def dumpApb(Db):
    bodyDump0(Db)
    Module = Db['chip'].Params['names'][0] 
    Dir = Db['dir']
    Db['fout'] = open('%s/%s.v'%(Dir,Module),'w')
    Str = INSTANCE.replace('MODULE',Db['module'])
    Finst = open('%s.inst'%Db['module'],'w')
    Finst.write(Str)
    apbHead()
    Temp = helper0(Finst)
    enclosingModule(Temp,Finst)
    dumpRam('_ram',Db['fout'])
    Finst.close()

def apbHead():
    Str = APBHead.replace('MODULE',Db['module'])
    Buswid = Db['chip'].Params['width']
    Addwid = Db['chip'].Params['addrwid']
    if Buswid == 32:
        Wstrb = 4
    else:
        Wstrb = logs.neededBits(int(Buswid/8))
    Str = Str.replace('BUSWID',str(Buswid))
    Str = Str.replace('ADDWID',str(Addwid))
    Str = Str.replace('WSTRB',str(Wstrb))
    Db['fout'].write(Str)

def helper0(Finst):
    Temp = []
    for Li in LINES[0]:
        Li = Li.replace(' reg ',' ')
        Wrds = Li.split()
        if Wrds[-1] not in FIELDED_REGS:
            Db['fout'].write(Li+'\n')
            Finst.write('    ,.%s(%s)\n'%(Wrds[-1],Wrds[-1]))
        else:
            Li = Li.replace('input','wire')
            Li = Li.replace('output','wire')
            Li = Li.replace(',','')
            Li = Li + ';'
            Temp.append(Li)
    return Temp

def enclosingModule(Temp,Finst):
    for Li in LINES[7]:
         Db['fout'].write('%s\n'%Li)
         wrds = Li.split()
         Finst.write('    ,.%s(%s)\n'%(wrds[-1],wrds[-1]))
    for Line in LINES[9]:
        Db['fout'].write('    ,input %s_ready\n'%Line)
    Db['fout'].write(');\n')
    Finst.write(');\n')

    for Li in Temp:
        Db['fout'].write('%s\n'%Li)
    Db['fout'].write(APB2RAM)
    if LINES[9]==[]:
        Db['fout'].write('assign pready = 1;\n')
    else:
        Db['fout'].write('assign pready = \n')
        for Name in LINES[9]:
            Db['fout'].write('    %s_pulse ? %s_ready :\n'%(Name,Name))
        Db['fout'].write('    1;\n')

    Str = APBInst.replace('MODULE',Db['module']+'_ram')
    Db['fout'].write(Str)
    for Li in LINES[0]:
        wrds = Li.split()
        Conn = wrds[-1]
        Conn2 = wrds[-1]
        if Conn in Db['splits']:
            RR = Db['splits'][Conn]
            Acc = RR.Params['access']
            Wid = RR.Params['width']
            if inAccess(Acc):
                Conn2 = 'ZEROES[%d:0] | %s'%(Wid-1,Conn2)
        Db['fout'].write('    ,.%s(%s)\n'%(Conn,Conn2))
    Db['fout'].write(');\n')
    for Li in LINES[6]:
         Db['fout'].write('%s\n'%Li)



    Db['fout'].write('endmodule\n')




def  outAccess(Access):
    if 'rw' in Access: return True
    if 'wr' in Access: return True
    return False
def  inAccess(Access):
    if 'ro' in Access: return True
    return False



if __name__ == '__main__': main()

