#! /usr/bin/python


import os,sys,string
import veri
import logs

TOOMANYBADS = 9000
Filename = 'sequence.stil'
Patterns=[]
started=0
PatternName = ['"PATTERN"']
CLOCKS = []

class swav_class:
    def __init__(self,Swavname,Indx):
        if not os.path.exists(Swavname):
            print 'swav file cannot be opened',Swavname
            veri.finish()
            sys.exit()
        self.File = open(Swavname,'read')
        self.Logf = open('swav.logfile'+str(Indx),'write')
        self.Recordf = open('record.swav'+str(Indx),'write')
        self.state='idle'
        self.emitting=0
        self.swavsig={}
        self.swavpos={}
        self.ithlen=0
        self.buffer=[]
        self.linenum=0
        self.goods=0
        self.bads=0
        self.cycle=1
        self.pattern=[]
        self.activeline=0
        state='idle'
        pos=0
        while (self.state!='work'):
            line = self.File.readline()
            if (len(line)==0)or(self.state=='quit'):
                print '>>>>> %s'%(self.swavsig)
                return
            self.linenum = self.linenum+1
            line = string.replace(line,';',' ; ')
            line = string.replace(line,'{',' { ')
            self.Recordf.write(line)
            wrds = string.split(line)
            if (len(wrds)>0):
                if (state=='idle'):
                    if (wrds[0]=='SignalGroups'):
                        state='SignalGroups'
                    elif (wrds[0]=='Pattern'):
                        state='pattern'
                        PatternName[0] = wrds[1];
                elif (state=='SignalGroups'):
                    if '}' == wrds[0]:
                        state='idle'
                    elif wrds[1]=='=':
                        Vector = line
                        x = Vector.index("'")
                        Vector = Vector[x+1:]
                        x = Vector.index("'")
                        Vector = Vector[:x]
                        Vector= string.replace(Vector,'+',' ')
                        Sigs = string.split(Vector)
                        pos=0
                        for Sig in Sigs:
                            self.add_swav_sig(Sig,pos)
                            pos=pos+1
                elif (state=='pattern'):
                    self.fill_buffers("74")
                    self.state='work'
    def add_swav_sig(self,Name,Pos): 
        self.swavsig[Name]=Pos
        self.swavpos[Pos]=Name
        if (Pos>=self.ithlen):
            self.ithlen=Pos+1
    def fill_buffers(self,Where):
        self.comment=0
        self.state='idle'
        if (len(self.buffer)>1000): return
        while (len(self.buffer)<20000)or(self.comment==1)or(self.state!='idle'):
            line = self.File.readline()
            line = string.replace(line,';',' ; ')
            line = string.replace(line,'{',' { ')
##            self.Recordf.write(line)
            self.linenum +=1
            useit=1
            if (len(line)==0):
#                print '%s buffer ended len=%d lnum=%d emittded=%d %d %s %s'%(Where,len(self.buffer),self.linenum,self.cycle,self.emitting,self.state,self.comment)
                return
            if (self.comment):
                useit=0
                ind = string.find(line,'*/')
                if (ind>=0):
                    self.comment=0
            if (not self.comment):
                ind = string.find(line,'/*')
                if (ind>=0):
                    ind2 = string.find(line,'*/')
                    if (ind2<0):
                        self.comment=1
                    line=line[0:ind]    
            self.Logf.write('useit=%d %d %s %s %d\n'%(useit,self.comment,line[:-1],line[:-1],self.linenum))
#            print '%s buffer used len=%d lnum=%d emittded=%d %d %s %s'%(Where,len(self.buffer),self.linenum,self.cycle,self.emitting,self.state,self.comment)
            if (useit):
                self.use_line(line)
#        print '%s buffer filled len=%d lnum=%d emittded=%d %d %s %s'%(Where,len(self.buffer),self.linenum,self.cycle,self.emitting,self.state,self.comment)
    def use_line(self,line):
        wrds = string.split(line)
        X = match_line(line,'V { ? = ? ; }')
        if X:
            (_,Vector)=X
            self.buffer.append((self.linenum,Vector))
#            print 'buffer append %d'%(len(self.buffer))
        elif (':' in line):
            line = string.replace(line,'"','')
            line = string.replace(line,':','')
            line = line[:-1]
            self.buffer.append((self.linenum,'marker',line))
        else:
            X = match_line(line,'Stop ;')
            if X:
                self.state='quit'



    def emit_pattern(self):
        if (len(self.buffer)==0):
            return 0 
#        print 'emit_pattern len=%d %s'%(len(self.buffer[0]),self.buffer[0])
        if (len(self.buffer[0])==3):
            (self.activeline,marker,self.marker) = self.buffer[0]
            veri.force('tb.marker',str(self.activeline))
            for i in range(8):
                mrkr = self.marker
                if (len(mrkr)>8):
                    mrkr = mrkr[-8:]
                if (len(mrkr)>i):
                    Ch = ord(mrkr[i])
                else:
                    Ch = ord(' ')
                veri.force('tb.mrkr%d'%(i),str(Ch))
            self.Logf.write('marker %s\n'%(self.marker))
            self.Recordf.write('marker %s ;\n'%(self.marker))
            self.buffer=self.buffer[1:]
            return self.emit_pattern()
        else:
            (self.activeline,self.pattern) = self.buffer[0]
            self.cycle += 1
            veri.force('tb.cycles',str(self.cycle))
            if ((self.cycle % 100)==0):
                print 'cycle ',self.cycle
            veri.force('tb.fline',str(self.activeline))
            self.emitting+=1
            self.buffer=self.buffer[1:]
            for Ind in range(0,self.ithlen):
                Char = self.pattern[Ind]
                Sig = self.swavpos[Ind]
                if (Sig in CLOCKS):
                    force_sig(Sig,'0')
                else:
                    force_sig(Sig,Char)
            return 1


    def pulse_clocks(self):
        for Ind in range(0,self.ithlen):
            Char = self.pattern[Ind]
            Sig = self.swavpos[Ind]
            if (Char=='+')or((Sig in CLOCKS)and(Char=='1')):
                force_sig(Sig,'1')
        return 1

    def un_pulse_clocks(self):
        for Ind in range(0,self.ithlen):
            Char = self.pattern[Ind]
            Sig = self.swavpos[Ind]
            if (Char=='+')or(Sig in CLOCKS):
                force_sig(Sig,'0')
        return 1




    def print_fail(self,What,Sig,Char,Now):
        Str = '%s %s exp=%s act=%s vec=%d line=%d cycle=%d time=%s\n'%(What,Sig,str(Char),str(Now),self.emitting,self.activeline,self.cycle,str(veri.stime()))
        logs.log_wrong(Str)
        self.bads += 1
        veri.force('tb.bads',str(self.bads))



    def check_pattern(self):
        Exit = ''
        Failed = False
        for Ind in range(0,self.ithlen):
            Char = self.pattern[Ind]
            Sig = self.swavpos[Ind]
            Exit = Exit + Char
            if (Char == '?'):
                Now = veri.peek('tb.'+Sig)
                Exit= Exit[0:-1]+look(NN)
            elif (Char in ['H','L'])and (Sig != 'sda'):
                Now = veri.peek('tb.'+Sig)
                if ((not(Now=='0'))and(Char=='L')):
                    self.bads=self.bads+1
                    Failed = True
                    self.print_fail('fail0',Sig,Char,Now)
                    Exit= Exit[0:-1]+look(Now)
                elif ((not(Now=='1'))and(Char=='H')):
                    self.bads=self.bads+1
                    Failed = True
                    self.print_fail('fail1',Sig,Char,Now)
                    Exit= Exit[0:-1]+look(Now)
                elif (Now in ['X','Z','x','z'])and(Char in ['L','H']):
                    self.bads=self.bads+1
                    Failed = True
                    self.print_fail('failx',Sig,Char,Now)
                    Exit= Exit[0:-1]+look(Now)
                else:
                    self.goods=self.goods+1
                if (self.bads>TOOMANYBADS):
                    print 'too many fails'
                    self.Logf.close()
                    self.Recordf.write('pattern_end %s ;\n'%(PatternName[0]))
                    self.Recordf.close()
                    veri.finish()
                else:
                    veri.force('tb.bads',str(self.bads))
                    veri.force('tb.goods',str(self.goods))
        if ((self.activeline % 100)==0):
            logs.log_info('goods=%d bads=%d pattern_width=%d activeline=%d '%(self.goods,self.bads,self.ithlen,self.activeline))
        if (Failed):
            self.Recordf.write('V { bist = %s ; } /* %5d fail exp=%s */\n'%(Exit,self.activeline,self.pattern))
        else:
            self.Recordf.write('V { bist = %s ; } /* %5d */\n'%(Exit,self.activeline))

# V  {  bist = 000LHXXXXXX11 ;  }




def starting():
    global pattern
    global started
    global Patterns
    started=1
#    veri.force('top.avdd','1800')
#    veri.force('top.vdd33','3300')
    Fnames = string.split(Filename,':')
    print 'starting ',Fnames,len(Fnames)
    if (len(Fnames)==1):
        Patterns = []
        pattern = swav_class(Filename,0)
    else:
        pattern = swav_class(Fnames[0],1+len(Patterns))
        Patterns = Fnames[1:]

def force_sig(Sig,Char):
    if (Char in ['X','H','L','?','x','h','l']):
        veri.force('tb.'+Sig+'_dr','0')
        if (Char=='H'):
            veri.force('tb.'+Sig+'_va','1')
        elif (Char=='L'):
            veri.force('tb.'+Sig+'_va','0')
#        elif (Char in ['x','X']):
#            veri.force('tb.'+Sig+'_va','x')
    elif (Char in ['0','1']):
        veri.force('tb.'+Sig+'_dr','1')
        veri.force('tb.'+Sig+'_va',Char)
def look(In):
    if (In=='0'):
        return 'L'
    if (In=='1'):
        return 'H'
    return 'X'



def end_reason(Why):
    File = open('end_reason','write')
    File.write(Why+'\n')
    File.close()
    veri.finish()


def match_line(Line,Pattern):
    wrds1 = string.split(Line)
    wrds2 = string.split(Pattern)
    if len(wrds2)!=len(wrds1):
        return False
    res=[]
    for (Ind,Pat) in enumerate(wrds2):
        Val=wrds1[Ind]
        if Pat=='?':
            res.append(Val)
        elif (Pat!=Val):
            return False
    if res!=[]:
        return tuple(res)
    return True


def force_sigs():
    global Patterns
    global pattern
    if (not started):
        starting()
    pattern.fill_buffers("302")
    done = pattern.emit_pattern()
    if (done==0):
        pattern.Logf.close()
        pattern.Recordf.write('pattern_end %s ;\n'%PatternName[0])
        pattern.Recordf.close()
        if (len(Patterns)>0):
            pattern = swav_class(Patterns[0],len(Patterns))
            pattern.fill_buffers("310")
            done = pattern.emit_pattern()
            Patterns = Patterns[1:]
        else:
            print 'goods=%d bads=%d'%(pattern.goods,pattern.bads)
            if (pattern.bads>0):
                end_reason('failed on bads')
            elif (pattern.goods>0):
                end_reason('Success')
            else:
                end_reason('Nothing happenned')
            veri.finish()

def check_sigs():
    global pattern
    if (not started):
        starting()
    pattern.check_pattern()

def pulse_clocks():
    global pattern
    pattern.pulse_clocks()

def un_pulse_clocks():
    global pattern
    pattern.un_pulse_clocks()

state = 'idle'
def run():
    global state
    if state=='idle':
        starting()
        state='ready'
    elif state=='ready':
        force_sigs()
        state='checks'
    elif state=='checks':
        check_sigs()
        state='clocks'
    elif state=='clocks':
        pulse_clocks()
        state='after'
    elif state=='after':
        un_pulse_clocks()
        state='ready'

    

