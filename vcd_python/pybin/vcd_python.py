#! /usr/bin/python
HELP = '''
    invocation:    vcd_python <vcdfile> <python module> [-path PATH] [-path PATH] [-print paths] [-print nets]
        [-start TIME] [-end TIME]  

    if no -path is given, all hierarchy signals are kept,
    if at least one -path is given, only signals in mentioned paths are monitored. (it reduces work).

    TIME is in vcd time units. so if in vcd appears line "#100234566"   - i dont look at NanoS/PicoS/FemtoSec, i just compare the number.


    -print paths will print all paths in vcd and exit.
    -print nets  will print all nets that are monitored an exit.

'''
import os,sys,string
import logs



def main():
    global observer
    if len(sys.argv)==1: 
        print HELP
        print PROTOTYPE
        return
    Args = logs.parse_args()
    if '-help' in Args:
        print HELP
        print PROTOTYPE
        return
        
    Fnames =Args['fnames']
    Fname= Fnames[0]
        
    if len(Fnames)>1:
        Python = Fnames[1]
    else:
        Python = False
    if '-end' in Args:
        endTime = int(Args['-end'][-1])
    else:
        endTime = -1
    if '-start' in Args:
        startTime = int(Args['-start'][-1])
    else:
        startTime = 0

    if Python:
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


    if '-path' in Args:
        mainPaths = Args['-path']
    else:
        mainPaths = False
    read_headers(File,mainPaths)
    logs.log_info('loaded %d nets and regs'%(len(Codes.keys())))
    if '-print' in Args:
        Whats = Args['-print']
        if 'paths' in Whats:
            for Path in allPaths:
                logs.log_info('path %s'%Path)
        if 'nets' in Whats:
            for Code in Codes:
                LL = Codes[Code]
                for Sig in LL:
                    logs.log_info('net %s %s'%(Code,Sig))
        return
        


    setVar('startTime',startTime)
    setVar('endTime',endTime)
#    skip_to_enddefinitions(File)
    if Python:
        work(File,startTime,endTime)




Codes={}
def add_sig(Path,Sig,Wid,Code,keepPaths):
    This = Path+'.'+Sig
    if not keepPaths:
        if Code not in Codes:
            Codes[Code]= [This]
        else:
            Codes[Code].append(This)
        return

    if Path in keepPaths:
        if Code not in Codes:
            Codes[Code]= [This]
        else:
            Codes[Code].append(This)






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



def use_value(Sigs,Str,Time):
    for Sig in Sigs:
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

allPaths = []

def read_headers(File,mainPaths):
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
            allPaths.append(Pathstr)
        elif (wrds[0]=='$var')and(wrds[1] in ['reg','wire','integer']):
            Wid = int(wrds[2])
            Code = wrds[3]
            Sig = wrds[4]
            add_sig(Pathstr,Sig,Wid,Code,mainPaths)
        elif (wrds[0]=='$upscope'):
            Path.pop(-1)
            Pathstr = string.join(Path,'.')
        elif (wrds[0]=='$enddefinitions'):
            logs.log_info('enddefs %d'%lnum)
            return
        elif (wrds[0][0]=='#'):
            logs.log_info('enddefs %d'%lnum)
            return
                    
                    
PROTOTYPE = '''

#example of python file


import logs
import string
cycles=0

def get_cycles():
    return cycles

logs.get_cycles = get_cycles

Values = {}
Base = 'tb.top.cpu'
def peek(Sig):
    if (',' in Sig)or(' ' in Sig):
        Sig1 = string.replace(Sig,',',' ')
        ww = string.split(Sig)
        res=[]
        for AA in ww:
            Val = peek(AA)
            res.append(Val)
        return res

    Full = '%s.%s'%(Base,Sig)
    if Full not in Values:
        logs.log_error('sig %s not in path %s'%(Sig,Base))
        return -1
    return logs.intx(Values[Full][0])

argv={}
def setVar(Var,Val):
    argv[Var]=Val


Panics = []
Clk0=0
def observer(Sig,Str,Time):
    global cycles,Clk0
    Values[Sig]=(Str,Time)
    if Time<argv['startTime']:
        return
    if '%s.clk'%Base not in Values: return
    Clk = peek('clk')
    if ('panic' in Sig)and(Sig not in Panics): Panics.append(Sig)
    if (Clk==0)and(Clk0==1):
        negedge(Time)
        cycles += 1
    Clk0 = Clk

    if (argv['endTime']>0)and (Time>=argv['endTime']):
        logs.log_info('exiting on time=%d because of endTime=%d'%(Time,argv['endTime']))
        sys.exit()

def negedge(Time):
# put your code here
    if (peek('valid')==1)and(peek('ready')==1):
        data = peek('rdata')
        logs.log_info('new data arrived "%x"'%data)
    return

'''



main()



        
