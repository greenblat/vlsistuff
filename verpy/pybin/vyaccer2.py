#! /usr/bin/python

Verbose = False
import os,sys,string
import pickle
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs'%NewName)

import logs
print 'mmmmmmmmmmmmmmmmmmmmmmmmmmm '
from verilog_yacc_table import *
def main():
    YaccTableName = False
    if len(sys.argv)==1:
        FlexName = 'lex.out'
        YaccTableName = False
    elif len(sys.argv)==2:
        FlexName = sys.argv[1]
        YaccTableName = False
    elif len(sys.argv)==3:
        FlexName = sys.argv[1]
        YaccTableName =  sys.argv[2]
    run_yacc(YaccTableName,FlexName,'.','aaa.vhdl')

def run_yacc(YaccTableName,Flexname,RunDir,Fname):
    global DataBase
    global Fout
    global Stack
    global Lex    
    global Uniques
    global origFname
    origFname=Fname

    Lex=[]
    Stack=[]
    DataBase={}
    Uniques={}

    Fout=open('%s/yacc.log'%RunDir,'w')

    if YaccTableName:
        load_yacc_table(YaccTableName)
    logs.log_info('yacc step0')
    readlexfile(Flexname)
    logs.log_info('yacc step1')
    run_machine()
    logs.log_info('yacc step2')
    reportDb(RunDir)
    logs.log_info('yacc step3')
    Fout.close()

def readlexfile(Flexname):
    Flex=open(Flexname)
    while 1:
        line = Flex.readline()
        if line=='':
            Lex.append(('$end','$end',-1,-1))
            Lex.append(('$end','$end',-1,-1))
            Flex.close()
            return
        wrds = string.split(line)
        if len(wrds)==0:
            pass
        elif len(wrds)==4:
            if wrds[1]=='single':
                wrds[1]=wrds[0]
            elif wrds[1]=='double':
                wrds[1]=wrds[0]
            Lex.append(tuple(wrds))
        elif (wrds[-3]=='pragma'):
            Str = string.join(line[1:-4],' ')
            Lex.append(tuple([Str]+wrds[-3:]))
        elif (line[0]=='"'):
            Ind = string.index(line[1:],'"')
            Str = line[:Ind+2]
            wrds = string.split(line[Ind+2:])
            Lex.append(tuple([Str]+wrds))
        elif (len(wrds)>4):
            wrds2 = wrds[-3:]
            wrds1 = wrds[:-3]
            wrd0=string.join(wrds1,' ')
            Lex.append(tuple([wrd0]+wrds2))

def run_machine():
    state='0'
    Steps =0
    while (state!=0):
        Steps += 1
        if (Steps % 100000)==0: logs.log_info('%dK steps'%(Steps/1000))
        if (Verbose):
            logs.log_info('stepit state=%s tok=%s stack=%s\n\n\n\n'%(state,Lex[0],Stack))
        nextstate = step_machine(state)
        state=nextstate
    logs.log_info('exit state %s %s'%(state,len(Lex)))

def uniq(What):
    if (What not in Uniques):
        Uniques[What]=1
    X = Uniques[What]
    Uniques[What] += 1
    return X



def step_machine(state):
    List = States[state]
    (Tok,Kind,Lnum,Pos)=Lex[0]
    if Verbose: logs.log_info('yacc %s %s %s %s %s'%(Tok,Kind,Lnum,Pos,state))
#    logs.log_info('    LIST = %s'%str(List))
    for (Act,Param,Next) in List:
        if Verbose:
            logs.log_info('try tok=%s %s act=%s param=%s next=%s match=%s'%(Tok,Kind,Act,Param,Next,matches_ok(Tok,Kind,Act,Param)))
        if (Act=='shift'):
            if (matches_ok(Tok,Kind,Act,Param)):
                Stack.append((Tok,Kind,Lnum,Pos,state))
                Lex.pop(0)
                return Next
        elif Act=='reduce':
#            print matches_ok(Tok,Kind,Act,Param),Tok,Kind,Act,Param
            if compatibleGoto(Param,Kind) or (Param=='$default') or matches_ok(Tok,Kind,Act,Param):
                Rule=Next
                Name,Wrds = Rules[Rule]
                Wrds=Wrds[:]
#                print 'reduce action rule=%s name=%s wrds=%s'%(Rule,Name,Wrds)
                Id = uniq(Name)
    #            Fout.write('reduce %s %d %s\n'%(Name,Id,Stack[-len(Wrds):]))
                if len(Wrds)==0:
                    addToDb(Name,Id,[])
                else:
                    addToDb(Name,Id,Stack[-len(Wrds):])
                NST=state
                while Wrds!=[]:
    #                print 'work reduce wrds=%s stack=%s %s %s %s %s %s'%(Wrds,Stack,Lnum,Pos,Rule,Name,Wrds)
                    TT,KK,Lnum1,Pos1,NST = Stack.pop(-1)
                    Wrds.pop(0)
                Lex.insert(0,(Name,Name,Id,-1))
                return NST
        elif Act=='goto':
#            print 'goto param=%s kind=%s %s'%(Param,Kind,Next)
            if compatibleGoto(Param,Kind):
                Lex.pop(0)
                Stack.append((Tok,Kind,Lnum,Pos,state))
                return Next
        elif Act=='accept':
            return 0
        else:
            logs.log_error('shouldnt be here %s'%Act)
    logs.log_error('yaccer: no valid operation act=%s tok=%s kind=%s lnum=%s pos=%s state=%s fname=%s'%(Act,Tok,Kind,Lnum,Pos,state,origFname))
    return False

def compatibleGoto(Param,Kind):
    if Param==Kind: return True
    if (Kind=='END')and(Param=='END_ERR'): return True
    if (Kind=='END')and(Param=='END_'): return True
    if (Kind=='BEGIN')and(Param=='BEGIN_'): return True
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


def reportDb(RunDir):
    for Key in DataBase:
        Fout.write('%s %s\n'%(Key,DataBase[Key]))
    Outf = open('%s/db0.pickle'%RunDir,'w')
    pickle.dump(DataBase,Outf)
    Outf.close()



def matches_ok(Tok,Kind,Act,Param):
#    print 'matches_ok',(Tok==Param)or(Kind==Param),Tok,Kind,Act,Param
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



