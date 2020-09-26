#! /usr/bin/env python3.8

HelpString = '''
    invocation: mWave.py  <csvfile> <ctrfile>
    format of csvfile:
        first line must be:   time,sig1,sig2,sig3,.....
        then all lines are numbers separated by comas
        first number in every line is time value.
        rest of the line are just values.
    the display is divided into number of panels.
    each panel can host several signals.
    panels are displayed one above the other.
    lines in control file:
        add <panelid> sig1 sig2 ....    panelid is number from 0 till some number not large (3,4,5,...10). 
        ones sig1 sig2               add each signal to new panel after last one
        smooth <panelid> sig1 <factor>     make smoothing of signal on len/factor base.  len is the number of datapoints. default factor is 8. smaller the factor smoothier the result.
        sum  <panelid> sig1 sig2 ...    create new signal (called _sumX) which is sum of sigs
        del <panelid> sig1 sig2 ...     delete signal from panel.
            sigs are names from the first line in csvfile.
        del * sig1 sig2 ...     delete these signals from all panels.
        reset_panels                     erase all panels and restart
        new <csvfilename>                restart all and load new csvfilename
        dofile   <filename>              execute control lines from file.
        source   <filename>              alias to the above.
        help                             print this text
        marker <time>                    draw vertical line
        wave <sigs>                      print values in time of these signals
        averages                         report averages of all signals
        quit or exit                     You guess what it is!
        for commands "add smooth sum" , if You omit the panel number, it creates new panel on top.
        You can type part command name, we match by the unique beginning


Keys pressed in the window:
    0  : display full time range
    2  : zoom in by 2, and pan to cursor
    5  : zoom out by 0.5, and pan to cursor
    Q  : quit 
    <esc>  : quit 
    : ;  :  goto control text window
    h  : help
    x  : remove vertical line at the cursor
    l  : list all loaded signals
    p  : dump png image of the screen

Keys pressed in panel signals listing
    a   : add new sig to panel (for names goes to text window)
    d   : delete sig from panel (for names goes to text window)

'''

import os,sys,string,types
import pyglet
from pyglet.window import mouse
import threading
import re

class GlobalsClass:
    def __init__(self):
        self.reset()

    def reset(self):
        self.PanelOffset=20
        self.Time0=0
        self.FullTime0=0
        self.Time1=1
        self.FullTime1=0
        self.Ind0=0
        self.Ind1=1
        self.Msx=0
        self.Msy=0
        self.Vertical=False
        self.graphicsChanged=True
        self.SigDb = {}
        self.SigSum = {}
        self.SigMax ={}
        self.SigMin ={}
        self.SigNames ={}
        self.CurVal ={}
        self.markers=[]
        self.CsvFileName=False
        self.Banner='iliaWaves greenblat@mac.com'
        self.sumNames=0
        self.SmoothWidth = 10
        self.LastMentionedSigs=[]
        self.Image=False
        self.displayImage=False
        self.finished=False



Glbs = GlobalsClass()

def main():
    global CmdFile,Thr
    Glbs.Pwd = os.path.realpath(os.path.curdir)
    Glbs.dirmode=False
    CmdFile = open_command_file()
    if len(sys.argv)==2:
        Fname =sys.argv[1]
        if os.path.isdir(Fname):
            print('isdir %s, assuming new dir format'%(Fname))
            Glbs.dirmode=True
            Names = os.listdir(Fname)
            Glbs.dirnames=Names
            Glbs.dirdir=Fname
            Glbs.CsvFileName=Fname
            Glbs.Banner='pwd=%s fname=%s'%(Glbs.Pwd,Glbs.CsvFileName)
            absorb_dir_times()
        elif '.csv' in Fname:
            Glbs.dirmode=False
            absorb_lines(Fname)
            report_averages()
            if CmdFile:
                CmdFile.write('new %s\n'%(Fname))
        else:
            execute_control_file(Fname)
    elif len(sys.argv)>2:
        if '.csv' in sys.argv[2]:
            absorb_lines(sys.argv[2])
        elif '.csv' in sys.argv[1]:
            absorb_lines(sys.argv[1])

        if 'cmd' in sys.argv[2]:
            execute_control_file(sys.argv[2])
        elif 'cmd' in sys.argv[1]:
            execute_control_file(sys.argv[1])
        report_averages()
    Thr = threading.Thread(target=execute_terminal_commands)
    Thr.start()
    reset_panels(3)
    pyglet.app.run()
    if CmdFile:
        CmdFile.close()
    

def open_command_file():
    Cnt = 1
    while True:
        Fname = 'cmd.%d'%Cnt
        if not os.path.exists(Fname):
            try:
                return open(Fname,'w')
            except:
                print('failed to open command trace file  (%s)'%Fname)
                return 0
        Cnt +=1

def execute_control_file(Fname):
    try:
        File = open(Fname)
    except:
        print('cannot open %s file'%Fname)
        return
    while 1:
        line = File.readline()
        if (len(line)==0):
            return
        wrds = line.split()
        use_command_wrds(wrds)


def expand_sigs(Sig):
        if '*' in Sig: 
            List = findSignals(Sig)
            return List
        if Sig not in Glbs.SigDb:
            print('sig %s not in database'%Sig)
            return []
        return [Sig]

def make_sure_sig_loaded(Sig):
    if Sig in Glbs.SigLoaded:
        return
    if not Glbs.dirmode:
        return
    load_sig_from_dirmode(Sig)    

def load_sig_from_dirmode(Sig):
    Fname = '%s/%s'%(Glbs.dirdir,Sig)
    File = open(Fname)
    Glbs.SigLoaded[Sig]=True
    while 1:
        line = File.readline()
        if line=='':
            print('loaded %s got %d  max=%f min=%f'%(Fname,len(Glbs.SigDb[Sig]),Glbs.SigMax[Sig],Glbs.SigMin[Sig]))
            return
        wrds=line.split()
        Val = float(wrds[0])
        Glbs.SigDb[Sig].append(Val)
        Glbs.SigSum[Sig] += Val
        if Sig not in Glbs.SigMax:
            Glbs.SigMax[Sig]=Val
        else:
            Glbs.SigMax[Sig]=max(Val,Glbs.SigMax[Sig])
        if Sig not in Glbs.SigMin:
            Glbs.SigMin[Sig]=Val
        else:
            Glbs.SigMin[Sig]=min(Val,Glbs.SigMin[Sig])

def use_command_wrds(wrds):
    if (CmdFile and (not CmdFile.closed) and (len(wrds)!=0)):
        CmdFile.write('%s\n'%' '.join(wrds))
    if len(wrds)==0:
        return
    elif (wrds[0]=='time'):
        Glbs.Time0 = int(wrds[1])
        Glbs.Time1 = int(wrds[2])
        set_vectors_start_stop()
    elif (wrds[0] in ['addones','ones']):
        if len(wrds)==1:
            Sigs = Glbs.LastMentionedSigs
            print('auto list',Sigs)
        else:
            Sigs=prepList(wrds[1:])
        for Sig in Sigs:
            if Sig in Glbs.SigNames:
                Panel = PanelClass(len(Panels))
                Panels.append(Panel)
                Panel.add(Sig)
            else:
                print('%s rejected'%Sig)
    elif (wrds[0]=='smooth'):
        Factor = is_it_factor(wrds[-1],8)
        if can_be_panel(wrds[1]):
            Pnl = pnl_int(wrds[1])
            Sigs = prepList(wrds[2:])
        else:
            Pnl = pnl_int('-')
            Sigs = prepList(wrds[1:])
        Len = len(Glbs.SigDb['time'])
        Glbs.SmoothWidth = Len/Factor
        print('smoothwidth=%d factor=%d datalen=%d'%(Glbs.SmoothWidth,Factor,Len))
        if len(Sigs)==0:
            print('no sigs given to smooth',wrds)
            return

        while len(Panels)<=Pnl:
            Panel = PanelClass(len(Panels))
            Panels.append(Panel)
        for Sig in Sigs:
            Name = 'avrg_%s'%(Sig)
            make_sure_sig_loaded(Sig)
            Glbs.SigLoaded[Name]=True
            Glbs.SigNames.append(Name) 
            List = Glbs.SigDb[Sig][:]
            List=smoothify(List)
            Glbs.SigDb[Name]=List
            Glbs.SigMax[Name]=Glbs.SigMax[Sig]
            Glbs.SigMin[Name]=Glbs.SigMin[Sig]
            Panels[Pnl].add(Name)

    elif (wrds[0]=='sum'):
        if len(wrds)==1:
            Pnl = pnl_int('-')
            Sigs = Glbs.LastMentionedSigs
            More = ' '.join(Sigs)
        elif can_be_panel(wrds[1]):
            Pnl = pnl_int(wrds[1])
            Sigs = wrds[2:]
            More = ' '.join(wrds[2:])
        else:
            Pnl = pnl_int('-')
            Sigs = wrds[1:]
            More = ' '.join(wrds[1:])
        Sigs = prepList(Sigs)
        for Sig in Sigs:
            make_sure_sig_loaded(Sig)
        if len(More)>10:
            More=More[:10]
        if len(Sigs)<1:
            print('no sigs in sum %s'%wrds[2:])
            return
        More = More.replace('*','+')
        Name = 's%d_%s'%(Glbs.sumNames,More)
        Glbs.SigNames.append(Name) 
        Glbs.SigLoaded[Name]=True
        Glbs.sumNames +=1
        while len(Panels)<=Pnl:
            Panel = PanelClass(len(Panels))
            Panels.append(Panel)
        Max = 0
        Glbs.SigDb[Name]=[]
        for i in range(len(Glbs.SigDb[Sigs[0]])):
            sum = 0
            for Sig in Sigs:
                sum += Glbs.SigDb[Sig][i]
            if (i==0):
                Min=sum
            else:
                Min = min(Glbs.SigMin[Sig],sum)
            Max = max(Max,sum)
            Glbs.SigDb[Name].append(sum)
        Glbs.SigMax[Name]=Max        
        Glbs.SigMin[Name]=Min        
        Panels[Pnl].add(Name)

    elif (wrds[0]=='png'):
        if Glbs.displayImage:
            Glbs.displayImage=False
        else:
            if len(wrds)>1:
                Name = wrds[1]
            else:
                Name = 'network.png'
            try:
                Glbs.Image = pyglet.image.load(Name)
                Glbs.displayImage=True
                print('loaded image %s'%Name)
            except:
                print('cannot load image %s'%Name)
                Glbs.displayImage=False
    elif (wrds[0]=='add'):
        if len(wrds)==1:
            Pnl = pnl_int('-')
            Sigs = Glbs.LastMentionedSigs
        elif can_be_panel(wrds[1]):
            Pnl = pnl_int(wrds[1])
            Sigs = wrds[2:]
        else:
            Pnl = pnl_int('-')
            Sigs = wrds[1:]
        List = prepList(Sigs)
        if len(List)==0:
            print('no sigs to add out of %s'%str(Sigs))
            return
        while len(Panels)<=Pnl:
            Panel = PanelClass(len(Panels))
            Panels.append(Panel)
        for Sig in Sigs:
            Panels[Pnl].add(Sig)
    elif (wrds[0]=='del'):
        Sigs = wrds[2:]
        if wrds[1]=='*':
            for Pnl in range(len(Panels)):
                for Sig in Sigs:
                    Panels[Pnl].delx(Sig)
            return
        try:
            Pnl = int(wrds[1])
            if len(Panels)<=Pnl:
                return
            for Sig in Sigs:
                Panels[Pnl].delx(Sig)
        except:
            for Pnl in range(len(Panels)):
                for Sig in Sigs:
                    Panels[Pnl].delx(Sig)
            return
    elif (wrds[0]=='reset_panels'):
        reset_panels(3)
    elif (wrds[0]=='averages'):
        report_averages()
    elif (wrds[0]=='new'):
        Glbs.reset()
        absorb_lines(wrds[1])
        report_averages()
    elif (wrds[0] in ['source','dofile']):
        execute_control_file(wrds[1])
    elif (wrds[0]=='help'):
        print(HelpString)
    elif (wrds[0]=='mark'):
        Glbs.markers.append(float(wrds[1]))
    elif (wrds[0]=='list'):
        if len(wrds)>1:
            Mask=wrds[1]
        else:
            Mask='*'
        listAllSignals(Mask)
    elif (wrds[0]=='desc'):
        if len(wrds)>1:
            Mask=wrds[1]
        else:
            Mask='*'
        descAllSignals(Mask)
    elif (wrds[0]=='wave'):
        if len(wrds)>1:
            Mask=wrds[1]
        else:
            Mask='*'
        L1 = findSignals(Mask)
        while len(L1)>=5:
            Now = L1[:5]
            L1=L1[5:]
            waves_of_one(Now)
        if len(L1)>0:
            waves_of_one(L1)
    elif (wrds[0]=='print'):
        if len(wrds)>1:
            Fname=wrds[1]
        else:
            Fname='screenshot.png'
        printScreen()
    elif (wrds[0] in ['quit','exit']):
        print('thanks and see you again')
        Glbs.finished=True
        sys.exit()
    elif matchesCommand(wrds[0]):
        Comm = matchesCommand(wrds[0])
        wrds[0]=Comm
        use_command_wrds(wrds)
        return
    else:
        print('dont know to %s'%wrds)
    Glbs.graphicsChanged=True
        
ValidCommandsTxt = '''
    time
    ones
    smooth
    sum
    add
    del
    reset_panels
    averages
    new
    dofile
    source
    help
    desc
    mark
    list
    wave
    print
    quit exit
'''
ValidCommands = ValidCommandsTxt.split()
ValidCommands.sort()

def matchesCommand(Wrd0):
    res=[]
    for Comm in ValidCommands:
        if startsTheSame(Wrd0,Comm):
            res.append(Comm)
    if len(res)==1:
        return res[0]
    if len(res)>1:
        print('ambigious command %s matches %s'%(Wrd0,res))
    elif len(res)==0:
        print('valid cmds: %s'%ValidCommands)

    return False
    

def startsTheSame(Wrd0,Comm):
    Len = len(Wrd0)
    if Len >len(Comm):
        return False
    Part = Comm[:Len]
    return Part==Wrd0

def is_it_factor(Txt,Default):
    try:
        Fact = int(Txt)
        return Fact
    except:
        return Default

def smoothify(List):
    res = List[:]
    for i in range(len(List)):
        res[i]=smooth_op(List,i,Glbs.SmoothWidth)
    return res

def smooth_op(List,i,Width):
    sum=0
    for j in range(i-Width/2,1+i+Width/2):
        if (j<0):
            sum += List[0]
        elif (j>=len(List)):
            sum += List[-1]
        else:
            sum += List[j]
    return int(1.0*sum/Width)
        


def can_be_panel(Txt):
    if Txt=='-':
        return True
    try:
        x = int(Txt)
    except:
        return False
    return True

def pnl_int(Txt):
    if Txt=='-':
        return len(Panels)
    try:
        Pnl = int(Txt)
    except:
        print('panel should be a number (or - for last) , you typed %s'%Txt)
        Pnl =  len(Panels)
    return  Pnl

def waves_of_one(Now):
    Head=''
    for Sig in Now:
       Head += '  %s (%d:%d)'%(Sig,Glbs.SigMax[Sig],Glbs.SigMin[Sig])
    print('waves: %s'%Head)
    tt = Glbs.SigDb['time']
    for i in range(len(tt)):
        print(tt[i])
        for S in Now:
            print(' %d '%(Glbs.SigDb[S][i]))


def prepList(wrds):
    Sigs=[]
    for wrd in wrds:
        if '*' in wrd:
            List = findSignals(wrd)
            Sigs.extend(List)
        elif (wrd in Glbs.SigNames):
            Sigs.append(wrd)
        else:
            print('dropped unexisting sig %s'%wrd)
    Sigs.sort()
    return Sigs
def printScreen(Fname='screenshot.png'):
    pyglet.image.get_buffer_manager().get_color_buffer().save(Fname)

def set_vectors_start_stop():
    ok=True
    ii=0
    try:
       Tlist = Glbs.SigDb['time']
    except:
       return
    while ok and(ii<len(Tlist)):
        if Tlist[ii]>=Glbs.Time0:
            Glbs.Ind0=ii
            ok=False
        else:
            ii+=1
    if ii==len(Tlist):
        print('time0 was not found in times vector')
        Glbs.Ind0=0
    ii=len(Tlist)-1
    while ok and(ii>0):
        if Tlist[ii]<=Glbs.Time1:
            Glbs.Ind1=ii
            ok=False
        else:
            ii-=1
    if ii==0:
        print('time1 was not found in times vector')
        Glbs.Ind1=len(Tlist)-1

def X2Time(X):
    if X>Glbs.PanelOffset:
        Wx = window1.width-Glbs.PanelOffset
        Tx = Glbs.Time1-Glbs.Time0
        Ratio = 1.0 * (X-Glbs.PanelOffset) /Wx
        Time = Tx * Ratio + Glbs.Time0
        return Time
    return 0

def report_sig_values_at_cursor():
    X,_Y=Glbs.Vertical
    Time = X2Time(X)
    Ind0,Ind1,Ratio = findTimeIndex(Time)
    print('\n\n values at @%sns %d:%d '%(int(Time),Ind0,Ind1))
    for Panel in Panels:
        for Sig in Panel.Sigs:
            LL = Glbs.SigDb[Sig]
            Len = len(LL)
            if (Ind0>=Len)or(Ind1>=Len):
                print('warning sig=%s len=%d donot fit ind01 = %d : %d'%(Sig,Len,Ind0,Ind1))
                Val=0
            else:
                Val0 = LL[Ind0]
                Val1 = LL[Ind1]
                Val = (Val0*Ratio+Val1*(1.0-Ratio))
            print('%20s  = %.3f'%(Sig,Val))
            Glbs.CurVal[Sig]=Val
        
def findTimeIndex(Time):
    try:
        Tlist = Glbs.SigDb['time']
    except:
        return 0
    Last = len(Tlist)-1
    First=0
    if (Time>=Tlist[Last]):
        return Last,Last,1.0
    if (Time<=Tlist[First]):
        return First,First,1.0
    for Pos in range(First,Last-1):
        if (Time>=Tlist[Pos])and(Time<=Tlist[Pos+1]):
            Diff0 = Time-Tlist[Pos]
            Diff = Tlist[Pos+1]-Tlist[Pos]
            Ratio = 1.0 - (1.0*Diff0/Diff)
            return Pos,Pos+1,Ratio
    return Last,Last,1.0
     

def findTimeIndex_good(Time):
    try:
        Tlist = Glbs.SigDb['time']
    except:
        return 0
    Pos = len(Tlist)/2
    Last = len(Tlist)-1
    First = 0
    if (Time>=Tlist[Last]):
        return Last
    if (Time<=Tlist[First]):
        return First
    while 1:
        if (Last==First):
            return Last
        Pos = (Last+First)/2
        if (Time>=Tlist[Pos])and(Time<=Tlist[Pos+1]):
            Diff0 = Time-Tlist[Pos]
            Diff1 = Tlist[Pos+1]-Time
            if (Diff0<Diff1):
                return Pos
            else:
                return Pos+1


    Step = Pos/2
    while 1:
        if (Step<2):
            return Pos
        if (Time==Tlist[Pos]):
            return Pos
        elif (Time>Tlist[Pos]):
            if (Pos>=Last):
                return Pos
            elif (Time<=Tlist[Pos+1]):
                return Pos
        elif (Time<Tlist[Pos]):
            if (Pos==0):
                return Pos
            elif (Time>=Tlist[Pos-1]):
                return Pos

        if (Time>Tlist[Pos]):
            Pos = Pos + Step
            Step = Step / 2
        elif (Time<Tlist[Pos]):
            Pos = Pos - Step
            Step = Step / 2
            
        

def report_averages():
    tmp=[]
    for Sig in Glbs.SigNames:
        wrds = Sig.split('.')
        if (len(wrds)==2):
            Pref=wrds[1]
        else:
            Pref=wrds[0]
        tmp.append((Pref,Sig))
    tmp.sort()
    for _,Sig in tmp:
        Sum = Glbs.SigSum[Sig]
        Len = len(Glbs.SigDb[Sig])
        Ave = Sum/Len
        print('%s = %f  < %d  < %f'%(Sig,Glbs.SigMin[Sig],Ave,Glbs.SigMax[Sig]))

def absorb_dir_times():
    Names = Glbs.dirnames
    Glbs.SigNames=[]
    Glbs.SigLoaded={}
    for Sig in Glbs.dirnames:
        if '.time' not in Sig:
            Glbs.SigDb[Sig]=[]
            Glbs.SigSum[Sig]=0
            Glbs.SigNames.append(Sig)
    for Name in Names:
        if '.time' in Name:
            File = open('%s/%s'%(Glbs.dirdir,Name))
            Glbs.SigDb['time'] =[]
            Glbs.SigSum['time'] = 0
            Glbs.Ind0=0
            Glbs.Ind1=0
            while 1:
                line = File.readline()
                if line=='':
                    Glbs.Ind1 =len(Glbs.SigDb['time'])
                    return
                wrds=line.split()
                Val = float(wrds[0])
                Glbs.Time1 = max(Glbs.Time1,Val)
                Glbs.FullTime1=Glbs.Time1
                if (Glbs.Time0<0):
                    Glbs.Time0=Val
                    Glbs.FullTime0=Val
                Glbs.SigDb['time'].append(Val)
                Glbs.SigSum['time'] += Val

def absorb_lines(Fname):
    try:
        File = open(Fname)
    except:
        print('cannot open csv file %s'%Fname)
        return
    Glbs.CsvFileName=Fname
    Glbs.Banner='pwd=%s fname=%s'%(Glbs.Pwd,Glbs.CsvFileName)
    line = File.readline()
    Glbs.SigNames = line[:-1].split(',')
    Glbs.SigLoaded={}
    if Glbs.SigNames[0]!='time':
        print('first line must start with token "time"')
        sys.exit()
    for Sig in Glbs.SigNames:
        Glbs.SigDb[Sig]=[]
        Glbs.SigSum[Sig]=0
        Glbs.SigLoaded[Sig]=True
    Glbs.Time0=-1
    Glbs.Ind0=0
    Glbs.Ind1=0
    print('header sig names',Glbs.SigNames)
    while 1:
        line = File.readline()
        if line=='':
            return
        wrds = line[:-1].split(',')
        if len(wrds)==len(Glbs.SigNames):
            Glbs.Ind1 +=1
            for ii in range(len(Glbs.SigNames)):
                Sig =Glbs.SigNames[ii]
                    
                Val = float(wrds[ii])
                if (Sig=='time'):
                    Glbs.Time1 = max(Glbs.Time1,Val)
                    Glbs.FullTime1=Glbs.Time1
                    if (Glbs.Time0<0):
                        Glbs.Time0=Val
                        Glbs.Ind0=0
                        Glbs.FullTime0=Val
                Glbs.SigDb[Sig].append(Val)
                Glbs.SigSum[Sig] += Val
                if Sig not in Glbs.SigMax:
                    Glbs.SigMax[Sig]=Val
                else:
                    Glbs.SigMax[Sig]=max(Val,Glbs.SigMax[Sig])
                if Sig not in Glbs.SigMin:
                    Glbs.SigMin[Sig]=Val
                else:
                    Glbs.SigMin[Sig]=min(Val,Glbs.SigMin[Sig])
        else:
            print('line dropped ',len(wrds),len(Glbs.SigNames),wrds)

def findSignals(Mask='*'):
    L1=[]
    for Sig in Glbs.SigNames:
        if mask_fits(Sig,Mask):
            L1.append(Sig)
    Glbs.LastMentionedSigs = L1
    return L1

def listAllSignals(Mask='*'):
    L1 = findSignals(Mask)
    while len(L1)>5:
        print(' '.join(L1[:5]))
        L1 = L1[5:]
    print(' '.join(L1))
        
def descAllSignals(Mask='*'):
    L1 = findSignals(Mask)
    for Sig in L1:
        ww = Sig.split('.')
        if len(ww)==2:
            if ww[0]=='999':
                Key = ww[1]
                try:
                    Desc = desc_globals[Key]
                except:
                    Desc = '????'
                print('%20s   :    %s'%(Sig,Desc))
            else:
                Key = ww[1]
                try:
                    Desc = desc_per_chip[Key]
                except:
                    Desc = '????'
                print('%20s   :    %s'%(Sig,Desc))
        




def mask_fits(Sig1,Mask1):
    if Sig1 in ['time']:
        return False
    Sig = Sig1.lower()
    Mask = Mask1.lower()
    if Mask=='*':
        return True
    if Sig==Mask:
        return True
    if '*' not in Mask1:
        return False
    Pattern = Mask1.replace('*','.*')+'$'
    Result = re.match(Pattern, Sig1)
    if Result:
        return True
    return False

    Stars = count_stars(Mask)
    if (Stars==2)and(Mask[-1]=='*')and(Mask[0]=='*'):
        return Mask[1:-1] in Sig
    if (Stars==1)and(Mask[-1]=='*'):
        return starts_same(Sig,Mask[:-1])
    if (Stars==1)and(Mask[0]=='*'):
        return ends_same(Sig,Mask[1:])
    if (Stars==1):
        Parts = Mask.split('*')
        return starts_same(Sig,Parts[0])and ends_same(Sig,Parts[1])

    if (Stars>1):
        Parts = Mask.split('*')
        Pos=0
        Sigi=Sig

        OkSkip=False
        for Part in Parts:
            if Part=='':
                OkSkip=True
            else:
                X = Sigi.find(Part)
                if X<0:
                    return False
                if not OkSkip and X>0:
                    return False
                        
                Sigi = Sigi[X:]
                OkSkip=True
        return True 
    return False

def count_stars(Txt):
    i=0
    for Chr in Txt:
        if Chr=='*':
            i+=1
    return i
def starts_same(Txt,Mask):
    Lm = len(Mask)
    Lt = len(Txt)
    if Lt<Lm:
        return False
    return Mask==Txt[:Lm]

def ends_same(Txt,Mask):
    Lm = len(Mask)
    Lt = len(Txt)
    if Lt<Lm:
        return False
    return Mask==Txt[-Lm:]

def screenDimensions():  
    return window1.width,window1.height

COLORS = [
    [255,0,0],
    [0,255,0],
    [100,100,255],
    [255,255,0],
    [255,0,255],
    [0,255,255],
    [255,0,100],
    [0,255,100],
    [100,200,255],
    [255,255,100],
    [255,100,255],
    [100,255,255]
]


class PanelClass:
    def __init__(self,Id):
        self.Id=Id
        self.Sigs=[]
        self.verts={}
        self.labels={}
        self.frames=[]
        self.ftxts=[]
        self.colors={}
        self.longestName=0

    def hit(self,X,Y):
        Sx,Sy = screenDimensions()
        StepY = (Sy-30)/len(Panels)
        Y0 = StepY*self.Id
        Y1 = StepY*(self.Id+1)
        return (Y>Y0)and(Y<Y1)

    def add(self,Sig):
        if '*' in Sig:
            List = findSignals(Sig)
            for S in List:
                self.add(S)
            return
        make_sure_sig_loaded(Sig)
        if Sig not in Glbs.SigDb:
            print('sig %s not in database'%Sig)
            return
        if Sig not in self.Sigs:
            self.Sigs.append(Sig)
            if len(Sig)>self.longestName:
                self.longestName=len(Sig)
        if Sig not in self.colors:
            Ind = self.Sigs.index(Sig)
            self.colors[Sig]= COLORS[(self.Id+Ind)%len(COLORS)]
        Glbs.graphicsChanged=True


    def delx(self,Sig):
        L1=[]
        for S1 in self.Sigs:
            if mask_fits(S1,Sig):
                L1.append(S1)
        if L1==[]:
            return
        for S1 in L1:
            ind = self.Sigs.index(S1)
            self.Sigs.pop(ind)
            if S1 in self.verts:
                self.verts.pop(S1)
            if S1 in self.labels:
                self.labels.pop(S1)
            if S1 in self.colors:
                self.colors.pop(S1)
            self.longestName=0
            for S1 in self.Sigs:
                self.longestName=max(self.longestName,len(S1))
        Glbs.graphicsChanged=True



    def draw(self):
        if ('time' not in Glbs.SigDb):
            return
        Sx,Sy = screenDimensions()
        StepY = (Sy-30)/len(Panels)
        Y0 = StepY*self.Id
        X0 = Glbs.PanelOffset
        X1 = Sx
        Max1= -10e9
        Min1= +10e9
        i=0
        while i<len(self.Sigs):
            Sig =self.Sigs[i]
            if Sig not in Glbs.SigMin:
                self.Sigs.pop(i)
            else:
                i+=1
        for Sig in self.Sigs:
            Min=Glbs.SigMin[Sig]
            Max=Glbs.SigMax[Sig]
            Max1 = max(Max,Max1)
            Min1 = min(Min,Min1)
        if (Max1>Min1):
            ScaleY = 0.95*StepY/(Max1-Min1)
        else:
            ScaleY = 1.0
        ScaleX = 1.0*(Sx-Glbs.PanelOffset)/(Glbs.Time1-Glbs.Time0)
        vertex_list1 = pyglet.graphics.vertex_list(2,
                 ('v2i',(Glbs.PanelOffset,int(Y0),int(Sx),int(Y0)))
                 ,('c3B', (50,50,50,50,50,50))
                 )
        vertex_list2 = pyglet.graphics.vertex_list(2,
                 ('v2i',(int(Glbs.PanelOffset),int(Y0),int(Glbs.PanelOffset),int(Y0+StepY)))
                 ,('c3B', (50,50,50,50,50,50))
                 )
        self.frames = [vertex_list1,vertex_list2]
        if Min1<Max1:
            M1lbl = pyglet.text.Label('%.2f'%(Min1),
                          font_name='Times New Roman',
                          font_size=12,
                          color=xglcolor('white'),
                          x=Glbs.PanelOffset+5, y=10+Y0,
                          anchor_x='left', anchor_y='center')
            M2lbl = pyglet.text.Label('%.2f'%(Max1),
                          font_name='Times New Roman',
                          font_size=12,
                          color=xglcolor('white'),
                          x=Glbs.PanelOffset+5, y=-10+Y0+StepY,
                          anchor_x='left', anchor_y='center')
            self.ftxts  = [M1lbl,M2lbl]
        

        Tlist = Glbs.SigDb['time']
        for Sig in self.Sigs:
            Ind = self.Sigs.index(Sig)
            if Sig in Glbs.CurVal:
                Val = Glbs.CurVal[Sig]
                if type(Val) is int:
                    Txt = '%s %d'%(Sig,Glbs.CurVal[Sig])
                else:
                    Txt = '%s %.3f'%(Sig,Glbs.CurVal[Sig])
            else:
                Txt = Sig
            lbl = pyglet.text.Label(Txt,
                          font_name='Times New Roman',
                          font_size=12,
                          color=list(self.colors[Sig])+[255],
                          x=1, y=10+StepY*self.Id+((StepY-20)/len(self.Sigs))*Ind,
                          anchor_x='left', anchor_y='center')
            self.labels[Sig]=lbl
            Points = []
            List = Glbs.SigDb[Sig]
            for Ind in range(Glbs.Ind0,Glbs.Ind1):
                try:
                    Val = List[Ind]
                except:
                    Val=0
                XX = (Tlist[Ind]-Glbs.Time0)*ScaleX
                YY = (Val-Min1)*ScaleY
                Points.append(X0+int(XX))
                Points.append(Y0+int(YY))
            Colors=self.colors[Sig]*(int(len(Points)/2))
            vertex_list = pyglet.graphics.vertex_list(
                 int(len(Points)/2),
                 ('v2i', tuple(map(int,Points)))
                 ,('c3B', tuple(Colors))
                 )
            self.verts[Sig] = vertex_list
            


Panels=[]
def reset_panels(Many):
    Panels=[]
    for i in range(Many):
        Panel = PanelClass(i)
        Panels.append(Panel)
    
    Glbs.graphicsChanged=True


Labels=[]

window1 = pyglet.window.Window(resizable=True)
# window1.push_handlers(pyglet.window.event.WindowEventLogger())
label1 = pyglet.text.Label('XLS waves',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window1.width//2, y=window1.height//2,
                          anchor_x='center', anchor_y='center')
Labels=[]
Lines=[]

@window1.event
def on_resize(width,height):
    Glbs.graphicsChanged=True


def update_graphics():
    if Glbs.finished:
        sys.exit()
    if not Glbs.graphicsChanged:
        return
    Glbs.graphicsChanged=False
    Glbs.longest=0
    for Panel in Panels:
        Glbs.longest=max(Glbs.longest,Panel.longestName)
    Glbs.PanelOffset = Glbs.longest*10 + 60
    for Panel in Panels:
        Panel.draw()

@window1.event
def on_draw():
    update_graphics()
    window1.clear()
    if Glbs.displayImage:
        Ww = window1.width
        Wh = window1.height
        Ih = Glbs.Image.height
        Iw = Glbs.Image.width
        Scale1 = 1.0 * Ww/Iw
        Scale2 = 1.0 * Wh/Ih
        Scale = min(Scale1,Scale2)

        sprite = pyglet.sprite.Sprite(Glbs.Image)
        sprite.scale = Scale
        sprite.draw()
        return

    draw_rect(0,0,window1.width,window1.height,'black')
    draw_label(Glbs.Banner,(window1.width+Glbs.PanelOffset)/2,window1.height-15,'yellow','center',13)
    draw_horizontal(0,window1.width,window1.height-30,'magenta')
    draw_label('t0=%.2f'%(Glbs.Time0),Glbs.PanelOffset+5,window1.height-15,'white')
    draw_label('t1=%.2f'%(Glbs.Time1),window1.width-70,window1.height-15,'white')
    for Label in Labels:
        Label.draw()
    for Panel in Panels:
        for Vert in Panel.frames:
            Vert.draw(pyglet.gl.GL_LINE_STRIP)
        for Sig in Panel.verts:
            Panel.verts[Sig].draw(pyglet.gl.GL_LINE_STRIP)
        for Sig in Panel.labels:
            Panel.labels[Sig].draw()
        for Txt in Panel.ftxts:
            Txt.draw()

    for Time in Glbs.markers:
        draw_time_marker(Time)

    if Glbs.Vertical:
        (X,Y)=Glbs.Vertical
        if X>Glbs.PanelOffset:
            Wx = window1.width-Glbs.PanelOffset
            Tx = Glbs.Time1-Glbs.Time0
            Ratio = 1.0 * (X-Glbs.PanelOffset) /Wx
            Time = Tx * Ratio + Glbs.Time0
            draw_label('%.3f'%(Time),X,10,'white')
            draw_vertical(X,0,window1.height-30,'white')


def draw_time_marker(Time):
    if Time<Glbs.Time0:
        return
    Wx = window1.width-Glbs.PanelOffset
    Tx = Glbs.Time1-Glbs.Time0
    Rx = Time-Glbs.Time0
    Ratio1 = 1.0*Rx/Tx
    XX = int(Glbs.PanelOffset + Ratio1 * Wx)
    draw_label('%.3f'%(Time),XX,10,'white')
    draw_vertical(XX,0,window1.height-30,'yellow')


def draw_rect(X0,Y0,X1,Y1,Color):
   colory=xglcolor(Color)
   colorx=colory[:-1]*4
   vlist = pyglet.graphics.vertex_list(4,
        ('v2i',(X0,Y0,X1,Y0,X1,Y1,X0,Y1))
       ,('c3B', colorx))   
   vlist.draw(pyglet.gl.GL_POLYGON)


def draw_horizontal(X0,X1,Y0,Color):
   colory=xglcolor(Color)
   colorx=colory[:-1]+colory[:-1]
   vlist = pyglet.graphics.vertex_list(2,
        ('v2i',(X0,Y0,X1,Y0))
       ,('c3B', colorx))   
   vlist.draw(pyglet.gl.GL_LINES)

def draw_vertical(X,Y0,Y1,Color):
   colory=xglcolor(Color)
   colorx=colory[:-1]+colory[:-1]
   pyglet.gl.glEnable(pyglet.gl.GL_LINE_STIPPLE)
   pyglet.gl.glLineStipple(1, 0x3333)
   vlist = pyglet.graphics.vertex_list(2,
        ('v2i',(X,Y0,X,Y1))
       ,('c3B', colorx)   
       ,('t2i', (0,1,2,3))   
   )
   vlist.draw(pyglet.gl.GL_LINES)
   pyglet.gl.glDisable(pyglet.gl.GL_LINE_STIPPLE)

def draw_label(Text,X,Y,Color,AnchorX='left',FontSize=12):
    lbl = pyglet.text.Label(Text,
          font_name='Times New Roman',
          font_size=FontSize,
          color=xglcolor(Color),
          x=X+1, y=Y,
          anchor_x=AnchorX, anchor_y='center')
    lbl.draw()    
GLCOLORS = {}
GLCOLORS['white']=[255,255,255,255]
GLCOLORS['red']=[255,0,0,255]
GLCOLORS['green']=[0,255,0,255]
GLCOLORS['blue']=[0,0,255,255]
GLCOLORS['cyan']=[0,255,255,255]
GLCOLORS['magenta']=[255,0,255,255]
GLCOLORS['yellow']=[255,255,0,255]
GLCOLORS['black']=[0,0,0,255]
def xglcolor(Color):
    if Color in GLCOLORS:
        return GLCOLORS[Color]
    return xglcolor('black')

def execute_terminal_commands():
    while 1:
        Txt = input('?:')
        wrds = Txt.split()
        if len(wrds)>0:
            use_command_wrds(wrds)



def do_command_line():
    Txt = raw_input('?:')
    wrds = Txt.split()
    if len(wrds)==0:
        return
    use_command_wrds(wrds)
    do_command_line()

def pan_window_left():
    Glbs.graphicsChanged=True
    Diff = 0.6*(Glbs.Time1-Glbs.Time0)
    Glbs.Time1 -= Diff
    Glbs.Time0 -= Diff
    set_vectors_start_stop()
def pan_window_right():
    Glbs.graphicsChanged=True
    Diff = 0.6*(Glbs.Time1-Glbs.Time0)
    Glbs.Time1 += Diff
    Glbs.Time0 += Diff
    set_vectors_start_stop()

def draw_marker_line():
    Time = X2Time(Glbs.Msx)
    Glbs.markers.append(float(Time))
    Glbs.markers.sort()
    if len(Glbs.markers)<2:
        return
    for i in range(len(Glbs.markers)-1):
        X0 = Glbs.markers[i]
        X1 = Glbs.markers[i+1]
        Diff = X1-X0
        print('markers diff = %d'%int(Diff))
        
    Glbs.graphicsChanged=True
def zoom_in_cursor(Factor):
    Glbs.graphicsChanged=True
    if (Factor=='full'):
        Glbs.Time0 = Glbs.FullTime0
        Glbs.Time1 = Glbs.FullTime1
        set_vectors_start_stop()
        return

    Time = X2Time(Glbs.Msx)
    Diff = (Glbs.Time1-Glbs.Time0)/2
    Now = Diff/Factor
    Glbs.Time0 = Time -Now
    Glbs.Time1 = Time +Now
    set_vectors_start_stop()

def remove_something():
    X0 = Glbs.Msx-5
    X1 = Glbs.Msx+5
    Y0 = Glbs.Msy-5
    Y1 = Glbs.Msy+5
    if X1<Glbs.PanelOffset:
        for i in range(len(Panels)):            
            Panel = Panels[i]
            if Panel.hit(Glbs.Msx,Glbs.Msy):
                Panels.pop(i)
                for i in range(len(Panels)):            
                    Panel = Panels[i]
                    Panel.Id=i
                Glbs.graphicsChanged=True
                return
        return     
     
    if (Glbs.Vertical):
        X,Y = Glbs.Vertical
        if (X<=X1)and(X>=X0):
            Glbs.Vertical=False
            return
    for i in range(len(Glbs.markers)):
        Xw = Glbs.markers[i]
        Xs,Ys = xworld2screen(Xw,0)
        if (Xs<=X1)and(Xs>=X0):
            Glbs.markers.pop(i)
            return


def xworld2screen(X,Y):
     Wx = window1.width-Glbs.PanelOffset
     Tx = Glbs.Time1-Glbs.Time0
     Ratio = 1.0 * (X-Glbs.Time0)/Tx
     Dist = Wx * Ratio + Glbs.PanelOffset
     return Dist,Y
    

def add_waveform_to_panel():
    for Panel in Panels:
        if Panel.hit(Glbs.Msx,Glbs.Msy):
            add_sig_to_panel_from_text(Panel)
            
def add_sig_to_panel_from_text(Panel):
    Txt = raw_input('type signal name[s]:')
    wrds = Txt.split()
    if len(wrds)==0:
        return
    for Sig in wrds:
        Panel.add(Sig)
    

def del_waveform_from_panel():
    for Panel in Panels:
        if Panel.hit(Glbs.Msx,Glbs.Msy):
            del_sig_from_panel_from_text(Panel)
            
def del_sig_from_panel_from_text(Panel):
    Txt = raw_input('type signal name[s]:')
    wrds = Txt.split()
    if len(wrds)==0:
        return
    for Sig in wrds:
        Panel.delx(Sig)
        

KeysMac ={}
KeysMac['a'] = 97
KeysMac['d'] = 100
KeysMac['x'] = 120
KeysMac['p'] = 112
KeysMac['h'] = 104
KeysMac['l'] = 108
KeysMac['2'] = 50
KeysMac['5'] = 53
KeysMac['0'] = 48
KeysMac['q'] = 113

KeysLinux ={}
KeysLinux['a'] = 97
KeysLinux['d'] = 100
KeysLinux['x'] = 120
KeysLinux['p'] = 112
KeysLinux['h'] = 104
KeysLinux['l'] = 108
KeysLinux['2'] = 50
KeysLinux['5'] = 53
KeysLinux['0'] = 48
KeysLinux['q'] = 113
KeysLinux['m'] = 109

def keysCode(Char):
    if os.path.exists('/Users/ilia'):
        try:
            return KeysMac[Char]
        except:
            return 0
    try:
        return KeysLinux[Char]
    except:
        return 0

@window1.event
def on_text_motion(motion):
    if motion==pyglet.window.key.MOTION_RIGHT:
        pan_window_right()
    elif motion==pyglet.window.key.MOTION_LEFT:
        pan_window_left()

@window1.event
def on_key_press(symbol, modifiers):
#    lbl = pyglet.text.Label(str(symbol),
#          font_name='Times New Roman',
#          font_size=9,
#          x=Glbs.Msx, y=Glbs.Msy,
#          anchor_x='center', anchor_y='center')
#    Labels.append(lbl)
    if (symbol==keysCode('q'))and(modifiers==1):   # Q key
        sys.exit()
    elif (symbol==keysCode('p')):
        printScreen()
    elif (symbol==keysCode('h')):
        print(HelpString)
    elif (symbol==keysCode('l')):
        listAllSignals()
    elif (symbol==keysCode('2')):
        zoom_in_cursor(2.0)
    elif (symbol==keysCode('m')):
        draw_marker_line()
    elif (symbol==keysCode('5')):
        zoom_in_cursor(0.5)
    elif (symbol==keysCode('x')):
        remove_something()
    elif (symbol==keysCode('a')):
        add_waveform_to_panel()
    elif (symbol==keysCode('d')):
        del_waveform_from_panel()
    elif (symbol==keysCode('0')):
        zoom_in_cursor('full')
    else:
        print('key code=%d mod=%d unused'%(symbol,modifiers))

@window1.event
def on_mouse_press(x, y, button, modifiers):
    Glbs.Vertical=(x,y)
    Glbs.graphicsChanged=True
    report_sig_values_at_cursor()


@window1.event
def on_mouse_leave(x,y):
    return
@window1.event
def on_mouse_enter(x,y):
    return
@window1.event
def on_move(x,y):
    Glbs.Msx=x
    Glbs.Msy=y
@window1.event
def on_mouse_motion(x,y,dx,dy):
    Glbs.Msx=x
    Glbs.Msy=y

@window1.event
def on_mouse_release(x,y,button,modifiers):
    return

@window1.event
def on_mouse_drag(x,y,dx,dy,buttons,modifiers):
    return
@window1.event
def on_key_release(symbol,modifiers):
    return

@window1.event
def on_deactivate():
    return

@window1.event
def on_text(text):
    return

desc_globals={}
desc_per_chip={}
def build_xlswavemeanings():
    Lines= XLSWAVEMEANING.split('\n')
    for line in Lines:
        wrds = line.split(',')
        if len(wrds)==2:
            ww = wrds[0].split('.')
            Desc = wrds[1]
            if ww[0]=='999':
                desc_globals[ww[1]]=Desc
            else:
                desc_per_chip[ww[1]]=Desc






XLSWAVEMEANING = '''
999.step,current step number in STEPS sequence
999.mark,user defined marker
999.genrate,number of mcell bits produced by all generators in Gbit/sec
999.genlp,total number of low priority cells generated in last period
999.genhp,total number of high priority cells generated in last period
999.rate,number of cells reaching destination in Gbit/sec
999.intransit,number of cells generated; but not yet sunk.
999.totalBackPressures,total number of BP indications. helpful in estimating the status of the simulation.
999.backPressureFtoTx,total number of blocked Txs in ftos 
999.backPressureTower,total number of blocked towers
999.backPressureStopNp,total number of stop np requests (by voq)
999.backPressureIbfStopFpga,total number of ibf requests to stop voq
999.backPressureStopAll,total number of stop all indications to voqs.
999.backPressureStopLow,total number of stop low indications to voqs.
999.backPressureStopFto,total number of stop fto indications to voqs.
999.bpcells,number of back pressure mcells generated
999.onehops,number of onehop mcells received in all sinks.
999.twohops,number of onehop mcells received in all sinks. 

<chip>.zerobanks0,fpga_back: number of ddr banks with zero waiting.
<chip>.zerobanks1,fpga_back: number of ddr banks with zero waiting.
<chip>.reorder0,fpga_reorder: total length of reorder fpga0 queue
<chip>.reorder1,fpga_reorder: total length og reorder fpga1 queue

<chip>.StopDobfLow0,fgpa_reorder0: stops low traffic from dobf.
<chip>.StopDobfHigh0,fpga_reorder0: stops high traffic from dobf.
<chip>.StopDobfLow1,fpga_reorder1: reorder 1 stops low traffic from from chip.
<chip>.StopDobfHigh1,fpga_reorder1: reorder 1 stops high traffic from from chip.

<chip>.flowfifo0,fpga_back: number of mcells from fpga back to np0
<chip>.flowfifo1,fpga_back: number of mcells from fpga back to np1
<chip>.flowfifo2,fpga_back: number of mcells from fpga back to np2

<chip>.burst0,gen0: in np0 gen:length of burst queue
<chip>.burst1,gen1: in np1 gen:length of burst queue 
<chip>.burst2,gen2: in np2 generator; current number of burst cells.
<chip>.genhp0,gen0: number of hi-pri mcells generated (dli) by np0
<chip>.genlp0,gen0: number of LowPri mcells generated (dli) by np0
<chip>.genhp1,gen1: number of hi-pri mcells generated (dli) by np1
<chip>.genlp1,gen1: number of LowPri mcells generated (dli) by np1
<chip>.genhp2,gen2: number of hi-pri mcells generated (dli) by np2
<chip>.genlp2,gen2: number of LowPri mcells generated (dli) by np2

<chip>.eops0,gen0: number of eop mcells in np0 queue.
<chip>.eops1,gen1: number of eop mcells in np1 queue
<chip>.eops2,gen2: number of eop mcells in np2 queue

<chip>.sinkrate0,sink0: rate of mcells in Gbit/sec sunk at Np0
<chip>.sinkrate1,sink1: rate of mcells in Gbit/sec sunk at Np1
<chip>.sinkrate2,sink2: rate of mcells in Gbit/sec sunk at Np2

<chip>.0dlylo,sink_np0: arrival delay ro np0 sink of low-pri mcells
<chip>.0dlyhi,sink_np0: arrival delay ro np0 sink of high-pri mcells
<chip>.sinkh0,sink_np0: number of hi-pri mcells sunk by np0
<chip>.sinkl0,sink_np0: number of LowPri mcells sunk by np0
<chip>.1dlylo,sink_np1: arrival delay ro np0 sink of low-pri mcells
<chip>.1dlyhi,sink_np1: arrival delay ro np0 sink of high-pri mcells
<chip>.sinkh1,sink_np1: number of hi-pri mcells sunk by np1
<chip>.sinkl1,sink_np1: number of LowPri mcells sunk by np1
<chip>.2dlylo,sink_np2: arrival delay for np2 sink of low-pri mcells
<chip>.2dlyhi,sink_np2: arrival delay for np2 sink of hi-pri mcells
<chip>.sinkh2,sink_np2: number of hi-pri mcells sunk by np2
<chip>.sinkl2,sink_np2: number of hi-pri mcells sunk by np2
<chip>.chip2Fpga0Stop,ibf0: stops voq because ibf is too full
<chip>.chip2Fpga1Stop,ibf1: stops voq because ibf is too full
<chip>.chip2FpgaSlows,"number of ""slow"" requests from the network to voq"
<chip>.chip2FpgaCrawls,"number of ""crawl"" requests from the network to voq"
<chip>.chip2FpgaLowsTh,number of twohops blocked for low traffic
<chip>.chip2FpgaAllsTh,number of twohops blocked for all traffic
<chip>.chip2FpgaLowsDbf,number of dobfs blocked for low traffic
<chip>.chip2FpgaAllsDbf,number of dobfs blocked
<chip>.stopFto0,dobf asks to stop ftos
<chip>.stopLow0,dobf asks to stop low traffic
<chip>.stopAll0,dobf asks to stop all traffic
<chip>.dbfhp0,dbuf0: number of hi-pri mcells alive in dobf
<chip>.dbflp0,dbuf0: number of lo-pri mcells alive in dobf
<chip>.bellyDobf0,dobf0: number of mcells sitting in dobf0
<chip>.bellyDobf1,number of mcells sitting in dobf1
<chip>.stopFto1,dobf asks to stop ftos
<chip>.stopLow1,dobf asks to stop low traffic
<chip>.stopAll1,dobf asks to stop all traffic
<chip>.dbfhp1,dbuf 1 number of hi-pri mcells
<chip>.dbflp1,dbuf 1 number of lo-pri mcells
<chip>.inOptics,chip: number of mcells arrived to this chip during last interval (dli)
<chip>.outOptics,chip: number of mcells leaving this chip (dli)
<chip>.fpga2chip,number of mcells from voq to chip (dli)
<chip>.chip2fpga,number of mcells sent from chip to reorders (dli)
<chip>.belly,number of mcells alive inside chip
<chip>.bellyfpga,number of mcells alive in half card fpgas (voq reorder and back)
<chip>.lowcap,lowest current capacity of voq in percents per flow.
<chip>.fgpaStopNp,fpga_voq stops all NPs because it's queues load.
<chip>.QueueStopped,total length of voq queues
<chip>.voqlp,number of lo-pri mcells going from voq to ibf in (dli)
<chip>.voqhp,number of hi-pri mcells going from voq to ibf in (dli)
<chip>.stopNpLow0,ibf: how many dobfs asked to stop low traffic to Np0
<chip>.stopNpLow1,ibf: how many dobfs asked to stop low traffic to Np1
<chip>.stopNpLow2,ibf: how many dobfs asked to stop low traffic to Np2
<chip>.stopNpAll0,ibf: how many dobfs asked to stop all traffic to Np0
<chip>.stopNpAll1,ibf: how many dobfs asked to stop all traffic to Np1
<chip>.stopNpAll2,ibf: how many dobfs asked to stop all traffic to Np2
<chip>.perNpAll0,dobf: asks to stop all traffic to Np0
<chip>.perNpAll1,dobf: asks to stop all traffic to Np0
<chip>.perNpAll2,dobf: asks to stop all traffic to Np0
<chip>.perNpLow0,dobf: asks to stop low traffic to Np0
<chip>.perNpLow1,dobf: asks to stop low traffic to Np0
<chip>.perNpLow2,dobf: asks to stop low traffic to Np0


<chip>.outcntlo0,reorder fpga: number of low mcells in ordered fifo going to NP0
<chip>.outcntlo1,reorder fpga: number of low mcells in ordered fifo going to NP1
<chip>.outcntlo2,reorder fpga: number of low mcells in ordered fifo going to NP2
<chip>.outcnthi0,reorder fpga: number of hi mcells in ordered fifo going to NP0
<chip>.outcnthi1,reorder fpga: number of hi mcells in ordered fifo going to NP1
<chip>.outcnthi2,reorder fpga: number of hi mcells in ordered fifo going to NP2
<chip>.0maxlo,sink0: max delay on low mcells arriving to NP0 during last sampling period
<chip>.1maxlo,sink1: max delay on low mcells arriving to NP1 during last sampling period
<chip>.2maxlo,sink2: max delay on low mcells arriving to NP2 during last sampling period
<chip>.0maxhi,sink0: max delay on hi mcells arriving to NP0 during last sampling period
<chip>.1maxhi,sink1: max delay on hi mcells arriving to NP1 during last sampling period
<chip>.2maxhi,sink2: max delay on hi mcells arriving to NP2 during last sampling period

<chip>.fcnt0,ibf: number of mcells in processed-mcells fifo 0 (mcells got routing)
<chip>.fcnt1,ibf: number of mcells in processed-mcells fifo 0 (mcells got routing)
<chip>.fcnt00,ibf: number of mcells in entrance fifo 0 from voq 
<chip>.fcnt11,ibf: number of mcells in entrance fifo 1 from voq
<chip>.voqTotal,fpga_voq: total number of mcells in voq fpga

<chip>.txBlocked0,fto: number of blocked tx in fto 0
<chip>.txBlocked1,fto: number of blocked tx in fto 1
<chip>.txBlocked2,fto: number of blocked tx in fto 2
<chip>.txBlocked3,fto: number of blocked tx in fto 3
<chip>.txBlocked4,fto: number of blocked tx in fto 4
<chip>.txBlocked5,fto: number of blocked tx in fto 5
<chip>.txBlocked6,fto: number of blocked tx in fto 6
<chip>.txBlocked7,fto: number of blocked tx in fto 7
<chip>.txBlocked8,fto: number of blocked tx in fto 8
<chip>.txBlocked9,fto: number of blocked tx in fto 9

<chip>.twrBlocked0,fto: number of blocked twr in fto 0
<chip>.twrBlocked1,fto: number of blocked twr in fto 1
<chip>.twrBlocked2,fto: number of blocked twr in fto 2
<chip>.twrBlocked3,fto: number of blocked twr in fto 3
<chip>.twrBlocked4,fto: number of blocked twr in fto 4
<chip>.twrBlocked5,fto: number of blocked twr in fto 5
<chip>.twrBlocked6,fto: number of blocked twr in fto 6
<chip>.twrBlocked7,fto: number of blocked twr in fto 7
<chip>.twrBlocked8,fto: number of blocked twr in fto 8
<chip>.twrBlocked9,fto: number of blocked twr in fto 9

<chip>.dobf2ro0,dobf: number of bits sent by dobf to fpga 0 during last period
<chip>.dobf2ro1,dobf: number of bits sent by dobf to fpga 1 during last period
<chip>.stp_fpga0,ibf: entry fifo on port 0 is too full (>IBF_FIFO00_TOO_FULL)
<chip>.stp_fpga1,ibf: entry fifo on port 1 is too full (>IBF_FIFO00_TOO_FULL)

'''






build_xlswavemeanings()

main()





