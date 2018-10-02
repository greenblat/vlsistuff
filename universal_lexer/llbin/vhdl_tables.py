Joines = []
Modifiers = [('std_logic_vector','Types'),('std_logic','Types'),('integer','Types'),('bit_vector','Types')]
EOL = []

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
Spaces = '\t\n '
AnyChar = Letters+Digits+Spaces+'_'+Singles+Doubles+"',\\"



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
    ,('idle','-',':',             'newx','add',0)
    ,('idle','+',':',             'newx','add',0)
    ,('newx',':','',             'idle','push','double')
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
library package body use entity is port in out inout to floating GreaterEqual EqualLess
end of signal architecture process if then elsif else when 
behavioral begin token string event
and or xor not nand nor neq 

type subtype case others arrow cassign constant literal
map Component hexstring hobstring null generic
configuration structural for  variable wait loop while until
alias procedure  function after return file  assert array
buffer range generate timeunit
shared Postponed report mod attribute  on  
pure impure block record new 
with select
transport inertial exit power reject
guarded next linkage openevent
tick
downto to
srl
natural
'''

