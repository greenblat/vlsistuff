#! /usr/bin/python3

import string,sys,os
import lexer_tables as lex

def main():
    Fname = sys.argv[1]
    if len(sys.argv)>2: Foutname = sys.argv[2]
    else:
        Foutname = 'lex.out'
    run(Fname,Foutname)


def run(Fname,Foutname):
    try:
        File = open(Fname)
    except:
        print('failed to open %s'%Fname)
        return
    Ofile = open(Foutname,'w')
    work(File,Ofile)
    work_out_queue(Queue,True,Ofile)
    Ofile.close()

def work(File,Ofile):
    LineNum=0
    while 1:
        line=File.readline()
        if len(line)==0:
            return
        LineNum+=1
        if len(line)>1:
            if ord(line[-1])!=10:
                line = line+ chr(10)
            work_line(line,LineNum,Ofile)

state='idle'
Token=''
def work_line(line,LineNum,Ofile):
    global state,Token
    Len=len(line)
    for i in range(Len-1):
        state,action,kind=stepit(i,line[i],line[i+1],state)
        if (action=='skipline'):
            state='idle'
            return
        if (action=='push'):
            Token=Token+line[i]
            push_token(Token,kind,LineNum,i,Ofile)
            Token=''
        elif (action=='add'):
            Token=Token+line[i]
        elif (action=='clear'):
            Token=''
        elif (action!='none'):
            print(state,action,kind,'error line=%d pos=%d chr="%s" %s'%(LineNum,i,line[i],line[:-1]))
            sys.exit()
Queue=[]
def push_token(Token,kind,LineNum,LinePos,Ofile):
    if (kind=='token')and(Token in lex.ReservedWords):
        kind=Token
    elif (kind=='define')and(Token in lex.ReservedWords):
        kind='backtick_'+Token[1:]
    Queue.append((Token,kind,LineNum,LinePos))
    work_out_queue(Queue,False,Ofile)

def work_out_queue(Queue,Flush,Ofile):
    if (Flush):
        if Queue==[]:
            return
        Tup = Queue.pop(0)
        Tup = rework_tup(Tup)
        Ofile.write('%s %s %s %s\n'%Tup)
        work_out_queue(Queue,Flush,Ofile)
    if (len(Queue)>=2)and(Queue[0][1]=='number')and(Queue[1][1] in ['uhex','ubin','udig']):
        Item = [Queue[0][0]+Queue[1][0],Queue[1][1][1:],Queue[0][2],Queue[0][3]]
        Queue[0]=tuple(Item)
        Queue.pop(1)

    if (len(Queue)>3):
        Tup = rework_tup(Queue.pop(0))
        Ofile.write('%s %s %s %s\n'%Tup)
        return
            

def rework_tup(Tup):
    List = list(Tup)
    List[-1] += 1
    if Tup[1]=='single':
        List[1]=List[0]
        return tuple(List)
        
    if Tup[1]=='double':
        if (len(List[0])==1):
            List[1]=List[0]
            return tuple(List)
        List[1]=lex.DoubleNames[List[0]]
        return tuple(List)
    return Tup

def stepit(Pos,Char,Char1,State):
    rule=0
    for (St,Ch0,Ch1,Next,Action,Kind) in lex.Table:
        if (St==State):
            rule +=1 
            if (Ch0=='')or(Char in Ch0):
                if (Ch1=='')or(Char1 in Ch1):
                    return  Next,Action,Kind
    print('no rule fits st=%s ch=%s ch1=%s'%(State,Char,Char1))
    return 'idle','error',0
    
if __name__ == '__main__': main()
