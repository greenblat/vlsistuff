#! /usr/bin/python3

import sys,os
import cProfile
import traceback

def main():
    Fname = sys.argv[1]
    run_lexer(Fname,'lex.out')

class DbClass:
    def __init__(self):
        self.state='idle'
        self.Token=''
        self.Queue=[]


def run_lexer(Fname,Ofname):
    global Db
    Db=DbClass()
    try:
        File = open(Fname)
    except:
        print('lexer failed to open %s'%Fname)
        print(traceback.print_stack())
        return
    Db.Ofile = open(Ofname,'w')
    work(File)
    work_out_queue(True)
    Db.Ofile.close()

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
#            print('line',line,)
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
            print(Db.state,action,kind,'error line=%d pos=%d chr="%s" %s'%(LineNum,i,line[i],line[:-1]))
            sys.exit()
def push_token(Token,kind,LineNum,LinePos):
#    print('push_token    %s %s %s %s\n'%(Token,kind,LineNum,LinePos))
    if (kind=='token')and(Token in ReservedWords):
        kind=Token
    elif (kind=='define')and(Token in ReservedWords):
        kind='backtick_'+Token[1:]
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
        List[1]=doublesName(List[0])
        return tuple(List)
    return Tup

DoubleNames = {}
DoubleNames['&&'] = 'and_and'
DoubleNames['=='] = 'eq_eq'
DoubleNames['!='] = 'not_eq'
DoubleNames['||'] = 'or_or'
DoubleNames['>='] = 'gr_eq'
DoubleNames['<='] = 'sm_eq'
DoubleNames['->'] = 'emit'
DoubleNames['!^'] = 'xnor'
DoubleNames['>>'] = 'shift_right'
DoubleNames['<<'] = 'shift_left'
DoubleNames['+:'] = 'plus_range'
DoubleNames['-:'] = 'minus_range'


def doublesName(Txt):
    if Txt in DoubleNames:
        return DoubleNames[Txt]
    else:
        print('ilia! doubles names missing %s'%Txt)
        return Txt


def stepit(Pos,Char,Char1,State):
    rule=0
    for (St,Ch0,Ch1,Next,Action,Kind) in Table:
        if (St==State):
#            print('tryrule%d ch=%s ch1=%s in0=%d in1=%d st=%s ch0=%s ch1=%s next=%s act=%s kind=%s'%(rule,Char,Char1,(Char in Ch0),(Char1 in Ch1),State,Ch0,Ch1,Next,Action,Kind))
            rule +=1
            if (Ch0=='')or(Char in Ch0):
                if (Ch1=='')or(Char1 in Ch1):
                    return  Next,Action,Kind
    print('lexer: no rule fits st=%s ch=%s ch1=%s'%(State,Char,Char1))
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
Spaces = '\t \\'
AnyChar = Letters+Digits+Spaces+'_'+Singles+Doubles+"',\\"

LegalDoublesStr = '** -> == != <= >= => =< && ||'
LegalDoubles = LegalDoublesStr.split()

#    ,('idle','(','*',               'pragma','add',0)
#    ,('pragma','*',' ',             'idle','push','pragma_start')
#    ,('idle','*',')',               'pragma2','add',0)
#    ,('pragma2',')','',             'idle','push','pragma_end')

Table = [
     ('idle',Spaces,'',             'idle','none',0)
    ,('idle','/','/',               'idle','skipline',0)


    ,('idle','/','*',               'comment','none',0)
    ,('comment','*','/',            'comment2','none',0)
    ,('comment2','/','',            'idle','none',0)
    ,('comment','','',              'comment','none',0)

    ,('idle','`',Letters,           'define','add',0)
    ,('define',Alphas,Alphas,       'define','add',0)
    ,('define',Alphas,'',           'idle','push','define')
    ,('idle',Letters+'$'+'_',Alphas,    'token','add',0)
    ,('token',Alphas,Alphas,        'token','add',0)
    ,('token',Alphas,'',            'idle','push','token')
    ,('idle',Letters,'',             'idle','push','token')

    ,('idle',Digits,Digits,         'number','add',0)
    ,('idle',Digits,'.',            'floating0','add',0)
#    ,('idle',Digits,"'",            'sizednumber','add',0)
    ,('idle',Digits,'',             'idle','push','number')
    ,('idle',"'",'b',               'ubin1','add',0)
    ,('idle',"'",'h',               'uhex1','add',0)
    ,('idle',"'",'d',               'udig1','add',0)

    ,('number',Digits,Digits,       'number','add',0)
    ,('number',Digits,"'",          'sizednumber','add',0)
    ,('number',Digits,'.',          'floating0','add',0)
    ,('number',Digits,'',           'idle','push','number')
    ,('floating0','.',Digits,     'floating','add',0)
    ,('floating',Digits,Digits,     'floating','add',0)
    ,('floating',Digits,'e',     'floating','add',0)
    ,('floating','e',Digits,     'floating','add',0)
    ,('floating','e','-',     'floating','add',0)
    ,('floating','-',Digits,     'floating','add',0)
    ,('floating',Digits,'',         'idle','push','floating')

    ,('sizednumber',"'",'b',          'bin1','add',0)
    ,('sizednumber',"'",'h',          'hex1','add',0)
    ,('sizednumber',"'",'d',          'dig1','add',0)

    ,('bin1','b',BinDig,         'bin2','add',0)
    ,('hex1','h',HexDig,         'hex2','add',0)
    ,('dig1','d',Digits,         'dig2','add',0)

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

    ,('idle','-',':',             'new:','add',0)
    ,('idle','+',':',             'new:','add',0)
    ,('new:',':','',             'idle','push','double')
    ,('idle','=','=',             'eqeq2','add',0)
    ,('eqeq2','=','=',             'eqeq3','add',0)
    ,('eqeq3','=','',             'idle','push','double')
    ,('eqeq2','=','',             'idle','push','double')

    ,('idle','!','=',             'neq2','add',0)
    ,('neq2','=','=',             'neq3','add',0)
    ,('neq3','=','',              'idle','push','double')
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
library cell pin timing
statetable  ff latch test_cell
values
'''

ReservedWords = ReservedWordsStr.split()




if __name__ == '__main__':
    main()

