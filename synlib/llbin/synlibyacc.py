#! /usr/bin/python3

import os,sys
import pickle
from synlib_yacc_table import *
def main():
    FlexName = sys.argv[1]
    run_yacc(FlexName)

def run_yacc(Flexname):
    global DataBase
    global Fout
    global Stack
    global Lex    
    global Uniques

    Lex=[]
    Stack=[]
    DataBase={}
    Uniques={}

    Fout=open('yacc.log','w')
    readlexfile(Flexname)
    run_machine()
    reportDb()
    Fout.close()

def readlexfile(Flexname):
    Flex=open(Flexname)
    while 1:
        line = Flex.readline()
        if line=='':
            Lex.append(('$end','$end',-1,-1))
            Lex.append(('$end','$end',-1,-1))
            Flex.close()
            print('%d lex tokens read'%len(Lex))
            return
        wrds = line.split()
        if len(wrds)==0:
            pass
        elif len(wrds)==4:
            if wrds[1]=='single':
                wrds[1]=wrds[0]
            elif wrds[1]=='double':
                wrds[1]=wrds[0]
            Lex.append(tuple(wrds))
        elif (wrds[-3]=='pragma'):
            Str = ' '.join(line[1:-4])
            Lex.append(tuple([Str]+wrds[-3:]))
        elif (line[0]=='"'):
            Ind = line[1:].index('"')
            Str = line[:Ind+2]
            wrds = line[Ind+2:].split()
            Lex.append(tuple([Str]+wrds))
        fix_bad_syntax(Lex)

def fix_bad_syntax(Lex):
    if len(Lex)<4:
        return
    if (Lex[-1][1]=='token')and(Lex[-3][1]==':')and(Lex[-4][1]=='token')and(Lex[-2][1] in ['number','floating']):
        Line1 = int(Lex[-1][2])
        Line2 = int(Lex[-2][2])
        if Line1>Line2:
            Pop = Lex.pop(-1)
            Lex.append((';',';',Line2,0))
            Lex.append(Pop)
#            print(Lex[-1][1],Lex[-2][1],Lex[-3][1],Lex[-4][1],Lex[-1][2],Lex[-2][2],Lex[-3][2],Lex[-4][2])



Verbose=False
def run_machine():
    state='0'
    steps=0
    while (state!=0):
        if (Verbose):
            print('stepit state=%s tok=%s stack=%s'%(state,Lex[0],Stack))
        nextstate = step_machine(state)
        state=nextstate
        steps +=1
        if (steps % 2000)==0:
            print('%d steps synlibyacc  line=%s '%(steps,Lex[0][2]))
    print('exit state',state,len(Lex))

def uniq(What):
    if (What not in Uniques):
        Uniques[What]=1
    X = Uniques[What]
    Uniques[What] += 1
    return X



def step_machine(state):
    List = States[state]
    (Tok,Kind,Lnum,Pos)=Lex[0]
#    print( 'yacc tok="%s" kind=%s lnum=%s pos=%s state=%s'%(Tok,Kind,Lnum,Pos,state))
    for (Act,Param,Next) in List:
#        print('try',Act,Param,Next)
        if (Act=='shift'):
            if (matches_ok(Tok,Kind,Act,Param)):
                Stack.append((Tok,Kind,Lnum,Pos,state))
                Lex.pop(0)
                return Next
        elif Act=='reduce':
            Rule=Next
            Name,Wrds = Rules[Rule]
            Wrds=Wrds[:]
#            print('reduce action rule=%s name=%s wrds=%s'%(Rule,Name,Wrds))
            Id = uniq(Name)
#            Fout.write('reduce %s %d %s\n'%(Name,Id,Stack[-len(Wrds):]))
            if len(Wrds)==0:
                addToDb(Name,Id,[])
            else:
                addToDb(Name,Id,Stack[-len(Wrds):])
            NST=state
            while Wrds!=[]:
#                print('work reduce wrds=%s stack=%s %s %s %s %s %s'%(Wrds,Stack,Lnum,Pos,Rule,Name,Wrds))
                TT,KK,Lnum1,Pos1,NST = Stack.pop(-1)
                Wrds.pop(0)
            Lex.insert(0,(Name,Name,Id,-1))
            return NST
        elif Act=='goto':
            if (Param==Kind):
                Lex.pop(0)
                Stack.append((Tok,Kind,Lnum,Pos,state))
                return Next
        elif Act=='accept':
            return 0
    print('error! yaccer: no valid operation act=%s tok=%s kind=%s lnum=%s pos=%s state=%s'%(Act,Tok,Kind,Lnum,Pos,state))
    for (T,K,L,P,S) in Stack:
        print('stack tok="%s" kind=%s lnum=%s pos=%s state=%s'%(T,K,L,P,S))
    return False

def addToDb(Name,Id,List):
    DataBase[(Name,Id)]=clean_up(List)

def clean_up(List):
    Res=[]
    for Item in List:
        Item1 = Item[:-1]
        if Item[3]==-1:
            Res.append((Item[0],Item[2]))
        else:
            Res.append(Item1)
    return Res


def reportDb():
    for Key in DataBase:
        Fout.write('%s %s\n'%(Key,DataBase[Key]))
    Outf = open('db0.pickle','wb')
    pickle.dump(DataBase,Outf)
    Outf.close()



def matches_ok(Tok,Kind,Act,Param):
#    print('matches_ok',(Tok==Param)or(Kind==Param),Tok,Kind,Act,Param)
    if (Tok==Param)or(Kind==Param):
        return True
    return False


Mstack=[]


def load_yacc_table(Fname):
    global Rules,States
    File = open(Fname)
    Rules = pickle.load(File) 
    States = pickle.load(File) 
    File.close()

if __name__ == '__main__':
    main()



