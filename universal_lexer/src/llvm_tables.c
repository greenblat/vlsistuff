
#include "stdio.h"
#include "string.h"
int in_string(char Chk, char *Again);
void action(char *act,char *tokentype,char Char) ;
int EOL_FLAG() { return 1;}
#define st_exlm 1
#define st_floating 2
#define st_func 3
#define st_gader 4
#define st_idle 5
#define st_number 6
#define st_string 7
#define st_token 8
#define st_var 9
char strx0[]=" \t \\";
char strx1[]="";
char strx2[]="%";
char strx3[]="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789_.-";
char strx4[]="-";
char strx5[]="0123456789";
char strx6[]=".";
char strx7[]="e";
char strx8[]="+";
char strx9[]="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM";
char strx10[]="@";
char strx11[]="#";
char strx12[]="!";
char strx13[]="\"";
char strx14[]="{";
char strx15[]="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789_";
char strx16[]="'";
char strx17[]="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789 \t \\-_.:=;*,}{()[]<>,\\/+";
char strx18[]=":=;*,}{()[]<>";
int State=st_idle;
void stepit(char Char,char Next) {
//    printf("state=%d char=|%c| next=|%c|\n",State,Char,Next);
    switch (State) {
    case st_exlm: {
        if (in_string(Char,strx3)&&in_string(Next,strx3)) {
              action("add","0",Char);
              State=st_exlm;
              return;
        }
        if (in_string(Char,strx3)&&in_string(Next,strx1)) {
              action("push","exlm",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_floating: {
        if (in_string(Char,strx6)&&in_string(Next,strx5)) {
              action("add","0",Char);
              State=st_floating;
              return;
        }
        if (in_string(Char,strx5)&&in_string(Next,strx5)) {
              action("add","0",Char);
              State=st_floating;
              return;
        }
        if (in_string(Char,strx5)&&in_string(Next,strx7)) {
              action("add","0",Char);
              State=st_floating;
              return;
        }
        if (in_string(Char,strx7)&&in_string(Next,strx8)) {
              action("add","0",Char);
              State=st_floating;
              return;
        }
        if (in_string(Char,strx8)&&in_string(Next,strx5)) {
              action("add","0",Char);
              State=st_floating;
              return;
        }
        if (in_string(Char,strx5)&&in_string(Next,strx1)) {
              action("push","floating",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_func: {
        if (in_string(Char,strx3)&&in_string(Next,strx3)) {
              action("add","0",Char);
              State=st_func;
              return;
        }
        if (in_string(Char,strx3)&&in_string(Next,strx1)) {
              action("push","func",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_gader: {
        if (in_string(Char,strx5)&&in_string(Next,strx5)) {
              action("add","0",Char);
              State=st_gader;
              return;
        }
        if (in_string(Char,strx5)&&in_string(Next,strx1)) {
              action("push","gader",Char);
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
        if (in_string(Char,strx2)&&in_string(Next,strx3)) {
              action("add","0",Char);
              State=st_var;
              return;
        }
        if (in_string(Char,strx4)&&in_string(Next,strx5)) {
              action("add","0",Char);
              State=st_number;
              return;
        }
        if (in_string(Char,strx5)&&in_string(Next,strx5)) {
              action("add","0",Char);
              State=st_number;
              return;
        }
        if (in_string(Char,strx5)&&in_string(Next,strx6)) {
              action("add","0",Char);
              State=st_floating;
              return;
        }
        if (in_string(Char,strx5)&&in_string(Next,strx1)) {
              action("push","number",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx3)&&in_string(Next,strx3)) {
              action("add","0",Char);
              State=st_token;
              return;
        }
        if (in_string(Char,strx9)&&in_string(Next,strx1)) {
              action("push","token",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx10)&&in_string(Next,strx9)) {
              action("add","0",Char);
              State=st_func;
              return;
        }
        if (in_string(Char,strx11)&&in_string(Next,strx5)) {
              action("add","0",Char);
              State=st_gader;
              return;
        }
        if (in_string(Char,strx12)&&in_string(Next,strx13)) {
              action("push","meta",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx12)&&in_string(Next,strx14)) {
              action("push","meta",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx12)&&in_string(Next,strx15)) {
              action("add","0",Char);
              State=st_exlm;
              return;
        }
        if (in_string(Char,strx13)&&in_string(Next,strx1)) {
              action("add","0",Char);
              State=st_string;
              return;
        }
        if (in_string(Char,strx16)&&in_string(Next,strx1)) {
              action("add","0",Char);
              State=st_string;
              return;
        }
        if (in_string(Char,strx18)&&in_string(Next,strx1)) {
              action("push","single",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_number: {
        if (in_string(Char,strx5)&&in_string(Next,strx5)) {
              action("add","0",Char);
              State=st_number;
              return;
        }
        if (in_string(Char,strx5)&&in_string(Next,strx6)) {
              action("add","0",Char);
              State=st_floating;
              return;
        }
        if (in_string(Char,strx5)&&in_string(Next,strx1)) {
              action("push","number",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_string: {
        if (in_string(Char,strx17)&&in_string(Next,strx1)) {
              action("add","0",Char);
              State=st_string;
              return;
        }
        if (in_string(Char,strx13)&&in_string(Next,strx1)) {
              action("push","string",Char);
              State=st_idle;
              return;
        }
        if (in_string(Char,strx16)&&in_string(Next,strx1)) {
              action("push","string",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_token: {
        if (in_string(Char,strx3)&&in_string(Next,strx3)) {
              action("add","0",Char);
              State=st_token;
              return;
        }
        if (in_string(Char,strx3)&&in_string(Next,strx1)) {
              action("push","token",Char);
              State=st_idle;
              return;
        }
    } break;
    case st_var: {
        if (in_string(Char,strx3)&&in_string(Next,strx3)) {
              action("add","0",Char);
              State=st_var;
              return;
        }
        if (in_string(Char,strx3)&&in_string(Next,strx1)) {
              action("push","var",Char);
              State=st_idle;
              return;
        }
    } break;
    }
    printf("no action!!!! |%x| <%c> |%x| <%c> state=%d \n",Char,Char,Next,Next,State);
}
void reserved_words(char *Token,char *tokenType){
    if (strcmp(Token,"Attrs")==0) {strcpy(tokenType,"Attrs"); return; }
    if (strcmp(Token,"Function")==0) {strcpy(tokenType,"Function"); return; }
    if (strcmp(Token,"ModuleID")==0) {strcpy(tokenType,"ModuleID"); return; }
    if (strcmp(Token,"add")==0) {strcpy(tokenType,"add"); return; }
    if (strcmp(Token,"align")==0) {strcpy(tokenType,"align"); return; }
    if (strcmp(Token,"alloca")==0) {strcpy(tokenType,"alloca"); return; }
    if (strcmp(Token,"and")==0) {strcpy(tokenType,"and"); return; }
    if (strcmp(Token,"ashr")==0) {strcpy(tokenType,"ashr"); return; }
    if (strcmp(Token,"attributes")==0) {strcpy(tokenType,"attributes"); return; }
    if (strcmp(Token,"bitcast")==0) {strcpy(tokenType,"bitcast"); return; }
    if (strcmp(Token,"br")==0) {strcpy(tokenType,"br"); return; }
    if (strcmp(Token,"byval")==0) {strcpy(tokenType,"byval"); return; }
    if (strcmp(Token,"call")==0) {strcpy(tokenType,"call"); return; }
    if (strcmp(Token,"common")==0) {strcpy(tokenType,"common"); return; }
    if (strcmp(Token,"datalayout")==0) {strcpy(tokenType,"datalayout"); return; }
    if (strcmp(Token,"declare")==0) {strcpy(tokenType,"declare"); return; }
    if (strcmp(Token,"define")==0) {strcpy(tokenType,"define"); return; }
    if (strcmp(Token,"div")==0) {strcpy(tokenType,"div"); return; }
    if (strcmp(Token,"double")==0) {strcpy(tokenType,"double"); return; }
    if (strcmp(Token,"eq")==0) {strcpy(tokenType,"eq"); return; }
    if (strcmp(Token,"exact")==0) {strcpy(tokenType,"exact"); return; }
    if (strcmp(Token,"extractelement")==0) {strcpy(tokenType,"extractelement"); return; }
    if (strcmp(Token,"fadd")==0) {strcpy(tokenType,"fadd"); return; }
    if (strcmp(Token,"false")==0) {strcpy(tokenType,"false"); return; }
    if (strcmp(Token,"fcmp")==0) {strcpy(tokenType,"fcmp"); return; }
    if (strcmp(Token,"float")==0) {strcpy(tokenType,"float"); return; }
    if (strcmp(Token,"fmul")==0) {strcpy(tokenType,"fmul"); return; }
    if (strcmp(Token,"fptrunc")==0) {strcpy(tokenType,"fptrunc"); return; }
    if (strcmp(Token,"fsub")==0) {strcpy(tokenType,"fsub"); return; }
    if (strcmp(Token,"getelementptr")==0) {strcpy(tokenType,"getelementptr"); return; }
    if (strcmp(Token,"global")==0) {strcpy(tokenType,"global"); return; }
    if (strcmp(Token,"i1")==0) {strcpy(tokenType,"i1"); return; }
    if (strcmp(Token,"i16")==0) {strcpy(tokenType,"i16"); return; }
    if (strcmp(Token,"i32")==0) {strcpy(tokenType,"i32"); return; }
    if (strcmp(Token,"i64")==0) {strcpy(tokenType,"i64"); return; }
    if (strcmp(Token,"i8")==0) {strcpy(tokenType,"i8"); return; }
    if (strcmp(Token,"icmp")==0) {strcpy(tokenType,"icmp"); return; }
    if (strcmp(Token,"inbounds")==0) {strcpy(tokenType,"inbounds"); return; }
    if (strcmp(Token,"insertelement")==0) {strcpy(tokenType,"insertelement"); return; }
    if (strcmp(Token,"label")==0) {strcpy(tokenType,"label"); return; }
    if (strcmp(Token,"load")==0) {strcpy(tokenType,"load"); return; }
    if (strcmp(Token,"lshr")==0) {strcpy(tokenType,"lshr"); return; }
    if (strcmp(Token,"metadata")==0) {strcpy(tokenType,"metadata"); return; }
    if (strcmp(Token,"mul")==0) {strcpy(tokenType,"mul"); return; }
    if (strcmp(Token,"ne")==0) {strcpy(tokenType,"ne"); return; }
    if (strcmp(Token,"nocapture")==0) {strcpy(tokenType,"nocapture"); return; }
    if (strcmp(Token,"nounwind")==0) {strcpy(tokenType,"nounwind"); return; }
    if (strcmp(Token,"nsw")==0) {strcpy(tokenType,"nsw"); return; }
    if (strcmp(Token,"null")==0) {strcpy(tokenType,"null"); return; }
    if (strcmp(Token,"nuw")==0) {strcpy(tokenType,"nuw"); return; }
    if (strcmp(Token,"ogt")==0) {strcpy(tokenType,"ogt"); return; }
    if (strcmp(Token,"olt")==0) {strcpy(tokenType,"olt"); return; }
    if (strcmp(Token,"or")==0) {strcpy(tokenType,"or"); return; }
    if (strcmp(Token,"phi")==0) {strcpy(tokenType,"phi"); return; }
    if (strcmp(Token,"preds")==0) {strcpy(tokenType,"preds"); return; }
    if (strcmp(Token,"readnone")==0) {strcpy(tokenType,"readnone"); return; }
    if (strcmp(Token,"readonly")==0) {strcpy(tokenType,"readonly"); return; }
    if (strcmp(Token,"ret")==0) {strcpy(tokenType,"ret"); return; }
    if (strcmp(Token,"sdiv")==0) {strcpy(tokenType,"sdiv"); return; }
    if (strcmp(Token,"select")==0) {strcpy(tokenType,"select"); return; }
    if (strcmp(Token,"sext")==0) {strcpy(tokenType,"sext"); return; }
    if (strcmp(Token,"sgt")==0) {strcpy(tokenType,"sgt"); return; }
    if (strcmp(Token,"shl")==0) {strcpy(tokenType,"shl"); return; }
    if (strcmp(Token,"shl")==0) {strcpy(tokenType,"shl"); return; }
    if (strcmp(Token,"shufflevector")==0) {strcpy(tokenType,"shufflevector"); return; }
    if (strcmp(Token,"signext")==0) {strcpy(tokenType,"signext"); return; }
    if (strcmp(Token,"slt")==0) {strcpy(tokenType,"slt"); return; }
    if (strcmp(Token,"srem")==0) {strcpy(tokenType,"srem"); return; }
    if (strcmp(Token,"ssp")==0) {strcpy(tokenType,"ssp"); return; }
    if (strcmp(Token,"store")==0) {strcpy(tokenType,"store"); return; }
    if (strcmp(Token,"sub")==0) {strcpy(tokenType,"sub"); return; }
    if (strcmp(Token,"switch")==0) {strcpy(tokenType,"switch"); return; }
    if (strcmp(Token,"tail")==0) {strcpy(tokenType,"tail"); return; }
    if (strcmp(Token,"tail")==0) {strcpy(tokenType,"tail"); return; }
    if (strcmp(Token,"target")==0) {strcpy(tokenType,"target"); return; }
    if (strcmp(Token,"to")==0) {strcpy(tokenType,"to"); return; }
    if (strcmp(Token,"triple")==0) {strcpy(tokenType,"triple"); return; }
    if (strcmp(Token,"trunc")==0) {strcpy(tokenType,"trunc"); return; }
    if (strcmp(Token,"type")==0) {strcpy(tokenType,"type"); return; }
    if (strcmp(Token,"udiv")==0) {strcpy(tokenType,"udiv"); return; }
    if (strcmp(Token,"ugt")==0) {strcpy(tokenType,"ugt"); return; }
    if (strcmp(Token,"ult")==0) {strcpy(tokenType,"ult"); return; }
    if (strcmp(Token,"undef")==0) {strcpy(tokenType,"undef"); return; }
    if (strcmp(Token,"urem")==0) {strcpy(tokenType,"urem"); return; }
    if (strcmp(Token,"uwtable")==0) {strcpy(tokenType,"uwtable"); return; }
    if (strcmp(Token,"void")==0) {strcpy(tokenType,"void"); return; }
    if (strcmp(Token,"x")==0) {strcpy(tokenType,"x"); return; }
    if (strcmp(Token,"xor")==0) {strcpy(tokenType,"xor"); return; }
    if (strcmp(Token,"zeroext")==0) {strcpy(tokenType,"zeroext"); return; }
    if (strcmp(Token,"zeroinitializer")==0) {strcpy(tokenType,"zeroinitializer"); return; }
    if (strcmp(Token,"zext")==0) {strcpy(tokenType,"zext"); return; }
}
void doubleNames(char *Token,char *tokenType){
}
int joinable(char *typeA, char *typeB){
     return 0;
}
