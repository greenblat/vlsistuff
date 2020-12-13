


import logs
import veri
import sys,os,string
import random

#built in commands: finish,wait,marker,force,print,define,include,exec

# finish    # kill simulation
# wait 100    # dont do for 100 clocks
#marker 5     # shortcut for "force tb.marker 5"
# force rst 1   # plain force (uses given self.Path path as prepend )
#print some words   # if any word matches real signal name - it will be peeked and printed as sig=val
#define vector 0x345
#include filename   # full of the above commands

#most of parameters above go through eval() - it means "define variable value" works in translation of eval.

# accessing installed agents: goes by their nickname. rest of command is send to .action(self,Cmd) string.
#agents:   apb write 0x200 0x300

#checking on agent that is not busy (finished all jobs)
#agents:   apb notbusy


#

# def initialSequence(Fname):


class sequenceClass:
    def __init__(self,Path,Monitors,SEQUENCE='',AGENTS=[],Translates={}):
        self.Path = Path
        Monitors.append(self)
        self.Sequence = SEQUENCE.split('\n')
        self.workIncludes()
        self.waiting = 0
        self.waitNotBusy = False
        self.agents={}
        self.Translates = Translates
        self.Translates['rnd'] = self.rnd
        for (Nickname,Object) in AGENTS:
            self.agents[Nickname]=Object
        self.searchPath = ['.'] 


    def rnd(self,Low,High):
        L,H = self.eval(Low),self.eval(High)
        X = random.randint(L,H)
        return X


    def readfile(self,Filename):
        File = open(Filename)
        List = File.readlines()
        File.close()
        for Line in List:
            if len(Line)>1:
                self.Sequence.append(Line[:-1])
        self.searchPath.append(os.path.abspath(os.path.dirname(Filename)))
        self.workIncludes()


    def workIncludes(self):
        Dones = True
        while Dones:
            Dones = False
            Seq = []
            for ind,Line in enumerate(self.Sequence):
                wrds = Line.split()
                if (len(wrds)==0)or(wrds[0][0] in '#/'):
                    pass
                elif (wrds[0]=='include'):
                    Fname = wrds[1]
                    Found = False
                    for Path in self.searchPath:
                        if (not Found) and os.path.exists('%s/%s'%(Path,Fname)):
                            Lines = open('%s/%s'%(Path,Fname)).readlines()
                            Seq.extend(Lines) 
                            Found = True
                            Dones = True
                    if not Found:
                        logs.log_error('include file "%s" no found in %s'%(Fname,self.searchPath))
                        Dones = False
                else:
                    Seq.append(Line)
            self.Sequence = Seq


    def force(self,Sig,Val):
        veri.force('%s.%s'%(self.Path,Sig),str(Val))

    def peek(self,Sig):
        Full = '%s.%s'%(self.Path,Sig)
        if veri.exists(Full)=='0': return False
        Val = hex(logs.peek(Full))
        return Val

    def eval(self,Txt):
        if Txt in self.Translates:
            return self.eval(self.Translates[Txt])

        try:
            Val = eval(Txt,self.Translates)
            return Val
        except:
            return Txt


    def run(self):
        if self.waiting>0:
            self.waiting -= 1
            return
        if self.waitNotBusy:
            if self.agents[self.waitNotBusy].busy(): return
            self.waitNotBusy = False
        if self.Sequence==[]: return
        Line = self.Sequence.pop(0)
        if '#' in Line: Line = Line[:Line.index('#')]
        if '//' in Line: Line = Line[:Line.index('//')]
        wrds = Line.split()
        if len(wrds)==0: return
        if wrds[0] == 'seed':
            random.seed = eval(wrds[1])
            return
        if wrds[0] == 'wait':
            self.waiting = eval(wrds[1])
            return
        if wrds[0] == 'exec':
            Cmd = ' '.join(wrds[1:])
            exec(Cmd)
            return
        if wrds[0] == 'define':
            Var = wrds[1]
            Val = self.eval(wrds[2])
            self.Translates[Var]=Val
            return
        if wrds[0] == 'finish':
            logs.log_info('finishing on sequence')
            veri.finish()
            sys.exit()
        if (wrds[0] == 'marker'):
            veri.force('tb.marker',wrds[1])
            return
        elif (wrds[0] == 'force'):
            self.force(wrds[1],self.eval(wrds[2]))
            return
        elif wrds[0] in self.agents:
            if wrds[1]=='waitNotBusy':
                self.waitNotBusy = wrds[0]
                return
            Wrds = map(str,map(self.eval,wrds[1:]))
            Wrds2 = []
            for Wrd in Wrds:
                if '=' in Wrd:
                    ww = Wrd.split('=')
                    w1 = self.eval(ww[1])
                    Wrds2.append('%s=%s'%(ww[0],w1))
                else:
                    Wrds2.append(Wrd)
            self.agents[wrds[0]].action(' '.join(Wrds2))
            return
        elif (wrds[0] == 'print'):
            Res = ''
            for Wrd in wrds[1:]:
                if self.peek(Wrd):
                    Res += ' %s=%s'%(Wrd,self.peek(Wrd))
                else:
                    Res += ' '+Wrd
            logs.log_info('PRINT %s'%Res)
            return
        else:
            logs.log_error('what!! sequence failed %s on %s agents=%s'%(wrds[0],Line,list(self.agents.keys())))


