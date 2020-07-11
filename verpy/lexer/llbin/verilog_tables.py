
Joines = [('number','uhex'),('number','udig'),('number','ubin')]
Modifiers = []
EOL = [10]



DoubleNames = {}
DoubleNames['::'] = 'domino'
DoubleNames['&&'] = 'and_and'
DoubleNames['=='] = 'eq_eq'
DoubleNames['!='] = 'not_eq'
DoubleNames['||'] = 'or_or'
DoubleNames['>='] = 'gr_eq'
DoubleNames['<='] = 'sm_eq'
DoubleNames['->'] = 'emit'
DoubleNames['!^'] = 'xnor'
DoubleNames['~^'] = 'xnor'
DoubleNames['>>'] = 'shift_right'
DoubleNames['>>>'] = 'arith_shift_right'
DoubleNames['<<'] = 'shift_left'
DoubleNames['+:'] = 'plus_range'
DoubleNames['-:'] = 'minus_range'
DoubleNames['!&'] = 'nand'
DoubleNames['~&'] = 'nand'
DoubleNames['!|'] = 'nor'
DoubleNames['~|'] = 'nor'
DoubleNames['==='] = 'eq3'
DoubleNames['!=='] = 'noteqeq'


    
LowLetters = 'qwertyuiopasdfghjklzxcvbnm'
CapLetters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
Letters = LowLetters+CapLetters
Digits='0123456789'
Alphas = Letters+Digits+'_'
HexDig = Digits+'abcdef'+'ABCDEF'+'_'+'xX'
BinDig = '01_xzXZ?'
Singles = '?.,[]{}#@()~%^;:/+-*'
Doubles = '~-=!<>&|'
Doubles2 = '^=<>&|'
Spaces = '\t \n'
AnyChar = Letters+Digits+Spaces+'_'+Singles+Doubles+"`',\\"

Multi = Alphas+Singles+Doubles+Doubles2


Table = [
     ('idle',Spaces,'',             'idle','none',0)
    ,('idle','/','/',               'idle','skipline',0)

    ,('idle','\\','',               'backline','add',0)
    ,('backline',' ','',            'idle','push','token')
    ,('backline',Multi,'',          'backline','add',0)

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
    ,('idle',Digits,'',             'idle','push','number')
    ,('idle',"'",'b',               'ubin1','add',0)
    ,('idle',"'",'h',               'uhex1','add',0)
    ,('idle',"'",'d',               'udig1','add',0)
    ,('idle',"'",'{',               'idle','none',0)

    ,('number',Digits,Digits,       'number','add',0)
    ,('number',Digits,"'",          'sizednumber','add',0)
    ,('number',Digits,'.',          'floating0','add',0)
    ,('number',Digits,'',           'idle','push','number')
    ,('floating0','.',Digits,     'floating','add',0)
    ,('floating',Digits,Digits,     'floating','add',0)
    ,('floating',Digits,'',         'idle','push','floating')

    ,('sizednumber',"'",'b',          'bin1','add',0)
    ,('sizednumber',"'",'h',          'hex1','add',0)
    ,('sizednumber',"'",'d',          'dig1','add',0)

    ,('bin1','b',' ',         'bin2','add',0)
    ,('bin1','b',BinDig,         'bin2','add',0)
    ,('hex1','h',HexDig,         'hex2','add',0)
    ,('dig1','d',Digits,         'dig2','add',0)
    ,('dig1','d',' ',         'dig2','add',0)

    ,('dig2',Digits,Digits,         'dig2','add',0)
    ,('dig2',Digits,'_',         'dig2','add',0)
    ,('dig2',Digits,'',             'idle','push','dig')

    ,('hex2',HexDig,HexDig,         'hex2','add',0)
    ,('hex2',HexDig,'',              'idle','push','hex')

    ,('bin2',' ','',         'bin2','add',0)
    ,('bin2',BinDig,BinDig,         'bin2','add',0)
    ,('bin2',BinDig,'',              'idle','push','bin')


    ,('ubin1','b',' ',            'ubin2','add',0)
    ,('ubin1','b',BinDig,         'ubin2','add',0)
    ,('uhex1','h',HexDig,         'uhex2','add',0)
    ,('udig1','d',Digits,         'udig2','add',0)
    ,('udig1','d',' ',         'udig2','add',0)
    ,('uhex1','h',' ',         'uhex2','add',0)

    ,('udig2',' ',Digits,         'udig2','add',0)
    ,('udig2',Digits,Digits,         'udig2','add',0)
    ,('udig2',Digits,'',             'idle','push','udig')

    ,('uhex2',' ',HexDig,         'uhex2','add',0)
    ,('uhex2',HexDig,HexDig,         'uhex2','add',0)
    ,('uhex2',HexDig,'',              'idle','push','uhex')

    ,('ubin2',' ','',         'ubin2','add',0)
    ,('ubin2',BinDig,BinDig,         'ubin2','add',0)
    ,('ubin2',BinDig,'',              'idle','push','ubin')


    ,('idle','(','*',             'either','add',0)
    ,('either','*',')',             'either1','add',0)
    ,('either1',')','',             'idle','push','star')
    ,('either','*','',             'pragma1','none',0)
    ,('pragma1','*',')',             'pragma2','none',0)
    ,('pragma1','','',             'pragma1','none',0)
    ,('pragma2',')','',             'idle','clear',0)

    ,('idle',':',':',             'new','add',0)
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

    ,('idle','<','>',        'newver','add',0)
    ,('newver','<','>',        'newver3','add',0)
    ,('newver',AnyChar,AnyChar,        'newver','add',0)
    ,('newver3','','',        'idle','push','newver')

    ,('idle','>','>',        'shift0','add',0)
    ,('shift0','>','>',        'shift1','add',0)
    ,('shift0','>','',        'idle','push','double')
    ,('shift1','>','',        'idle','push','double')

    ,('idle','*','*',                'power','add',0)
    ,('power','*','',                'idle','push','power')
    ,('idle',Doubles,Doubles2,        'double','add',0)
    ,('double',Doubles2,'',           'idle','push','double')

    ,('idle',Doubles,'',       'idle','push','double')
    ,('idle','"','',                  'string','add',0)
    ,('string','"','',                'idle','push','string')
    ,('string',AnyChar,'',                'string','add',0)

    ,('idle',Singles,'',             'idle','push','single')
    ,('idle','\\','',             'idle','add','idle')
]

ReservedWordsStr = '''
    `define `include `ifdef `ifndef `endif `undef `timescale
    `default_nettype
    module endmodule primitive endprimitive function endfunction
    task endtask
    generate endgenerate genvar
    table endtable
    signed input output inout wire reg tri0 tri1
    always begin end

assign deassign
force release

fork join join_any join_none
specify specparam defparam endspecify

vectored
repeat
wreal
tri tri0 tri1 wand trireg
supply0 supply1
wait
case
casex
casez
endcase
default
forever
always_ff
always_comb
always_latch
property
endproperty
sequence
endsequence
assert
_unique
_priority
or
if
else
parameter
for
while
initial
forever
endprimitive
strong1 strong0 pull1 pull0 weak1 weak0 highz1 highz0
posedge negedge
integer real time
event
disable
localparam
    
class
rand
bit
endclass
constraint
enum
typedef
covergroup
endgroup
coverpoint
cross
bins
iff
new
with
semaphore
randomize
extends
mailbox
'''





