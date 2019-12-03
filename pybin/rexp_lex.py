#! /usr/bin/python3
'''
USAGE:
rexp_lex.py lex.out parse.py
parse.py is attempt to recognize stuff in vhdl lexed file (using vhdl_lexer).

parse.py file:

from __main__ import adddouble,addset,addpat,sequence,Pattern
def entity(Map,What):
    print('entity MAP',Map[0][0],len(Map[1]),What)
    sequence(Map[1],Pattern)
    print('KKKLK')


def architecture(Map,What):
    print('architecture MAP',Map[0][0],len(Map[1]),What)

def inout(Map,What):
    print('input what ',What,Map)

def ending():
    print('ending')


adddouble('beginend begin end')

# addpat('process () beginend process ;',process,1,False)
# addpat('process () *  end process ;',process,2,False)


addpat('entity ? is port () ; end ? ;',entity,1,False)
addpat('ARCHITECTURE struct of ? is * end struct ;',architecture,1,False)

addset('dir in out inout')
addpat('? : dir STD_LOGIC ;',inout,1,False)
addpat('? : dir STD_LOGIC_VECTOR () ;',inout,2,False)


'''

import os,sys,string
sys.path.append('.')
import logs3 as logs
import importlib

Tokens = []
def main():
    global Ptr,Pattern
    Fname = sys.argv[1]
    Pattern = sys.argv[2]
    print(Pattern,logs.endsWith(Pattern,'.py'))
    sys.exit()
    if logs.endsWith(Pattern,'.py'):
        Pattern = Pattern[:-3]
#    exec('import %s as Ptr'%Pattern)
    Ptr = importlib.__import__(Pattern)
    File = open(Fname)
    logs.setVar('fname',Fname)
    loadFile(File)    
    sequence(Tokens,Pattern)
    Ptr.ending()

def sequence(Tokens,Pattern):
    print('tokens=%d'%len(Tokens))
    logs.setVar('tokens',len(Tokens))
    run(Pattern,Tokens)

def run(Pattern,Tokens):
    Ptr = importlib.__import__(Pattern)
    indtok = 0
    Limittok = len(Tokens)
    Limitpat = len(PATTERNS)
    while indtok<Limittok:
        indpat = 0
        while (indpat<Limitpat):
            Pat,Action,Mode,Verbose = PATTERNS[indpat]
            Tok0 = Tokens[indtok]
            try:
                Tok1 = Tokens[indtok+1]
            except:
                Tok1 = ('eof','eof',0,0)
            Len,Vars =  matches(indtok,Tokens,Pat,0,Verbose)
            if Verbose:
                logs.log_info('final out %s %s %s'%(Len,Vars,Tokens[indtok]))
            indpat += 1
            if Len>0:
                indpat = Limitpat + 10
                Action(Vars,Mode)
                indtok += Len  
        if (indpat==Limitpat):
            indtok += 1


def loadFile(File):
    while 1:
        line = File.readline()
        if line=='': 
            Tokens.append(('eol','eol',99999,00000))
            Tokens.append(('eol','eol',99999,00000))
            Tokens.append(('eol','eol',99999,00000))
            return
        line = line.lower()
        wrds = line.split()
        if len(wrds)==0:
            pass
        elif(len(wrds)==4):
            Rec = (wrds[0],wrds[1],int(wrds[2]),int(wrds[3]))
            Tokens.append(Rec)
        elif(len(wrds)>4):
            Str = string.join(wrds[:-3])
            Rec = (Str,wrds[-3],int(wrds[-2]),int(wrds[-1]))
            Tokens.append(Rec)

def matches(ind,Tokens,Pat,Level=0,Verbose=False):
    if (ind+len(Pat))>=logs.getVar('tokens'):
        return 0,[]
    if Verbose and (Level>0): logs.log_info('%d enter %s %s %s %s'%(Level,Pat,ind,Tokens[ind],Tokens[ind+1]))
    Tok,Kind,Lnum,Cnum = Tokens[ind]
    PP = Pat[0]
    
    if PP in SETS:
        Set = SETS[PP]
        for P0 in Set:
            if (P0==Tok):
                if len(Pat)==1:
                    return 1,[Tokens[ind]]
                LL,VV = matches(ind+1,Tokens,Pat[1:],Level+1,Verbose)
                if LL>0:
                    return LL+1,[Tokens[ind]]+VV
                else:
                    return 0,[]

    if (PP==Tok):
        if len(Pat)==1:
            return 1,[]
        LL,VV = matches(ind+1,Tokens,Pat[1:],Level+1,Verbose)
        if LL>0:
            return LL+1,VV
        else:
            return 0,[]

    elif( (PP[0]=='?')and(PP[1:]==Kind))or(PP=='?'):
        if len(Pat)==1:
            return 1,[Tokens[ind]]
        LL,VV = matches(ind+1,Tokens,Pat[1:],Level+1,Verbose)
        if LL>0:
            return LL+1,[Tokens[ind]]+VV
        else:
            return 0,[]

    if PP=='*':
        Next = Pat[1]
        LL=0
        org = ind
        while True:
            while (ind<logs.getVar('tokens'))and(Tokens[ind][0]!=Next):
                ind += 1
                LL += 1
            if ind==logs.getVar('tokens'): return 0,[]
            if len(Pat)==2: 
                return LL,[]
            LL,VV = matches(ind+1,Tokens,Pat[2:],Level+1,Verbose)
            if LL>0: 
                return LL+1,[Tokens[org:ind]]+VV
            else:
                ind += 1

    if PP in DOUBLES:
        Bef,Aft = DOUBLES[PP]
        if Tokens[ind][0]=='eol': ind+=1 
        if Tokens[ind][0]!=Bef:
            if Verbose: logs.log_info('() failed on %s'%Bef)
            return 0,[]
        Closing = findBalancedClosing(ind,Tokens,Bef,Aft)
        if Closing<0: 
            if Verbose: logs.log_info('doubles failed on closing')
            return 0,[]
#        print('>>closingDBL>>>',Closing,Tokens[Closing])
        if len(Pat)==1:
            return Closing-ind,[Tokens[ind:Closing]]

        LL,VV = matches(Closing,Tokens,Pat[1:],Level+1,Verbose)
        if LL==0: 
            if Verbose: 
                logs.log_info('double failed on postmatch tokens=%s %s pattern=%s'%(Tokens[Closing],Tokens[Closing+1],Pat[1:]))
            return 0,[]
        return LL+Closing-ind,[Tokens[ind:Closing]]+VV

    if PP in ['()','[]']:
        if PP=='()': Bef,Aft = '(',')'
        if PP=='[]': Bef,Aft = '[',']'
        if Tokens[ind][0]=='eol': ind+=1 
        if Tokens[ind][0]!=Bef:
            if Verbose: print('() failed on %s'%Bef)
            return 0,[]
        Closing = findBalancedClosing(ind,Tokens,Bef,Aft)
        if Closing<0: 
            if Verbose: print('() failed on closing')
            return 0,[]
#        print('>>closing()()>>>',Closing,Tokens[Closing])
        if len(Pat)==1:
            return Closing-ind,[Tokens[ind:Closing]]
        LL,VV = matches(Closing,Tokens,Pat[1:],Level+1,Verbose)
        if LL==0: 
            if Verbose: 
                logs.log_info('lvl=%d ()[] failed on postmatch tokens=%s %s  patern=%s'%(Level,Tokens[Closing],Tokens[Closing+1],Pat[1:]))
            return 0,[]
        return LL+Closing-ind,[Tokens[ind:Closing]]+VV


    if (Level>0)and(Tokens[ind][0]=='eol'):
        return matches(ind+1,Tokens,Pat,Level,Verbose)
    return 0,[]
            
def findBalancedClosing(ind,Tokens,Up,Down):
    if Tokens[ind][0]!=Up: return -1
    Lvl = 0
    Len=logs.getVar('tokens')
    while ind<Len:
        if Tokens[ind][0]==Up: Lvl += 1
        if Tokens[ind][0]==Down: Lvl -= 1
        ind += 1
        if Lvl==0: return ind
    return -1
            

SETS = {}
def addset(Str):
    wrds = Str.split()
    Set = wrds[0]
    SETS[Set] = wrds[1:]

DOUBLES = {}
def adddouble(Str):
    wrds = Str.split()
    Set = wrds[0]
    DOUBLES[Set] = (wrds[1],wrds[2])

PATTERNS = []
def addpat(Str,Action,Mode=False,Verbose=False):
    PATTERNS.append((Str.lower().split(),Action,Mode,Verbose))



if __name__ == '__main__': main()

