#include <string.h>
#include "stdio.h"
#include <stdlib.h>



FILE *Infile;
FILE *Outfile;

int EOL_FLAG();
char Token[10000];
int  tokenPtr=0;
int lineNum=0;
int charNum=0;
int skipLine=0;
void stepit(char A,char B,int Lnum);
void read_in_file();
void reserved_words(char *Token,char *tokenType);
void doubleNames(char *Token,char *newType);
int joinable(char *Type0,char *Type1);
int in_string(char Chk, char *Again) { 
    int i;
    if (Again[0]==0) return 1;
    for (i=0;Again[i];i+=1) if (Again[i]==Chk) return 1;
    return 0;
}

char pToken[10000];
int  pLineNum,pCharNum;
char pType[1000];
int pValid=0;
int dumpedTokens=0;

void push_token(char *Token,int lineNum,int charNum, char *tokenType) {
    char newType[1000];
    strcpy(newType,tokenType);
    if (strcmp(tokenType,"token")==0) {
        reserved_words(Token,newType);
    } else if (strcmp(tokenType,"double")==0) {
        if (strlen(Token)==1) { 
            strcpy(newType,Token);

        } else {
            doubleNames(Token,newType);
        }
    } else if (strcmp(tokenType,"single")==0) {
        strcpy(newType,Token);
    }    
    if (pValid && joinable(pType,newType)) {
        strcat(pToken,Token);
        fprintf(Outfile,"%s %s %d %d\n",pToken,newType,pLineNum,pCharNum);
		dumpedTokens++;
        pValid=0;
    } else if (pValid) {
        fprintf(Outfile,"%s %s %d %d\n",pToken,pType,pLineNum,pCharNum);
		dumpedTokens++;
        pLineNum=lineNum;
        pCharNum=charNum;
        strcpy(pToken,Token);
        strcpy(pType,newType);
        pValid=1;
    } else {
        pLineNum=lineNum;
        pCharNum=charNum;
        strcpy(pToken,Token);
        strcpy(pType,newType);
        pValid=1;
    }

//    fprintf(Outfile,"%s %s %d %d\n",Token,newType,lineNum,charNum);
}

void print_help() {
    printf("-no_eol = dont insert eol tokens.\n");
    return;
}


void action(char *act,char *tokenType,char Char) {
//    printf(">>>> %s %s |%c|\n",act,tokenType,Char);
    if (act[0]=='a') {
        Token[tokenPtr]=Char;
        tokenPtr++;
        Token[tokenPtr]=0;
        return;
    }
    if (act[0]=='c') {
        Token[0]=0;
        tokenPtr=0;
        return;
    }

    if (act[0]=='p') {
        Token[tokenPtr]=Char;
        tokenPtr++;
        Token[tokenPtr]=0;
        push_token(Token,lineNum,charNum,tokenType);
        Token[0]=0;
        tokenPtr=0;
        return;
    }
    if (act[0]=='s') {
        skipLine=1;
        return;
    }
    if (act[0]=='n') {
        return;
    }
    printf("action %s %s %c\n",act,tokenType,Char);
}

int noEol = 0;

char inFileName[300];
char outFileName[300];
int main(argc, argv)
    int             argc;
    char           *argv[];
{
    char option[300];
    int k,pos=0;
    if (argc==1) { print_help(); return 0; }
    inFileName[0]=0;
    strcpy(outFileName,"lex.out");
    for (k = 2; k <= argc; k++) {
        strcpy(option, *++argv);
        if (option[0]!='-') {
            if (pos==0) {
                strcpy(inFileName,option);
                pos=1;
            } else if (pos==1) {
                strcpy(outFileName,option);
                pos=2;
            } else {
                printf("too many filenames!\n");
                print_help();
                return 0;
            }
        } else {
            if (strcmp(option,"-a")==0) {
                strcpy(option, *++argv);
                k++;
            } else if (strcmp(option,"-no_eol")==0) {
                noEol=1;
            } else if (strcmp(option,"-h")==0) {
                print_help();
                return 0;
            } else {
                print_help();
                return 0;
            }
        }
    }
    Infile = fopen(inFileName,"r");
    if (!Infile) {
        printf("cannot open file \"%s\" \n",inFileName);
        return 2;
    }
    Outfile = fopen(outFileName,"w");
    read_in_file();
    fclose(Outfile);
    return 0;
}

void read_in_file() {
    char *x;
    char line[10000];
    char tmpline[10000];
    int i,nop;
    while (1) {
        x = fgets(line,10000,Infile);
        lineNum += 1;
        if (strlen(line)>7) {
            if ((line[0] == '_') && (line[1] == '_') && (line[2] == 'L')
                && (line[3] == 'N') && (line[4] == 'U') 
                && (line[5] == 'M'))
            {
                lineNum = 1+atoi( &(line[6]));
                int xx = 7;
                while (line[xx] != ' ') xx++;
                strcpy(tmpline, &(line[xx]));
                strcpy(line,tmpline);
            }
        }
//        printf("%d: line=%s",lineNum,line);
        if ((lineNum % 50000)==0) {
            printf(" %d lines\n",lineNum);
        }
        charNum=0;
        if (!x) { 
            push_token(" ",lineNum,charNum,"none");
            printf(" %d lines and %d tokens\n",lineNum,dumpedTokens);
            fclose(Infile);
            return; }
        for (i=0;(!skipLine && (line[i+1]!=0));i++) {
            charNum += 1;
            if (line[i]<0)    line[i]=' ';
            if (line[i+1]<0)    line[i+1]=' ';
            if (line[i]==0xd) line[i]=' ';
            if (line[i]==0xa) line[i]=' ';
            if (line[i+1]==0xd) line[i+1]=' ';
            if (line[i+1]==0xa) line[i+1]=' ';
//            printf("iii lnum=%d chr=%d  line[i]=0x%x 0x%x    '%c' '%c' \n",lineNum,charNum,line[i],line[i+1],line[i],line[i+1]);
            if ((line[i]==0x5c)&&(line[i+1]==0xa)) {
                nop=0;
            } else if ((i>0)&&(line[i-1]==0x5c)&&(line[i]==0xa)) {
                nop=0;
            } else if ((i>0)&&(line[i+1]==0x5c)) {
                stepit(line[i],line[i+3],lineNum);
            } else 
                stepit(line[i],line[i+1],lineNum);
        }    
        skipLine=0;
        if ((!noEol) && EOL_FLAG()) {
            push_token("eol",lineNum,charNum,"eol");
        }
    }
}




