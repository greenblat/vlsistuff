#! /usr/bin/python3

import os,sys

Specific = sys.argv[1]
Str = 'import %s as tables'%Specific
exec(Str)

#('define', 'qwertyuiopas0123456789_', 'qwertyuiopTM0123456789_', 'define', 'add', 0)
def main():
    Fout = open('tables.c','w')
    Fout.write(String0)
    States=[]
    Chars0=[]
    CharSets={}
    for Tuple in tables.Table:
        St = Tuple[0]
        if St not in States:
            States.append(St)
        Char0=Tuple[1]
        if Char0 not in Chars0:
            Chars0.append(Char0)
        Char1=Tuple[2]
        if Char1 not in Chars0:
            Chars0.append(Char1)

    Fout.write('int EOL_FLAG() { return %d;}\n'%(tables.EOL!=[]))

    States.sort()
    for ind,State in enumerate(States,1):
        Fout.write('#define st_%s %d\n'%(State,ind))

    for ind,Char0 in  enumerate(Chars0):
        Char1 = Char0.replace("\\","\\\\")
        Char1 = Char1.replace('"','\\"')
        res=''
        for Chr in Char1:
            if Chr=='\t':
                res = res + '\\t'
            elif Chr=='\n':
                res = res + '\\n'
            else:
                res += Chr
        Fout.write('char strx%d[]="%s";\n'%(ind,res))
        CharSets[Char0]='strx%d'%ind

    Fout.write('int State=st_idle;\n')
    Fout.write('void stepit(char Char,char Next) {\n')
    Fout.write('//    printf("state=%d char=|%c| next=|%c|\\n",State,Char,Next);\n')
    Fout.write('    switch (State) {\n')
    for State in States:
        Fout.write('    case st_%s: {\n'%State)
        for Tuple in tables.Table:
            if Tuple[0]==State:
                Chars0 = CharSets[Tuple[1]]
                Chars1 = CharSets[Tuple[2]]
                Fout.write('        if (in_string(Char,%s)&&in_string(Next,%s)) {\n'%(Chars0,Chars1))
                Fout.write('              action("%s","%s",Char);\n'%(Tuple[4],Tuple[5]))
                Fout.write('              State=st_%s;\n'%(Tuple[3]))
                Fout.write('              return;\n')
                Fout.write('        }\n')
        Fout.write('    } break;\n')
    Fout.write('    }\n')
    Fout.write('    printf("no action!!!! |%x| <%c> |%x| <%c> state=%d \\n",Char,Char,Next,Next,State);\n')
    Fout.write('}\n')
    treat_reserveds(Fout)
    treat_doubles(Fout)
    treat_joines(Fout)
        
    Fout.close()

def  treat_joines(Fout):
    Fout.write('int joinable(char *typeA, char *typeB){\n')
    for (A,B) in tables.Joines:
        Fout.write('    if ((strcmp("%s",typeA)==0)&&(strcmp("%s",typeB)==0)) return 1;\n'%(A,B))
    Fout.write('     return 0;\n')
    Fout.write('}\n')



def  treat_reserveds(Fout):
    Reserved = tables.ReservedWordsStr.split()
    Reserved.sort()
    Fout.write('void reserved_words(char *Token,char *tokenType){\n')
    for Word in Reserved:
        Fout.write('    if (strcmp(Token,"%s")==0) {strcpy(tokenType,"%s"); return; }\n'%(Word,Word))

    for (Word,Type) in tables.Modifiers:
        Fout.write('    if (strcmp(Token,"%s")==0) {strcpy(tokenType,"%s"); return; }\n'%(Word,Type))


    Fout.write('}\n')

def treat_doubles(Fout):
    Doubles = tables.DoubleNames
    Keys = list(Doubles.keys())
    Keys.sort()
    Fout.write('void doubleNames(char *Token,char *tokenType){\n')
    for Key in Keys:
        Rename = Doubles[Key]
        Fout.write('    if (strcmp(Token,"%s")==0) {strcpy(tokenType,"%s"); return; }\n'%(Key,Rename))
    Fout.write('}\n')


String0 = '''
#include "stdio.h"
#include "string.h"
int in_string(char Chk, char *Again);
void action(char *act,char *tokentype,char Char) ;
'''


main()
    

