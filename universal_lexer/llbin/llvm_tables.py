
Joines = []
Modifiers = []
EOL = [10]

DoubleNames = {}
Types = ''


LowLetters = 'qwertyuiopasdfghjklzxcvbnm'
CapLetters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
Letters = LowLetters+CapLetters
Digits='0123456789'
Alphas = Letters+Digits+'_'
Singles = ':=;*,}{()[]<>'
Doubles = ''
Doubles2 = ''
Spaces = ' \t \\'
AnyChar = Letters+Digits+Spaces+'-_.'+Singles+Doubles+",\\/+"


Vars = Alphas + '.-'

Table = [
     ('idle',Spaces,'',             'idle','none',0)
    ,('idle','%',Vars,           'var','add',0)
    ,('var',Vars,Vars,              'var','add',0)
    ,('var',Vars,'',                'idle','push','var')


    ,('idle','-',Digits,             'number','add',0)
    ,('idle',Digits,Digits,             'number','add',0)
    ,('idle',Digits,'.',             'floating','add',0)
    ,('number',Digits,Digits,       'number','add',0)
    ,('number',Digits,'.',       'floating','add',0)
    ,('number',Digits,'',           'idle','push','number')
    ,('idle',Digits,'',             'idle','push','number')


    ,('floating','.',Digits,       'floating','add',0)
    ,('floating',Digits,Digits,       'floating','add',0)
    ,('floating',Digits,'e',       'floating','add',0)
    ,('floating','e','+',       'floating','add',0)
    ,('floating','+',Digits,       'floating','add',0)
    ,('floating',Digits,'',       'idle','push','floating')



    ,('idle',Vars,Vars,            'token','add',0)
    ,('token',Vars,Vars,        'token','add',0)
    ,('token',Vars,'',            'idle','push','token')
    ,('idle',Letters,'',            'idle','push','token')

    ,('idle','@',Letters,          'func','add',0)
    ,('func',Vars,Vars,        'func','add',0)
    ,('func',Vars,'',            'idle','push','func')

    ,('idle','#',Digits,          'gader','add',0)
    ,('gader',Digits,Digits,        'gader','add',0)
    ,('gader',Digits,'',            'idle','push','gader')

    ,('idle','!','"',          'idle','push','meta')
    ,('idle','!','{',          'idle','push','meta')
    ,('idle','!',Alphas,          'exlm','add',0)
    ,('exlm',Vars,Vars,        'exlm','add',0)
    ,('exlm',Vars,'',            'idle','push','exlm')


    ,('idle','"','',             'string','add',0)
    ,('idle',"'",'',             'string','add',0)
    ,('string',AnyChar,'',       'string','add',0)
    ,('string','"','',           'idle','push','string')
    ,('string',"'",'',           'idle','push','string')


    ,('idle',Singles,'',             'idle','push','single')
]

ReservedWordsStr = '''
target datalayout triple global common align define i16 i1 i32  i64
load store ret mul div udiv add sub 
void nocapture 
nounwind ssp uwtable
ModuleID
Function Attrs
attributes bitcast
metadata
alloca and br call declare eq extractelement false getelementptr
i8 icmp inbounds label ne nsw nuw or phi preds readnone readonly sdiv
shufflevector to trunc ugt ult undef x zeroext zext
ashr byval double exact fadd fcmp float fmul fptrunc fsub insertelement ogt olt sext 
shl switch tail type zeroinitializer 
signext
sgt slt 
xor lshr  shl srem urem
null select tail
''' 
