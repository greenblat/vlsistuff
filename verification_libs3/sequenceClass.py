
DEFAULTWAITGUARD = 10000000

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

#NEW! assert tb.dut.regx==0x50   [OPTIONAL_TEXT]  : will to log_ensure of the expression.
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
        self.workIncludes()
        self.workIncludes()
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
        self.Timed = {}
        self.Loops = []
        self.Break = False 
        self.AGENTS = AGENTS
        for NickObj in AGENTS:
            if type(NickObj) is int:
                pass
            elif (type(NickObj) is tuple):
                (Nickname,Object) = NickObj
                if Object:
                    self.agents[Nickname]=Object
                    Object.Caller = self
                    Object.SeqObj = self
            elif 'Name' in dir(NickObj):
                self.agents[NickObj.Name]=NickObj
            else:
                logs.log_error('sequence agent failed to connect "%s"' % (NickObj,AGENTS))

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


# def __init__(self,Path,Monitors,SEQUENCE='',AGENTS=[],Translates={}):

    def newone(self,Seq,Name):
        New = sequenceClass(self.Path,self.Monitors,'',self.AGENTS,self.Translates)
        logs.log_info('NEWONE %s' % str(Seq))
        for ind,Line in enumerate(Seq[1]):
            New.Sequence.append((Line,ind+1000))
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
                if Line[-1] == '\n': Line = Line[:-1]
                self.Sequence.append((Line,lnum))
                Wrds = Line.split()
                if (Wrds!=[]) and (Wrds[0] == 'searchpath'):
                    self.searchPath.append(Wrds[1])
        self.searchPath.append(os.path.abspath(os.path.dirname(Filename)))
        self.workIncludes()
        self.workIncludes()
        self.workIncludes()
        self.workIncludes()
        self.definesPreRun()
        self.pythonCodes()
        self.extractSequences()
        logs.log_info("SUBS %s" % str(list(self.Subs.keys())))
        for Sub in self.Subs:
            List = self.Subs[Sub]
            logs.log_info('SUB %s %s' % (Sub,List))
        for ind,Line in enumerate(self.Sequence):
            wrds = Line[0].split()
            if (wrds!=[])and(wrds[0] in ['include']):
                logs.log_error('SEQ INCLUDE %d %s' % (ind,Line))
            else:
                logs.log_info('SEQ %d %s' % (ind,Line),verbose=False)

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
            elif (len(wrds)==3) and (wrds[1] == '='):
                Var = wrds[0]
                Val = self.eval(wrds[2])
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
                    self.Subs[SEQ] = Params[:],SUB[:]
                    for PP in Params:
                        self.Translates[PP] = 0
                    SUB = []
                    state = 'idle'
                    logs.log_info('SUBDEF %s %s' % (SEQ,self.Subs[SEQ]))
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
                    print("DBG %s %s " % (wrds[1],Fname))
                    if os.path.exists(Fname):
                        Lines = open(Fname).readlines()
                        for x,Line in enumerate(Lines):
                            Seq.append((Line,1000+x))
                        Found = True
                        Dones = True

                    if 'PYINCLUDE' in os.environ:
                        Try = os.environ['PYINCLUDE'] +  '/' + wrds[1]
                        if os.path.exists(Try):
                            Lines = open(Try).readlines()
                            for x,Line in enumerate(Lines):
                                Seq.append((Line,1000+x))
                            Found = True
                            Dones = True


                    for Path in self.searchPath:
                        if (not Found) and os.path.exists('%s/%s'%(Path,wrds[1])):
                            Lines = open('%s/%s'%(Path,wrds[1])).readlines()
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
        if self.Path == '':
            veri.force('%s'%(Sig),str(Val))
        else:
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

    def evalh(self,Txt,Bad=False):
        X = self.eval(Txt,Bad)
        if type(X) is int: return hex(X)
        if type(X) is float: return str(X)
        return X

    def eval(self,Txt,Bad=False):
        if type(Txt) is int: return Txt
        if Txt in self.Translates: return self.eval(self.Translates[Txt])
        if Txt[0] == '"': return Txt.replace('"','')
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

    def runTimed(self):
        for When in self.Timed:
            if logs.get_cycles() == When:
                Line = self.Timed[When]
                logs.log_info('TIMED USE %s %s' % (When,Line))
                self.seq_line(Line,0)
                
            
    def runBreak(self):
        Txt = input("seq break:") 
        wrds = Txt.split()
        if wrds==[]: return
        if wrds[0] in ['return','resume']:
            self.Break = False
            return
        self.seq_line(Txt,-1)
        


    def run(self):
        if self.Break: 
            self.runSons()
            if self.waiting>0:
                self.waiting -= 1
                return True
            self.runBreak()
            return
        self.runSons()
        self.runTimed()
        if self.waiting>0:
            self.waiting -= 1
            return True
        if self.waitNotBusy:
            if self.agents[self.waitNotBusy].busy(): 
                if self.Guardian>0:
                    self.Guardian -= 1
                    if self.Guardian==0:
                        Lnum = self.Sequence[self.Ptr][1]
                        logs.log_error('Guardian expired %s at line %s  seq=%s'%(self.waitNotBusy,Lnum,self.Sequence[self.Ptr]))
                        logs.log_error('          %s'%(self.agents[self.waitNotBusy].busy(True)))
                        self.agents[self.waitNotBusy].busy()
                        self.agentsFinish()
                        logs.finish('Guardian expired %s at line %s'%(self.waitNotBusy,Lnum))
                        logs.talk('simulation finished on guardian of %s line number %s' % (self.waitNotBusy,Lnum))
#                        os.system('say  -v Carmit שלום איליה שים לב' )
#                        os.system('say -v Majed انتهت المحاكاة' )
#                        os.system('say  -v Samantha simulation finished on guardian of %s line number %s' % (self.waitNotBusy,Lnum))
                        logs.closeLogs()
                        veri.finish()
                        sys.exit()
                return True
            self.Guardian = 0
            self.waitNotBusy = False
        if self.Ptr == len(self.Sequence): return False
        try:
            Line,lnum = self.Sequence[self.Ptr]
        except:
            logs.log_info('XXXXXXX %s %s {{%s}} ' % (self.Ptr,self.Sequence[self.Ptr],self.Sequence))
            Line = ''
            lnum = 999
        self.Ptr += 1
        if '#' in Line: Line = Line[:Line.index('#')]
#        if '//' in Line: Line = Line[:Line.index('//')]
        logs.log_write('@%d: sequence: %s'%(logs.get_cycles(),Line),'seq')
#        print(lnum,Line)
        veri.force('tb.seqptr',str(lnum))
        self.seq_line(Line,lnum)

    def seq_line(self,Line,lnum):
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
        if wrds[0] in ('wait','run'):
            self.waiting = self.eval(wrds[1])
            return True
        if wrds[0] == 'exec':
            Cmd = ' '.join(wrds[1:])
            exec(Cmd)
            return True
        if wrds[0] == 'break':
            self.Break = lnum
            return



        if wrds[0] == 'define':
            Var = wrds[1]
            if len(wrds)==3:
                Val = self.eval(wrds[2])
                self.Translates[Var]=Val
#                logs.log_info('DBG %s %s "%s"   %s' % (Var,Val,wrds,logs.without(self.Translates)))
            elif len(wrds)>3:
                Val = list(map(self.eval,wrds[2:]))
                self.Translates[Var]=Val
            return True
        if (len(wrds) >= 3) and (wrds[1] == '='):
            List1 = list(map(self.eval,wrds[2:]))
            List1 = list(map(str,List1))
            Expr = ' '.join(List1)
            Val = self.eval(Expr)
            self.Translates[wrds[0]]=Val
            return 

        if wrds[0] == 'quit':
            Line = Line.replace('quit','finish_verilator')
            self.seq_line(Line,lnum)
            sys.exit()
        if wrds[0] == 'finish':
            Line = Line.replace('finish','finish_verilator')
            self.seq_line(Line,lnum)
            sys.exit()

        if wrds[0] == 'finish_verilator':
            logs.log_info('finishing on sequence')
            self.agentsFinish()
            logs.talk("",'שלום איליה שים לב' )
            if (logs.Wrongs>0) or (logs.Errors>0):
                HH = HEB2.replace('1@',str(logs.Wrongs))
                HH = HH.replace('2@',str(logs.Errors))
                HH = HH.replace('@2',str(logs.Errors))
                HH = HH.replace('@1',str(logs.Wrongs))
                logs.talk(HH)
            elif (logs.Wrongs==0) or (logs.Errors==0):
                if (logs.Corrects == 0):
                    logs.talk("",HEB0)
                else:
                    logs.talk(HEB1.replace('@',str(logs.Corrects)))
#            os.system('say -v Majed انتهت المحاكاة' )
            logs.talk('Simulation finished on sequence! we have %s corrects, %s wrongs %d warnings and %s errors' % (logs.Corrects,logs.Wrongs,logs.Warnings,logs.Errors))
            logs.finish('sequence %s seed=%d '%(self.testFileName,self.Seed))
        if (wrds[0] == 'marker'):
            veri.force('%s.marker'%TB,wrds[1])
            return True
        elif wrds[0] == 'label':
            self.Labels[wrds[1]] = self.Ptr-1
        elif wrds[0] in ['spawn','fork']:
            Seq = self.Subs[wrds[1]]
            if len(wrds)==2:
                wrds.append(Name)
            Name = wrds[2]
            self.newone(Seq,Name)
            logs.log_info('spawning seq=%s %s'%(wrds[1],Name))
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
        elif wrds[0] == 'for':
            X = wrds[1].replace('=',' = ').split()
            if len(X) == 3:
                self.Translates[X[0]] = self.eval(X[2])
            print("FOR",self.Ptr,wrds[2],wrds[3])
            self.Loops.append((self.Ptr,wrds[2],wrds[3]))

        elif wrds[0] == 'endfor':
            Ptr,Cond,End = self.Loops.pop(0)
            X = End.replace('=',' = ').split()
            if len(X) == 3:
                self.Translates[X[0]] = self.eval(X[2])
            if self.eval(Cond):
                self.Loops.append((Ptr,Cond,End))
                self.Ptr = Ptr+1
                logs.log_info("ENDFOR cond=%s ptr=%d  %s  %s" % (Cond,self.Ptr,self.Sequence[self.Ptr],logs.without(self.Translates)))
                return
            logs.log_info("AFTER ENDFOR cond=%s ptr=%d  %s  %s" % (Cond,self.Ptr,self.Sequence[self.Ptr],logs.without(self.Translates)))
            self.Ptr += 1
            return

        elif wrds[0] == 'goto':
            Lbl = wrds[1]
            self.jumpLabel(Lbl)
            return
        elif (wrds[0] == 'if') and (len(wrds)==2):   # if version: if cond execute till endif, otherwise skip
            BB = makeExpr(wrds[1])
            Val = self.evalExpr(BB)
            if Val: return
            ind = self.Ptr
            Guard = 10
            while (Guard>0) and ('endif' not in self.Sequence[ind][0]):
                ind += 1
                Guard -= 1
                if len(self.Sequence)<=ind: Guard = 0
            if Guard == 0:
                logs.log_error("if condition, failed on distance to endif. this is simple 'if', cannot include other ifs")
                return
            self.Ptr = ind    

        elif (wrds[0] == 'endif'): return    

        elif (wrds[0] == 'if') and (len(wrds)==3):   # if version: if cond goto label
            BB = makeExpr(wrds[1])
            Val = self.evalExpr(BB)
#            logs.log_info("EXPRIF %s -> %s %s     %s" % (wrds[1],BB,Val,self.Translates['BB']))
            if not Val:  return
            Lbl = wrds[2]
            self.jumpLabel(Lbl)
            return
        elif (wrds[0][0] == '@'):
            Time = eval(wrds[0][1:])
            self.Timed[Time] = ' '.join(wrds[1:])
            logs.log_info('TIMED added %d %s' % (Time,self.Timed[Time]))
        elif (wrds[0] == 'searchpath'):
            pass
        elif (wrds[0] == 'force'):
            Ind = 1
            while Ind < len(wrds):
                BB = makeExpr(wrds[Ind+1])
                Val = self.evalExpr(BB)
                self.force(wrds[Ind],Val)
                Ind += 2
            return True
        elif (wrds[0] == 'assert'):
            if (len(wrds)==3):
                Marker = wrds[2]
            else:
                Marker = 'lnum #%d' % lnum
            BB = makeExpr(wrds[1])
            Val = self.evalExpr(BB)
            logs.log_ensure(Val,'ASSERT '+Marker)
            return True
        elif (wrds[0] == 'waitUntil'):
            if self.Guardian>0:
                self.Guardian -= 1
                if self.Guardian==0:
                    Lnum = self.Sequence[self.Ptr][1]
                    logs.log_error('waitUntil Guardian expired at line %s   x=%s'%(Lnum,self.Sequence[self.Ptr]))
                    self.agentsFinish()
                    logs.finish('Guardian expired %s  at line %s'%(self.testFileName,Lnum))
                    logs.talk('Hei Ilia  simulation finished on guardian!')
                    veri.finish()
                    sys.exit()
            if (len(wrds)==3)and(self.Guardian==0):
                Guard = self.eval(wrds[2])
                self.Guardian=Guard
                Lnum = self.Sequence[self.Ptr][1]
                logs.log_info('GUARDIAN %s started %s at line %s' % (wrds,Guard,Lnum))

            if (self.Guardian % 10000) == 1:
                Lnum = self.Sequence[self.Ptr][1]
                logs.log_info('GUARDIAN %s lnum=%d wrds=%s len=%d' % (self.Guardian,Lnum,wrds,len(wrds)))
                    
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
            if wrds[1] == 'listing':
                if len(wrds)>2:
                    Fname = wrds[2]
                else:
                    Fname = 'deep.list'
                veri.listing('tb','100',Fname)
            elif wrds[1] == 'import':
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
            if (len(wrds)>1) and (wrds[1]=='waitNotBusy'):
                self.waitNotBusy = wrds[0]
                if len(wrds)>2:
                    self.Guardian = eval(wrds[2])
                else:
                    self.Guardian = DEFAULTWAITGUARD

                return True
            Wrds = list(map(self.evalh,wrds[2:]))
            Wrds2 = []
            for Wrd in Wrds:
                if '=' in Wrd:
                    ww = Wrd.split('=')
                    w1 = self.eval(ww[1])
                    Wrds2.append('%s=%s'%(ww[0],w1))
                else:
                    Wrds2.append(Wrd)
            Cmd = wrds[1]+' '+' '.join(Wrds2)
            logs.log_info('tell %s <- %s   (%s)   2(%s)' % (Line[:-1],Cmd,Wrds,Wrds2))
# @259: info: write 0x454 0x19  ['write', 'LVL_classic_end_of_phase_seg1', 'SEG1']
            ww = Cmd.split()
#            if ww[0] == 'write':
#                logs.log_info('A%s. w%s. //  %s' % (ww[1][2:],ww[2][2:],wrds[1:]),'uart')
            self.agents[wrds[0]].action(Cmd,wrds[1:])
            return True
        elif (wrds[0] == 'check'):
            BB = makeExpr(wrds[1])
            Val = self.evalExpr(BB)
            logs.log_ensure(Val,'CHECK of %s == %s  vars=%s %s '%(wrds[1],Val,self.DEFS,' '.join(wrds[2:]))) 
        elif (wrds[0] in ['correct','wrong','print','say']):
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
                    Val = self.evalExpr(BB)
                    Res += ' '+str(Val)
                else:
                    Res += ' '+Wrd
            if wrds[0]=='correct':
                logs.log_correct('   %s'%Res)
            elif wrds[0]=='wrong':
                logs.log_wrong('   %s'%Res)
            elif (wrds[0] == 'say'):
                os.system('say  -v Samantha %s' % Res)
            else:
                logs.log_info('PRINT %s'%Res)
            return True
        elif (wrds[0] == 'debuglevel'):
            veri.debuglevel(wrds[1])
        else:
            logs.log_error('what!! sequence failed %s on %s agents=%s'%(wrds[0],Line,list(self.agents.keys())))
            return False

    def agentAction(self,Agent,Txt):
        wrds = Txt.split()
        Wrds = list(map(str,map(self.eval,wrds[1:])))
        Wrds2 = []
        for Wrd in Wrds:
            if '=' in Wrd:
                ww = Wrd.split('=')
                w1 = self.eval(ww[1])
                Wrds2.append('%s=%s'%(ww[0],w1))
            else:
                Wrds2.append(Wrd)
        Cmd = wrds[0]+' '+' '.join(Wrds2)
        logs.log_info('tell %s %s -> %s' % (Agent,Txt,Cmd),'seq')
        self.agents[Agent].action(Cmd)

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
                if type(Wrd) is bool:
                    Wrds[ind] = Wrd
                elif Wrd in self.Translates:
                    self.Defs[Wrd]=self.Translates[Wrd]
                    Wrds[ind]=self.Translates[Wrd]
                elif self.exists(Wrd):
                    Val = self.peek(Wrd)
                    self.Defs[Wrd]=Val
                    self.DEFS.append((Wrd,Val))
                    Wrds[ind]=Val

        Txt = ' '.join(map(str,Wrds))
        Txt = Txt.replace(' ( )','()')

        if Txt == '': return 0
        try:
            X = self.eval(Txt)    # ,self.Defs,self.Translates)
            return X
        except:
            logs.log_error('evaluation of "%s" failed'%Txt,0,True,True)
#            logs.log_info('TRANSLATES %s'%(str(self.Translates)))
#            logs.log_info('SEQUENCE RDS %s'%(str(Wrds)))
            return 0

    def agentsFinish(self):
        if self.onFinishes:
            self.onFinishes()
        for Agent in self.agents:
            Obj = self.agents[Agent]
            Obj.onFinish()
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
    for Chr in '%&|<>=()!+-*/':
        Txt = Txt.replace(Chr,' %s '%Chr)
    Txt  = Txt.replace('  ',' ')
    Txt = Txt.replace(' ( )','()')
    for From in ['^','= =','> =','! =','< =','< <','> >','/ /']:
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
        if X not in ('._'+string.digits + string.ascii_letters): return False
    return True

HEB0 = "טסט נגמר ללא שגיאות, אבל עם אפס מדויקים "
HEB1 = " טסט נגמר ללא שגיאות, עם  @ מדויקים"
HEB2 = " טסט נגמר עם  @1 כשלים , @2 שגיאות"
HEB3 = " טסט נגמר עם  @1 כשלים , @2 שגיאות"
