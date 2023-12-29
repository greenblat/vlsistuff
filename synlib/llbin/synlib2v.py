#! /usr/bin/python3

import os,sys,pickle
import traceback

def main():
    Fname = sys.argv[1]
    load_db0(Fname)
    Key = 'libraries',1
    scan1(Key)
    for Cell in Cells:
        Cells[Cell].dump()
    Fout=open('fault_cells.v','w')
    print('dumping %d faultable cells ' % len(list(Cells.keys())))
    dones=0
    for Cell in Cells:
        Cells[Cell].fault_dump(Fout)
        dones += 1
    Fout.close()
    print('done %d cells'%dones)
    print('dumping regular cells')
    Fout=open('syn_cells.v','w')
    dones=0
    for Cell in Cells:
        dones += 1
        Cells[Cell].cell_dump(Fout)
    Fout.close()
    print('done %d cells'%dones)
    Fout=open('dual_cells.v','w')
    dones=0
    for Cell in Cells:
        dones += 1
        Cells[Cell].cell_dual_dump(Fout)
    Fout.close()
    print('done %d cells'%dones)

Cells = {}

class cellClass:
    def __init__(self,Name):
        self.Name=Name
        self.pins={}
        self.pairs={}
        self.ff=0
        self.latch=0
        self.statetable=0
   
    def dump(self):
        print('cell %s'%self.Name)
        for Pin in self.pins:
            print('pin: %s %s'% (Pin,self.pins[Pin]))
        print('pairs: %s'%self.pairs)
        print('ff: %s'%str(self.ff))
        print('latch: %s'%str(self.latch))
        print('statetable: %s'%str(self.latch))


    def create_exceptions_and_redundants(self):
        self.Exceptions = []
        if self.ff!=0:
            for (Prm,Var) in self.ff[1]:
                for Chr in '^()!" ':
                    Var = Var.replace(Chr,'')
                if Prm=='clocked_on':
                    self.Exceptions.append(Var)
                if Prm=='clear':
                    self.Exceptions.append(Var)
                if Prm=='preset':
                    self.Exceptions.append(Var)

        if self.latch!=0:
            for (Prm,Var) in self.latch[1]:
                for Chr in '^()!" ':
                    Var = Var.replace(Chr,'')
                if Prm=='enable':
                    self.Exceptions.append(Var)
                if Prm=='clear':
                    self.Exceptions.append(Var)
                if Prm=='preset':
                    self.Exceptions.append(Var)

        if (self.latch==0)and(self.ff==0)and(self.statetable==0):
            Funcs = []
            for Pin in self.pins:
                Dir = self.pins[Pin]['direction']
                if Dir in ['output']:
                    Pdir= self.pins[Pin]
                    if 'function' in Pdir:
                        Func = Pdir['function']
                    elif 'state_function' in Pdir:
                        Func = Pdir['state_function']
                    else:
                        Func = '0' 
                    Func = funcify(Func)
                    Funcs.append(Func)
            if Funcs==[]:
                print('strange error! no func for cell=%s'%self.Name)
            self.Redundants = analyze_faults(self.Name,Funcs)
        else:
            self.Redundants = []

        for (Pin,Val) in self.Redundants:
            Inv = int(invert_func(Val))
            if (Pin,Inv) in self.Redundants:
                self.Exceptions.append(Pin)

#        print('exceptions',self.Name,self.Exceptions,self.Redundants)


    def fault_dump(self,Fout):
        if len(self.pins)==2:
            self.cell_dump(Fout)
            return

        res=[]
        ppp={}
        wires = []

        self.create_exceptions_and_redundants()
        for Pin in self.pins:
            Dir = self.pins[Pin]['direction']
            if Dir in ['input','output']:
                res.append('%s %s'%(Dir,Pin))
                if ('clock' not in self.pins[Pin])and(Pin not in self.Exceptions):
                    ppp[Pin]=Dir
            else:
                wires.append(Pin)
        P1 = ', '.join(res)
        Fout.write('module %s (%s);\n'%(self.Name,P1))
        Fout.write('`ifdef REGISTER\ninitial begin\n')
        for Pin in ppp:
            if (Pin,0) not in self.Redundants:
                Fout.write('   $display("register  %%m.stuck_0_%s %s");\n'%(Pin,ppp[Pin]))
            if (Pin,1) not in self.Redundants:
                Fout.write('   $display("register  %%m.stuck_1_%s %s");\n'%(Pin,ppp[Pin]))
        Fout.write('end\n`endif\n')

        for Pin in ppp:
            if (Pin,0) not in self.Redundants:
                Fout.write('reg stuck_0_%s; initial stuck_0_%s=0;\n'%(Pin,Pin))
            if (Pin,1) not in self.Redundants:
                Fout.write('reg stuck_1_%s; initial stuck_1_%s=0;\n'%(Pin,Pin))
            if ppp[Pin]=='input':
                if (Pin,0) in self.Redundants:
                    Fout.write('wire d_%s = stuck_1_%s ? 1 : %s;\n'%(Pin,Pin,Pin))
                elif (Pin,1) in self.Redundants:
                    Fout.write('wire d_%s = stuck_0_%s ? 0 : %s;\n'%(Pin,Pin,Pin))
                else:
                    Fout.write('wire d_%s = stuck_1_%s ? 1 : stuck_0_%s ? 0 : %s;\n'%(Pin,Pin,Pin,Pin))
            else:
                Fout.write('wire d_%s;\n'%Pin)
                if (Pin,0) in self.Redundants:
                    Fout.write('assign %s = stuck_1_%s ? 1 : d_%s;\n'%(Pin,Pin,Pin))
                elif (Pin,1) in self.Redundants:
                    Fout.write('assign %s = stuck_0_%s ? 0 : d_%s;\n'%(Pin,Pin,Pin))
                else:
                    Fout.write('assign %s = stuck_1_%s ? 1 : stuck_0_%s ? 0 : d_%s;\n'%(Pin,Pin,Pin,Pin))
        if not self.statetable:
            for Wire in wires:
                Fout.write('wire %s;\n'%Wire)
        if self.ff!=0:
            Reg =self.ff[0][0]
            Regn =self.ff[0][1]
            Clocked='0'
            Clear = False
            Preset = False
            Next = Reg
            for (Prm,Var) in self.ff[1]:
                if Prm=='clocked_on':
                    Clocked = Var
                if Prm=='next_state':
                    Next = Var
                if Prm=='clear':
                    Clear = Var
                if Prm=='preset':
                    Preset = Var

            Next = funcify(Next,ppp)
            Clocked = funcify(Clocked)
            Edge = edged(Clocked)
            Fout.write('reg %s;\n'%Reg)
            Fout.write('wire %s = !%s;\n'%(Regn,Reg))
            if (not Clear) and (not Preset):
                Fout.write('always @(%s) %s <= %s;\n'%(Edge,Reg,Next))
            elif (not Preset): 
                Clear = funcify(Clear,ppp)
                Clear1 = edged(Clear)
                Fout.write('always @(%s or %s) if (%s) %s<=0; else %s<= %s;\n'%(Edge,Clear1,Clear,Reg,Reg,Next))
            elif (not Clear): 
                Preset = funcify(Preset,ppp)
                Preset1 = edged(Preset)
                Fout.write('always @(%s or %s) if(%s) %s<=1; else %s<=%s;\n'%(Edge,Preset1,Preset,Reg,Reg,Next))
            else:
                Clear = funcify(Clear,ppp)
                Preset = funcify(Preset,ppp)
                Preset1 = edged(Preset)
                Clear1 = edged(Clear)
                Fout.write('always @(%s or %s or %s) if(%s) %s<=1; else if (%s) %s<=0; else %s <= %s;\n'%(Edge,Clear1,Preset1,Preset,Reg,Clear,Reg,Reg,Next))

        elif self.latch!=0:
            Reg =self.latch[0][0]
            Regn =self.latch[0][1]
            Enable='0'
            Clear = False
            Preset = False
            Next = False
            Enable = False
            for (Prm,Var) in self.latch[1]:
                if Prm=='enable':
                    Enable = Var
                    Enable = funcify(Enable,ppp)
                if Prm=='data_in':
                    Next = Var
                    Next = funcify(Next,ppp)
                if Prm=='clear':
                    Clear = Var
                    Clear = funcify(Clear,ppp)
                if Prm=='preset':
                    Preset = Var
                    Preset = funcify(Preset,ppp)

            Fout.write('reg %s;\n'%Reg)
            Fout.write('wire %s = !%s;\n'%(Regn,Reg))
            if (not Clear) and (not Preset):
                Fout.write('always @* if (%s) %s = %s;\n'%(Enable,Reg,Next))
            elif (not Preset): 
                Fout.write('always @* if (%s) %s<=0; else if (%s) %s<= %s;\n'%(Clear,Reg,Enable,Reg,Next))
            elif (not Clear): 
                Fout.write('always @* if(%s) %s<=1; else if (%s) %s<=%s;\n'%(Preset,Reg,Enable,Reg,Next))
            elif (not Enable): 
                Fout.write('always @* if(%s) %s<=1; else if (%s) %s<=0;\n'%(Preset,Reg,Clear,Reg))
            else:
                Fout.write('always @* if(%s) %s<=1; else if (%s) %s<=0; else if (%s) %s <= %s;\n'%(Preset,Reg,Clear,Reg,Enable,Reg,Next))

        elif self.statetable!=0:
            Stx = self.statetable[0]
            St0 = Stx[0]
            Vars = St0.replace('"','')
            St1 = Stx[1]
            Vars = St0.replace('"','')
            Qs   = St1.replace('"','')
            Vars = Vars.strip()
            Vars = Vars.split()
            Qs = Qs.strip()
            Qs = Qs.split()
            Ta1 = self.statetable[1]
            Ta1 = Ta1[0]
            if Ta1[0]=='table':
                Table = Ta1[1]
                if Table[0]=='"':
                    Table=Table[1:]
                if Table[-1]=='"':
                    Table=Table[:-1]
                Table = Table.replace('\\','')
                Lines = Table.split(',')
                Fout.write('// stateable vars=%s qs=%s\n'%(str(Vars),str(Qs)))
                VV = Vars+Qs
                Fout.write('reg %s;\n'%Qs[0])
                Fout.write('always @*  %s =\n'%(Qs[0]))
                for Line in Lines:
                    Line = Line.strip()
                    Line = Line.replace(':','')
                    LL = Line.split()
                    Expr,New = match_table(VV,LL,self.Name)
                    if New:
                        Fout.write('(%s) ? %s :\n'%(Expr,New))
                Fout.write('   %s;\n'%Qs[0])
            else:
                print('errors!!! stateable')
                Fout.write('// error statetable vars=%s\n'%(str(Vars)))
                Fout.write('%s\n'%str(self.statetable))
        for Pin in ppp:
            if ppp[Pin]=='output':
                Pdir= self.pins[Pin]
                if 'function' in Pdir:
                    Func = Pdir['function']
                elif 'state_function' in Pdir:
                    Func = Pdir['state_function']
                else:
                    Func = '0'

                Func = funcify(Func,ppp)
                Fout.write('assign d_%s = %s;\n'%(Pin,Func))
        Fout.write('endmodule\n')

    def cell_dump(self,Fout):
        res=[]
        ppp={}
        wires = []
        for Pin in self.pins:
            Dir = self.pins[Pin]['direction']
            if Dir in ['input','output']:
                res.append('%s %s'%(Dir,Pin))
                ppp[Pin]=Dir
            else:
                wires.append(Pin)
        P1 = ', '.join(res)
        Fout.write('module %s (%s);\n'%(self.Name,P1))

        if not self.statetable:
            for Wire in wires:
                Fout.write('wire %s;\n'%Wire)
        if self.ff!=0:
            Reg =self.ff[0][0]
            Regn =self.ff[0][1]
            Clear = False
            Preset = False
            Clocked = False
            Edge = 'posedge'
            Next = 'reg'
            for (Prm,Var) in self.ff[1]:
                if Prm=='clocked_on':
                    Clocked = Var
                    Clocked = funcify(Clocked)
                    Edge = edged(Clocked)
                    OrigClk = Var
                if Prm=='next_state':
                    Next = Var
                    Next = funcify(Next)
                if Prm=='clear':
                    Clear = Var
                    Clear = funcify(Clear)
                    Clear1 = edged(Clear)
                if Prm=='preset':
                    Preset = Var
                    Preset = funcify(Preset)
                    Preset1 = edged(Preset)

            Fout.write('reg %s;\n'%Reg)
            Fout.write('wire %s = !%s;\n'%(Regn,Reg))
            if (not Clear) and (not Preset):
                Fout.write('always @(%s) %s <= %s;\n'%(Edge,Reg,Next))
            elif (not Preset): 
                Fout.write('always @(%s or %s) if (%s) %s<=0; else %s<= %s;\n'%(Edge,Clear1,Clear,Reg,Reg,Next))
            elif (not Clear): 
                Fout.write('always @(%s or %s) if(%s) %s<=1; else %s<=%s;\n'%(Edge,Preset1,Preset,Reg,Reg,Next))
            else:
                Fout.write('always @(%s or %s or %s) if(%s) %s<=1; else if (%s) %s<=0; else %s <= %s;\n'%(Edge,Clear1,Preset1,Preset,Reg,Clear,Reg,Reg,Next))
            if 'neg' in Edge: ClkDir = 0
            if 'pos' in Edge: ClkDir = 1
            Fout.write('flop_monitor fm(.q(%s),.clk(%s),.cdir(%s));\n' % (Reg,OrigClk,ClkDir))
        elif self.latch!=0:
            Reg =self.latch[0][0]
            Regn =self.latch[0][1]
            Enable='0'
            Clear = False
            Preset = False
            Enable = False
            Next = False
            for (Prm,Var) in self.latch[1]:
                if Prm=='enable':
                    Enable = Var
                    Enable = funcify(Enable)
                if Prm=='data_in':
                    Next = Var
                    Next = funcify(Next)
                if Prm=='clear':
                    Clear = Var
                    Clear = funcify(Clear)
                if Prm=='preset':
                    Preset = Var
                    Preset = funcify(Preset)

            Fout.write('reg %s;\n'%Reg)
            Fout.write('wire %s = !%s;\n'%(Regn,Reg))
            if (not Clear) and (not Preset):
                Fout.write('always @* if (%s) %s = %s;\n'%(Enable,Reg,Next))
            elif (not Preset): 
                Fout.write('always @* if (%s) %s<=0; else if (%s) %s<= %s;\n'%(Clear,Reg,Enable,Reg,Next))
            elif (not Clear): 
                Fout.write('always @* if(%s) %s<=1; else if (%s) %s<=%s;\n'%(Preset,Reg,Enable,Reg,Next))
            elif (not Enable): 
                Fout.write('always @* if(%s) %s<=1; else if (%s) %s<=0;\n'%(Preset,Reg,Clear,Reg))
            else:
                Fout.write('always @* if(%s) %s<=1; else if (%s) %s<=0; else if (%s) %s <= %s;\n'%(Preset,Reg,Clear,Reg,Enable,Reg,Next))

        elif self.statetable!=0:
            Stx = self.statetable[0]
            St0 = Stx[0]
            Vars = St0.replace('"','')
            St1 = Stx[1]
            Vars = St0.replace('"','')
            Qs   = St1.replace('"','')
            Vars = Vars.strip()
            Vars = Vars.split()
            Qs = Qs.strip()
            Qs = Qs.split()
            Ta1 = self.statetable[1]
            Ta1 = Ta1[0]
            if Ta1[0]=='table':
                Table = Ta1[1]
                if Table[0]=='"':
                    Table=Table[1:]
                if Table[-1]=='"':
                    Table=Table[:-1]
                Table = Table.replace('\\','')
                Lines = Table.split(',')
                Fout.write('// stateable vars=%s qs=%s\n'%(str(Vars),str(Qs)))
                VV = Vars+Qs
                Fout.write('reg %s;\n'%Qs[0])
                Fout.write('always @*  %s =\n'%(Qs[0]))
                for Line in Lines:
                    Line = Line.strip()
                    Line = Line.replace(':','')
                    LL = Line.split()
                    Expr,New = match_table(VV,LL,self.Name)
                    if New:
                        Fout.write('(%s) ? %s :\n'%(Expr,New))
                Fout.write('   %s;\n'%Qs[0])
            else:
                print('errors!!! stateable')
                Fout.write('// error statetable vars=%s\n'%(str(Vars)))
                Fout.write('// %s\n'%str(self.statetable))
        for Pin in ppp:
            if ppp[Pin]=='output':
                Pdir= self.pins[Pin]
                if 'function' in Pdir:
                    Func = Pdir['function']
                elif 'state_function' in Pdir:
                    Func = Pdir['state_function']
                else:
                    Func = '0'

                Func = funcify(Func)
                Fout.write('assign %s = %s;\n'%(Pin,Func))
        Fout.write('endmodule\n')


    def cell_dual_dump(self,Fout):
        res=[]
        ppp={}
        wires = []
        for Pin in self.pins:
            Dir = self.pins[Pin]['direction']
            if Dir in ['input','output']:
                res.append('%s n_%s'%(Dir,Pin))
                res.append('%s p_%s'%(Dir,Pin))
                ppp[Pin]=Dir
            else:
                wires.append(Pin)
        P1 = ', '.join(res)
        Fout.write('module %s (%s);\n'%(self.Name,P1))

        if not self.statetable:
            for Wire in wires:
                Fout.write('wire n_%s;\n'%Wire)
                Fout.write('wire p_%s;\n'%Wire)
        if self.ff!=0:
            Reg =self.ff[0][0]
            Regn =self.ff[0][1]
            Clear = False
            Preset = False
            Clocked = False
            Edge = 'posedge'
            Next = Reg
            for (Prm,Var) in self.ff[1]:
                if Prm=='clocked_on':
                    Clocked = Var
                    Clocked = funcify(Clocked)
                    Edge = edged(Clocked)
                if Prm=='next_state':
                    Next = Var
                    Next = funcify(Next)
                if Prm=='clear':
                    Clear = Var
                    Clear = funcify(Clear)
                    Clear1 = edged(Clear)
                if Prm=='preset':
                    Preset = Var
                    Preset = funcify(Preset)
                    Preset1 = edged(Preset)

            Fout.write('reg %s;\n'%Reg)
            Fout.write('wire %s = !%s;\n'%(Regn,Reg))
            if (not Clear) and (not Preset):
                Fout.write('always @(%s) %s <= %s;\n'%(Edge,Reg,Next))
            elif (not Preset): 
                Fout.write('always @(%s or %s) if (%s) %s<=0; else %s<= %s;\n'%(Edge,Clear1,Clear,Reg,Reg,Next))
            elif (not Clear): 
                Fout.write('always @(%s or %s) if(%s) %s<=1; else %s<=%s;\n'%(Edge,Preset1,Preset,Reg,Reg,Next))
            else:
                Fout.write('always @(%s or %s or %s) if(%s) %s<=1; else if (%s) %s<=0; else %s <= %s;\n'%(Edge,Clear1,Preset1,Preset,Reg,Clear,Reg,Reg,Next))

        elif self.latch!=0:
            Reg =self.latch[0][0]
            Regn =self.latch[0][1]
            Enable='0'
            Clear = False
            Preset = False
            Enable = False
            Next = False
            for (Prm,Var) in self.latch[1]:
                if Prm=='enable':
                    Enable = Var
                    Enable = funcify(Enable)
                if Prm=='data_in':
                    Next = Var
                    Next = funcify(Next)
                if Prm=='clear':
                    Clear = Var
                    Clear = funcify(Clear)
                if Prm=='preset':
                    Preset = Var
                    Preset = funcify(Preset)

            Fout.write('reg %s;\n'%Reg)
            Fout.write('wire %s = !%s;\n'%(Regn,Reg))
            if (not Clear) and (not Preset):
                Fout.write('always @* if (%s) %s = %s;\n'%(Enable,Reg,Next))
            elif (not Preset): 
                Fout.write('always @* if (%s) %s<=0; else if (%s) %s<= %s;\n'%(Clear,Reg,Enable,Reg,Next))
            elif (not Clear): 
                Fout.write('always @* if(%s) %s<=1; else if (%s) %s<=%s;\n'%(Preset,Reg,Enable,Reg,Next))
            elif (not Enable): 
                Fout.write('always @* if(%s) %s<=1; else if (%s) %s<=0;\n'%(Preset,Reg,Clear,Reg))
            else:
                Fout.write('always @* if(%s) %s<=1; else if (%s) %s<=0; else if (%s) %s <= %s;\n'%(Preset,Reg,Clear,Reg,Enable,Reg,Next))

        elif self.statetable!=0:
            Stx = self.statetable[0]
            St0 = Stx[0]
            Vars = St0.replace('"','')
            St1 = Stx[1]
            Vars = St0.replace('"','')
            Qs   = St1.replace('"','')
            Vars = Vars.strip()
            Vars = Vars.split()
            Qs = Qs.strip()
            Qs = Qs.split()
            Ta1 = self.statetable[1]
            Ta1 = Ta1[0]
            if Ta1[0]=='table':
                Table = Ta1[1]
                if Table[0]=='"':
                    Table=Table[1:]
                if Table[-1]=='"':
                    Table=Table[:-1]
                Table = Table.replace('\\','')
                Lines = Table.split(',')
                Fout.write('// stateable vars=%s qs=%s\n'%(str(Vars),str(Qs)))
                VV = Vars+Qs
                Fout.write('reg %s;\n'%Qs[0])
                Fout.write('always @*  %s =\n'%(Qs[0]))
                for Line in Lines:
                    Line = Line.strip()
                    Line = Line.replace(':','')
                    LL = Line.split()
                    Expr,New = match_table(VV,LL,self.Name)
                    if New:
                        Fout.write('(%s) ? %s :\n'%(Expr,New))
                Fout.write('   %s;\n'%Qs[0])
            else:
                print('errors!!! stateable')
                Fout.write('// error statetable vars=%s\n'%(str(Vars)))
                Fout.write('// %s\n'%str(self.statetable))
        for Pin in ppp:
            if ppp[Pin]=='output':
                Pdir= self.pins[Pin]
                if 'function' in Pdir:
                    Func = Pdir['function']
                elif 'state_function' in Pdir:
                    Func = Pdir['state_function']
                else:
                    Func = '0'

                Func = funcify(Func)
                Func2 = splitify(Func.split())
                Func3 = refactorFunc(Func2)
                posify_negify(Func3,Fout,'p_'+Pin,'n_'+Pin,0)
        Fout.write('endmodule\n')

def refactorFunc(Func):
    if type(Func) is str:
        return Func
    if len(Func) == 1:
        return refactorFunc(Func[0])
    if len(Func) == 2:
        if Func[0] == '!':
            F1 = refactorFunc(Func[1])
            return [Func[0],F1]
        else:
            print('error(2) posify_negify %s'%str(Func))

    if '!' in Func:
        Ind = Func.index('!')
        Func1 = Func[:Ind] + [['!',Func[Ind+1]]]+Func[Ind+2:]
        return refactorFunc(Func1)


    if len(Func) == 3:
        F0 = refactorFunc(Func[0])
        F2 = refactorFunc(Func[2])
        return [F0,Func[1],F2]
    if len(Func) == 4:
        F0 = refactorFunc(Func[0])
        F3 = refactorFunc(Func[3])
        return [F0,Func[1],[Func[2],F3]]
    if len(Func) == 5:
        F0 = refactorFunc(Func[0])
        F2 = refactorFunc(Func[2])
        F4 = refactorFunc(Func[4])
        return [F0,Func[1],[F2,Func[3],F4]]
    if (len(Func) &1) == 1:
        Func1 = Func[:]
        F0 = refactorFunc(Func1[0])
        F2 = refactorFunc(Func1[2])
        X = [[F0,Func1[1],F2]] + Func1[3:]
        return refactorFunc(X)


    print('error(6) refacrorFunc posify_negify %s'%str(Func))
    return 'ERROR','ERROR'
            


posnegid=0
def posify_negify(Func,Fout,pPin,nPin,Depth):
    global posnegid
    if type(Func) is str:
        if (Depth==0):
            Fout.write('assign %s = %s;\n'%(pPin,'p_'+Func))
            Fout.write('assign %s = %s;\n'%(nPin,'n_'+Func))
            return
        else:
            return 'p_'+Func,'n_'+Func
    if Func[0]=='!':
        P,N = posify_negify(Func[1],Fout,pPin,nPin,Depth+1)
        if Depth==0:
            Fout.write('assign %s = %s;\n'%(pPin,N))
            Fout.write('assign %s = %s;\n'%(nPin,P))
            return
        return N,P
    
    if len(Func)==3:
        N0,P0 = posify_negify(Func[0],Fout,pPin,nPin,Depth+1)
        N1,P1 = posify_negify(Func[2],Fout,pPin,nPin,Depth+1)
        return mergePosNeg(Depth,Func[1],N0,P0,N1,P1,pPin,nPin,Fout)


    print('error! posify_negify %s'%str(Func))
    return 'ERROR','ERROR'

def mergePosNeg(Depth,Func,N0,P0,N1,P1,pPin,nPin,Fout):
    global posnegid
    if Depth!=0:
        PP = 'wire p_wire%d'%posnegid
        NN = 'wire n_wire%d'%posnegid
        PPx = 'p_wire%d'%posnegid
        NNx = 'n_wire%d'%posnegid
        posnegid+=1
    else:
        PP = 'assign %s'%pPin
        NN = 'assign %s'%nPin
        PPx = 'p_wire%d'%posnegid
        NNx = 'n_wire%d'%posnegid
    if Func=='&&':
        Fout.write('%s = %s && %s;\n'%(PP,P0,P1))
        Fout.write('%s = %s || %s;\n'%(NN,N0,N1))
        return PPx,NNx

    if Func=='||':
        Fout.write('%s = %s || %s;\n'%(PP,P0,P1))
        Fout.write('%s = %s && %s;\n'%(NN,N0,N1))
        return PPx,NNx

    if Func=='^':
        Fout.write('%s = (%s&&%s)||(%s&&%s);\n'%(PP,P0,N1,P1,N0))
        Fout.write('%s = (%s&&%s)||(%s&&%s);\n'%(NN,P0,N0,P1,N1))
        return PPx,NNx


def splitify(List):
    while ')' in List:
        ind0 = List.index(')')
        ind1=ind0-1
        while List[ind1]!='(':
            ind1 -= 1
        if (ind1==0)and(ind0==(len(List)-1)):
            return List[1:-1]
        Sub = List[ind1+1:ind0]
        Bef = List[:ind1]
        Aft = List[ind0+1:]
        List = Bef+[Sub]+Aft
    return List



def match_table(VV,LL,Cell):
    res = []
    ind=0
    ptr=0
    while ind<len(VV):
        Var = VV[ind]
        Sym = LL[ind]
        if Sym=='H':
            res.append(Var)
        elif Sym=='L':
            res.append('!%s'%Var)
        elif Sym=='-':
            pass
        elif Sym=='N':
            pass
        else:
            print('error!! cell=%s match table vv=%s ll=%s ind=%s sym=%s'%(Cell,VV,LL,ind,Sym))

        ind+=1
    X = '&&'.join(res)    
    if LL[-1]=='H':
        Y = '1'
    elif LL[-1]=='L':
        Y = '0'
    elif LL[-1]=='N':
        Y = VV[-1]
        Y = False
    elif LL[-1]=='-':
        Y = VV[-1]
        Y = False
        Y = False
    elif LL[-1]=='X':
        Y="1'bx"
    else:
        print('ERROR cell=%s LL=%s last one is not in set. vv=%s'%(Cell,LL,VV))
        Y = "1'bx"
    return X,Y


def edged(Func):
    for Char in '()':
        Func = Func.replace(Char,'')
    wrds = Func.split()
    if len(wrds)==1:
        return 'posedge %s'%wrds[0]
    if wrds[0]=='!':
        return 'negedge %s'%wrds[1]
    return "error_edged(%s)"%Func

def funcify(Func,Trans={}):
    Func1= Func.replace('"','')
    for Char in '^()+*!&|':
        Func1 = Func1.replace(Char,' %s '%Char)
    Func2 = Func1.strip()
    wrds = Func2.split()
    res = []
    for wrd in wrds:
        if wrd[-1]=="'":
            res.append('!')
            res.append(wrd[:-1])
        else:
            res.append(wrd)
    wrds = res[:]



#    if (wrds[0]=='(')and(wrds[-1]==')'):
#        wrds = wrds[1:-1]
    guard = 100
    while ')' in wrds:
        guard -= 1
        if (guard<=0):
            print('ilia too much guard wrds=%s'%(str(wrds)))
            sys.exit()
        ind1 = wrds.index(')')
        ind0 = ind1-1
        while wrds[ind0]!='(':
            ind0 -= 1
        part = wrds[ind0+1:ind1]
        part = overwork(part)
        bef = wrds[:ind0]
        aft = wrds[ind1+1:]
        wrds = bef + [part] + aft
    wrds = overwork(wrds)
    wrds = flat_list(wrds)
    res=[]
    for wrd in wrds:
        if wrd in Trans:
            res.append('d_%s'%wrd)
        else:
            res.append(wrd)
            
    Str = ' '.join(res)
    return Str

def flat_list(wrds):
    ind = 0
    res = []
    while wrds!=[]:
        pp = wrds.pop(0)
        if type(pp) is list:
            wrds = ['(']+pp+[')']+wrds
        else:
            res.append(pp)
    return res


def overwork(part):
    ind=1
    while ind<len(part):
        Var = part[ind]
        if Var == '+':
            part[ind]='||'
        elif Var == '&':
            part[ind]='&&'
        elif Var == '|':
            part[ind]='||'
        elif Var == '*':
            part[ind]='&&'
            
        if (ind>0) and (is_var(Var) or (Var=='!')):
            Prev = part[ind-1]
            if not is_oper(Prev):
                part = part[:ind]+['&&']+part[ind:]
        ind +=1        
    return part
            
        
Letters = 'qwertyuiopasdfghjklzxcvbnm'
Letters += 'QWERTYUIOPASDFGHJKLZXCVBNM'
Opers = '+*||&&^!'    

def  is_var(Var):
    if (type(Var) is str)and(Var[0] in Letters):
        return True
    if (type(Var) is list):
        return True
    return False
        
def is_oper(Var):
    if (type(Var) is str)and(Var[0] in Opers):
        return True
    return False



def load_db0(Fname):
    global DataBase
    File = open(Fname,'rb')
    print('open %s pickle' % Fname)
    DataBase = pickle.load(File) 

def dump_dump():
    Fout = open('ttt.ttt','w')
    File.close()
    for Key in DataBase:
        Fout.write('key %s = %s\n'%(Key,DataBase[Key]))
    Fout.close()

def scan1(Key):
    List = DataBase[Key]
    if List==[]:
        return
    if (len(List)==7)and(List[5] in DataBase):
        work_on_lib(DataBase[List[5]])
    return
    for Item in List:
        if Item[0][0]=='library':
            go_in_lib(Item)
        else:
            print('// error',Key,List)

def go_in_lib(Key):
    List = DataBase[Key]
    if (len(List)==7)and(List[0][0]=='library'):
        work_on_lib(DataBase[List[5]])
    else:
        print('// error',Key,List)
    
def work_on_lib(List):
    for Key in DataBase:
        if Key[0] == 'Cell':
            add_cell(DataBase[Key])

def was_work_on_lib(List):
    for Item in List:
        if Item[0]=='Items':
            work_on_lib(DataBase[Item])
        else:
            work_on_lib_item(DataBase[Item])

def work_on_lib_item(List):
    if len(List)==1:
        Item = List[0]
        if Item[0]=='Pair':
            add_lib_pair(DataBase[Item])
        elif Item[0]=='Cell':
            add_cell(DataBase[Item])

def add_lib_pair(List):
    return
def add_cell(List):
    Cell = getToken(List[2])

    Items = DataBase[List[5]]
    Obj = cellClass(Cell)
    Cells[Cell]=Obj
    work_cell_items(Cell,Items)

def work_cell_items(Cell,Items):
    for Item in Items:
        if Item[0]=='cell_items':
            work_cell_items(Cell,DataBase[Item])
        elif (len(Item) == 4):
            pass
        else:
            List = DataBase[Item]
            if Item[0] == 'Ff':
                add_cell_ff(Cell,List)
            elif Item[0] == 'Statetable':
                add_cell_statetable(Cell,List)
            elif (len(List)==4)and(List[0][1] == 'token'):
                if List[0][0] == 'area':
                    Area = get_expr(List[2])
                    Cells[Cell].pairs['area']=Area
                elif List[0][0] in ['cell_footprint','cell_leakage_power','driver_waveform_fall','driver_waveform_rise','clock_gating_integrated_cell','user_function_class']:
                    pass
                else:
                    print('error(0) %s work_cell_items %s'%(Cell,List[0]))
            elif (len(List)==7) and (List[0][0] == 'pin'):
                add_cell_pin(Cell,List)
            elif (len(List)==7) and (List[0][0] == 'latch'):
                add_cell_latch(Cell,List)
            elif len(List)==1:
                if List[0][0]=='Pair':
                    add_cell_pair(Cell,DataBase[List[0]])
                elif List[0][0]=='Pin':
                    add_cell_pin(Cell,DataBase[List[0]])
                elif List[0][0]=='Ff':
                    add_cell_ff(Cell,DataBase[List[0]])
                elif List[0][0]=='Latch':
                    add_cell_latch(Cell,DataBase[List[0]])
                elif List[0][0]=='Statetable':
                    add_cell_statetable(Cell,DataBase[List[0]])
                else:
                    print('error(2) %s work_cell_items %s'%(Cell,List[0]))
            else:
                print('error(3) %s work_cell_items %s %s %s'%(Cell,Item,List[0],len(List)))

def add_cell_statetable(Cell,List):
    Toks = get_toks(List[2])
    Pairs = get_pairs(List[5])
    Cells[Cell].statetable=(Toks,Pairs)
def add_cell_ff(Cell,List):
    Toks = get_toks(List[2])
    Pairs = get_pairs(List[5])
    Cells[Cell].ff=(Toks,Pairs)

def add_cell_latch(Cell,List):
    Toks = get_toks(List[2])
    Pairs = get_pairs(List[5])
    Cells[Cell].latch=(Toks,Pairs)


def get_toks(Key):
    List = DataBase[Key]
    Res = []
    if List[0][0]=='toks':
        Part0 = get_toks(List[0])
        Tok = get_expr(List[2])
        return Part0+[Tok]
    elif len(List)==3:
        Tok0 = get_expr(List[0])
        Tok1 = get_expr(List[2])
        return [Tok0,Tok1]
    else:
        Tok = get_expr(List[0])
        return [Tok]
    print('error get tokes %s'%str(List))
    return []

def get_pairs(Key):
    List = DataBase[Key]
    if len(List)==2:
        if List[0][0]=='Pairs':
            P1 = get_pairs(List[0])
            if List[1][0]=='Pair':
                List2 = DataBase[List[1]]
                Param = List2[0][0]
                Val = get_expr(List2[2])
                return P1+[(Param,Val)]
    elif len(List)==1:
        List2 = DataBase[List[0]]
        Param = List2[0][0]
        Val = get_expr(List2[2])
        return [(Param,Val)]

    if List[0][0] == 'Pair':
        Res = []
        for Item in List:
            PP = DataBase[Item]
            Param = getToken(PP[0])
            Val = get_expr(PP[2])
            Res.append((Param,Val))
        return Res

    if (len(List)==4)and(List[0][0] == 'table'):
        return [('table',List[2][0])]

    print('error GetPairs ',len(List),List[0][0],List)
    return 0


def add_cell_pair(Cell,List):
    print('ADD_CELL_PAIR',List)
    if len(List)==4:
        First = getToken(List[0][0])
        Second = get_expr(List[2])
        Cells[Cell].pairs[First]=Second
    elif len(List)==7:
        First = getToken(List[0][0])
        Second = get_expr(List[2])
        Pairs = get_pairs(List[5])
        Cells[Cell].pairs[First]=(Second,Pairs)
    elif len(List)==6:
        First = getToken(List[0][0])
        Pairs = get_pairs(List[4])
        Cells[Cell].pairs[First]=Pairs
    else:
        print('error! add_cell_pair %s %d %s'%(Cell,len(List),List))





def get_expr(Item):
    if type(Item) is tuple:
        if Item[1]=='floating':
            return float(Item[0])
        if Item[1]=='string':
            return Item[0].replace('"','')
        if Item[1]=='token':
            return Item[0]
        if Item[1]=='number':
            return int(Item[0])
        if len(Item)!=2:
            print('error expr "%s"'%str(Item))
            traceback.print_stack()
            return 0
        
    if (type(Item) is list)and(len(Item)==1):
        return get_expr(Item[0])
   
    List = DataBase[Item]
    if len(List)==1:
        return get_expr(List[0])
    print('error expr',List)
    return 0


def getToken(Pin):
    if type(Pin) is str:
        return Pin.replace('"','')
    if type(Pin) is list:
        if len(Pin) == 1:
            return getToken(Pin[0])
    if Pin in DataBase:
        return getToken(DataBase[Pin])
    if (type(Pin) is tuple)and(len(Pin)==4):
        return Pin[0].replace('"','')
    print('ERROR getToken got %s' % str(Pin))
    return Pin


def add_cell_pin(Cell,List):
    if len(List)==7:
        Pin = getToken(List[2])
        Items = DataBase[List[5]]
        Cells[Cell].pins[Pin]={}
        work_on_pin_items(Cell,Pin,Items)
    else:
        print('error add_cell_pin %s'%List)

def work_on_pin_items(Cell,Pin,Items):
#    print('work_on_pin_items %s %s %s' % (Cell,Pin,Items))
    if (len(Items[0])== 4):
        if Items[0][0] == 'direction':
            Dir = getToken(Items[2])
            add_cell_pin_pair(Cell,Pin,'direction',Dir)
            print('direction',Dir)
        elif Items[0][0] == 'function':
            Val = get_expr(Items[2])
            add_cell_pin_pair(Cell,Pin,'function',Val)
        elif Items[0][0] == 'capacitance':
            Val = get_expr(Items[2])
            add_cell_pin_pair(Cell,Pin,'capacitance',Val)
        elif Items[0][0] == 'clock':
            Val = get_expr(Items[2])
            add_cell_pin_pair(Cell,Pin,'clock',Val)
        elif Items[0][0] == 'state_function':
            Val = get_expr(Items[2])
            add_cell_pin_pair(Cell,Pin,'state_function',Val)
        elif Items[0][0] in ['related_bias_pin','driver_waveform_rise','driver_waveform_fall','receiver_capacitance','fall_capacitance','max_transition','related_ground_pin','max_capacitance','power_down_function','related_power_pin','timing','rise_capacitance','min_capacitance','clock_gate_clock_pin','clock_gate_enable_pin','internal_node','clock_gate_out_pin','clock_gate_test_pin']:
            pass
        elif Items[0][0] == 'nextstate_type':
            pass
        else:
            print('ERROR work_on_pin_items %s %s %s' % (Cell,Pin,Items))
        return

    for Item in Items:
        if Item[0]=='pin_items':
            work_on_pin_items(Cell,Pin,DataBase[Item])
        else:
            List = DataBase[Item]
            if len(List)==1:
                List = DataBase[List[0]]
                if len(List)==4:
                    Par = getToken(List[0])
                    Val = get_expr(List[2])
                    add_cell_pin_pair(Cell,Pin,Par,Val)
                else:
                    print('error2 work_on_pin_items %s'%List)
            elif len(List)==4:
                work_on_pin_items(Cell,Pin,List)
            elif len(List)==6:
                work_on_pin_items(Cell,Pin,List)
            else:
                print('error3 work_on_pin_items  len=%d %s'%(len(List),List))
                
def add_cell_pin_pair(Cell,Pin,Par,Val):
    Cells[Cell].pins[Pin][Par]=Val

def analyze_faults(Cell,Funcs):
    if (len(Funcs)>1)or(Funcs==[]):
        return []
    Redundants=[]
    Vars={}
    Func = Funcs[0]
    Var1 = extract_vars(Func)
    for V in Var1:
        Vars[V]='x'
    for Var in Vars:
        Vars[Var]='0'
        Res = evaluate_func(Cell,Func,Vars)
        if Res in ['0','1']:
            Redundants.append((Var,0))
        Vars[Var]='1'
        Res = evaluate_func(Cell,Func,Vars)
        if Res in ['0','1']:
            Redundants.append((Var,1))
        Vars[Var]='x'
    return Redundants

def extract_vars(Func):
    wrds = Func.split()
    Vars=[]
    for wrd in wrds:
        if (wrd not in ['*','(',')','&&','^','||','!'])and(wrd not in Vars):
            Vars.append(wrd)
    Vars.sort()
    return Vars
        
def evaluate_func(Cell,Func,Vars):
    Func1 = ' '+Func+' '
    for Var in Vars:
        Val = Vars[Var]
        Func1 = Func1.replace(' %s '%Var,' %s '%Val)
    Oper = deep_oper(Func1,False)
    Res = compute_func(Cell,Oper)
    return Res


def compute_func(Cell,Lfunc):
    if type(Lfunc) is str:
        if Lfunc[0] not in '01x':
            print('error! strange compute_func got %s for cell=%s'%(str(Lfunc),Cell))
            return 'x'
        return Lfunc
    if len(Lfunc)==1:
        return compute_func(Cell,Lfunc[0])
    Lf = Lfunc[:]
    while '!' in Lf:
        Ind = Lf.index('!')
        Res = compute_func(Cell,Lf[Ind+1])
        Res = invert_func(Res)
        Lf = Lf[:Ind]+[Res]+Lf[Ind+2:]
    for Mul in ['&&','*']:
        while Mul in Lf:
            Ind = Lf.index(Mul)
            Res0 = compute_func(Cell,Lf[Ind-1])
            Res1 = compute_func(Cell,Lf[Ind+1])
            if (Res0=='0')or(Res1=='0'):
                Val='0'
            elif (Res0=='x')or(Res1=='x'):
                Val='x'
            else:
                Val='1'
            Lf = Lf[:Ind-1]+[Val]+Lf[Ind+2:]


    while '^' in Lf:
        Ind = Lf.index('^')
        Res0 = compute_func(Cell,Lf[Ind-1])
        Res1 = compute_func(Cell,Lf[Ind+1])
        if (Res0=='x')or(Res1=='x'):
            Val='x'
        elif (Res0==Res1):
            Val='0'
        else:
            Val='1'
        Lf = Lf[:Ind-1]+[Val]+Lf[Ind+2:]


    while '||' in Lf:
        Ind = Lf.index('||')
        Res0 = compute_func(Cell,Lf[Ind-1])
        Res1 = compute_func(Cell,Lf[Ind+1])
        if (Res0=='1')or(Res1=='1'):
            Val='1'
        if (Res0=='x')or(Res1=='x'):
            Val='x'
        else:
            Val='0'
        Lf = Lf[:Ind-1]+[Val]+Lf[Ind+2:]

    if len(Lf)>1:
        print('ilia error! lf=%s lfunc=%s'%(Lf,Lfunc))
        return 'x'
    return Lf[0]




def invert_func(Func):
    if Func=='0':
        return '1'
    elif Func=='1':
        return '0'
    elif Func==0:
        return '1'
    elif Func==1:
        return '0'
    else:
        return 'x'

def deep_oper(Func,Over=True):
    wrds = Func.split()
    guard = 100
    while ')' in wrds:
        guard -= 1
        if (guard<=0):
            print('ilia too much guard wrds=%s'%(str(wrds)))
            sys.exit()
        ind1 = wrds.index(')')
        ind0 = ind1-1
        while wrds[ind0]!='(':
            ind0 -= 1
        part = wrds[ind0+1:ind1]
        if (Over):
            part = overwork(part)
        bef = wrds[:ind0]
        aft = wrds[ind1+1:]
        wrds = bef + [part] + aft
    return wrds


main()

