#! /usr/bin/env python3
import os,sys,string

import traceback

sys.path.append('pys')
import importlib
sys.path.append('/Users/iliagreenblat/verpy/')
sys.path.append('/home/ilia/vlsistuff/verpy/pybin3')
import logs
from skywaterLib import cellLib

class  accessClass:
    def __init__(self,Dir):
        self.Modules = {}
        self.Dir = Dir
        self.bringAll(Dir)
        self.Top = None
        self.Path = []
        self.CommandsHistory = []
        logs.log_info('%d modules loaded' % len(self.Modules.keys()))
        self.chooseTop()
        
    def chooseTop(self):
        Alls = list(self.Modules.keys())
        MISSING = []
        for Cell in self.Modules:
            Mod = self.Modules[Cell]
            Children = list(Mod.types1.keys()) 
            if Children == []:
                if Cell in Alls: 
                    Ind = Alls.index(Cell)
                    Alls.pop(Ind)
                
            for Child in Children:
                if Child in Alls: 
                    Ind = Alls.index(Child)
                    Alls.pop(Ind)
                if Child not in self.Modules:
                    MISSING.append(Child)
        logs.log_info('TOPS: %s' % ' '.join(Alls))
        logs.log_info('MISSING: %s' % ' '.join(MISSING))
        self.Top = Alls[0]
        


    def bringAll(self,Dir):
        List = os.listdir(Dir)
        for Fname in List:
            if Fname.endswith('.py'):
                Cell = Fname[:-3]
                Mod = importlib.import_module(Cell)
                Class = getattr(Mod, '%sClass' % Cell)
                self.Modules[Cell] = Class()

    def listLoaded(self):
        List =  list(self.Modules.keys())
        return List
            
    def highlites(self,Cell):                
        Mod = Env.Modules[Cell]
        Dirs = len(Mod.netdirs.keys())
        Wids = len(Mod.netwids.keys())
        Types0 = len(Mod.types0.keys())
        Types1 = len(Mod.types1.keys())
        LibTypes0 = len(Mod.libtypes0.keys())
        LibTypes1 = len(Mod.libtypes1.keys())
        Insts = len(Mod.conns.keys())
        Wires = len(Mod.wires.keys())
        logs.log_info("highlites: %-30s    nets=%d wires= %d  child=%d libt=(%d %d)  insts= %d" % (Cell,Wids,Wires,Types1,LibTypes0,LibTypes1,Insts))
            
    def description(self,Cell):
        Mod = Env.Modules[Cell]
        Outs,Ins,Wires,Flops = 0,0,0,0
        for Net in Mod.netdirs:
            Dir = Mod.netdirs[Net]
            if Dir == 'output': Outs += 1
            elif Dir == 'input': Ins += 1
            elif Dir == 'wire': Wires += 1
            else: logs.log_error('DESC DIR is %s' % Dir)

        for Type in Mod.libtypes1:
            Many = len(Mod.libtypes1[Type])
            if isFlipFlop(Type):
                Flops += Many

        Types0 = len(Mod.types0.keys())
        Types1 = len(Mod.types1.keys())
        LibTypes0 = len(Mod.libtypes0.keys())
        LibTypes1 = len(Mod.libtypes1.keys())
        Res = (Outs,Ins,Wires,Flops,Types0,Types1,LibTypes0,LibTypes1)
        return Res

    def nicelist(self):
        for Cell in Env.Modules:
            self.highlites(Cell)

    def generatePng(self,Cell):
        Hier = {}
        self.buildHier(Cell,Hier)
        Fout = open('%s.dot' % Cell,'w')
        Fout.write('digraph %s {\n' % Cell)
        for MM in Hier:
            LL = Hier[MM]
            for Item in LL:
                Fout.write('    %s -> %s ;\n' % (MM,Item[0]))

        Fout.write('}\n')
        Fout.close()
        os.system('dot %s.dot -Tpng > %s.png ; open %s.png' % (Cell,Cell,Cell))

    def hierPaths(self,Cell):
        Paths = []
        Mod = self.Modules[Cell]
        self.buildHierPath(Mod,[(Cell,Cell)],Paths)
        Lines = []
        Ind = 0
        print("PATHS",len(Paths))
        for Path in Paths:
            Res = []
            for Inst,_ in Path:
                Res.append(Inst)
            Str = '.'.join(Res)
            Last = Path[-1][1]
            Line = '%d,%d,%s,%s' % (Ind,len(Res),Str,Last)
            Ind += 1
            Lines.append(Line)
        Fout = open('%s.paths.csv' % Cell,'w')
        Fout.write('%s,depth,path,type\n' % (Cell))
        for Line in Lines:
            Fout.write('%s\n' % Line)
        Fout.close()

    def buildHierPath(self,Mod,Sofar,Paths):
        for Inst in Mod.types0:
            Type = Mod.types0[Inst]
#            Sofar.append((Inst,Type))
            if Type in self.Modules:
                Down = self.Modules[Type]
#                print(">",' '*len(Sofar)*4,Type,Inst,len(Sofar))
                Paths.append(Sofar+[(Inst,Type)])
                self.buildHierPath(Down,Sofar+[(Inst,Type)],Paths)
                        




    def hierSizes(self):
        self.Sizes = {}
        self.selfSizes = {}
        dones = 1
        while dones>0:
            print("round",dones)
            dones = 0
            for Cell in self.Modules:
                if Cell not in self.Sizes:
                    Mod = self.Modules[Cell]
                    self.selfSizes[Cell] = len(list(Mod.libtypes0.keys()))
                    if len(list(Mod.types1.keys())) == 0:
                        self.Sizes[Cell] = len(list(Mod.libtypes0.keys()))
                        dones += 1
                    else:
                        Ok = True
                        Tot = self.selfSizes[Cell]
                        for Type in Mod.types1:
                            if Type in self.Sizes:
                                Len = len(Mod.types1[Type])
                                Here = Len * self.Sizes[Type]
                                Tot += Here
                            elif Type in self.Modules:
                                Ok = False
                        if Ok:
                            self.Sizes[Cell]  = Tot
                            dones += 1
                        else:
                            print("not yet",Cell)
                        





    def buildHier(self,Cell,Sofar):
         if Cell in Sofar: return
         if Cell not in Env.Modules: return
         Mod = Env.Modules[Cell]
         for TT in Mod.types1:
            if TT not in Sofar:
                self.buildHier(TT,Sofar)
         Sofar[Cell] = []
         for TT in Mod.types1:
            Len = len(Mod.types1[TT])
            Sofar[Cell].append((TT,Len))

    def buildNetTable(self,Cell):
        if type(Cell) is str:
            Mod = Env.Modules[Cell]
        else:
            Mod = Cell
        if hasattr(Mod, 'netTable'): return
        Mod.netTable = {}
        for Inst in Mod.conns:
            Conns = Mod.conns[Inst]
            for Pin in Conns:
                Sig = Conns[Pin]
                if Sig not in Mod.netTable: Mod.netTable[Sig] = []
                Mod.netTable[Sig].append((Inst,Pin))
                    
    def goto(self,Path):
        Path = Path.split('.')
        if Path[0] not in self.Modules:
            logs.log_error('cannot goto to %s' % str(Path))
            return
        self.Top = Path[0]
        Path.pop(0)
        Current = self.Modules[self.Top]
        New = [(self.Top,self.Top)]
        print(">>GOTO",New,Path)
        while Path != []:
            Inst = Path.pop(0)
            print(">>Inst",Inst,New,Path)
            if Inst not in Current.types0:
                logs.log_error('cannot goto to %s from %s' % (Inst,Current.Name))
                return
                
            Type = Current.types0[Inst]
            New.append((Inst,Type))
            Current = self.Modules[Type]

        self.Path = New


            
    def travelBack(self):
        if self.Path == []: 
            logs.log_error('run goto command first to point me to the right module')
            return
        Module = self.Path[-1][1]
        Mod = self.Modules[Module]
        Regs =  self.endPoints(Module)
        Results = {}
        for ind,Reg in enumerate(Regs):
            Distances = {}
            print("START q=%s d=%s" % (Reg[0],Reg[1]))
            self.travelsBack(Mod,Reg[0],Reg[1],self.Path[:],[(Module,Reg)],Distances)
            Results[Reg] = Distances
        
        return Results

    def travelsBack(self,Mod,Q,Net,Hier,Sofar,Distances):
        print("ENTER net %s   sofar=%s" % (Net,Sofar))
        self.buildNetTable(Mod)
        List = Mod.netTable[Net]
        for Inst,Pin in List:
            if Inst in Mod.libtypes0:
                Type = Mod.libtypes0[Inst]
                if isOutputPin(Type,Pin):
                    Ipins = libInputPins(Type)
                    print("FOUND DRIVER net=%s type=%s opin=%s ipins=%s" % (Net,Type,Pin,Ipins))
                    for Ipin in Ipins:
                        In = Mod.conns[Inst][Ipin]
                        Down = Sofar+[(Inst,Ipin,In)] 
                        print("CHOOSE  in=%s type=%s ipin=%s" % (In,Type,Ipin))
                        if In not in Distances: 
                            Distances[In] = Down
                            if not isFlipFlop(Type):
                                self.travelsBack(Mod,Q,In,Hier,Down,Distances)
                        else:
                            Was = len(Distances[In])
                            Now = len(Down)
                            if Now>Was:
                                Distances[In] = Down
                                if not isFlipFlop(Type):
                                    self.travelsBack(Mod,Q,In,Hier,Down,Distances)

            elif Inst in Mod.types0:
                Type = Mod.types0[Inst]
                if isModuleOutputPin(Type,Pin):
                    self.buildNetTable(Type)
                    Mod2 = self.Modules[Type]
                    Down = Sofar+[(Type,Inst,Pin)] 
                    self.travelsBack(Mod2,Q,Pin,Hier+[(Inst,Type)],Down,Distances)

        if (Net in Mod.netdirs) and (Mod.netdirs[Net] == 'input'):
            Down = Sofar+[(Type,Type,Net)] 
            if len(Hier)==1:
                if Net not in Distances: 
                    Distances[Net] = Down
                else:
                    Was = len(Distances[Net])
                    Now = len(Down)
                    if Now>Was:
                        Distances[Net] = Down
                return 
            Hier2 = Hier[:-1]
            _,Type = Hier2[-1]
            Father = self.Modules[Type]
            LL = Father.types1[Mod.Name]
            Inst = Hier[-1][0]
            if LL not in LL:
                logs.log_error('INST %s is not in module %s' % (Inst,Type))
                return

            Sig = Mod2.conns[Inst][Net]
            Down = Sofar+[(Type,Inst,Pin)] 
            self.travelsBack(Father,Q,Sig,Hier2,Down,Distances)


    def local_arcs(self,Cell):            
        self.buildNetTable(Cell)
        Mod = self.Modules[Cell]
        self.ARCS = {}
        Starts = self.sourcePoints(Cell)
        for Start in Starts:
            Longest = self.longestArc(Start,Cell)
            self.ARCS[Start] = Longest

    def longestArc(self,Start,Cell):
        Mod = self.Modules[Cell]
        Distances = {}
        Distances[Start] = [(Cell,Start,Start)]
        self.travelForwardLocal(Mod,Start,[(Cell,Start,Start)],Distances)
        Best,Len = [],0
        for Dist in Distances:
            LL = len(Distances[Dist])
            if LL>Len:
                Best = Distances[Dist]
                Len = LL
        return Best

    def travelForwardLocal(self,Mod,Start,Path,Distances):
        List = Mod.netTable[Start]
        for Inst,Pin in List:
            if Inst in Mod.libtypes0:
                Type = Mod.libtypes0[Inst]
                if isInputPin(Type,Pin):
                    Opin = libOutputPin(Type)
                    Out = Mod.conns[Inst][Opin]

                    Down = Path+[(Inst,Opin,Out)] 
                    if Out not in Distances: 
                        Distances[Out] = Down
                        if not isFlipFlop(Type):
                            self.travelForwardLocal(Mod,Out,Down,Distances)
                    else:
                        Was = len(Distances[Out])
                        Now = len(Down)
                        if Now>Was:
                            Distances[Out] = Down
                            if not isFlipFlop(Type):
                                self.travelForwardLocal(Mod,Out,Down,Distances)
            elif Inst in Mod.types0:
                Type = Mod.types0[Inst]
                if isModuleInputPin(Type,Pin):
                    self.buildNetTable(Type)
                    Mod2 = self.Modules[Type]
                    Down = Path+[(Type,Inst,Pin)] 
                    self.travelForwardLocal(Mod2,Pin,Down,Distances)



        
    def sourcePoints(self,Cell):
        Starts = []
        Mod = self.Modules[Cell]
        for Net in Mod.netdirs:
            if Mod.netdirs[Net] == 'input':
                Starts.append(Net)
            LL = Mod.netTable[Net]
            for (Inst,Pin) in LL:
                if Inst in Mod.libtypes0:
                    Type = Mod.libtypes0[Inst]
                    if isFlipFlop(Type) and isOutputPin(Type,Pin):
                        Starts.append(Net)
        return Starts 
        
    def findItems(self,Item,Cell,Path = [],List=[]):
        if Cell not in self.Modules: return
        Mod = self.Modules[Cell]
        for Net in Mod.netdirs:
            if compatible(Item,Net):
                List.append(('net','.'.join(Path),Net))
        for Inst in Mod.types0:
            if compatible(Item,Inst):
                List.append(('inst','.'.join(Path),Inst))
        for Inst in Mod.libtypes0:
            if compatible(Item,Inst):
                List.append(('inst','.'.join(Path),Inst))
        for Inst in Mod.types0:
            Type = Mod.types0[Inst]
            self.findItems(Item,Type,Path + [Inst],List)




    def endPoints(self,Cell):
        self.buildNetTable(Cell)
        Ends = []
        Mod = self.Modules[Cell]
        for Inst in Mod.conns:
            if Inst in Mod.libtypes0:
                Type = Mod.libtypes0[Inst]
                if isFlipFlop(Type):
                    QQ = Mod.conns[Inst]['Q'] 
                    DD = Mod.conns[Inst]['D'] 
                    Ends.append((QQ,DD))
        return Ends
            
        for Net in Mod.netdirs:
            if Net not in Mod.netTable:
                logs.log_error('NET %s not in module %s' % (Net,Mod.Name));
            else:
                LL = Mod.netTable[Net]
                Q,D = False,False
                for (Inst,Pin) in LL:
                    if Inst in Mod.libtypes0:
                        Type = Mod.libtypes0[Inst]
                        if isFlipFlop(Type) and isOutputPin(Type,Pin):
                            Q = Net
                        if isFlipFlop(Type) and isDataInPin(Type,Pin):
                            D = Net
                if (Q and D):
                    Ends.append((Q,D))
                elif (Q or D):
                    print("FLOP!!! %s %s %s" % (Inst,Type,LL))
        return Ends 
        

def main():
    global Env,Params
    Dir = 'pys'
    Params = logs.parse_args()
    if '-dir' in Params:
        Dir = Params['-dir'][0]
    Env = accessClass(Dir)
    if '-do' in Params:
        for Cmd in Params['-do']:
            use_command_wrds(Cmd.split())
    execute_terminal_commands()

def execute_terminal_commands():
    Intr = cmdxClass()
    Intr.prompt='?:'
    Intr.cmdloop('hello')

import cmd
class cmdxClass(cmd.Cmd):
    def do_exit(self,aaa):
        print('thanks and see you again')
        logs.closeLogs()
        cleanUp()
        saveHistory()
        sys.exit()
    def do_quit(self,aaa):
        print('thanks and see you again')
        logs.closeLogs()
        cleanUp()
        saveHistory()
        sys.exit()
    def do_help(self,aaa):
        logs.log_info(helpString)
    def emptyline(self):
        print('top: %s path=%s' % (Env.Top,Env.Path))
        return False
    def default(self,Txt):
        wrds = Txt.split()
        if len(wrds)>0:
            try:
                use_command_wrds(wrds)
            except:
                logs.log_info("Failed: %s " % Txt)
                traceback.print_last()
                traceback.print_last(None,logs.Flogs[0])
#                use_command_wrds(wrds)
            Env.CommandsHistory.append(Txt)
        return False

def cleanUp():
    return
def saveHistory():
    if len(Env.CommandsHistory) < 3: return
    Fout = open('cmd.hist','w')
    for line in Env.CommandsHistory:
        Fout.write('%s\n' % line)
    Fout.close()

COMMANDS = '''
source include paths description  top hier
nettable children
help
local_arcs
sizes
goto
list 
back_arcs
registers
where
find exit quit
'''.split()

def use_command_wrds(wrds):
    if wrds[0] == 'import':
        my_importing(wrds[1],Env)
        return
    if wrds[0] in ['source','include']:
        if len(wrds) == 1:
            use_command_wrds(['insts'])
            return
        Lines = readLines(wrds[1])
        for Line in Lines:
            X = Line.split()
            if X!= []:
                use_command_wrds(X)
        return

    if wrds[0] == 'goto':
        if len(wrds) == 1: 
            Str0 = []
            Str1 = []
            for Inst,Type in Env.Path:
                Str0.append(Inst)
                Str1.append(Type)
            logs.log_info('path is %s' % '.'.join(Str0))
            logs.log_info('path is %s' % '.'.join(Str1))
            return
        Env.goto(wrds[1])
        return
    if wrds[0] == 'where':
        Str0 = []
        Str1 = []
        for Inst,Type in Env.Path:
            Str0.append(Inst)
            Str1.append(Type)
        logs.log_info('path is %s' % '.'.join(Str0))
        logs.log_info('path is %s' % '.'.join(Str1))
        return
        

    if wrds[0] == 'description':
        if len(wrds) == 1:
            Tops = [Env.Top]
        elif wrds[1] == '*':
            Tops = list(Env.Modules.keys())
        else:
            Tops = []
            for Module in Env.Modules:
                if wrds[1] in Module:
                    Tops.append(Module)
                    
        print(Tops)
        for Top in Tops:
            Res = Env.description(Top)
            (Outs,Ins,Wires,Flops,Types0,Types1,LibTypes0,LibTypes1) = Res
            logs.log_info('%s : i=%d o=%d w=%d flops=%d child=%s libs=%d/%d' % (Top,Ins,Outs,Wires,Flops,Types1,LibTypes0,LibTypes1))
        return

        
    if wrds[0] in [ 'quit','exit']:
        print('thanks and see you again')
        logs.closeLogs()
        cleanUp()
        saveHistory()
        sys.exit()

    if wrds[0] == 'top':
        if len(wrds) == 1:
            logs.log_info('top is %s' % Env.Top)
            return
        Module = wrds[1]
        if Module in Env.Modules:
            Env.Top = Module
        else:
            logs.log_info("%s not loaded" % Module)
        return

    if wrds[0] == 'sizes':
        Env.hierSizes()
        LL = []
        for Cell in Env.Sizes:
            Size = Env.Sizes[Cell]
            Local = Env.selfSizes[Cell]
            LL.append((Size,Local,Cell))
        LL.sort()
        LL.reverse()
        for Size,Local,Cell in LL:
            Mod = Env.Modules[Cell]
            logs.log_info('%10d %10d    %s' % (Size,Local,Cell))
        return
    if wrds[0] == 'hier':
        if len(wrds)>1:
            Env.generatePng(wrds[1])
            return
        elif Env.Top:
            Env.generatePng(Env.Top)
            return

    if wrds[0] == 'nettable':
        if len(wrds)>1:
            Env.buildNetTable(wrds[1])
            Cell = wrds[1]
        elif self.Top:
            Env.buildNetTable(self.Top)
            Cell = Env.Top
        Mod = Env.Modules[Cell]
        for Net in Mod.netTable:
            LL = Mod.netTable[Net]
            logs.log_info('%d %s %s ' % (len(LL),Net,Mod.netTable[Net]))
        return
    if wrds[0] == 'list':
        Env.nicelist()
        return

    if wrds[0] == 'find':
        Item = wrds[1]
        List = []
        Env.findItems(Item,Env.Top,[Env.Top],List)
        for Kind,Path,Item0 in List:
            Prev = '  '*Path.count('.')
            logs.log_short('    %s%s %s.%s' % (Prev,Kind,Path,Item0))
        return

    if wrds[0] == 'path':
        logs.log_info('PATH: %s' % Env.Path)
        return
    if wrds[0] == 'paths':
        if len(wrds)>1:
            Env.hierPaths(wrds[1])
            os.system('open %s.paths.csv' % wrds[1])
        else:
            Env.hierPaths(Env.Top)
            os.system('open %s.paths.csv' % Env.Top)
        return
    if wrds[0] == 'children':
        Topm = getModuleByName(wrds)
        if not Topm: return
        Env.highlites(Topm.Name)
        logs.log_info('children: %s ' % Topm.types0)
        return

    if wrds[0] == 'help':
        logs.log_info('COMMANDS: help exit quit %s' % (' '.join(COMMANDS)))
        return

    if wrds[0] == 'registers':
        if len(wrds)>1:
            Module = wrds[1]
        else:
            if Env.Path == []: 
                logs.log_error('run goto command first to point me to the right module')
                return
            Module = Env.Path[-1][1]
        Regs =  Env.endPoints(Module)
        for ind,Reg in enumerate(Regs):
            logs.log_short('      %d:   %s    %s' % (ind,Reg,Module))

        Fout = open('%s.registers.csv' % Module,'w')
        Fout.write('%s,reg,datapin,module\n' % (Module))
        for ind,Reg in enumerate(Regs):
            Fout.write('%d,%s,%s,%s\n' % (ind,Reg[0],Reg[1],Module))
        Fout.close()
        os.system('open %s.registers.csv' % Module)


    if wrds[0] == 'back_arcs':
        Results = Env.travelBack()
        if not Results:
            logs.log_info("none")
            return
        ind = 0
        for Reg in Results:
            Distances = Results[Reg]
            Len = 0
            Longest = []
            for Start in Distances:
                Path0 = Distances[Start]
                if len(Path0)>Len:
                    Len = len(Path0)
                    Longest = Path0
            logs.log_info('%d %s %d\n\n\n' % (ind,Reg[0],Len))
            for Log in Longest:
                logs.log_short('     %s' % str(Log))
            ind += 1
        return

    if wrds[0] == 'local_arcs':
        if len(wrds)>1:
            Env.local_arcs(wrds[1])
            Mod = Env.Modules[wrds[1]]
        elif Env.Top:
            Env.local_arcs(Env.Top)
            Mod = Env.Modules[Env.Top]
        LL = []
        for Start in Env.ARCS:
            LL.append((len(Env.ARCS[Start]),Start,Env.ARCS[Start][-1],Env.ARCS[Start]))
        LL.sort()

        Ind = 0
        for Len,Start,End,Path in LL:
            Res = []
            for Inst,Pin,Sig in Path:
                if Inst in Mod.libtypes0:
                    Func = libFunction(Inst,Mod)
                    Type = Mod.libtypes0[Inst]
                    Type = Type.replace('scs130ms_','')
                    Type = Type.replace('_1','')
                    if Sig[0] != '_':
                        Res.append('%s %s.%s       = %s' % (Sig,Type,Pin,Func))
                    else:
                        Res.append('      %s .%s.%s  = %s' % (Sig,Type,Pin,Func))
                else:
                    Res.append('%s.%s' % (Inst,Sig))
            Str = '\n            '.join(Res)    
            logs.log_info('\n\n\n%d  %d   %s %s   \n         %s' % (Ind,Len,Start,End[2],Str))
            Ind += 1
            

        return

    if wrds[0] in COMMANDS: return

    for Command in COMMANDS:
        if wrds[0] in Command:
            wrds[0] = Command
            use_command_wrds(wrds)
            return

    logs.log_warning('no command %s' % str(wrds))

def getModuleByName(wrds):
    Topm = False
    if len(wrds)>1: 
        Top = wrds[1]
    else:
        Top = Env.Top

    if Top not in Env.Modules:
        logs.log_error('no module %s' % Top)
        return False
    Topm = Env.Modules[Top]
    return Topm
    
def isFlipFlop(Type):
    if Type not in cellLib: return False
    Desc = cellLib[Type].Job
    return Desc == 'flipflop'

def isOutputPin(Type,Pin):
    if Type not in cellLib: return False
    Pins = cellLib[Type].Pins
    return Pins[Pin] == 'output'

def isInputPin(Type,Pin):
    if Type not in cellLib: return False
    Pins = cellLib[Type].Pins
    return Pins[Pin] == 'input'

def isDataInPin(Type,Pin):
    if Type not in cellLib: return False
    Pins = cellLib[Type].Pins
    if Pins[Pin] != 'input': return False
    if Pin != 'D': return False
    return True

def libInputPins(Type):
    if Type not in cellLib: return False
    Pins = cellLib[Type].Pins
    Res = [] 
    for Pin in Pins:
        if Pins[Pin] == 'input':
            Res.append(Pin)
    return Res

def libOutputPin(Type):
    Pins = cellLib[Type].Pins
    for Pin in Pins:
        if Pins[Pin] == 'output': return Pin

def isModuleInputPin(Type,Pin):
    if Type not in Env.Modules: return False
    Mod = Env.Modules[Type]
    if Pin not in Mod.netdirs: return False
    return Mod.netdirs[Pin] == 'input'

def isModuleOutputPin(Type,Pin):
    if Type not in Env.Modules: return False
    Mod = Env.Modules[Type]
    if Pin not in Mod.netdirs: return False
    return Mod.netdirs[Pin] == 'output'

def libFunction(Inst,Mod):
    Type = Mod.libtypes0[Inst]
    Pins = cellLib[Type].Pins
    Conns = Mod.conns[Inst]
    Opin = libOutputPin(Type)
    Func = cellLib[Type].pinsFunc[Opin]

    for Pin in Pins:
        if Pin in Conns:
            Sig = Conns[Pin]
            Func = Func.replace(Pin,Sig)
    Func = Func.replace(' ','')
    return Func
        
def compatible(Pattern,Exact): 
    if Pattern==Exact: return True
    if Pattern in Exact: return True
    return False


helpString = '''
    %s
    invokation: llbin/loadall.py -dir "pys2" -do "command" 
    for -dir the default is pys
    for -do : no default.
    quit or exit
'''%(' '.join(COMMANDS))
if __name__ == '__main__': main()

