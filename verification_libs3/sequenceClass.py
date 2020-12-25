


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
        self.Name = 'main'
        if Monitors!= -1:
            Monitors.append(self)
        self.Sequence = SEQUENCE.split('\n')
        self.workIncludes()
        self.waiting = 0
        self.Guardian = 0   # against wait too long.
        self.waitNotBusy = False
        self.agents={}
        self.Translates = Translates
        self.Translates['rnd'] = self.rnd
        for (Nickname,Object) in AGENTS:
            self.agents[Nickname]=Object
        self.searchPath = ['.'] 
        self.Ptr = 0
        self.Labels = {}
        self.Subs = {}
        self.Sons = []

    def newone(self,Seq,Name):
        New = sequenceClass(self.Path,-1,'',self.agents,self.Translates)
        New.Sequence = Seq
        New.Name = Name
        self.Sons.append(New)


    def rnd(self,Low,High):
        L,H = self.eval(Low),self.eval(High)
        X = random.randint(L,H)
        return X


    def readfile(self,Filename):
        if not os.path.exists(Filename):
            logs.log_error('failed to read "%s" file.'%(Filename))
            sys.exit()
        File = open(Filename)
        List = File.readlines()
        File.close()
        for Line in List:
            if len(Line)>1:
                self.Sequence.append(Line[:-1])
        self.searchPath.append(os.path.abspath(os.path.dirname(Filename)))
        self.workIncludes()
        self.extractSequences()


    def extractSequences(self):
        LL = []
        SUB = []
        state = 'idle'
        for Line in self.Sequence:
            wrds = Line.split()
            if wrds==[]:
                pass
            elif (state=='idle'):
                if wrds[0]=='sequence':
                    SEQ = wrds[1]
                    state='sub'
                else:
                    LL.append(Line)
            elif (state=='sub'):
                if wrds[0]=='end':
                    self.Subs[SEQ] = SUB
                    SUB = []
                    state = 'idle'
                else:
                    SUB.append(Line)



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

    def exists(self,Sig):
        Full = '%s.%s'%(self.Path,Sig)
        if veri.exists(Full)=='0': return False
        return True

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

    def runSons(self):
        if self.Sons==[]: return
        ind = 0
        while ind <len(self.Sons):
            Son = self.Sons[ind]
            Busy = Son.run()
            if not Busy:
                self.Sons.pop(ind)
            else:
                ind += 1

    def run(self):
        self.runSons()
        if self.waiting>0:
            self.waiting -= 1
            return True
        if self.waitNotBusy:
            if self.agents[self.waitNotBusy].busy(): return True
            self.waitNotBusy = False
        if self.Ptr == len(self.Sequence): return False
        Line = self.Sequence[self.Ptr]
        self.Ptr += 1
        if '#' in Line: Line = Line[:Line.index('#')]
        if '//' in Line: Line = Line[:Line.index('//')]
        wrds = Line.split()
        if len(wrds)==0: return True
        if wrds[0] == 'seed':
            random.seed = self.eval(wrds[1])
            return True
        if wrds[0] == 'wait':
            self.waiting = self.eval(wrds[1])
            return True
        if wrds[0] == 'exec':
            Cmd = ' '.join(wrds[1:])
            exec(Cmd)
            return True
        if wrds[0] == 'define':
            Var = wrds[1]
            Val = self.eval(wrds[2])
            self.Translates[Var]=Val
            return True
        if wrds[0] == 'finish':
            logs.finish('finishing on sequence')
            sys.exit()
        if (wrds[0] == 'marker'):
            veri.force('tb.marker',wrds[1])
            return True
        elif wrds[0] == 'label':
            self.Labels[wrds[1]] = self.Ptr-1
        elif wrds[0] in ['spawn','fork']:
            Seq = self.Subs[wrds[1]]
            Name = wrds[2]
            self.newone(Seq,Name)
            logs.log_info('spawning %s %s'%(wrds[1],Name))
        elif wrds[0] == 'goto':
            Lbl = wrds[1]
            if Lbl in self.Labels:
                self.Ptr = self.Labels[Lbl]
                return
            for ind,Line in enumerate(self.Sequence):
                ww = Line.split()
                if (ww[0]=='label'):
                    if ww[1] not in self.Labels:
                        self.Labels[ww[1]] = ind
            if Lbl in self.Labels:
                self.Ptr = self.Labels[Lbl]
                return
            logs.log_error('didnt find label "%s"'%Lbl)
            sys.exit()
        elif wrds[0] == 'if':
            BB = makeExpr(wrds[1])
            Val = self.evalExpr(BB)
            if not Val:  return

            Lbl = wrds[2]
            if Lbl in self.Labels:
                self.Ptr = self.Labels[Lbl]
                return
            for ind,Line in enumerate(self.Sequence):
                ww = Line.split()
                if (ww[0]=='label'):
                    if ww[1] not in self.Labels:
                        self.Labels[ww[1]] = ind
            if Lbl in self.Labels:
                self.Ptr = self.Labels[Lbl]
                return
            logs.log_error('didnt find label "%s"'%Lbl)
            sys.exit()

        elif (wrds[0] == 'force'):
            BB = makeExpr(wrds[2])
            Val = self.evalExpr(BB)
            self.force(wrds[1],Val)
            return True
        elif (wrds[0] == 'waitUntil'):
            if self.Guardian>0:
                self.Guardian -= 1
                if self.Guardian==0:
                    logs.log_error('Guardian expired')
                    logs.finish('Guardian expired %s'%(self.Fname))
                    veri.finish()
                    sys.exit()
            if (len(wrds)==3)and(self.Guardian==0):
                Guard = self.eval(wrds[2])
                self.Guardian=Guard

                    
            BB = makeExpr(wrds[1])
            Val = self.evalExpr(BB)
            if not Val: 
                self.Ptr -= 1
                return True
            logs.log_info('>>>>> finished waitUntil %s (left %d)'%(str(BB),self.Guardian))
            self.Guardian = 0
            return True




        elif wrds[0] in self.agents:
            if wrds[1]=='waitNotBusy':
                self.waitNotBusy = wrds[0]
                return True
            Wrds = list(map(str,map(self.eval,wrds[1:])))
            Wrds2 = []
            for Wrd in Wrds:
                if '=' in Wrd:
                    ww = Wrd.split('=')
                    w1 = self.eval(ww[1])
                    Wrds2.append('%s=%s'%(ww[0],w1))
                else:
                    Wrds2.append(Wrd)
            self.agents[wrds[0]].action(' '.join(Wrds2))
            return True
        elif (wrds[0] == 'print'):
            Res = ''
            for Wrd in wrds[1:]:
                if self.peek(Wrd):
                    Res += ' %s=%s'%(Wrd,self.peek(Wrd))
                else:
                    Res += ' '+Wrd
            logs.log_info('PRINT %s'%Res)
            return True
        else:
            logs.log_error('what!! sequence failed %s on %s agents=%s'%(wrds[0],Line,list(self.agents.keys())))
            return False

    def evalExpr(self,Wrds1):
        Defs = {}
        Wrds = Wrds1[:]
        for ind,Wrd in enumerate(Wrds):
            if (str(Wrd)[0] in string.ascii_letters)and(Wrd not in ['or','and','not']):
#                print('AAAAAA',Wrd,veri.exists(Wrd),type(veri.exists(Wrd)))
                if self.exists(Wrd):
                    Val = self.peek(Wrd)
                    Defs[Wrd]=Val
                    Wrds[ind]=Val
                elif Wrd in self.Translates:
                    Defs[Wrd]=self.Translates[Wrd]
                    Wrds[ind]=self.Translates[Wrd]

        Txt = ' '.join(map(str,Wrds))
        if Txt == '': return 0
        try:
            X = eval(Txt,Defs)
            return X
        except:
            logs.log_error('evaluation of %s failed'%Txt)
            return 0



def makeExpr(Txt):
    for Chr in '<>=()!+-*/':
        Txt = Txt.replace(Chr,' %s '%Chr)
    Txt  = Txt.replace('  ',' ')
    for From in ['= =','> =','! =','< =']:
        To = From.replace(' ','')
        Txt  = Txt.replace(From,To)
    wrds = Txt.split()
    for ind,wrd in enumerate(wrds):
        try:
            val = eval(wrd)
            wrds[ind]=val
        except:
            pass
    return wrds


