
import os,sys,string,types
import logs

def help_main(Env):
    Mod = Env.Current
    
    Fval = open('src/values.h','w')
    forcesAndPeeks(Mod,Fval)
    widths(Mod,Fval)
    Fval.close()
    makeCpp(Mod)


def forcesAndPeeks(Mod,Fval):
    Fval.write(STR0)
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if ('input' in Dir)or('output' in Dir):
            Wid1 = Wid
            Wid = getWid(Net,Wid,Mod)
            Fval.write('// %s %d %s\n'%(Net,Wid,Wid1))
            if Wid<=32:
                Str = string.replace(STR1,'NET',Net)
                X = (Wid+3)/4
                Str = string.replace(Str,'LL',str(X))
                Fval.write(Str)
            elif Wid<=64:
                Str = string.replace(STR1_1,'NET',Net)
                X = (Wid+3)/4
                Str = string.replace(Str,'LL',str(X))
                Fval.write(Str)
            else:
                Str = string.replace(STR1_2,'NET',Net)
                PP = ''
                TOP = ''
                WW = Wid
                pos = 0
                while (WW>=32):
                    PP = '%08x'+PP
                    WW -= 32
                    TOP = 'top->%s[%d],'%(Net,pos)+TOP
                    pos += 1 
                X = (WW+3)/4
                if (X>0): 
                    PP = '%%0%dx'%X+PP
                    TOP = 'top->%s[%d],'%(Net,pos)+TOP
                Str = string.replace(Str,'LLL','"'+PP+'"')
                Str = string.replace(Str,'TOP',TOP[:-1])
                Fval.write(Str)



    Fval.write(STR2)
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if ('input' in Dir)or('output' in Dir):
            Wid = getWid(Net,Wid,Mod)
            Str = string.replace(STR3,'NET',Net)
            if Wid<=64:
                Str = string.replace(Str,'WID',str(Wid))
                Fval.write(Str)
            else:
                Fval.write('    if (strcmp(path,"%s")==0) {\n'%(Net))
                Many = (Wid+31)/32
                for ii in range(Many):
                    Fval.write('        copy8(val,%d); top->%s[%d] = strtol(tmp,NULL,16);\n'%(Many-ii-1,Net,Many-ii-1))
                Fval.write('        return; }\n')
    Fval.write(STR4)

def makeCpp(Mod):
    Fin  = open('llbin/sim_main.cpp')
    Fout = open('src/sim_main.cpp','w')
    lines = Fin.readlines()
    Fin.close()
    for line in lines:
        line = string.replace(line,'TOP',Mod.Module)
        Fout.write(line)
    Fout.close()

def widths(Mod,Fval):
    Fval.write(STR5)
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if ('input' in Dir)or('output' in Dir):
            Wid1 = Wid
            Wid = getWid(Net,Wid,Mod)
            Fval.write('    if (strcmp(path,"%s")==0) { strcpy(VVV,"%d"); return VVV;}\n'%(Net,Wid))
    Fval.write('    strcpy(VVV,"-1"); return VVV;\n}\n') 



STR3 ='    if (strcmp(path,"NET")==0) {top->NET = strtol(val,NULL,16);return;}\n'
STR4 = '''
    printf("error! net=%s is not defined for force\\n",path);
    return;
}
'''

STR5 = 'char *getWid(char *path) {\n'

def getWid(Net,Wid,Mod):
    if Wid in ['0',0]: return 0
    if Wid in ['1',1]: return 1
    if type(Wid)==types.IntType: return Wid
    if type(Wid) == types.TupleType:
        if len(Wid)==2:
            Hi = getWid(Net,Wid[0],Mod)
            Lo = getWid(Net,Wid[1],Mod)
            return Hi-Lo+1
        if (len(Wid)==3)and(Wid[0]=='packed'):
            AA = getWid(Net,Wid[1],Mod)
            BB = getWid(Net,Wid[2],Mod)
            return AA*BB
    if type(Wid)==types.ListType:
        if len(Wid)==3:
            AA = getWid(Net,Wid[1],Mod)
            BB = getWid(Net,Wid[2],Mod)
            Str = '%s %s %s'%(AA,Wid[0],BB)
            return getWid(Net,Str,Mod)
        return 1
    if type(Wid)==types.StringType:
        return eval(Wid,Mod.parameters)

    logs.log_error('wid of "%s" failed "%s"'%(Net,Wid)) 
    return 1





STR0 = '''
char VVV[50000];
char *getValue(char *path) {
'''
STR1 ='     if (strcmp(path,"NET")==0) { sprintf(VVV,"%0LLx",top->NET); return VVV;}\n'
STR1_1 ='     if (strcmp(path,"NET")==0) { sprintf(VVV,"%0LLlx",top->NET); return VVV;}\n'
STR1_2 ='     if (strcmp(path,"NET")==0) { sprintf(VVV,LLL,TOP); return VVV;}\n'

STR2 = '''
    printf("error! net=%s is not defined for peek\\n",path);
    sprintf(VVV,"%s","-1"); return VVV;
}

char tmp[9];
void copy8_old(char *Str,int Pos) {
    int pos = Pos*8;
    for (int ii=0;ii<8;ii++) tmp[ii]=Str[pos+ii];
    tmp[8]=0;
}
void copy8(char *Str,int Pos) {
    int Len = strlen(Str)-1;
    int ii = 7;
    int fr; 
    for (ii=7;(ii>=0);ii--) {
        fr = Len-(Pos*8)-7+ii;
        if (fr>=0) tmp[ii]=Str[fr];
        else tmp[ii]='0';
    }   
    tmp[8]=0;
}





void setValue(char *path,char *val) {
'''

