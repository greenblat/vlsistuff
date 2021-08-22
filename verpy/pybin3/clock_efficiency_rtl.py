

import logs
import matches

Holders = {}
Widths = []
class holderClass:
    def __init__(self,Path,Module):
        self.DB = {}
        self.SRC = {}
        self.Path = Path
        self.Module = Module



def help_main(Env):
    if 'clk' in Env.params:
        Clocks = Env.params['clk']
    else:
        Clocks = []
    Mod = Env.Current
    Holders[Mod.Module] = holderClass([],Mod.Module)
    Holders[Mod.Module].Clocks = Clocks
    work(Env,Mod,[],Clocks)
#    report(Mod)
    File = open('%s_efficiency.py' % (Mod.Module),'w')
    File.write(HEADER.replace('MODULE',Mod.Module))
    for Module in Holders:
        Modx = Env.Modules[Module]
        produceCode(Modx,File)
    File.write('\n\nWIDTH = {}\n')
    for Line in Widths:
        File.write(Line)
    File.close()            

def produceCode(Mod,File):
    holder = Holders[Mod.Module]
    Name = Mod.Module
    Path = holder.Path
    logs.log_info('CLOCKS: %s %s' % (Name,str(list(holder.DB.keys()))))
    for Clk in holder.DB:
        if Clk.startswith('p.'):
            File.write('    def run_%s_posedge_%s(self,Path):\n' % (Name,Clk[2:]))
            if Path == []:
                File.write('        self.Touched = []\n')
                File.write('        self.Peeked = {}\n')
                File.write('        self.peekedBus = {}\n')
            Edge = 'posedge'
        elif Clk.startswith('n.'):
            File.write('    def run_%s_negedge_%s(self,Path):\n' % (Name,Clk[2:]))
            if Path == []:
                File.write('        self.Touched = []\n')
                File.write('        self.Peeked = {}\n')
                File.write('        self.peekedBus = {}\n')
            Edge = 'negedge'
        else:
            logs.log_error('WTF %s clk=%s' % (Name,Clk))
            Edge = 'posedge'
        for Inst in Mod.insts:
            Type = Mod.insts[Inst].Type
            if Type in Holders:
                File.write('        self.run_%s_%s_%s(%s)\n' % (Type,Edge,Clk[2:],Holders[Type].Path))
            
        for Flop in holder.DB[Clk]:
            List = holder.DB[Clk][Flop]
            Rework = reworkExpr(List,Path)
            File.write('        Vld = self.evaluate_valid(%s)\n' % (Rework))
            File.write('        if (Vld):\n')
            File.write('            Changed = self.changed("%s")\n' % (path(Path,Flop)))
            File.write('            if Changed:\n')
            File.write('                self.increment_work("%s")\n' % (path(Path,Flop)))
            File.write('            else:\n')
            File.write('                self.increment_waste("%s")\n' % (path(Path,Flop)))
            if holder.SRC[Flop] != []:
                Rework2 = reworkExpr(holder.SRC[Flop],Path)
                File.write('        if self.changed_input("%s",%s):\n' % (path(Path,Flop),Rework2))
                File.write('            self.increment_dropped("%s")\n' % (path(Path,Flop)))
    for Clk in holder.DB:
        for Flop in holder.DB[Clk]:
            if '[' in Flop:
                Width = 1
            else:
                Dir,Wid = Mod.nets[Flop]
                Width = Mod.computeWidth(Wid)
            Widths.append('WIDTH["%s"] = %d\n' % (path(Path,Flop),Width))


def path(Path,Flop):
    Tog = Path+[Flop]
    return '.'.join(Tog)
    
def reworkExpr(List,Path):
    if type(List) == bool: return List
    if type(List) == str:
        if (List in '|| | & && ~ ! + - == > < !='.split()):
            return List
        return '"%s"' % path(Path,List)
    if type(List) is int: return True
    if len(List) == 1:
        return reworkExpr(List[0],Path)
    if type(List[0]) == list:
        LL = ['||']
        for Item in List:
            Fx = reworkExpr(Item,Path)
            LL.append(Fx)
        return LL
    LL = []
    for Item in List:
        Fx = reworkExpr(Item,Path)
        LL.append(Fx)
    return LL

def report(Mod):
    hld = Holders[Mod.Module]
    for Key in hld.DB:
        logs.log_info('KEY %s %s' % (Key,DB[Key]))

def work(Env,Mod,Path,Clocks):
    workThis(Mod,Path,Clocks)
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Env.try_and_load_module(Obj.Type,Env)
        if Obj.Type in Env.Modules:
            SonMod = Env.Modules[Obj.Type]
            Clocks2 = []
            Clocks3 = {}
            for Pin in Obj.conns:
                if  Obj.conns[Pin] in Clocks:
                    Clocks2.append(Pin)
                    Clocks3[Obj.conns[Pin]] = Pin
            if Clocks2 != []:
                Holders[SonMod.Module] = holderClass(Path+[Inst],SonMod.Module)
                Holders[SonMod.Module].Clocks = Clocks3
                work(Env,SonMod,Path+[Inst],Clocks2)



def workThis(Mod,Path,Clocks):
    for Always in Mod.alwayses:
        Head,Body,AlwaysKind = Always
        Vars = []
        if matches.matches(Head,['list', ['edge', 'posedge', '?'], ['edge', 'negedge', '?']]):
            Vars = ['p.'+matches.Varsx[0],'n.'+matches.Varsx[0]]
        elif matches.matches(Head,['list', ['edge', 'negedge', '?'], ['edge', 'negedge', '?']]):
            Vars = ['n.'+matches.Varsx[0],'n.'+matches.Varsx[0]]
        elif matches.matches(Head,['edge', 'posedge', '?']):
            Vars = ['p.'+matches.Varsx[0]]
        elif (Head == '*'):
            Vars = []
        else:
            logs.log_error('failed head match on %s' % str(Head))

        if (Vars!=[]): analyzeBody(Mod,Path,Body,Vars,True)





def analyzeBody(Mod,Path,Body,Head,Cond):
    if Body[0] == '<=':
        Dest = Body[1]
        Src = Body[2]
        record(Mod,Path,Dest,Head,Cond,Src)
    elif Body[0] == 'if':
        Plus = Body[1]
        analyzeBody(Mod,Path,Body[2],Head,('&&',Plus,Cond))
    elif Body[0] == 'ifelse':
        Yes = Body[1]
        analyzeBody(Mod,Path,Body[2],Head,('&&',Yes,Cond))
        analyzeBody(Mod,Path,Body[3],Head,('&&',('!',Yes),Cond))
    elif Body[0] == 'list':
        for Item in Body[1:]:
            analyzeBody(Mod,Path,Item,Head,Cond)
            
    else:
        logs.log_error('BODY %s' % str(Body))


def record(Mod,Path,Flops,Head,Cond,Src):
    if (len(Flops)>1)and(Flops[0] == 'subbit'):
        Flops = '%s[%s]' % (Flops[1],Flops[2])
    if (len(Flops)>1)and(Flops[0] == 'subbus'):
        Flops = Flops[1]
    Cond0 = simplifyCond(Mod,Cond)


    for Clk in Head:
        if type(Flops) is list:
            for Flop in Flops:
                addRecord(Mod,Path,Clk,Flop,Cond0,Src)
        else:
            addRecord(Mod,Path,Clk,Flops,Cond0,Src)

def addRecord(Mod,Path,Clk,Flop,Cond0,Src):
    if type(Flop) is not str: return
    hld = Holders[Mod.Module]
    if Clk not in hld.DB: hld.DB[Clk] = {}
    if Flop not in hld.DB[Clk] : hld.DB[Clk][Flop] = []
    hld.DB[Clk][Flop].append(Cond0)

    if Flop not in hld.SRC:
        hld.SRC[Flop] = []
    if isConstant(Src):
        pass
    else:
        Src1 = simplifyCond(Mod,Src)
        if Src1 not in hld.SRC[Flop]:
             hld.SRC[Flop].append(Src1)

def isConstant(Src):
    if type(Src) is int: return True
    if type(Src) is list:
        if Src[0] in ['hex','bin','dig']: return True
    return False

def simplifyCond(Mod,Cond,Consts=False):
    if Cond == True: return True
    if type(Cond) is int: return Cond
    if Cond[0] == 'subbit':
        return '%s[%s]' % (Cond[1],Cond[2])
    if Cond[0] == 'subbus':
        return Cond[1]
    if Cond[-1] == True:
        return simplifyCond(Mod,Cond[1])

    if Cond[0] in ['hex','bin','dig']:
        return Cond

    if Cond[0] == 'question':
        A = simplifyCond(Mod,Cond[1])
        B = simplifyCond(Mod,Cond[2])
        C = simplifyCond(Mod,Cond[3])
        return ['question',A,B,C]

    if matches.matches(Cond,['!',['!','?']]):
        return simplifyCond(Mod,matches.Varsx[0])
    if matches.matches(Cond,['!','?']):
        X =  simplifyCond(Mod,matches.Varsx[0])
        return ['!',X]
    if matches.matches(Cond,['~','?']):
        X =  simplifyCond(Mod,matches.Varsx[0])
        return ['!',X]
    if matches.matches(Cond,['~|','?']):
        X =  simplifyCond(Mod,matches.Varsx[0])
        return ['!',['|',X]]
    if Cond[0] in ['>=','>>','<<','<','>','*','+','-','curly','^','&&','||','|','&','==','!=']:
        Res = [Cond[0]]
        for Item in Cond[1:]:
            X = simplifyCond(Mod,Item)
            Res.append(X)
        return Res

    if type(Cond) is str:
        if Cond in Mod.parameters:
            return Mod.parameters[Cond]
        if Cond in Mod.localparams:
            return Mod.localparams[Cond]
        return Cond

    logs.log_error('simplifyCond(%s)' % str(Cond))
    return Cond

HEADER = '''
import veri
import logs
def subbit(Sig):
    Bus = Sig[:Sig.index('[')]
    Ind = int(Sig[Sig.index('[')+1:-1])
    return Bus,Ind
class MODULE_efficiency(logs.driverClass):
    def __init__(self,Path,Monitors):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Path = Path
        self.History = {}
        self.Peeked = {}
        self.Touched = {}
        self.Counters = {}
        self.DataInputs = {}
        self.peekedBus = {}


    def changed_input(self,Flop,Exprs):
        Res = []
        if Flop not in self.DataInputs:
            self.DataInputs[Flop] = [0] * len(Exprs)
        for Expr in Exprs:
            Val = self.evaluateExpr(Expr)
            Res.append(Val)
        Ret = Res != self.DataInputs[Flop] 
        self.DataInputs[Flop]  = Res
        return Ret

    def evaluateWidth(self,Expr):
        if type(Expr) is str:
            if '[' in Expr:
                Expr = Expr.replace('[',' ')
                Expr = Expr.replace(']',' ')
                Expr = Expr.replace(':',' ')
                Wrds = Expr.split()
                if len(Wrds)==2:
                    return 1
                Wid = logs.computeWidth(Wrds[1],{})-logs.computeWidth(Wrds[2],{})+1
                return Wid


            X = veri.peek(self.Path+Expr)
            return len(X)
        if type(Expr)is list:
            if Expr[0] in ['bin','hex','dig']:
                return eval(Expr[1])
            if Expr[0] == 'question':
                return self.evaluateWidth(Expr[1])
        logs.log_error('evaluateWidth %s' % str(Expr))
        return 1



    def evaluateExpr(self,Expr):
        if type(Expr) is str:
            if Expr in self.peekedBus:
                return self.peekedBus[Expr]
            Val = self.peekBus(Expr)
            self.peekedBus[Expr] = Val
            return Val
        if type(Expr) is int: return Expr 
        if Expr[0] in ['hex','dig','bin']:
            if type(Expr[2]) is int: return Expr[2]
            return int(Expr[2])
        if Expr[0] == 'question':
            A = self.evaluateExpr(Expr[1])
            B = self.evaluateExpr(Expr[2])
            C = self.evaluateExpr(Expr[3])
            if C: return A
            return B
        if Expr[0] == '!':
            A = self.evaluateExpr(Expr[1])
            if A: return 0
            return 1
            
        if Expr[0] == 'curly':

            Res = 0
            ptr = 1
            while ptr < len(Expr):
                if Expr[ptr] == 'repeat':
                    if type(Expr[2]) is int:
                        Many = Expr[2]
                    else:
                        Many = eval(Expr[2])
                    Val = self.evaluateExpr(Expr[3])
                    Wid = self.evaluateWidth(Expr[3])
                    Res = (Res << (Many*Wid))+Val
                    ptr += 4
                else:
                    Exp = Expr[ptr]
                    Val = self.evaluateExpr(Exp)
                    Wid = self.evaluateWidth(Exp)
                    Res = (Res << Wid)+Val
                    ptr += 1
            return Res

        if Expr[0] == '*':
            A = self.evaluateExpr(Expr[1])
            B = self.evaluateExpr(Expr[2])
            return A*B
        if Expr[0] == '>>':
            A = self.evaluateExpr(Expr[1])
            B = self.evaluateExpr(Expr[2])
            return A>>B

        if Expr[0] == '<<':
            A = self.evaluateExpr(Expr[1])
            B = self.evaluateExpr(Expr[2])
            return A<<B
        if Expr[0] == '+':
            A = self.evaluateExpr(Expr[1])
            B = self.evaluateExpr(Expr[2])
            return A+B
        if Expr[0] == '-':
            A = self.evaluateExpr(Expr[1])
            if len(Expr)==3:
                B = self.evaluateExpr(Expr[2])
                return A-B
            else:
                return -A

        if Expr[0] == '<':
            A = self.evaluateExpr(Expr[1])
            B = self.evaluateExpr(Expr[2])
            return int(A < B)

        if Expr[0] == '==':
            A = self.evaluateExpr(Expr[1])
            B = self.evaluateExpr(Expr[2])
            return int(A == B)
        if Expr[0] == '^':
            A = self.evaluateExpr(Expr[1])
            B = self.evaluateExpr(Expr[2])
            return A^B
        if Expr[0] == '&':
            A = self.evaluateExpr(Expr[1])
            B = self.evaluateExpr(Expr[2])
            return A&B
        if Expr[0] == '||':
            A = self.evaluateExpr(Expr[1])
            if A: return 1
            B = self.evaluateExpr(Expr[2])
            if B: return 1
            return 0
        if Expr[0] == '&&':
            A = self.evaluateExpr(Expr[1])
            if not A: return 0
            B = self.evaluateExpr(Expr[2])
            return int(B!=0)
            return A&B

        if Expr[0] == '|':
            A = self.evaluateExpr(Expr[1])
            if len(Expr) == 2:
                return int(A!=0)
            B = self.evaluateExpr(Expr[2])
            return A|B
        if Expr[0] == '~':
            A = self.evaluateExpr(Expr[1])
            return ~A
            



        logs.log_error('evaluateExpr failed on "%s"' % str(Expr))
        return 0

    def peekBus(self,Bus):
        if '[' in Bus:
            Bus = Bus.replace('[',' ')
            Bus = Bus.replace(']',' ')
            Bus = Bus.replace(':',' ')
            Wrds = Bus.split()
            Val = self.peek(Wrds[0])
            if len(Wrds) == 2:
                return (Val>>int(Wrds[1])) & 1
            elif len(Wrds) == 3:
                X = int(Wrds[1])-int(Wrds[2])+1
                Mask = (1<<X)-1
                return (Val>>int(Wrds[2])) & Mask
        else:
            return self.peek(Bus)

    def changed(self,Clk):
        if Clk not in self.History:
            self.History[Clk] = ['x','x']
        if Clk not in self.Touched:
            self.Touched.append(Clk)
            if '[' in Clk:
                Bus,Ind = subbit(Clk)
                Val = self.peek(Bus)
                Val = (Val>>Ind) & 1
            else:
                Val = self.peek(Clk)
            self.History[Clk] = [Val,self.History[Clk][0]]
        return self.History[Clk][0] != self.History[Clk][1] 

    def posedge(self,Sig):
        self.changed(Sig)
        Now,Was = self.History[Sig]
        return (Now == 1)and(Was == 0)
    def negedge(self,Sig):
        self.changed(Sig)
        Now,Was = self.History[Sig]
        return (Now == 0)and(Was == 1)

    def increment_work(self,Sig):
        if Sig not in self.Counters: self.Counters[Sig] = [0,0,0]
        Work,Waste,Dropped = self.Counters[Sig] 
        self.Counters[Sig] = [Work+1,Waste,Dropped]

    def increment_waste(self,Sig):
        if Sig not in self.Counters: self.Counters[Sig] = [0,0,0]
        Work,Waste,Dropped = self.Counters[Sig] 
        self.Counters[Sig] = [Work,Waste+1,Dropped]

    def increment_dropped(self,Sig):
        if Sig not in self.Counters: self.Counters[Sig] = [0,0,0]
        Work,Waste,Dropped = self.Counters[Sig] 
        self.Counters[Sig] = [Work,Waste,Dropped+1]

    def evaluate_valid(self,List):
        if type(List) is bool: return List
        if type(List) is str:
            List = List.replace('"','')
            if '[' in List:
                Bus,Ind = subbit(List)
                if Bus not in self.Peeked:
                    self.Peeked[Bus] = self.peek(Bus)
                return ((self.Peeked[Bus]>>Ind) & 1) != 0


            if List not in self.Peeked:
                self.Peeked[List] = self.peek(List)
            return self.Peeked[List] != 0
        if List[0] == '||':
            for Item in List[1:]:
                X = self.evaluate_valid(Item)
                if X: return True
            return False

        if List[0] == '&&':
            for Item in List[1:]:
                X = self.evaluate_valid(Item)
                if not X: return False
            return True

        if List[0] == '!':
            X = self.evaluate_valid(List[1])
            return not X


    def onFinish(self):
        logs.log_info('ONFINISH of clock efficiency in MODULE') 
        Used,Wasted,Dropped = 0,0,0
        Keys = list(self.Counters.keys())
        Keys.sort()
        for Sig in Keys:
            logs.log_info('MODULE %40s          used=%8d   wasted=%8d   dropped=%8d   width=%d' % (Sig,self.Counters[Sig][0],self.Counters[Sig][1],self.Counters[Sig][2]-self.Counters[Sig][0],WIDTH[Sig]))
            Used += self.Counters[Sig][0] * WIDTH[Sig]
            Wasted += self.Counters[Sig][1] * WIDTH[Sig]
            Dropped += self.Counters[Sig][2] * WIDTH[Sig]
        logs.log_info('-----------------------------------------------------------------')
        logs.log_info('Total for MODULE:      used=%d wasted=%d dropped=%d' % (Used,Wasted,Dropped-Used))
        logs.log_info('-----------------------------------------------------------------\\\n\\n')
        
    def run(self):
        self.Touched = []
        self.Peeked = {}
        self.PeekeBus = {}
'''

