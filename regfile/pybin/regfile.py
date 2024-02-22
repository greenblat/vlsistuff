#! /usr/bin/env python3


HELPSTRING = '''
needs regfile description file.

example of regfile file:

chip plug_rgf  bus=apb addrwid=20 width=32 reset=async empty=0xdeadbeaf
reg cucu width=72 access=rw desc="this is very important register"
// access(can be ro wo rw_pulse ro_pulse)  
array arr width=12 depth=13 access=ro desc="less important"
// several other options appear in docs
include filename   = new option, to include
'''


import os,sys,string

import logs

import xml_regfile2_create
import regfile_html
import regfile_c

def wopen(Fname):
    if (Fdirx!='') and (Fdirx!='.') and not os.path.exists(Fdirx):
        os.mkdir(Fdirx)
    Full = '%s/%s' % (Fdirx,Fname)
    File =  open(Full,'w')
    return File

regfile_c.wopen = wopen
regfile_html.wopen = wopen
xml_regfile2_create.wopen = wopen

def main():
    global Fdirx
    if len(sys.argv) == 1:
        print(HELPSTRING)
        return
    Fname = sys.argv[1]
    Fdirx = '.'
    if len(sys.argv)>2:
        Fdirx = sys.argv[2]
    Cell,Dir,Ext = logs.fnameCell(Fname)
    if Dir == '': 
        Dir = '.'
    if Fdirx == '':
        Fdir = Dir
    if Ext=='':
        run(Cell,Fdirx)
    else:
        run(Fname,Fdirx)



def run(Fname,Dirx='.',Base=0):
    global Dir
    Dir = Dirx
    for Key in Db.keys():
        Db[Key] = []
    Db['checkNames'] = {}
    Db['BASE'] = Base
    File = open(Fname)
    readFile(File)
    missParam(Db['chip'].Params,'width',32)
    missParam(Db['chip'].Params,'addrwid',32)
    missParam(Db['chip'].Params,'reset','async')
    missParam(Db['chip'].Params,'empty',0xdeadbeef)
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
    Dir = Db['dir']
    Db['fout'] = wopen('%s.v'%(Module))
    if 'apb' in Params:
        dumpApb(Db)
    elif 'ram' in Params:
        bodyDump0(Db)
        dumpRam('_ram',Db['fout'],True)
        Db['fout'].close()
    else:
        logs.log_error('need to specify output format:  apb ram')
    dumpDefines()
    runXml()
#    report()
#    report2(LINES)
    if LINES[8]!=[]:
        Fspl = wopen('%s.splits'%Module)
        for Line in LINES[8]:
            Fspl.write(Line+'\n')
        Fspl.close()
    return Db['module']

def report2(LINES):
    for Key in LINES:
        LL = LINES[Key]
        for Li in LL:
            logs.log_info('%s: %s'%(Key,Li))

Db = {'items':[],'clocks':[],'regs':[],'fields':[],'splitted':[],'enable_writes':[]}


def dealIncludes(Lines):
    ind = 0
    while ind<len(Lines):
        line = Lines[ind]
        wrds = line.split()
        if (wrds!=[]) and (wrds[0] == 'include'):
            Fname = wrds[1]
            Ftmp = open(Fname)
            More = Ftmp.readlines()
            for indx,llx in enumerate(More):
                wrdsx = llx.split()
                if ('chip' in llx)and(wrdsx[0] == 'chip'):
                    More[indx] = ''
                if ('end' in llx)and(wrdsx[0] == 'end'):
                    More[indx] = ''
            Lines = Lines[:ind-1] + More + Lines[ind+1:]
        else:
            ind += 1
    return Lines



def createLines(File):
    Lines = File.readlines()
    Lines = dealIncludes(Lines)

    Long = ''
    Lnum = 0
    for line in Lines:
        if '//' in line: line = line[:line.index('//')]
        else:
            line = line[:-1]
        Long += line + ' ;;; '
    Wrds = Long.split()
    Res = []
    state = 'idle'
    for Wrd in Wrds:
        if state=='idle':
            if ('"' in Wrd)and(Wrd.count('"')==1):
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
        Lnum += 1
        Head = Res[:X]
        Pos = -1
        for ind,Tok in enumerate(Head):
            if Tok[0]=='#': Pos = ind
        if Pos>=0:
            Head = Head[:Pos]
        Res = Res[X+1:]
        if Head!=[]:
            Res2.append((Lnum,Head))
    return Res2        


def readFile(File):
    Lines = createLines(File)  
    Lines = treatTemplates(Lines)
    for Lnum,wrds in Lines:
        if (wrds[0]=='end'):
            generate()
            return
        elif (wrds[0]=='chip'):
            Db['chip'] = itemClass(Lnum,wrds)
        else:
            Split = False
            if wrds[0] == 'array':
                Params = getParams(Lnum,wrds[1:])
                if ('pulse' in Params['access']) or (Params['width'] >32):
                    Split = True
                    Base = Params['names'][0]
                    Prepare = 'reg %sNNN width=%s access=%s desc=%s' % (Params['names'][0],Params['width'],Params['access'],Params['desc'])
                    if 'fields' in Params:
                        Prepare += ' fields=external'
                    Splitted = [Base,Params['depth']]
                    Members = []
                    Members_pulse = []
                    for II in range(Params['depth']):
                        Prep = Prepare.replace('NNN',str(II))
                        wrds = Prep.split()
                        Item = itemClass(Lnum,wrds)
                        Db['items'].append(Item)
                        Kind = Item.Kind
                        Item.Name = Item.Params['names'][0]
                        Members.append('%s' % Item.Name)
                        Members_pulse.append('%s_pulse' % Item.Name)
                        Splitted.append(Item.Name)
                        if len(Item.Params['names'])>0:
                            Name = Item.Params['names'][0]
                            Item.Name = Name
                            checkPair(Item,Kind,Name)
                        else:
                            Item.Name = 'none'
                    Db['splitted'].append(Splitted)
                    if outAccess(Params['access']):
                        LINES[0].append('    ,output [%s-1:0] [%s-1:0] %s' % (Params['depth'],Params['width'],Base))
                        Members.reverse()
                        LINES['split2'].append('assign %s = { %s };' % (Base,','.join(Members)))
                    else:
                        LINES[0].append('    ,input [%s-1:0] [%s-1:0] %s' % (Params['depth'],Params['width'],Base))
                        LINES['split2'].append('assign { %s } = %s;' % (','.join(Members),Base))

                    if ('pulse' in Params['access']):
                        LINES[0].append('    ,output [%s-1:0] %s_pulse' % (Params['depth'],Base))
                        Members_pulse.reverse()
                        LINES['split2'].append('assign %s_pulse = { %s };' % (Base,','.join(Members_pulse)))
                    if 'ready' in Params:
                        Line = '    ,input %s_ready'%(Base)
                        LINES[0].append(Line)
                        LINES[9].append(Base)

            if (not Split):
                Item = itemClass(Lnum,wrds)
                Db['items'].append(Item)
                Kind = Item.Kind
                if len(Item.Params['names'])>0:
                    Name = Item.Params['names'][0]
                    Item.Name = Name
                    checkPair(Item,Kind,Name)
                else:
                    Item.Name = 'none'
    logs.log_warning('You should have "end" line as last line.')
    generate()



def checkPair(Item,Kind,Name):
    if Kind == 'field': return
    if Kind not in Db['checkNames']: 
        Db['checkNames'][Kind]=[Name]
        return
    if Name in Db['checkNames'][Kind]:
        logs.log_error('#%d: double defined item %s of kind %s . previous=%s'%((Item.Lnum,Name,Kind,Db['checkNames'][Kind])))
        return

    Db['checkNames'][Kind].append(Name)

def treatTemplates(Lines):
    Templates = {}
    Curr = []
    state = 'idle'
    Result = []
    for Lnum,Line in Lines:
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
                    Result.append((Lnum,LX))
            else:
                Result.append((Lnum,Line))
        elif state=='work':
            if Line[0] == 'endtemplate':
                Templates[Name] = Curr[:]
                state='idle'
            else:
                Curr.append(Line)
    return Result


SYNONYMS = {'wid':'width','desc':'description','rw':'wr','rw_pulse':'wr_pulse'}



class itemClass:
    def __init__(self,Lnum,Wrds):
        self.Kind = Wrds[0]
        self.Lnum = Lnum
        self.Params = getParams(Lnum,Wrds[1:])
        self.Synonyms()
        self.Addr = -1
        self.RAMS = ''
        self.PREADIES = '1'
        self.RAMS_WIRES = ''
        self.incs = []
        self.enable_writes = []


    def dump(self):
        print('#%d %s : (%d 0x%x) %s'%(self.Lnum,self.Kind,self.Addr,self.Addr,self.Params))


    def Synonyms(self):
        for Key in SYNONYMS:
            if Key in self.Params:
                Val = SYNONYMS[Key]
                if Val not in self.Params:
                    self.Params[Val] = self.Params[Key]


def getParams(Lnum,wrds):
    Res = {}
    Nn = []
    for wrd in wrds:
        if '=' in wrd:
            ww = wrd.split('=')
            if len(ww)>2:
                Join = '='.join(ww[1:])
                ww = [ww[0],Join]
            AA = examine(Lnum,ww[1])
            Res[ww[0]] = AA
        else:
            Nn.append(wrd)
    Res['names']=Nn
    return Res 
    

def examine(Lnum,Txt):
    if Txt=='': return Txt
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
            logs.log_error('#%d: examine of "%s" failed'%(Lnum,Txt))
            return 0
    else:
        return Txt


def expandBits(Name,Wid,Bits):
    if Wid==Bits: return Name
    if Wid<Bits:
        Line = '{%d\'b0,%s}'%(Bits-Wid,Name)
        return Line
    return 'ERROR%s'%Name
    

def treatFields():
    DbFields = Db['fields']
    Nc = 0
    for Reg in DbFields:
        Split=True
        RegObj = findObj(Db['regs'],Reg)
        RegWid = RegObj.Params['width']
        if ('fields' in RegObj.Params)and(RegObj.Name not in EXTERNAL_REGS):
            Wid = getPrm(RegObj,'width',0)
            if Wid<=1:
                WW = ''
            else:
                WW = '[%s:0]'%(Wid-1)
            Access = RegObj.Params['access']
            Split=False
            EXTERNAL_FIELDS.append(RegObj.Name)
            
        Fields = DbFields[Reg]
        Pos = 0
        Winaccess='gap'
        Access = Fields[0].Params['access']
        Cover = []
        for X in range(RegWid): Cover.append('0')

        for Field in Fields:
            Wid= getPrm(Field,'width',0)
            Hi,Lo = Field.Params['position']
            Name = Field.Params['names'][0]
            if 'access' in Field.Params:
                Access = Field.Params['access']
                if Access!='gap':
                    Winaccess = Access

            if Wid<=1:
                WW = ''
                if RegWid<=1:
                    RegHiLo = Reg
                else:
                    RegHiLo = '%s[%s]'%(Reg,Hi)
                    if (Hi!=Lo):
                        logs.log_error('#%d: ILIA reg=%s field=%s hilo= %s %s'%(RegObj.Lnum,Reg,Field,Hi,Lo))
            else:
                WW = '[%s:0]'%(Wid-1)
                RegHiLo = '%s[%s:%s]'%(Reg,Hi,Lo)

            for PP in range(Lo,Hi+1):
                Cover[PP] = '1'
            if Name == 'gap':
                pass
            elif outAccess(Access):
                if Split:
                    LINES[7].append('    ,output %s %s'%(WW,Name))

                if ('fields' in RegObj.Params):
                    LINES[8].append('assign %s = %s;'%(Name,RegHiLo))
                else:
                    LINES[6].append('assign %s = %s;'%(Name,RegHiLo))
            elif inAccess(Access):
                if Split:
                    LINES[7].append('    ,input  %s %s'%(WW,Name))
                if ('fields' in RegObj.Params):
                    if Name == 'gap':
                        Name = '0'
                    LINES[8].append('assign %s = %s;'%(RegHiLo,Name))
                else:
                    if Name == 'gap':
                        Name = '0'
                    LINES[6].append('assign %s = %s;'%(RegHiLo,Name))
            elif Access in ['external' ,'w1c']:
                LINES[8].append('\n\n// external reg with fields, take one')
                LINES[8].append('assign %s = %s;'%(RegHiLo,Name))
                LINES[8].append('assign %s = %s;\n'%(Name,RegHiLo))
            else:
                logs.log_error('#%d: fields not legal access %s for %s'%(RegObj.Lnum,Access,Name))
        if inAccess(Access)and('0' in Cover):
            Ranges = getRanges(Cover)
            for Lo,Hi in Ranges:
                LINES[6].append('assign %s[%d:%d] = 0;'%(Reg,Hi,Lo))

def findObj(List,Name):
    for Obj in List:
        if Obj.Name==Name: return Obj
    return False

def getRanges(List):
    Ranges = []
    Lo = 0
    Hi = 0
    state='idle'
    for ii in range(len(List)):
        if state=='idle':
            if List[ii]=='0':
                state = 'work'
                Lo = ii
        elif state=='work':
            if List[ii]=='1':
                state = 'idle'
                Ranges.append((Lo,Hi))
            else:
                Hi = ii
    if state=='work':
        Ranges.append((Lo,Hi))
    return Ranges

def generate():
    gatherFields()
    uniquifyFields()

FIELDED_REGS = []    
EXTERNAL_REGS = []    
EXTERNAL_FIELDS = []    

def uniquifyFields():
    Takens = {}
    for Reg in Db['regs']:
        Name = Reg.Name
        if Name in Db['fields']:
            List = Db['fields'][Name]
            for Field in List:
                Fname = Field.Name
                if Fname == 'gap':
                    pass
                elif Fname in Takens:
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
        elif (len(List)==1):
            Field,Reg = List[0]
            if 'suffix' in Reg.Params:
                logs.log_warning('no need for suffix in reg=%s field=%s - it is unique'%(Reg.Name,Field.Name))
            if 'prefix' in Reg.Params:
                logs.log_warning('no need for prefix in reg=%s field=%s - it is unique'%(Reg.Name,Field.Name))

            
        


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
            if ('access' in Reg.Params) and (Reg.Params['access']=='external'):
                EXTERNAL_REGS.append(Reg.Name)
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
                Obj.incs.append(Reg.Name)
            else:
                logs.log_error('#%d: no reg for field %s'%(Reg.Lnum,Reg.Params))
        else:
            Db['regs'].append(Reg)
            Active=False
    for Reg in Db['regs']:
        if len(Reg.incs)==1:
            logs.log_warning('#%d: REG "%s" has just one field "%s". this is not needed.'%(Reg.Lnum,Reg.Name,Reg.incs[0]))


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
            OrigReset = getPrm(Reg,'reset',0)
            Ptr = 0
            Wid = 0
            Map = []
            BuildReset = 0
            if Name in Db['fields']:
                List = Db['fields'][Name]
                for Obj in List:
                    Name= getPrm(Obj,'names',['err'])[0]
                    Obj.Name = Name
                    Add0 = getPrm(Obj,'width',0)
                    Add = getPrm(Obj,'width',0)
                    if Add==0:
                        logs.log_error('#%d: reg %s field %s has no width'%(Reg.Lnum,Name,Obj.Name))
                    Align = getPrm(Obj,'align',0)
                    if (Align>0):
                       if (Align<=Add):
                          logs.log_error('#%d: field %s of reg %s has bith width and align. align is smaller.'%(Reg.Lnum,Obj.Name,Name))
                       else:
                          Add = Align
                          Db['splits'][Reg.Name] = Reg
                    Obj.Params['position'] = (Wid+Add0-1,Wid)
                    while (len(Map)<(Wid+Add0)): Map.append('0')
                    if (Name=='gap'):
                        for X in range(Wid+Add0-1,Wid-1,-1):
                            Map[X] = '0'
                            Db['splits'][Reg.Name] = Reg
                    else:                        
                        for X in range(Wid+Add0-1,Wid-1,-1):
                            Map[X] = '1'
                        
                    if 'reset' in Obj.Params:
                        Freset = Obj.Params['reset']
                        Bin = len(bin(Freset))-2
                        if Add0<Bin:
                            logs.log_error('#%d: reset value 0x%x of field %s of reg %s is wider than bits allocated to it = %d'%(Reg.Lnum,Freset,Name,Reg.Name,Add0))
                            Freset = Freset & ((1<<Add)-1)
                        BuildReset |= (Freset<<Wid)

                    Wid += Add
                if OrigWid==0:
                    Reg.Params['width']=Wid
                elif (OrigWid<Wid):
                    logs.log_error('#%d: fields of reg %s (wid=%d) take more bits (%d)'%(Reg.Lnum,Reg.Name,OrigWid,Wid))
                elif (OrigWid>Wid):
                    logs.log_warning('#%d: fields of reg %s (wid=%d) take less bits (%d). consider removing width= from reg definition line'%(Reg.Lnum,Reg.Name,OrigWid,Wid))
                if Reg.Name in Db['splits']:
                    Db['splitsw'][Reg.Name]=Map

                if (OrigReset==0)and(BuildReset!=0):
                    Reg.Params['reset'] = BuildReset
                elif (OrigReset!=0)and(BuildReset!=0)and(OrigReset!=BuildReset):
                    logs.log_error("#%d: reg %s has reset value of it's own and also fields. remove one or the other"%(Reg.Lnum,Reg.Name))

            if (OrigWid==0)and( getPrm(Reg,'width',0)==0):
                logs.log_error('#%d: reg %s has no width and no fields (defined %s)'%(Reg.Lnum,Name,list(Db['fields'].keys())))
            



def assignAddresses():
    Chip = Db['chip']
#    Addr = getPrm(Chip,'base',0)
    Addr = Db['BASE'] 
    HADDR = Addr
    for Reg in Db['regs']:
        Reg.Addr = Addr
        if Reg.Kind in ['reg','array','ram']:
            Name= getPrm(Reg,'names',['err'])[0]
            LINES[5].append('%s = 0x%x'%(Name,Addr))
            LINES[5].append('ADDR_MAP["%s"] = 0x%x'%(Name,Addr))
            LINES[5].append('WIDTH_MAP["%s"] = %d'%(Name,advanceAddr(Reg)))
        Addr += int(advanceAddr(Reg))
        Reg.HADDR = Addr
    Chip.Addr = Addr
    Chip.HADDR = Addr
    Db['lastAddr'] = Addr


def computeWid(Obj):
    Wid = Obj.Params['width']
    AA = int(Wid/32)
    Rest = Wid-(AA*32)
    if Rest>0: AA += 1
    return AA

def bytes(Wid):
    A = int(Wid/8)
    B= (Wid % 8)>0
    return A+B


def simpleAdvanceAddr(Obj):
    if 'width' in Db['chip'].Params:
        Bytes = int(Db['chip'].Params['width']/8)
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
        Bytes = int(Db['chip'].Params['width']/8)
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
            Add0 = int(Bytes2/Bytes)
            Add1 = int((Bytes2 % Bytes)>0)
            Add  = Add0 + Add1
    elif (Obj.Kind not in ['gap']):
        logs.log_error('#%d: advanceAddr: missing wid in %s %s  defs:%s'%(Obj.Lnum,Obj.Kind,Obj.Name,Obj.Params))
        Add = 4


    if Obj.Kind in ['reg','external']:
        logs.mustKey(Obj.Params,'width')
        return Add*Bytes
    elif Obj.Kind in ('ram'):
        logs.mustKey(Obj.Params,'width')
        logs.mustKey(Obj.Params,'depth')
        if 'modifier' in Obj.Params:
            Modif = Obj.Params['modifier']
            if Modif not in ['internal','external']:
                logs.log_error('#%d: ram mode=%s of %s is not supported (external,internal) '%(Obj.Lnum,Modif,Obj.Params['names'][0]))
                
        Dep = Obj.Params['depth']
        if (Bytes2<=Bytes):
            return Dep*Bytes
        else:
            logs.log_error('#%d: ram %s is not supported to  be wider than bus (%d>%d)'%(Obj.Lnum,Obj.Params['names'][0],Bytes2,Bytes))
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
            
            return Obj.Params['abs']-Obj.Addr
        elif 'width' in Obj.Params:
            return Add*Bytes

        else:
            logs.log_error('#%d: advanceAddr GAP got %s'%str(Obj.Lnum,Obj.Params))
    else:
        logs.log_error('#%d: advanceAddr got %s'%(Obj.Lnum,Obj.Kind))
        return Bytes

INSTANCE = '''
MODULE MODULE (.pclk(pclk),.presetn(presetn)
    .pwrite(pwrite),.paddr(paddr),.psel(psel),.penable(penable)
    ,.prdata(prdata),.prdata_wire(),.pwdata(pwdata),.pstrb(pstrb)
    ,.pready(pready),.pslverr(pselverr)
    ,.penable(penable)
'''




HEADER = '''`timescale 1ns / 1ps
module MODULE (
    input pclk,input presetn,input pwrite, input pread, input penable
    ,input [BUSWID-1:0] pwdata, output [BUSWID-1:0] prdata, output [BUSWID-1:0] prdata_wire
    ,input [WSTRB-1:0] pstrb
    ,input [ADDWID-1:0] paddr ,output reg [BUSWID-1:0] last_wdata
    ,output pready
'''

STRING0 = '''
wire [ADDWID-1:0] mpaddr0 =  ADDWID'hMASK & (paddr - 'hBASE);
wire [ADDWID-1:0] mpaddr = (pread||pwrite) ? mpaddr0  : 0;
assign prdata_wire =
'''

PSTRB1 = '{8{pstrb}}'
PSTRB2 = '{{8{pstrb[1]}},{8{pstrb[0]}}}'
PSTRB4 = '{{8{pstrb[3]}},{8{pstrb[2]}},{8{pstrb[1]}},{8{pstrb[0]}}}'
PSTRB8 = '{{8{pstrb[7]}},{8{pstrb[6]}},{8{pstrb[5]}},{8{pstrb[4]}},{8{pstrb[3]}},{8{pstrb[2]}},{8{pstrb[1]}},{8{pstrb[0]}}}'
PSTRB16 = '{{8{pstrb[15]}},{8{pstrb[14]}},{8{pstrb[13]}},{8{pstrb[12]}},{8{pstrb[11]}},{8{pstrb[10]}},{8{pstrb[9]}},{8{pstrb[8]}}' + PSTRB8


STRING1 = '''

reg [BUSWID-1:0] prdata_reg;
always @(posedge pclk) prdata_reg <=  prdata_wire;
PREADIES
assign prdata =   RAMS
    prdata_reg;

wire [BUSWID-1:0] mask = { PSTRB };
always @(posedge pclk) if (pwrite) last_wdata <= wdata & mask;
always @(posedge pclk ASYNCRST) begin
    if (!presetn) begin '''


W1C = '''
wire NAME_wr_sel;
always @(posedge pclk ASYNCRST) begin
    if (!presetn) begin 
        NAME_int <= 0;
    end else begin
        NAME_int <= (NAME_wr_sel ? (NAME_int & ~ wdata[WID:0]) : NAME_int) | NAME;
    end
end
'''

LINES = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],'split':[],'split2':[]}
def dumpRam(Postfix,File,Alone):
    Module = Db['chip'].Params['names'][0] 
    try:
        Buswid = Db['chip'].Params['width']
        Addwid = Db['chip'].Params['addrwid']
    except:
        logs.log_error('You need to have width and addrwid in chip line. it is buswidth')
        sys.exit()
    if Buswid==128: Wstrb=16
    elif Buswid==64: Wstrb=8
    elif Buswid==32: Wstrb=4
    elif Buswid==16: Wstrb=2
    elif Buswid==8: Wstrb=1
    else:
        logs.log_error('BUSWIDTH is %d , allowed values are 32,64,128'%Buswid)
        Wstrb = 4
        Buswid = 32
    Str = HEADER.replace('MODULE',Module+Postfix)
    Str = Str.replace('BUSWID',str(Buswid))
    Str = Str.replace('ADDWID',str(Addwid))
    Str = Str.replace('WSTRB',str(Wstrb))
    File.write(Str)
    Db['module']=Module
#    bodyDump0(Db,File)
    Finstram = wopen('%s.inst' % Module)
    for Line in LINES[0]:
        forInst(Line,'wire',Finstram)
    Str  = APBInst.replace('MODULE',Module)
    Finstram.write('%s\n' % Str)
    for Line in LINES[0]:
        File.write('%s\n'%Line)
        forInst(Line,'con',Finstram)
    bodyDump1(Db,File,Alone)
    Finstram.write(');\n')
    Finstram.close()
    return File
    
def forInst(Line,Which,Finst):
    wrds = Line.split()
    if wrds[1] == 'reg': wrds.pop(1)
    Sig = wrds[-1]
    if Which == 'wire':
        if len(wrds) == 3:
            Finst.write('wire %s %s;\n' % (wrds[1],Sig))
        if len(wrds) == 4:
            Finst.write('wire %s %s %s;\n' % (wrds[1],wrds[2],Sig))
    if Which == 'con':
        Finst.write('    ,.%s(%s)\n' % (Sig,Sig))


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
            logs.log_error('#%d: wrong kind %s %s'%(Reg.Lnum,Reg.Kind,Reg.Params))
    

def bodyDump1(Db,File,Alone):
    Base = getPrm(Db['chip'],'base',0)
    X = logs.neededBits(Db['chip'].Addr-Base)
    Buswid = Db['chip'].Params['width']
    Addwid = Db['chip'].Params['addrwid']
    if Buswid == 128:
        Mask = ((1<<Addwid)-1) & 0xffffffe0
    elif Buswid == 64:
        Mask = ((1<<Addwid)-1) & 0xfffffff8
    elif Buswid == 32:
        Mask = ((1<<Addwid)-1) & 0xfffffffc
    elif Buswid == 16:
        Mask = ((1<<Addwid)-1) & 0xfffffffe
    elif Buswid == 8:
        Mask = ((1<<Addwid)-1) & 0xffffffff

    if Buswid==128: Wstrb=16
    elif Buswid==64: Wstrb=8
    elif Buswid==32: Wstrb=4
    elif Buswid==16: Wstrb=2
    elif Buswid==8: Wstrb=1
    else:
        logs.log_error('#%d: BUSWIDTH is %d , allowed values are 32,64,128'%(Reg.Lnum,Buswid))
        Wstrb = 4
        Buswid = 32
    if Alone:
        for Line in LINES[7]:
            File.write('%s\n' % Line)
    File.write(');\n')
    for Line in LINES['split']+LINES['split2']:
        File.write('%s\n'%Line)
    Str = 'wire [BUSWID-1:0] wdata = pwdata;\n'.replace('BUSWID',str(Buswid))
    File.write(Str)

    for Line in LINES[10]:
        File.write('%s\n'%Line)
#    Haddr = Db['chip'].HADDR

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
            Default = hex(eval(Default))
        except:
            logs.log_error('#empty of chip (default value for cases) is not a legal integer "%s"'%(Default))
            Default='0; // BAD DEFAULT %s'%Default
            
    File.write("    %d'h%s;\n" % (Buswid,Default[-8:]))
    Str = STRING1.replace('RAMS',Db['chip'].RAMS)
    Str = Str.replace('PREADIES',makePready())
    Str = Str.replace('BUSWID',str(Buswid))
    Str = Str.replace('ADDWID',str(Addwid))
    Str = Str.replace('WSTRB',str(Wstrb))
    if Buswid==128:
        Str = Str.replace('PSTRB',PSTRB16)
    if Buswid==64:
        Str = Str.replace('PSTRB',PSTRB8)
    elif Buswid==32:
        Str = Str.replace('PSTRB',PSTRB4)
    elif Buswid==16:
        Str = Str.replace('PSTRB',PSTRB2)
    elif Buswid==8:
        Str = Str.replace('PSTRB',PSTRB1)

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
    if Alone:
        for Line in LINES[6]:
            File.write('%s\n' % Line)

    File.write('endmodule\n')

ROPULSE = '''
wire REG_rd_sel = pread && (mpaddr=='hADDR);
reg REG_rd_pulse_reg; always @(posedge pclk or negedge presetn)  if (!presetn) REG_rd_pulse_reg<=0; else REG_rd_pulse_reg <= REG_rd_sel;
assign REG_pulse = REG_rd_pulse_reg && penable;
'''

W1CPULSE = '''
assign REG_wr_sel = pwrite && (mpaddr=='hADDR);
'''

RWPULSE = '''
wire REG_wr_sel = pwrite && (mpaddr=='hADDR);
reg REG_wr_pulse_reg; always @(posedge pclk or negedge presetn)  if (!presetn) REG_wr_pulse_reg<=0; else REG_wr_pulse_reg <= REG_wr_sel;
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
    busWid = Db['chip'].Params['width']
    Jump = busWid//8
    if (Wid<busWid):
        Line = '    (mpaddr == \'h%x) ? %s :'%(Reg.Addr,expandBits(Name,Wid,busWid))
        LINES[1].append(Line)
    else:
        Wid1 = Wid
        Ad = Reg.Addr
        Hi,Lo = busWid-1,0
        while Wid1>0:
            Line = '    (mpaddr == \'h%x) ? %s :'%(Ad,expandBits('%s[%d:%d]'%(Name,Hi,Lo),min(Wid1,busWid),busWid))
            Wid1 -= busWid
            Ad += Jump
            Lo += busWid
            Hi = min(Wid-1,Hi+busWid)
            LINES[1].append(Line)

def fromArray(Reg):
    Name = Reg.Name
    Arrs = Db['splitted']
    for Arlist in Arrs:
        Base = Arlist[0]
        if Name.startswith(Base):
            Ind = Arlist.index(Name)
            return Ind
    return False
            

def treatReg(Reg):
    busWid = Db['chip'].Params['width']
    Jump = busWid//8
    Access= getPrm(Reg,'access','rw')
    EnableWr= getPrm(Reg,'enable_write','none')
    if EnableWr!='none':
        if EnableWr not in Db['chip'].enable_writes:
            LINES[0].append('    ,input %s' % EnableWr)
            Db['chip'].enable_writes.append(EnableWr)
    Wid= getPrm(Reg,'width',busWid)
    Reset= getPrm(Reg,'reset',0)
    Default= getPrm(Reg,'default',0)
    if (Reset==0)and(Default!=0): Reset=Default
    Name= getPrm(Reg,'names',['err'])[0]
    isArray = fromArray(Reg)
    if 'ro' in Access:
        if isArray:
            Line = 'wire %s %s;'%(widi(Wid),Name)
            LINES['split'].append(Line)
        else:
            Line = '    ,input %s %s'%(widi(Wid),Name)
            LINES[0].append(Line)

        if 'pulse' in Access:
            lastAddr = Reg.Addr
            Wid2 = Wid
            while Wid2>busWid:
                lastAddr += Jump
                Wid2 -= busWid
            if isArray:
                Line = 'wire %s_pulse;'%(Name)
                LINES['split'].append(Line)
            else:
                Line = '    ,output %s_pulse'%(Name)
                LINES[0].append(Line)
            if 'ready' in Reg.Params:
                Line = '    ,input %s_ready'%(Name)
                LINES[0].append(Line)
                LINES[9].append(Name)

            STR = ROPULSE
            Str = STR.replace('REG',Name)
            Str = Str.replace('ADDR',hex(lastAddr)[2:])
            LINES[4].append(Str)

        treatPrdata(Reg,Wid,Name)
    elif outAccess(Access):
        if isArray:
            Line = 'reg %s %s;'%(widi(Wid),Name)
            LINES['split'].append(Line)
        else:
            Line = '    ,output reg %s %s'%(widi(Wid),Name)
            LINES[0].append(Line)
        lastAddr = Reg.Addr
        Wid2 = Wid
        while Wid2>busWid:
            lastAddr += Jump
            Wid2 -= busWid
        if 'pulse' in Access:
            if not isArray:
                Line = '    ,output %s_pulse'%(Name)
                LINES[0].append(Line)
            else:
                Line = 'wire %s_pulse;'%(Name)
                LINES['split'].append(Line)
            STR = RWPULSE
            if 'ready' in Reg.Params:
                Line = '    ,input %s_ready'%(Name)
                LINES[0].append(Line)
                LINES[9].append(Name)
            Str = STR.replace('REG',Name)
            Str = Str.replace('ADDR',hex(lastAddr)[2:])
            LINES[4].append(Str)
        if 'wo' not in Access:
            treatPrdata(Reg,Wid,Name)
        if EnableWr!='none':
            pre_WRITE = '(%s && ' % EnableWr
            post_WRITE = ')'
        else:
            pre_WRITE = ''
            post_WRITE = ''
        if Wid<busWid:
            Line = '        if %s(mpaddr == \'h%x)%s %s <= (%s & ~mask[%d:0]) | (wdata[%d:0] & mask[%d:0]);'%(pre_WRITE,Reg.Addr,post_WRITE,Name,Name,Wid-1,Wid-1,Wid-1)
            LINES[3].append(Line)
        elif Wid==busWid:
            Line = '        if %s(mpaddr == \'h%x)%s %s <= (%s & ~mask) | (wdata & mask);'%(pre_WRITE,Reg.Addr,post_WRITE,Name,Name)
            LINES[3].append(Line)
        else:
            Wid1 = Wid
            Ad = Reg.Addr
            Hi,Lo = busWid-1,0
            Lim = busWid-1
            while Wid1>0:
                Line = '        if %s(mpaddr == \'h%x)%s %s[%d:%d] <= (%s[%d:%d] & ~mask[%d:%d]) | (wdata[%d:%d] & mask[%d:%d]);'%(pre_WRITE,Ad,post_WRITE,Name,Hi,Lo,Name,Hi,Lo,Lim,0 ,Lim,0,Lim,0)
                LINES[3].append(Line)
                Ad += Jump
                Lo += busWid
                Wid1 -= busWid
                Hi = min(Wid-1,Hi+busWid)
                Lim = min(Wid-1,busWid-1)


        Line = '        %s <= %d\'h%x;'%(Name,Wid,Reset)
        LINES[2].append(Line)

    elif Access in ['external','w1c']:
        Line = '    ,input %s %s'%(widi(Wid),Name)
        LINES[0].append(Line)
        if Access == 'w1c':
            Line = '    ,output %s %s_out_reg'%(widi(Wid),Name)
            LINES[0].append(Line)
            

        if Access=='external':
            LINES[0].append('    ,output  %s_rd_pulse'%(Name))
            LINES[0].append('    ,output  %s_wr_pulse'%(Name))
            treatPrdata(Reg,Wid,Name)
            Db['chip'].Params['external'] = True
        else:
#            Line0 = '    wire %s_rd_pulse;'%(Name)
#            Line1 = '    wire %s_wr_pulse;'%(Name)
            Line2 = '    reg %s %s_int;'%(widi(Wid),Name)
            Line3 = 'assign %s_out_reg = %s_int;'%(Name,Name)
            Str = W1C.replace('NAME',Name)
            if Wid>busWid:
                logs.log_error('#%d: W1C registers (%s : %sbits) are not geared for width>32. please split'%(Reg.Lnum,Name,Wid))
            Str = Str.replace('WID',str(Wid-1))
            RST = getPrm(Db['chip'],'reset','async')
            if RST=='async':
                Str = Str.replace('ASYNCRST','or negedge presetn')
            else:
                Str = Str.replace('ASYNCRST','')
            LINES[10].extend([Line2,Line3,Str])
            treatPrdata(Reg,Wid,Name+'_int')


        if (Access == 'external'):
            Str = ROPULSE.replace('assign REG','assign %s_rd'%Name)
            Str = Str.replace('REG',Name)
            Str = Str.replace('ADDR',hex(Reg.Addr)[2:])
            LINES[4].append(Str)

            Str = RWPULSE.replace('assign REG','assign %s_wr'%Name)
            Str = Str.replace('REG',Name)
            Str = Str.replace('ADDR',hex(Reg.Addr)[2:])
            LINES[4].append(Str)
        elif (Access == 'w1c'):
            Str = W1CPULSE.replace('REG',Name)
            Str = Str.replace('ADDR',hex(Reg.Addr)[2:])
            LINES[4].append(Str)

    else:
        logs.log_error('#%d: ACCESS not recognized "%s" of %s, valid accesses:  "rw ro w1c rw_pulse ro_pulse external"'%(Reg.Lnum,Access,Name))

def widi(WID):
    if type(WID) is int:
        if WID<2: return ''
        return '[%d:0]'%(WID-1)
    return '[%s-1:0]'%(WID)


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

    elif outAccess(Access):
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
    busWid = Db['chip'].Params['width']
    for Ind in range(Dep):
        Line = '    (mpaddr == \'h%x) ? %s :'%(Ad,expandBits(Name+'[%d]'%Ind,Wid,busWid))
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
    BusBytes = int(BusWidth/8)
    if BusBytes==8: AdShift = 3
    elif BusBytes==4: AdShift = 2

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

    if 'ready' in Reg.Params:
        Line = '    ,input %s_ready'%(Name)
        LINES[0].append(Line)
        LINES[9].append(('ram',Name))


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
    File = wopen('%s_defs.py'%(Module))
    File2 = wopen('%s_inc.seq'%(Module))
    File.write('ADDR_MAP = {}\n')
    File.write('WIDTH_MAP = {}\n')
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
    regfile_html.produce_md(Module,Db)
    regfile_html.produce_html(Module,Db)
    regfile_c.produce_c_headers(Module,Db)

APBHead = '''
`timescale 1ns / 1ps
module MODULE (input pclk, input presetn,
    input psel, input penable, input pwrite, input [WSTRB-1:0] pstrb, input [ADDWID-1:0] paddr, input [BUSWID-1:0] pwdata, output [BUSWID-1:0] prdata,output [BUSWID-1:0] prdata_wire
    ,output pready, output pslverr
'''
APBInst = '''
wire [1023:0] ZEROES = 1024'b0;
MODULE rgf (.pclk(pclk),.presetn(presetn),.pwrite(i_pwrite),.pread(i_pread),.paddr(paddr)
    ,.pwdata(pwdata),.prdata(prdata),.prdata_wire(prdata_wire)
    ,.pstrb(pstrb),.last_wdata(last_wdata)
    ,.penable(penable)
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
    Str = INSTANCE.replace('MODULE',Db['module'])
    Finst = wopen('%s.inst'%Db['module'])
    Finst.write(Str)
    apbHead()
    Temp = helper0(Finst)
    enclosingModule(Temp,Finst)
    dumpRam('_ram',Db['fout'],False)
    Finst.close()

def apbHead():
    Str = APBHead.replace('MODULE',Db['module'])
    missParam(Db['chip'].Params,'width',32)
    missParam(Db['chip'].Params,'addrwid',32)
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
    if 'external' in Db['chip'].Params:
        Db['fout'].write('    ,output [%s:0] last_wdata\n'%(Buswid-1))


def missParam(Dir,Param,Default):
    if Param in Dir: return
    Dir[Param]=Default
    if (type(Default) is int) and (Default > 1000):
        Default = hex(Default)
    logs.log_info('missingParam added %s = %s' % (Param,Default))


def helper0(Finst):
    Temp = []
    for Li in LINES[0]:
        Li = Li.replace(' reg ',' ')
        Wrds = Li.split()
        Reg = Wrds[-1]
#        print('HELPER0',Reg, (Wrds[-1] not in FIELDED_REGS),(Wrds[-1] in EXTERNAL_REGS), (Wrds[-1] in EXTERNAL_FIELDS))
        if (Wrds[-1] not in FIELDED_REGS)or(Wrds[-1] in EXTERNAL_REGS)or (Wrds[-1] in EXTERNAL_FIELDS):
            Db['fout'].write(Li+'\n')
            Finst.write('    ,.%s(%s)\n'%(Wrds[-1],Wrds[-1]))
        else:
            Li = Li.replace('input','wire')
            Li = Li.replace('output','wire')
            Li = Li.replace(',','')
            Li = Li + '; // hhh'
            Temp.append(Li)
    return Temp


def makePready():
    if LINES[9]==[]:
        return 'assign pready = 1;\n'
    else:
        Str = 'assign pready = \n'
        for Name in LINES[9]:
            if (type(Name) is tuple)and(Name[0]=='ram'):
                Str += '    (%s_wr_pulse || %s_rd_pulse) ? %s_ready :\n'%(Name[1],Name[1],Name[1])
            else:
                Str += '    %s_pulse ? %s_ready :\n'%(Name,Name)
        Str += '    1;\n'
        return Str


def enclosingModule(Temp,Finst):
    for Li in LINES[7]:
         Db['fout'].write('%s\n'%Li)
         wrds = Li.split()
         Finst.write('    ,.%s(%s)\n'%(wrds[-1],wrds[-1]))
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
            if (type(Name) is tuple)and(Name[0]=='ram'):
                Db['fout'].write('    (%s_wr_pulse || %s_rd_pulse) ? %s_ready :\n'%(Name[1],Name[1],Name[1]))
            else:
                Db['fout'].write('    %s_pulse ? %s_ready :\n'%(Name,Name))
        Db['fout'].write('    1;\n')
    if 'external' not in Db['chip'].Params:
        BusWid = Db['chip'].Params['width']
        Db['fout'].write('wire [%s:0] last_wdata;\n'%(BusWid-1))
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
    if 'wo' in Access: return True
    return False
def  inAccess(Access):
    if 'ro' in Access: return True
    return False



if __name__ == '__main__': main()


