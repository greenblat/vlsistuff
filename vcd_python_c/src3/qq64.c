#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long unsigned qqai(char *a);

int p1_a_alloc_at_once = 16384;
unsigned long minimal_valid=0;

int real_ugly_way_to_keep_track_of_new_strings;

typedef struct alphax {

/* int star; */
char lc;
struct alphax  *downp,*nextp,*fatherp;
long  value;

} Anode;

Anode *alpha_add(Anode *arun, char *str);
Anode * allocate_rest_alpha(Anode *arun, char *str);

Anode *afree=0;

Anode *first_access[256];
int anodes_allocations=0;

Anode *check_access[256];


void debug_call(int d) {    
    int x;
    x=0;
    printf("debug call \n");
    x = d/x;
}

void check_me(int x) {
    int i;
    for (i=0;i<256;i++) {
        if (first_access[i]!=check_access[i])
            printf("++++++++ %d %d\n",i,x);
    }
}
void p1_clear_anode(Anode *anode) {
    (*anode).lc =0;
    (*anode).downp =0;
    (*anode).nextp =0;
    (*anode).fatherp =0;
    (*anode).value =99999999;
} 


Anode *a1_get_node() {
    Anode *temp;
    int i;
    if (afree) {
        temp = afree;
        afree = (Anode *) ((*afree).nextp);
        p1_clear_anode(temp); 
        return temp;
    }
    temp = (Anode*) malloc(p1_a_alloc_at_once*sizeof(Anode));
    if (!temp) {
        printf("oopst!! run out of memory on anode allocations\n");
        exit(3);
    }
    anodes_allocations++;
    if ((anodes_allocations % 100) == 0)
        printf("%% anode total allocated %luMeg\n",p1_a_alloc_at_once*anodes_allocations*sizeof(Anode)/(1024*1024));
    for (i=1;i<p1_a_alloc_at_once;i++) {
        (temp[i]).nextp = (Anode *) &(temp[i+1]);
    }
    afree = &(temp[1]);
    (temp[p1_a_alloc_at_once-1]).nextp = 0;
    p1_clear_anode(temp); 
    if (!minimal_valid) minimal_valid = (long unsigned) temp;
    return temp;
}



int init_run = 0;
void alpha_init() 
{
    long unsigned i;
    Anode *anode;
    if (init_run) return;
    init_run=1;
    for (i=0;i<256;i++) {
        anode = a1_get_node();
        (*anode).lc = (char) i;
        first_access[i]=anode;
/*        check_access[i]=anode; */
    }
    i = qqai("aaa"); 
}


long unsigned qqai(char *str) {
    Anode *arun;
    long unsigned j;
    if (str[0]==0) return 0l;
    arun = first_access[(unsigned)str[0]];

/*    check_me(1); */
    real_ugly_way_to_keep_track_of_new_strings=0;
     j =  (long unsigned) alpha_add(arun,&(str[1])); 
    return j;
}
    


void cucu(int ind) {
        printf("ilia error!! %d got qqia empty\n",ind);
}


char *alpha_ia1(long unsigned ind, char *str) {
    int a,b,i=0;
    Anode *run;
    char tmp;

    if (!ind) {str[0]=0; return str;}
    run = (Anode *) ind;
    while (run) {
        str[i]= (*run).lc;
        i++;
        run = (Anode *) (*run).fatherp;
    }
    a = 0;
    b = i-1;
    str[i]=0;
    while (b>a) {
        tmp = str[b];
        str[b]=str[a];
        str[a]=tmp;
        b--;
        a++;
    }
    return str;
}

char alphas[64][50000];
int use_alpha=0;

char *qqia(long unsigned ind)
{
    char *ch1;
/*    int star; */

//    printf("qqia %lx\n",ind);
    use_alpha++;
    if (use_alpha>63) use_alpha=0;

    if (!ind) {
        alphas[use_alpha][0]=0;
        return alphas[use_alpha];
    }
//    if (ind<minimal_valid) {
//        printf("warning!! ilia qqia got ind=0x%lx which is illegal min=0x%lu \n",ind,minimal_valid);
//        minimal_valid = ind;
//        debug_call(ind);
//    }
/*
    star = ( * (Anode *)ind).star;
    if (star != 178) {
        printf("error!! ilia qqia got ind=%d which was not starred\n",ind);
        alphas[use_alpha][0]=0;
        return alphas[use_alpha];
    }
*/


    if (!ind) {
        alphas[use_alpha][0]=0;
        return alphas[use_alpha];
    }
    ch1 =  alpha_ia1(ind,alphas[use_alpha]);
    if (!ch1[0]) {
        cucu(ind);
    }
    return ch1;
}




    
    
Anode * alpha_add(Anode *arun, char *str) {
    Anode * last;
    Anode *anode,*newdown,*down,*next,*prevnext;
    if (str[0]==0) return (Anode *) arun;

    down = (Anode*)(*arun).downp;
    if (!down) {
        last = allocate_rest_alpha(arun,str);
        real_ugly_way_to_keep_track_of_new_strings=1;
        return last;
    } else {
        if (str[0]<(*down).lc) {
            last = allocate_rest_alpha(arun,str);
            newdown = (Anode*)(*arun).downp; 
            (*newdown).nextp = (Anode *)down;
            real_ugly_way_to_keep_track_of_new_strings=1;
            return last;
            
        } else if (str[0]==(*down).lc) {
            return alpha_add(down,&(str[1]));
        } else {
            prevnext = down;
            next = (Anode*)(*down).nextp;
            while (next && ( (*next).lc < str[0]))  {
                prevnext = next;
                next = (Anode*)(*next).nextp;
            }
            if (!next) {
                anode = a1_get_node();
                (*anode).lc=str[0];
                last = allocate_rest_alpha(anode,&(str[1]));
                (*prevnext).nextp = (Anode *) anode;
                (*anode).fatherp = (Anode *) arun;
                real_ugly_way_to_keep_track_of_new_strings=1;
            } else if ((*next).lc == str[0]){
                return alpha_add(next,&(str[1]));
            } else {
                anode = a1_get_node();
                (*anode).lc=str[0];
                last = allocate_rest_alpha(anode,&(str[1]));

                (*anode).nextp=(Anode *) next;
                (*anode).fatherp = (Anode *) arun;
                (*prevnext).nextp = (Anode *) anode;
                real_ugly_way_to_keep_track_of_new_strings=1;
            }
            return last;                
        }
    }
}

Anode * allocate_rest_alpha(Anode *arun, char *str) {
    Anode *anode;
    if (str[0]==0) return (Anode *)arun;
    anode = a1_get_node();
    (*arun).downp = (Anode *) anode;
    (*anode).fatherp = (Anode *) arun;
    (*anode).lc = str[0];
    return allocate_rest_alpha(anode,&(str[1]));
}




void qqsa(long unsigned ind,long val) {
    Anode *x;
    x = (Anode *)ind;

    (*x).value = val;
}

long qqas(long unsigned ind) {
    Anode *x;
    x = (Anode *)ind;

    return (*x).value;
}





/***********
int Index_ilia(s, t)
    char            *s, *t;
{
    int             i, j, k;
    for (i = 0; s[i] != '\0'; i++) {
        for (j = i, k = 0; (s[j]!=0)&&(t[k] != '\0') &&(s[j] == t[k]); j++, k++);
        if (t[k] == '\0')
            return (i);
    }
    return (-1);
}
*******/



