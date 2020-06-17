

#include <stdlib.h>
#include "stdio.h"
#include "strings.h"
#include "ctype.h"
#include <string.h>

// #include "qq64.h"

// char *strcat(char *dest, const char *src);
// size_t strlen(const char *s);


FILE *Fout;

void do_help() { return; }
void readVcdFile(char *fname);
void readFilterFile(char *fname);

int debug = 0;
int linenum = 0;
int dones = 0;
int qdones = 0;
double start_time = 0.0;
double end_time = -1.0;
char fname1[500];
char fname2[500];


#define maxsignals 100000000


int intcode(char *st) {
    int cur,i,res=0,machpil=1,more;
    for (i=0;(st[i]!=0)&&(st[i]!='\n');i++) {
        cur = (st[i]-' ');
        if ((cur>=0)&&(cur<=94)) {
            more = cur*machpil;
            res += more;
            machpil *= 94;
        }
    }
    return res-1;
}






int main(argc, argv)
    int             argc;
    char           *argv[];

{
    char option[100];
    fname1[0] = 0;
    fname2[0] = 0;
    if (argc <= 1) do_help();
    if (argc > 1) {
        for (int k = 2; k <= argc; k++) {
            strcpy(option, *++argv);
            if (strcmp(option,"-debug")==0) {
                debug=1;
            } else if (strcmp(option,"-help")==0) {
              do_help();
            } else if (strcmp(option,"-start")==0) {
                    strcpy(option, *++argv);
                  start_time=atof(option);
                  k++;
            } else if (strcmp(option,"-end")==0) {
                    strcpy(option, *++argv);
                  end_time=atof(option);
                  k++;
            } else if (fname1[0]==0) strcpy(fname1,option);
            else if (fname2[0]==0) strcpy(fname2,option);
        }
    }

    Fout = fopen("trimmed.vcd","w");
    readFilterFile(fname2);
    readVcdFile(fname1);
}


int usefuls[maxsignals];    



int startsWith(char *str,char *key) {
    int ii;
    for (ii=0;key[ii];ii++) {
        if (key[ii]!=str[ii]) return 0;
    }
    return 1;
}

char line0[1000];
char line1[1000];
char line2[1000];
char line3[1000];
char line4[1000];
char line5[1000];
char line6[1000];
char line7[1000];
char line8[1000];
char line9[1000];
char line10[1000];
char line11[1000];
char line12[1000];
char line13[1000];
char line14[1000];
char line15[1000];


void flush() {
    if (line15[0]) fprintf(Fout,"%s",line15);
    if (line14[0]) fprintf(Fout,"%s",line14);
    if (line13[0]) fprintf(Fout,"%s",line13);
    if (line12[0]) fprintf(Fout,"%s",line12);
    if (line11[0]) fprintf(Fout,"%s",line11);
    if (line10[0]) fprintf(Fout,"%s",line10);
    if (line9[0]) fprintf(Fout,"%s",line9);
    if (line8[0]) fprintf(Fout,"%s",line8);
    if (line7[0]) fprintf(Fout,"%s",line7);
    if (line6[0]) fprintf(Fout,"%s",line6);
    if (line5[0]) fprintf(Fout,"%s",line5);
    if (line4[0]) fprintf(Fout,"%s",line4);
    if (line3[0]) fprintf(Fout,"%s",line3);
    if (line2[0]) fprintf(Fout,"%s",line2);
    if (line1[0]) fprintf(Fout,"%s",line1);
    if (line0[0]) fprintf(Fout,"%s",line0);
    line0[0]=0;
    line1[0]=0;
    line2[0]=0;
    line3[0]=0;
    line4[0]=0;
    line5[0]=0;
    line6[0]=0;
    line7[0]=0;
    line8[0]=0;
    line9[0]=0;
    line10[0]=0;
    line11[0]=0;
    line12[0]=0;
    line13[0]=0;
    line14[0]=0;
    line15[0]=0;
//    fprintf(Fout,"flush\n");
}
int depth=0;
void pushline(char *line) {
    depth += 1;
    if (line15[0]) {
        printf("overflow %s",line15);
        exit(0);
    }

    strcpy(line15,line14);
    strcpy(line14,line13);
    strcpy(line13,line12);
    strcpy(line12,line11);
    strcpy(line11,line10);
    strcpy(line10,line9);
    strcpy(line9,line8);
    strcpy(line8,line7);
    strcpy(line7,line6);
    strcpy(line6,line5);
    strcpy(line5,line4);
    strcpy(line4,line3);
    strcpy(line3,line2);
    strcpy(line2,line1);
    strcpy(line1,line0);
    strcpy(line0,line);
}

void popline() {
    depth -= 1;
    strcpy(line0,line1);
    strcpy(line1,line2);
    strcpy(line2,line3);
    strcpy(line3,line4);
    strcpy(line4,line5);
    strcpy(line5,line6);
    strcpy(line6,line7);
    strcpy(line7,line8);
    strcpy(line8,line9);
    strcpy(line9,line10);
    strcpy(line10,line11);
    strcpy(line11,line12);
    strcpy(line12,line13);
    strcpy(line13,line14);
    strcpy(line14,line15);

    line15[0]=0;
}


void push(char *line,int Mode) {
    if (Mode==0) {
        flush();
        fprintf(Fout,"%s",line);
        return;
    }
    if (Mode==7) {
        flush();
        fprintf(Fout,"%s",line);
        return;
    }
    if (Mode==8) {
        flush();
        fprintf(Fout,"%s",line);
        return;
    }
    if (Mode==9) {
        flush();
        fprintf(Fout,"%s",line);
        return;
    }
    if (Mode==1) {
        if ((line[0]=='#')&&(line0[0]=='#')) {
            strcpy(line0,line);
        } else {
            strcpy(line0,line);
        }
        return;
    }
    if (Mode==2) {
        pushline(line);
//        fprintf(Fout,"%d [%d %d %d %d] pushline %s",depth,strlen(line3),strlen(line2),strlen(line1),strlen(line0),line);
        return;
    }

    if (Mode==3) {
        if (startsWith(line0,"$scope")) {
            popline();
//            fprintf(Fout,"%d [%d %d %d %d] popline %s",depth,strlen(line3),strlen(line2),strlen(line1),strlen(line0),line);
        } else {
//            fprintf(Fout,"realline %d %d %s",depth,strlen(line0),line);
            fprintf(Fout,"%s",line);
        }
        return;
    }
}


#define longestVal  200000
void readVcdFile(fname) char *fname; {

    char s1[longestVal];
    char s2[longestVal];
    char s3[10000];
    char s4[10000];
    char s5[10000];
    char s6[10000];
    char s7[10000];


    FILE *inf;
    inf = fopen(fname, "r");

   if (inf==NULL) {
        printf("error: cannot open input file %s\n",fname);
        exit(2);
    }
    int i,x,Code;
    char *j;
    char line[longestVal];
    int searchEnd = 0;
    j = (char *) 1;
    int switched = 0;
    double Time;
    while ((j != NULL)&&(inf!=NULL)) {
        j = fgets(line, longestVal, inf);

        if (j==NULL) {
            fclose(Fout);
            printf("exit on EOF\n");
            exit(0);
        }

        i=sscanf(line,"%s %s %s %s %s %s %s",s1,s2,s3,s4,s5,s6,s7);
        linenum ++;
        if ((linenum % 50000000)==0) {
            printf("line=%d mil now=%f\n",linenum/1000000,(Time/1000.0));
        }
        
        if (i>0) {
            if (switched) {
                if (line[0]=='#')  {
                    Time = atof(&line[1]);
                    if ((Time>=end_time)&&(end_time>0)) {
                        printf("exit on end_time\n");
                        fclose(Fout);
                        exit(0);
                    }
                    push(line,1);
                } else if ((line[0]=='b')||(line[0]=='r'))  {
                    Code = intcode(s2);
                    if (usefuls[Code]) {
                        push(line,8);
                    }
                } else if ((line[0]=='z')||(line[0]=='x')||(line[0]=='0')||(line[0]=='1'))  {
                    Code = intcode(&(s1[1]));
                    if (usefuls[Code]) {
//                        printf("code %d %s         %s",Code,s1,line);
                        push(line,9);
                    }
                }
            } else if (line[0]=='$')  {
                if (startsWith(line,"$scope")) {
                    push(line,2);
                } else if (startsWith(line,"$upscope")) {
                    push(line,3);
                } else if (strcmp(s1,"$var")==0) {
                    Code = intcode(s4);
                    if (usefuls[Code]) {
                        push(line,0);
                    }
                } else if (strcmp(s1,"$enddefinitions")==0) {
                    push(line,0);
                    switched=1;
                    printf("switched\n");
                } else {
                    push(line,0);
                }
            } else {
                push(line,7);
            }
        }
    }
}

    
void readFilterFile(char *fname) {

    char s1[longestVal];
    char s2[longestVal];
    char s3[10000];
    char s4[10000];
    char s5[10000];
    char s6[10000];
    char s7[10000];


    FILE *inf;
    inf = fopen(fname, "r");

   if (inf==NULL) {
        printf("error: cannot open input file %s\n",fname);
        exit(2);
    }
    int i,x,Code;
    char *j;
    char line[longestVal];
    int dones = 0;
    for (i=0;i<maxsignals;i++) {
        usefuls[i]=0;
    }
    j = (char *) 1;
    while ((j != NULL)&&(inf!=NULL)) {
        j = fgets(line, longestVal, inf);

        if (j==NULL) {
            printf("usefuls %d\n",dones);
            return;
        }

        i=sscanf(line,"%s %s %s %s %s %s %s",s1,s2,s3,s4,s5,s6,s7);
        linenum ++;

        if ((i==4)&&((strcmp(s1,"reg")==0)||(strcmp(s1,"record")==0))) {
            Code = intcode(s3);
            if (Code>=maxsignals) {
                printf("fatal. too many signals (%d>=%d)\n",Code,maxsignals);
                exit(0);
            }
            usefuls[Code]=1;
//            printf("code %d useful %s    %s",Code,s3,line);
            dones ++;
        }
    }
}

    
    









