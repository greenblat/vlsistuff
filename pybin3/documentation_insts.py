#! /usr/bin/env python3


import os,string,sys,types
instructions={}
inst_id=1
OpcodeWidth=25
Chip = 'chip'
docfname = 'documentation'
def get_inst_id():
    global inst_id
    x = inst_id
    inst_id=inst_id+1
    return x

class Instruction:
    def __init__(self,Name):
        self.name=Name
        self.id=get_inst_id()
        self.fields=[]
    def has_field(self,Field):
        if '[' in Field:
            Field = Field[:Field.index('[')]
        return Field in self.fields

def main():
    global Chip,docInsts
    print('invocation: documentation_insts.py ChipName InstructionsFile docfname')
    if len(sys.argv)>1:
        Chip = sys.argv[1]
    if len(sys.argv)>2:
        InstFileName = sys.argv[2]
    else:
        InstFileName = 'instructions.assigned'
    if len(sys.argv)>3:
        docfname = sys.argv[3]

    print('set: documentation_insts.py %s %s'%(Chip,InstFileName))
    File = open(InstFileName,'r')
    LLL = read_inst_file(File)
    for Item in LLL:
        deal_one_inst(Item)

    File2 = open(docfname)
    doclines1 = File2.readlines()
    doclines=[]
    docInsts=[]
    for line in doclines1:
        wrds = line.split()
        if (len(wrds)>0)and(wrds[0][0] not in '#/'):
            doclines = doclines+[wrds]
            if wrds[0][0]=='*':
                docInsts.append(wrds[0][1:])
    File2.close()
    print('doclines ',len(doclines))
    produce_documentation(doclines)
    for Inst in docInsts:
        if Inst not in instructions:
            print('doc %s not in instruction set'%Inst)
    










        


def ok_name(Name):
    if (len(Name)>len('unused'))and(Name[0:len('unused')]=='unused'):
        return 0
    return 1



    


header_string = '\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">\n\
<html>\n\
  <head>\n\
    <title>chip instruction set </title>\n\
  </head>\n\
\n\
  <body>\n\
    <left>\n\
\n\
      <h1>%s instruction set</h1>\n\
\n\
'

stam = '\n\
      <table border>\n\
      <tr>\n\
        <td align="center"><b>opc2de</b></td>\n\
        <td colspan=OCPODEWIDTH align="center"><b>data bits</b></td>\n\
      </tr>\n\
'

table_header_string = '\
      <table border align="center" width="600" >\n\
'
xxx = '\
      <tr>\n\
        <td colspan=OPCODEWIDTH align="center"></td>\n\
      </tr>\n\
'


tail_string = ' </center> </body> </html>\n\n'
def switch_colors():
    global color,othercolor
    x = color
    color=othercolor
    othercolor=x




def produce_documentation(doclines):
    global color,othercolor
    ofile = open('%s_doc.html'%(Chip),'w')
    ofile.write(header_string%(Chip))
    mdfile = open('%s_doc.md'%(Chip),'w')
    mdfile.write('# MLCPU instruction set\n')
    for wrds in doclines:
        if (wrds[0]=='header'):
             ofile.write('%s <br>\n'%(' '.join(wrds[1:])))
    ofile.write('<br> <br>\n')
    color = '#ffa0ff'
    othercolor = '#ffffa0'
    instruction = 'bits'
    color = '#80ff80'
    othercolor = '#ffffa0'

    explanation = ''
    lll=[]
    for Inst in instructions:
        lll = lll + [(instructions[Inst].id,Inst)]
    lll.sort()
    Insts = []
    for (id,Inst) in lll:
        if ok_name(Inst):
            Insts = [Inst]+Insts
    Insts.sort()
    for Inst in Insts:
        for (id,Inst2) in lll:
            if (Inst2==Inst):
                produce_page_for_instruction(ofile,Inst,doclines)
                produce_md_for_instruction(mdfile,Inst,doclines)




    ofile.write(tail_string)
    ofile.close()
    mdfile.close()

def do_bits(ofile):
    rng = list(range(0,OpcodeWidth))
    rng.reverse()
    origarr=[]
    for x in rng:
        origarr = origarr + [str(x)]
    ofile.write('<tr bgcolor='+color+'> \n')
    run_on_coding(origarr,ofile)


def produce_page_for_instruction(ofile,Inst,doclines):
    ofile.write('<table border> <tr> <td>\n')
    ofile.write('<h2  align="left">%s\n'%(Inst))
    ofile.write('<a name=%s></h2>\n'%(Inst))
    expl = instructions[Inst].oneliner.replace('.',' ')
    expl = expl.replace('<<',' shiftleft ')
    expl = expl.replace('>>',' shiftright ')
    ofile.write('<13 align="left">"%s"</h3>\n'%(expl))
    ofile.write(table_header_string.replace('OPCODEWIDTH',str(OpcodeWidth)))
    do_bits(ofile)
    ofile.write('<tr bgcolor='+color+'>\n')
    run_on_coding(instructions[Inst].coding,ofile)
    ofile.write('</tr>\n')
    ofile.write('</table>\n')
    Flgs=''
    for Txt in instructions[Inst].flags:
        if (len(Txt)>8)and(Txt[:8]=='updates_'):
            Flgs = Flgs + Txt[8:]
    if (Flgs==''):
        ofile.write('Flags affected: None<br>\n')
    else:
        ofile.write('Flags affected: <b> %s </b> <br>\n'%(Flgs))
    if 'cnd_active' in instructions[Inst].flags:
        ofile.write('<b> This instruction can be conditionally executed</b> <br>\n')

#    for Txt in instructions[Inst].details:
#        ofile.write('%s<br>\n'%(Txt))
    switch_colors()
    use_doclines(Inst,ofile,doclines)
    ofile.write('<hr>\n')
    ofile.write('</td> </tr> </tabler>\n')


def produce_md_for_instruction(ofile,Inst,doclines):
    ofile.write('## %s\n' % Inst)
    expl = instructions[Inst].oneliner.replace('.',' ')
    expl = expl.replace('<<',' shiftleft ')
    expl = expl.replace('>>',' shiftright ')
    expl = expl.replace('<h3>','')
    expl = expl.replace('</h3>','')
    ofile.write('    **%s**\n' % expl)
    run_on_md_coding(instructions[Inst].coding,ofile)
    Flgs=''
    for Txt in instructions[Inst].flags:
        if (len(Txt)>8)and(Txt[:8]=='updates_'):
            Flgs = Flgs + Txt[8:]
    if (Flgs==''):
        ofile.write('Flags affected: None\n')
    else:
        ofile.write('Flags affected: %s\n'%(Flgs))

    use_doclines(Inst,ofile,doclines)
    ofile.write('\n')




def get_inst_explanation(Inst):
    return '???'


def run_on_coding(wrds,ofile):
    wrds = gather_busses(wrds)

    for word in wrds:
        if (word=='1'):
            ofile.write('<td align="center">'+str(word)+'</td>\n')
        elif (word=='0'):
            ofile.write('<td align="center">'+str(word)+'</td>\n')
        elif (type(word)is str):
             ofile.write('<td align="center" >'+str(word)+'</td>\n')
        elif (type(word) is tuple):
            (Bus,ind1,ind2)=word
            text = '%s[%d:%d]'%(Bus,ind1,ind2)
            many = ind1-ind2+1
            ofile.write('<td  align="center" colspan='+str(many)+'>'+text+'</td>\n')
        else:
            print('error! ilia, coding field bad ',word, wrds)

def run_on_md_coding(wrds,ofile):
#    wrds = gather_busses(wrds)

    
    Jstr = '|'.join(wrds)
    Len = len(wrds)
    J0 =  ''
    for I in wrds:
        J0 += ' | '
    J1 = J0.replace(' ','x')
    J0 = J0.replace('  ',' ')
    ofile.write('|%s|\n' % J1)
    ofile.write('|%s|\n' % J0)
    ofile.write('|%s|\n' % Jstr)

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
        catch_error('bad field search %s on %s, bailing out'%(Field,' '.join(List)),'nnn')
    return Default



def deal_opcode_width(List):
    global OpcodeWidth
    Inst = get_field(List,'opcode_width','bubu')
    if (Inst!='bubu'):
        OpcodeWidth = int(Inst)
        print('set opcode width ',OpcodeWidth)
        return 1

    Inst = get_field(List,'properties','bubu')
    if (Inst!='bubu'):
        Regs = get_fields(List,'regs')
        return 1
    Inst = get_field(List,'manual_ifield','bubu')
    if (Inst!='bubu'):
        Regs = get_fields(List,'regs')
        return 1
    Inst = get_field(List,'manual_opcode','bubu')
    if (Inst!='bubu'):
        Regs = get_fields(List,'regs')
        return 1
    Inst = get_field(List,'dnf_special','bubu')
    if (Inst!='bubu'):
        Regs = get_fields(List,'regs')
        return 1


    return 0


def gather_fields(Coding):
    Fields=[]
    for X in Coding:
        if X[0] not in '01':
            if '[' in X:
                X = X[:X.index('[')]
            if X not in Fields:
                Fields.append(X)
    return Fields

def deal_one_inst(List):
    global txtline,instructions
    txtline = ' '.join(List)+' ;'
    x = deal_opcode_width(List)
    if (x): 
        return  

    Inst = get_field(List,'instruction','error')
    coding = get_field(List,'coding','error')
    Coding = parse_coding(coding)
    inst = Instruction(Inst)
    inst.coding=Coding
    inst.oneliner = get_field(List,'oneliner','')
    inst.flags = get_fields(List,'flag')
    inst.details = get_fields(List,'details')
    inst.fields = gather_fields(Coding)
    instructions[Inst] = inst
    if (len(inst.coding)!=OpcodeWidth):
        catch_error('instruction_coding_length',len(inst.coding))

    
def parse_coding(Text):
    res=[]
    wrds = Text.split(',')
    for X in wrds:
        Y = parse_item(X)
        res=res+Y
    return res
def parse_item(Item):  
    if (Item=='1')or(Item=='0'):
        return [Item]
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
    longline = File.read()
    longline = longline.replace(';',' ; ')
    wrds = longline.split()
    wrds = gather_string(wrds)
    LLL = []
    while (len(wrds)>0):
        if ';' in wrds:
            X = wrds.index(';')
            OneDef = wrds[0:X]
            wrds = wrds[X+1:]
            LLL = LLL + [OneDef]
        else:
            print('ERROR>>>',wrds)
            sys.exit()
    return LLL


def oldii(File):
    longline=''
    ok=1
    while ok:
        line = File.readline()
        if (len(line)==0):
            ok=0
        else:
            longline=longline+' '+line
    longline = longline.replace(';',' ; ')
    wrds = longline.split()
    wrds = gather_string(wrds)
    LLL = []
    while (len(wrds)>0):
        X = wrds.index(';')
        OneDef = wrds[0:X]
        wrds = wrds[X+1:]
        LLL = LLL + [OneDef]
    return LLL



def gather_string(wrds):
    res = []
    current = ''
    state='idle'
    for wrd in wrds:
        if state=='idle':
            if ('"' in wrd)and(wrd[-1]!='"'):
                current = wrd
                state='work'
            else:   
                res.append(wrd)
        elif state=='work':
            current = current + ' '+wrd 
            if wrd[-1]=='"':
                res.append(current)
                current=''
                state='idle'
    return res                



def build_skeleton(Inst):
    Obj = instructions[Inst]
    Str = '*%s\n'%Inst
    Str += 'short %s\n'%Obj.oneliner.replace('.',' ')
    for Field in Obj.fields:
        Str += 'field %s xxxx\n'%(Field)

    Str += ';\n'
    return Str

Fskel = False
missing_doclines=0
def use_doclines(Inst,ofile,doclines):
    global missing_doclines
    global Fskel
    if not Fskel:
        Fskel = open('skeleton.docs','w')
    lines = get_relevant_lines(Inst,doclines)
    if (len(lines)==0):
        missing_doclines=missing_doclines+1
        print(' (%d)instruction %s dosn"t have doclines'%(missing_doclines,Inst))
        Str = build_skeleton(Inst)
        Fskel.write(Str)
        return
    for wrds in lines:
        if (wrds[0]=='short'):
            ofile.write('<h3> %s </h3>\n'%(' '.join(wrds[1:])))

    x=0
    for wrds in lines:
        if (wrds[0]=='field'):
            x=x+1

    if (x>0):
        ofile.write('<table border align="left">\n<tr>\n<td colspan=2 align="left">fields</td>\n</tr>\n')
        x=0
        Used=instructions[Inst].fields[:]
        for wrds in lines:
            if (wrds[0]=='field'):
                Field = wrds[1]
                if instructions[Inst].has_field(Field):
                    ofile.write('<tr> <td> <b> %s </b> </td>'%(wrds[1]))
                    ofile.write('<td>  %s </td></tr>\n'%(' '.join(wrds[2:])))
                    if '[' in Field:
                        Field = Field[:Field.index('[')]
                    if Field in Used: Used.remove(Field)
                else:
                    ofile.write('<tr> <td> <b> %s </b> </td>'%(wrds[1]))
                    ofile.write('<td>  %s </td></tr>\n'%('NOT DEFINED!!!'))
                x=x+1
        for Field in Used:
            ofile.write('<tr> <td> <b> %s </b> </td>'%(Field))
            ofile.write('<td>  %s </td></tr>\n'%('no description given'))


        ofile.write('</table> \n')
        for i in range(2+2*x):
            ofile.write('<br>')
        ofile.write('\n')

    x=0
    for wrds in lines:
        if (wrds[0]=='|'):
            x=x+1
    if (x>0):
        ofile.write('<b>operation:</b><br>\n')
    for wrds in lines:
        if (wrds[0]=='|'):
            ofile.write('   %s <br>\n'%(' '.join(wrds[1:])))


def get_relevant_lines(Inst,doclines):
    Result = []
    ok=0
    for wrds in doclines:
        if (wrds[0]==';'):
            ok=0
        if (ok):
            Result = Result + [wrds]
        if (wrds[0]==('*'+Inst)):
            ok=1
    return Result


# utlities

def catch_error(Text,What):
    print('catch error',Text,What,'  >>>',txtline)
    sys.exit()
    
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


def bin2int(Bin):
    res=0   
    for X in Bin: 
        if (X=='1'):
            res=2*res+1
        else:   
            res=res*2
    return res

main()





