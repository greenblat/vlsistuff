
import logs
def subbit(Sig):
    Bus = Sig[:Sig.index('[')]
    Ind = int(Sig[Sig.index('[')+1:-1])
    return Bus,Ind
class encrypt_piped_efficiency(logs.driverClass):
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

    def evaluateExpr(self,Expr):
        if type(Expr) is str:
            if Expr in self.peekedBus:
                return self.peekedBus[Expr]
            Val = self.peekBus(Expr)
            self.peekedBus[Expr] = Val
            return Val
        if type(Expr) is int: return Expr 
        if Expr[0] == '^':
            A = self.evaluateExpr(Expr[1])
            B = self.evaluateExpr(Expr[2])
            return A^B
        if Expr[0] == '&':
            A = self.evaluateExpr(Expr[1])
            B = self.evaluateExpr(Expr[2])
            return A&B
        if Expr[0] == '|':
            A = self.evaluateExpr(Expr[1])
            B = self.evaluateExpr(Expr[2])
            return A|B
        if Expr[0] == '~':
            A = self.evaluateExpr(Expr[1])
            return ~A
            



        logs.log_error('evaluateExpr failed on "%s"' % str(Expr))

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
        logs.log_info('ONFINISH of clock efficiency in encrypt_piped') 
        Used,Wasted,Dropped = 0,0,0
        for Sig in self.Counters.keys():
            logs.log_info('encrypt_piped %50s          used=%8d   wasted=%8d   dropped=%8d   width=%d' % (Sig,self.Counters[Sig][0],self.Counters[Sig][1],self.Counters[Sig][2]-self.Counters[Sig][0],WIDTH[Sig]))
            Used += self.Counters[Sig][0] * WIDTH[Sig]
            Wasted += self.Counters[Sig][1] * WIDTH[Sig]
            Dropped += self.Counters[Sig][2] * WIDTH[Sig]
        logs.log_info('-----------------------------------------------------------------')
        logs.log_info('Total for encrypt_piped:      used=%d wasted=%d dropped=%d' % (Used,Wasted,Dropped-Used))
        logs.log_info('-----------------------------------------------------------------\
\
')
        
    def run(self):
        self.Touched = []
        self.Peeked = {}
        self.PeekeBus = {}
    def run_posedge_clk(self):
        self.Touched = []
        self.Peeked = {}
        self.peekedBus = {}
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'vldin', 'rst_n']])
        if (Vld):
            Changed = self.changed("stage0")
            if Changed:
                self.increment_work("stage0")
            else:
                self.increment_waste("stage0")
        if self.changed_input("stage0",[['^', 'datain', 'CONST']]):
            self.increment_dropped("stage0")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], 'rst_n'])
        if (Vld):
            Changed = self.changed("vlds[0]")
            if Changed:
                self.increment_work("vlds[0]")
            else:
                self.increment_waste("vlds[0]")
        if self.changed_input("vlds[0]",['vldin']):
            self.increment_dropped("vlds[0]")
        Vld = self.evaluate_valid("vlds[0]")
        if (Vld):
            Changed = self.changed("stage1")
            if Changed:
                self.increment_work("stage1")
            else:
                self.increment_waste("stage1")
        if self.changed_input("stage1",['tmpb1']):
            self.increment_dropped("stage1")
        Vld = self.evaluate_valid(True)
        if (Vld):
            Changed = self.changed("vlds[1]")
            if Changed:
                self.increment_work("vlds[1]")
            else:
                self.increment_waste("vlds[1]")
        if self.changed_input("vlds[1]",['vlds[0]']):
            self.increment_dropped("vlds[1]")
        Vld = self.evaluate_valid("vlds[1]")
        if (Vld):
            Changed = self.changed("stage2")
            if Changed:
                self.increment_work("stage2")
            else:
                self.increment_waste("stage2")
        if self.changed_input("stage2",['tmpb2']):
            self.increment_dropped("stage2")
        Vld = self.evaluate_valid(True)
        if (Vld):
            Changed = self.changed("vlds[2]")
            if Changed:
                self.increment_work("vlds[2]")
            else:
                self.increment_waste("vlds[2]")
        if self.changed_input("vlds[2]",['vlds[1]']):
            self.increment_dropped("vlds[2]")
        Vld = self.evaluate_valid("vlds[2]")
        if (Vld):
            Changed = self.changed("stage3")
            if Changed:
                self.increment_work("stage3")
            else:
                self.increment_waste("stage3")
        if self.changed_input("stage3",['tmpb3']):
            self.increment_dropped("stage3")
        Vld = self.evaluate_valid(True)
        if (Vld):
            Changed = self.changed("vlds[3]")
            if Changed:
                self.increment_work("vlds[3]")
            else:
                self.increment_waste("vlds[3]")
        if self.changed_input("vlds[3]",['vlds[2]']):
            self.increment_dropped("vlds[3]")
        Vld = self.evaluate_valid("vlds[3]")
        if (Vld):
            Changed = self.changed("stage4")
            if Changed:
                self.increment_work("stage4")
            else:
                self.increment_waste("stage4")
        if self.changed_input("stage4",['tmpb4']):
            self.increment_dropped("stage4")
        Vld = self.evaluate_valid(True)
        if (Vld):
            Changed = self.changed("vlds[4]")
            if Changed:
                self.increment_work("vlds[4]")
            else:
                self.increment_waste("vlds[4]")
        if self.changed_input("vlds[4]",['vlds[3]']):
            self.increment_dropped("vlds[4]")
        Vld = self.evaluate_valid("vlds[4]")
        if (Vld):
            Changed = self.changed("stage5")
            if Changed:
                self.increment_work("stage5")
            else:
                self.increment_waste("stage5")
        if self.changed_input("stage5",['tmpb5']):
            self.increment_dropped("stage5")
        Vld = self.evaluate_valid(True)
        if (Vld):
            Changed = self.changed("vlds[5]")
            if Changed:
                self.increment_work("vlds[5]")
            else:
                self.increment_waste("vlds[5]")
        if self.changed_input("vlds[5]",['vlds[4]']):
            self.increment_dropped("vlds[5]")
        Vld = self.evaluate_valid("vlds[5]")
        if (Vld):
            Changed = self.changed("stage6")
            if Changed:
                self.increment_work("stage6")
            else:
                self.increment_waste("stage6")
        if self.changed_input("stage6",['tmpb6']):
            self.increment_dropped("stage6")
        Vld = self.evaluate_valid(True)
        if (Vld):
            Changed = self.changed("vlds[6]")
            if Changed:
                self.increment_work("vlds[6]")
            else:
                self.increment_waste("vlds[6]")
        if self.changed_input("vlds[6]",['vlds[5]']):
            self.increment_dropped("vlds[6]")
        Vld = self.evaluate_valid("vlds[6]")
        if (Vld):
            Changed = self.changed("stage7")
            if Changed:
                self.increment_work("stage7")
            else:
                self.increment_waste("stage7")
        if self.changed_input("stage7",['tmpb7']):
            self.increment_dropped("stage7")
        Vld = self.evaluate_valid(True)
        if (Vld):
            Changed = self.changed("vlds[7]")
            if Changed:
                self.increment_work("vlds[7]")
            else:
                self.increment_waste("vlds[7]")
        if self.changed_input("vlds[7]",['vlds[6]']):
            self.increment_dropped("vlds[7]")
        Vld = self.evaluate_valid("vlds[7]")
        if (Vld):
            Changed = self.changed("stage8")
            if Changed:
                self.increment_work("stage8")
            else:
                self.increment_waste("stage8")
        if self.changed_input("stage8",['tmpb8']):
            self.increment_dropped("stage8")
        Vld = self.evaluate_valid(True)
        if (Vld):
            Changed = self.changed("vlds[8]")
            if Changed:
                self.increment_work("vlds[8]")
            else:
                self.increment_waste("vlds[8]")
        if self.changed_input("vlds[8]",['vlds[7]']):
            self.increment_dropped("vlds[8]")
        Vld = self.evaluate_valid("vlds[8]")
        if (Vld):
            Changed = self.changed("stage9")
            if Changed:
                self.increment_work("stage9")
            else:
                self.increment_waste("stage9")
        if self.changed_input("stage9",['tmpb9']):
            self.increment_dropped("stage9")
        Vld = self.evaluate_valid(True)
        if (Vld):
            Changed = self.changed("vlds[9]")
            if Changed:
                self.increment_work("vlds[9]")
            else:
                self.increment_waste("vlds[9]")
        if self.changed_input("vlds[9]",['vlds[8]']):
            self.increment_dropped("vlds[9]")
        Vld = self.evaluate_valid("vlds[9]")
        if (Vld):
            Changed = self.changed("stage10")
            if Changed:
                self.increment_work("stage10")
            else:
                self.increment_waste("stage10")
        if self.changed_input("stage10",['tmpb10']):
            self.increment_dropped("stage10")
        Vld = self.evaluate_valid(True)
        if (Vld):
            Changed = self.changed("vlds[10]")
            if Changed:
                self.increment_work("vlds[10]")
            else:
                self.increment_waste("vlds[10]")
        if self.changed_input("vlds[10]",['vlds[9]']):
            self.increment_dropped("vlds[10]")
        Vld = self.evaluate_valid("vlds[10]")
        if (Vld):
            Changed = self.changed("stage11")
            if Changed:
                self.increment_work("stage11")
            else:
                self.increment_waste("stage11")
        if self.changed_input("stage11",['tmpb11']):
            self.increment_dropped("stage11")
        Vld = self.evaluate_valid(True)
        if (Vld):
            Changed = self.changed("vlds[11]")
            if Changed:
                self.increment_work("vlds[11]")
            else:
                self.increment_waste("vlds[11]")
        if self.changed_input("vlds[11]",['vlds[10]']):
            self.increment_dropped("vlds[11]")
        Vld = self.evaluate_valid("vlds[11]")
        if (Vld):
            Changed = self.changed("stage12")
            if Changed:
                self.increment_work("stage12")
            else:
                self.increment_waste("stage12")
        if self.changed_input("stage12",['tmpb12']):
            self.increment_dropped("stage12")
        Vld = self.evaluate_valid(True)
        if (Vld):
            Changed = self.changed("vlds[12]")
            if Changed:
                self.increment_work("vlds[12]")
            else:
                self.increment_waste("vlds[12]")
        if self.changed_input("vlds[12]",['vlds[11]']):
            self.increment_dropped("vlds[12]")
    def run_negedge_clk(self):
        self.Touched = []
        self.Peeked = {}
        self.peekedBus = {}
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'vldin', 'rst_n']])
        if (Vld):
            Changed = self.changed("stage0")
            if Changed:
                self.increment_work("stage0")
            else:
                self.increment_waste("stage0")
        if self.changed_input("stage0",[['^', 'datain', 'CONST']]):
            self.increment_dropped("stage0")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], 'rst_n'])
        if (Vld):
            Changed = self.changed("vlds[0]")
            if Changed:
                self.increment_work("vlds[0]")
            else:
                self.increment_waste("vlds[0]")
        if self.changed_input("vlds[0]",['vldin']):
            self.increment_dropped("vlds[0]")


WIDTH = {}
WIDTH["stage0"] = 32
WIDTH["vlds[0]"] = 1
WIDTH["stage1"] = 32
WIDTH["vlds[1]"] = 1
WIDTH["stage2"] = 32
WIDTH["vlds[2]"] = 1
WIDTH["stage3"] = 32
WIDTH["vlds[3]"] = 1
WIDTH["stage4"] = 32
WIDTH["vlds[4]"] = 1
WIDTH["stage5"] = 32
WIDTH["vlds[5]"] = 1
WIDTH["stage6"] = 32
WIDTH["vlds[6]"] = 1
WIDTH["stage7"] = 32
WIDTH["vlds[7]"] = 1
WIDTH["stage8"] = 32
WIDTH["vlds[8]"] = 1
WIDTH["stage9"] = 32
WIDTH["vlds[9]"] = 1
WIDTH["stage10"] = 32
WIDTH["vlds[10]"] = 1
WIDTH["stage11"] = 32
WIDTH["vlds[11]"] = 1
WIDTH["stage12"] = 32
WIDTH["vlds[12]"] = 1
WIDTH["stage0"] = 32
WIDTH["vlds[0]"] = 1
