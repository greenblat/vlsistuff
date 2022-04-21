
DEFAULTWAITGUARD = 1000000

import logs
import veri
import sys,os,string
import random
import importlib

#built in commands: finish,wait,marker,force,print,define,include,exec,check,seq import

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
#agents:   apb waitNotBusy


#

# def initialSequence(Fname):

TB = 'tb'



class sequenceClass:
    def __init__(self,Path,Monitors,SEQUENCE='',AGENTS=[],Translates={}):
        self.Path = Path
        self.Name = 'main'
        self.testFileName = '?'
        logs.testFileName = '?'
        if Monitors!= -1:
            Monitors.append(self)
        self.Monitors = Monitors
        self.Sequence = []
        logs.log_info('INCLUDES STARTED')
        self.workIncludes()
        logs.log_info('INCLUDES DONE')
        self.waiting = 0
        self.Guardian = 0   # against wait too long.
        self.waitNotBusy = False
        self.agents={}
        self.agents['logs'] = logs
        self.Translates = Translates
        self.Translates['rnd'] = self.rnd
        self.Translates['envir'] = self.envir
        self.Translates['eflash'] = self.eflash
        self.Translates['peek'] = self.seq_peek
        self.Translates['float2int'] = logs.float2binary
        for (Nickname,Object) in AGENTS:
            self.agents[Nickname]=Object
            Object.Caller = self
            Object.SeqObj = self
        self.searchPath = ['.'] 
        self.Ptr = 0
        self.Stack = []
        self.Labels = {}
        self.Subs = {}
        self.Sons = []
        self.Seed = 0
        self.onFinishes = False

    def restart(self):
        self.Ptr = 0
        # do i need to restart more items???



    def newone(self,Seq,Name):
        New = sequenceClass(self.Path,-1,'',self.agents,self.Translates)
        New.Sequence = Seq
        New.Name = Name
        self.Sons.append(New)

    def eflash(self,Addr):
        if 'EFLASH' in dir(self):
            if Addr in self.EFLASH:
                return self.EFLASH[Addr]
            logs.log_error('eflash preloaded, but addr %x is not in there'%Addr)
            return 0
        logs.log_error('no eflash preloaded')
        return 0

    def seq_peek(self,Txt):
        if self.exists(Txt):
            return self.peek(Txt)
        return -1
        

    def envir(self,Txt):
        if Txt in os.environ:
            X = os.environ[Txt]
            return self.eval(X)

        return 0

    def rnd(self,Low,High=0):
        if High==0:
            L = self.eval(Low)
            X = random.randint(0,L)
            return X
        if type(Low) is list:
            X = random.randint(0,len(Low)-1)
            return eval(Low[X])

        L,H = self.eval(Low),self.eval(High)
        X = random.randint(L,H)
        return X


    def readfile(self,Filename):
        if not os.path.exists(Filename):
            logs.log_error('failed to read "%s" file.'%(Filename))
            sys.exit()
        self.testFileName = Filename
        logs.testFileName = Filename
        File = open(Filename)
        List = File.readlines()
        File.close()
        for lnum,Line in enumerate(List):
            if len(Line)>1:
                self.Sequence.append((Line[:-1],lnum))
        self.searchPath.append(os.path.abspath(os.path.dirname(Filename)))
        self.workIncludes()
        self.definesPreRun()
        self.pythonCodes()
        self.extractSequences()

    def pythonCodes(self):
        Pythons = []
        Seqs = []
        state = 'idle'
        for Line,AA in self.Sequence:
            wrds = Line.split()
            if state == 'idle':
                if wrds == []:
                    Seqs.append((Line,AA))
                elif wrds[0] == '+python':
                    state = 'python' 
                else:
                    Seqs.append((Line,AA))
            elif state == 'python':
                if wrds == []:
                    Pythons.append((Line,AA))
                elif wrds[0] == '-python':
                    state = 'idle' 
                else:
                    Pythons.append(Line)

        self.Sequence = Seqs
        Code = '\n'.join(Pythons)
        exec(Code,globals())
        



                    
    def definesPreRun(self):
        for Line,_ in self.Sequence:
            wrds = Line.split()
            if wrds == []:
                pass
            elif wrds[0] == 'define':
                Var = wrds[1]
                if len(wrds)==3:
                    Val = self.eval(wrds[2])
                    self.Translates[Var]=Val
                elif len(wrds)>3:
                    Val = list(map(self.eval,wrds[2:]))
                    self.Translates[Var]=Val


    def extractSequences(self):
        LL = []
        SUB = []
        state = 'idle'
        for Line,_ in self.Sequence:
            wrds = Line.split()
            if wrds==[]:
                pass
            elif (state=='idle'):
                if wrds[0]=='sequence':
                    SEQ = wrds[1]
                    Params = wrds[2:]
                    state='sub'
                else:
                    LL.append(Line)
            elif (state=='sub'):
                if wrds[0]=='end':
                    self.Subs[SEQ] = Params,SUB
                    for PP in Params:
                        self.Translates[PP] = 0
                    SUB = []
                    state = 'idle'
                else:
                    SUB.append(Line)



    def workIncludes(self):
        Dones = True
        while Dones:
            Dones = False
            Seq = []
            for ind,Linex in enumerate(self.Sequence):
                try:
                    Line,x = Linex
                except:
                    Line = Linex
                    x = '???'
                wrds = Line.split()
                if (len(wrds)==0)or(wrds[0][0] in '#/'):
                    pass
                elif (wrds[0]=='include'):
                    Fname = wrds[1]
                    Fname = os.path.expanduser(Fname)
                    Fname = os.path.expandvars(Fname)
                    Fname = os.path.abspath(Fname)
                    Found = False
                    if os.path.exists(Fname):
                        Lines = open(Fname).readlines()
                        for x,Line in enumerate(Lines):
                            Seq.append((Line,1000+x))
                        Found = True
                        Dones = True
                    for Path in self.searchPath:
                        if (not Found) and os.path.exists('%s/%s'%(Path,Fname)):
                            Lines = open('%s/%s'%(Path,Fname)).readlines()
                            for xx,LL in enumerate(Lines):
                                Seq.append((LL,xx)) 
                            Found = True
                            Dones = True
                    if not Found:
                        logs.log_warning('include file "%s" no found in %s'%(Fname,self.searchPath))
                        Dones = False
                else:
                    Seq.append((Line,x))
            self.Sequence = Seq


    def force(self,Sig,Val):
        veri.force('%s.%s'%(self.Path,Sig),str(Val))

    def exists(self,Sig):
        if Sig.startswith(self.Path+'.'):
            Sig = Sig.replace(self.Path+'.','')
        elif Sig.startswith(self.Path):
            Sig = Sig.replace(self.Path,'')
            
        Full = '%s.%s'%(self.Path,Sig)
        if veri.exists(Full)=='0': return False
        return True

    def peek(self,Sig):
        if Sig.startswith(self.Path+'.'):
            Sig = Sig.replace(self.Path+'.','')
        elif Sig.startswith(self.Path):
            Sig = Sig.replace(self.Path,'')
        Full = '%s.%s'%(self.Path,Sig)
        if veri.exists(Full)=='0': return False
        Val = hex(logs.peek(Full))
        return Val

    def eval(self,Txt,Bad=False):
        if type(Txt) is int: return Txt
        if Txt in self.Translates: return self.eval(self.Translates[Txt])
        try:
            Val =  eval(Txt)
            return Val
        except:            
            try:
                Val = eval(Txt,self.Translates)
                return Val
            except:
                try:
                    Val = self.evalStr(Txt,self.Translates)
                    return Val
                except:
                    X =  self.exists(Txt)
                    if X:
                        return self.peek(Txt)


                    if Bad:
                        logs.log_error('failed eval of "%s"' % str(Txt))
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
            if self.agents[self.waitNotBusy].busy(): 
                if self.Guardian>0:
                    self.Guardian -= 1
                    if self.Guardian==0:
                        Lnum = self.Sequence[self.Ptr][1]
                        logs.log_error('Guardian expired %s at line %s'%(self.waitNotBusy,Lnum))
                        self.agents[self.waitNotBusy].busy(True)
                        self.agentsFinish()
                        logs.finish('Guardian expired %s at line %s'%(self.waitNotBusy,Lnum))
                        logs.closeLogs()
                        veri.finish()
                        sys.exit()
                return True
            self.waitNotBusy = False
        if self.Ptr == len(self.Sequence): return False
        Line,lnum = self.Sequence[self.Ptr]
        self.Ptr += 1
        if '#' in Line: Line = Line[:Line.index('#')]
        if '//' in Line: Line = Line[:Line.index('//')]
        logs.log_write('sequence: %s'%Line,'seq')
#        print(lnum,Line)
        wrds = Line.split()
        if len(wrds)==0: return True
        if wrds[0] == 'seed':
            Val = self.eval(wrds[1])
            random.seed(Val)
            logs.log_info('SEED FROM Sequence %s'%Val)
            return True
        if wrds[0] == 'logfile':
            logs.setLogfileName(wrds[1],0)
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
            if len(wrds)==3:
                Val = self.eval(wrds[2])
                self.Translates[Var]=Val
                logs.log_info('DBG %s %s' % (Var,Val))
            elif len(wrds)>3:
                Val = list(map(self.eval,wrds[2:]))
                self.Translates[Var]=Val



            return True
        if wrds[0] == 'finish':
            logs.log_info('finishing on sequence')
            self.agentsFinish()
            logs.finish('sequence %s seed=%d '%(self.testFileName,self.Seed))
            sys.exit()
        if (wrds[0] == 'marker'):
            veri.force('%s.marker'%TB,wrds[1])
            return True
        elif wrds[0] == 'label':
            self.Labels[wrds[1]] = self.Ptr-1
        elif wrds[0] in ['spawn','fork']:
            Seq = self.Subs[wrds[1]]
            Name = wrds[2]
            self.newone(Seq,Name)
            logs.log_info('spawning %s %s'%(wrds[1],Name))
        elif wrds[0] == 'return':
            if self.Stack==[]:
                logs.log_error('return in sequence from empty stack')
                return
            self.Ptr = self.Stack.pop(-1)
            return
        elif wrds[0] == 'call':
            Sub = wrds[1]
            if Sub not in self.Subs:
                logs.log_error('subsequence %s is not defined, ok %s'%(Sub,list(self.Subs.keys())))
                return
            Params,_ = self.Subs[Sub]
            self.Stack.append(self.Ptr)
            Actuals = wrds[2:]
            if len(Actuals)!=len(Params):
                logs.log_error('subsequence %s params %d != %d  act  %s params %s'%(Sub,len(Actuals),len(Params),Actuals,Params))
                return
            Zip = list(zip(Params,Actuals))
            for (PP,AA) in Zip:
                Val = self.eval(AA)
                self.Translates[PP]=Val

            self.jumpLabel(Sub)
            self.Ptr += 1
            return
        elif wrds[0] == 'goto':
            Lbl = wrds[1]
            self.jumpLabel(Lbl)
            return
        elif wrds[0] == 'if':
            BB = makeExpr(wrds[1])
            Val = self.evalExpr(BB)
            if not Val:  return
            Lbl = wrds[2]
            self.jumpLabel(Lbl)
            return
        elif (wrds[0] == 'force'):
            Ind = 1
            while Ind < len(wrds):
                BB = makeExpr(wrds[Ind+1])
                Val = self.evalExpr(BB)
                self.force(wrds[Ind],Val)
                Ind += 2
            return True
        elif (wrds[0] == 'waitUntil'):
            if self.Guardian>0:
                self.Guardian -= 1
                if self.Guardian==0:
                    Lnum = self.Sequence[self.Ptr][1]
                    logs.log_error('Guardian expired at line %s'%(Lnum))
                    self.agentsFinish()
                    logs.finish('Guardian expired %s  at line %s'%(self.testFileName,Lnum))
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
            Lnum = self.Sequence[self.Ptr][1]
            logs.log_info('>>>>> finished waitUntil %s (left %d)   at line %s'%(str(BB),self.Guardian,Lnum))
            self.Guardian = 0
            return True

        elif (wrds[0] == 'seq'):  # commands to myself
            if wrds[1] == 'import':
                Module = wrds[2]
                if Module.endswith('.py'):
                    Module = Module[:-3]
                if '/' in Module:
                    wrds = Module.split('/')
                    Path = '/'.join(wrds[:-1])
                    Module = wrds[-1]
                    sys.path.append(Path)
                That = importlib.import_module(Module)
                self.agents[Module] = That
                That.Caller = self
                self.Monitors.append(That)
                logs.log_info('helper %s added'%(Module))
            else:
                logs.log_error('sequence class accepts only import, not %s'%str(wrds))
            return

        elif wrds[0] in self.agents:
            if wrds[1]=='waitNotBusy':
                self.waitNotBusy = wrds[0]
                if len(wrds)>2:
                    self.Guardian = eval(wrds[2])
                else:
                    self.Guardian = DEFAULTWAITGUARD

                return True
            Wrds = list(map(str,map(self.eval,wrds[2:])))
            Wrds2 = []
            for Wrd in Wrds:
                if '=' in Wrd:
                    ww = Wrd.split('=')
                    w1 = self.eval(ww[1])
                    Wrds2.append('%s=%s'%(ww[0],w1))
                else:
                    Wrds2.append(Wrd)
            self.agents[wrds[0]].action(wrds[1]+' '+' '.join(Wrds2))
            return True
        elif (wrds[0] == 'check'):
            BB = makeExpr(wrds[1])
            Val = self.evalExpr(BB)
            logs.log_ensure(Val,'CHECK of %s  vars=%s '%(wrds[1],self.DEFS)) 
        elif (wrds[0] in ['correct','wrong','print']):
            Res = ''
            for Wrd in wrds[1:]:
                if acceptablePath(Wrd) and self.peek(Wrd):
                    Res += ' %s=%s'%(Wrd,self.peek(Wrd))
                elif Wrd in self.Translates:
                    Trx = self.Translates[Wrd]
                    if type(Trx) is int:
                        Res += ' %s' % hex(self.Translates[Wrd])
                    else:
                        Res += str(self.Translates[Wrd])
                elif (Wrd[0] == '('):
                    BB = makeExpr(Wrd)
                    print('>>>>>>>',BB)
                    logs.log_info('>>>>>>> %s' % str(BB))
                    Val = self.evalExpr(BB)
                    Res += ' '+str(Val)
                else:
                    Res += ' '+Wrd
            if wrds[0]=='correct':
                logs.log_correct('   %s'%Res)
            elif wrds[0]=='wrong':
                logs.log_wrong('   %s'%Res)
            else:
                logs.log_info('PRINT %s'%Res)
            return True
        elif (wrds[0] == 'debuglevel'):
            veri.debuglevel(wrds[1])
        else:
            logs.log_error('what!! sequence failed %s on %s agents=%s'%(wrds[0],Line,list(self.agents.keys())))
            return False

    def jumpLabel(self,Lbl):
        if Lbl in self.Labels:
            self.Ptr = self.Labels[Lbl]
            return
        for ind,(Line,_) in enumerate(self.Sequence):
            ww = Line.split()
            if (ww[0] in ['sequence','label']):
                if ww[1] not in self.Labels:
                    self.Labels[ww[1]] = ind
        if Lbl in self.Labels:
            self.Ptr = self.Labels[Lbl]
            return
        logs.log_error('didnt find label "%s"'%Lbl)
        sys.exit()
    def evalStr(self,Str):
        BB = makeExpr(Str)
        Val = self.evalExpr(BB)
        return Val
    def evalExpr(self,Wrds1):
        self.Defs = {}
        self.DEFS = []
        Wrds = Wrds1[:]
        for ind,Wrd in enumerate(Wrds):
            if (str(Wrd)[0] in '_'+string.ascii_letters)and(Wrd not in ['or','and','not']):
                if Wrd in self.Translates:
                    self.Defs[Wrd]=self.Translates[Wrd]
                    Wrds[ind]=self.Translates[Wrd]
                elif self.exists(Wrd):
                    Val = self.peek(Wrd)
                    self.Defs[Wrd]=Val
                    self.DEFS.append((Wrd,Val))
                    Wrds[ind]=Val

        Txt = ' '.join(map(str,Wrds))
        if Txt == '': return 0
        try:
            X = eval(Txt,self.Defs,self.Translates)
            return X
        except:
            logs.log_error('evaluation of %s failed'%Txt,0,True,True)
            logs.log_info('TRANSLATES %s'%(str(self.Translates)))
            logs.log_info('RDS %s'%(str(Wrds)))
            return 0

    def agentsFinish(self):
        if self.onFinishes:
            self.onFinishes()
        for Agent in self.agents:
            Obj = self.agents[Agent]
            if 'onFinish' in dir(Obj):
                try:
                    Obj.onFinish()
                except:
                    logs.log_info('%s.onFinish() failed'%Agent)
            else:
                logs.log_info('no  %s.onFinish() found , add "    def onFinish(self):" to the agent'%Agent)

            if 'busy' in dir(Obj):
                Busy = Obj.busy()
                if Busy and (Obj.Name != 'main'):
                    logs.log_error('agent "%s" "%s" stayed busy to the end' % (Agent,Obj.Name))
                    if 'busyWhy' in dir(Obj):
                        Obj.busyWhy()

def makeExpr(Txt):
    for Chr in '&|<>=()!+-*/':
        Txt = Txt.replace(Chr,' %s '%Chr)
    Txt  = Txt.replace('  ',' ')
    for From in ['= =','> =','! =','< =','< <','> >']:
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

def acceptablePath(Word):
    if Word[0] not in string.ascii_letters: return False
    for X in Word[1:]:
        if X not in ('_'+string.digits + string.ascii_letters): return False
    return True

