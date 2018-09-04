#! /usr/bin/python


import os,sys,string


def main():
    Fnamein = sys.argv[1]
    Fnameout = sys.argv[2]
    Fin = open(Fnamein)
    Fout = open(Fnameout,'w')
    while 1:
        line = Fin.readline()
        if line=='':
            Fout.close()
            Fin.close()
            return
        modified = modifyLine(line)
        Fout.write(modified)

LIST0 = string.split('''
    Library Use Package End Return Downto Is Function Body Entity Port In Inout Out
    Architecture Of Signal  Process If Then Else Variable Range Wait  Until
    To And  Elsif Not Or Xor Case When Others Component Map For Loop Exit Srl
    Type Assert Report Generic Buffer Array Generate
''')
LIST1 = {'token':'Identifier','dotted':'DOTTED'
    ,'number':'DecimalInt'
    ,'Types':'Identifier'
    ,'Constant':'CONSTANT'
    ,'Cassign':'VarAsgn'
    ,'string':'BitStringLit'
    ,'Assign':'LESym'
    ,'tick':'Apostrophe'
    ,'Event':'Identifier'
    ,'Neq':'NESym'
    ,'floating':'DecimalReal'
    ,'hexdig':'BasedInt'
    ,'+':'Plus'
    ,'-':'Minus'
    ,'|':'Bar'
    ,'characters':'StringLit'
    ,'Null':'NULL_'
}
LIST2 = { 
     '(':'LeftParen'
    ,')':'RightParen'
    ,':':'Colon'
    ,';':'Semicolon'
    ,',':'Comma'
    ,'.':'Dot'
    ,'*':'Star'
    ,'/':'Slash'
    ,'=':'EQSym'
    ,'<=':'LESym'
    ,'<':'LTSym'
    ,'=>':'GESym'
    ,'>=':'GESym'
    ,'>':'GTSym'
    ,'gr_eq':'GESym'
    ,'&':'Ampersand'
    ,'Begin':'BEGIN_'
}

def modifyLine(line):
    wrds = string.split(line)
    if (len(wrds)>4)and(wrds[0][0]=='"'):
        New = wrds[0]
        ind=1
        while '"' not in wrds[ind]:
            New += '.'+wrds[ind]
            ind += 1
        New += '.'+wrds[ind]
        wrds = [New,'characters',wrds[-2],wrds[-1]]
        print 'wrds',wrds
        
    if len(wrds)==4:
        Key = wrds[0]
        if wrds[0]=='severity':
            modified = 'SEVERITY SEVERITY %s %s\n'%(wrds[2],wrds[3])
            return modified
        if Key in LIST0:
            New = string.upper(Key)
            modified = '%s %s %s %s\n'%(New,New,wrds[2],wrds[3])
            return modified
        if wrds[1] in LIST1:
            New = LIST1[wrds[1]]
            modified = '%s %s %s %s\n'%(wrds[0],New,wrds[2],wrds[3])
            return modified
        if wrds[1] in LIST2:
            New = LIST2[wrds[1]]
            modified = '%s %s %s %s\n'%(New,New,wrds[2],wrds[3])
            return modified
            


    return line



main()


