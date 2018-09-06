#! /usr/bin/python

import string,sys,os,types
import cProfile
import traceback
def main():
    global Style
    Fname = sys.argv[1]
    Style = 'old'
    for Opt in sys.argv[1:]:
        if '-n' in Opt:
            Style = 'new'
    run_lexer(Fname,'lex.out')

class DbClass:
    def __init__(self):
        self.state='idle'
        self.Token=''
        self.Queue=[]
        self.Types=string.split('positive string std_logic_vector std_logic integer line bit_vector boolean natural')


def run_lexer(Fname,Ofname):
    global Db
    Db=DbClass()
    try:
        File = open(Fname)
    except:
        print 'lexer failed to open %s'%Fname
        print traceback.print_stack()
        return
    Db.Ofile = open(Ofname,'w')
    checkTable()
    work(File)
    work_out_queue(True)
    Db.Ofile.close()

def checkTable():
    for X in Table:
        if len(X)!=6:
            print 'ERROR! ilia in table "%s"'%(str(X))

def work(File):
    LineNum=0
    while 1:
        line=File.readline()
        if len(line)==0:
            return
        LineNum+=1
        if len(line)>1:
            if ord(line[-2])==13:
                line=line[:-2]+chr(10)
            elif ord(line[-1])!=10:
                line = line+ chr(10)
#            print 'line',line,
            work_line(line,LineNum)

def work_line(line,LineNum):
    Len=len(line)
    for i in range(Len-1):
        Db.state,action,kind=stepit(i,line[i],line[i+1],Db.state)
        if (action=='skipline'):
            Db.state='idle'
            return
        if (action=='push'):
            Db.Token=Db.Token+line[i]
            push_token(Db.Token,kind,LineNum,i)
            Db.Token=''
        elif (action=='add'):
            Db.Token=Db.Token+line[i]
        elif (action!='none'):
            print Db.state,action,kind,'error line=%d pos=%d chr="%s" %s'%(LineNum,i,line[i],line[:-1])
            sys.exit()
def push_token(Token,kind,LineNum,LinePos):
#    print 'push_token    %s %s %s %s\n'%(Token,kind,LineNum,LinePos)
    if (kind=='token')and(string.lower(Token) in ReservedWords):
        kind=string.capitalize(Token)
        Token=string.capitalize(Token)
    elif (kind=='define')and(Token in ReservedWords):
        kind='backtick_'+Token[1:]
    elif (kind=='token')and('.' in Token):
        kind = 'dotted'

    if string.lower(Token) in Db.Types:
        kind = 'Types'
    if len(Db.Queue)>0:
        PrevT,PrevK,_,_ = Db.Queue[-1]
        if (PrevT=='Type'):
            Db.Types.append(string.lower(Token))

    Db.Queue.append((Token,kind,LineNum,LinePos))
    work_out_queue()

def work_out_queue(Flush=False):
    if (Flush):
        if Db.Queue==[]:
            return
        Tup = Db.Queue.pop(0)
        Tup = rework_tup(Tup)
        Db.Ofile.write('%s %s %s %s\n'%Tup)
        work_out_queue(Flush)
    if (len(Db.Queue)>=2)and(Db.Queue[0][1]=='number')and(Db.Queue[1][1] in ['uhex','ubin','udig']):
        Item = [Db.Queue[0][0]+Db.Queue[1][0],Db.Queue[1][1][1:],Db.Queue[0][2],Db.Queue[0][3]]
        Db.Queue[0]=tuple(Item)
        Db.Queue.pop(1)

    if (len(Db.Queue)>3):
        Tup = rework_tup(Db.Queue.pop(0))
        Db.Ofile.write('%s %s %s %s\n'%Tup)
        return
            

def rework_tup(Tup):
    if Tup[1]=='single':
        List = list(Tup)
        List[1]=List[0]
        return tuple(List)
        
    if Tup[1]=='double':
        List = list(Tup)
        if (len(List[0])==1):
            List[1]=List[0]
            return tuple(List)
        if Style=='old':
            List[1]=doublesName(List[0])
        else:
            List[1]=List[0]
        return tuple(List)
    return Tup

DoubleNames = {}
DoubleNames['&&'] = 'and_and'
DoubleNames['=='] = 'eq_eq'
DoubleNames['!='] = 'Neq'
DoubleNames['/='] = 'Neq'
DoubleNames['||'] = 'or_or'
DoubleNames['>='] = 'gr_eq'
DoubleNames['<='] = 'Assign'
DoubleNames['->'] = 'emit'
DoubleNames['!^'] = 'xnor'
DoubleNames['>>'] = 'shift_right'
DoubleNames['<<'] = 'shift_left'
DoubleNames['+:'] = 'plus_range'
DoubleNames['-:'] = 'minus_range'
DoubleNames['<>'] = 'sm_gr'
DoubleNames['=>'] = 'Arrow'
DoubleNames[':='] = 'Cassign'


def doublesName(Txt):
    if Txt in DoubleNames:
        return DoubleNames[Txt]
    else:
        print 'ilia! doubles names missing %s'%Txt
        return Txt


def stepit(Pos,Char,Char1,State):
    rule=0
    for (St,Ch0,Ch1,Next,Action,Kind) in Table:
        if (St==State):
#            print 'tryrule%d ch=%s ch1=%s in0=%d in1=%d st=%s ch0=%s ch1=%s next=%s act=%s kind=%s'%(rule,Char,Char1,(Char in Ch0),(Char1 in Ch1),State,Ch0,Ch1,Next,Action,Kind)
            rule +=1
            if (Ch0=='')or(Char in Ch0):
                if (Ch1=='')or(Char1 in Ch1):
                    return  Next,Action,Kind
    print 'lexer: no rule fits st=%s ch=%s ch1=%s'%(State,Char,Char1)
#    sys.exit()
    return 'idle','error',0
    
LowLetters = 'qwertyuiopasdfghjklzxcvbnm'
CapLetters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
Letters = LowLetters+CapLetters
Digits='0123456789'
Alphas = Letters+Digits+'_'
HexDig = Digits+'abcdef'+'ABCDEF'+'_'+'xX'
BinDig = '01_xzXZ?'
Singles = '?.,[]{}#@()~%^;:/+-*'
Doubles = '-=!<>&|'
Doubles2 = '=<>&|'
Spaces = '\t '
AnyChar = Letters+Digits+Spaces+'_'+Singles+Doubles+"',\\"

LegalDoublesStr = '** -> == != <= >= => =< && ||'
LegalDoubles = string.split(LegalDoublesStr)

#    ,('idle','(','*',               'pragma','add',0)
#    ,('pragma','*',' ',             'idle','push','pragma_start')
#    ,('idle','*',')',               'pragma2','add',0)
#    ,('pragma2',')','',             'idle','push','pragma_end')

Table = [
     ('idle',Spaces,'',             'idle','none',0)
    ,('idle','-','-',               'idle','skipline',0)

    ,('idle','xXoObB','"',     'hex','add',0)
    ,('hex','"',HexDig,         'hex2','add',0)
    ,('hex2',HexDig,HexDig,     'hex2','add',0)
    ,('hex2',HexDig,'"',        'hex3','add',0)
    ,('hex3','"','',            'idle','push','hexdig')

    ,('idle','`',Letters,           'define','add',0)
    ,('define',Alphas,Alphas,       'define','add',0)
    ,('define',Alphas,'',           'idle','push','define')
    ,('idle',Letters,Alphas+'.',    'token','add',0)
    ,('token',Alphas+'.',Alphas+'.',        'token','add',0)
    ,('token',Alphas,'',            'idle','push','token')
    ,('idle',Letters,'',             'idle','push','token')

    ,('idle',Digits,Digits,         'number','add',0)
    ,('idle',Digits,'.',            'floating0','add',0)
    ,('idle',Digits,'',             'idle','push','number')
    ,('idle',"'",Digits+'-Zz',               'Literal1','add',0)
    ,('Literal1',Digits+'-Zz','',            'Literal1','add',0)
    ,('Literal1',"'",'',            'idle','push','literal')
    ,('idle',"'",'',               'idle','push','tick')

    ,('number',Digits,Digits,       'number','add',0)
    ,('number',Digits,"#",          'basednumber','add',0)
    ,('number',Digits,'.',          'floating0','add',0)
    ,('number',Digits,'',           'idle','push','number')
    ,('floating0','.',Digits,     'floating','add',0)
    ,('floating',Digits,Digits,     'floating','add',0)
    ,('floating',Digits,'',         'idle','push','floating')

    ,('basednumber',"#",HexDig,      'based2','add',0)
    ,('based2',HexDig,HexDig,        'based2','add',0)
    ,('based2',HexDig,'#',           'based3','add',0)
    ,('based3','#','',               'idle','push','based')


    ,('dig2',Digits,Digits,         'dig2','add',0)
    ,('dig2',Digits,'',             'idle','push','dig')

    ,('hex2',HexDig,HexDig,         'hex2','add',0)
    ,('hex2',HexDig,'',              'idle','push','hex')

    ,('bin2',BinDig,BinDig,         'bin2','add',0)
    ,('bin2',BinDig,'',              'idle','push','bin')


    ,('ubin1','b',BinDig,         'ubin2','add',0)
    ,('uhex1','h',HexDig,         'uhex2','add',0)
    ,('udig1','d',Digits,         'udig2','add',0)

    ,('udig2',Digits,Digits,         'udig2','add',0)
    ,('udig2',Digits,'',             'idle','push','udig')

    ,('uhex2',HexDig,HexDig,         'uhex2','add',0)
    ,('uhex2',HexDig,'',              'idle','push','uhex')

    ,('ubin2',BinDig,BinDig,         'ubin2','add',0)
    ,('ubin2',BinDig,'',              'idle','push','ubin')


    ,('idle','(','*',             'either','add',0)
    ,('either','*',')',             'either1','add',0)
    ,('either1',')','',             'idle','push','star')
    ,('either','*','',             'pragma1','add',0)
    ,('pragma1','*',')',             'pragma2','add',0)
    ,('pragma2',')','',             'idle','push','pragma')

    ,('idle',':','=',             'cassign','add',0)
    ,('cassign','=','',             'idle','push','double')
    ,('idle','-',':',             'new:','add',0)
    ,('idle','+',':',             'new:','add',0)
    ,('new:',':','',             'idle','push','double')
    ,('idle','=','=',             'eqeq2','add',0)
    ,('eqeq2','=','=',             'eqeq3','add',0)
    ,('eqeq3','=','',             'idle','push','double')
    ,('eqeq2','=','',             'idle','push','double')

    ,('idle','/','=',             'neq2','add',0)
    ,('neq2','=','',              'idle','push','double')



    ,('idle','*','*',                'power','add',0)
    ,('power','*','',                'idle','push','power')
    ,('idle',Doubles,Doubles2,        'double','add',0)
    ,('double',Doubles,'',           'idle','push','double')

    ,('idle',Doubles,'',       'idle','push','double')
    ,('idle','"','',                  'string','add',0)
    ,('string','"','',                'idle','push','string')
    ,('string',AnyChar,'',                'string','add',0)

    ,('idle',Singles,'',             'idle','push','single')
    ,('idle','\\','',             'idle','add','idle')
]

ReservedWordsStr = '''
Library Package Body Use Entity Is Port In Out InOut To Floating GreaterEqual EqualLess
End Of Signal Architecture Process If Then Elsif Else When 
Behavioral Begin Token String Event
And Or Xor Not Nand Nor Neq 

Type Subtype Case Others Arrow Cassign Constant Literal
Map Component HexString HobString Null Generic
Configuration Structural For  Variable Wait Loop While Until
Alias Procedure  Function After Return File  Assert Array
Buffer Range Generate Timeunit
Shared Postponed Report Mod Attribute  On  
Pure Impure Block Record New 
With Select
Transport Inertial Exit Power Reject
Guarded Next Linkage Openevent
Tick
downto to
srl
'''

ReservedWords = string.split(string.lower(ReservedWordsStr))




if __name__ == '__main__':
    main()
