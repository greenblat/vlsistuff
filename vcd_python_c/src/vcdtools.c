#include "stdio.h"
#include "ctype.h"
#define maxsig 500000
int best_block = 0;
double atof();
double speed_up=1.0;
int usb=1;
FILE *File;
FILE *Prologf = NULL;
#include "qq64.h"
int DoProlog = 0;
void put_tester();
void use_sigs_file();
void use_sigs_file2();
void record();
void do_value();
void pushtok();
void readfile();
void search_time();

char active_module_s[1000],active_sig_s[1000];
int active_module_dump,active_sig_dump,active_count_dump=0,active_count_run=0;
int onlys[100];
int ponly=0;
double activity_interval= -1.0;
double last_activity_dump= 0.0;
int activity_counter=0;
int tester_lines=0;
int dump_no_x=0;
int LASTCHANGE=0;
int search=0;
int phsh=0;
int linenum=0;
int debug=0;
int firstsig=0;
double start_time=0.0;
double end_time=0.0;
int maxusedsig=0;
int single=0;
int nowwidth=0;
int nowlow=0;
int nowhigh=0;
int current_block_ok=0;
int vsf=0;
int next_activity_also=0;

#define Idle 0
#define Wait_end 1
#define Scope 2
#define Var 3
#define Upscope 4
#define Dumpvars 5
#define Values 6
#define Enddef 7

int pgood=0;
int goods[2000];
int usedg[2000];
int widths[2000];
int minind[2000];

int iname[10000];
int imult=0,inews=0,piname=0;

FILE *inf;
FILE *vcdf2;
int state=Idle;
double run_time=0.0;
double previous_time=0.0;
int instate=0;
typedef struct NEXT {
	int name;
	int next;
	int path;
	int psig;
	int fpath;
} nexts;
int pnext=1;
#define maxpnext 300000

nexts nexta[maxpnext];


int psig=1;
typedef struct SIG {
	int block_ok;
	int name;
	int high,low;
	int orig;
	int width;
	int code;
	int ind;
	int sfok;
	int vsf0;
	int vsf1;
	int vsf2;
	int vsf3;
	int next;
	int path;
	int fpath;
	int activity;
	int activity0;
	int activity1;
	int lastchange;
	int monitor;
	int mini;
	char value;
} change_sig;

 change_sig sigs[maxsig];
									  


int monitors[1000];
int pmonitor=0;


main(argc, argv)
	int             argc;
	char           *argv[];

{
	int argvx;
	char            line[5000];
	char 			longline[5000];
	char           *j;
	int i,m,k;
    char hshinit[200],fname2[100];
	int             maxhash = 3000, stringlength = 8, maxchars = 12000000, maxtabs = 3, maxstrings = 3000;

	char option[100],fname1[100];
//  sprintf(hshinit, "maxchar=%d maxtabs=%d maxhash=%d strlen=%d", maxchars, maxtabs, maxhash, stringlength);
//  hsh_init(&phsh, hshinit);  /* qqai: string->integer ; qqia: integer back to string */
  alpha_init();

/* update hash table maxsize, if wanted */
	argvx = (int) argv;
    if (argc > 1)
             for (k = 2; k <= argc; k++) {
              strcpy(option, *++argv);
              if (strcmp(option,"-hc")==0) {
              		strcpy(option, *++argv);
					maxchars=atoi(option);
					k++;
				} else if (strcmp(option,"-m")==0) {
              		strcpy(option, *++argv);
					k++;
					monitors[pmonitor]=qqai(option);
					printf("add monitor1 %d %s\n",pmonitor,option);
					pmonitor++;
				}
			
			}

/* init hash table object */

/* usage of hash table, through qqai, qqia only */
/* respool args */
	argv = argvx;
	fname2[0]=0;
	for (i=0;i<maxsig;i++) { sigs[i].code=-1;sigs[i].next=0;} 
     if (argc <= 1) do_help();
     if (argc > 1)
              for (k = 2; k <= argc; k++) {
                  strcpy(option, *++argv);
                  if (strcmp(option,"-debug")==0) {
                      debug=1;
                  } else if (strcmp(option,"-help")==0) {
					do_help();
                  } else if (strcmp(option,"-start")==0) {
                  		strcpy(option, *++argv);
						start_time=atof(option);
						k++;
                  } else if (strcmp(option,"-m")==0) {
                  		strcpy(option, *++argv);
						k++;
                  } else if (strcmp(option,"-only")==0) {
                  		strcpy(option, *++argv);
						onlys[ponly]=qqai(option);
						ponly++;
						k++;
                  } else if (strcmp(option,"-block")==0) {
                  		strcpy(option, *++argv);
						k++;
						best_block = qqai(option);
                  } else if (strcmp(option,"-nox")==0) {
					dump_no_x = 1;
                  } else if (strcmp(option,"-next_activity_also")==0) {
					next_activity_also = 1;
                  } else if (strcmp(option,"-ok")==0) {
                  		strcpy(option, *++argv);
						k++;
						qqsa(qqai(option),-1);
                  } else if (strcmp(option,"-vsf")==0) {
                  		strcpy(option, *++argv);
						k++;
						vsf=1;
						read_sigs_file(option);
                  } else if (strcmp(option,"-prolog")==0) {
                  		strcpy(option, *++argv);
						k++;
						DoProlog = qqai(option);
                  } else if (strcmp(option,"-end")==0) {
                  		strcpy(option, *++argv);
						end_time=atoi(option);
						k++;
                  } else if (strcmp(option,"-speed")==0) {
                  		strcpy(option, *++argv);
						speed_up=atof(option);
						k++;
                  } else if (strcmp(option,"-activity_interval")==0) {
                  		strcpy(option, *++argv);
						activity_interval=atof(option);
						k++;
                  } else if (strcmp(option,"-activity")==0) {
                  		strcpy(option, *++argv);
						sscanf(option,"%s %s %d",active_module_s,active_sig_s,&active_count_dump);
						active_module_dump = qqai(active_module_s);
						active_sig_dump = qqai(active_sig_s);
						k++;
                  } else strcpy(fname1,option);
              }
	for (i=0;i<maxsig;i++) {
		sigs[i].sfok=0;
		sigs[i].vsf0=-1;
		sigs[i].vsf1=-1;
		sigs[i].vsf2=-1;
		sigs[i].vsf3=-1;
		sigs[i].value='x';
	}
		
	readfile(fname1);
	fclose(File);
	if (DoProlog) fclose(Prologf);
	report_activity();
	exit(0);
}

do_help() 
{
	printf("usage: vcdusb file -vsf 3signalfilename [options -help]\n");
	printf("-nox   = in vsf file (for tester) put zeroes instead of X values\n");
	printf("-activity Interval   = dump activity every interval\n");
	printf("-end_time   = quit at this time\n");
	printf("-block Block   = take vsf signals from this block\n");
	printf("-start_time   = flush data til start time\n");
	printf("-vsf file   = signal file for verilog_tester \n");
	printf("-speed (float)factor   = multiplies vcd times by this factor (1.0 by default)\n");
	printf(" three-signal file format:\n");
	printf(" on each line one signame\n");
	printf(" on first line the clock\n");
	printf(" on second line the positive\n");
	printf(" on third line the negative\n");
	exit(0);

}


void readfile(fname) 
char *fname;
{
	char *j;
	char line[1000];
	int i;
	int guard=0;
	char s1[10000];
	char s2[10000];
	char s3[10000];
	char s4[10000];
	char s5[10000];
	char s6[10000];
	char s7[10000];
	inf = fopen(fname, "r");
	if (DoProlog) {
		sprintf(line,"%s.plvcd",qqia(DoProlog));
		Prologf = fopen(line, "w");
	}
	if (inf==NULL) {
		printf("error: cannot open input file %s\n",fname);
		exit(2);
	}
	vcdf2 = fopen("vcdf2", "w");
	File = fopen("tester.rom", "w");
	do_starters();
	j = (char *) 1;
	while ((j != NULL)&&((end_time<=0)||(run_time<=end_time))&&(inf!=NULL)) {
		j = fgets(line, 4999, inf);
		linenum++;
		guard++;
		if (guard>9999) { guard=0;fprintf(stderr,"%d lines %g %d %d/%d %s\n",linenum,run_time,0,imult,inews,line);}
		if (j == NULL) {
			return;
		}
		i=sscanf(line,"%s %s %s %s %s %s %s",s1,s2,s3,s4,s5,s6,s7);
		switch (i) {
		case 7:
			pushtok(s1,1);
			pushtok(s2,2);
			pushtok(s3,3);
			pushtok(s4,4);
			pushtok(s5,5);
			pushtok(s6,6);
			pushtok(s7,7);
			break;
		case 6:
			pushtok(s1,1);
			pushtok(s2,2);
			pushtok(s3,3);
			pushtok(s4,4);
			pushtok(s5,5);
			pushtok(s6,6);
			break;
		case 5:
			pushtok(s1,1);
			pushtok(s2,2);
			pushtok(s3,3);
			pushtok(s4,4);
			pushtok(s5,5);
			break;
		case 4:
			pushtok(s1,1);
			pushtok(s2,2);
			pushtok(s3,3);
			pushtok(s4,4);
			break;
		case 3:
			pushtok(s1,1);
			pushtok(s2,2);
			pushtok(s3,3);
			break;
		case 2:
			pushtok(s1,1);
			pushtok(s2,2);
			break;
		case 1:
			pushtok(s1,1);
			break;
		}
	}
}

void pushtok(s,ind)
int ind;
char *s;
{
	int pr;
	int n;
	if ((ind==1)&&(s[0]=='#')) {
		run_time=speed_up*atof(&(s[1]));
		LASTCHANGE++;
		if ((run_time>=0)&&(run_time<start_time)&&(search)) search_time(start_time);
		if ((activity_interval>0)&&((run_time-last_activity_dump)>=activity_interval)) {
			last_activity_dump = run_time;
			report_mid_activity();
		}
		state=Values;
		return;
	}
	instate++;

	switch (state) {
	case Idle:
		n = qqai(s);
		instate=0;
		if (n==qqai("$scope")) state=Scope;
		else if (n==qqai("$var")) state=Var;
		else if (n==qqai("$upscope")) state=Upscope;
		else if (n==qqai("$enddefinitions")) state=Enddef;
		else if (n==qqai("$dumpvars")) { 
			state=Dumpvars;
			search=1;
		} else if (s[0]=='#') {
			state=Values;
			do_value(s);
		} else { 
			printf("idle token %s\n",s);
		}
		check_x(1);
		break;
	case Values: do_value(s);check_x(2);break;
	case Scope: n=qqai(s);do_scope(n);check_x(3);break;			
	case Var: n=qqai(s);do_var(n);check_x(4);break;			
	case Upscope: n=qqai(s);do_upscope(n);check_x(5);break;			
	case Enddef: n=qqai(s);do_enddefinitions(n);check_x(6);break;			
	case Dumpvars: do_dumpvars(s);check_x(7);break;			
	}

}
check_x(i)
int i;
{
	if (inf==NULL) {
		printf("check %d found\n",i);
	}
}

char wide_value_s[1000];
int  wide_state=0;
int  real_state=0;




void do_value(s)
char *s;
{
	char temp[10000];
	char value;
	int sig,pr,nexti;
	int high,low,j;


	strcpy(temp,s);
	if (strlen(temp)>256) temp[256]=0;;
	if (real_state) {
		real_state=0;
		return;
	}
	if (wide_state) {
		wide_state=0;
		sig = intcode(temp);
		if (sig>=maxsig) {
			printf("Error! sig %d >=maxsig %d\n",sig,maxsig);
			wide_state=0;
			return;
		}
		if (sigs[sig].lastchange!=LASTCHANGE) {
			(sigs[sig].activity)++;
			(sigs[sig].activity0)++;
			(sigs[sig].activity1)++;
			sigs[sig].lastchange=LASTCHANGE;
		}
		high = sigs[sig].high;
		low = sigs[sig].low;
		if (sigs[sig].monitor) {
			printf(">>mon1: %d %s %s\n",(int)run_time,qqia(sigs[sig].name),wide_value_s);
		}
		if (may_print(sig)) {
			if (high>low) for (j=high;j>=low;j--) {
				sprintf(temp,"%s[%d]",qqia(sigs[sig].name),j);
				put_tester(wide_value_s[high-j],sigs[sig].vsf0+j-low,temp,0);
			} else if (low>high) for (j=low;j>=high;j++) {
				sprintf(temp,"%s[%d]",qqia(sigs[sig].name),j);
				put_tester(wide_value_s[high-j],sigs[sig].vsf0+j-low,temp,0);
			}
				
			}
		return;
	}
	if ((run_time<start_time)&&(search)) { 
		search_time(start_time);
		return;
	}
	if (temp[0]=='$') { 
	} else if (temp[0]=='#') { 
		LASTCHANGE++;
		run_time=speed_up*atof(&(temp[1]));
		if ((activity_interval>0)&&((run_time-last_activity_dump)>=activity_interval)) {
			last_activity_dump = run_time;
			report_mid_activity();
		}
	} else {
		value=temp[0];

		if (value=='r') {
			real_state=1;
			strcpy(wide_value_s,&(temp[1]));
			return;
		} else if (value=='b') {
			wide_state=1;
			strcpy(wide_value_s,&(temp[1]));
			return;
		} else {
			sig = intcode(&(temp[1]));
			if ((sig<0)||(sig>=maxsig)) {
				printf("ilia sig,maxsig %d,%d warning, %s\n",sig,maxsig,temp);
				return;
			}
			if (DoProlog) {
				fprintf(Prologf,"change_%s(%d,'%s','%s',%c).\n",qqia(DoProlog),(int)run_time,qqia(sigs[sig].name),qqia(sigs[sig].fpath),value);
			} 
			if (sigs[sig].monitor) {
				printf("mon1(%d,'%s',%c).\n",(int)run_time,qqia(sigs[sig].name),value);
			}
			sigs[sig].value=value;
			if (sigs[sig].lastchange!=LASTCHANGE) {
				(sigs[sig].activity)++;
				(sigs[sig].activity0)++;
				(sigs[sig].activity1)++;
				sigs[sig].lastchange=LASTCHANGE;
				if ((active_count_dump) &&(sigs[sig].name==active_sig_dump)&&(sigs[sig].path==active_module_dump)) {
					active_count_run++;
					if (active_count_run>=active_count_dump) {
						active_count_run=0;
						report_mid_activity();
					}
				}
			}

			if ((vsf)&&(pgood>0)) {
				if (may_print(sig)) {
					fprintf(vcdf2,"%c%x\n",temp[0],sigs[sig].vsf0);
					put_tester(temp[0],sigs[sig].vsf0,qqia(sigs[sig].name),sigs[sig].monitor);
					put_tester(temp[0],sigs[sig].vsf1,qqia(sigs[sig].name),sigs[sig].monitor);
					put_tester(temp[0],sigs[sig].vsf2,qqia(sigs[sig].name),sigs[sig].monitor);
					put_tester(temp[0],sigs[sig].vsf3,qqia(sigs[sig].name),sigs[sig].monitor);
				}
			} 
		}
	}
}



may_print(int sig)
{
	if (sigs[sig].code==-1) return 0;
	if (sigs[sig].sfok==0) return 0;
	return 1;
}
do_dumpvars(s) 
char *s;
{ 
	if (strcmp(s,"$end")==0) {
		state=Values;
		search=1;
	} else {
		run_time=0.0;
		LASTCHANGE=0;
		do_value(s);
	}
}
do_scope(n)
int n;
{
	if (n==qqai("$end")) state=Idle;
	else if (instate==2)  {
		pushscope(n);
	}
}

do_upscope(n) int n;{
	if (instate==1) popscope();
	if (n==qqai("$end")) state=Idle;
}
do_enddefinitions(n) int n;{
	if (n==qqai("$end")) { 
		state=Idle;
		run_monitors();
		use_sigs_file();
		printf("maxusedsig %d/%d\n",maxusedsig,maxsig);
	}
}


int code,bus;
char temp[1000];
char temp2[1000];

do_var(n) int n;
{
	switch (instate) {
		case 1:
			if (
			 	  (n==qqai("parameter"))
				||(n==qqai("wire"))
				||(n==qqai("wand"))
				||(n==qqai("tri"))
				||(n==qqai("tri0"))
				||(n==qqai("tri1"))
				||(n==qqai("reg"))
				||(n==qqai("trireg"))
				||(n==qqai("supply1"))
				||(n==qqai("supply0"))
				||(n==qqai("real"))
				||(n==qqai("integer"))
				||(n==qqai("event"))
			) break;
			shouldbe("wire",n); break;
		case 2:
			nowwidth=atoi(qqia(n));
			break;
		case 3:
			code=n; break;
		case 4:
			bus=n; break;
		case 5:
			if (n==qqai("$end")) { state=Idle;record(code,bus);}
			else {
				if (n==qqai("[-1]")) {
					record(code,bus);
				} else {
					strcpy(temp,qqia(n));
					if (temp[0]=='[') {
						int j;
						for (j=1;(temp[j]&&(temp[j]!=':'));j++);
						if (temp[j-1]==']') {
							sprintf(temp,"%s%s",qqia(bus),qqia(n));
							record(code,qqai(temp));
						} else if (temp[j]==':') {
							strcpy(temp2,&(temp[1]));
							temp2[j-1]=0;
							nowhigh = atoi(temp2);
							strcpy(temp2,&(temp[j+1]));
							temp2[strlen(temp2)-1]=0;
							nowlow = atoi(temp2);
							record(code,bus);
						}
					}
				}
			}
		case 6:
			state=Idle;
			break;
	}
}

shouldbe(st,n)
 char *st;
 int n;
 {
	if (n!=qqai(st)) {
		fprintf(stderr,"line %d syntax error expected %s got %s\n",linenum,st,qqia(n));
	}
}



int pscope=0,scopes[100];

pushscope(n)
int n;
{
	scopes[pscope++]=n;
	current_block_ok=block_ok(n)||(pgood>0);
}
popscope(n)
int n;
{
	pscope--;
	current_block_ok=0;
}
getscope(temp)
char *temp;
{
	int i;
	temp[0]=0;
	for (i=0;i<pscope;i++) {
		strcat(temp,qqia(scopes[i]));
		strcat(temp,".");
	}
	temp[strlen(temp)-1]=0;
	return qqai(temp);
}
void record(code,bus)
int code,bus;
{
	char temp[1000];
	char temp2[1000];
	int ind,i,pcode;
/*	if (!current_block_ok) return 0; */
	psig = intcode(qqia(code));
	if (psig>=maxsig) {
		printf("sigs code is larger then array, recompile (%s,%s,%d)\n",qqia(bus),qqia(code),psig);
		return;
	}
	if (psig>maxusedsig)
		maxusedsig = psig;

	if (sigs[psig].code!= -1)  {
		nexta[pnext].name=bus;
		nexta[pnext].psig=psig;
		nexta[pnext].path=scopes[pscope-1];
		nexta[pnext].fpath=getscope(temp);
		nexta[pnext].next=sigs[psig].next;
		sigs[psig].next=pnext;
/*		printf(">>record_next %s %d %d %s %s\n",qqia(bus),psig,pnext,qqia(code),qqia(nexta[pnext].path));  */
		pnext++;
		if (pnext>maxpnext) {
			printf("pnext code is larger then array, recompile (%s,%s,%d)\n",qqia(bus),qqia(code),psig);
		}
	} else {
		sigs[psig].next=0;
		sigs[psig].name=bus;
		sigs[psig].orig=bus;
		sigs[psig].monitor=0;
		sigs[psig].code=code;
		sigs[psig].width=nowwidth;
		sigs[psig].high=nowhigh;
		sigs[psig].low=nowlow;
		sigs[psig].activity=0;
		sigs[psig].activity0=0;
		sigs[psig].activity1=0;
		sigs[psig].lastchange=0;
		sigs[psig].path=scopes[pscope-1];
		sigs[psig].fpath=getscope(temp);
		qqsa(code,psig);
/*		printf(">>record %s %d %s %s\n",qqia(bus),psig,qqia(code),qqia(sigs[psig].path));  */
	}
}





block_ok(n)
int n;
{
	int i;
	i=qqas(n);
	return (i<0)||((i>0)&&(sigs[i].block_ok));
}
do_starters()
{
    return;
}


void search_time(start_time) int start_time;
{
	char *j;
	char line[1000];
	int nexti,sig,i;
	j = (char *) 1;
	while (j != NULL) {
		j = fgets(line, 4999, inf);
		linenum++;
		if (!(linenum&0x3fff)) fprintf(stderr,"%d lines t= %g %s %d\n",linenum,run_time,line,(int)j);
		if (line[0]=='$') {
		} else if (line[0]=='#') {
			run_time=speed_up*atof(&(line[1]));
			if (run_time>=start_time) {
				if (vsf) {
					fprintf(vcdf2,"$dumpvars\n");
					for (i=0;i<maxsig;i++) { 
						sig=i;
						if (may_print(i)) {	
							fprintf(vcdf2,"%c%x\n",sigs[i].value,sigs[i].vsf0);
						}
					}
					fprintf(vcdf2,"$end\n");
				}
				state=Values;
				return;
			}
		} else {
			sig = intcode(&(line[1]));
			if ((sig>0)&&(sig<=maxsig))
				sigs[sig].value=line[0];
		}
	}
}


intcode(st) 
char *st;
{
	int cur,i,res=0,machpil=1,more;
	for (i=0;(st[i]!=0)&&(st[i]!='\n');i++) {
		cur = (1+st[i]-'!');
		if ((cur>=0)&&(cur<=94)) {
			more = cur*machpil;
			res += more;
			machpil *= 94;
		}
	}
	return res;
}


read_sigs_file(fname)
char *fname;
{
FILE *inf;

int i;
char line[1000];
char sig[1000];
	char *j;
	inf = fopen(fname,"r");
	if (inf==NULL) {
		printf("error: cannot open input file %s\n",fname);
		exit(2);
	}
	j = (char *) 1;
	while (j != NULL) {
		int wid,mini;
		j = fgets(line, 399, inf);
		i=sscanf(line,"%s %d %d",sig,&wid,&mini);
		if ((i>0)&&(strlen(line)>0)) {
			usedg[pgood]=0;
			goods[pgood]=qqai(sig);
			minind[pgood]=0;
			widths[pgood]=1;
			if (i>1) {
				widths[pgood]=wid;
				if (i>2)
					minind[pgood]=mini;
			} 
			pgood++;
		}
	}
	printf("pgood = %d\n",pgood);
}
is_it_good(sig,psig,mini)
int sig,psig,*mini;
{
int i,sofar;


	if (best_block&&(sigs[psig].path!=best_block))  {
		return 0;
	}
	sofar=0;
	for (i=0;i<pgood;i++) {
		sofar += widths[i];
		if (goods[i]==sig){
			if (usedg[i]) { 
				printf("info: reason=2, sig %s is already used  path=%s\n",qqia(sig),qqia(sigs[psig].path));
				return 0;
			}
			sofar -= widths[i];
			usedg[i]=1;
			printf("sig %s / %d taken from %s num %d code %s name %s :%d   min=%d\n",
				qqia(sig),sofar,qqia(sigs[psig].path),
			intcode(qqia(sigs[psig].code)),qqia(sigs[psig].code),qqia(sigs[psig].name),psig,minind[i]);
			*mini=minind[i];
			return sofar+1;
		}
	}
	return 0;

}

is_it_good_next(sig,psig,org)
int sig,psig,org;
{
int i;
	int sofar=0;
	if (best_block&&(nexta[psig].path!=best_block)) 
		return 0;
	for (i=0;i<pgood;i++) {
		sofar += widths[i];
		if (goods[i]==sig){
			if (usedg[i]) return 0;
			usedg[i]=1;
			sofar -= widths[i];
			printf("sig %s taken from %s name %s aliased from %s\n",
				qqia(sig),qqia(nexta[psig].path),
				qqia(nexta[psig].name),qqia(sigs[org].name));
			return (sofar+1);
		}
	}
	return 0;

}

run_monitors() {
	int pos,i,j,x,nexti,mini;
	for (i=0;i<maxsig;i++)  if (sigs[i].name) {
		for (x=0;x<pmonitor;x++) {
			if (monitors[x]==sigs[i].name) {
				sigs[i].monitor=1;
				sigs[i].sfok=1;
				monitors[x]=0;
				printf(">add monitor %s\n",qqia(sigs[i].name));
			}
		}
	}
	for (i=0;i<maxsig;i++) {
		nexti=sigs[i].next;
		while (nexti) {
			for (x=0;x<pmonitor;x++) {
				if (monitors[x]==nexta[nexti].name) {
					sigs[i].monitor=1;
					monitors[x]=0;
				}
			}
			nexti = nexta[nexti].next;
		}
	}
	for (x=0;x<pmonitor;x++) {
		if (monitors[x]) printf(">>didnt find monitor %s\n",qqia(monitors[x]));
	}
}

void use_sigs_file2()
{
	int pos,i,j,x,nexti,mini;
	for (i=0;i<maxsig;i++)  if (sigs[i].name) {
		pos =is_it_good(sigs[i].name,i,&mini);
		for (x=0;x<pmonitor;x++) {
			if (monitors[x]==sigs[i].name) {
				sigs[i].monitor=1;
				sigs[i].sfok=1;
				monitors[x]=0;
				printf(">add monitor %s\n",qqia(sigs[i].name));
			}
		}
		if (pos) {
			sigs[i].sfok=1;
			if (sigs[i].vsf0<0)
				sigs[i].vsf0=pos-1;
			else if (sigs[i].vsf1<0)
				sigs[i].vsf1=pos-1;
			else if (sigs[i].vsf2<0)
				sigs[i].vsf2=pos-1;
			else if (sigs[i].vsf3<0)
				sigs[i].vsf3=pos-1;
			else
				printf(">>>error! oopst0 run out of vsfs i=%d %s pos=%d  \n",i,qqia(sigs[i].name),pos-1);

			sigs[i].mini=mini;
			for (x=0;x<pmonitor;x++) {
				if (monitors[x]==sigs[i].name) {
					sigs[i].monitor=1;
					monitors[x]=0;
				}
			}

			if (vsf)
				fprintf(vcdf2,"$var wire 1 %x %s $end\n",pos-1,qqia(sigs[i].name));
		}
		nexti=sigs[i].next;
		while (nexti) {
			pos = is_it_good_next(nexta[nexti].name,nexti,i);
			if (pos) {
				if (sigs[i].vsf0<0)
					sigs[i].vsf0=pos-1;
				else if (sigs[i].vsf1<0)
					sigs[i].vsf1=pos-1;
				else if (sigs[i].vsf2<0)
					sigs[i].vsf2=pos-1;
				else if (sigs[i].vsf3<0)
					sigs[i].vsf3=pos-1;
				else
					printf(">>>error! oopst1 run out of vsfs i=%d %s pos=%d  \n",i,qqia(nexta[nexti].name),pos-1);
				sigs[i].sfok=1;
				for (x=0;x<pmonitor;x++) {
					if (monitors[x]==nexta[nexti].name) {
						sigs[i].monitor=1;
						monitors[x]=0;
					}
				}
				if (vsf)
					fprintf(vcdf2,"$var wire 1 %x %s\n",pos-1,qqia(nexta[nexti].name));
			}
			nexti = nexta[nexti].next;
		}
	}
	if (vsf)  {
		fprintf(vcdf2,"$upscope $end\n");
		fprintf(vcdf2,"$enddefinitions $end\n");
	}
	for (x=0;x<pmonitor;x++) {
		if (monitors[x]) printf("Error! monitor=%s is not used\n",qqia(monitors[x]));
	}
}
			
void use_sigs_file()
{
	int pos,i,j,nexti,bb;

	if (pgood==0) { return; }
	printf("start using sigs file\n");	
	use_sigs_file2();
	if (best_block) {
		bb=best_block;
		best_block=0;
		printf("start using sigs file again\n");	
		use_sigs_file2();
		best_block=bb;
		printf("end using sigs file again\n");	
	}


	for (i=0;i<pgood;i++) 
		if (!usedg[i]) 
			printf("warning %s wasnt used\n",qqia(goods[i]));
}





int binstr(x,len)
int x,len;
{
	char binres[1000];

	int i,j;
	for (i=len-1;i>=0;i--) {
		j= (x>>i)&1;
		binres[len-i-1] = (j) ? '1' : '0';
	}
	binres[len]=0;
	return qqai(binres);
}

where_am_i_plus(){}





char bin2hex(tmp) char *tmp;
{
	int res=0;
	if (tmp[0]=='1') res=res+8;
	if (tmp[1]=='1') res=res+4;
	if (tmp[2]=='1') res=res+2;
	if (tmp[3]=='1') res=res+1;

	if (res<10) {
		return '0'+res;
	} else {
		return 'a'+res-10;
	}
}


void put_tester(val,indx,comm,mon) char val; int indx; char *comm; int mon;
{
	int i;
	char temp[1000];
	char str[1000];
	char hxstr[1000];
	int xx;
	int dly;
	if (indx<0) return;
	str[32]=0;
	if (val=='x') { if (dump_no_x) { str[0]='0';str[1]='0'; } else { str[0]='1';str[1]='1'; }}
	if (val=='0') { str[0]='0';str[1]='0'; }
	if (val=='1') { str[0]='0';str[1]='1'; }

	strcpy(temp,qqia(binstr(indx,14)));
	for (i=0;i<14;i++) str[2+i]=temp[i];
	xx = (int)(run_time-previous_time);
	while (xx>=0) {
		if (xx>64000) {
			strcpy(temp,qqia(binstr(64000,16)));
			dly=64000;
			xx = xx-64000;
		} else {
			strcpy(temp,qqia(binstr(xx,16)));
			dly=xx;
			xx = xx-64000;
		}
		for (i=0;i<16;i++) str[16+i]=temp[i];
		for (i=0;i<8;i++) {
			strcpy(temp,&(str[i*4]));
			temp[4]=0;
			hxstr[i]=bin2hex(temp);
		}
		hxstr[8]=0;
		fprintf(File,"%s\n",hxstr);
		tester_lines++;
		if (mon)
 			printf(">>monin  %s indx=%d val=%c dt=%d %g %s tl=%d\n",comm,indx,val,dly,run_time,hxstr,tester_lines);  
	}
	previous_time=run_time;
}


int family_reported=0;

family_report()
{
	int nexti,i,x;
	char temp[1000];
	char father[1000];

	if (!family_reported) {
		family_reported=1;
		for (i=0;i<maxsig;i++) {
			strcpy(father,qqia(sigs[i].name));
			for (x=0;father[x];x++) {
				if (father[x]=='/') father[x]='_';
				if (father[x]=='[') father[x]='_';
				if (father[x]==']') father[x]='_';
			}
			nexti=sigs[i].next;
			while (nexti) {
				strcpy(temp,qqia(nexta[nexti].name));
				for (x=0;temp[x];x++) {
					if (temp[x]=='/') temp[x]='_';
					if (temp[x]=='[') temp[x]='_';
					if (temp[x]==']') temp[x]='_';
				}
				printf("same_signal('%s','%s','%s','%s').\n",temp,qqia(nexta[nexti].path),father,qqia(sigs[i].path));
				nexti = nexta[nexti].next;
			}
		}
	}
}
int please_report_0=1;
report_mid_activity() {
	fprintf(stderr,">>reporting mid activity report #%d %g %g\n",activity_counter,run_time,activity_interval);
	if (please_report_0) {
		report_activity0();
		please_report_0=0;
	} else {
		please_report_0=1;
		report_activity1();
	}
}


report_activity0()
{
	int nexti,i,x;
	char temp[1000];
	char father[1000];

	family_report();
	for (i=0;i<maxsig;i++) {
		if (sigs[i].activity0>=5) { 
			if (in_only_list(sigs[i].path)) {
				strcpy(temp,qqia(sigs[i].name));
				for (x=0;temp[x];x++) {
					if (temp[x]=='/') temp[x]='_';
					if (temp[x]=='[') temp[x]='_';
					if (temp[x]==']') temp[x]='_';
				}
				printf("mid_activity(%d,'%s','%s',%d,%d).\n",activity_counter,qqia(sigs[i].path),temp,sigs[i].width,sigs[i].activity0);
			} else {
				nexti=sigs[i].next;
				while (nexti) {
					strcpy(temp,qqia(nexta[nexti].name));
					for (x=0;temp[x];x++) {
						if (temp[x]=='/') temp[x]='_';
						if (temp[x]=='[') temp[x]='_';
						if (temp[x]==']') temp[x]='_';
					}
					if (in_only_list(nexta[nexti].path)) 
						printf("mid_activity(%d,'%s','%s',%d,%d).\n",activity_counter,qqia(nexta[nexti].path),temp,sigs[i].width,sigs[i].activity0);
					nexti = nexta[nexti].next;
				}
			}
		}
		sigs[i].activity0=0;
	}
	activity_counter++;
}

report_activity1()
{
	int nexti,i,x;
	char temp[1000];
	char father[1000];

	family_report();
	for (i=0;i<maxsig;i++) {
		if (sigs[i].activity1>=5) { 
			if (in_only_list(sigs[i].path)) {
				strcpy(temp,qqia(sigs[i].name));
				for (x=0;temp[x];x++) {
					if (temp[x]=='/') temp[x]='_';
					if (temp[x]=='[') temp[x]='_';
					if (temp[x]==']') temp[x]='_';
				}
				printf("mid_activity(%d,'%s','%s',%d,%d).\n",activity_counter,qqia(sigs[i].path),temp,sigs[i].width,sigs[i].activity1);
			} else {
				nexti=sigs[i].next;
				while (nexti) {
					strcpy(temp,qqia(nexta[nexti].name));
					for (x=0;temp[x];x++) {
						if (temp[x]=='/') temp[x]='_';
						if (temp[x]=='[') temp[x]='_';
						if (temp[x]==']') temp[x]='_';
					}
					if (in_only_list(nexta[nexti].path)) 
						printf("mid_activity(%d,'%s','%s',%d,%d).\n",activity_counter,qqia(nexta[nexti].path),temp,sigs[i].width,sigs[i].activity1);
					nexti = nexta[nexti].next;
				}
			}
		}
		sigs[i].activity1=0;
	}
	activity_counter++;
}




report_activity()
{
	int nexti,i,x;
	char temp[1000];
	char father[1000];

	family_report();
	for (i=0;i<maxsig;i++) {
		if (sigs[i].activity>=10) {
			strcpy(temp,qqia(sigs[i].name));
			for (x=0;temp[x];x++) {
				if (temp[x]=='/') temp[x]='_';
				if (temp[x]=='[') temp[x]='_';
				if (temp[x]==']') temp[x]='_';
			}
			if (in_only_list(sigs[i].path)) 
				printf("activity('%s','%s','%s',%d,%d).\n",qqia(sigs[i].fpath),qqia(sigs[i].path),temp,sigs[i].width,sigs[i].activity);
			if (next_activity_also) {
				nexti=sigs[i].next;
				while (nexti) {
					strcpy(temp,qqia(nexta[nexti].name));
					for (x=0;temp[x];x++) {
						if (temp[x]=='/') temp[x]='_';
						if (temp[x]=='[') temp[x]='_';
						if (temp[x]==']') temp[x]='_';
					}
					if (in_only_list(nexta[nexti].path)) 
						printf("activity('%s','%s','%s',%d,%d).\n",qqia(nexta[nexti].fpath),qqia(nexta[nexti].path),temp,sigs[i].width,sigs[i].activity);
					nexti = nexta[nexti].next;
				}
			}
		}
	}
}

in_only_list(sigi) int sigi;
{
	int i;
	if (!ponly) return 1;
	for (i=0;i<ponly;i++) if (onlys[i]==sigi) return 1;
	return 0;
}


