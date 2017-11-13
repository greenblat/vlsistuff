#! /usr/bin/python
'''
    invocation:    vcd_python <vcdfile> <python module>

    python module will get 


'''
import os,sys,string
import logs



def main():
    global observer
    Args = logs.parse_args()
    Fnames =Args['fnames']
    Fname= Fnames[0]
    Python = Fnames[1]
    if '-end' in Args:
        endTime = int(Args['-end'][-1])
    else:
        endTime = -1
    if '-start' in Args:
        startTime = int(Args['-start'][-1])
    else:
        startTime = 0

    if '.py' in Python: 
        Python = Python[:-3]
    if '/' in Python:
        ww = string.split(Python,'/')
        Path = string.join(ww[:-1],'/')
        Module = ww[-1]
    else:
        Path = '.'
        Module = Python
    sys.path.append(Path)
    
    exec('global observer; from %s import observer,setVar'%Module)
    File = open(Fname)
    read_headers(File)
    logs.log_info('loaded %d nets and regs'%(len(Codes.keys())))
    setVar('startTime',startTime)
    setVar('endTime',endTime)
#    skip_to_enddefinitions(File)
    work(File,startTime,endTime)




Codes={}
Codes2={}
def add_sig(Path,Sig,Wid,Code):
    Codes[Code]=Path+'.'+Sig
    Codes2[Path+'.'+Sig]=Code





linenum=0
outlinenum=0
Time=-1
def work(File,startTime,endTime):
    global Time,linenum
    while 1:
        line=File.readline()
        linenum +=1
        if (linenum % 1000000)==0:
            logs.log_info('line in=%d time=%s'%(linenum,Time))
        if (len(line)==0):
            return
        wrds = string.split(line)
        if (len(wrds)==0):
            pass
        elif (wrds[0]=='$dumpvars'):
            pass
        elif (wrds[0]=='$end'):
            pass
        elif (wrds[0][0]=='#'):
            Time = int(wrds[0][1:])
        elif (len(wrds)==2)and(wrds[0][0]=='b'):
            Str = wrds[0][1:]
            Code = wrds[1]
            if Code in Codes:
                Sig = Codes[wrds[1]]
                use_value(Sig,Str,Time)
        elif (len(wrds)==1):
            Str = wrds[0][0]
            Code = wrds[0][1:]
            if (Code in Codes):
                Sig = Codes[Code]
                use_value(Sig,Str,Time)



def use_value(Sig,Str,Time):
    observer(Sig,Str,Time)            
    


def skip_to_enddefinitions(File):
    while 1:
        line=File.readline()
        if (len(line)==0):
            return
        wrds = string.split(line)
        if (len(wrds)==0):
            pass
        elif (wrds[0]=='$enddefinitions'):
            return


def read_headers(File):
    state='idle'
    Path = []
    Pathstr = ''
    lnum=0
    while 1:
        line=File.readline()
        lnum += 1
        if (len(line)==0):
            logs.log_error('ended in headers')
            return
        wrds = string.split(line)
        if (len(wrds)==0):
            pass
        elif (wrds[0]=='$scope'):
            Path.append(wrds[2])
            Pathstr = string.join(Path,'.')
        elif (wrds[0]=='$var')and(wrds[1] in ['reg','wire','integer']):
            Wid = int(wrds[2])
            Code = wrds[3]
            Sig = wrds[4]
            add_sig(Pathstr,Sig,Wid,Code)
        elif (wrds[0]=='$upscope'):
            Path.pop(-1)
            Pathstr = string.join(Path,'.')
        elif (wrds[0]=='$enddefinitions'):
            logs.log_info('enddefs %d'%lnum)
            return
                    
                    



main()



        
