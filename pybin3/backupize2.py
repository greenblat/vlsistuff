#! /usr/bin/env python3
'''
    uses .backup files in hierarchy given to create one tar.gz backup file
    in the name there is date and who did it and from where.
'''
 
errors = 0

#import recordActivity
help_text = '\
 backupize2.py creates a backup file starting at current directory.  \n\
  it looks for .backup file, which is configuration file of backup.  \n\
 based on things read from .backup file and .backup files in son directories, one  \n\
 big <long file name with date>.tar.gz is created locally.  \n\
 currently parameter is [ -report ] which will list the files to be tarred without making tar.  \n\
  \n\
 format of .backup file:  \n\
 each line starts with keyword, followed by parameters  \n\
  \n\
 lines with keyword "file" will backup single (or wildcard) file[s]  \n\
 file  *.v   cucu.*  son/log.log   \n\
  \n\
 deep keyword, applied on directory tars the entire directory without further checks  \n\
 deep  important_files/  \n\
  \n\
 ignore  keyword, will ignore the entire directory (or several dirs) .   \n\
 this program will warn you of directories not treated by any line.  \n\
 ignore  temp_files junk   \n\
  \n\
 ignore_deep <dir1> <dir2> ...   <- will ignore deeply these files and directories.  \n\
  \n\
 byfile keyword, followed by directory name (or names) will try to read .backup file in these directories   \n\
 and will behave accordingly.  ignore files/directories are carried into these.  \n\
  \n\
 shallow directory <files1> <files2> ....  \n\
 similar to file keyword, but all files are searched only in directory and not deeper.  \n\
 '



example_backup = '\
deep  important_files llbin \n\
shallow  sequencer6 *.v *.mvlg \n\
shallow  green_src *.v *.mvlg \n\
shallow  fp_yellows *.v *.mvlg \n\
shallow  8051 *.v *.mvlg \n\
shallow  vsrc *.v *.mvlg \n\
shallow  vmisc *.v \n\
shallow  vendor_lib *.v \n\
byfile   tda synthesis vruns jtag_serial usim \n\
file derived/irmcf100_poststitch.v \n\
file derived/irmcf100.allrtl \n\
file *.mvlg \n\
ignore gen_fp empty_modules empty_shells drives logs celogs  orig.8051 minisyn \n\
ignore_deep INCA_libs  tmp  \n\
maxsize_deep 70 \n\
'



import os, sys,string
import tarfile
import datetime

for_real = 1
Objs = {}
StartFiles = []


class backup_class:
    def __init__(self,Path):
        self.Path=Path
        self.files = []
        self.ignores = []
        self.maxsize = 0
        self.maxsize_deep = 0
        self.ignores_deep = []
        self.deeps = []
        self.byfile = []
        self.shallows = []
        self.has_backup=0
    def read_deep(self):
        Locals=[]
        for By in self.byfile:
            Locals = Locals + [parse_backup_file(self.Path+'/'+By)]
        for Local in Locals:
            Local.read_deep()
            
    def propogate_globals(self):
        self.ignores = self.ignores + self.ignores_deep
        for By in self.byfile:
            Obj = Objs[self.Path+'/'+By]
            Obj.ignores_deep = Obj.ignores_deep + self.ignores_deep
            Obj.propogate_globals()
        
    def check_deep(self):
        self.check_yourself()
        for By in self.byfile:
            Obj = Objs[self.Path+'/'+By]
            Obj.check_deep()
        
    def check_yourself(self):
        if not os.path.exists(self.Path):
            return
        List = os.listdir(self.Path)
        for Item in List:
            if os.path.isdir(self.Path+'/'+Item):
               if ( (Item not in self.ignores) and 
                    (Item not in self.byfile) and 
                    (Item not in self.shallows) and 
                    (Item not in self.deeps) and
                    (Item[0]!='.')
                   ):
                   print('please check %s from %s'%(Item,self.Path),self.deeps,self.shallows)
                   has_errors(1)

    def deep_names(self):
        List = self.names_yourself()
        for By in self.byfile:
            Obj = Objs[self.Path+'/'+By]
            List = List + Obj.deep_names()
        return List

    def names_yourself(self):
        List = []
        if (self.has_backup==1):
            List = List + [self.Path+'/.backup']
        for F in self.deeps:
            List = List + [self.Path+'/'+F]
        for F in self.files:
            List = List + [self.Path+'/'+F]
        return List

def main():
    global for_real,StartFiles
    Path = '.'
    for arg in sys.argv[1:]:
        if (arg[0]=='-'):
            if (arg=='-report'):
                for_real=0
            else:
                print_help()
                return
        else:
            Path = arg
    StartFiles = [Path]
    BasePath = os.getcwd()
    while (StartFiles!=[]):
        Path1 = StartFiles[0]
        StartFiles = StartFiles[1:]
        if not os.path.exists(Path1):        
            print('path doesnot exist',Path1,os.getcwd())
        else:
            os.chdir(Path1)
            Tarname = run_one_backup_file('.')
            print('changing back to ',BasePath)
            os.chdir(BasePath)
            if (Path1==Path):
                print('>>>>>',Objs[Path].ignores_deep)
            if (Tarname != 0):
                if (for_real):
                    if Path1!='.':
                        os.system('/bin/mv %s/%s .'%(Path1,Tarname))
                else:
                    print('/bin/mv %s/%s .'%(Path1,Tarname))


def run_one_backup_file(Path):
    if not os.path.exists(Path+'/.backup'):        
        print('you must have "%s/.backup" file in start directory (try -help to get idea)'%(Path))
        has_errors(1)
        sys.exit() 
    parse_backup_file(Path)
    Top = Objs[Path]
    Top.read_deep()
    Top.propogate_globals()
    Top.check_deep()
    Tarname = get_backup_name(Path)

    tar = tarfile.open(Tarname, "w:gz")
    List = Top.deep_names()

    count = 0
    Total = len(List)

    for DDD in List:
       if (for_real):
           count=count+1
           print(count,' out of ',Total,DDD)
           if os.path.exists(DDD):        
               tar.add(DDD)
       else:
           print('adding ',DDD)
    tar.close()
    print('closing ',Tarname)
    return Tarname




def parse_backup_file(Path):
    Fname = Path+'/.backup'
    if not os.path.exists(Fname):        
        print('no .backup file in ',Path)
        has_errors(1)
        Obj =  backup_class(Path)
        Objs[Path]=Obj
        return Obj

    File = open(Fname,'r')
    lines = File.readlines()
    File.close()
    return use_backup_lines(Path,lines)

def use_backup_lines(Path,lines):
    global Objs,StartFiles
    Obj = backup_class(Path)
    Obj.has_backup=1
    Objs[Path]=Obj
    for line in lines:
        wrds = line.split()
        if (len(wrds)>0)and(is_not_comment(wrds[0])):
            if (wrds[0]=='ignore'):
                Obj.ignores.extend(clean_files_list(wrds[1:]))
            elif (wrds[0]=='ignore_deep'):
                Obj.ignores_deep.extend(clean_files_list(wrds[1:]))
            elif (wrds[0]=='file'):
                for wrd in wrds[1:]:
                    if ('*' in wrd):
                        ws = wrd.split('/')
                        ddd = '/'.join(ws[:-1])
                        if (ddd!='')and(ddd not in Obj.shallows):
                             Obj.shallows.append(ddd)
                        if (ddd==''):
                            ddd='.'
                        L11 = os.listdir(Path+'/'+ddd)
                        Mask = ws[-1]
                        for L2 in L11:
                            if compatible_wild_card(Mask,L2)and (not os.path.isdir(L2)):
                                Obj.files = Obj.files + [ddd+'/'+L2]
                    else:
                        if (os.path.exists(Path+'/'+wrd)):
                            ws = wrd.split('/')
                            ddd = '/'.join(ws[:-1])
                            if (ddd!='')and(ddd not in Obj.shallows):
                                Obj.shallows = Obj.shallows + [ddd]
                            Obj.files = Obj.files + [wrd]
                        else:
                            print('check: file doesnt exist ',Path,' ',wrd)
                            has_errors(1)
            elif (wrds[0]=='deep'):
                LL = clean_files_list(wrds[1:])
                for wrd in LL:
                    if (os.path.exists(Path+'/'+wrd)):
                        Obj.deeps = Obj.deeps + [wrd]
                    else:
                        print('check: directory/file doesnt exist ',Path,' ',wrd)
                        has_errors(1)
            elif (wrds[0]=='byfile'):
                Obj.byfile.extend(clean_files_list(wrds[1:]))
            elif (wrds[0]=='standalone'):
                StartFiles.extend(clean_files_list(wrds[1:]))
            elif (wrds[0]=='maxsize'):
                Obj.maxsize = int(wrds[1])
            elif (wrds[0]=='maxsize_deep'):
                Obj.maxsize_deep = int(wrds[1])
            elif (wrds[0]=='shallow'):
                Dir = clean_dir_name(wrds[1])
                Obj.shallows.extend(Dir)
                for wrd in wrds[2:]:
                    if ('*' in wrd):
                        L1 = os.popen('ls %s/%s/%s'%(Path,Dir,wrd)).readlines()
                        for L2 in L1:
                            L2 = L2[:-1]
                            W1 = '/'.split(L2)
                            Obj.files = Obj.files + [Dir+'/'+W1[-1]]
                    else:
                        Obj.files = Obj.files + [Dir+'/'+wrd]
            elif (wrds[0] in ['erase','remove','delete']):
                List = os.listdir(Obj.Path)
                Res = []
                for Fnamex in wrds[1:]:
                    if '*' in Fnamex:
                        for FF in List:
                            if matches_text(Fnamex,FF): Res.append(FF)
                    else:
                        Fnamey = '%s/%s'%(Obj.Path,Fnamex)
                        if os.path.exists(Fnamey): os.system('/bin/rm %s'%(Fnamey))
                if Res!=[]:
                    for FF in Res:
                        Fnamey = '%s/%s'%(Obj.Path,FF)
                        if os.path.exists(Fnamey): os.system('/bin/rm %s'%(Fnamey))
            elif (wrds[0]=='clear'):
                print('clear %s %s'%(os.getcwd(),str(wrds[1:])))
            else:
                print('check: error!  not a valid .backup keyword ',wrds[0])
                has_errors(1)
    return Obj

    if '*' in Dirin:
        List = os.listdir('.')
        Res=[]
        for Dir in List:
            if matches_text(Dirin,Dir):
                Res.append(Dir)
        return Res 


do_zip = True # set to false to debug

types = ["v", "py", "mvlg", "asm", "sas", "s", "makefile", "dino", "c", "h", "htm", "html", "doc", "pdf", "ucf",'prj','sdc','scn','pl','yacc','file']
fulldir = ["llbin", "important_files", "readmemh", "derived", "inst_set", "build"]
blockdir = ["work",'work2','workshop','work3','INCA_libs']
block_fname = ["ss_log_"]


def get_backup_name(Path):
    Date = datetime.date.today()
    Time = datetime.datetime.now()

    DDD = str(Date.day)+'_'+str(Date.month)+'_'+str(Date.year)+'_'+str(Time.hour)

    Pipe = os.popen('whoami','r')
    User = Pipe.read()
    Pipe.close

    Pipe = os.popen('hostname','r')
    HostName = Pipe.read()
    Pipe.close
    HostName = HostName[:-1]
    HostName = HostName.replace('.local','')

    Curdir = os.getcwd()+'/'+Path
    WWW = Curdir.split('/')
    if (WWW[-1]==''):
        WWW=WWW[:-1]
    if (WWW[-1]=='.'):
        WWW=WWW[:-1]
    if (len(WWW)>1):
        Last = WWW[-2]+'_'+WWW[-1]
    else:
        Last = WWW[-1]
    backup_name = 'b_'+HostName+'_'+Last+'_'+User[:-1]+'_'+DDD+'.tar.gz'
    print("opening %s (cur=%s) (%s)"%(backup_name,Curdir,os.getcwd()),WWW)
    return backup_name

def clean_dir_name(Dirin):
    if (Dirin[-1]=='/'):
        Dirin = Dirin[:-1]

    if '*' in Dirin:
        List = os.listdir('.')
        Res=[]
        for Dir in List:
            if matches_text(Dirin,Dir):
                Res.append(Dir)
        return Res
    return [Dirin]

def matches_text(Pattern,Text):
    Wrds = Pattern.split('*')
    Pos=-1
    for wrd in Wrds:
        if wrd!='':
            if wrd not in Text:
                return False
            ind=Text.index(wrd)
            if ind<=Pos:
                return False
            Pos=ind+len(wrd)
    return True



def clean_files_list(List):
    Res = []
    for F in List:
        Res.extend(clean_dir_name(F))
    return Res

def print_help():
    print('invocation: backupize2.py [-report] create backup tar.gz based on recursive .backup file')
    print(help_text)
    print('here is example of .backup file:')
    print(example_backup)

def has_errors(many):
    global errors
    errors = errors+many

def is_not_comment(word):
    if (word[0]=='*'):
        return 0
    if (word[0]=='/'):
        return 0
    return 1

def compatible_wild_card(Mask,Fname):
    if (Mask=='*'):
        return 1
    List = Mask.split('*')
    if (List[0]=='*'):
        List = List[1:]
    if (List[-1]=='*'):
        List = List[:-1]
    Indx = -1
    for M in List:
        Pos = Fname.find(M)
        if (Pos==-1):
            return 0
        if (Pos<Indx):
            return 0
        Indx=Pos
    return 1

if __name__=='__main__':
    main()
    if (errors):
        print('run had %d errors'%(errors))
    else:
        print('run had no errors')



