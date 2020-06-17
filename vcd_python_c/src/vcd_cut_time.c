
#include <stdlib.h>
#include "stdio.h"
#include "strings.h"
#include "ctype.h"
#include "string.h"

char HELP[] = "vcd_trim_time <VCDFILENAME> -start 222 -end 44444";

#define longestVal  200000

void do_help() { printf("%s\n",HELP); return; }
void readfile(char *fname);

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
                  end_time=atoi(option);
                  k++;
            } else if (fname1[0]==0) strcpy(fname1,option);
        }
    }

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

    j = (char *) 1;
    while ((j != NULL)&&(inf!=NULL)) {
        j = fgets(line, longestVal, inf);

        if (j==NULL) {
            printf("exit on EOF lnum=%d\n",linenum);
            exit(0);
        }
        linenum ++;
        if ((linenum % 100000)==0) {
            printf(" state=%d lnum=%d %f\n",state,linenum,now);
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
                    fprintf(Fout,"%s",line);
                    state = 1;
                }
            }
        }
    }
}














