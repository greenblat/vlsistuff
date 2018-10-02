#! /usr/bin/python

import string,sys,os,types
import cProfile
import traceback

Specific = sys.argv[1]
Str = 'import %s as specific_tables'%Specific
exec(Str)

def main():
    Fname = sys.argv[2]
    run_lexer(Fname,'lex.out')

class DbClass:
    def __init__(self):
        self.state='idle'
        self.Token=''
        self.Queue=[]
        self.Types=string.split(specific_tables.Types)


def run_lexer(Fname,Ofname):
    global Db
    Db=DbClass()
    try:
        File = open(Fname)
    except:
        print 'lexer failed to open %s'%Fname
        print traceback.print_stack()
        return
    Db.Ofile = open(Ofname,'w')
    checkTable()
    work(File)
    work_out_queue(True)
    Db.Ofile.close()

def checkTable():
    for X in specific_tables.Table:
        if len(X)!=6:
            print 'ERROR! ilia in table "%s"'%(str(X))

def work(File):
    LineNum=0
    while 1:
        line=File.readline()
        if len(line)==0:
            return
        LineNum+=1
        if len(line)>1:
            if ord(line[-2])==13:
                line=line[:-2]+' '+chr(10)
            elif ord(line[-1])!=10:
                line = line+ ' '+chr(10)
            else:
                line = line[:-1]+' '+chr(10)
#            print 'line',line,
            work_line(line,LineNum)

def work_line(line,LineNum):
    Len=len(line)
    for i in range(Len-1):
        Db.state,action,kind=stepit(i,line[i],line[i+1],Db.state)
#        print '>>>aft>>> |%s| |%s| state=%s'%(line[i],line[i+1],Db.state)
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
            print Db.state,action,kind,'error line=%d pos=%d chr="%s" %s'%(LineNum,i,line[i],line[:-1])
            sys.exit()
    if specific_tables.EOL!=[]:
        push_token('eol','eol',LineNum,i)

def push_token(Token,kind,LineNum,LinePos):
#    print 'push_token    %s %s %s %s\n'%(Token,kind,LineNum,LinePos)
    if (kind=='token')and(string.lower(Token) in ReservedWords):
#        kind=string.capitalize(Token)
#        Token=string.capitalize(Token)
         kind=Token
    elif (kind=='define')and(Token in ReservedWords):
        kind='backtick_'+Token[1:]
    elif (kind=='token')and('.' in Token):
        kind = 'dotted'

    if string.lower(Token) in Db.Types:
        kind = 'Types'
    if len(Db.Queue)>0:
        PrevT,PrevK,_,_ = Db.Queue[-1]
        if (PrevT=='Type'):
            Db.Types.append(string.lower(Token))

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
        
    if Tup[1]=='ddouble':
        List = list(Tup)
        if (len(List[0])==1):
            List[1]=List[0]
            return tuple(List)
        List[1]=doublesName(List[0])
        return tuple(List)
    return Tup

def doublesName(Txt):
    if Txt in specific_tables.DoubleNames:
        return specific_tables.DoubleNames[Txt]
    else:
        print 'ilia! doubles names missing "%s"'%Txt
        return Txt


def stepit(Pos,Char,Char1,State):
    rule=0
    for (St,Ch0,Ch1,Next,Action,Kind) in specific_tables.Table:
        if (St==State):
#            print 'tryrule%d ch=%s ch1=%s in0=%d in1=%d st=%s ch0=%s ch1=%s next=%s act=%s kind=%s'%(rule,Char,Char1,(Char in Ch0),(Char1 in Ch1),State,Ch0,Ch1,Next,Action,Kind)
            rule +=1
            if (Ch0=='')or(Char in Ch0):
                if (Ch1=='')or(Char1 in Ch1):   # or(ord(Char1) in specific_tables.EOLS):
                    return  Next,Action,Kind
    print 'lexer: no rule fits st=|%s| ch=|%s| ch1=|%s|'%(State,Char,Char1)
#    sys.exit()
    return 'idle','error',0
    


ReservedWords = string.split(string.lower(specific_tables.ReservedWordsStr))




if __name__ == '__main__':
    main()
