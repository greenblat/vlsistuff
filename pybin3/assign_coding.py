#! /usr/bin/env python3
'''
    project instructions creator.  assigns coding to instructions.
'''


import os,string,sys,types,random
instructions={}
inst_id=1
txtline='no line'
OpcodeWidth=25
Props=[]
def get_inst_id():
    global inst_id
    x = inst_id
    inst_id=inst_id+1
    return x

class Instruction:
    def __init__(self,Name):
        self.name=Name
        self.id=get_inst_id()

def main():
    if (len(sys.argv)>1):
        Fname = sys.argv[1]
    else:
        Fname = 'instructionsB'
    File = open(Fname,'r')
    LLL = read_inst_file(File)
    for Item in LLL:
        deal_one_inst(Item)
    tablex = assign_coding()
    dump_new_coding(tablex)
    check_contentions(tablex,'final')

def check_contentions(tablex,pref):
    was=0
    for i in range(1,len(tablex)):
        atxt = tablex[i]
        for j in range(i+1,len(tablex)):
            btxt = tablex[j]
            if collides(atxt,btxt):
                was=was+1
    if (was==0):
        print('no collisions for ',pref)
    else:
        print(was,' collisions for ',pref)
        
def collides(atxt,btxt):
    if len(atxt)!=len(btxt):
        catch_error('different txt for collides |%s|%s|'%(atxt,btxt),btxt)
    for i in range(0,len(atxt)):
        if (atxt[i]=='0')and(btxt[i]=='1'):
            return 0
        if (atxt[i]=='1')and(btxt[i]=='0'):
            return 0
    return 1

def get_id(Id):
    for Inst in instructions:
        if (instructions[Inst].id==Id):
            return instructions[Inst].name
    return 'xxxxx'

def dump_new_coding(tablex):
    File = open('instructions.assigned','w')
    File.write('opcode_width=%d ;\n'%(OpcodeWidth))
    for L in Props:
        File.write('%s;\n'%(' '.join(L)))
    for Id in range(1,len(tablex)):
        for Inst in instructions:
            if (instructions[Inst].id==Id):
                CodingB = instructions[Inst].codingB
#                Id = instructions[Inst].id
                newcoding=tablex[Id]
                ind = 0
                for Item in CodingB:
                    if (Item=='F'):
                        if (newcoding[ind]=='1'):
                            CodingB[ind]='0'
                        elif (newcoding[ind]=='0'):
                            CodingB[ind]='1'
                        else:
                            CodingB[ind]=newcoding[ind]
                    ind=ind+1
                File.write('instruction=%s coding=%s '%(Inst,','.join(CodingB)))
                if (instructions[Inst].oneliner!=''):
                    File.write('oneliner=%s '%(instructions[Inst].oneliner))
                if (instructions[Inst].pattern!=''):
                    File.write('pattern=%s '%(instructions[Inst].pattern))
                if (instructions[Inst].translate!=''):
                    File.write('translate=%s '%(instructions[Inst].translate))
                for Flag in instructions[Inst].flags:
                    File.write('flag=%s '%(Flag))
                for Detail in instructions[Inst].details:
                    File.write('details=%s '%(Detail))
                File.write(' id=%d  color=%s;\n'%(Id,instructions[Inst].color))
    File.close()



def build_initial_table():
    tablex = []
    for Inst in instructions:
        CodingB = instructions[Inst].codingB
        Id = instructions[Inst].id
        res = ''
        for X in CodingB:
            if (X=='F'):
                res=res+'0'
            elif (X == '0'):
                res=res+'L'
            elif (X == '1'):
                res=res+'H'
            else:
                res=res+'x'
        while (len(tablex)<=Id):
            tablex=tablex+['']
        print('build ',Inst,Id,len(res),res)
        tablex[Id]=res
    return tablex

trytbl = [
    '',
    '0000x',
    '00xxx',
    '000xx',
    '000xx',
    '00xxx',
    '0000x'
]

trytbl_ = [
    '',
    '00xxx',
    '00xxx',
    '000xx',
    '000xx',
    '0000x',
    '0000x'
]


def assign_coding():
    tablex = build_initial_table()
    tablex2=tree_solution(tablex)
    check_contentions(tablex2,'tree algor')
    sumx= print_tablex(tablex2,' tree ')
    print('useds=0x%8x 0d%d'%(sumx,sumx))
    return tablex2 

def usedsin(txt):
    xses = 0
    for x in txt:
        if (x=='x'):
            xses=xses+1
    S = (1<<xses)
    return S

def split_score(GrA,GrB):
    score=0
    for A in GrA:
        for B in GrB:
            if not are_split(A,B):
                score=score+1
    return score        

def optimize_split(Bit,In0,In1):
    if ((len(In0)+len(In1))==2):
        return (In0,In1)
    start_score = split_score(In0,In1)
    sofar_score = split_score(In0,In1)
    better=1
    for i in range(0,10):
        better=0
        for A in In0:
            In0.remove(A)
            scr = split_score(In0,In1+[A])
            if (scr>sofar_score):
                In1=In1+[A]
                sofar_score=scr
                better=1
            else:
                In0=In0+[A]
        
        for A in In1:
            In1.remove(A)
            scr = split_score(In1,In0+[A])
            if (scr>sofar_score):
                In0=In0+[A]
                sofar_score=scr
                better=1
            else:
                In1=In1+[A]
        if (not better):
            print('bail out round=',i)
            return (In0,In1)

    if (start_score<sofar_score): 
        print(Bit,start_score,sofar_score)
    return (In0,In1)


class bitClass:
    def __init__(self,Bit):
        self.Bit=Bit
        self.opcodes=[]
        self.split0=[]
        self.split1=[]
    def add(self,Id):
        self.opcodes=self.opcodes+[str(Id)]
        self.opcodes.sort()
    def force_split(self,A,B):
        if (A not in self.opcodes)or (B not in self.opcodes):
            return 0
        if (A in self.split0)and(B in self.split0):
            self.opcodes.remove(A)
            self.opcodes = [A]+self.opcodes
            return 1
        if (A in self.split1)and(B in self.split1):
            self.opcodes.remove(B)
            self.opcodes = [B]+self.opcodes
            return 1
        return 0
    def splitme(self):
        self.split0=[]
        self.split1=[]
        Spl0=[self.opcodes[0]]
        Spl1=[]
        for A in self.opcodes[1:]:
            sc0 = split_score(Spl0+[A],Spl1)
            sc1 = split_score(Spl1+[A],Spl0)
            if (sc1>sc0):
                Spl1=Spl1+[A]
            else:
                Spl0=Spl0+[A]


        self.split0=Spl0
        self.split1=Spl1
        return (Spl0,Spl1)
                


def are_split2(A,B):
    for b in bits:
        if (A in b.split0)and(B in b.split1):
            return 1
        if (A in b.split1)and(B in b.split0):
            return 1
        print('failed',A,B,b.Bit,b.split0,b.split1)
    return 0



def are_split(A,B):
    for b in bits:
        if (A in b.split0)and(B in b.split1):
            return 1
        if (A in b.split1)and(B in b.split0):
            return 1
    return 0



bits = []

def add_opcode(Id,Item):
    global bits
    for x in range(0,len(Item)):
        pos = len(Item)-1-x
        if (Item[pos]=='0'):
            bits[x].add(Id)

def find_shortest_bit(bits):
    res = []
    for bit in bits:
        Len = len(bit.opcodes)
        Bit = bit.Bit
        if (Len>1):
            res = res + [(Len,Bit)]
    res.sort()
    resu=[]
    for (L,Bit) in res:
        resu = resu + [Bit]
    return resu


def find_shortest_bit_(bits):
    Shrts = 1000
    Good= -1
    for bit in bits:
        Len = len(bit.opcodes)
        Bit = bit.Bit
        if (Len>1)and(Len<Shrts)and(len(bit.split0)==0):
            Good=Bit
            Shrts=Len
        elif (Len>1)and(Len==Shrts)and(len(bit.split0)==0)and(Bit<Good):
            Good=Bit
            Shrts=Len
    return Good

def split_solution(tablex):
    global bits
    for i in range(0,len(tablex[1])):
        bits=bits+[bitClass(i)]
    for Id in range(1,len(tablex)):
        add_opcode(Id,tablex[Id])
    Order = find_shortest_bit(bits)
    bads=[0]
    guard=20
    Ids = range(1,len(tablex))
    while (len(bads)>0)and(guard>0):
        for Bit in Order: 
            bits[Bit].splitme()
        for Bit in Order: 
            bits[Bit].splitme()
        bads = []
        for i in range(1,len(tablex)):
            for j in range(i+1,len(tablex)):
                if (are_split(str(i),str(j))==0):
                    print('not split ',i,j)
                    bads=bads+[(str(i),str(j))]
                    
        print('round ',guard,len(bads))
        for (i,j) in bads: 
            for Bit in Order: 
                bits[Bit].force_split(i,j)


        guard=guard-1

        


    for b in bits:
        print(b.Bit,b.split0,b.split1)

    newtablex=[]
    for X in tablex:
        newtablex = newtablex + [X]

    for Id in range(1,len(tablex)):
        was = tablex[Id]
        for bit in bits:
            pos = bit.Bit
            strpos = len(was)-pos-1
            if (was[strpos]=='0')and(str(Id) in bit.split1):
                    was = was[:strpos]+'1'+was[strpos+1:]
        newtablex[Id]=was
    return newtablex
    
def try_and_fix_it(A,B):
    print('try and fix',A,B)
    for b in bits:
        if (A in b.split0)and(B in b.split0):
            print(A,B,b.Bit)   

    return
        



def bads_still(Split):
    res = []
    for i in range(0,len(Split)):
        A=Split[i]
        for j in range(i+1,len(Split)):
            B=Split[j]
            if not are_split(A,B):
                res=res+[(A,B)]
    res.sort()
    return res

def bads_total():
    bads = []
    for b in bits:
        bads = bads_still(b.split0)+bads_still(b.split1)
    bads.sort()
    return bads


def extract_bus(Txt):
    x = Txt.index('[')
    Bus = Txt[0:x]
    Ins = Txt[x+1:-1]
    return (Bus,int(Ins))
    







def int2bin(Int,Wid):
    res = 32*'0'
    for i in range(0,32):
        x = Int & (1<<i)
        if (x):
            res[31-i] = '1'
    res = res[32-Wid:]
    return ''.join(res)


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
    global OpcodeWidth,Props
    Inst = get_field(List,'opcode_width','bubu')
    if (Inst!='bubu'):
        OpcodeWidth = int(Inst)
        print('set opcode width ',OpcodeWidth)
        return 1
    Inst = get_field(List,'properties','bubu')
    if (Inst!='bubu'):
        Props = Props + [List]
        return 1
    Inst = get_field(List,'manual_ifield','bubu')
    if (Inst!='bubu'):
        Props = Props + [List]
        return 1
    Inst = get_field(List,'manual_opcode','bubu')
    if (Inst!='bubu'):
        Props = Props + [List]
        return 1
    Inst = get_field(List,'dnf_special','bubu')
    if (Inst!='bubu'):
        Props = Props + [List]
        return 1
    return 0

def deal_one_inst(List):
    global txtline,instructions
    txtline = ' '.join(List)+' ;'
    x = deal_opcode_width(List)
    if (x):
        return
    Inst = get_field(List,'instruction','error')
    coding = get_field(List,'coding','error')
    color = get_field(List,'color','none')
    Coding = parse_coding(coding)
    inst = Instruction(Inst)
    inst.codingB=Coding
    inst.oneliner = get_field(List,'oneliner','')
    inst.pattern = get_field(List,'pattern','')
    inst.translate = get_field(List,'translate','')
    inst.flags = get_fields(List,'flag')
    inst.details = get_fields(List,'details')
    inst.color=color
    if (Inst in instructions):
        catch_error('instruction defined twice ',Inst)
    instructions[Inst] = inst
    if (len(inst.codingB)!=OpcodeWidth):
        catch_error('instruction_coding_length',len(inst.codingB))
    
def parse_coding(Text):
    res=[]
    wrds = Text.split(',')
    for X in wrds:
        Y = parse_item(X)
        res=res+Y
    if ('FX' in res):
        Len = len(res)
        More = OpcodeWidth-Len+1
        Ind = res.index('FX')
        res=res[:Ind]+(More*['F'])+res[Ind+1:]
        if ('FX' in res):
            catch_error('too many BX in words',' '.join(res))
    print(Text,res)
    return res

def parse_item(Item):  
    if (Item=='1')or(Item=='0'):
        return [Item]
    if (Item=='BX'):
        return ['FX']
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
        else:
            catch_error('parse_item',Item)
    return [Item]

def read_inst_file(File):
    longline=''
    ok=1
    while ok:
        line = File.readline()
        if (len(line)==0):
            ok=0
        else:
            if (line[0]!='/')and(line[0]!='#'):
                longline=longline+' '+line
    longline = longline.replace(';',' ; ')
    wrds = longline.split()
    LLL = []
    while (len(wrds)>0):
        if (';' not in wrds):
            catch_error('no ; in line','xxx')
        X = wrds.index(';')
        OneDef = wrds[0:X]
        wrds = wrds[X+1:]
        LLL = LLL + [OneDef]
    return LLL

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
    

def print_tablex(tablex,pref):
    i=1
    sumx=0
    for tblx in tablex[1:]:
        sumx = sumx + usedsin(tblx)
        print('%s %2d %s    %s    %d    %d '%(pref,i,tblx,get_id(i),sumx,usedsin(tblx)))
        i=i+1
    return sumx

def tree_solution(tablex):
    Tree = range(1,len(tablex))
    mask0 =  mutual_mask(Tree,tablex)
    print_tablex(tablex,' tree ')
    print('mask0 ',mask0)
    Trees = split_tree(Tree,mask0,tablex,32)
    print_tree(Trees,' ')
    newtables = tree_assignments(Trees,tablex)
    return newtables

def mutual_trees_mask(Trees,mask0,tablex):
    if (type(Trees)is int):
       mask0=maskify1(tablex[Trees],mask0)
       return mask0
    for X in Trees:
        if (type(X)is int):
            mask0=maskify1(tablex[X],mask0)
        else:
            mask0 = mutual_trees_mask(X,mask0,tablex)
    return mask0


def tree_assignments(Trees,tablex):
    global newtablex
    newtablex = ['']*len(tablex)
    mask0 = '0'*(len(tablex[1]))
    start = '0'*(len(tablex[1]))
    last = deep_tree_assignment(Trees,start,tablex)
    print('last ',last)
    return newtablex

def deep_tree_assignment(Trees,coding,tablex):
    global newtablex
    if (Trees==[]):
        return coding
    Item = Trees[0]
    if (type(Item)is int):
        if (Item in specials):
            similar=[]
            different=[]
            for Key in Trees:
                if (Key in specials)and(specials[Key]==specials[Item]):
                    similar=similar+[Key]
                else:
                    different=different+[Key]
            previous=''
            for Key in similar:
                codingHere1=''
                for i in range(0,len(coding)):
                    if (tablex[Item][i]=='x'):
                        codingHere1 = codingHere1+'x'
                    else:
                        codingHere1 = codingHere1+coding[i]
                nextCoding = incr_coding(codingHere1)
                newtablex[Key]=codingHere1
                previous=coding
                coding=nextCoding
            used = mask_used[Item]
            codingHere=''
            for i in range(0,len(coding)):
                if (used[i]=='x'):
                    codingHere = codingHere+'x'
                else:
                    codingHere = codingHere+coding[i]
                    
            if collides(codingHere,codingHere1):
                nextCoding = incr_coding(codingHere)
            else:
                nextCoding = coding
            print('after specials goto next=%s here=%s prev=%s coding=%s'%(nextCoding,codingHere,previous,coding))
            return deep_tree_assignment(different,nextCoding,tablex)
        else:
            codingHere=''
            codingHere1=''
            used = mask_used[Item]
            for i in range(0,len(coding)):
                if (tablex[Item][i]=='x')or(used[i]=='x'):
                    codingHere = codingHere+'x'
                else:
                    codingHere = codingHere+coding[i]
                if (tablex[Item][i]=='x'):
                    codingHere1 = codingHere1+'x'
                else:
                    codingHere1 = codingHere1+coding[i]
            nextCoding = incr_coding(codingHere)
            newtablex[Item]=codingHere1
            return deep_tree_assignment(Trees[1:],nextCoding,tablex)
    else:
        nextCoding =  deep_tree_assignment(Item,coding,tablex) 
        return deep_tree_assignment(Trees[1:],nextCoding,tablex)
    




def  incr_coding(codingHere):
    txt1 = codingHere.replace('',' ')
    lets = txt1.split(' ')
    lets.reverse()
    for i in range(0,len(lets)):
        if (lets[i]=='0'):
            lets[i]='1'
            lets.reverse()
            txt1 = ''.join(lets)
            txt2 = txt1.replace('x','0')
            return txt2
        elif (lets[i]=='1'):
            lets[i]='0'
    print('bad incr ',codingHere)
    return codingHere
    



def print_tree(Trees,Pref):
    for X in Trees:
        if (type(X) is list):
            print('%s['%(Pref))
            print_tree(X,Pref+'   ')
            print('%s]'%(Pref))
        else:
            print('%s%s'%(Pref,str(X)))
            


    

def mutual_mask(List,tablex):
    mask0 = '0'*(len(tablex[1]))
    for tblx in List:
        mask1 = maskify1(mask0,tablex[tblx])
        mask0=mask1
    return mask0        

mask_used={}
def split_tree(List,mask0,tablex,Guard):
    global mask_used
    if (Guard<=0):
        catch_error('split tree hit guard depth','xxx')
    ones=[]
    more=[]
    for Id in List:
        mask2 = maskify1(inverse_mask(mask0),tablex[Id])
        if ('0' in mask2):
            more=more+[Id]
        else:
            ones=ones+[Id]
            mask_used[Id]=mask0
    if (more==[]):
        return [ones]
    if (ones==[]):
        split_second_tree(more,tablex)
        for idx in more:
            mask_used[idx]=mask0
        return [more]
    Mut = mutual_mask(more,tablex)
    Deep = split_tree(more,Mut,tablex,Guard-1)
    return ones+[Deep] 

specials={}
def split_second_tree(List,tablex):
    global specials 
    mask0 =  mutual_mask(List,tablex)
    res=[]
    for X in List:
        specials[X]=maskify1(inverse_mask(mask0),tablex[X])


def inverse_mask(atxt):
    res=''
    for x in atxt:
        if (x=='x'):
            res = res + '0'
        else:
            res = res + 'x'
    return res



def or_mask(txta,txtb):
    res = ''
    for i in range(0,len(txta)):
        if (txta[i]=='0')or(txtb[i]=='0'):
            res=res+'0'
        else:
            res=res+'x'
    return res

def maskify1(txta,txtb):
    res = ''
    if len(txta)!=len(txtb):
        catch_error('bad error, lens dont match',len(txta))
    for i in range(0,len(txta)):
        if (txta[i]=='x')or(txtb[i]=='x'):
            res=res+'x'
        else:
            res=res+'0'
    return res
main()

