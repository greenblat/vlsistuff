#! /usr/bin/env python3


import os,string,sys,types
instructions={}
inst_id=1
OpcodeWidth=25
Dnops={}
DmanualIfields={}
DmanualOpcodes={}
DnfSpecials = {}
Chip = 'chip'
def get_inst_id():
    global inst_id
    x = inst_id
    inst_id=inst_id+1
    return x

class Instruction:
    def __init__(self,Name):
        self.name=Name
        self.id=get_inst_id()
        self.coding=''
        self.pattern=''
        self.translate=''

def main():
    global Chip
    print('invocation: insts.py ChipName InstructionsFile')
    if len(sys.argv)>1:
        Chip = sys.argv[1]
    if len(sys.argv)>2:
        InstFileName = sys.argv[2]
    else:
        InstFileName = 'instructions.assigned'

    print('set: insts.py %s %s'%(Chip,InstFileName))
    File = open(InstFileName,'r')
    LLL = read_inst_file(File)
    for Item in LLL:
        deal_one_inst(Item)
    check_contentions()
    if (OpcodeWidth<17):
        check_usage()
    check_usage2()
    produce_verilog()
    produce_func_verilog()
    produce_disasm()
    produce_html(1)
    produce_html(2)
    produce_csv()
    produce_asm_driver()
    produce_py_simulator()
    produce_c_decoder()
    produce_c_simulator()
    produce_c_instr_list()
    produce_scheme()
    






Header0 = '''
def exr(Int,High,Wid):
    Low = High-Wid+1
    Mask = (1<<Wid)-1
    Res = (Int>>Low)&Mask
    return Res


def instructions_scheduler(cpu,opcode):
'''

def produce_py_simulator():
    ofile=open('%s_decoder.py'%(Chip),'w')
    ofile.write(Header0)
    prefi = ''
    for Inst in instructions:
        Coding = instructions[Inst].coding
        (Mask,Data)=build_expr(Coding)
        ofile.write('    %sif ((opcode & 0x%s)==0x%s):\n'%(prefi,Mask[4:],Data[4:]))
        prefi='el'
        wrds = gather_fields(Inst,Coding)
        res=[]
        (Fields,names)=get_good_names(wrds)
        for Name in Fields:
            L1 = names[Name]
            if (len(L1)==1):
                (x_,Offset,Width) = L1[0]
                res = res + ['exr(opcode,%d,%d)'%(Offset,Width)]
            else:
                part=[]
                L1.sort()
                L1.reverse()
                for (x_,O,W) in L1:
                    part = part + [str(O-W+1),str(W)]
                prts = ','.join(part)
                res = res + ['exr%d(opcode,%s)'%(len(part)/2,prts)]

        ofile.write('        cpu.execute_%s(%s)\n'%(Inst,','.join(res)))
    ofile.write('    else: cpu.execute_illegal(opcode)\n')
    for Inst in instructions:
        Coding = instructions[Inst].coding
        wrds = gather_fields(Inst,Coding)
        (Fields,names)=get_good_names(wrds)
        res=[]
        for Name in Fields:
            res = res + [Name]
        Prms = ','.join(['self']+res)
        ofile.write('def execute_%s(%s):\n'%(Inst,Prms))
        ofile.write('    notImplemented("%s","%s",%s)\n'%(Inst,Prms,Prms))
        ofile.write('    return\n')

    ofile.close()

def get_good_names(wrds):
    names={}
    orders = []
    for NameOffsetWidth in wrds:
        (Name,Offset,Width) = NameOffsetWidth
        if ('[' in Name):
            x = Name.index('[')
            s1 = Name[x+1:-1]
            s2 = s1.split(':')
            Hi = int(s2[0])
            Name = Name[:x]
        else:
            Hi=0
        if (Name in names):
            L1 = names[Name]
            names[Name]=L1+[(Hi,Offset,Width)]
        else:
            names[Name]=[(Hi,Offset,Width)]
            orders = orders + [Name]
#    Fields = names.keys()
#    Fields.sort()
    return (orders,names)

def get_good_names_no_sort(wrds):
    names={}
    for NameOffsetWidth in wrds:
        (Name,Offset,Width) = NameOffsetWidth
        if ('[' in Name):
            x = Name.index('[')
            s1 = Name[x+1:-1]
            s2 = s1.split(':')
            Hi = int(s2[0])
            Name = Name[:x]
        else:
            Hi=0
        if (Name in names):
            L1 = names[Name]
            names[Name]=L1+[(Hi,Offset,Width)]
        else:
            names[Name]=[(Hi,Offset,Width)]
    Fields = names.keys()
    # Fields.sort()
    return (Fields,names)

def gather_fields(Inst,Coding):
    Coding1=toAsm(Inst,Coding)
    return Coding1
        
def produce_disasm():
    opyfile=open('%s_disasm.py'%(Chip),'w')
    opyfile.write('#! /usr/bin/env python3\n')
    opyfile.write('import os,sys,string\n')
    opyfile.write('codings={}\n')
    Keys = instructions.keys()
    for Name in Keys:
        Coding =  instructions[Name].coding
        opyfile.write('codings["%s"]=%s\n'%(Name,str(Coding)))

    opyfile.write('def disasm(Code):\n')
    Rep = "%d'h"%OpcodeWidth
    for Name in Keys:
        if ok_name(Name):
            (Mask,Data)=build_expr(instructions[Name].coding)
            opyfile.write('    if ((Code & %s)==%s):\n'%(Mask.replace(Rep,'0x'),Data.replace(Rep,'0x')))
            opyfile.write('         return "%s %%s"%%(fields_extr(Code,codings["%s"]))\n'%(Name,Name))

    opyfile.write('    return "*%08x"%(Code)\n')
    opyfile.write('OpcodeWidth = %d\n'%OpcodeWidth)
    opyfile.write(DISASMSTRING)
    opyfile.close()

DISASMSTRING = """
def int2bin(Int,Len):
    if (Int==0):
        res= '0' 
        while (len(res)<Len):
            res = '0'+res
        return res 
    res = ''
    while (Int):
        if (Int&1):
            res = '1'+res 
        else:   
            res = '0'+res 
        Int=Int>>1
    while (len(res)<Len):
        res = '0'+res
    return res 


def fields_extr(Code,List):
    Fields={}
    Str = int2bin(Code,OpcodeWidth)
    L1 = list(Str)
    for i in range(OpcodeWidth):
        Tok = List[i]
        if (Tok[0] not in '01'):
            Bit = int(L1[i],2)
            if ('[' in Tok):
                ww = Tok.split('[')
                Key = ww[0]
                Ind = int(ww[1][:-1])
                if Key not in Fields:
                    Fields[Key]=0
                Fields[Key] |= (Bit<<Ind)
            else:
                Fields[Tok]=Bit
    res=''
    for Key in Fields:
        res += ' %s=0x%x'%(Key,Fields[Key])

    return res 

def main():
    Fname = sys.argv[1]
    if len(sys.argv)>2:
        Foutname = sys.argv[2]
    else:
        Foutname = 'dis.listing'
    print('i take rom file "%s"  as input file and produce "%s" as output'%(Fname,Foutname))
    load_rom(Fname)
    Fout=open(Foutname,'w')
    run_disasm(Fout)
    Fout.close()

def run_disasm(Fout):
    for Addr,Code in enumerate(Program):
        Txt2 = disasm(Code)
        Str = '0x%04x : %08x  %s\\n'%(Addr,Code,Txt2)
        print(Str),
        Fout.write(Str)

Program=[]
def load_rom(Fname):
    File = open(Fname)
    Addr=0
    while 1:
        line = File.readline()
        if (len(line)==0):
            return
        if "//" in line: line=line[:line.index("//")]
        wrds = line.split()
        for wrd in wrds:
            if (wrd[0]=='@'):
                Addr = int(wrd[1:],16)
            else:
                Data = int(wrd,16)
                while len(Program)<=Addr:
                    Program.append(0)
                Program[Addr]=Data
                Addr += 1

if __name__=='__main__':
    main()

"""


def produce_verilog():
    ofile=open('%s_decoder.v'%(Chip),'w')
    ofile2 = open('%s_h.py'%(Chip),'w')
    ifile=open('%s_decoder.inst'%(Chip),'w')
    ifile.write('wire pvalidXX; wire [%d:0] popcodXX; \n'%(OpcodeWidth-1))
    ofile.write('module %s_decoder(input [%d:0] opcode,input valid,output not_opcode\n'%(Chip,OpcodeWidth-1))
    Fields = collect_fields()
    Flags = collect_flags()
    Keys = instructions.keys()
    III = ['%s_decoder XX%s_decoder (.valid(pvalidXX),.opcode(popcodXX),.version_code(version_code)\n'%(Chip,Chip)]
    for Name in Keys:
        if ok_name(Name):
            ofile.write(',output %s_code\n'%(Name))
            if Name=='nop':
                ofile.write(',output [%s:0] nop_opcode\n'%(OpcodeWidth-1))
                
            ifile.write('wire XX%s_code;\n'%(Name))
            III.append('   ,.%s_code(XX%s_code)\n'%(Name,Name))
    for Name in Fields:
        if ok_name(Name)and(Name!='x'):
            if (Fields[Name]==0):
                ofile.write(',output %s_field\n'%(Name))
                ifile.write('wire XX%s_field;\n'%(Name))
                III.append('   ,.%s_field(XX%s_field)\n'%(Name,Name))
            else:
                (H,L)=Fields[Name]
                ofile.write(',output [%d:%d] %s_field\n'%(H,L,Name))
                ifile.write('wire [%d:%d] XX%s_field;\n'%(H,L,Name))
                III.append('   ,.%s_field(XX%s_field)\n'%(Name,Name))
    for Name in Flags:
        ofile.write(',output %s_flag\n'%(Name))
        ifile.write('wire XX%s_flag;\n'%(Name))
        III.append('   ,.%s_flag(XX%s_flag)\n'%(Name,Name))
    ofile.write(');\n')
    GoodOpCodes = []
    for Name in Keys:
        if ok_name(Name):
            (Mask,Data)=build_expr(instructions[Name].coding)
            Name1 = Name.upper()
            ofile2.write('global %s\n'%(Name1))
            ofile2.write('%s = %s\n'%(Name1,Data.replace("16'h",'0x')))
            ofile2.write('MASK_%s = %s\n'%(Name1,Mask.replace("16'h",'0x')))
            if instructions[Name].cond!='':
                Cond = instructions[Name].cond
                if '=' not in  Cond:
                    Cond = '&&(%s_field!=0)'%instructions[Name].cond
            else:
                Cond = ''

            ofile.write('assign %s_code = valid && ((opcode & %s)==%s) %s;\n'%(Name,Mask,Data,Cond))
            if Name=='nop':
                ofile.write('assign nop_opcode = %s;\n'%(Data))
            GoodOpCodes.append(Name+'_code')
                
    Str = ' ||'.join(GoodOpCodes)
    ofile.write('assign not_opcode = !(\n')
    while len(Str)>80:
        x = 60;
        while Str[x]!=' ': x += 1
        Bef = Str[:x]
        Str = Str[x:]
        ofile.write('    %s\n'%(Bef))
            

    ofile.write('    %s);\n'%Str)

    for Name in Fields:
        if ok_name(Name)and(Name!='x'):
            if (Fields[Name]==0):
                Expr=build_field_expr(Name)
                ofile.write('assign %s_field = %s;\n'%(Name,Expr))
            else:
                (H,L)=Fields[Name]
                for Ind in range(L,H+1):
                    Expr=build_field_expr('%s[%d]'%(Name,Ind))
                    ofile.write('assign %s_field[%d] = %s;\n'%(Name,Ind,Expr))
    for Name in Flags:
        res=[]
        for Inst in Flags[Name]:
            res = res + [Inst+'_code']
        txt = ' ||'.join(res)
        ofile.write('assign %s_flag = valid && (%s);\n'%(Name,txt))
    ofile.write('endmodule\n\n')
    ofile.close()
    ofile2.close()
    for Line in III:
        ifile.write(Line)
    ifile.write(');\n')
    ifile.close()



def produce_func_verilog():
    ofile=open('%s_func_decoder.v'%(Chip),'w')
    ofile.write('module %s_decoder(input [%d:0] opcode,input valid);\n'%(Chip,OpcodeWidth-1))
    Fields = collect_fields()
    Flags = collect_flags()
    Keys = instructions.keys()

#    for Name in Keys:
#        if ok_name(Name):
#            ofile.write(',output %s_code\n'%(Name))
#

#    for Name in Fields:
#        if ok_name(Name)and(Name!='x'):
#            if (Fields[Name]==0):
#                ofile.write(',output %s_field\n'%(Name))
#            else:
#                (H,L)=Fields[Name]
#                ofile.write(',output [%d:%d] %s_field\n'%(H,L,Name))
#    for Name in Flags:
#        ofile.write(',output %s_flag\n'%(Name))
#    ofile.write(');\n')
#    for Name in Keys:
#        if ok_name(Name):
#            (Mask,Data)=build_expr(instructions[Name].coding)
#            ofile.write('assign %s_code = valid && ((opcode & %s)==%s);\n'%(Name,Mask,Data))
    for Name in Fields:
        if (Fields[Name]==0):
            Wids =''
        else:
            (H,L)=Fields[Name]
            Wids = '[%d:%d]'%(H,L)
        ofile.write('function %s field_%s(input [%d:0] opcode);\n'%(Wids,Name,OpcodeWidth-1))
        ofile.write('begin\n')
        if ok_name(Name)and(Name!='x'):
            if (Fields[Name]==0):
                Expr=build_func_field_expr(Name)
                ofile.write('    field_%s = %s;\n'%(Name,Expr))
            else:
                (H,L)=Fields[Name]
                for Ind in range(L,H+1):
                    Expr=build_func_field_expr('%s[%d]'%(Name,Ind))
                    ofile.write('    field_%s[%d] = %s;\n'%(Name,Ind,Expr))
        ofile.write('end\n')
        ofile.write('endfunction\n')
    for Name in Flags:
        ofile.write('function flag_%s(input [%d:0] opcode,input valid);\n'%(Name,OpcodeWidth-1))
        ofile.write('begin\n')
        res=[]
        for Inst in Flags[Name]:
            (Mask,Data)=build_expr(instructions[Inst].coding)
            this = '((opcode & %s)==%s)'%(Mask,Data)
            res = res + [this]
        txt = ' ||'.join(res)
        ofile.write('flag_%s = valid && (%s);\n'%(Name,txt))
        ofile.write('end\n')
        ofile.write('endfunction\n')
    ofile.write('endmodule\n')
    ofile.close()

def opcode_expr(Inst):
   (Mask,Data)=build_expr(instructions[Inst].coding)
   this = '((opcode & %s)==%s)'%(Mask,Data)
   return this


def ok_name(Name):
    if (len(Name)>len('unused'))and(Name[0:len('unused')]=='unused'):
        return 0
    return 1
def build_field_expr(Name):
    gotit={}
    for Inst in instructions:
        ind=OpcodeWidth-1
        for Id in instructions[Inst].coding:    
            if ok_name(Inst):
                if (Id==Name):
                    if (ind in gotit):
                        Was = gotit[ind]
                        gotit[ind]=Was+[Inst+'_code']
                    else:
                        gotit[ind]=[Inst+'_code']
                ind=ind-1
    if (len(gotit.keys())==1):    
        ll = list(gotit.keys())
        return 'opcode[%s]'%(ll[0])
    inds  = list(gotit.keys())
    res=''
    for ind in inds:
        insts = gotit[ind]
        insts1 = '||'.join(insts)
        res = res + '||(opcode[%s] && (%s))'%(ind,insts1)


    return res[2:]

def build_func_field_expr(Name):
    gotit={}
    for Inst in instructions:
        ind=OpcodeWidth-1
        for Id in instructions[Inst].coding:    
            if ok_name(Inst):
                if (Id==Name):
                    if (ind in gotit):
                        Was = gotit[ind]
                        gotit[ind]=Was+[Inst]
                    else:
                        gotit[ind]=[Inst]
                ind=ind-1
    inds  = gotit.keys()
    res=''
    for ind in inds:
        insts = gotit[ind]
        insts2 = []
        for Inst in insts:
            Expr = opcode_expr(Inst)
            insts2 += [Expr]
        
        insts1 = '||'.join(insts2)
        res = res + '||(opcode[%s] && (%s))'%(ind,insts1)
    return res[2:]

def collect_fields():
    fields={}
    for Inst in instructions:
        Coding = instructions[Inst].coding
        for X in Coding:
            if (X not in ['0','1']):
                if ('[' in X):
                    (Bus,Ind)=extract_bus(X)                    
                    if Bus in fields:
                        XX = fields[Bus]
                        if (XX==0):
                            catch_error('field names collide',Inst+' '+Bus)
                        (H,L)=fields[Bus]
                        fields[Bus]=(max(H,Ind),min(L,Ind))
                    else:
                        fields[Bus]=(Ind,Ind)
                else:
                    fields[X]=0
    return fields


def collect_flags():
    flags={}
    for Inst in instructions:
        for flag in instructions[Inst].flags:
            if (flag in flags):
                flags[flag]=flags[flag]+[Inst]
            else:
                flags[flag]=[Inst]

    return flags

def collect_inst_fields(Coding):
    fields={}
    for X in Coding:
        if (X not in ['0','1']):
            if ('[' in X):
                (Bus,Ind)=extract_bus(X)                    
                if fields.has_key(Bus):
                    (H,L)=fields[Bus]
                    fields[Bus]=(max(H,Ind),min(L,Ind))
                else:
                    fields[Bus]=(Ind,Ind)
            else:
                fields[X]=0
    return fields

def extract_bus(Txt):
    x = Txt.index('[')
    Bus = Txt[0:x]
    Ins = Txt[x+1:-1]
    return (Bus,int(Ins))
    

def build_expr(Coding):
    mask=''
    data=''
    for X in Coding:
        if (X=='1'):
            mask=mask+'1'
            data=data+'1'
        elif (X=='0'):
            mask=mask+'1'
            data=data+'0'
        else:
            mask=mask+'0'
            data=data+'0'
    return ( str(OpcodeWidth)+"'h"+bin2hex(mask),str(OpcodeWidth)+"'h"+bin2hex(data) )

header_string = '\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">\n\
<html>\n\
  <head>\n\
    <title>CHIPCHIP instruction set </title>\n\
  </head>\n\
\n\
  <body>\n\
    <center>\n\
\n\
      <h1>CHIPCHIP instruction set</h1>\n\
\n\
'

table_header_string = '\
      <table border>\n\
      <tr>\n\
        <td align="center"><b>opcode</b></td>\n\
        <td colspan=OPCODEWIDTH align="center"><b>data bits</b></td>\n\
        <td align="center"><b>comment</b></td>\n\
      </tr>\n\
'


tail_string = '</table> </center> </body> </html>\n\n'
def switch_colors():
    global color,othercolor
    x = color
    color=othercolor
    othercolor=x


def produce_csv():
    File = open('%s_table.csv'%(Chip),'w')
    File.write('id,inst,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0,comment\n')
    explanation = ''
    lll=[]
    for Inst in instructions:
        lll = lll + [(instructions[Inst].id,Inst)]
    lll.sort()
    for (id,Inst) in lll:
        File.write('%s,%s'%(id,Inst))
        run_on_csv_coding(instructions[Inst].coding,File)
        expl = instructions[Inst].oneliner.replace('.',' ')
        File.write(',%s\n'%expl)
    File.close()

def produce_html(Which):
    global color,othercolor
    ofile = open('%s_table%d.html'%(Chip,Which),'w')
    ofile.write(header_string.replace('CHIPCHIP',Chip))
    ofile.write(table_header_string.replace('OPCODEWIDTH',str(OpcodeWidth)))
    color = '#ffa0ff'
    othercolor = '#ffffa0'
    instruction = 'bits'
    color = '#80ff80'
    othercolor = '#ffffa0'
    rng = list(range(0,OpcodeWidth))
    rng.reverse()
    origarr=[]
    for x in rng:
        origarr = origarr + [str(x)]
    ofile.write('<tr bgcolor='+color+'> <td>'+instruction+'</td>\n')
    run_on_coding(origarr,ofile)

    explanation = ''
    lll=[]
    for Inst in instructions:
        lll = lll + [(instructions[Inst].id,Inst)]
    lll.sort()
    if (Which==1):
        for (id,Inst) in lll:
            if ok_name(Inst):
                acolor = instructions[Inst].color
                if acolor!='none': 
                    acolor='#'+acolor
                else:
                    acolor=color
                ofile.write('<tr bgcolor='+acolor+'> <td><a target="_blank" href="file:chip_doc.html/#'+Inst+'">'+Inst+'</a></td>\n')
                run_on_coding(instructions[Inst].coding,ofile)
                expl = instructions[Inst].oneliner.replace('.',' ')
                ofile.write('<td align="center">'+expl+'</td>\n')
                ofile.write('</tr>\n')
                switch_colors()
    else:
        Insts = []
        for (id,Inst) in lll:
            if ok_name(Inst):
                Insts = [Inst]+Insts
        Insts.sort()
        for Inst in Insts:
            for (id,Inst2) in lll:
                if (Inst2==Inst):
                    acolor = instructions[Inst].color
                    if acolor!='none': 
                        acolor='#'+acolor
                    else:
                        acolor=color
                    ofile.write('<tr bgcolor='+acolor+'> <td><a target="_blank" href="file:chip_doc.html#'+Inst+'">'+Inst+'</a></td>\n')
                    run_on_coding(instructions[Inst].coding,ofile)
                    expl = instructions[Inst].oneliner.replace('.',' ')
                    ofile.write('<td align="center">'+expl+'</td>\n')
                    ofile.write('</tr>\n')
                    switch_colors()



    ofile.write(tail_string)
    ofile.close()

def get_inst_explanation(Inst):
    return '???'

def run_on_csv_coding(wrds,File):
#    wrds = gather_busses(wrds)
    for word in wrds:
        if (word=='1'):
            File.write(',1')
        elif (word=='0'):
            File.write(',0')
        elif (type(word) is str):
            File.write(',%s'%str(word))
        elif (type(word) is tuple):
            (Bus,ind1,ind2)=word
            text = '%s[%d:%d]'%(Bus,ind1,ind2)
            many = ind1-ind2+1
            File.write(',%s'%str(many))
        else:
            print('error! ilia, coding field bad ',word, wrds)


def run_on_coding(wrds,ofile):
    wrds = gather_busses(wrds)

    for word in wrds:
        if (word=='1'):
            ofile.write('<td align="center">'+str(word)+'</td>\n')
        elif (word=='0'):
            ofile.write('<td align="center">'+str(word)+'</td>\n')
        elif (type(word) is str):
             ofile.write('<td align="center" >'+str(word)+'</td>\n')
        elif (type(word) is tuple):
            (Bus,ind1,ind2)=word
            text = '%s[%d:%d]'%(Bus,ind1,ind2)
            many = ind1-ind2+1
            ofile.write('<td  align="center" colspan='+str(many)+'>'+text+'</td>\n')
        else:
            print('error! ilia, coding field bad ',word, wrds)

def gather_busses(wrds):
    res = []
    state='idle'
    for word in wrds:
        if (state=='idle'):
            if ('[' in word):
                state='bus'
                x = word.index('[')
                Bus = word[:x]
                St=int(word[x+1:-1])
                En=St
            else:
                res = res + [word]
        elif (state=='bus'):
            if ('[' in word):
                state='bus'
                x = word.index('[')
                Bus1 = word[:x]
                Here=int(word[x+1:-1])
                if (Here==(En-1))and(Bus1==Bus):
                    En=Here
                else:
                    res = res + [(Bus,St,En)]
                    Bus=Bus1
                    St=Here
                    En=Here
            else:
                res = res + [(Bus,St,En)]
                res = res + [word]
                state='idle'
    if (state=='bus'):
        res = res + [(Bus,St,En)]
    return res

def produce_scheme():
    kinds={}
    ofile=open('%s.inc'%(Chip),'w')
    ofile.write('; -*- Scheme -*-\n')
    fields = {}
    comes_from={}
    for Inst in instructions:
        Coding=instructions[Inst].coding
        wrds = gather_fields(Inst,Coding)
        (Fields,names)=get_good_names(wrds)
        for Key in names:
            L1 = names[Key]
            (A,St,Wid)=L1[0]
            Str = '%s%d_%d'%(Key,Wid,St+Wid-1)
            Kind = get_field_kind(Inst,Key)
            fields[Str]=(St,Wid)
            comes_from[Str]=(Inst,Key)
            Key='%s %d %d'%(Str,St,Wid)
            if Key in kinds:
                (Was,Winst) = kinds[Key]
                if (Was!=Kind):
                    print('error kind collision field=(%s) new=%s / %s old= %s / %s'%(Key,Inst,Kind,Winst,Was))
            kinds['%s %d %d'%(Str,St,Wid)]=(Kind,Inst)
    for Field in fields:
        (St,Wid)= fields[Field]
        (Kind,Winst)=kinds['%s %d %d'%(Field,St,Wid)]
        Manual = is_it_manual(Field,comes_from[Field])
        (I,K)=comes_from[Field]
        Special = get_dnf_special(I,K)
        if (Manual):
            ofile.write(';manual ')
        if (Kind=='sint'):
            ofile.write('(df f-%s "%s" (%s) %d %d INT #f #f )\n'%(Field,Field,Special,St+Wid-1,Wid))
        else:
            ofile.write('(dnf f-%s "%s" (%s) %d %d)\n'%(Field,Field,Special,St+Wid-1,Wid))
    for Field in fields:
        (St,Wid)= fields[Field]
        (Kind,Winst)=kinds['%s %d %d'%(Field,St,Wid)]
        Manual = is_it_manual_opcode(Field,comes_from[Field])
        if (Manual):
            ofile.write(';manual ')
        ofile.write('(dnop %s "%s" () h-%s  f-%s)\n'%(Field,Field,Kind,Field))

    opcodes={}
    for Inst in instructions:
        Coding=instructions[Inst].coding
        (Wid,Id)=get_constants(Coding)
        if Wid in opcodes:
            was = opcodes[Wid]
        else:
            was = []
        opcodes[Wid] = was + [(Id,Inst)]

    for Wid in opcodes:
        ofile.write('(dnf f-opc%d "opcode %d-bits field" () 31 %d);\n'%(Wid,Wid,Wid))

    for Wid in opcodes:
        ofile.write('(define-normal-insn-enum insn-opc%d "opc enums" () OPC%d_ f-opc%d (\n'%(Wid,Wid,Wid))
        for (Id,Inst) in opcodes[Wid]:
            if (Id>1000):
                ofile.write('     ("%s" #x%x)\n'%(Inst,Id))
            else:
                ofile.write('     ("%s" %d)\n'%(Inst,Id))
        ofile.write('))\n')

    for Inst in instructions:
        Coding=instructions[Inst].coding
        wrds = gather_fields(Inst,Coding)
        (Fields,names)=get_good_names(wrds)
        (Wid,Id)=get_constants(Coding)
        ofile.write('(dni %s\n'%(Inst))
        ofile.write('     "%s"\n'%(instructions[Inst].oneliner.replace('.',' ')))
        if (len(Fields)>0):
            ofile.write('     (%s'%('NO-DIS'))
            if (Inst in Dnops):
                DIS = Dnops[Inst]
                ofile.write('  %s'%(DIS))
            ofile.write(')\n')
        else:
            ofile.write('    ()\n')
        ofile.write('     "%s'%(Inst))
        Psik=' '
        for Key in Fields:
            L1 = names[Key]
            (A,St,Wid1)=L1[0]
            Str = '%s%d_%d'%(Key,Wid1,St+Wid1-1)
            ofile.write('%s$%s'%(Psik,Str))
            Psik=','
        ofile.write('"\n')
        ofile.write('     (+ OPC%d_%s'%(Wid,Inst))
        for Key in Fields:
            L1 = names[Key]
            (A,St,Wid1)=L1[0]
            Str = '%s%d_%d'%(Key,Wid1,St+Wid1-1)
            ofile.write(' %s'%(Str))
        ofile.write(')\n')
        ofile.write('    (nop)\n')
        ofile.write('    ()\n')
        ofile.write(')\n')

    ofile.close()    

def is_it_manual(Field,Tuple):
    (Inst,Key)=Tuple
    Ok = Inst+'+'+Key
    if (Key in DmanualIfields):
        return True
    if (Ok in DmanualIfields):
        return True
    return False

def is_it_manual_opcode(Field,Tuple):
    (Inst,Key)=Tuple
    Ok = Inst+'+'+Key
    if (Key in DmanualOpcodes):
        return True
    if (Ok in DmanualOpcodes):
        return True
    return False





def get_field_kind(Inst,Field):
    if (Field in Dnops):
        return Dnops[Field]

    if (Inst+'+'+Field in Dnops):
        return Dnops[Inst+'+'+Field]

    return 'uint'


def get_dnf_special(Inst,Field):
    if (Field in DnfSpecials):
        return DnfSpecials[Field]

    if (Inst+'+'+Field in DnfSpecials):
        return DnfSpecials[Inst+'+'+Field]

    return ''



def get_constants(Coding):
    res = []
    for X in Coding:
        if (X in ['0','1']):
            res = res + [X]
    X = ''.join(res)
    Id = bin2int(X)
    return (len(res),Id)

def produce_asm_driver():
    ofile=open('%s_asm_coding.py'%(Chip),'w')
    ofile.write('Coding={}\n')
    ofile.write('def init_coding(add_coding):\n')
    for Inst in instructions:
        Pattern=instructions[Inst].pattern
        Translate=instructions[Inst].translate
        Coding=instructions[Inst].coding
        Coding1=toAsm(Inst,Coding)
        (Mask,Data)=build_expr(Coding)
        Flags = ','.join(instructions[Inst].flags)
#        ofile.write('Coding["%s"]=(0x%s,%s)\n'%(Inst,Data[4:],Coding1))
        ofile.write('    add_coding("%s",0x%s,%s,"%s","%s","%s")\n'%(Inst,Data[4:],Coding1,Pattern,Translate,Flags))
    ofile.close()    




def toAsm(Inst,Coding):
    wrds = gather_busses(Coding)
    pos=OpcodeWidth-1
    res=[]
    for i in range(0,len(wrds)):
        if (wrds[i] in ['0','1']):
            pos=pos-1
        elif (type(wrds[i]) is str):
            res = res+[(wrds[i],pos,1)]
            pos=pos-1
        elif (type(wrds[i]) is tuple):
            (Bus,ind1,ind2)=wrds[i]
            many = ind1-ind2+1
            res = res+[('%s[%d:%d]'%(Bus,ind1,ind2),pos,many)]
#            res = res+[('%s[%d:%d]'%(Bus,ind1,ind2),many-1,many)]
            pos=pos-many
    return res



def produce_c_decoder():
    ofile=open('osim_%s_dis_template.c'%(Chip),'w')
    for Inst in instructions:
        Coding = instructions[Inst].coding
        Fields = toC(Inst,Coding)
        res=[]
        for fld in Fields:
            (fldname,pos,wid)=fld
            res = res + [fldname]
        if len(res)>0:
           ofile.write('static void osim_opal_dis_%s(uint32_t %s)\n'%(Inst,', uint32_t '.join(res)))
        else:
           ofile.write('static void osim_opal_dis_%s(void)\n'%(Inst))
        ofile.write('{\n')
        ofile.write('        opal->parms.print("%s is not supported\\n");\n'%(Inst))
        ofile.write('}\n\n')
    ofile.close()

    ofile=open('osim_%s_dis_driver_h.c'%(Chip),'w')
    ofile.write('int osim_dis_instr(uint32_t instr)\n')
    ofile.write('{\n')
    ofile.write('        int rc=0;\n')
    prefi = ''
    for Inst in instructions:
        Coding = instructions[Inst].coding
        (Mask,Data)=build_expr(Coding)
        ofile.write('        %sif ((instr & 0x%s)==0x%s)\n'%(prefi,Mask[4:],Data[4:]))
        prefi='else '
        Fields = toC(Inst,Coding)
        res=[]
        for fld in Fields:
            (fldname,pos,wid)=fld
            res = res + ['field(instr,%d,%d)'%(pos,wid)]

        ofile.write('                osim_opal_dis_%s(%s);\n'%(Inst,','.join(res)))
    ofile.write('        else\n')
    ofile.write('        {\n')
    ofile.write('                opal->parms.print("%x*invalid*\\n", instr);\n')
    ofile.write('                rc = -EINVAL;\n')
    ofile.write('        }\n')
    ofile.write('        return rc;\n')
    ofile.write('}\n')
    ofile.close()


def produce_c_simulator():
    ofile=open('osim_%s_exec_template.c'%(Chip),'w')
    for Inst in instructions:
        Coding = instructions[Inst].coding
        Fields = toC(Inst,Coding)
        res=[]
        for fld in Fields:
            (fldname,pos,wid)=fld
            res = res + [fldname]
        if len(res)>0:
            ofile.write('static int osim_opal_exec_%s(struct osim_opal *_opal, uint32_t %s)\n'%(Inst,', uint32_t '.join(res)))
        else:
            ofile.write('static int osim_opal_exec_%s(struct osim_opal *_opal)\n'%(Inst))
        ofile.write('{\n')
        ofile.write('        opal->parms.print("%s is not supported\\n");\n'%(Inst))
        ofile.write('        return -EINVAL;\n')
        ofile.write('}\n\n')
    ofile.close()

    ofile=open('osim_%s_exec_driver_h.c'%(Chip),'w')
    ofile.write('int osim_exec_instr(struct osim_opal *_opal, uint32_t instr)\n')
    ofile.write('{\n')
    ofile.write('        int rc=-EINVAL;\n')
    prefi = ''
    for Inst in instructions:
        Coding = instructions[Inst].coding
        (Mask,Data)=build_expr(Coding)
        ofile.write('        %sif ((instr & 0x%s)==0x%s)\n'%(prefi,Mask[4:],Data[4:]))
        prefi='else '
        Fields = toC(Inst,Coding)
        res=[]
        for fld in Fields:
            (fldname,pos,wid)=fld
            res = res + ['field(instr,%d,%d)'%(pos,wid)]

        if len(res)>0:
            ofile.write('                rc = osim_opal_exec_%s(_opal,%s);\n'%(Inst,','.join(res)))
        else:
            ofile.write('                rc = osim_opal_exec_%s(_opal);\n'%(Inst))
    ofile.write('        else\n')
    ofile.write('                OSIM_RUN_ERR(_opal, "***Invalid instruction\\n", instr);\n')
    ofile.write('        return rc;\n')
    ofile.write('}\n')
    ofile.close()


def toC(Inst,Coding):
    wrds = gather_busses(Coding)
    pos=OpcodeWidth-1
    res=[]
    for i in range(0,len(wrds)):
        if (wrds[i] in ['0','1']):
            pos=pos-1
        elif (type(wrds[i]) is str):
            res = res+[(wrds[i],pos,1)]
            pos=pos-1
        elif (type(wrds[i]) is tuple):
            (fname,ind1,ind2)=wrds[i]
            many = ind1-ind2+1
            res = res+[(fname,pos-many+1,many)]
            pos=pos-many
        
    return res

def produce_c_instr_list():
    ofile=open('%s_instructions.h'%(Chip),'w')
    ofile.write('#ifndef OPAL_INSTRUCTIONS_H\n')
    ofile.write('#define OPAL_INSTRUCTIONS_H\n')
    ofile.write('typedef enum {\n')
    for Inst in instructions:
        ofile.write('        opal_instr_%s,\n'%(Inst))
    ofile.write('} opal_instr;\n')
    ofile.write('#endif\n')
    ofile.close()

def check_usage2():
    Total = 1<<OpcodeWidth
    Names = instructions.keys()
    UsedTotal=0
    for Inst in Names:
        Coding = instructions[Inst].coding
        res=0
        for Chr in Coding:
            if Chr in ['0','1']:
                res += 1
        UsedLocal = 1<<(OpcodeWidth-res)
        UsedTotal+= UsedLocal
    print('checkUsage2 total=%d used=%d free=%d'%(Total,UsedTotal,Total-UsedTotal))

def check_usage():
    global useds
    useds=list(range(0,1<<OpcodeWidth))
    for i in useds:
        useds[i]=0
    print('check_usage step=0')
    Names = instructions.keys()
    for Inst in Names:
        Coding = instructions[Inst].coding
        register_used(Coding,0)
    print('check_usage step=1')
    print_unused()
    print('check_usage step=2')


def register_used(code,sofar):
    global useds
    if (len(code)==0):
        useds[sofar]=useds[sofar]+1
        return  
    if (code[-1]=='0'):
        register_used(code[:-1],sofar*2)
    elif (code[-1]=='1'):
        register_used(code[:-1],sofar*2+1)
    else:   
        register_used(code[:-1],sofar*2)
        register_used(code[:-1],sofar*2+1)

    
def print_unused():
    nons=0  
    baby=[] 
    for i in range(0,len(useds)):
        if (useds[i]==0):
            baby = baby + [int2bin(i,OpcodeWidth)]
            nons=nons+1
    print('we have %d not useds opcodes (baby=%d)'%(nons,len(baby)))
    return
    baby = compressbin_round(baby,0)
    print('baby %d'%(len(baby)))
    baby = compressbin_round(baby,0)
    print('baby %d'%(len(baby)))
    total=0
    for b in baby:
        xfr = binfree(b)
        total = total + xfr
        b0 = b.replace('',' ')
        b1 = b0.split()
        b1.reverse()
        print(''.join(b1),'  ',xfr)
    print('total free', total)

def binfree(In):
    res = 1
    for ch in In:
        if (ch=='x'):
            res = res *2
    return res



def int2bin(Int,Wid):
    res = ['0','0','0','0']
    res = res + res + res + res
    res = res + res
    for i in range(0,32):
        x = Int & (1<<i)
        if (x):
            res[31-i] = '1'
    res = res[32-Wid:]
    return ''.join(res)

def compressbin_round(In,Pr):
    Len = len(In)
    if (Len>512):
        A = compressbin_round(In[0:Len/2],Pr)
        B = compressbin_round(In[Len/2:],Pr)
        C = A+B
        C.sort()
        XX=  compressbin(C,Pr)
        return XX
    else:
        return compressbin(In,Pr)
        

def compressbin(In,Pr):
    flag=1
    while (flag):
        flag=0
        for i in range(0,len(In)-1):
            for j in range(i+1,len(In)):
                if (i<(len(In)-1))and(j<(len(In))):
                    x1 = In[i]
                    x2 = In[j]
                    x3 = bincompatible(x1,x2)
                    if (Pr):
                        print(x3,'===',x1,x2,i,j,len(In))
                    if (x3!=0):
                        In[i]=x3
                        In.pop(j)
                        flag = 1
    return In



def bincompatible(x1,x2):
    count=0
    res = ''
    for  i in range(0,OpcodeWidth):
        if (x2[i]==x1[i]):
            res = res + x1[i]
        else:
            if (count==1):
                return 0
            res = res + 'x'
            count=1
    return res


def check_contentions():
    global txtline
    Names = list(instructions.keys())
    for Ind,Inst1 in enumerate(Names):
        Coding1 = instructions[Inst1].coding
        Cond1 = instructions[Inst1].cond
        for Inst2 in Names[Ind+1:]:
            if (Inst2!=Inst1):
                Coding2 = instructions[Inst2].coding
                Cond2 = instructions[Inst2].cond
                if coding_collide(Coding1,Coding2)and(Cond1=='')and(Cond2==''):
                    txtline='%s<>%s'%(Inst1,Inst2)
                    catch_error('coding_collide',txtline)
    print('no contentions found')
def coding_collide(Coding1,Coding2):
    for X in range(0,OpcodeWidth):
        C1 = Coding1[X]
        C2 = Coding2[X]
        if (C1 != C2) and(C1 in ['0','1'])and(C2 in ['0','1']):
            return 0
    return 1


def get_fields(List,Field):
    Len = len(Field)+1
    res=[]  
    for X in List:
        if (len(X)>Len)and(X[:Len-1]==Field):
            res = res + [ X[Len:]]
    return res        



def get_field(List,Field,Default):
    Len = len(Field)+1
    for X in List:
        if (len(X)>Len)and(X[:Len-1]==Field):
            return X[Len:]
    if (Default=='error'):
        catch_error('bad field search field="%s" on "%s"  bailing out'%(Field,' '.join(List)),'nnn')
    return Default



def deal_opcode_width(List):
    global OpcodeWidth,Dnops,DmanualIfields,DnfSpecials,DmanualOpcodes
    Inst = get_field(List,'opcode_width','bubu')
    if (Inst!='bubu'):
        OpcodeWidth = int(Inst)
        print('set opcode width ',OpcodeWidth)
        return 1

    Inst = get_field(List,'properties','bubu')
    if (Inst!='bubu'):
        Regs = get_fields(List,'regs')
        for Item in Regs:
            Dnops[Item]=Inst
        return 1
    Inst = get_field(List,'manual_ifield','bubu')
    if (Inst!='bubu'):
        Regs = get_fields(List,'regs')
        for Item in Regs:
            DmanualIfields[Item]=Inst
        return 1

    Inst = get_field(List,'manual_opcode','bubu')
    if (Inst!='bubu'):
        Regs = get_fields(List,'regs')
        for Item in Regs:
            DmanualOpcodes[Item]=Inst
        return 1

    Inst = get_field(List,'dnf_special','bubu')
    if (Inst!='bubu'):
        Regs = get_fields(List,'regs')
        for Item in Regs:
            DnfSpecials[Item]=Inst
        return 1


    return 0




def deal_one_inst(List):
    global txtline,instructions
#    if len(List)<2: return
    txtline = ' '.join(List)+' ;'
    x = deal_opcode_width(List)
    if (x): 
        return  
    Inst = get_field(List,'instruction','error')
    Cond = get_field(List,'cond','')
    coding = get_field(List,'coding','error')
    pattern = get_field(List,'pattern','')
    translate = get_field(List,'translate','')
    color = get_field(List,'color','none')
    Coding = parse_coding(coding)
    print(Inst,len(Coding),Coding)
    inst = Instruction(Inst)
    inst.coding=Coding
    inst.color=color
    inst.pattern=pattern
    inst.translate=translate
    inst.oneliner = get_field(List,'oneliner','')
    inst.flags = get_fields(List,'flag')
    inst.cond = Cond
    instructions[Inst] = inst
    if (len(inst.coding)!=OpcodeWidth):
        catch_error('instruction_coding_length %s %s'%(len(inst.coding),inst.coding),'')

    
def parse_coding(Text):
    res=[]
    wrds = Text.split(',')
    for X in wrds:
        Y = parse_item(X)
        res=res+Y
    return res
def parse_item(Item):  
    if (Item[0] in ['1','0']):
        LL = list(Item)
        return LL

    if (Item[0]=='B'):
        Wid = int(Item[1:])
        return ['F']*Wid
    if ('[' in Item):
        X = Item.index('[')
        if (Item[-1]!=']'):
            catch_error('parse_item "]" ',Item)
        Bus = Item[:X]
        Inds = Item[X+1:-1]
        wrds = Inds.split(':')
        if (len(wrds)==2):
            St = int(wrds[0])
            En = int(wrds[1])
            if (St<=En):
                catch_error('parse_item St<=En',Item)
            I = St
            res=[]
            while(I>=En):
                II = '%s[%d]'%(Bus,I)
                res = res + [II]
                I=I-1
            return res
        elif (len(wrds)==1):
            return ['%s[%d]'%(Bus,int(wrds[0]))]
        else:
            catch_error('parse_item',Item)
    return [Item]

def read_inst_file(File):
    longline=''
    ok=1
    while ok:
        line = File.readline()
        ww = line.split()
        if (len(line)==0):
            ok=0
        elif len(ww)==0:
            pass
        elif ww[0][0] in '/#':
            pass
        else:
            longline=longline+' '+line
    longline = longline.replace(';',' ; ')
    wrds = longline.split()
    wrds = gatherQuotes(wrds)
    LLL = []
    while (len(wrds)>0):
        X = wrds.index(';')
        OneDef = wrds[0:X]
        wrds = wrds[X+1:]
        LLL = LLL + [OneDef]
    return LLL

def catch_error(Text,What):
    print('catch error',Text,What,'  >>>',txtline)
#    sys.exit()
    
def hex2bin(In):
    res = ''
    for X in In:
        HH = hexdig2bin(X)
        res = res + HH
    return res

hexdigs={}
hexdigs['0']='0000'
hexdigs['1']='0001'
hexdigs['2']='0010'
hexdigs['3']='0011'
hexdigs['4']='0100'
hexdigs['5']='0101'
hexdigs['6']='0110'
hexdigs['7']='0111'
hexdigs['8']='1000'
hexdigs['9']='1001'
hexdigs['a']='1010'
hexdigs['b']='1011'
hexdigs['c']='1100'
hexdigs['d']='1101'
hexdigs['e']='1110'
hexdigs['f']='1111'
hexdigs['A']='1010'
hexdigs['B']='1011'
hexdigs['C']='1100'
hexdigs['D']='1101'
hexdigs['E']='1110'
hexdigs['F']='1111'

def hexdig2bin(Dig):
    if (Dig in hexdigs):
        return hexdigs[Dig]
    else:
        catch_error('hexdig2bin',Dig)
    
def bin2hex(Bin):
    res=''
    while (len(Bin)>0):
        A = Bin[0:4]
        Bin=Bin[4:]
        ok=0
        for K in hexdigs:
            if (hexdigs[K]==A)and(ok==0)and(K not in 'ABCDEF'):
                ok=1
                res=res+K
    return res


def bin2hex(Bin):
    res = ''
    while ((len(Bin)%4)!=0):
        Bin='0'+Bin
    while 1:
        X = Bin[-4:]
        Bin=Bin[:-4]
        S = '%x'%(int(X,2))
        res =S+res
        if (len(Bin)==0):
            return res

def gatherQuotes(wrds):
    state = 'idle'
    res = []
    Wrd = ''
    for wrd in wrds:
#        print("XXXX",wrd,state)
        if state=='idle':
            if ('"' in wrd)and(wrd[-1] != '"'):
                state = 'work'
                Wrd = wrd 
            else:
                res.append(wrd)
        elif state=='work':
            Wrd += ' '+wrd
            if (wrd[-1] == '"'):
                res.append(Wrd)
                Wrd = ''
                state = 'idle'
    if len(Wrd)>0:  
        res.append(Wrd)
    return res 




def bin2int(Bin):
    res=0   
    for X in Bin: 
        if (X=='1'):
            res=2*res+1
        else:   
            res=res*2
    return res

main()




