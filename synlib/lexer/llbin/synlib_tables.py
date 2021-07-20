Joines = []
Modifiers = []
EOL = [10]
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
    ,('idle',Digits,'e',            'floating','add',0)
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
    ,('floating','e','+',     'floating','add',0)
    ,('floating','+',Digits,     'floating','add',0)
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

    ,('idle','-',':',             'new','add',0)
    ,('idle','+',':',             'new','add',0)
    ,('new',':','',             'idle','push','double')
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





