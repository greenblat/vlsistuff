#! /usr/bin/env python3
import os,sys,string

import traceback

sys.path.append('gutted')
sys.path.append('pys')
sys.path.append('.')
import importlib
sys.path.append('/Users/iliagreenblat/verpy/')
sys.path.append('/home/ilia/vlsistuff/verpy/pybin3')
import logs
from skywaterLib import cellLib as cellLib
if os.path.exists('tsmc12library.py'):
    from tsmc12library import cellLib as cellLib1
    for Cell in cellLib1:
        Desc = cellLib1[Cell]
        cellLib[Cell] = Desc




singleGateArea = 0.258048


def toreport(Cell):
    if Cell.startswith('sub_unsigned'): return False
    if Cell.startswith('sub_signed'): return False
    if Cell.startswith('add_unsigned'): return False
    if Cell.startswith('add_signed'): return False
    if Cell.startswith('csa_tree'): return False
    return True



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
        self.filters = []
        self.Areas = {}   # computed area and gatecount
        
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
        if MISSING == []:
            logs.log_info('NO MISSING modules')
        else:
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
        logs.log_short("  highlites: %-30s    nets=%d wires= %d  child=%d libt=(%d %d)  insts= %d" % (Cell,Wids,Wires,Types1,LibTypes0,LibTypes1,Insts))
        return Cell,Wids,Wires,Types0,Types1,LibTypes0,LibTypes1,Insts
            
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

    def getModuleArea(self,Cell):
        if Cell not in self.Modules: return 0
        if Cell in self.Areas: return self.Areas[Cell]
        Mod = Env.Modules[Cell]
        Total = 0
        for Inst in Mod.libtypes0:
            Type = Mod.libtypes0[Inst]
            Area = libArea(Type)
            Total += Area
        for Inst in Mod.types0:
            Type = Mod.types0[Inst]
            Area = self.getModuleArea(Type)
            Total += Area
        self.Areas[Cell] = Total
        return Total





    def nicelist(self):
        List = []
        for Cell in self.Modules:
            Item = self.highlites(Cell)
            List.append(Item)
        return List

    def generatePng(self,Cell):
        Hier = {}
        self.buildHier(Cell,Hier)
        print("HH",Hier)
        Fout = open('%s.dot' % Cell,'w')
        Fout.write('digraph %s {\n' % Cell)

        self.hierSizes()

        for MM in Hier:
            Size = self.Sizes[MM]
            Local = self.selfSizes[MM]
            Fout.write('%s [label="%s\n%s/%s"];\n' % (MM,MM,Local,Size))

        for MM in Hier:
            LL = Hier[MM]
            for Item in LL:
                Fout.write('    %s -> %s [label="%s"];\n' % (MM,Item[0],Item[1]))

        Fout.write('}\n')
        Fout.close()
        os.system('dot %s.dot -Tpng > %s.png ; open %s.png' % (Cell,Cell,Cell))
    def sizeOf(self,Cell):
        Mod = self.Modules[Cell]


    def hierPaths(self,Cell):
        Paths = []
        Mod = self.Modules[Cell]
        self.buildHierPath(Mod,[(Cell,Cell)],Paths)
        Lines = []
        Ind = 0
#        print("PATHS",len(Paths))
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
                        

    def localDrivers(self,Cell):
        if Cell not in self.Modules: return {}
        Mod = self.Modules[Cell]
        Drivers = {}
        for Inst in Mod.conns:
            if Inst in Mod.libtypes0:
                Type =  Mod.libtypes0[Inst]
                Opin =  libOutputPin(Type)
                Out = Mod.conns[Inst][Opin]
                Drivers[Out] = Inst,Type,Opin
            elif Inst in Mod.types0:
                Type =  Mod.types0[Inst]
                if Type in self.Modules:
                    Mod2 = self.Modules[Type]
                    for Net in Mod2.netdirs:
                        Dir = Mod2.netdirs[Net]
                        if Dir == 'output':
                            if Net in Mod.conns[Inst]:
                                Out = Mod.conns[Inst][Net]
                                Drivers[Out] = Inst,Type,Net
        return Drivers

    def deepDrivers(self,Cell,Path):
        Locals = self.localDrivers(Cell)
        Sigs = list(Locals.keys())
        New = {}
        for Sig in Sigs:
            (Inst,Type,Net) = Locals[Sig]
            Inst2 = '%s.%s' % ('.'.join(Path),Inst)
            Sig2 = '%s.%s' % ('.'.join(Path),Sig)
            New[Sig2] = (Inst2,Type,Net)
        if Cell not in self.Modules: return New
        Mod = self.Modules[Cell]
        for Inst in Mod.types0:
            Type = Mod.types0[Inst]
            More = self.deepDrivers(Type,Path + [Inst])
            for Key in More:
                New[Key] = More[Key]
        return New 


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
#            print("START q=%s d=%s" % (Reg[0],Reg[1]))
            Hpath = hier2path(self.Path) 
            self.travelsBack(Mod,Reg[0],Reg[1],self.Path[:],[(Module,Reg[0],Reg[1],Hpath,Module)],Distances)
            Results[Reg] = Distances
        
        return Results

    def travelsBack(self,Mod,Q,Net,Hier,Sofar,Distances):
#        print("ENTER net %s   sofar=%s" % (Net,Sofar))
        self.buildNetTable(Mod)
        List = Mod.netTable[Net]
        Hpath = hier2path(Hier)
        for Inst,Pin in List:
            if Inst in Mod.libtypes0:
                Type = Mod.libtypes0[Inst]
                if isOutputPin(Type,Pin):
                    Ipins = libInputPins(Type)
#                    print("FOUND DRIVER net=%s type=%s opin=%s ipins=%s" % (Net,Type,Pin,Ipins))
                    for Ipin in Ipins:
                        In = Mod.conns[Inst][Ipin]
                        Down = Sofar+[(Inst,Ipin,In,Hpath,Mod.Name)] 
#                        print("CHOOSE  in=%s type=%s ipin=%s" % (In,Type,Ipin))
                        if isResetPin(Type,Ipin) or isClockPin(Type,Ipin):
                            pass
                        elif In not in Distances: 
                            Distances[In] = Down
                            if not isFlipFlop(Type):
                                self.travelsBack(Mod,Q,In,Hier,Down,Distances)
                            else:
                                Opin =  libOutputPin(Type)
                                Out = Mod.conns[Inst][Opin]
                                Distances[In] = Down+[(Inst,Opin,Out,Hpath,Mod.Name)]
                                
                        else:
                            Was = len(Distances[In])
                            Now = len(Down)
                            if Now>Was:
                                Distances[In] = Down
                                if not isFlipFlop(Type):
                                    self.travelsBack(Mod,Q,In,Hier,Down,Distances)
                                else:
                                    Opin =  libOutputPin(Type)
                                    Out = Mod.conns[Inst][Opin]
                                    Distances[In] = Down+[(Inst,Opin,Out,Hpath,Mod.Name)]

            elif Inst in Mod.types0:
                Type = Mod.types0[Inst]
                if isModuleOutputPin(Type,Pin):
                    self.buildNetTable(Type)
                    Mod2 = self.Modules[Type]
                    Down = Sofar+[(Type,Inst,Pin,Hpath,Mod.Name)] 
                    self.travelsBack(Mod2,Q,Pin,Hier+[(Inst,Type)],Down,Distances)

        if (Net in Mod.netdirs) and (Mod.netdirs[Net] == 'input'):
            Down = Sofar+[(Type,Type,Net,Hpath,Mod.Name)] 
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
            if Inst not in LL:
                logs.log_error('INST %s is not in module %s' % (Inst,Type))
                return

            self.buildNetTable(Father)
            if Net in Father.conns[Inst]:
                Sig = Father.conns[Inst][Net]
                Down = Sofar+[(Type,Inst,Net,Hpath,Father.Name)] 
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



    def travelForward(self,Mod,Start,Net,Hier,Sofar,Distances):
        self.buildNetTable(Mod.Name)
        if Net not in Mod.netTable: 
            logs.log_error('net %s not in %s' % (Net,Mod.Name))
            return
        List = Mod.netTable[Net]
        Hpath = hier2path(Hier)
        for Inst,Pin in List:
            if Inst in Mod.libtypes0:
                Type = Mod.libtypes0[Inst]
                if isInputPin(Type,Pin):
                    Opin = libOutputPin(Type)
                    Out = Mod.conns[Inst][Opin]

                    Down = Sofar+[(Inst,Opin,Out,Hpath,Mod.Name)]
                    if Out not in Distances: 
                        Distances[Out] = Down
                        if not isFlipFlop(Type):
                            self.travelForward(Mod,Start,Out,Hier,Down,Distances)
                    else:
                        Was = len(Distances[Out])
                        Now = len(Down)
                        if Now>Was:
                            Distances[Out] = Down
                            if not isFlipFlop(Type):
                                self.travelForward(Mod,Start,Out,Hier,Down,Distances)
            elif Inst in Mod.types0:
                Type = Mod.types0[Inst]
                if isModuleInputPin(Type,Pin):
                    self.buildNetTable(Type)
                    Mod2 = self.Modules[Type]
                    Down = Sofar+[(Type,Inst,Pin,Hpath,Mod.Name)] 
                    self.travelForward(Mod2,Start,Pin,Hier+[(Inst,Type)],Down,Distances)


        if (Net in Mod.netdirs) and (Mod.netdirs[Net] == 'output'):
            Down = Sofar+[(Type,Type,Net,Hpath,Mod.Name)] 
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
            if Inst not in LL:
                logs.log_error('INST %s is not in module %s' % (Inst,Type))
                return

            self.buildNetTable(Father)
            if Net in Father.conns[Inst]:
                Sig = Father.conns[Inst][Net]
                Down = Sofar+[(Type,Inst,Net,Hpath,Father.Name)] 
                self.travelForward(Father,Start,Sig,Hier2,Down,Distances)


        
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
                    logs.log_error("FLOP!!! %s %s %s" % (Inst,Type,LL))
        return Ends 
    def passesFilters(self,Txt):
        for wrd in self.filters:
            if (wrd[0] == '-'):
                if wrd in Txt: return False
            else:
                if wrd not in Txt: return False
        return True

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
drivers
to from
inputs outputs flops
filters
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
            logs.log_short('%10d %10d    %s' % (Size,Local,Cell))
        Fout = open('sizes.csv','w')
        Fout.write('ind,deep,local,module\n')
        for ind,(Local,Size,Cell) in enumerate(LL):
            Mod = Env.Modules[Cell]
            Fout.write('%d,%s,%s,%s\n' % (ind,Local,Size,Cell))
        Fout.close()
        os.system('open sizes.csv')



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
    if wrds[0] == 'area':
        if len(wrds) >= 2:
            Cells = wrds[1:]
        else: 
            Cells = list(Env.Modules.keys())
        LL = []
        for Cell in Cells:            
            Area = Env.getModuleArea(Cell)
            LL.append((Area,Cell))
        LL.sort()
        LL.reverse()
        for Area,Cell in LL:            
            Gates = int(Area/singleGateArea)
            logs.log_info('%50s        area= %-15s gates= %d' % (Cell,'%.2f' % Area,Gates))
        return
        

    if wrds[0] == 'list':
        List = Env.nicelist()
        File = open('list.csv','w')
        List.sort()
        File.write('module,rtlnets,synnets,rtlinsts,rtltypes,libinsts,libtypes,total_insts,area,gatecount\n')
        for Cell,Wids,Wires,Types0,Types1,LibTypes0,LibTypes1,Insts in List:
            Area = Env.getModuleArea(Cell)
            Gates = int(Area/singleGateArea)
            if toreport(Cell):
                File.write('%s,%d,%d,%d,%d,%d,%d,%d,%f,%d\n' % ( Cell,Wids,Wires,Types0,Types1,LibTypes0,LibTypes1,Insts,Area,Gates))
            
        File.close()
        os.system('open list.csv')
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
        for Inst in Topm.types0:
            Type = Topm.types0[Inst]
            logs.log_short('    %s  %s ' % (Inst,Type))
        return

    if wrds[0] == 'help':
        logs.log_info(helpString)

        for Cmd in COMMANDS:
            if Cmd in Helpers:
                logs.log_short('   %s : %s' % (Cmd,Helpers[Cmd]))
            else:
                logs.log_short('   %s : ...' % (Cmd))
        return

    if wrds[0] == 'registers':
        if len(wrds)>1:
            Module = wrds[1]
        elif Env.Path != []: 
            Module = Env.Path[-1][1]
        elif Env.Top != '':
            Module = Env.Top
        else:
            logs.log_error('run goto command first to point me to the right module')
            return
        Regs =  Env.endPoints(Module)
        for ind,Reg in enumerate(Regs):
            logs.log_short('      %d:   %s    %s' % (ind,Reg,Module))

        Fout = open('%s.registers.csv' % Module,'w')
        Fout.write('%s,reg,datapin,module\n' % (Module))
        for ind,Reg in enumerate(Regs):
            Fout.write('%d,%s,%s,%s\n' % (ind,Reg[0],Reg[1],Module))
        Fout.close()
        os.system('open %s.registers.csv' % Module)


    if wrds[0] == 'filters':
        if len(wrds) == 1:
            logs.log_short('FILTERS: %s' % str(Env.filters))
            return
        if (len(wrds) == 2) and (wrds[1] == '-'):
            Env.filters = []
            return
        Env.filters = parseFilter(wrds[1:])
        return


    if wrds[0] == 'drivers':
        Cell = Env.Top
        Drivers = Env.deepDrivers(Cell,[Cell])
        Fout = open('drivers.csv','w')
        Fout.write(',Sig,A,B,C\n')
        for Sig in Drivers:
            if Env.passesFilters(Sig):
                logs.log_short('    %s   = %s %s %s' % (Sig,Drivers[Sig][0],Drivers[Sig][1],Drivers[Sig][2]))
                Fout.write(',%s,%s,%s,%s\n' % (Sig,Drivers[Sig][0],Drivers[Sig][1],Drivers[Sig][2]))
        Fout.close()
        return

    if wrds[0] == 'inputs':
        if len(wrds)>1:
            Module = wrds[1]
        elif Env.Path != []: 
            Module = Env.Path[-1][1]
        elif Env.Top != '':
            Module = Env.Top
        else:
            logs.log_error('run goto command first to point me to the right module')
            return

        Mod = Env.Modules[Module]
        LL = []
        for Net in Mod.netdirs:
            if Mod.netdirs[Net] == 'input':
                if Env.passesFilters(Net):
                    LL.append(Net)
        LL.sort()
        for ind,NN in enumerate(LL):
            logs.log_short('    %5d   %s' % (ind,NN))

        return

    if wrds[0] == 'outputs':
        if len(wrds)>1:
            Module = wrds[1]
        elif Env.Path != []: 
            Module = Env.Path[-1][1]
        elif Env.Top != '':
            Module = Env.Top
        else:
            logs.log_error('run goto command first to point me to the right module')
            return

        Mod = Env.Modules[Module]
        LL = []
        for Net in Mod.netdirs:
            if Mod.netdirs[Net] == 'outputs':
                if Env.passesFilters(Net):
                    LL.append(Net)
        LL.sort()
        for ind,NN in enumerate(LL):
            logs.log_short('    %5d   %s' % (ind,NN))

        return


    if wrds[0] == 'flops':
        if len(wrds)>1:
            Module = wrds[1]
        elif Env.Path != []: 
            Module = Env.Path[-1][1]
        elif Env.Top != '':
            Module = Env.Top
        else:
            logs.log_error('run goto command first to point me to the right module')
            return
        Regs = []
        Mod = Env.Modules[Module]
        for Inst in Mod.libtypes0:
            Type = Mod.libtypes0[Inst]
            if isFlipFlop(Type):
                    Opin =  libOutputPin(Type)
                    Osig = Mod.conns[Inst][Opin]
                    if Env.passesFilters(Inst)or  Env.passesFilters(Osig):
                        Regs.append((Osig,Type,Inst))
        Regs.sort()
        for ind,(Sig,Type,Inst) in enumerate(Regs):
            logs.log_short('    %20s     %s   %s' % (Sig,Type,Inst))
        return

    if wrds[0] == 'from':
        Full = wrds[1]
        ww = wrds[1].split('.')
        Reg = ww[-1]
        Path = '.'.join(ww[:-1])
        Env.goto(Path)
        Distances = {}
        Cell = Env.Path[-1][1]
        Mod = Env.Modules[Cell]
        Hpath = hier2path(Env.Path) 
        Env.travelForward(Mod,Full,Reg,Env.Path[:],[(Cell,Full,Full,Hpath,Cell)],Distances)
        Env.FROMDIST = Distances
        Prints = []
        for Key in Env.FROMDIST:
            List = Env.FROMDIST[Key]
            Hpath = List[-1][3]
            Prints.append((len(List),Hpath,Key,List))
        Prints.sort()
        Prints.reverse()
        for Len,Hpath,Key,List in Prints:
            logs.log_short('\n\n    %s.%s    %d' % (Hpath,Key,Len))
            for Item in List:
                logs.log_short('        %s' % str(Item))
        return


    if wrds[0] == 'fanout':
        buildFrom(Env,wrds[1])
        for Key in Env.FROMDIST:
            if Key[0] != '_':
                logs.log_short('   %s %d  %s' % (Key,len(Env.FROMDIST[Key]),Env.FROMDIST[Key][-1]))
                for Item in Env.FROMDIST[Key]:
                    logs.log_short('        %s' % str(Item))
        return


    if wrds[0] == 'support':
        buildTo(Env,wrds[1])
        LL = []
        for Key in Env.TODIST:
            if Key[0] != '_':
                List = Env.TODIST[Key]
                LL.append((len(List),Key))
        LL.sort()
        for _,Key in LL:
            List = Env.TODIST[Key]
            if Key.startswith('invented'):
                Cell = List[0][-1]
                Meaning = whoInvented(Key,Cell)
            else:
                Meaning = ''
            logs.log_short('   %s %d  %s %s' % (Key,len(List),Meaning,List[-1]))
            for Item in List:
                if Item[2].startswith('invented'):
                    Cell = Item[-1]
                    Meaning = whoInvented(Item[2],Cell)
                    Itemx = [Meaning,Item[2],Item[0],Item[1],Item[3],Item[3]]
                    logs.log_short('        %s' % str(Itemx))
                elif Item[2][0] == '_' :
                    Itemx = [Item[2],Item[0],Item[1],Item[3],Item[3]]
                    logs.log_short('            %s' % str(Itemx))
                else:
                    Itemx = [Item[2],Item[0],Item[1],Item[3],Item[3]]
                    logs.log_short('        %s' % str(Itemx))
        return

    if wrds[0] == 'to':
        Full = wrds[1]
        ww = wrds[1].split('.')
        Reg = ww[-1]
        Path = '.'.join(ww[:-1])
        if Path=='': Path = Env.Top
        Env.goto(Path)
        Distances = {}
        Cell = Env.Path[-1][1]
        Mod = Env.Modules[Cell]
        Hpath = hier2path(Env.Path) 
        Reg2 = skipQtoD(Mod,Reg)
        Env.travelsBack(Mod,Full,Reg2,Env.Path[:],[(Cell,Full,Full,Hpath,Cell)],Distances)

        Env.TODIST = Distances
        LL = []
        for Key in Env.TODIST:
            List = Env.TODIST[Key]
            LL.append((len(List),Key))
        LL.sort()
        for (_,Key) in LL:
            List = Env.TODIST[Key]
            Hpath = List[-1][3]

            logs.log_short('\n\n    %s.%s    %d' % (Hpath,Key,len(List)))
            for Item in List:
                logs.log_short('        %s' % str(Item))
        return

    

    if wrds[0] == 'back_arcs':
        Results = Env.travelBack()
        if not Results:
            logs.log_info("none")
            return
        ind = 0
        Fout = open('back_arcs.csv','w')
        Fout.write(',Sig,Cell,Type,Pin,Inst,Func\n')
        for Reg in Results:
            Distances = Results[Reg]
            Len = 0
            Longest = []
            for Start in Distances:
                Path0 = Distances[Start]
                if len(Path0)>Len:
                    Len = len(Path0)
                    Longest = Path0
            logs.log_info('\n\n\n %d %s %d' % (ind,Reg[0],Len))
            Fout.write(',,,\n')
            Fout.write(',,,\n')
            Fout.write('newPath,ind=%d,reg=%s,len=%d\n' % (ind,Reg[0],Len))
            Fout.write(',Sig,Cell,Type,Pin,Inst,Func\n')
            for Log in Longest:
                if len(Log) == 4:
                    Inst,Pin,Sig,Cell = Log
                    Mod2 = Env.Modules[Cell]
                    if Inst in Mod2.types0:
                        Type = Mod2.types0[Inst]
                    elif Inst in Mod2.libtypes0:
                        Type = Mod2.libtypes0[Inst]
                    else:
                        Type = 'type?'
                    Type = Type.replace('scs130ms_','')
                    Type = Type.replace('_1','')
                    Func = libFunction(Inst,Mod2)
                    Pref = '          '
                    if Sig[0] == '_':
                        Pref += '            '
                    logs.log_short('     %s%20s   %s %s %s %s  %s' % (Pref,Sig,Cell,Type,Pin,Inst,Func))
                    Fout.write(',%s,%s,%s,%s,%s,%s\n' % (Sig,Cell,Type,Pin,Inst,Func))
                else:
                    logs.log_short('222     %s %s' % (Log[0],Log[1]))
            ind += 1
        Fout.close()
        os.system('open back_arcs.csv')
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


def buildFrom(Env,Full):
    ww = Full.split('.')
    Reg = ww[-1]
    Path = '.'.join(ww[:-1])
    if Path=='': Path = Env.Top
    Env.goto(Path)
    Distances = {}
    Cell = Env.Path[-1][1]
    Mod = Env.Modules[Cell]
    Hpath = hier2path(Env.Path) 
    Env.travelForward(Mod,Full,Reg,Env.Path[:],[(Cell,Full,Full,Hpath,Cell)],Distances)
    Env.FROMDIST = Distances

def buildTo(Env,Full):
        ww = Full.split('.')
        Reg = ww[-1]
        Path = '.'.join(ww[:-1])
        if Path=='': Path = Env.Top
        Env.goto(Path)
        Distances = {}
        Cell = Env.Path[-1][1]
        Mod = Env.Modules[Cell]
        Hpath = hier2path(Env.Path) 
        Regs2 = skipQtoD(Mod,Reg)
        print("JUMP",Full,Regs2)
        for Reg2 in Regs2:
            Env.travelsBack(Mod,Full,Reg2,Env.Path[:],[(Cell,Full,Full,Hpath,Cell)],Distances)
        Env.TODIST = Distances

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

def libArea(Type):
    if Type == 'BUF': return 0
    if Type not in cellLib: 
        logs.log_info('cell is not in cellLib "%s"' % (Type))
        return 0
    Area = cellLib[Type].properties['area']
    return float(Area)

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
    if Inst not in Mod.libtypes0: return ''
    Type = Mod.libtypes0[Inst]
    Pins = cellLib[Type].Pins
    Conns = Mod.conns[Inst]
    Opin = libOutputPin(Type)
    Func = cellLib[Type].pinsFunc[Opin]

    for Pin in Pins:
        if Pin in Conns:
            Sig = Conns[Pin]
            Func = Func.replace(Pin,Sig)
    Osig = Conns[Opin] 
    Func = '%s=%s' % (Osig,Func.replace(' ',''))
    return Func
        
def isResetPin(Type,Pin):
    if Type not in cellLib: return False
    Obj = cellLib[Type]
    if Pin not in Obj.pinsJobs: return False
    return Obj.pinsJobs[Pin] == 'reset'

def isClockPin(Type,Pin):
    if Type not in cellLib: return False
    Obj = cellLib[Type]
    if Pin not in Obj.pinsJobs: return False
    return Obj.pinsJobs[Pin] == 'clock'

def hier2path(Hier):
    Res = []
    for A,B in Hier:
        Res.append(A)
    Path = '.'.join(Res)
    return Path


def compatible(Pattern,Exact): 
    if Pattern==Exact: return True
    if Pattern in Exact: return True
    return False

def skipQtoD(Mod,Reg):
    Env.buildNetTable(Mod)
    List = Mod.netTable[Reg]
    for Inst,Pin in List:
        Type = Mod.libtypes0[Inst]
        if isOutputPin(Type,Pin) and  isFlipFlop(Type):
            QQ = Mod.conns[Inst]['Q'] 
            if QQ == Reg:
                DD = Mod.conns[Inst]['D'] 
                if 'DE' in Mod.conns[Inst]:
                    DE = Mod.conns[Inst]['DE'] 
                    return [DD,DE]
                return [DD]
    return [Reg] 

def parseFilter(wrds):
    Res = wrds
    return Res
            
import importlib
INVENTIONS = {} 
def  whoInvented(Key,Cell):
    if Cell in INVENTIONS:
        DD = INVENTIONS[Cell].INVENTIONS[Key]
        return DD
    
    That = importlib.import_module('%s_invents' % Cell)
    INVENTIONS[Cell] = That
    return whoInvented(Key,Cell)






Helpers = {}
Helpers['flops'] = 'flops <cell>  :list all flops in top or cell'
Helpers['inputs'] = 'inputs <cell>  :list all inputs in top or cell'
Helpers['outputs'] = 'outputs <cell>  :list all outputs in top or cell'
Helpers['where'] = 'list current "goto" path'
Helpers['children'] = 'children of top module or <cell> module'
Helpers['sizes'] = 'compute and list sizes of modules [in number of lib cells]'
Helpers['exit'] = 'exit'
Helpers['quit'] = 'same as exit'
Helpers['filters'] = 'set filter(s) on report lines'
Helpers['drivers'] = 'list all driven nets and their driver in top and deeper hierarchy.'

helpString = '''
    invokation: llbin/loadall.py -dir "pys2" -do "command" 
    for -dir the default is pys
    for -do : no default.
    quit or exit

'''
if __name__ == '__main__': main()

