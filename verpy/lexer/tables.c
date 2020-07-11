
#include "stdio.h"
#include "string.h"
int in_string(char Chk, char *Again);
void action(char *act,char *tokentype,char Char) ;
int EOL_FLAG() { return 1;}
#define st_backline 1
#define st_bin1 2
#define st_bin2 3
#define st_comment 4
#define st_comment2 5
#define st_define 6
#define st_dig1 7
#define st_dig2 8
#define st_double 9
#define st_either 10
#define st_either1 11
#define st_eqeq2 12
#define st_eqeq3 13
#define st_floating 14
#define st_floating0 15
#define st_hex1 16
#define st_hex2 17
#define st_idle 18
#define st_neq2 19
#define st_neq3 20
#define st_new 21
#define st_newver 22
#define st_newver3 23
#define st_number 24
#define st_power 25
#define st_pragma1 26
#define st_pragma2 27
#define st_shift0 28
#define st_shift1 29
#define st_sizednumber 30
#define st_string 31
#define st_token 32
#define st_ubin1 33
#define st_ubin2 34
#define st_udig1 35
#define st_udig2 36
#define st_uhex1 37
#define st_uhex2 38
char strx0[]="\t \n";
char strx1[]="";
char strx2[]="/";
char strx3[]="\\";
char strx4[]=" ";
char strx5[]="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789_?.,[]{}#@()~%^;:/+-*~-=!<>&|^=<>&|";
char strx6[]="*";
char strx7[]="`";
char strx8[]="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM";
char strx9[]="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789_";
char strx10[]="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM$_";
char strx11[]="0123456789";
char strx12[]=".";
char strx13[]="'";
char strx14[]="b";
char strx15[]="h";
char strx16[]="d";
char strx17[]="{";
char strx18[]="01_xzXZ?";
char strx19[]="0123456789abcdefABCDEF_xX";
char strx20[]="_";
char strx21[]="(";
char strx22[]=")";
char strx23[]=":";
char strx24[]="-";
char strx25[]="+";
char strx26[]="=";
char strx27[]="!";
char strx28[]="<";
char strx29[]=">";
char strx30[]="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789\t \n_?.,[]{}#@()~%^;:/+-*~-=!<>&|`',\\";
char strx31[]="~-=!<>&|";
char strx32[]="^=<>&|";
char strx33[]="\"";
char strx34[]="?.,[]{}#@()~%^;:/+-*";
int State=st_idle;
void stepit(char Char,char Next) {
//    printf("state=%d char=|%c| next=|%c|\n",State,Char,Next);
    switch (State) {
    case st_backline: {
        if (in_string(Char,strx4)&&in_string(Next,strx1)) {
              action("push","token",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx5)&&in_string(Next,strx1)) {
              action("add","0",Char);
              State=st_backline;
              return;
        }
    } break;
    case st_bin1: {
        if (in_string(Char,strx14)&&in_string(Next,strx4)) {
              action("add","0",Char);
              State=st_bin2;
              return;
        }
        if (in_string(Char,strx14)&&in_string(Next,strx18)) {
              action("add","0",Char);
              State=st_bin2;
              return;
        }
    } break;
    case st_bin2: {
        if (in_string(Char,strx4)&&in_string(Next,strx1)) {
              action("add","0",Char);
              State=st_bin2;
              return;
        }
        if (in_string(Char,strx18)&&in_string(Next,strx18)) {
              action("add","0",Char);
              State=st_bin2;
              return;
        }
        if (in_string(Char,strx18)&&in_string(Next,strx1)) {
              action("push","bin",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_comment: {
        if (in_string(Char,strx6)&&in_string(Next,strx2)) {
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
        if (in_string(Char,strx9)&&in_string(Next,strx9)) {
              action("add","0",Char);
              State=st_define;
              return;
        }
        if (in_string(Char,strx9)&&in_string(Next,strx1)) {
              action("push","define",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_dig1: {
        if (in_string(Char,strx16)&&in_string(Next,strx11)) {
              action("add","0",Char);
              State=st_dig2;
              return;
        }
        if (in_string(Char,strx16)&&in_string(Next,strx4)) {
              action("add","0",Char);
              State=st_dig2;
              return;
        }
    } break;
    case st_dig2: {
        if (in_string(Char,strx11)&&in_string(Next,strx11)) {
              action("add","0",Char);
              State=st_dig2;
              return;
        }
        if (in_string(Char,strx11)&&in_string(Next,strx20)) {
              action("add","0",Char);
              State=st_dig2;
              return;
        }
        if (in_string(Char,strx11)&&in_string(Next,strx1)) {
              action("push","dig",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_double: {
        if (in_string(Char,strx32)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_either: {
        if (in_string(Char,strx6)&&in_string(Next,strx22)) {
              action("add","0",Char);
              State=st_either1;
              return;
        }
        if (in_string(Char,strx6)&&in_string(Next,strx1)) {
              action("none","0",Char);
              State=st_pragma1;
              return;
        }
    } break;
    case st_either1: {
        if (in_string(Char,strx22)&&in_string(Next,strx1)) {
              action("push","star",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_eqeq2: {
        if (in_string(Char,strx26)&&in_string(Next,strx26)) {
              action("add","0",Char);
              State=st_eqeq3;
              return;
        }
        if (in_string(Char,strx26)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_eqeq3: {
        if (in_string(Char,strx26)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_floating: {
        if (in_string(Char,strx11)&&in_string(Next,strx11)) {
              action("add","0",Char);
              State=st_floating;
              return;
        }
        if (in_string(Char,strx11)&&in_string(Next,strx1)) {
              action("push","floating",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_floating0: {
        if (in_string(Char,strx12)&&in_string(Next,strx11)) {
              action("add","0",Char);
              State=st_floating;
              return;
        }
    } break;
    case st_hex1: {
        if (in_string(Char,strx15)&&in_string(Next,strx19)) {
              action("add","0",Char);
              State=st_hex2;
              return;
        }
    } break;
    case st_hex2: {
        if (in_string(Char,strx19)&&in_string(Next,strx19)) {
              action("add","0",Char);
              State=st_hex2;
              return;
        }
        if (in_string(Char,strx19)&&in_string(Next,strx1)) {
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
        if (in_string(Char,strx3)&&in_string(Next,strx1)) {
              action("add","0",Char);
              State=st_backline;
              return;
        }
        if (in_string(Char,strx2)&&in_string(Next,strx6)) {
              action("none","0",Char);
              State=st_comment;
              return;
        }
        if (in_string(Char,strx7)&&in_string(Next,strx8)) {
              action("add","0",Char);
              State=st_define;
              return;
        }
        if (in_string(Char,strx10)&&in_string(Next,strx9)) {
              action("add","0",Char);
              State=st_token;
              return;
        }
        if (in_string(Char,strx8)&&in_string(Next,strx1)) {
              action("push","token",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx11)&&in_string(Next,strx11)) {
              action("add","0",Char);
              State=st_number;
              return;
        }
        if (in_string(Char,strx11)&&in_string(Next,strx12)) {
              action("add","0",Char);
              State=st_floating0;
              return;
        }
        if (in_string(Char,strx11)&&in_string(Next,strx1)) {
              action("push","number",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx13)&&in_string(Next,strx14)) {
              action("add","0",Char);
              State=st_ubin1;
              return;
        }
        if (in_string(Char,strx13)&&in_string(Next,strx15)) {
              action("add","0",Char);
              State=st_uhex1;
              return;
        }
        if (in_string(Char,strx13)&&in_string(Next,strx16)) {
              action("add","0",Char);
              State=st_udig1;
              return;
        }
        if (in_string(Char,strx13)&&in_string(Next,strx17)) {
              action("none","0",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx21)&&in_string(Next,strx6)) {
              action("add","0",Char);
              State=st_either;
              return;
        }
        if (in_string(Char,strx23)&&in_string(Next,strx23)) {
              action("add","0",Char);
              State=st_new;
              return;
        }
        if (in_string(Char,strx24)&&in_string(Next,strx23)) {
              action("add","0",Char);
              State=st_new;
              return;
        }
        if (in_string(Char,strx25)&&in_string(Next,strx23)) {
              action("add","0",Char);
              State=st_new;
              return;
        }
        if (in_string(Char,strx26)&&in_string(Next,strx26)) {
              action("add","0",Char);
              State=st_eqeq2;
              return;
        }
        if (in_string(Char,strx27)&&in_string(Next,strx26)) {
              action("add","0",Char);
              State=st_neq2;
              return;
        }
        if (in_string(Char,strx28)&&in_string(Next,strx29)) {
              action("add","0",Char);
              State=st_newver;
              return;
        }
        if (in_string(Char,strx29)&&in_string(Next,strx29)) {
              action("add","0",Char);
              State=st_shift0;
              return;
        }
        if (in_string(Char,strx6)&&in_string(Next,strx6)) {
              action("add","0",Char);
              State=st_power;
              return;
        }
        if (in_string(Char,strx31)&&in_string(Next,strx32)) {
              action("add","0",Char);
              State=st_double;
              return;
        }
        if (in_string(Char,strx31)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx33)&&in_string(Next,strx1)) {
              action("add","0",Char);
              State=st_string;
              return;
        }
        if (in_string(Char,strx34)&&in_string(Next,strx1)) {
              action("push","single",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx3)&&in_string(Next,strx1)) {
              action("add","idle",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_neq2: {
        if (in_string(Char,strx26)&&in_string(Next,strx26)) {
              action("add","0",Char);
              State=st_neq3;
              return;
        }
        if (in_string(Char,strx26)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_neq3: {
        if (in_string(Char,strx26)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_new: {
        if (in_string(Char,strx23)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_newver: {
        if (in_string(Char,strx28)&&in_string(Next,strx29)) {
              action("add","0",Char);
              State=st_newver3;
              return;
        }
        if (in_string(Char,strx30)&&in_string(Next,strx30)) {
              action("add","0",Char);
              State=st_newver;
              return;
        }
    } break;
    case st_newver3: {
        if (in_string(Char,strx1)&&in_string(Next,strx1)) {
              action("push","newver",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_number: {
        if (in_string(Char,strx11)&&in_string(Next,strx11)) {
              action("add","0",Char);
              State=st_number;
              return;
        }
        if (in_string(Char,strx11)&&in_string(Next,strx13)) {
              action("add","0",Char);
              State=st_sizednumber;
              return;
        }
        if (in_string(Char,strx11)&&in_string(Next,strx12)) {
              action("add","0",Char);
              State=st_floating0;
              return;
        }
        if (in_string(Char,strx11)&&in_string(Next,strx1)) {
              action("push","number",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_power: {
        if (in_string(Char,strx6)&&in_string(Next,strx1)) {
              action("push","power",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_pragma1: {
        if (in_string(Char,strx6)&&in_string(Next,strx22)) {
              action("none","0",Char);
              State=st_pragma2;
              return;
        }
        if (in_string(Char,strx1)&&in_string(Next,strx1)) {
              action("none","0",Char);
              State=st_pragma1;
              return;
        }
    } break;
    case st_pragma2: {
        if (in_string(Char,strx22)&&in_string(Next,strx1)) {
              action("clear","0",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_shift0: {
        if (in_string(Char,strx29)&&in_string(Next,strx29)) {
              action("add","0",Char);
              State=st_shift1;
              return;
        }
        if (in_string(Char,strx29)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_shift1: {
        if (in_string(Char,strx29)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_sizednumber: {
        if (in_string(Char,strx13)&&in_string(Next,strx14)) {
              action("add","0",Char);
              State=st_bin1;
              return;
        }
        if (in_string(Char,strx13)&&in_string(Next,strx15)) {
              action("add","0",Char);
              State=st_hex1;
              return;
        }
        if (in_string(Char,strx13)&&in_string(Next,strx16)) {
              action("add","0",Char);
              State=st_dig1;
              return;
        }
    } break;
    case st_string: {
        if (in_string(Char,strx33)&&in_string(Next,strx1)) {
              action("push","string",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx30)&&in_string(Next,strx1)) {
              action("add","0",Char);
              State=st_string;
              return;
        }
    } break;
    case st_token: {
        if (in_string(Char,strx9)&&in_string(Next,strx9)) {
              action("add","0",Char);
              State=st_token;
              return;
        }
        if (in_string(Char,strx9)&&in_string(Next,strx1)) {
              action("push","token",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_ubin1: {
        if (in_string(Char,strx14)&&in_string(Next,strx4)) {
              action("add","0",Char);
              State=st_ubin2;
              return;
        }
        if (in_string(Char,strx14)&&in_string(Next,strx18)) {
              action("add","0",Char);
              State=st_ubin2;
              return;
        }
    } break;
    case st_ubin2: {
        if (in_string(Char,strx4)&&in_string(Next,strx1)) {
              action("add","0",Char);
              State=st_ubin2;
              return;
        }
        if (in_string(Char,strx18)&&in_string(Next,strx18)) {
              action("add","0",Char);
              State=st_ubin2;
              return;
        }
        if (in_string(Char,strx18)&&in_string(Next,strx1)) {
              action("push","ubin",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_udig1: {
        if (in_string(Char,strx16)&&in_string(Next,strx11)) {
              action("add","0",Char);
              State=st_udig2;
              return;
        }
        if (in_string(Char,strx16)&&in_string(Next,strx4)) {
              action("add","0",Char);
              State=st_udig2;
              return;
        }
    } break;
    case st_udig2: {
        if (in_string(Char,strx4)&&in_string(Next,strx11)) {
              action("add","0",Char);
              State=st_udig2;
              return;
        }
        if (in_string(Char,strx11)&&in_string(Next,strx11)) {
              action("add","0",Char);
              State=st_udig2;
              return;
        }
        if (in_string(Char,strx11)&&in_string(Next,strx1)) {
              action("push","udig",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_uhex1: {
        if (in_string(Char,strx15)&&in_string(Next,strx19)) {
              action("add","0",Char);
              State=st_uhex2;
              return;
        }
        if (in_string(Char,strx15)&&in_string(Next,strx4)) {
              action("add","0",Char);
              State=st_uhex2;
              return;
        }
    } break;
    case st_uhex2: {
        if (in_string(Char,strx4)&&in_string(Next,strx19)) {
              action("add","0",Char);
              State=st_uhex2;
              return;
        }
        if (in_string(Char,strx19)&&in_string(Next,strx19)) {
              action("add","0",Char);
              State=st_uhex2;
              return;
        }
        if (in_string(Char,strx19)&&in_string(Next,strx1)) {
              action("push","uhex",Char);
              State=st_idle;
              return;
        }
    } break;
    }
    printf("no action!!!! |%x| <%c> |%x| <%c> state=%d \n",Char,Char,Next,Next,State);
}
void reserved_words(char *Token,char *tokenType){
    if (strcmp(Token,"_priority")==0) {strcpy(tokenType,"_priority"); return; }
    if (strcmp(Token,"_unique")==0) {strcpy(tokenType,"_unique"); return; }
    if (strcmp(Token,"`default_nettype")==0) {strcpy(tokenType,"`default_nettype"); return; }
    if (strcmp(Token,"`define")==0) {strcpy(tokenType,"`define"); return; }
    if (strcmp(Token,"`endif")==0) {strcpy(tokenType,"`endif"); return; }
    if (strcmp(Token,"`ifdef")==0) {strcpy(tokenType,"`ifdef"); return; }
    if (strcmp(Token,"`ifndef")==0) {strcpy(tokenType,"`ifndef"); return; }
    if (strcmp(Token,"`include")==0) {strcpy(tokenType,"`include"); return; }
    if (strcmp(Token,"`timescale")==0) {strcpy(tokenType,"`timescale"); return; }
    if (strcmp(Token,"`undef")==0) {strcpy(tokenType,"`undef"); return; }
    if (strcmp(Token,"always")==0) {strcpy(tokenType,"always"); return; }
    if (strcmp(Token,"always_comb")==0) {strcpy(tokenType,"always_comb"); return; }
    if (strcmp(Token,"always_ff")==0) {strcpy(tokenType,"always_ff"); return; }
    if (strcmp(Token,"always_latch")==0) {strcpy(tokenType,"always_latch"); return; }
    if (strcmp(Token,"assert")==0) {strcpy(tokenType,"assert"); return; }
    if (strcmp(Token,"assign")==0) {strcpy(tokenType,"assign"); return; }
    if (strcmp(Token,"begin")==0) {strcpy(tokenType,"begin"); return; }
    if (strcmp(Token,"bins")==0) {strcpy(tokenType,"bins"); return; }
    if (strcmp(Token,"bit")==0) {strcpy(tokenType,"bit"); return; }
    if (strcmp(Token,"case")==0) {strcpy(tokenType,"case"); return; }
    if (strcmp(Token,"casex")==0) {strcpy(tokenType,"casex"); return; }
    if (strcmp(Token,"casez")==0) {strcpy(tokenType,"casez"); return; }
    if (strcmp(Token,"class")==0) {strcpy(tokenType,"class"); return; }
    if (strcmp(Token,"constraint")==0) {strcpy(tokenType,"constraint"); return; }
    if (strcmp(Token,"covergroup")==0) {strcpy(tokenType,"covergroup"); return; }
    if (strcmp(Token,"coverpoint")==0) {strcpy(tokenType,"coverpoint"); return; }
    if (strcmp(Token,"cross")==0) {strcpy(tokenType,"cross"); return; }
    if (strcmp(Token,"deassign")==0) {strcpy(tokenType,"deassign"); return; }
    if (strcmp(Token,"default")==0) {strcpy(tokenType,"default"); return; }
    if (strcmp(Token,"defparam")==0) {strcpy(tokenType,"defparam"); return; }
    if (strcmp(Token,"disable")==0) {strcpy(tokenType,"disable"); return; }
    if (strcmp(Token,"else")==0) {strcpy(tokenType,"else"); return; }
    if (strcmp(Token,"end")==0) {strcpy(tokenType,"end"); return; }
    if (strcmp(Token,"endcase")==0) {strcpy(tokenType,"endcase"); return; }
    if (strcmp(Token,"endclass")==0) {strcpy(tokenType,"endclass"); return; }
    if (strcmp(Token,"endfunction")==0) {strcpy(tokenType,"endfunction"); return; }
    if (strcmp(Token,"endgenerate")==0) {strcpy(tokenType,"endgenerate"); return; }
    if (strcmp(Token,"endgroup")==0) {strcpy(tokenType,"endgroup"); return; }
    if (strcmp(Token,"endmodule")==0) {strcpy(tokenType,"endmodule"); return; }
    if (strcmp(Token,"endprimitive")==0) {strcpy(tokenType,"endprimitive"); return; }
    if (strcmp(Token,"endprimitive")==0) {strcpy(tokenType,"endprimitive"); return; }
    if (strcmp(Token,"endproperty")==0) {strcpy(tokenType,"endproperty"); return; }
    if (strcmp(Token,"endsequence")==0) {strcpy(tokenType,"endsequence"); return; }
    if (strcmp(Token,"endspecify")==0) {strcpy(tokenType,"endspecify"); return; }
    if (strcmp(Token,"endtable")==0) {strcpy(tokenType,"endtable"); return; }
    if (strcmp(Token,"endtask")==0) {strcpy(tokenType,"endtask"); return; }
    if (strcmp(Token,"enum")==0) {strcpy(tokenType,"enum"); return; }
    if (strcmp(Token,"event")==0) {strcpy(tokenType,"event"); return; }
    if (strcmp(Token,"extends")==0) {strcpy(tokenType,"extends"); return; }
    if (strcmp(Token,"for")==0) {strcpy(tokenType,"for"); return; }
    if (strcmp(Token,"force")==0) {strcpy(tokenType,"force"); return; }
    if (strcmp(Token,"forever")==0) {strcpy(tokenType,"forever"); return; }
    if (strcmp(Token,"forever")==0) {strcpy(tokenType,"forever"); return; }
    if (strcmp(Token,"fork")==0) {strcpy(tokenType,"fork"); return; }
    if (strcmp(Token,"function")==0) {strcpy(tokenType,"function"); return; }
    if (strcmp(Token,"generate")==0) {strcpy(tokenType,"generate"); return; }
    if (strcmp(Token,"genvar")==0) {strcpy(tokenType,"genvar"); return; }
    if (strcmp(Token,"highz0")==0) {strcpy(tokenType,"highz0"); return; }
    if (strcmp(Token,"highz1")==0) {strcpy(tokenType,"highz1"); return; }
    if (strcmp(Token,"if")==0) {strcpy(tokenType,"if"); return; }
    if (strcmp(Token,"iff")==0) {strcpy(tokenType,"iff"); return; }
    if (strcmp(Token,"initial")==0) {strcpy(tokenType,"initial"); return; }
    if (strcmp(Token,"inout")==0) {strcpy(tokenType,"inout"); return; }
    if (strcmp(Token,"input")==0) {strcpy(tokenType,"input"); return; }
    if (strcmp(Token,"integer")==0) {strcpy(tokenType,"integer"); return; }
    if (strcmp(Token,"join")==0) {strcpy(tokenType,"join"); return; }
    if (strcmp(Token,"join_any")==0) {strcpy(tokenType,"join_any"); return; }
    if (strcmp(Token,"join_none")==0) {strcpy(tokenType,"join_none"); return; }
    if (strcmp(Token,"localparam")==0) {strcpy(tokenType,"localparam"); return; }
    if (strcmp(Token,"mailbox")==0) {strcpy(tokenType,"mailbox"); return; }
    if (strcmp(Token,"module")==0) {strcpy(tokenType,"module"); return; }
    if (strcmp(Token,"negedge")==0) {strcpy(tokenType,"negedge"); return; }
    if (strcmp(Token,"new")==0) {strcpy(tokenType,"new"); return; }
    if (strcmp(Token,"or")==0) {strcpy(tokenType,"or"); return; }
    if (strcmp(Token,"output")==0) {strcpy(tokenType,"output"); return; }
    if (strcmp(Token,"parameter")==0) {strcpy(tokenType,"parameter"); return; }
    if (strcmp(Token,"posedge")==0) {strcpy(tokenType,"posedge"); return; }
    if (strcmp(Token,"primitive")==0) {strcpy(tokenType,"primitive"); return; }
    if (strcmp(Token,"property")==0) {strcpy(tokenType,"property"); return; }
    if (strcmp(Token,"pull0")==0) {strcpy(tokenType,"pull0"); return; }
    if (strcmp(Token,"pull1")==0) {strcpy(tokenType,"pull1"); return; }
    if (strcmp(Token,"rand")==0) {strcpy(tokenType,"rand"); return; }
    if (strcmp(Token,"randomize")==0) {strcpy(tokenType,"randomize"); return; }
    if (strcmp(Token,"real")==0) {strcpy(tokenType,"real"); return; }
    if (strcmp(Token,"reg")==0) {strcpy(tokenType,"reg"); return; }
    if (strcmp(Token,"release")==0) {strcpy(tokenType,"release"); return; }
    if (strcmp(Token,"repeat")==0) {strcpy(tokenType,"repeat"); return; }
    if (strcmp(Token,"semaphore")==0) {strcpy(tokenType,"semaphore"); return; }
    if (strcmp(Token,"sequence")==0) {strcpy(tokenType,"sequence"); return; }
    if (strcmp(Token,"signed")==0) {strcpy(tokenType,"signed"); return; }
    if (strcmp(Token,"specify")==0) {strcpy(tokenType,"specify"); return; }
    if (strcmp(Token,"specparam")==0) {strcpy(tokenType,"specparam"); return; }
    if (strcmp(Token,"strong0")==0) {strcpy(tokenType,"strong0"); return; }
    if (strcmp(Token,"strong1")==0) {strcpy(tokenType,"strong1"); return; }
    if (strcmp(Token,"supply0")==0) {strcpy(tokenType,"supply0"); return; }
    if (strcmp(Token,"supply1")==0) {strcpy(tokenType,"supply1"); return; }
    if (strcmp(Token,"table")==0) {strcpy(tokenType,"table"); return; }
    if (strcmp(Token,"task")==0) {strcpy(tokenType,"task"); return; }
    if (strcmp(Token,"time")==0) {strcpy(tokenType,"time"); return; }
    if (strcmp(Token,"tri")==0) {strcpy(tokenType,"tri"); return; }
    if (strcmp(Token,"tri0")==0) {strcpy(tokenType,"tri0"); return; }
    if (strcmp(Token,"tri0")==0) {strcpy(tokenType,"tri0"); return; }
    if (strcmp(Token,"tri1")==0) {strcpy(tokenType,"tri1"); return; }
    if (strcmp(Token,"tri1")==0) {strcpy(tokenType,"tri1"); return; }
    if (strcmp(Token,"trireg")==0) {strcpy(tokenType,"trireg"); return; }
    if (strcmp(Token,"typedef")==0) {strcpy(tokenType,"typedef"); return; }
    if (strcmp(Token,"vectored")==0) {strcpy(tokenType,"vectored"); return; }
    if (strcmp(Token,"wait")==0) {strcpy(tokenType,"wait"); return; }
    if (strcmp(Token,"wand")==0) {strcpy(tokenType,"wand"); return; }
    if (strcmp(Token,"weak0")==0) {strcpy(tokenType,"weak0"); return; }
    if (strcmp(Token,"weak1")==0) {strcpy(tokenType,"weak1"); return; }
    if (strcmp(Token,"while")==0) {strcpy(tokenType,"while"); return; }
    if (strcmp(Token,"wire")==0) {strcpy(tokenType,"wire"); return; }
    if (strcmp(Token,"with")==0) {strcpy(tokenType,"with"); return; }
    if (strcmp(Token,"wreal")==0) {strcpy(tokenType,"wreal"); return; }
}
void doubleNames(char *Token,char *tokenType){
    if (strcmp(Token,"!&")==0) {strcpy(tokenType,"nand"); return; }
    if (strcmp(Token,"!=")==0) {strcpy(tokenType,"not_eq"); return; }
    if (strcmp(Token,"!==")==0) {strcpy(tokenType,"noteqeq"); return; }
    if (strcmp(Token,"!^")==0) {strcpy(tokenType,"xnor"); return; }
    if (strcmp(Token,"!|")==0) {strcpy(tokenType,"nor"); return; }
    if (strcmp(Token,"&&")==0) {strcpy(tokenType,"and_and"); return; }
    if (strcmp(Token,"+:")==0) {strcpy(tokenType,"plus_range"); return; }
    if (strcmp(Token,"-:")==0) {strcpy(tokenType,"minus_range"); return; }
    if (strcmp(Token,"->")==0) {strcpy(tokenType,"emit"); return; }
    if (strcmp(Token,"::")==0) {strcpy(tokenType,"domino"); return; }
    if (strcmp(Token,"<<")==0) {strcpy(tokenType,"shift_left"); return; }
    if (strcmp(Token,"<=")==0) {strcpy(tokenType,"sm_eq"); return; }
    if (strcmp(Token,"==")==0) {strcpy(tokenType,"eq_eq"); return; }
    if (strcmp(Token,"===")==0) {strcpy(tokenType,"eq3"); return; }
    if (strcmp(Token,">=")==0) {strcpy(tokenType,"gr_eq"); return; }
    if (strcmp(Token,">>")==0) {strcpy(tokenType,"shift_right"); return; }
    if (strcmp(Token,">>>")==0) {strcpy(tokenType,"arith_shift_right"); return; }
    if (strcmp(Token,"||")==0) {strcpy(tokenType,"or_or"); return; }
    if (strcmp(Token,"~&")==0) {strcpy(tokenType,"nand"); return; }
    if (strcmp(Token,"~^")==0) {strcpy(tokenType,"xnor"); return; }
    if (strcmp(Token,"~|")==0) {strcpy(tokenType,"nor"); return; }
}
int joinable(char *typeA, char *typeB){
    if ((strcmp("number",typeA)==0)&&(strcmp("uhex",typeB)==0)) return 1;
    if ((strcmp("number",typeA)==0)&&(strcmp("udig",typeB)==0)) return 1;
    if ((strcmp("number",typeA)==0)&&(strcmp("ubin",typeB)==0)) return 1;
     return 0;
}
