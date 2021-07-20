
#include "stdio.h"
#include "string.h"
int in_string(char Chk, char *Again);
void action(char *act,char *tokentype,char Char) ;
int EOL_FLAG() { return 1;}
#define st_bin1 1
#define st_bin2 2
#define st_comment 3
#define st_comment2 4
#define st_define 5
#define st_dig1 6
#define st_dig2 7
#define st_double 8
#define st_either 9
#define st_either1 10
#define st_eqeq2 11
#define st_eqeq3 12
#define st_floating 13
#define st_floating0 14
#define st_hex1 15
#define st_hex2 16
#define st_idle 17
#define st_neq2 18
#define st_neq3 19
#define st_new 20
#define st_number 21
#define st_power 22
#define st_pragma1 23
#define st_pragma2 24
#define st_sizednumber 25
#define st_string 26
#define st_token 27
#define st_ubin1 28
#define st_ubin2 29
#define st_udig1 30
#define st_udig2 31
#define st_uhex1 32
#define st_uhex2 33
char strx0[]="\t \\";
char strx1[]="";
char strx2[]="/";
char strx3[]="*";
char strx4[]="`";
char strx5[]="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM";
char strx6[]="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789_";
char strx7[]="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM$_";
char strx8[]="0123456789";
char strx9[]=".";
char strx10[]="e";
char strx11[]="'";
char strx12[]="b";
char strx13[]="h";
char strx14[]="d";
char strx15[]="-";
char strx16[]="+";
char strx17[]="01_xzXZ?";
char strx18[]="0123456789abcdefABCDEF_xX";
char strx19[]="(";
char strx20[]=")";
char strx21[]=":";
char strx22[]="=";
char strx23[]="!";
char strx24[]="-=!<>&|";
char strx25[]="=<>&|";
char strx26[]="\"";
char strx27[]="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789\t \\_?.,[]{}#@()~%^;:/+-*-=!<>&|',\\";
char strx28[]="?.,[]{}#@()~%^;:/+-*";
char strx29[]="\\";
int State=st_idle;
void stepit(char Char,char Next) {
//    printf("state=%d char=|%c| next=|%c|\n",State,Char,Next);
    switch (State) {
    case st_bin1: {
        if (in_string(Char,strx12)&&in_string(Next,strx17)) {
              action("add","0",Char);
              State=st_bin2;
              return;
        }
    } break;
    case st_bin2: {
        if (in_string(Char,strx17)&&in_string(Next,strx17)) {
              action("add","0",Char);
              State=st_bin2;
              return;
        }
        if (in_string(Char,strx17)&&in_string(Next,strx1)) {
              action("push","bin",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_comment: {
        if (in_string(Char,strx3)&&in_string(Next,strx2)) {
              action("none","0",Char);
              State=st_comment2;
              return;
        }
        if (in_string(Char,strx1)&&in_string(Next,strx1)) {
              action("none","0",Char);
              State=st_comment;
              return;
        }
    } break;
    case st_comment2: {
        if (in_string(Char,strx2)&&in_string(Next,strx1)) {
              action("none","0",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_define: {
        if (in_string(Char,strx6)&&in_string(Next,strx6)) {
              action("add","0",Char);
              State=st_define;
              return;
        }
        if (in_string(Char,strx6)&&in_string(Next,strx1)) {
              action("push","define",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_dig1: {
        if (in_string(Char,strx14)&&in_string(Next,strx8)) {
              action("add","0",Char);
              State=st_dig2;
              return;
        }
    } break;
    case st_dig2: {
        if (in_string(Char,strx8)&&in_string(Next,strx8)) {
              action("add","0",Char);
              State=st_dig2;
              return;
        }
        if (in_string(Char,strx8)&&in_string(Next,strx1)) {
              action("push","dig",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_double: {
        if (in_string(Char,strx24)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_either: {
        if (in_string(Char,strx3)&&in_string(Next,strx20)) {
              action("add","0",Char);
              State=st_either1;
              return;
        }
        if (in_string(Char,strx3)&&in_string(Next,strx1)) {
              action("add","0",Char);
              State=st_pragma1;
              return;
        }
    } break;
    case st_either1: {
        if (in_string(Char,strx20)&&in_string(Next,strx1)) {
              action("push","star",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_eqeq2: {
        if (in_string(Char,strx22)&&in_string(Next,strx22)) {
              action("add","0",Char);
              State=st_eqeq3;
              return;
        }
        if (in_string(Char,strx22)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_eqeq3: {
        if (in_string(Char,strx22)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_floating: {
        if (in_string(Char,strx8)&&in_string(Next,strx8)) {
              action("add","0",Char);
              State=st_floating;
              return;
        }
        if (in_string(Char,strx8)&&in_string(Next,strx10)) {
              action("add","0",Char);
              State=st_floating;
              return;
        }
        if (in_string(Char,strx10)&&in_string(Next,strx8)) {
              action("add","0",Char);
              State=st_floating;
              return;
        }
        if (in_string(Char,strx10)&&in_string(Next,strx15)) {
              action("add","0",Char);
              State=st_floating;
              return;
        }
        if (in_string(Char,strx10)&&in_string(Next,strx16)) {
              action("add","0",Char);
              State=st_floating;
              return;
        }
        if (in_string(Char,strx16)&&in_string(Next,strx8)) {
              action("add","0",Char);
              State=st_floating;
              return;
        }
        if (in_string(Char,strx15)&&in_string(Next,strx8)) {
              action("add","0",Char);
              State=st_floating;
              return;
        }
        if (in_string(Char,strx8)&&in_string(Next,strx1)) {
              action("push","floating",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_floating0: {
        if (in_string(Char,strx9)&&in_string(Next,strx8)) {
              action("add","0",Char);
              State=st_floating;
              return;
        }
    } break;
    case st_hex1: {
        if (in_string(Char,strx13)&&in_string(Next,strx18)) {
              action("add","0",Char);
              State=st_hex2;
              return;
        }
    } break;
    case st_hex2: {
        if (in_string(Char,strx18)&&in_string(Next,strx18)) {
              action("add","0",Char);
              State=st_hex2;
              return;
        }
        if (in_string(Char,strx18)&&in_string(Next,strx1)) {
              action("push","hex",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_idle: {
        if (in_string(Char,strx0)&&in_string(Next,strx1)) {
              action("none","0",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx2)&&in_string(Next,strx2)) {
              action("skipline","0",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx2)&&in_string(Next,strx3)) {
              action("none","0",Char);
              State=st_comment;
              return;
        }
        if (in_string(Char,strx4)&&in_string(Next,strx5)) {
              action("add","0",Char);
              State=st_define;
              return;
        }
        if (in_string(Char,strx7)&&in_string(Next,strx6)) {
              action("add","0",Char);
              State=st_token;
              return;
        }
        if (in_string(Char,strx5)&&in_string(Next,strx1)) {
              action("push","token",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx8)&&in_string(Next,strx8)) {
              action("add","0",Char);
              State=st_number;
              return;
        }
        if (in_string(Char,strx8)&&in_string(Next,strx9)) {
              action("add","0",Char);
              State=st_floating0;
              return;
        }
        if (in_string(Char,strx8)&&in_string(Next,strx10)) {
              action("add","0",Char);
              State=st_floating;
              return;
        }
        if (in_string(Char,strx8)&&in_string(Next,strx1)) {
              action("push","number",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx11)&&in_string(Next,strx12)) {
              action("add","0",Char);
              State=st_ubin1;
              return;
        }
        if (in_string(Char,strx11)&&in_string(Next,strx13)) {
              action("add","0",Char);
              State=st_uhex1;
              return;
        }
        if (in_string(Char,strx11)&&in_string(Next,strx14)) {
              action("add","0",Char);
              State=st_udig1;
              return;
        }
        if (in_string(Char,strx19)&&in_string(Next,strx3)) {
              action("add","0",Char);
              State=st_either;
              return;
        }
        if (in_string(Char,strx15)&&in_string(Next,strx21)) {
              action("add","0",Char);
              State=st_new;
              return;
        }
        if (in_string(Char,strx16)&&in_string(Next,strx21)) {
              action("add","0",Char);
              State=st_new;
              return;
        }
        if (in_string(Char,strx22)&&in_string(Next,strx22)) {
              action("add","0",Char);
              State=st_eqeq2;
              return;
        }
        if (in_string(Char,strx23)&&in_string(Next,strx22)) {
              action("add","0",Char);
              State=st_neq2;
              return;
        }
        if (in_string(Char,strx3)&&in_string(Next,strx3)) {
              action("add","0",Char);
              State=st_power;
              return;
        }
        if (in_string(Char,strx24)&&in_string(Next,strx25)) {
              action("add","0",Char);
              State=st_double;
              return;
        }
        if (in_string(Char,strx24)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx26)&&in_string(Next,strx1)) {
              action("add","0",Char);
              State=st_string;
              return;
        }
        if (in_string(Char,strx28)&&in_string(Next,strx1)) {
              action("push","single",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx29)&&in_string(Next,strx1)) {
              action("add","idle",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_neq2: {
        if (in_string(Char,strx22)&&in_string(Next,strx22)) {
              action("add","0",Char);
              State=st_neq3;
              return;
        }
        if (in_string(Char,strx22)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_neq3: {
        if (in_string(Char,strx22)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_new: {
        if (in_string(Char,strx21)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_number: {
        if (in_string(Char,strx8)&&in_string(Next,strx8)) {
              action("add","0",Char);
              State=st_number;
              return;
        }
        if (in_string(Char,strx8)&&in_string(Next,strx11)) {
              action("add","0",Char);
              State=st_sizednumber;
              return;
        }
        if (in_string(Char,strx8)&&in_string(Next,strx9)) {
              action("add","0",Char);
              State=st_floating0;
              return;
        }
        if (in_string(Char,strx8)&&in_string(Next,strx1)) {
              action("push","number",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_power: {
        if (in_string(Char,strx3)&&in_string(Next,strx1)) {
              action("push","power",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_pragma1: {
        if (in_string(Char,strx3)&&in_string(Next,strx20)) {
              action("add","0",Char);
              State=st_pragma2;
              return;
        }
    } break;
    case st_pragma2: {
        if (in_string(Char,strx20)&&in_string(Next,strx1)) {
              action("push","pragma",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_sizednumber: {
        if (in_string(Char,strx11)&&in_string(Next,strx12)) {
              action("add","0",Char);
              State=st_bin1;
              return;
        }
        if (in_string(Char,strx11)&&in_string(Next,strx13)) {
              action("add","0",Char);
              State=st_hex1;
              return;
        }
        if (in_string(Char,strx11)&&in_string(Next,strx14)) {
              action("add","0",Char);
              State=st_dig1;
              return;
        }
    } break;
    case st_string: {
        if (in_string(Char,strx26)&&in_string(Next,strx1)) {
              action("push","string",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx27)&&in_string(Next,strx1)) {
              action("add","0",Char);
              State=st_string;
              return;
        }
    } break;
    case st_token: {
        if (in_string(Char,strx6)&&in_string(Next,strx6)) {
              action("add","0",Char);
              State=st_token;
              return;
        }
        if (in_string(Char,strx6)&&in_string(Next,strx1)) {
              action("push","token",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_ubin1: {
        if (in_string(Char,strx12)&&in_string(Next,strx17)) {
              action("add","0",Char);
              State=st_ubin2;
              return;
        }
    } break;
    case st_ubin2: {
        if (in_string(Char,strx17)&&in_string(Next,strx17)) {
              action("add","0",Char);
              State=st_ubin2;
              return;
        }
        if (in_string(Char,strx17)&&in_string(Next,strx1)) {
              action("push","ubin",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_udig1: {
        if (in_string(Char,strx14)&&in_string(Next,strx8)) {
              action("add","0",Char);
              State=st_udig2;
              return;
        }
    } break;
    case st_udig2: {
        if (in_string(Char,strx8)&&in_string(Next,strx8)) {
              action("add","0",Char);
              State=st_udig2;
              return;
        }
        if (in_string(Char,strx8)&&in_string(Next,strx1)) {
              action("push","udig",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_uhex1: {
        if (in_string(Char,strx13)&&in_string(Next,strx18)) {
              action("add","0",Char);
              State=st_uhex2;
              return;
        }
    } break;
    case st_uhex2: {
        if (in_string(Char,strx18)&&in_string(Next,strx18)) {
              action("add","0",Char);
              State=st_uhex2;
              return;
        }
        if (in_string(Char,strx18)&&in_string(Next,strx1)) {
              action("push","uhex",Char);
              State=st_idle;
              return;
        }
    } break;
    }
    printf("no action!!!! |%x| <%c> |%x| <%c> state=%d \n",Char,Char,Next,Next,State);
}
void reserved_words(char *Token,char *tokenType){
    if (strcmp(Token,"cell")==0) {strcpy(tokenType,"cell"); return; }
    if (strcmp(Token,"ff")==0) {strcpy(tokenType,"ff"); return; }
    if (strcmp(Token,"latch")==0) {strcpy(tokenType,"latch"); return; }
    if (strcmp(Token,"library")==0) {strcpy(tokenType,"library"); return; }
    if (strcmp(Token,"pin")==0) {strcpy(tokenType,"pin"); return; }
    if (strcmp(Token,"statetable")==0) {strcpy(tokenType,"statetable"); return; }
    if (strcmp(Token,"test_cell")==0) {strcpy(tokenType,"test_cell"); return; }
    if (strcmp(Token,"timing")==0) {strcpy(tokenType,"timing"); return; }
    if (strcmp(Token,"values")==0) {strcpy(tokenType,"values"); return; }
}
void doubleNames(char *Token,char *tokenType){
    if (strcmp(Token,"!=")==0) {strcpy(tokenType,"not_eq"); return; }
    if (strcmp(Token,"!^")==0) {strcpy(tokenType,"xnor"); return; }
    if (strcmp(Token,"&&")==0) {strcpy(tokenType,"and_and"); return; }
    if (strcmp(Token,"+:")==0) {strcpy(tokenType,"plus_range"); return; }
    if (strcmp(Token,"-:")==0) {strcpy(tokenType,"minus_range"); return; }
    if (strcmp(Token,"->")==0) {strcpy(tokenType,"emit"); return; }
    if (strcmp(Token,"<<")==0) {strcpy(tokenType,"shift_left"); return; }
    if (strcmp(Token,"<=")==0) {strcpy(tokenType,"sm_eq"); return; }
    if (strcmp(Token,"==")==0) {strcpy(tokenType,"eq_eq"); return; }
    if (strcmp(Token,">=")==0) {strcpy(tokenType,"gr_eq"); return; }
    if (strcmp(Token,">>")==0) {strcpy(tokenType,"shift_right"); return; }
    if (strcmp(Token,"||")==0) {strcpy(tokenType,"or_or"); return; }
}
int joinable(char *typeA, char *typeB){
     return 0;
}
