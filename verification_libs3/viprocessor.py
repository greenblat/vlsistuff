
import logs
import sys
import veri
import importlib
import random

import parseCode
import txGenClass

class vipClass(logs.driverClass):
    def __init__(self,Path,Monitors,Params=''):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Params = Params
        self.Renames = {}
        PV = getParams(Params)
        self.prefix = ''
        if 'prefix' in PV:
            self.prefix = PV['prefix']
        self.Procs = []
        self.apb_state = 'idle'
        self.Locks = {}
        self.apbs = False
        self.axis = False
#        self.Agents = {}
        self.scoreBoard = {}

    def add_agent(self,Name,Agent):
        Agent.Father = self.SeqObj
#        self.Agents[Name] = Agent
        self.SeqObj.Agents[Name] = Agent


    def run(self):
        for Proc in self.Procs:
            Proc.run()

    def busy(self):
        Busy = False
        for Proc in self.Procs:
            if Proc.Active: Busy = True
        return Busy

    def onFinish(self):
        return

    def action(self,Txt,Orig=[]):
        wrds = Txt.split()
        if wrds == []: return
        if wrds[0] == 'rename':
            www = wrds[1:]
            while len(www)>=2:
                self.Renames[www[0]] = www[1]
                www.pop(0)
                www.pop(0)
        elif wrds[0] == 'setvar':
            Var = wrds[1]
            Expr = wrds[2]
            Val = self.eval(wrds[2])
            self.VARS[Var] = Val
            logs.log_info("%s SETVAR %s %s %s    %s" % (self,self.prefix,Var,Val,self.VARS))
        elif wrds[0] == 'program':
            parseCode.parseCode(wrds[1],'proc_x0.py')
            That = importlib.import_module('proc_x0')
            self.PAIRS  = That.PAIRS
            self.DEFINES  = That.DEFINES
            self.LINES  = That.LINES
            self.VARS = {}
            for Var in That.VARS:
                self.VARS[Var] = That.VARS[Var]
            Main = self.DEFINES['main']+1
            self.Procs.append(processorClass(self,'main',self.PAIRS,self.DEFINES,self.VARS,self.LINES,Main))

        else:
            logs.log_error('vipClass got %s' % Txt)

    def forkit(self,Type,Name):
        Addr = self.DEFINES[Type]
        X = processorClass(self,Name,self.PAIRS,self.DEFINES,self.VARS,self.LINES,Addr+1)
        self.Procs.append(X)
    def force(self,Sig,Val):
        if Sig in self.Renames: Sig = self.Renames[Sig]
        if type(Val) is int:
            Val = str(Val)
        else:
            Val = self.eval(Val)
            Val = str(Val)
        veri.force('%s%s%s' % (self.Path,self.prefix,Sig),str(Val))

    def peek(self,Sig):
        if Sig in self.Renames: Sig = self.Renames[Sig]
        return logs.peek('%s%s' % (self.Path,Sig))

    def rnd(self,Lo,Hi):
        Val = random.randint(Lo,Hi)
        return Val
        
    def eval(self,Expr):
        Tmp = {'peek':self.peek,'rnd':self.rnd}
        Dict = { **self.VARS, **Tmp}
        Val = eval(Expr,self.DEFINES,Dict)
        try:
            Val = eval(Expr,self.DEFINES,Dict)
        except:
            self.DEFINES.pop('__builtins__')
            logs.log_error('EVAL FAILED "%s" %s %s' % (Expr,self.DEFINES,Dict))
            Val = 0
        return Val

    def setLock(self,Lock,Key):
        if Lock not in self.Locks: self.Locks[Lock] = False
        if not self.Locks[Lock] :
            self.Locks[Lock]  = Key
            logs.log_info("setLock OK %s %s" % (Lock,Key))
            return True

        logs.log_info("setLock ?? %s %s %s    %s" % (Lock,Key,self.Locks[Lock], Key == self.Locks[Lock]))
        return Key == self.Locks[Lock]

    def releaseLock(self,Lock,Key):
        Was = self.Locks[Lock]
        if Key != Was:
            logs.log_error('release of lock %s attempted by key=%s' %(Lock,Key))
            return 
        logs.log_info("releaseLock  %s %s" % (Lock,Key))
        self.Locks[Lock] = False
            

class processorClass:
    def __init__(self,Father,Name,PAIRS,DEFINES,VARS,LINES,PC):
        self.PAIRS  = PAIRS
        self.DEFINES  = DEFINES
        self.VARS = VARS
        self.LINES  = LINES
        self.PC = PC
        self.Father = Father
        self.Name = Name
        self.Stack = []
        self.Active = True
        self.force = self.Father.force
        self.peek = self.Father.peek
        self.eval = self.Father.eval
        self.rnd = self.Father.rnd
        self.txLines = []
        self.showLine = True

    def run(self):
        logs.log_info("run pref=%s procs=%d %s %s pc=%d %s  %s line=%s vars=%s rnms=%s" % (self.Father.prefix,len(self.Father.Procs),self.Name,self.Active,self.PC,self.Father.apb_state,self.Father.Locks,self.LINES[self.PC],self.VARS,self.Father.Renames))
        if not self.Active: return
        Ok = True
        while Ok:
            Ok = self.execute() 
            logs.log_info(">>>>>> %s %s %d %s" % (self.Name,Ok,self.PC,self.LINES[self.PC]))

    def execute(self):
        if self.PC not in self.LINES:
            print(self.PC,self.LINES)
        Line = self.LINES[self.PC]
        if '//' in Line: Line = Line[:Line.index('//')]
        if self.showLine:
            logs.force_str('tb.LINE',Line)
        wrds = Line.split()
        if wrds==[]: 
            self.PC += 1
            return True
        if (len(wrds)>=3) and (wrds[1] == '='):
            Var = wrds[0]
            Expr = ' '.join(wrds[2:])
            Val = self.eval(Expr)
            self.VARS[Var] = Val
            self.PC += 1
            return False

        if wrds[0] == 'return':
            self.PC = self.Stack.pop(-1)
            return True

        if wrds[0] == '}':
            From = self.PAIRS[self.PC]
            There  = self.LINES[From]
            ww = There.split()
            if ww[0] in ['for','while']:
                self.PC = From
                return True
            if ww[0] == 'def':
                self.Active = False
                return
            self.PC += 1
            return True
        if wrds[0] == 'if':
            Cond = ' '.join(wrds[1:-1])
            Val = self.eval(Cond)
            logs.log_info("EVALIF %s: %d    %s %s" % (self.Name,self.PC,Cond,Val))
            if Val:
                self.PC += 1
                return True
            else:
                To = self.PAIRS[self.PC]
                self.PC = 1+To
                return True
        if wrds[0] == 'while':
            Cond = ' '.join(wrds[1:-1])
            Val = self.eval(Cond)
            if Val:
                self.PC += 1
                return True
            else:
                To = self.PAIRS[self.PC]
                self.PC = 1+To
                return True
                
        if wrds[0] == 'print':
            Str = 'PRINT'+' %s ' % (self.Father.prefix + self.Name)
            for wrd in wrds[1:]:
                if wrd[0] == '"': Str += ' %s ' % wrd[1:-1]
                elif wrd in self.VARS:
                    Str += ' %s ' % hex(self.VARS[wrd])
                else:
                    Str += ' ERROR(%s)' % wrd
            logs.log_info('>>>>>>>>>>>>>>>>> %s' % Str)
            self.PC += 1
            return False


        if wrds[0] == 'wait':
            Cond = wrds[1]
            Val = self.eval(Cond)
#            print("WAIT ",Cond,Val)
            if Val:
                self.PC += 1
                return True 
            return False 
        if wrds[0] == 'call':
            Sub = wrds[1]
            Addr = self.DEFINES[Sub]+1
            self.Stack.append(self.PC+1)
            self.PC = Addr
            return True
        if wrds[0] == 'fork':
            Sub = wrds[1]
            Name = '%s_%s' % (Sub,self.PC)
            self.Father.forkit(Sub,Name)
            self.PC += 1
            return True 

            
        if wrds[0] == 'apb_write':
            Locked = self.Father.setLock('apb',self.PC)
            if not Locked: return False
            Ok = self.apb_write(wrds[1],wrds[2])
            if Ok:
                self.Father.releaseLock('apb',self.PC)
                self.PC += 1
            return False

        if wrds[0] == 'apb_read':
            Locked = self.Father.setLock('apb',self.PC)
            if not Locked: return False
            Ok = self.apb_read(wrds[1],wrds[2])
            if Ok:
                self.Father.releaseLock('apb',self.PC)
                self.PC += 1
            return False

        if wrds[0] == 'apbs_ram':
            Ok = self.apbs_ram(wrds[1],wrds[2])
            if Ok:
                self.PC += 1
                return True
            return False
        if wrds[0] == 'txgen':
            self.generateFrame(wrds)
            self.PC += 1
            return False
        
#        logs.log_info("AGENTS %s %s %s " % (wrds[0],wrds[1:],list(self.Father.Agents.keys())))
#        if wrds[0] in self.Father.Agents:
#            logs.log_info("AGENT %s %s %s " % (wrds[0],wrds[1:],self.Father.Agents[wrds[0]]))
#            Done = self.Father.Agents[wrds[0]].run(wrds[1:])
#            if Done:
#                self.PC += 1
#                return False
#            return True

        logs.log_error("PROC %s got bad line %s" % (self.Name,Line))
        self.PC += 1
        return False


    def eval(self,Expr):
        Tmp = {'peek':self.peek}
        Dict = { **self.VARS, **Tmp}
        Val = eval(Expr,self.DEFINES,Dict)
        return Val

    def apbs_ram(self,Addr,Wdata):
        eA = self.eval(str(Addr))
        eW = self.eval(str(Wdata))
        if 'apbs' in self.Father.SeqObj.agents:
            self.Father.SeqObj.agents['apbs'].action('ram %s %s' % (hex(eA),hex(eW)))
        elif 'axis' in self.Father.SeqObj.agents:
            self.Father.SeqObj.agents['axis'].action('ram %s %s' % (hex(eA),hex(eW)))
        else:
            logs.log_error("APBS_RAM 0x%x 0x%x  %s" % (eA,eW,list(self.Father.SeqObj.agents.keys())))
        return True

    def apb_write(self,Addr,Wdata):
#        logs.log_info("name=%s st=%s" % (self.Name,self.Father.apb_state))
        if self.Father.apb_state == 'idle':
            eA = self.eval(Addr)
            eW = self.eval(Wdata)
#            logs.log_info("APB %s %s %s %s %s    %s %s" % (self.Name,self.Father,self.Father.apb_state,Addr,Wdata,eA,eW))
            self.force('pstrb',15)
            self.force('psel',1)
            self.force('paddr',eA)
            self.force('pwdata',eW)
            self.force('pwrite',1)
            self.Father.apb_state = 'phase0'
            return False

        if self.Father.apb_state == 'phase0':
            self.force('penable',1)
            self.Father.apb_state = 'phase1'
            return False

        if self.Father.apb_state == 'phase1':
            self.force('penable',0)
            self.force('psel',0)
            self.force('pwrite',0)
            self.force('paddr',0)
            self.force('pwdata',0)
            self.Father.apb_state = 'phase2'
            return False
        if self.Father.apb_state == 'phase2':
            self.Father.apb_state = 'idle'
            return True



    def apb_read(self,Var,Addr):
        if Var not in self.VARS: self.VARS[Var] = 0
#        logs.log_info("AAAAA %s %s %s" % (Var,Addr,self.Father.apb_state))
        if self.Father.apb_state == 'idle':
            eA = self.eval(Addr)
            self.force('pstrb',0)
            self.force('psel',1)
            self.force('paddr',eA)
            self.force('pwrite',0)
            self.Father.apb_state = 'phase0'
            return False

        if self.Father.apb_state == 'phase0':
            self.force('penable',1)
            self.force('pwrite',0)
            self.Father.apb_state = 'phase1'
            Rdata = self.peek('%sprdata' % self.Father.prefix)
            self.VARS[Var] = Rdata
            return False

        if self.Father.apb_state == 'phase1':
            self.force('penable',0)
            self.force('psel',0)
            self.force('pwrite',0)
            self.force('paddr',0)
            self.force('pwdata',0)
            self.Father.apb_state = 'phase2'
            logs.log_info("BBBBB %s:%d    var=%s addr=%s (%x)  state=%s %s " % (self.Name,self.PC,Var,Addr,self.eval(Addr),self.Father.apb_state,hex(self.VARS[Var])))
            return False
        if self.Father.apb_state == 'phase2':
            self.Father.apb_state = 'idle'
            return True
        return

    def generateFrame(self,wrds):
        line = ' '.join(wrds[1:])
        params = getParams(line)
        txgen = txGenClass.txGenClass(self)
        if ('from_file=') in line:
            txgen.apbs_ram = self.apbs_ram
            txgen.eval = self.eval
            txgen.action('from_file %s' % line)
            return


        for prm in params:
            Expr = params[prm]
            Val = self.eval(Expr)
            if wrds[1] == 'cl':
                txgen.clParams[prm] = Val
            elif wrds[1] == 'fd':
                txgen.fdParams[prm] = Val
            elif wrds[1] == 'xl':
                txgen.xlParams[prm] = Val
        txgen.apbs_ram = self.apbs_ram
        txgen.action('send %s' % wrds[1])



def getParams(Str):
    Res = {}
    wrds = Str.split()
    for wrd in wrds:
        ww = wrd.split('=')
        if len(ww) == 2:
            Res[ww[0]] = ww[1]
    return Res


