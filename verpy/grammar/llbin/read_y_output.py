#! /usr/bin/env python3

import os,sys
import pickle

class Db_class:
    def __init__(self):
        self.state='idle'
db = Db_class()
Rules={}
States = {}
Reduces = {}

def main():
    YaccFname = sys.argv[1]
    os.system('yacc -dv %s '%YaccFname)
#    os.system('yacc -dv %s -Wcounterexamples'%YaccFname)
    File = open('y.output')
    work1(File)
    work2()
#    Outf = open('yacc.pickle','w')
#    pickle.dump(Rules,Outf)
#    pickle.dump(States,Outf)
#    Outf.close()
    report()
    mysave()
def mysave():
    Outf = open('mysave.py','w')
    Outf.write('Rules = %s\n'%Rules)
    Outf.write('States = %s\n'%States)
    Outf.close()

def work2():
    for State in States:
        List = States[State]
        rework_list(State,List)

def rework_list(State,List):
    if len(List)<2:
        return

    ind = -1
    for i in range(len(List)):
        A,B,C = List[i]
        if (A=='reduce')and(B=='$default'):
            if ind<0:
                ind=i
            else:
                print('ilia rework list got %s'%List)
    if ind>=0:
        X = List.pop(ind)
        List.append(X)



def report():
    Fout = open('my.listing','w')
    for X in Rules:
        Fout.write('rule %s %s\n'%(X,Rules[X]))
    for X in States:
        Fout.write('state %s %s\n'%(X,States[X]))
    Fout.close()

def work1(File):
    while 1:
        line=File.readline()
        if len(line)==0:
            return
        wrds = line.split()
        if len(wrds)>0:
            use_line(wrds)


def use_line(wrds):
    if (db.state=='idle'):
        if wrds[0]=='Grammar':
            db.state='rules'
        elif (len(wrds) == 2) and (wrds[0] in ['state','State']):
            db.state='state'
            db.inState=wrds[1]
            States[wrds[1]]=[]
    elif (db.state=='rules'):
        if (len(wrds) == 2) and (wrds[0] in ['state','State']):
            db.state='state'
            db.inState=wrds[1]
            States[wrds[1]]=[]
        elif (wrds[0]=='Terminals,'):
            db.state='idle'
        elif is_num(wrds[0]):
            if wrds[1][-1]==':':
                db.Rule=wrds[1][:-1]
                X = wrds[2:]
                if (len(X)==3)and(X[1]=='empty'):
                    Rules[wrds[0]]=(db.Rule,[])
                else:
                    Rules[wrds[0]]=(db.Rule,wrds[2:])
            elif wrds[1]=='|':
                X = wrds[2:]
                if (len(X)==3)and(X[1]=='empty'):
                    Rules[wrds[0]]=(db.Rule,[])
                else:
                    Rules[wrds[0]]=(db.Rule,wrds[2:])


    elif (db.state=='state'):
        if wrds==[]:
            pass
        elif (len(wrds) == 2) and (wrds[0] in ['state','State']):
            db.state='state'
            db.inState=wrds[1]
            States[wrds[1]]=[]
        elif is_num(wrds[0]):
            db.rule=wrds[:]
        elif len(wrds)<2:
            pass
        elif wrds[1]=='shift,':
            Tok = clean_token(wrds[0])
            State = wrds[-1]
            States[db.inState].append(('shift',Tok,State))
        elif wrds[1]=='reduce':
            Rstate= ('reduce',wrds[0],wrds[4])
            States[db.inState].append(Rstate)
        elif wrds[1]=='accept':
            States[db.inState].append(('accept','$default',0))
        elif (wrds[1]=='go')and(wrds[2]=='to')and(wrds[3]=='state'):
            Rstate= ('goto',wrds[0],wrds[4])
            States[db.inState].append(Rstate)

def use_reduces():
    for State,Goto in Reduces:
        List = States[State]
        i = 0
        for i in range(len(List)):
            X = List[i]
            if (X[0]=='reduce')and(X[-1]==Goto):
                Y = list(X)
                Y[-1]=Reduces[(State,Goto)]
                print('replace reduce st=%s goto=%s'%(State,Goto))
                List[i]=tuple(Y)
        States[State]=List

def clean_token(Tok):
    if Tok[0]=='(':
        Tok=Tok[1:]
    if Tok[-1]==')':
        Tok=Tok[:-1]
    if Tok[0]=="'":
        Tok=Tok[1:]
    if Tok[-1]=="'":
        Tok=Tok[:-1]
    return Tok

def is_num(Txt):
    try:
        X = int(Txt)
        return True
    except:
        return False


main()

