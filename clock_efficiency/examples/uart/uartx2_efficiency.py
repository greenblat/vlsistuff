
import veri
import logs
def subbit(Sig):
    Bus = Sig[:Sig.index('[')]
    Ind = int(Sig[Sig.index('[')+1:-1])
    return Bus,Ind
class uartx2_efficiency(logs.driverClass):
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
                Wid = eval(Wrds[1])-eval(Wrds[2])+1
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
        if Expr[0] == 'bin':
            if type(Expr[2]) is int: return Expr[2]
            return int(Expr[2])
        if Expr[0] == 'hex':
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
        logs.log_info('ONFINISH of clock efficiency in uartx2') 
        Used,Wasted,Dropped = 0,0,0
        Keys = list(self.Counters.keys())
        Keys.sort()
        for Sig in Keys:
            logs.log_info('uartx2 %40s          used=%8d   wasted=%8d   dropped=%8d   width=%d' % (Sig,self.Counters[Sig][0],self.Counters[Sig][1],self.Counters[Sig][2]-self.Counters[Sig][0],WIDTH[Sig]))
            Used += self.Counters[Sig][0] * WIDTH[Sig]
            Wasted += self.Counters[Sig][1] * WIDTH[Sig]
            Dropped += self.Counters[Sig][2] * WIDTH[Sig]
        logs.log_info('-----------------------------------------------------------------')
        logs.log_info('Total for uartx2:      used=%d wasted=%d dropped=%d' % (Used,Wasted,Dropped-Used))
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
        Vld = self.evaluate_valid(True)
        if (Vld):
            Changed = self.changed("rxd1")
            if Changed:
                self.increment_work("rxd1")
            else:
                self.increment_waste("rxd1")
        if self.changed_input("rxd1",['rxd']):
            self.increment_dropped("rxd1")
        Vld = self.evaluate_valid(True)
        if (Vld):
            Changed = self.changed("rxd_raw")
            if Changed:
                self.increment_work("rxd_raw")
            else:
                self.increment_waste("rxd_raw")
        if self.changed_input("rxd_raw",['rxd1']):
            self.increment_dropped("rxd_raw")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'rx_midbit', 'rst_n']])
        if (Vld):
            Changed = self.changed("rxd_filt")
            if Changed:
                self.increment_work("rxd_filt")
            else:
                self.increment_waste("rxd_filt")
        if self.changed_input("rxd_filt",[['question', 'is_one', ['bin', '1', '1'], ['question', 'is_zero', ['bin', '1', '0'], 'rxd_filt']]]):
            self.increment_dropped("rxd_filt")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], 'rst_n'])
        if (Vld):
            Changed = self.changed("last_rxd")
            if Changed:
                self.increment_work("last_rxd")
            else:
                self.increment_waste("last_rxd")
        if self.changed_input("last_rxd",['rxd_raw']):
            self.increment_dropped("last_rxd")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'rx_midbit', 'rst_n']])
        if (Vld):
            Changed = self.changed("was_bit_noise")
            if Changed:
                self.increment_work("was_bit_noise")
            else:
                self.increment_waste("was_bit_noise")
        if self.changed_input("was_bit_noise",['is_noise']):
            self.increment_dropped("was_bit_noise")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', ['&&', 'rxnewdata', 'rx_bufa_valid'], 'rst_n'], ['&&', ['&&', 'rxnewdata', ['!', 'rx_bufa_valid']], ['&&', ['!', ['&&', 'rxnewdata', 'rx_bufa_valid']], 'rst_n']]])
        if (Vld):
            Changed = self.changed("rx_overrun")
            if Changed:
                self.increment_work("rx_overrun")
            else:
                self.increment_waste("rx_overrun")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], 'rst_n'])
        if (Vld):
            Changed = self.changed("rxinbit")
            if Changed:
                self.increment_work("rxinbit")
            else:
                self.increment_waste("rxinbit")
        if self.changed_input("rxinbit",[['question', 'negedge_rxd', 0, ['question', ['!', 'rx_active'], 0, ['question', ['<', 'rxinbit', 'baudrate'], 'rxinbit', 0]]]]):
            self.increment_dropped("rxinbit")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'negedge_rxd', 'rst_n'], ['&&', 'rxnewdata', ['&&', ['!', 'negedge_rxd'], 'rst_n']]])
        if (Vld):
            Changed = self.changed("rx_active")
            if Changed:
                self.increment_work("rx_active")
            else:
                self.increment_waste("rx_active")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'negedge_rxd', 'rst_n'], ['&&', 'rxnewdata', ['&&', ['!', 'negedge_rxd'], 'rst_n']], ['&&', 'rx_shift', ['&&', ['!', 'rxnewdata'], ['&&', ['!', 'negedge_rxd'], 'rst_n']]]])
        if (Vld):
            Changed = self.changed("rxsr")
            if Changed:
                self.increment_work("rxsr")
            else:
                self.increment_waste("rxsr")
        if self.changed_input("rxsr",[['curly', ['question', 'first', ['bin', '1', '0'], 'rxd_filt'], ['question', 'control_eight_bits', 'rxd_filt', 'rxsr[10]'], 'rxsr[9:1]']]):
            self.increment_dropped("rxsr")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'negedge_rxd', 'rst_n'], ['&&', 'rx_shift', ['&&', ['!', 'rxnewdata'], ['&&', ['!', 'negedge_rxd'], 'rst_n']]]])
        if (Vld):
            Changed = self.changed("rx_noise")
            if Changed:
                self.increment_work("rx_noise")
            else:
                self.increment_waste("rx_noise")
        if self.changed_input("rx_noise",[['|', 'rx_noise', ['||', 'was_bit_noise', ['&&', 'first', 'rxd_filt']]]]):
            self.increment_dropped("rx_noise")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'negedge_rxd', 'rst_n'], ['&&', 'rxnewdata', ['&&', ['!', 'negedge_rxd'], 'rst_n']], ['&&', 'rx_shift', ['&&', ['!', 'rxnewdata'], ['&&', ['!', 'negedge_rxd'], 'rst_n']]]])
        if (Vld):
            Changed = self.changed("first")
            if Changed:
                self.increment_work("first")
            else:
                self.increment_waste("first")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'rxnewdata', 'rst_n']])
        if (Vld):
            Changed = self.changed("rx_bufa")
            if Changed:
                self.increment_work("rx_bufa")
            else:
                self.increment_waste("rx_bufa")
        if self.changed_input("rx_bufa",['rxsr[9:1]']):
            self.increment_dropped("rx_bufa")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', ['&&', 'rx_bufa_valid', ['!', 'rx_bufb_valid']], 'rst_n']])
        if (Vld):
            Changed = self.changed("rx_bufb")
            if Changed:
                self.increment_work("rx_bufb")
            else:
                self.increment_waste("rx_bufb")
        if self.changed_input("rx_bufb",['rx_bufa[7:0]']):
            self.increment_dropped("rx_bufb")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', ['&&', 'rx_bufa_valid', ['!', 'rx_bufb_valid']], 'rst_n'], ['&&', 'rxnewdata', 'rst_n']])
        if (Vld):
            Changed = self.changed("rx_bufa_valid")
            if Changed:
                self.increment_work("rx_bufa_valid")
            else:
                self.increment_waste("rx_bufa_valid")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', ['&&', 'rx_bufa_valid', ['!', 'rx_bufb_valid']], 'rst_n'], ['&&', 'read_rx', 'rst_n']])
        if (Vld):
            Changed = self.changed("rx_bufb_valid")
            if Changed:
                self.increment_work("rx_bufb_valid")
            else:
                self.increment_waste("rx_bufb_valid")
        if self.changed_input("rx_bufb_valid",[['&&', 'filtered_ok_byte', 'byte_is_acceptable']]):
            self.increment_dropped("rx_bufb_valid")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'rxnewdata', 'rst_n']])
        if (Vld):
            Changed = self.changed("rxstatusa")
            if Changed:
                self.increment_work("rxstatusa")
            else:
                self.increment_waste("rxstatusa")
        if self.changed_input("rxstatusa",[['curly', 'rx_overrun', 'rx_framing_error', 'rx_noise']]):
            self.increment_dropped("rxstatusa")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', ['&&', 'rx_bufa_valid', ['!', 'rx_bufb_valid']], 'rst_n']])
        if (Vld):
            Changed = self.changed("rxstatusb")
            if Changed:
                self.increment_work("rxstatusb")
            else:
                self.increment_waste("rxstatusb")
        if self.changed_input("rxstatusb",[['curly', 'rx_bufa[8]', 'rxstatusa[2]', 'rx_parity_error', 'rxstatusa[1:0]']]):
            self.increment_dropped("rxstatusb")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', ['&&', 'write_tx', ['!', 'tx_bufa_valid']], 'rst_n']])
        if (Vld):
            Changed = self.changed("tx_bufa")
            if Changed:
                self.increment_work("tx_bufa")
            else:
                self.increment_waste("tx_bufa")
        if self.changed_input("tx_bufa",['txdata']):
            self.increment_dropped("tx_bufa")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', ['&&', 'write_tx', ['!', 'tx_bufa_valid']], 'rst_n'], ['&&', ['&&', ['!', 'tx_bufb_valid'], 'tx_bufa_valid'], 'rst_n']])
        if (Vld):
            Changed = self.changed("tx_bufa_valid")
            if Changed:
                self.increment_work("tx_bufa_valid")
            else:
                self.increment_waste("tx_bufa_valid")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', ['&&', ['!', 'tx_bufb_valid'], 'tx_bufa_valid'], 'rst_n']])
        if (Vld):
            Changed = self.changed("tx_bufb")
            if Changed:
                self.increment_work("tx_bufb")
            else:
                self.increment_waste("tx_bufb")
        if self.changed_input("tx_bufb",[['curly', 'txbit_nine', 'tx_bufa']]):
            self.increment_dropped("tx_bufb")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', ['&&', ['!', 'tx_bufb_valid'], 'tx_bufa_valid'], 'rst_n'], ['&&', 'tx_start', 'rst_n']])
        if (Vld):
            Changed = self.changed("tx_bufb_valid")
            if Changed:
                self.increment_work("tx_bufb_valid")
            else:
                self.increment_waste("tx_bufb_valid")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', ['<', 'txinbit', 'baudrate'], 'rst_n'], ['&&', ['!', ['<', 'txinbit', 'baudrate']], 'rst_n']])
        if (Vld):
            Changed = self.changed("txinbit")
            if Changed:
                self.increment_work("txinbit")
            else:
                self.increment_waste("txinbit")
        if self.changed_input("txinbit",['txinbit']):
            self.increment_dropped("txinbit")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'tx_start', 'rst_n'], ['&&', 'tx_shift', ['&&', ['!', 'tx_start'], 'rst_n']], ['&&', ['!', 'tx_active'], ['&&', ['!', 'tx_shift'], ['&&', ['!', 'tx_start'], 'rst_n']]]])
        if (Vld):
            Changed = self.changed("txsr")
            if Changed:
                self.increment_work("txsr")
            else:
                self.increment_waste("txsr")
        if self.changed_input("txsr",[['curly', 'control_nine_bits', 'tx_bufb', ['bin', '1', '0']], ['curly', ['bin', '1', '0'], 'txsr[10:1]']]):
            self.increment_dropped("txsr")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'tx_start', 'rst_n'], ['&&', ['==', 'txsr', ['bin', '11', '0']], ['&&', ['!', 'tx_start'], 'rst_n']]])
        if (Vld):
            Changed = self.changed("tx_active")
            if Changed:
                self.increment_work("tx_active")
            else:
                self.increment_waste("tx_active")
    def run_negedge_clk(self):
        self.Touched = []
        self.Peeked = {}
        self.peekedBus = {}
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'rx_midbit', 'rst_n']])
        if (Vld):
            Changed = self.changed("rxd_filt")
            if Changed:
                self.increment_work("rxd_filt")
            else:
                self.increment_waste("rxd_filt")
        if self.changed_input("rxd_filt",[['question', 'is_one', ['bin', '1', '1'], ['question', 'is_zero', ['bin', '1', '0'], 'rxd_filt']]]):
            self.increment_dropped("rxd_filt")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], 'rst_n'])
        if (Vld):
            Changed = self.changed("last_rxd")
            if Changed:
                self.increment_work("last_rxd")
            else:
                self.increment_waste("last_rxd")
        if self.changed_input("last_rxd",['rxd_raw']):
            self.increment_dropped("last_rxd")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'rx_midbit', 'rst_n']])
        if (Vld):
            Changed = self.changed("was_bit_noise")
            if Changed:
                self.increment_work("was_bit_noise")
            else:
                self.increment_waste("was_bit_noise")
        if self.changed_input("was_bit_noise",['is_noise']):
            self.increment_dropped("was_bit_noise")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', ['&&', 'rxnewdata', 'rx_bufa_valid'], 'rst_n'], ['&&', ['&&', 'rxnewdata', ['!', 'rx_bufa_valid']], ['&&', ['!', ['&&', 'rxnewdata', 'rx_bufa_valid']], 'rst_n']]])
        if (Vld):
            Changed = self.changed("rx_overrun")
            if Changed:
                self.increment_work("rx_overrun")
            else:
                self.increment_waste("rx_overrun")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], 'rst_n'])
        if (Vld):
            Changed = self.changed("rxinbit")
            if Changed:
                self.increment_work("rxinbit")
            else:
                self.increment_waste("rxinbit")
        if self.changed_input("rxinbit",[['question', 'negedge_rxd', 0, ['question', ['!', 'rx_active'], 0, ['question', ['<', 'rxinbit', 'baudrate'], 'rxinbit', 0]]]]):
            self.increment_dropped("rxinbit")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'negedge_rxd', 'rst_n'], ['&&', 'rxnewdata', ['&&', ['!', 'negedge_rxd'], 'rst_n']]])
        if (Vld):
            Changed = self.changed("rx_active")
            if Changed:
                self.increment_work("rx_active")
            else:
                self.increment_waste("rx_active")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'negedge_rxd', 'rst_n'], ['&&', 'rxnewdata', ['&&', ['!', 'negedge_rxd'], 'rst_n']], ['&&', 'rx_shift', ['&&', ['!', 'rxnewdata'], ['&&', ['!', 'negedge_rxd'], 'rst_n']]]])
        if (Vld):
            Changed = self.changed("rxsr")
            if Changed:
                self.increment_work("rxsr")
            else:
                self.increment_waste("rxsr")
        if self.changed_input("rxsr",[['curly', ['question', 'first', ['bin', '1', '0'], 'rxd_filt'], ['question', 'control_eight_bits', 'rxd_filt', 'rxsr[10]'], 'rxsr[9:1]']]):
            self.increment_dropped("rxsr")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'negedge_rxd', 'rst_n'], ['&&', 'rx_shift', ['&&', ['!', 'rxnewdata'], ['&&', ['!', 'negedge_rxd'], 'rst_n']]]])
        if (Vld):
            Changed = self.changed("rx_noise")
            if Changed:
                self.increment_work("rx_noise")
            else:
                self.increment_waste("rx_noise")
        if self.changed_input("rx_noise",[['|', 'rx_noise', ['||', 'was_bit_noise', ['&&', 'first', 'rxd_filt']]]]):
            self.increment_dropped("rx_noise")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'negedge_rxd', 'rst_n'], ['&&', 'rxnewdata', ['&&', ['!', 'negedge_rxd'], 'rst_n']], ['&&', 'rx_shift', ['&&', ['!', 'rxnewdata'], ['&&', ['!', 'negedge_rxd'], 'rst_n']]]])
        if (Vld):
            Changed = self.changed("first")
            if Changed:
                self.increment_work("first")
            else:
                self.increment_waste("first")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'rxnewdata', 'rst_n']])
        if (Vld):
            Changed = self.changed("rx_bufa")
            if Changed:
                self.increment_work("rx_bufa")
            else:
                self.increment_waste("rx_bufa")
        if self.changed_input("rx_bufa",['rxsr[9:1]']):
            self.increment_dropped("rx_bufa")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', ['&&', 'rx_bufa_valid', ['!', 'rx_bufb_valid']], 'rst_n']])
        if (Vld):
            Changed = self.changed("rx_bufb")
            if Changed:
                self.increment_work("rx_bufb")
            else:
                self.increment_waste("rx_bufb")
        if self.changed_input("rx_bufb",['rx_bufa[7:0]']):
            self.increment_dropped("rx_bufb")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', ['&&', 'rx_bufa_valid', ['!', 'rx_bufb_valid']], 'rst_n'], ['&&', 'rxnewdata', 'rst_n']])
        if (Vld):
            Changed = self.changed("rx_bufa_valid")
            if Changed:
                self.increment_work("rx_bufa_valid")
            else:
                self.increment_waste("rx_bufa_valid")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', ['&&', 'rx_bufa_valid', ['!', 'rx_bufb_valid']], 'rst_n'], ['&&', 'read_rx', 'rst_n']])
        if (Vld):
            Changed = self.changed("rx_bufb_valid")
            if Changed:
                self.increment_work("rx_bufb_valid")
            else:
                self.increment_waste("rx_bufb_valid")
        if self.changed_input("rx_bufb_valid",[['&&', 'filtered_ok_byte', 'byte_is_acceptable']]):
            self.increment_dropped("rx_bufb_valid")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'rxnewdata', 'rst_n']])
        if (Vld):
            Changed = self.changed("rxstatusa")
            if Changed:
                self.increment_work("rxstatusa")
            else:
                self.increment_waste("rxstatusa")
        if self.changed_input("rxstatusa",[['curly', 'rx_overrun', 'rx_framing_error', 'rx_noise']]):
            self.increment_dropped("rxstatusa")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', ['&&', 'rx_bufa_valid', ['!', 'rx_bufb_valid']], 'rst_n']])
        if (Vld):
            Changed = self.changed("rxstatusb")
            if Changed:
                self.increment_work("rxstatusb")
            else:
                self.increment_waste("rxstatusb")
        if self.changed_input("rxstatusb",[['curly', 'rx_bufa[8]', 'rxstatusa[2]', 'rx_parity_error', 'rxstatusa[1:0]']]):
            self.increment_dropped("rxstatusb")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', ['&&', 'write_tx', ['!', 'tx_bufa_valid']], 'rst_n']])
        if (Vld):
            Changed = self.changed("tx_bufa")
            if Changed:
                self.increment_work("tx_bufa")
            else:
                self.increment_waste("tx_bufa")
        if self.changed_input("tx_bufa",['txdata']):
            self.increment_dropped("tx_bufa")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', ['&&', 'write_tx', ['!', 'tx_bufa_valid']], 'rst_n'], ['&&', ['&&', ['!', 'tx_bufb_valid'], 'tx_bufa_valid'], 'rst_n']])
        if (Vld):
            Changed = self.changed("tx_bufa_valid")
            if Changed:
                self.increment_work("tx_bufa_valid")
            else:
                self.increment_waste("tx_bufa_valid")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', ['&&', ['!', 'tx_bufb_valid'], 'tx_bufa_valid'], 'rst_n']])
        if (Vld):
            Changed = self.changed("tx_bufb")
            if Changed:
                self.increment_work("tx_bufb")
            else:
                self.increment_waste("tx_bufb")
        if self.changed_input("tx_bufb",[['curly', 'txbit_nine', 'tx_bufa']]):
            self.increment_dropped("tx_bufb")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', ['&&', ['!', 'tx_bufb_valid'], 'tx_bufa_valid'], 'rst_n'], ['&&', 'tx_start', 'rst_n']])
        if (Vld):
            Changed = self.changed("tx_bufb_valid")
            if Changed:
                self.increment_work("tx_bufb_valid")
            else:
                self.increment_waste("tx_bufb_valid")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', ['<', 'txinbit', 'baudrate'], 'rst_n'], ['&&', ['!', ['<', 'txinbit', 'baudrate']], 'rst_n']])
        if (Vld):
            Changed = self.changed("txinbit")
            if Changed:
                self.increment_work("txinbit")
            else:
                self.increment_waste("txinbit")
        if self.changed_input("txinbit",['txinbit']):
            self.increment_dropped("txinbit")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'tx_start', 'rst_n'], ['&&', 'tx_shift', ['&&', ['!', 'tx_start'], 'rst_n']], ['&&', ['!', 'tx_active'], ['&&', ['!', 'tx_shift'], ['&&', ['!', 'tx_start'], 'rst_n']]]])
        if (Vld):
            Changed = self.changed("txsr")
            if Changed:
                self.increment_work("txsr")
            else:
                self.increment_waste("txsr")
        if self.changed_input("txsr",[['curly', 'control_nine_bits', 'tx_bufb', ['bin', '1', '0']], ['curly', ['bin', '1', '0'], 'txsr[10:1]']]):
            self.increment_dropped("txsr")
        Vld = self.evaluate_valid(['||', ['!', 'rst_n'], ['&&', 'tx_start', 'rst_n'], ['&&', ['==', 'txsr', ['bin', '11', '0']], ['&&', ['!', 'tx_start'], 'rst_n']]])
        if (Vld):
            Changed = self.changed("tx_active")
            if Changed:
                self.increment_work("tx_active")
            else:
                self.increment_waste("tx_active")


WIDTH = {}
WIDTH["rxd1"] = 1
WIDTH["rxd_raw"] = 1
WIDTH["rxd_filt"] = 1
WIDTH["last_rxd"] = 1
WIDTH["was_bit_noise"] = 1
WIDTH["rx_overrun"] = 1
WIDTH["rxinbit"] = 16
WIDTH["rx_active"] = 1
WIDTH["rxsr"] = 11
WIDTH["rx_noise"] = 1
WIDTH["first"] = 1
WIDTH["rx_bufa"] = 9
WIDTH["rx_bufb"] = 8
WIDTH["rx_bufa_valid"] = 1
WIDTH["rx_bufb_valid"] = 1
WIDTH["rxstatusa"] = 3
WIDTH["rxstatusb"] = 5
WIDTH["tx_bufa"] = 8
WIDTH["tx_bufa_valid"] = 1
WIDTH["tx_bufb"] = 9
WIDTH["tx_bufb_valid"] = 1
WIDTH["txinbit"] = 16
WIDTH["txsr"] = 11
WIDTH["tx_active"] = 1
WIDTH["rxd_filt"] = 1
WIDTH["last_rxd"] = 1
WIDTH["was_bit_noise"] = 1
WIDTH["rx_overrun"] = 1
WIDTH["rxinbit"] = 16
WIDTH["rx_active"] = 1
WIDTH["rxsr"] = 11
WIDTH["rx_noise"] = 1
WIDTH["first"] = 1
WIDTH["rx_bufa"] = 9
WIDTH["rx_bufb"] = 8
WIDTH["rx_bufa_valid"] = 1
WIDTH["rx_bufb_valid"] = 1
WIDTH["rxstatusa"] = 3
WIDTH["rxstatusb"] = 5
WIDTH["tx_bufa"] = 8
WIDTH["tx_bufa_valid"] = 1
WIDTH["tx_bufb"] = 9
WIDTH["tx_bufb_valid"] = 1
WIDTH["txinbit"] = 16
WIDTH["txsr"] = 11
WIDTH["tx_active"] = 1
