#! /usr/bin/python3
"""
         usage:    ver_macro_pp2.py   <verilog_files>   [-use_defines] [-y libdir] [-odir out_dir] [-d define]

         this program splits verilog file into separate modules in output directory.
         each file is called <module>.v

         if -use_defines is specified, all defines are replaced, and all ifdef/ifndef are also replaced.


         Ilia cell: +972-54-4927322     skype: igreenblat  email:  greenblat@mac.com

"""

import sys
import os

new_defines = []
pre_defines = []
modules = []
Tempindex=0
ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
alphas = ascii_letters + digits + '_'

Fx = open('log.log','w')
def work_on_lines(lines,filename):
    global pre_defines
    global Tempindex
    wrds = filename.split('/')
    wrds = wrds[:-1]
    directory = '/'.join(wrds)
    ifdefstate = [1]
    total = len(lines)
    sofar=0
    guard=0
    Tempname = 'ver_macro_pp.temp'+str(Tempindex)
    Tempindex=Tempindex+1
    Temp = open(Tempname,'w')
    print('open_write',Tempname,len(lines))
    for line in lines:
        sofar = sofar + 1
        guard = guard + 1
        if (guard>9999):
            guard=0
            print('done ',sofar,' out of ',total)
        line = line.replace('//',' //')
        words = line.split()
        Fx.write('%s\n'%(str(words)))
        if (len(words)>0):
            if (words[0]=='`include'):
                Temp.write('//+++ '+line)
                if (ok(ifdefstate)):
                    print('including ',words[1])
                    mlines = deal_include(words[1],ydirs+[directory],filename)
                    for lll in mlines:
                        wordsx = lll.split()
                        if (wordsx[0]=='`define'):
                            if (len(wordsx)>=3):
                                value1 = ' '.join(words[2:])
                                wrds2 = value1.split('//')
                                value = wrds2[0]
                                pre_defines = pre_defines + [(wordsx[1],value)]
                            else:
                                pre_defines = pre_defines + [(wordsx[1],'')]
                        elif (len(lll)>0):
                            if (lll[-1]!='\n'):
                                lll += '\n'
                            Temp.write(lll)

            elif (words[0]=='`else'):
                ifdefstate[0]= not ifdefstate[0]
                Temp.write('//+++ '+line)
            elif (words[0]=='`endif'):
                ifdefstate=ifdefstate[1:]
                Temp.write('//+++ '+line)
            elif (words[0]=='`ifdef'):
                Temp.write('//+++ '+line)
                found=0
                for (A,B) in pre_defines:
                    if (words[1]==A):
                        found = 1
#                        print('debug ifdef found ',A,B)
                ifdefstate = [found]+ifdefstate
#                if (not found):
#                    print('debug ifdef not found ',words[1])
            elif (words[0]=='`ifndef'):
                Temp.write('//+++ '+line)
                found=1
                for (A,B) in pre_defines:
                    if (words[1]==A):
                        found = 0
                ifdefstate = [found]+ifdefstate
            elif (words[0]=='`define'):
                Temp.write('//+++ '+line)
                if (ok(ifdefstate)):
                    if (len(words)>=3):
                        done=0
                        value1 = ' '.join(words[2:])
                        wrds2 = value1.split('//')
                        value = wrds2[0]
                        pre_defines = pre_defines + [(words[1],value)]
                    else:
                        pre_defines = pre_defines + [(words[1],'')]
            else:
                if (ok(ifdefstate)):
                    Temp.write(line)
                else:
                    Temp.write('//+++ '+line)
    Temp.close()
    print('close_write',Tempname,sofar,ok(ifdefstate),ifdefstate)
    Temp = open(Tempname,'r')
    result =  Temp.readlines()
    Temp.close()
    return result

def deal_include(fname1,Ydirs,filename):
    global pre_defines
    mlines=[]
    fname1 = fname1[1:-1]
    fname=''
    fname2=''
    if (os.access(fname1,os.R_OK)):
        fname2=fname1
    else:
        print('searching ',Ydirs)
        for Dir in Ydirs:
            tryme = Dir+'/'+fname1
            if (os.access(tryme,os.R_OK)):
                fname2 = tryme
        if (fname2==''):
            print('include not found',fname1, Dir+'/'+fname1)
            fname2=' BAD '
    if (fname2!=' BAD '):
        File = open(fname2,'r')
        ilines = File.readlines()
        mlines = work_on_lines(ilines,fname2)
        print('return include ',len(ilines),len(mlines),fname2)
    return mlines



def work_on_file(fname):
    global pre_defines,TopFileName
    File = open(fname,'r')
    TopFileName=fname
    lines = File.readlines()
    File.close()
    lines1 = work_on_lines(lines,fname)
    reduce_predefines()
    if (use_defines):
        lines2= use_defines_yes(lines1)
#        for x in lines2:
#            print('xxxx',x,)
        split_into_files(lines2,odir)
    else:
        split_into_files(lines1,odir)

def reduce_predefines():
    global pre_defines
    pre_defines.sort()
    result = []
    for (A,B) in pre_defines:
        if not( (A,B) in result ):
            result = result + [(A,B)]
    pre_defines = result

def scan_for_defines(fileslist):
    return []

def get_ffiles():
    result = []
    for fname in ffiles:
        if not(os.access(fname,os.R_OK)):
            print('cannot open -f file ',fname)
            sys.exit(3)
        File = open(fname,'r')
        lines = File.readlines()
        ll = len(lines)
        for line in lines:
            if (len(line)>2):
                line = line[:-1].strip()
                if (line[0]=='~')or(line[0]=='/')or(line[0] in ascii_letters)or(line[0]=='.'):
                    result = result + [line]
    return result



def main():
    global pre_defines
    argv = sys.argv
    read_arguments(argv[1:])
    from_f = get_ffiles()
    all_files = files + from_f + libfiles
    defines1 = scan_for_defines(all_files)
    defines2 = defines+defines1
    predefines = defines2
    if not os.path.exists(odir):
        os.system('mkdir '+odir)
    for fname in all_files:
        fname  = absolute_file_name(fname)
        if (os.access(fname,os.R_OK)):
            print('working on file ',fname)
            work_on_file(fname)
        else:
            print('Error! skipping, cannot open verilog file ',fname,os.path.normpath(fname))
    dump_ff_file()
    write_defines()
    clean_temp_files()

def clean_temp_files():
    os.system('/bin/rm ver_macro_pp.temp*')

def dump_ff_file():
    if (len(modules)==0):
        return
    File = open('ver.ffiles','w')
    for module in modules:
        File.write(module+'\n')
    File.write('\n')
    File.close()


def read_arguments(argv):
    global use_defines
    use_defines=0
    was = ''
    global odir,defines,files,ffiles,ydirs,libfiles
    odir='tmp'
    files=[]
    ffiles=[]
    ydirs=[]
    libfiles=[]
    defines=[]
    for arg in argv:
        if (was==''):
            if (arg=='-f'):
                was = 'ffile'
            elif (arg=='-y'):
                was = 'ydir'
            elif (arg=='-use_define'):
                use_defines=1
            elif (arg=='-use_defines'):
                use_defines=1
            elif (arg=='-d'):
                was = 'define'
            elif (arg=='-v'):
                was = 'libfile'
            elif (arg=='-odir'):
                was = 'odir'
            elif (arg[0]=='-'):
                print('error! argument ',arg)
            else:
                files = files + [arg]
        elif (was=='odir'):
            odir = arg
            was=''
        elif (was=='ffile'):
            ffiles = ffiles + [arg]
            was=''
        elif (was=='define'):
            defines = defines + [(arg,'')]
            was=''
        elif (was=='ydir'):
            ydirs = ydirs + [arg]
            was=''
        elif (was=='libfile'):
            libfiles = libfiles + [arg]
            was=''
        else:
            print('error! argument ',arg,' was=',was)

def use_defines_yes(wholelib):
    result = []
    for line in wholelib:
        line2 = use_defines_on_line(line,pre_defines)
        result = result + [line2]
    return result

def use_defines_on_line(line,defines):
    origline = line
    wrds = line.split()
    if (len(wrds)>0)and(len(wrds[0])>=2):
        wrd = wrds[0]
        if (wrd[0:2]=='//'):
            return line
    ind = line.find('`')
    while (ind>=0):
        pre = line[0:ind]
        aft1 = line[ind:]
        x=1
        while (aft1[x] in alphas):
            x=x+1
        macro = aft1[1:x]
        if (macro=='define'):
            words = line.split()
            if (len(words)>=3):
                value = ' '.join(words[2:])
                defines = defines + [(words[1],value)]
            else:
               defines = defines + [(words[1],'')]
            line = ''
            ind= -1
        elif (macro=='timescale'):
           ind= -1
        elif (macro=='protect'):
           ind= -1
        elif (macro=='endprotect'):
           ind= -1
        elif (macro=='resetall'):
           ind= -1
        elif (macro=='celldefine'):
           ind= -1
        elif (macro=='endcelldefine'):
           ind= -1
        elif (macro=='include'):
           ind= -1
        else:
            aft = aft1[x:]
            ok = 'NOT EVER FOUND'
            for (M,V) in defines:
                if (M==macro):
                    ok = V
            if (ok=='NOT EVER FOUND'):
                print('error! macro ',macro,' not found in ',TopFileName,' line=',origline)
#                for (M,V) in defines:
#                    print((M,V))
            line = pre+' '+ok+' '+aft
            ind = line.find('`')
    return line

Longs = 0
def split_into_files(wholelib,dir):
    global modules,Longs
    state=0
    for line1 in wholelib:
        line = fix_stupid_problems(line1)
        wrds =  line.split()
        if (state==0):
            if (len(wrds)>0)and(wrds[0]=='module'):
                wrds=wrds[1].split('(')
                Module = wrds[0]
                if (Module[-1]==';'):
                    Module = Module[:-1]
                Module = relax(Module)

                if len(Module)>256:
                    Modl = 'longmodule%d' % Longs
                    File=open(dir+'/'+Modl+'.v','w')
                    Longs += 1
                else:
                    File=open(dir+'/'+Module+'.v','w')
                modules = [Module]+modules
#               if (not use_defines):
#                   for (A,B) in pre_defines:
#                       File.write('`define %s %s\n'%(A,B))
                File.write(line)
                print('opening ',Module)
                state=1
            elif (len(wrds)>0)and(wrds[0]=='primitive'):
                wrds=wrds[1].split('(')
                Module = wrds[0]
                if (Module[-1]==';'):
                    Module = Module[:-1]
                File=open(dir+'/'+Module+'.v','w')
                modules = [Module]+modules
#               if (not use_defines):
#                   for (A,B) in pre_defines:
#                       File.write('`define %s %s\n'%(A,B))
                File.write(line)
                print('opening p ',Module)
                state=10
        elif (state==1):
            if (len(wrds)>0)and(has_end(wrds[0])):
                File.write(line)
                File.close()
                state=0
            else:
                File.write(line)
        elif (state==10):
            if (len(wrds)>0)and(has_end(wrds[0])):
                File.write(line)
                File.close()
                state=0
            else:
                File.write(line)

def relax(Txt):
    for Chr in "'.\\/$=":
        Txt = Txt.replace(Chr,'_')
    return Txt

def has_end(word):
    if (word=='endmodule'):
        return 1
    if (word=='endprimitive'):
        return 1
    x = word.find('//')
    if (x>0):
        word = word[0:x]
        return has_end(word)
    x = word.find('/*')
    if (x>0):
        word = word[0:x]
        return has_end(word)
    return 0

def ok(state):
    if 0 in state:
        return 0
    return 1

def fix_stupid_problems(inline):
    for pattern in ["'b ","'h ","'d "]:
        ind  = 1
        while (ind>0):
            ind  = inline.find(pattern)
            if (ind>=0):
                inline = inline[0:ind+2]+inline[ind+3:]


    return inline

def absolute_file_name(fname):
    if (fname[0]=='~'):
        return os.path.expanduser(fname)
    if (fname[0]=='/'):
        return fname
    return os.path.abspath(fname)

def write_defines():
    if (not use_defines):
        File  = open('defines.v','w')
        for (A,B) in pre_defines:
            File.write('`define %s %s\n'%(A,B))
        File.close()

main()




