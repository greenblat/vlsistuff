
#include "stdio.h"
#include "string.h"
int in_string(char Chk, char *Again);
void action(char *act,char *tokentype,char Char) ;
int EOL_FLAG() { return 0;}
#define st_Literal1 1
#define st_based2 2
#define st_based3 3
#define st_basednumber 4
#define st_bin2 5
#define st_cassign 6
#define st_define 7
#define st_dig2 8
#define st_double 9
#define st_either 10
#define st_either1 11
#define st_eqeq2 12
#define st_eqeq3 13
#define st_floating 14
#define st_floating0 15
#define st_hex 16
#define st_hex2 17
#define st_hex3 18
#define st_idle 19
#define st_neq2 20
#define st_newx 21
#define st_number 22
#define st_power 23
#define st_pragma1 24
#define st_pragma2 25
#define st_string 26
#define st_token 27
#define st_ubin1 28
#define st_ubin2 29
#define st_udig1 30
#define st_udig2 31
#define st_uhex1 32
#define st_uhex2 33
char strx0[]="\t\n ";
char strx1[]="";
char strx2[]="-";
char strx3[]="xXoObB";
char strx4[]="\"";
char strx5[]="0123456789abcdefABCDEF_xX";
char strx6[]="`";
char strx7[]="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM";
char strx8[]="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789_";
char strx9[]="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789_.";
char strx10[]="0123456789";
char strx11[]=".";
char strx12[]="'";
char strx13[]="0123456789-Zz";
char strx14[]="#";
char strx15[]="01_xzXZ?";
char strx16[]="b";
char strx17[]="h";
char strx18[]="d";
char strx19[]="(";
char strx20[]="*";
char strx21[]=")";
char strx22[]=":";
char strx23[]="=";
char strx24[]="+";
char strx25[]="/";
char strx26[]="-=!<>&|";
char strx27[]="=<>&|";
char strx28[]="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789\t\n _?.,[]{}#@()~%^;:/+-*-=!<>&|',\\";
char strx29[]="?.,[]{}#@()~%^;:/+-*";
char strx30[]="\\";
int State=st_idle;
void stepit(char Char,char Next) {
//    printf("state=%d char=|%c| next=|%c|\n",State,Char,Next);
    switch (State) {
    case st_Literal1: {
        if (in_string(Char,strx13)&&in_string(Next,strx1)) {
              action("add","0",Char);
              State=st_Literal1;
              return;
        }
        if (in_string(Char,strx12)&&in_string(Next,strx1)) {
              action("push","literal",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_based2: {
        if (in_string(Char,strx5)&&in_string(Next,strx5)) {
              action("add","0",Char);
              State=st_based2;
              return;
        }
        if (in_string(Char,strx5)&&in_string(Next,strx14)) {
              action("add","0",Char);
              State=st_based3;
              return;
        }
    } break;
    case st_based3: {
        if (in_string(Char,strx14)&&in_string(Next,strx1)) {
              action("push","based",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_basednumber: {
        if (in_string(Char,strx14)&&in_string(Next,strx5)) {
              action("add","0",Char);
              State=st_based2;
              return;
        }
    } break;
    case st_bin2: {
        if (in_string(Char,strx15)&&in_string(Next,strx15)) {
              action("add","0",Char);
              State=st_bin2;
              return;
        }
        if (in_string(Char,strx15)&&in_string(Next,strx1)) {
              action("push","bin",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_cassign: {
        if (in_string(Char,strx23)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_define: {
        if (in_string(Char,strx8)&&in_string(Next,strx8)) {
              action("add","0",Char);
              State=st_define;
              return;
        }
        if (in_string(Char,strx8)&&in_string(Next,strx1)) {
              action("push","define",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_dig2: {
        if (in_string(Char,strx10)&&in_string(Next,strx10)) {
              action("add","0",Char);
              State=st_dig2;
              return;
        }
        if (in_string(Char,strx10)&&in_string(Next,strx1)) {
              action("push","dig",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_double: {
        if (in_string(Char,strx26)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_either: {
        if (in_string(Char,strx20)&&in_string(Next,strx21)) {
              action("add","0",Char);
              State=st_either1;
              return;
        }
        if (in_string(Char,strx20)&&in_string(Next,strx1)) {
              action("add","0",Char);
              State=st_pragma1;
              return;
        }
    } break;
    case st_either1: {
        if (in_string(Char,strx21)&&in_string(Next,strx1)) {
              action("push","star",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_eqeq2: {
        if (in_string(Char,strx23)&&in_string(Next,strx23)) {
              action("add","0",Char);
              State=st_eqeq3;
              return;
        }
        if (in_string(Char,strx23)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_eqeq3: {
        if (in_string(Char,strx23)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_floating: {
        if (in_string(Char,strx10)&&in_string(Next,strx10)) {
              action("add","0",Char);
              State=st_floating;
              return;
        }
        if (in_string(Char,strx10)&&in_string(Next,strx1)) {
              action("push","floating",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_floating0: {
        if (in_string(Char,strx11)&&in_string(Next,strx10)) {
              action("add","0",Char);
              State=st_floating;
              return;
        }
    } break;
    case st_hex: {
        if (in_string(Char,strx4)&&in_string(Next,strx5)) {
              action("add","0",Char);
              State=st_hex2;
              return;
        }
    } break;
    case st_hex2: {
        if (in_string(Char,strx5)&&in_string(Next,strx5)) {
              action("add","0",Char);
              State=st_hex2;
              return;
        }
        if (in_string(Char,strx5)&&in_string(Next,strx4)) {
              action("add","0",Char);
              State=st_hex3;
              return;
        }
        if (in_string(Char,strx5)&&in_string(Next,strx5)) {
              action("add","0",Char);
              State=st_hex2;
              return;
        }
        if (in_string(Char,strx5)&&in_string(Next,strx1)) {
              action("push","hex",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_hex3: {
        if (in_string(Char,strx4)&&in_string(Next,strx1)) {
              action("push","hexdig",Char);
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
        if (in_string(Char,strx3)&&in_string(Next,strx4)) {
              action("add","0",Char);
              State=st_hex;
              return;
        }
        if (in_string(Char,strx6)&&in_string(Next,strx7)) {
              action("add","0",Char);
              State=st_define;
              return;
        }
        if (in_string(Char,strx7)&&in_string(Next,strx9)) {
              action("add","0",Char);
              State=st_token;
              return;
        }
        if (in_string(Char,strx7)&&in_string(Next,strx1)) {
              action("push","token",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx10)&&in_string(Next,strx10)) {
              action("add","0",Char);
              State=st_number;
              return;
        }
        if (in_string(Char,strx10)&&in_string(Next,strx11)) {
              action("add","0",Char);
              State=st_floating0;
              return;
        }
        if (in_string(Char,strx10)&&in_string(Next,strx1)) {
              action("push","number",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx12)&&in_string(Next,strx13)) {
              action("add","0",Char);
              State=st_Literal1;
              return;
        }
        if (in_string(Char,strx12)&&in_string(Next,strx1)) {
              action("push","tick",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx19)&&in_string(Next,strx20)) {
              action("add","0",Char);
              State=st_either;
              return;
        }
        if (in_string(Char,strx22)&&in_string(Next,strx23)) {
              action("add","0",Char);
              State=st_cassign;
              return;
        }
        if (in_string(Char,strx2)&&in_string(Next,strx22)) {
              action("add","0",Char);
              State=st_newx;
              return;
        }
        if (in_string(Char,strx24)&&in_string(Next,strx22)) {
              action("add","0",Char);
              State=st_newx;
              return;
        }
        if (in_string(Char,strx23)&&in_string(Next,strx23)) {
              action("add","0",Char);
              State=st_eqeq2;
              return;
        }
        if (in_string(Char,strx25)&&in_string(Next,strx23)) {
              action("add","0",Char);
              State=st_neq2;
              return;
        }
        if (in_string(Char,strx20)&&in_string(Next,strx20)) {
              action("add","0",Char);
              State=st_power;
              return;
        }
        if (in_string(Char,strx26)&&in_string(Next,strx27)) {
              action("add","0",Char);
              State=st_double;
              return;
        }
        if (in_string(Char,strx26)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx4)&&in_string(Next,strx1)) {
              action("add","0",Char);
              State=st_string;
              return;
        }
        if (in_string(Char,strx29)&&in_string(Next,strx1)) {
              action("push","single",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx30)&&in_string(Next,strx1)) {
              action("add","idle",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_neq2: {
        if (in_string(Char,strx23)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_newx: {
        if (in_string(Char,strx22)&&in_string(Next,strx1)) {
              action("push","double",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_number: {
        if (in_string(Char,strx10)&&in_string(Next,strx10)) {
              action("add","0",Char);
              State=st_number;
              return;
        }
        if (in_string(Char,strx10)&&in_string(Next,strx14)) {
              action("add","0",Char);
              State=st_basednumber;
              return;
        }
        if (in_string(Char,strx10)&&in_string(Next,strx11)) {
              action("add","0",Char);
              State=st_floating0;
              return;
        }
        if (in_string(Char,strx10)&&in_string(Next,strx1)) {
              action("push","number",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_power: {
        if (in_string(Char,strx20)&&in_string(Next,strx1)) {
              action("push","power",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_pragma1: {
        if (in_string(Char,strx20)&&in_string(Next,strx21)) {
              action("add","0",Char);
              State=st_pragma2;
              return;
        }
    } break;
    case st_pragma2: {
        if (in_string(Char,strx21)&&in_string(Next,strx1)) {
              action("push","pragma",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_string: {
        if (in_string(Char,strx4)&&in_string(Next,strx1)) {
              action("push","string",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx28)&&in_string(Next,strx1)) {
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
        if (in_string(Char,strx8)&&in_string(Next,strx1)) {
              action("push","token",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_ubin1: {
        if (in_string(Char,strx16)&&in_string(Next,strx15)) {
              action("add","0",Char);
              State=st_ubin2;
              return;
        }
    } break;
    case st_ubin2: {
        if (in_string(Char,strx15)&&in_string(Next,strx15)) {
              action("add","0",Char);
              State=st_ubin2;
              return;
        }
        if (in_string(Char,strx15)&&in_string(Next,strx1)) {
              action("push","ubin",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_udig1: {
        if (in_string(Char,strx18)&&in_string(Next,strx10)) {
              action("add","0",Char);
              State=st_udig2;
              return;
        }
    } break;
    case st_udig2: {
        if (in_string(Char,strx10)&&in_string(Next,strx10)) {
              action("add","0",Char);
              State=st_udig2;
              return;
        }
        if (in_string(Char,strx10)&&in_string(Next,strx1)) {
              action("push","udig",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_uhex1: {
        if (in_string(Char,strx17)&&in_string(Next,strx5)) {
              action("add","0",Char);
              State=st_uhex2;
              return;
        }
    } break;
    case st_uhex2: {
        if (in_string(Char,strx5)&&in_string(Next,strx5)) {
              action("add","0",Char);
              State=st_uhex2;
              return;
        }
        if (in_string(Char,strx5)&&in_string(Next,strx1)) {
              action("push","uhex",Char);
              State=st_idle;
              return;
        }
    } break;
    }
    printf("no action!!!! |%x| <%c> |%x| <%c> state=%d \n",Char,Char,Next,Next,State);
}
void reserved_words(char *Token,char *tokenType){
    if (strcmp(Token,"Component")==0) {strcpy(tokenType,"Component"); return; }
    if (strcmp(Token,"EqualLess")==0) {strcpy(tokenType,"EqualLess"); return; }
    if (strcmp(Token,"GreaterEqual")==0) {strcpy(tokenType,"GreaterEqual"); return; }
    if (strcmp(Token,"Postponed")==0) {strcpy(tokenType,"Postponed"); return; }
    if (strcmp(Token,"after")==0) {strcpy(tokenType,"after"); return; }
    if (strcmp(Token,"alias")==0) {strcpy(tokenType,"alias"); return; }
    if (strcmp(Token,"and")==0) {strcpy(tokenType,"and"); return; }
    if (strcmp(Token,"architecture")==0) {strcpy(tokenType,"architecture"); return; }
    if (strcmp(Token,"array")==0) {strcpy(tokenType,"array"); return; }
    if (strcmp(Token,"arrow")==0) {strcpy(tokenType,"arrow"); return; }
    if (strcmp(Token,"assert")==0) {strcpy(tokenType,"assert"); return; }
    if (strcmp(Token,"attribute")==0) {strcpy(tokenType,"attribute"); return; }
    if (strcmp(Token,"begin")==0) {strcpy(tokenType,"begin"); return; }
    if (strcmp(Token,"behavioral")==0) {strcpy(tokenType,"behavioral"); return; }
    if (strcmp(Token,"block")==0) {strcpy(tokenType,"block"); return; }
    if (strcmp(Token,"body")==0) {strcpy(tokenType,"body"); return; }
    if (strcmp(Token,"buffer")==0) {strcpy(tokenType,"buffer"); return; }
    if (strcmp(Token,"case")==0) {strcpy(tokenType,"case"); return; }
    if (strcmp(Token,"cassign")==0) {strcpy(tokenType,"cassign"); return; }
    if (strcmp(Token,"configuration")==0) {strcpy(tokenType,"configuration"); return; }
    if (strcmp(Token,"constant")==0) {strcpy(tokenType,"constant"); return; }
    if (strcmp(Token,"downto")==0) {strcpy(tokenType,"downto"); return; }
    if (strcmp(Token,"else")==0) {strcpy(tokenType,"else"); return; }
    if (strcmp(Token,"elsif")==0) {strcpy(tokenType,"elsif"); return; }
    if (strcmp(Token,"end")==0) {strcpy(tokenType,"end"); return; }
    if (strcmp(Token,"entity")==0) {strcpy(tokenType,"entity"); return; }
    if (strcmp(Token,"event")==0) {strcpy(tokenType,"event"); return; }
    if (strcmp(Token,"exit")==0) {strcpy(tokenType,"exit"); return; }
    if (strcmp(Token,"file")==0) {strcpy(tokenType,"file"); return; }
    if (strcmp(Token,"floating")==0) {strcpy(tokenType,"floating"); return; }
    if (strcmp(Token,"for")==0) {strcpy(tokenType,"for"); return; }
    if (strcmp(Token,"function")==0) {strcpy(tokenType,"function"); return; }
    if (strcmp(Token,"generate")==0) {strcpy(tokenType,"generate"); return; }
    if (strcmp(Token,"generic")==0) {strcpy(tokenType,"generic"); return; }
    if (strcmp(Token,"guarded")==0) {strcpy(tokenType,"guarded"); return; }
    if (strcmp(Token,"hexstring")==0) {strcpy(tokenType,"hexstring"); return; }
    if (strcmp(Token,"hobstring")==0) {strcpy(tokenType,"hobstring"); return; }
    if (strcmp(Token,"if")==0) {strcpy(tokenType,"if"); return; }
    if (strcmp(Token,"impure")==0) {strcpy(tokenType,"impure"); return; }
    if (strcmp(Token,"in")==0) {strcpy(tokenType,"in"); return; }
    if (strcmp(Token,"inertial")==0) {strcpy(tokenType,"inertial"); return; }
    if (strcmp(Token,"inout")==0) {strcpy(tokenType,"inout"); return; }
    if (strcmp(Token,"is")==0) {strcpy(tokenType,"is"); return; }
    if (strcmp(Token,"library")==0) {strcpy(tokenType,"library"); return; }
    if (strcmp(Token,"linkage")==0) {strcpy(tokenType,"linkage"); return; }
    if (strcmp(Token,"literal")==0) {strcpy(tokenType,"literal"); return; }
    if (strcmp(Token,"loop")==0) {strcpy(tokenType,"loop"); return; }
    if (strcmp(Token,"map")==0) {strcpy(tokenType,"map"); return; }
    if (strcmp(Token,"mod")==0) {strcpy(tokenType,"mod"); return; }
    if (strcmp(Token,"nand")==0) {strcpy(tokenType,"nand"); return; }
    if (strcmp(Token,"natural")==0) {strcpy(tokenType,"natural"); return; }
    if (strcmp(Token,"neq")==0) {strcpy(tokenType,"neq"); return; }
    if (strcmp(Token,"new")==0) {strcpy(tokenType,"new"); return; }
    if (strcmp(Token,"next")==0) {strcpy(tokenType,"next"); return; }
    if (strcmp(Token,"nor")==0) {strcpy(tokenType,"nor"); return; }
    if (strcmp(Token,"not")==0) {strcpy(tokenType,"not"); return; }
    if (strcmp(Token,"null")==0) {strcpy(tokenType,"null"); return; }
    if (strcmp(Token,"of")==0) {strcpy(tokenType,"of"); return; }
    if (strcmp(Token,"on")==0) {strcpy(tokenType,"on"); return; }
    if (strcmp(Token,"openevent")==0) {strcpy(tokenType,"openevent"); return; }
    if (strcmp(Token,"or")==0) {strcpy(tokenType,"or"); return; }
    if (strcmp(Token,"others")==0) {strcpy(tokenType,"others"); return; }
    if (strcmp(Token,"out")==0) {strcpy(tokenType,"out"); return; }
    if (strcmp(Token,"package")==0) {strcpy(tokenType,"package"); return; }
    if (strcmp(Token,"port")==0) {strcpy(tokenType,"port"); return; }
    if (strcmp(Token,"power")==0) {strcpy(tokenType,"power"); return; }
    if (strcmp(Token,"procedure")==0) {strcpy(tokenType,"procedure"); return; }
    if (strcmp(Token,"process")==0) {strcpy(tokenType,"process"); return; }
    if (strcmp(Token,"pure")==0) {strcpy(tokenType,"pure"); return; }
    if (strcmp(Token,"range")==0) {strcpy(tokenType,"range"); return; }
    if (strcmp(Token,"record")==0) {strcpy(tokenType,"record"); return; }
    if (strcmp(Token,"reject")==0) {strcpy(tokenType,"reject"); return; }
    if (strcmp(Token,"report")==0) {strcpy(tokenType,"report"); return; }
    if (strcmp(Token,"return")==0) {strcpy(tokenType,"return"); return; }
    if (strcmp(Token,"select")==0) {strcpy(tokenType,"select"); return; }
    if (strcmp(Token,"shared")==0) {strcpy(tokenType,"shared"); return; }
    if (strcmp(Token,"signal")==0) {strcpy(tokenType,"signal"); return; }
    if (strcmp(Token,"srl")==0) {strcpy(tokenType,"srl"); return; }
    if (strcmp(Token,"string")==0) {strcpy(tokenType,"string"); return; }
    if (strcmp(Token,"structural")==0) {strcpy(tokenType,"structural"); return; }
    if (strcmp(Token,"subtype")==0) {strcpy(tokenType,"subtype"); return; }
    if (strcmp(Token,"then")==0) {strcpy(tokenType,"then"); return; }
    if (strcmp(Token,"tick")==0) {strcpy(tokenType,"tick"); return; }
    if (strcmp(Token,"timeunit")==0) {strcpy(tokenType,"timeunit"); return; }
    if (strcmp(Token,"to")==0) {strcpy(tokenType,"to"); return; }
    if (strcmp(Token,"to")==0) {strcpy(tokenType,"to"); return; }
    if (strcmp(Token,"token")==0) {strcpy(tokenType,"token"); return; }
    if (strcmp(Token,"transport")==0) {strcpy(tokenType,"transport"); return; }
    if (strcmp(Token,"type")==0) {strcpy(tokenType,"type"); return; }
    if (strcmp(Token,"until")==0) {strcpy(tokenType,"until"); return; }
    if (strcmp(Token,"use")==0) {strcpy(tokenType,"use"); return; }
    if (strcmp(Token,"variable")==0) {strcpy(tokenType,"variable"); return; }
    if (strcmp(Token,"wait")==0) {strcpy(tokenType,"wait"); return; }
    if (strcmp(Token,"when")==0) {strcpy(tokenType,"when"); return; }
    if (strcmp(Token,"while")==0) {strcpy(tokenType,"while"); return; }
    if (strcmp(Token,"with")==0) {strcpy(tokenType,"with"); return; }
    if (strcmp(Token,"xor")==0) {strcpy(tokenType,"xor"); return; }
    if (strcmp(Token,"std_logic_vector")==0) {strcpy(tokenType,"Types"); return; }
    if (strcmp(Token,"std_logic")==0) {strcpy(tokenType,"Types"); return; }
    if (strcmp(Token,"integer")==0) {strcpy(tokenType,"Types"); return; }
    if (strcmp(Token,"bit_vector")==0) {strcpy(tokenType,"Types"); return; }
}
void doubleNames(char *Token,char *tokenType){
    if (strcmp(Token,"!=")==0) {strcpy(tokenType,"Neq"); return; }
    if (strcmp(Token,"!^")==0) {strcpy(tokenType,"xnor"); return; }
    if (strcmp(Token,"&&")==0) {strcpy(tokenType,"and_and"); return; }
    if (strcmp(Token,"+:")==0) {strcpy(tokenType,"plus_range"); return; }
    if (strcmp(Token,"-:")==0) {strcpy(tokenType,"minus_range"); return; }
    if (strcmp(Token,"->")==0) {strcpy(tokenType,"emit"); return; }
    if (strcmp(Token,"/=")==0) {strcpy(tokenType,"Neq"); return; }
    if (strcmp(Token,":=")==0) {strcpy(tokenType,"Cassign"); return; }
    if (strcmp(Token,"<<")==0) {strcpy(tokenType,"shift_left"); return; }
    if (strcmp(Token,"<=")==0) {strcpy(tokenType,"Assign"); return; }
    if (strcmp(Token,"<>")==0) {strcpy(tokenType,"sm_gr"); return; }
    if (strcmp(Token,"==")==0) {strcpy(tokenType,"eq_eq"); return; }
    if (strcmp(Token,"=>")==0) {strcpy(tokenType,"Arrow"); return; }
    if (strcmp(Token,">=")==0) {strcpy(tokenType,"gr_eq"); return; }
    if (strcmp(Token,">>")==0) {strcpy(tokenType,"shift_right"); return; }
    if (strcmp(Token,"||")==0) {strcpy(tokenType,"or_or"); return; }
}
int joinable(char *typeA, char *typeB){
     return 0;
}
