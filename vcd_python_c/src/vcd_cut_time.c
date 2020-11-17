
#include <stdlib.h>
#include "stdio.h"
#include "strings.h"
#include "ctype.h"
#include "string.h"

char HELP[] = "vcd_trim_time <VCDFILENAME> -start 222 -end 44444";

#define longestVal  200000

void do_help() { printf("%s\n",HELP); return; }
void readfile(char *fname);

int intcode(char *st);
void codeint(int Ind);
char codeintstr[30];


#define maxsig 7000000

int psig=1;
typedef struct SIG {
    char value[1024];
} change_sig;

change_sig sigs[maxsig];

int debug = 0;
int linenum = 0;
int dones = 0;
double start_time =0.0;
double end_time =0.0;
double now = 0.0;
char fname1[500];
int main(argc, argv)
    int             argc;
    char           *argv[];

{
    char option[100];
    fname1[0] = 0;
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
        }
    }
    for (int i=0;i<maxsig;i++) { sigs[i].value[0]=0;}
    readfile(fname1);
}

void readfile(fname) char *fname; {


    FILE *inf;
    FILE *Fout;
    inf = fopen(fname, "r");
    Fout = fopen("cut.vcd","w");

   if (inf==NULL) {
        printf("error: cannot open input file %s\n",fname);
        exit(2);
    }
    int i,x;
    char *j;
    char line[longestVal];
    int searchEnd = 0;

    int state=0;
    double Perc;
    j = (char *) 1;
    while ((j != NULL)&&(inf!=NULL)) {
        j = fgets(line, longestVal, inf);

        if (j==NULL) {
            printf("exit on EOF lnum=%d\n",linenum);
            exit(0);
        }
        linenum ++;
        if ((linenum % 50000000)==0) {
            if (end_time>0) {
                Perc = ((100.0 * now)/end_time);
            } else {
                Perc = 0.0;
            }
            printf(" state=%d lnum=%d %f    %f     %f\n",state,linenum,now,end_time,Perc);
        }
        if (state==0) {
            fprintf(Fout,"%s",line);
            if (line[0]=='#') {
                now = atof(&(line[1]));                
                if (now>=start_time) {
                    state = 1;
                    printf("state1 lnum=%d %f\n",linenum,now);
                } else {
                    state = 2;
                    printf("state2 lnum=%d %f\n",linenum,now);
                }
            }
        } else if (state==1) {
            fprintf(Fout,"%s",line);
            if (line[0]=='#') {
                now = atof(&(line[1]));                
                if ((now>=end_time)&&(end_time>start_time)) {
                    printf("exit on endtime lnum=%d %f\n",linenum,now);
                    fclose(Fout);
                    exit(0);
                }
            }
        } else if (state==2) {
            if (line[0]=='#') {
                now = atof(&(line[1]));                
                if (now>=start_time) {
                    printf("back to state1 lnum=%d %f\n",linenum,now);
                    for (int jj=0; jj<maxsig;jj++) {
                        if (sigs[jj].value[0] == 'b') {
                            codeint(jj);
                            fprintf(Fout,"%s %s\n",sigs[jj].value,codeintstr);

                        } else if (sigs[jj].value[0] == '0') {
                            codeint(jj);
                            fprintf(Fout,"%c%s\n",sigs[jj].value[0],codeintstr);
                        } else if (sigs[jj].value[0] == '1') {
                            codeint(jj);
                            fprintf(Fout,"%c%s\n",sigs[jj].value[0],codeintstr);
                        }
                    }
                    fprintf(Fout,"%s",line);
                    state = 1;
                }
            } else {
                int ll; ll= strlen(line);
                line[ll-1] = 0;
                if ((line[0]=='0')||(line[0]=='1')) {
                    int P = intcode(&line[1]);
                    line[1]=0;
                    strcpy(sigs[P].value,line);
                } else if (line[0]=='b') {
                    int xind;
                    for (xind=0;line[xind]!=' ';xind++);
                    line[xind] = 0;
                    int P = intcode(&line[xind+1]);
                    strcpy(sigs[P].value,line);
                }
            }
        }
    }
}






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



void codeint(int Ind) {
    int pp;  
    int pos = 1; 
    int xx = (Ind % 94); 
    Ind = Ind / 94;  
    codeintstr[0] = xx + '!'; 
    codeintstr[1] = 0; 
    while (Ind!=0) {
        xx = (Ind % 94)-1;
        Ind = Ind / 94;  
        codeintstr[pos] = xx + '!'; 
        pos++;
    }    
    codeintstr[pos] = 0; 
}













