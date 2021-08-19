

import logs
import matches

DB = {}
def help_main(Env):
    Mod = Env.Current
    work(Mod)
#    report(Mod)
    produceCode(Mod)

def produceCode(Mod):
    File = open('%s_efficiency.py' % (Mod.Module),'w')
    File.write(HEADER.replace('MODULE',Mod.Module))
    logs.log_info('CLOCKS: %s' % str(list(DB.keys())))
    for Clk in DB:
        if Clk.startswith('p.'):
            File.write('    def run_posedge_%s(self):\n' % Clk[2:])
            File.write('        self.Touched = []\n')
            File.write('        self.Peeked = {}\n')
#            File.write('        if self.posedge("%s"):\n' % Clk[2:])
        elif Clk.startswith('n.'):
            File.write('    def run_negedge_%s(self):\n' % Clk[2:])
            File.write('        self.Touched = []\n')
            File.write('        self.Peeked = {}\n')
#            File.write('        if self.negedge("%s"):\n' % Clk[2:])
        else:
            logs.log_error('WTF clk=%s' % Clk)
#            File.write('        if self.posedge("%s"):\n' % Clk[2:])
        for Flop in DB[Clk]:
            List = DB[Clk][Flop]
            Rework = reworkExpr(List)
            File.write('        if self.evaluate_valid(%s):\n' % (Rework))
            File.write('            if self.changed("%s"):\n' % (Flop))
            File.write('                self.increment_work("%s")\n' % (Flop))
            File.write('            else:\n')
            File.write('                self.increment_waste("%s")\n' % (Flop))
    File.write('\n\nWIDTH = {}\n')
    for Clk in DB:
        for Flop in DB[Clk]:
            Dir,Wid = Mod.nets[Flop]
            Width = Mod.computeWidth(Wid)
            File.write('WIDTH["%s"] = %d\n' % (Flop,Width))
    File.close()            
    
def reworkExpr(List):
    if type(List[0]) == list:
        return ['||']+List
    return List        

def report(Mod):
    for Key in DB:
        logs.log_info('KEY %s %s' % (Key,DB[Key]))


def work(Mod):
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

        if (Vars!=[]): analyzeBody(Body,Vars,True)

def analyzeBody(Body,Head,Cond):
    if Body[0] == '<=':
        Dest = Body[1]
        record(Dest,Head,Cond)
    elif Body[0] == 'if':
        Plus = Body[1]
        analyzeBody(Body[2],Head,('&&',Plus,Cond))
    elif Body[0] == 'ifelse':
        Yes = Body[1]
        analyzeBody(Body[2],Head,('&&',Yes,Cond))
        analyzeBody(Body[3],Head,('&&',('!',Yes),Cond))
    elif Body[0] == 'list':
        for Item in Body[1:]:
            analyzeBody(Item,Head,Cond)
            
    else:
        logs.log_error('BODY %s' % str(Body))


def record(Flops,Head,Cond):
    Cond0 = simplifyCond(Cond)
    for Clk in Head:
        if type(Flops) is list:
            for Flop in Flops:
                addRecord(Clk,Flop,Cond0)
        else:
            addRecord(Clk,Flops,Cond0)

def addRecord(Clk,Flop,Cond0):
    Key = (Clk,Flop)
    if Clk not in DB: DB[Clk] = {}
    if Flop not in DB[Clk] : DB[Clk][Flop] = []
    DB[Clk][Flop].append(Cond0)

def simplifyCond(Cond):
    if Cond[-1] == True:
        return simplifyCond(Cond[1])

    if matches.matches(Cond,['!',['!','?']]):
        return simplifyCond(matches.Varsx[0])
    if matches.matches(Cond,['!','?']):
        X =  simplifyCond(matches.Varsx[0])
        return ['!',X]
    if matches.matches(Cond,['~','?']):
        X =  simplifyCond(matches.Varsx[0])
        return ['!',X]
    if matches.matches(Cond,['~|','?']):
        X =  simplifyCond(matches.Varsx[0])
        return ['!',['|',X]]
    if Cond[0] in ['&&','||','|','&','==','!=']:
        Res = [Cond[0]]
        for Item in Cond[1:]:
            X = simplifyCond(Item)
            Res.append(X)
        return Res

    if type(Cond) is str:
        return Cond

    logs.log_error('simplifyCond(%s)' % str(Cond))
    return Cond

HEADER = '''
import logs
class MODULE_efficiency(logs.driverClass):
    def __init__(self,Path,Monitors):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Path = Path
        self.History = {}
        self.Peeked = {}
        self.Touched = {}
        self.Counters = {}
    def changed(self,Clk):
        if Clk not in self.History:
            self.History[Clk] = ['x','x']
        if Clk not in self.Touched:
            self.Touched.append(Clk)
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
        if Sig not in self.Counters: self.Counters[Sig] = [0,0]
        Work,Waste = self.Counters[Sig] 
        self.Counters[Sig] = [Work+1,Waste]

    def increment_waste(self,Sig):
        if Sig not in self.Counters: self.Counters[Sig] = [0,0]
        Work,Waste = self.Counters[Sig] 
        self.Counters[Sig] = [Work,Waste+1]

    def evaluate_valid(self,List):
        if type(List) is str:
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
        Used,Wasted = 0,0
        for Sig in self.Counters.keys():
            logs.log_info('MODULE %50s          used=%8d wasted=%8d   width=%d' % (Sig,self.Counters[Sig][0],self.Counters[Sig][1],WIDTH[Sig]))
            Used += self.Counters[Sig][0] * WIDTH[Sig]
            Wasted += self.Counters[Sig][1] * WIDTH[Sig]
        logs.log_info('-----------------------------------------------------------------')
        logs.log_info('Total for MODULE:      used=%d wasted=%d' % (Used,Wasted))
        logs.log_info('-----------------------------------------------------------------\\\n\\\n')
        
    def run(self):
        self.Touched = []
        self.Peeked = {}
'''

