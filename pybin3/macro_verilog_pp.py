#! /usr/bin/env python3
'''
    help:   invocation: macro_verilog_pp.py [-h] [-y Dir] [-I Dir] [-o <filename>]  [-split [dir]]  File1 File2 ....

    this script massages verilog files. 
    it interprets ifdef/elsif/else/endif directives
    it includes include files
    it replaces all macro definitions
    it computes constants, in the form of "16-1"

    -y Dir     adds search directory to includes list
    -I Dir     identical to -y
    -o Filename  [file3.v default] the script creates one file with all substitutions
    -split     create directory "tmp" where all modules have their own file called "module".v  if -split has parameter, it will be the dir name.
    -specify   remove specifies
    -h  print these instructions

verilog style params:
    +incdir+DIR+
    +libext+EXT+
    -v LIBFILE

'''


import os,sys,string
import re

from logs import parse_args

Lines2=[]
Lines3=[]
Defined={}
IncDirs=[]
LibExt = ['.v']
def main():
    Params = parse_args()
    run_main(Params)

def run_main(Params,Dumps='11111'):
    global Lines2,Lines3
    Fnames = Params['fnames']
    if Fnames==[]:
        print(__doc__)
        print('no files given')
        return
    if ('-h' in Params):
        print(__doc__)
        return
    if ('-d' in Params):
        Defs = Params['-d']
        for Def in Defs:
            print('defined',Def)
            Defined[Def]=1
    if ('-y' in Params):
        IncDirs.extend(Params['-y'])
    if ('-v' in Params):
        Fnames.extend(Params['-v'])
    if ('incdir' in Params):
        IncDirs.extend(Params['incdir'])
    if ('libext' in Params):
        LibExt.extend(Params['libext'])
    if ('-I' in Params):
        IncDirs.extend(Params['-I'])
    if ('-o' in Params):
        OutFileName = Params['-o'][0]
    else:
        OutFileName = 'file3.v'
    Synopsys = ('-synopsys' in Params)


    Lines = []
    for Fname in Fnames:
        File = open(Fname)
        Lines.extend(readfile(File))
        File.close()
    if (Synopsys):
        print('removing translates')
        Lines= remove_synopsys_on_off(Lines)

    scan0(Lines)
    if Dumps[0] == '1':
        File2 = open('filex0.v','w')
        for line in Lines:
            File2.write(line)
        File2.close()

    scan1(Lines)
    if Dumps[1] == '1':
        File2 = open('filex1.v','w')
        for line in Lines2:
            File2.write(line)
        File2.close()

    Def2=[]
    for Key in Defined:
        Def2.append((len(Key),Key,Defined[Key]))
    Def2.sort()
    Def2.reverse()
    print('computing...')
    dones=0
    for i,line in enumerate(Lines3):
        line = use_defines(line,Def2)
        linex = line
        Lines3[i]=linex
        dones += 1
        if (dones % 10000)==0:
            print('%d lines'%dones)
        
    if ('-specify' in Params):
        do_the_specify(Lines3)

    if Dumps[2] == '1':
        File3 = open(OutFileName,'w')
    Lines4=[]
    for line in Lines3:
        if Dumps[2] == '1':  File3.write(line)
        wrds = line.split()
        if len(wrds)!=0:
            Lines4.append(line)
    if Dumps[2] == '1': File3.close()


    if ('-split' in Params):
        Dir = Params['-split'][0]
        if (Dir=='y'):
            Dir='tmp'
        do_the_split(Lines4,Dir)
    Lines5 = []
    File4name = 'file4.v'
    if Dumps[2] == '0':
        File4name = OutFileName
    if (Dumps[3] == '1') or (Dumps[4] == '1'): doFile4(Lines4,Lines5,File4name)
    if Dumps[4] == '1': doFile5(Lines5)



def doFile4(Lines4,Lines5,Fname):
    File4 = open(Fname,'w')
    state='idle'
    for line in Lines4:
        if len(line)==0:
            pass
        elif line[-1]=='\n':
            line=line[:-1]
        if '//' in line:
            line = line[:line.index('//')]
        if ('/*' in line)and('*/' in line):
            ok=True
            ind0 = line.index('/*')
            ind1 = line.index('*/')
            while ok:
                if ind0>ind1: ok=False
                if ind0<ind1:
                    part1 = line[:line.index('/*')]
                    part2 = line[line.index('*/')+2:]
                    line=part1+part2
                    ok = ('/*' in line)and('*/' in line)
                if ok:
                    ind0 = line.index('/*')
                    ind1 = line.index('*/')
        if state=='idle':
            if ('/*' in line):
                line=line[:line.index('/*')]
                state='work'
        elif state=='work':
            if ('*/' in line):
                line=line[line.index('*/')+2:]
                state='idle'
            else:
                line=''
        


        wrds = line.split()
        if len(wrds)>0:
            File4.write('%s\n'%line)
            Lines5.append(line+'\n')
    File4.close()

def doFile5(Lines5):
    File5 = open('file5.v','w')
    state='header'
    for line in Lines5:
        if (state=='header'):
            File5.write(line)
            if ';' in line:
                state = 'externals'
        elif (state=='externals'):
            wrds = line.split()
            if (len(wrds)>0)and(wrds[0] in ['input','output','inout','parameter']):
                File5.write(line)
            elif (len(wrds)>0)and(wrds[0] in ['assign','localparam','always']):
                state = 'finish'
            elif (len(wrds)>0)and(wrds[0] in ['endmodule']):
                state = 'finish'
        elif (state=='finish'):
            File5.write('endmodule\n\n')
            File5.close()
            return
    File5.write('endmodule\n\n')
    File5.close()
    return



Pat0 = re.compile('[{:\-+ \[][0-9]+ *[\*] *[0-9]+')
Pat1 = re.compile('[{:\-+ \[][0-9]+ *[+-] *[0-9]+')
Pat2 = re.compile('\( *[0-9]+ *\)')
Pat3 = re.compile(' 0[0-9]+')
Pat4 = re.compile('[-+*/]0[0-9]+')

def stupid1(Str):
    while (len(Str)>1)and(Str[0]=='0')and(Str[1] in '0123456789'):
        Str = Str[1:]
    Mtch = Pat3.search(Str)
    while (Mtch):
        (A,B) = Mtch.span()
        P1 = Str[A:B]
        Bef = Str[:A]
        Aft = Str[B:]
        Str = Bef+P1[2:]+Aft
        Mtch = Pat4.search(Str)

    
    Mtch = Pat4.search(Str)
    while (Mtch):
        (A,B) = Mtch.span()
        P1 = Str[A:B]
        Bef = Str[:A]
        Aft = Str[B:]
        Str = Bef+P1[2:]+Aft
        Mtch = Pat4.search(Str)

    return Str


def computex(Str,Pat,Where):
    Mtch = Pat.search(Str)
    while (Mtch):
        (A,B) = Mtch.span()
        if Where in [0,1]:
            Bef = Str[:A+1]
            Aft = Str[B:]
            P1 = Str[A+1:B]
        else:
            Bef = Str[:A]
            Aft = Str[B:]
            P1 = Str[A:B]
        P1=stupid1(P1)


        P1 = P1.replace(' ','')
        try:
            Eval = str(eval(P1))
            Str= Bef+Eval+Aft
            Mtch = Pat.search(Str)
        except:
            print('error! failed %d eval on "%s" "%s" %s'%(Where,P1,Str[A:B],map(ord,list(Str[A:B]))))
            Mtch = False
    return Str 

def compute_constants(line):
    done = False
    while (not done):
        done=True
        linex = computex(line,Pat0,0)
        linex = computex(linex,Pat1,1)
        if linex!=line:
            linex = computex(linex,Pat2,2)
        done = linex==line
        line = linex
    return line 

def use_defines(line,Def2):
    dones=True
    if "`celldefine" in line: return ''
    if "`endcelldefine" in line: return ''
    if "`undef" in line: return ''
    while ('`' in line)and(dones):
        dones =False
        i = 0
        while i<len(Def2):
            (Len,Key,Val)=Def2[i]
            if '`'+Key in line:
                line = line.replace('`'+Key,Val)
                i=len(Def2)+5
                dones =True
            i +=1
    return line


def readfile(File):
    Lines = []
    num=0
    while 1:
        line = File.readline()
        num+=1
        if line=='':
            return Lines
        if line[-1]==13:
            line = line[:-1]+'\n'
        if (len(line)>1)and(ord(line[-2])==13):
            line = line[:-2]+'\n'

        if needs_work(line):
            more = work(line)
            Lines.extend(more)
        else:
            Lines.append(line)
    return Lines

def work(line):
    line = remove_comment1(line)
    line = clear_defs(line)
    if len(line)<2:
        return []
    wrds = line.split()
    if '`ifdef' in wrds:
        lines=rework(line,'`ifdef')
        return lines
    if '`ifndef' in wrds:
        lines=rework(line,'`ifndef')
        return lines
    if '`elsif' in wrds:
        lines=rework(line,'`elsif')
        return lines
    if '`else' in wrds:
        lines=rework(line,'`else',False)
        return lines
    if '`endif' in wrds:
        lines=rework(line,'`endif',False)
        return lines
    if '`include' in wrds:
        lines = include_file(wrds[1])
        return lines
    if line[-1]!='\n':
        line=line+'\n'
    return [line]

def include_file(Fname):
    if Fname[0]=='`': return ['`include "%s"\n'%Fname]
    Fname = Fname.replace('"','')
    print("INCLUDDE",Fname,os.path.exists(Fname))
    if os.path.exists(Fname):
        File = open(Fname)
        lines = readfile(File)
        return lines
    for Dir in IncDirs:
        Fname1 = '%s/%s'%(Dir,Fname)
        if os.path.exists(Fname1):
            return include_file(Fname1)
    print('file "%s" cannot be included'%Fname)
    return []
    


def rework(line,Ifdef,Two=True):
    wrds = line.split()
    Ind = wrds.index(Ifdef)
    Bef = wrds[:Ind]
    if Two:
        Aft = wrds[Ind+2:]
        This = '%s %s\n'%(wrds[Ind],wrds[Ind+1])
    else:
        Aft = wrds[Ind+1:]
        This = '%s\n'%(Ifdef)
    Line0= ' '.join(Bef)+'\n'
    Line2= ' '.join(Aft)+'\n'
    L0 = work(Line0)
    L2 = work(Line2)
    return L0+[This]+L2
        

def clear_defs(line):
    line = line.replace('`elsif',' `elsif ')
    line = line.replace('`ifdef',' `ifdef ')
    line = line.replace('`ifndef',' `ifndef ')
    line = line.replace('`else',' `else ')
    line = line.replace('`endif',' `endif ')
    return line

def remove_comment1(line):
    if '//' in line:
        ind = line.index('//')
        return line[:ind]
    return line

    
def needs_work(line):
    return  ('`ifdef' in line)or('`else' in line)or('`endif' in line)or('`define' in line)or('`ifndef' in line)or('`elsif' in line)or('`include' in line)

def scan0(Lines):
    ind=0
    while ind<len(Lines):
        line = Lines[ind]
        if '//' in line:
            line = line[:line.index('//')]+'\n'
            Lines[ind]=line
        ind += 1

    ind=0
    while ind<len(Lines):
        line = Lines[ind]
        if (len(line)>1)and(line[-2]=='\\'):
            line = line[:-2]+Lines[ind+1]
            Lines[ind]=line
            Lines.pop(ind+1)
        else:
            ind += 1
    ind=0
    while ind<len(Lines):
        line = Lines[ind]
        if (" 'b" in line): line = line.replace(" 'b","'b")
        if (" 'd" in line): line = line.replace(" 'd","'d")
        if (" 'h" in line): line = line.replace(" 'h","'h")
        if ("'b " in line): line = line.replace("'b ","'b")
        if ("'d " in line): line = line.replace("'d ","'d")
        if ("'h " in line): line = line.replace("'h ","'h")
        Lines[ind]=line
        ind += 1
            
    state = 'idle'
    ind=0
    while ind<len(Lines):
        line = Lines[ind]
        if state=='idle':
            if '/*' in line:
                Bef = line[:line.index('/*')]
                Aft = line[line.index('/*')+2:]
                if '*/' in Aft:
                    Aft2 = Aft[Aft.index('*/')+2:]
                    line = Bef+Aft2
                    Lines[ind]=line
                else:
                    Lines[ind]=Bef
                    state = 'inside'
                    ind += 1
            else: 
                ind += 1
        elif state=='inside':
            if '*/' in line:
                line = line[line.index('*/')+2:]
                Lines[ind]=line
                state='idle'
            else:
                Lines[ind]=''
                ind += 1
    


def scan1(Lines):
    state='idle'    
    queue=[]
    indx=0
    while indx<len(Lines):
        line = Lines[indx]
        indx+=1
        wrds = line.split()
        if state=='idle':
            if ('`define' in line):
                Defined[wrds[1]]=' '.join(wrds[2:])
                Lines2.append(line)
            elif ('`ifndef' in line):
                if wrds[1] in Defined:
                    state='ifdef_false'
                else:
                    state='ifdef_true'
            elif ('`ifdef' in line):
                if wrds[1] in Defined:
                    state='ifdef_true'
                else:
                    state='ifdef_false'
            elif ('`include' in line):
                Def2=[]
                for Key in Defined:
                    Def2.append((len(Key),Key,Defined[Key]))
                Def2.sort()
                Def2.reverse()
                wrds1 = use_defines(wrds[1],Def2)
                lines = include_file(wrds1)
                Lines = Lines[:indx-2]+lines+Lines[indx:] 
            elif needs_work(line):
                print('error! kind=1',state,indx,line)
            else:
                Lines2.append(line)
                Lines3.append(line)
        elif state=='ifdef_true':
            if ('`define' in line):
                Defined[wrds[1]]=' '.join(wrds[2:])
                Lines2.append(line)
            elif ('`ifdef' in line):
                queue = [state]+queue
                if wrds[1] in Defined:
                    state='ifdef_true'
                else:
                    state='ifdef_false'
            elif ('`ifndef' in line):
                queue = [state]+queue
                if wrds[1] in Defined:
                    state='ifdef_false'
                else:
                    state='ifdef_true'
            elif ('`else' in line):
                state='wait_endif'
            elif ('`elsif' in line):
                state='wait_endif'
            elif ('`endif' in line):
                if queue==[]:
                    state='idle'
                else:
                    state=queue.pop(0)
            elif needs_work(line):
                print('error! kind=2',state,line)
            else:
                Lines2.append(line)
                Lines3.append(line)
            
        elif state=='ifdef_false':
            if ('`else' in line):
                state='active_endif'
            elif ('`elsif' in line):
                if wrds[1] in Defined:
                    state='ifdef_true'
                else:
                    state='ifdef_false'
            elif ('`ifdef' in line):
                queue = [state]+queue
                state='wait_endif'
            elif ('`ifndef' in line):
                queue = [state]+queue
                state='wait_endif'
            elif ('`endif' in line):
                if queue==[]:
                    state='idle'
                else:
                    state=queue.pop(0)
            elif ('`define' in line):
                pass
            elif ('`include' in line):
                pass
            elif needs_work(line):
                print('error! kind=3',state,line)
        elif state=='active_endif':
            if ('`define' in line):
                Defined[wrds[1]]=' '.join(wrds[2:])
                Lines2.append(line)
            elif ('`ifdef' in line):
                queue = [state]+queue
                if wrds[1] in Defined:
                    state='ifdef_true'
                else:
                    state='ifdef_false'
            elif ('`ifndef' in line):
                queue = [state]+queue
                if wrds[1] in Defined:
                    state='ifdef_false'
                else:
                    state='ifdef_true'
            elif ('`else' in line):
                state='wait_endif'
            elif ('`elsif' in line):
                state='wait_endif'
            elif ('`endif' in line):
                if queue==[]:
                    state='idle'
                else:
                    state=queue.pop(0)
            elif ('`include' in line):
                Def2=[]
                for Key in Defined:
                    Def2.append((len(Key),Key,Defined[Key]))
                Def2.sort()
                Def2.reverse()
                wrds1 = use_defines(wrds[1],Def2)
                lines = include_file(wrds1)
                Lines = Lines[:indx-2]+lines+Lines[indx:] 
            elif needs_work(line):
                print('error! kind=4',state,line)
            else:
                Lines2.append(line)
                Lines3.append(line)
        elif state=='wait_endif':
            if ('`ifdef' in line):
                queue = [state]+queue
                state='wait_endif'
            elif ('`ifndef' in line):
                queue = [state]+queue
                state='wait_endif'
            elif ('`endif' in line):
                if queue==[]:
                    state='idle'
                else:
                    state=queue.pop(0)
            elif ('`else' in line):
                pass
            elif ('`elsif' in line):
                pass
            elif ('`define' in line):
                pass
            elif ('`include' in line):
                pass
            elif needs_work(line):
                print('error! kind=5',state,line)


def do_the_split(wholelib,dir='tmp'):
    modules=[]
    state=0
    if not os.path.exists(dir):
        os.system('mkdir %s'%dir)
    for ind,line1 in enumerate(wholelib):
        line = fix_stupid_problems(line1)
        wrds =  line.split()
        if (state==0):
            if (len(wrds)>0)and(wrds[0] in ['module','primitive','interface','package']):
                line2 = line.replace(';',' ; ')
                line2 = line2.replace('(',' ( ')
                wrds =  line2.split()
#                print('111',wrds)
                if len(wrds)==1:
                    line2 = wholelib[ind+1]
                    line2 = line2.replace(';',' ; ')
                    line2 = line2.replace('(',' ( ')
                    wrds =  line2.split()
                Module = relaxName(wrds[1])
                File=open(dir+'/'+Module+'.v','w')
#                print('222',wrds,Module)
                modules = [Module]+modules
                File.write(line)
                print('opening ',Module)
                state=1
        elif (state==1):
            if (len(wrds)>0)and(has_end(wrds[0])):
                File.write(line)
                File.close()
                state=0
            else:
                File.write(line)

def has_end(word):
    if word in ['endmodule','endprimitive','endinterface','endpackage']:
        return 1
    x =word.find('//')    
    if (x>0):
        word = word[0:x]
        return has_end(word)
    x =word.find('/*')    
    if (x>0):
        word = word[0:x]
        return has_end(word)
    return 0

def fix_stupid_problems(inline):
    for pattern in ["'b ","'h ","'d "]:
        ind  = 1
        while (ind>0):
            ind  = inline.find(pattern)
            if (ind>=0):
                inline = inline[0:ind+2]+inline[ind+3:]
    return inline

#  // synopsys translate_off
#  // synopsys translate_on

def remove_synopsys_on_off(Lines):
    Linesx = []
    state='on'
    for line in Lines:
        wrds = line.split()
        if 'synopsys' in wrds:
            ind = wrds.index('synopsys')
            if (state=='on'):
                if (len(wrds)>ind)and(wrds[ind+1]=='translate_off'):
                    state='off'
                else:
                    Linesx.append(line)

            elif (state=='off'):
                ind = wrds.index('synopsys')
                if (len(wrds)>ind)and(wrds[ind+1]=='translate_on'):
                    state='on'
        elif (state=='on'):
            Linesx.append(line)
    return Linesx

def relaxName(Txt):
    if Txt[0]=='\\': Txt = Txt[1:]
    for Chr in "\\/$='":
        Txt = Txt.replace(Chr,'_')
    return Txt

REMOVES = '''
`resetall
`delay_mode_path
`suppress_faults
`enable_portfaults
`timescale 
'''.split()

def do_the_specify(Lines):
    ind = 0
    state = 'idle'
    print('LINES',len(Lines))
    while ind < len(Lines):
        Line = Lines[ind]
        if state=='idle':
            Pop = False
            for Token in REMOVES: 
                if Token in Line:
                    Pop = True
            if Pop:
                Lines.pop(ind)
            elif 'specify' in Line:
                state = 'work'
                Lines.pop(ind)
            else:
                ind += 1
        elif state=='work':
            if 'endspecify' in Line:
                state = 'idle'
            Lines.pop(ind)
    
    print('LINES',len(Lines))




if __name__ == '__main__':
    main()





