#! /usr/bin/env python3
# stand alone app. loads from pys/ directory produced by synthesiz0

import os,sys,importlib
sys.path.append('/Users/iliagreenblat/vlsistuff/verpy/pybin3')
import logs
sys.path.append('pys')
# import axi_master_ml
ENV = {}
DB = {}
DB['filter'] = False
DB['filters+'] = []
DB['filters-'] = []
DB['dont_list'] = False
Top = ''
def main():
    global Top
    Top = sys.argv[1]
    Cmds = []
    if '-do' in sys.argv:
        Ind = sys.argv.index('-do')
        Cmd = sys.argv[Ind+1]
        if os.path.exists(Cmd):
            File = open(Cmd)
            Cmds = File.readlines()
            File.close()
        else:
            Cmds = [Cmd]
    bringType(Top)
    bringSons(Top)
    INSTPATH.append(Top)
    TYPEPATH.append(Top)
    COMMANDS.extend(list(ENV.keys()))
    while Cmds!= []:
        Cmd = Cmds.pop(0)
        if len(Cmd)>1:
            use_command_wrds(Cmd.split( ))
    execute_terminal_commands()

def bringSons(Top):
    Types = []
    for Inst in ENV[Top].INSTS:
        (Type,Params,Conns) = ENV[Top].INSTS[Inst]
        if (Type not in Types) and (Type not in BRICKS):
            Types.append(Type)

    Types.sort()
    for Type in Types:
        bringType(Type)

def bringType(Type):
        Fname = 'pys/%s.py' % Type
        if os.path.exists(Fname):
            That = importlib.import_module(Type)
            ENV[Type] = That
        if Type in ENV:
            bringSons(Type)
        elif Type not in BRICKS:
            lprint('failed to load %s' % Type)

# BRICKS = ['select','select_bus','adder', 'adder_lit', 'and2', 'bufx', 'comparator', 'comparator_lit', 'flipflop', 'inv', 'mux2', 'or2', 'or3', 'or4', 'or5','or6','or7','or8','shiftleft', 'shiftright', 'subtractor', 'subtractor_lit','multiplier','shiftright_lit','shiftleft_lit','mflipflop','mpflipflop','multiplier_lit']


BRICKS = '''
    select select_bus adder  adder_lit  and2  bufx  comparator  comparator_lit  
    flipflop  inv  mux2  
    shiftleft  shiftright  subtractor  subtractor_lit multiplier
    shiftright_lit shiftleft_lit mflipflop mpflipflop
    xor2 xor3 xor4 xor5 xor6 xor7 xor8
    and2 and3 and4 and5 and6 and7 and8
    or2  or3  or4  or5 or6 or7 or8 
    select_bus_lit
    multiplier_lit
'''.split()


import cmd  
class cmdxClass(cmd.Cmd):
    def do_exit(self,aaa):
        self.do_quit(aaa)

    def do_quit(self,aaa):
        quiting()
        return True 

    def do_help(self,aaa):
        helping()



    def emptyline(self):
        print('emptyline')
        return False
    def default(self,Txt):
        wrds = splitLine(Txt)
        if len(wrds)>0:
            use_command_wrds(wrds)
        return False

def helping():
    lprint('commands: %s' % str(COMMANDS))
    lprint(HELPSTRING)
    return True 


INSTPATH = []
TYPEPATH = []
Sfile = open('session.cmds','w')
Lfile = open('session.log','w')
def lprint(Txt):
    print(Txt)
    Lfile.write('%s\n' % Txt)

def use_command_wrds(wrds):
    global LEVELS
    Sfile.write('%s\n' % ' '.join(wrds))
    Lfile.write('%s\n' % ' '.join(wrds))
    if wrds[0] in ['quit','exit']: 
        quiting()
        return
    if wrds[0] == 'pwd':
        lprint('.'.join(INSTPATH))
        return
    if wrds[0] == 'ls':
        Last = TYPEPATH[-1]
        if Last not in ENV:
            lprint('type %s not loaded or is BRICK' % (Last))
            return
        lprint('type=%s path=%s insts=%d' % (TYPEPATH[-1],'.'.join(INSTPATH),len(ENV[Last].INSTS.keys())))
        Filter = False
        if len(wrds)>1: Filter = wrds[1]
        for Inst in ENV[Last].INSTS:
            Type,_,Conns = ENV[Last].INSTS[Inst]
            if (not Filter) or (Filter in Type) or (Filter in Inst):
                if Type not in BRICKS:
                    lprint('%s  (%s) conns=%d' % (Inst,Type,len(list(Conns.keys()))))
        return 
    if wrds[0] == 'unused':
        buildCross(Top,ENV[Top])
        for Base in NETTABLES:
            Mod = NETTABLES[Base]
            for Net in Mod:
                List = Mod[Net]
                if Net and ('sign_version' not in Net) and (len(List) == 1):
                    lprint("%s : %s      %s" % (Base,Net,List))

        return
    if wrds[0] == 'top':
        lprint(Top)
        return
    if wrds[0] == 'cd':
        if wrds[1] == '~':
            while len(TYPEPATH)>1:
                TYPEPATH.pop(-1)
                INSTPATH.pop(-1)
            return
        if wrds[1] == '..':
            if len(TYPEPATH)>1:
                TYPEPATH.pop(-1)
                INSTPATH.pop(-1)
            return
        Path = wrds[1].split('.')
        First = Path[0]
        Current = TYPEPATH[-1]
        if First == INSTPATH[-1]:
            Path.pop(0)
            use_command_wrds(['cd','.'.join(Path)])
            return
        Mod = ENV[Current]
        for Inst in Mod.INSTS:
            if (First in Inst) or (First in Mod.INSTS[Inst][0]):
                TYPEPATH.append(Mod.INSTS[Inst][0])
                INSTPATH.append(Inst)
                if len(Path) == 1: return
                Path.pop(0)
                use_command_wrds(['cd','.'.join(Path)])
                return


        lprint('failed to cd %s' % First)
        return            

    if wrds[0] == 'inst':
        buildHierarchy()
        if len(wrds) == 1:
            lprint('error! find needs something to find')
            return            
        Inst = wrds[1]
        for Path in HIER:
            Type = HIER[Path][0]
            if (Inst in Path) and accepted(str(Path)):
                lprint('INST> %s %s  %s' % (Type,Path,HIER[Path][2]))
        return
    if wrds[0] == 'find':
        buildHierarchy()
        if len(wrds) == 1:
            lprint('error! find needs something to find')
            return            

        What = wrds[1]
        What2 = False
        What3 = False
        if len(wrds)>2: What2 = wrds[2]
        if len(wrds)>3: What3 = wrds[3]
        ii = 0
        for Mod in ENV:
            Nets = ENV[Mod].NETS
            for Net in Nets:
                if compatible(Net,What,What2,What2) and accepted(Net):
                    lprint('%d N> %s %s %s' % (ii,Mod,Net,Nets[Net][0]))
                    ii+= 1
        ii = 0
        for Path in HIER:
            Type = HIER[Path][0]
            if compatible(Path + ' '+ Type,What,What2,What2) and accepted(str(Path)):
                lprint('%d M> %s %s' % (ii,HIER[Path][0],Path))
                ii += 1
#        for Path in HIER:
#            Type = HIER[Path][0]
#            if compatible(Type,What,What2,What2):
#                lprint('M> %s %s' % (HIER[Path][0],Path))
        return

    if wrds[0] == 'exfind':
        What = wrds[1]
        for Mod in ENV:
            Nets = ENV[Mod].NETS
            for Net in Nets:
                if What == Net:
                    lprint('> %s %s %s' % (Mod,Net,Nets[Net][0]))
        return
    if wrds[0] == 'import':
        my_importing(Fname)
        return
    if wrds[0] == 'source':
        File = open(wrds[1])
        Lines = File.readlines()
        File.close()
        for line in Lines:
            wrds0 = splitLine(line)
            if len(wrds)>0:
                use_command_wrds(wrds)
        return
    if wrds[0] == 'filter':
        if len(wrds) == 1:
            lprint("filter=%s" % DB['filter'])
            lprint("filters+=%s" % str(DB['filters+']))
            lprint("filters-=%s" % str(DB['filters-']))
        elif wrds[1] in ['off','0']:
            DB['filter'] = False
        elif wrds[1] in ['on','1']:
            DB['filter'] = True
        elif wrds[1] in ['clear']:
            DB['filter'] = False
            DB['filters+'] = []
            DB['filters-'] = []
        elif wrds[1] == '+':
            DB['filters+'].extend(wrds[2:])
        elif wrds[1] == '-':
            DB['filters-'].extend(wrds[2:])
        else:
            lprint('error! filter wrong "%s"' % str(wrds))
        return
    if wrds[0] == 'starts':
        if len(wrds) == 1:
            Sts = listRegsQ_(Top)
        else:
            Sts = listRegsQ_(wrds[1])
        DB['starts'] = Sts
        II = 0
        for Key in Sts:
            if accepted(Key):
                lprint("%05d     %s  %s" % (II,Key,Sts[Key]))
                II += 1
        return 
    if wrds[0] == 'hier':
        if len(wrds) == 1:
            run_hier(Top)
        else:
            run_hier(wrds[1])
        return
    if wrds[0] == 'clean':
        cleanTiming()
        return
    if wrds[0] == 'fromto':
        buildCross(Top,ENV[Top])
        if len(wrds)<3:
            lprint('error! expected command: fromto FROM TO')
            return
            
        From = wrds[1]
        To = wrds[2]
        DB['dont_list'] = True
#        use_command_wrds(['to',To])
        LEVELS = {}
        use_command_wrds(['from',From])
        DB['dont_list'] = False
        for Path in PATHSF+PATHSB:
            PP = str(Path)
            if (From in PP) and (To in PP):
                onepath(Path)
        return


    if wrds[0] == 'to':
        buildCross(Top,ENV[Top])
        Keys = wrds[1:]
        if 'starts' not in DB:
            lprint('run starts before from')
            return
        Sts = DB['starts']
        for Key in Keys:
            if Key in Sts:
                Path = Sts[Key]
                ww = Key.split('.')
                Base = Path[-1][0]
                travelTimeBack(ww[-1],Base,Path,[Key],0)
        timelisting()
        LEVELS = {}
        return

    if wrds[0] == 'from':
#        cleanTiming()
        buildCross(Top,ENV[Top])
        Keys = wrds[1:]
        if 'starts' not in DB:
            lprint('run starts before from')
            return
        Sts = DB['starts']
        for Key in Keys:
            if Key in Sts:
                Path = Sts[Key]
                ww = Key.split('.')
                Base = Path[-1][0]
                travelTimeDeep(ww[-1],Base,Path,[Key],0)
        timelisting()
        LEVELS = {}
        return
            
    if wrds[0] == 'timing':
        cleanTiming()
        if len(wrds) == 1:
            run_timing(Top)
        else:
            run_timing(wrds[1])
        return
    if wrds[0] in HIER:
        Type,Params,Conns = HIER[wrds[0]]
        lprint('%s:\n %s %s\n  %s' % (wrds[0],Type,Params,Conns))
        return

    if wrds[0] in ENV:
        Mod = ENV[wrds[0]]
        lprint("%s nets %s" % (wrds[0],Mod.NETS))
        lprint("%s insts %s" % (wrds[0],Mod.INSTS))
        return

        
    if wrds[0] in BRICKS:
        lprint('module %s is brick' % (wrds[0]))
        return
    Opts = []
    for Cmd in COMMANDS:
        if Cmd.startswith(wrds[0]):
            Opts.append(Cmd)
    if len(Opts) == 1:
        print("OPTS",Opts)
        use_command_wrds([Opts[0]]+wrds[1:])
        return
    if len(Opts) > 1:
        lprint('ambigious cmd %s matches %s' % (wrds[0],Opts))
        return
        
            
    lprint("USE %s" % str(wrds))

LEVELS = {}
PATHSF = []
PATHSB = []
NETTABLES = {}

def listRegsQ_(Base):
    Mod = ENV[Base]
    Starts = {}
    listRegsQ(Mod,Base,[(Base,Base)],Starts)
    return Starts

def listRegsQ(Mod,Base,Hier,Starts):
    for Inst in Mod.INSTS:
        Obj = Mod.INSTS[Inst]
        Type = Obj[0]
        if Type in ENV:
            Son = ENV[Type]
            listRegsQ(Son,Type,Hier+[(Type,Inst)],Starts)
        elif ('flipflop' in Type):
            Conns  = Obj[2]
            Tys,Ins = path0(Hier)
            for Pin in Conns:
                if (Pin[0] == 'q'):
                    Net = Conns[Pin]
                    NextSig = '.'.join(Ins + [Inst,Pin,Net])
                    NewPath = [NextSig]
                    Starts[NextSig] = Hier

def run_hier(Base):
    Mod = ENV[Base]
    LL = []
    scanHier(Mod,Base,Base,LL)
    for (Ty,Pa) in LL:
        if accepted(Pa):
            lprint('%5d %30s    %s' % (Pa.count('.'),Ty,Pa))

def scanHier(Mod,Base,Path,LL):
    for Inst in Mod.INSTS:
        Type,_,_ = Mod.INSTS[Inst]
        if Type in ENV:
            LL.append( (Type,Path+'.'+Inst) )
            scanHier(ENV[Type],Type,Path+'.'+Inst,LL)


def run_timing(Base):
    Mod = ENV[Base]
    buildCross(Base,Mod)
    Starts = getStarts(Mod,True)
#    for Start in Starts: LEVELS['%s.%s' % (Base,Start)] = 0

    for Net in Starts:
        travelTimeDeep(Net,Base,[(Base,Base)],['%s.%s' % (Base,Net)],0)

    exploreDeep(Mod,Base,[(Base,Base)])
    timelisting()

def onepath(Path):
    Len = len(Path)
    lprint('>>>>> %d %s' % (Len,Path[0]))
    Path0 = Path[:]
    while Path0!=[]:
        lprint('    %s' % Path0.pop(0))
    lprint('\n\n')

def timelisting():
    if DB['dont_list']: return
    LL = []
    for Path in PATHSF:
        LL.append((len(Path),Path))
    for Path in PATHSB:
        LL.append((len(Path),Path))
    LL.sort()

    for Len,Path in LL:
        if accepted(str(Path)):
            lprint("PP %s %s" % (Len,Path))

    lprint('\n\nWORST\n')
    for ii in range(10):
        if LL!=[]:
            Len,Path = LL.pop(-1)
            lprint('>>>>> %d %s' % (Len,Path[0]))
            Path0 = Path[:]
            while Path0!=[]:
                lprint('    %s' % Path0.pop(0))
            lprint('\n\n')
    Strs,Ends = [],[]
    for Path in PATHSB+PATHSF:
        Str = Path[0]
        End = Path[-1]
        Len = len(Path)
        if (Len,End) not in Ends: Ends.append( (Len,End))
        if (Len,Str) not in Strs: Strs.append( (Len,Str))
    Strs.sort()
    lprint("\n\n\nSTARTS:")
    for Len,Str in Strs:
        if accepted(Str):
            lprint(" %s %s" % (Len,Str))
    lprint("\n\n\nENDS:")
    for Len,End in Ends:
        if accepted(Str):
            lprint(" %s %s" % (Len,End))
    lprint("\n\n\n")
        

#    for Key in LEVELS:
#        lprint("LVL %s %s" % (LEVELS[Key],Key))
#    sys.exit()

def exploreDeep(Mod,Base,Hier):
    print("DEEP %s %s " % (Base,Hier))
    for Inst in Mod.INSTS:
        Obj = Mod.INSTS[Inst]
        Type = Obj[0]
        print("DEEP1 %s" % Type)
        if Type in ENV:
            Son = ENV[Type]
            exploreDeep(Son,Type,Hier+[(Type,Inst)])
        elif ('flipflop' in Type) and (len(Hier)>1):
            Conns  = Obj[2]
            Tys,Ins = path0(Hier)
            print("DEEP2 %s %s %s" % (Base,Inst,Conns))
            for Pin in Conns:
                if (Pin[0] == 'q'):
                    Net = Conns[Pin]
                    NextSig = '.'.join(Ins + [Inst,Pin,Net])
                    NewPath = [NextSig]
                    print("DEEP3 %s %s" % (Base,NextSig))
                    travelTimeDeep(Net,Base,Hier,NewPath,0)
            
def currentLevel(Sig):
    if Sig not in LEVELS: return 0
    return LEVELS[Sig]
def path0(Hier):
    Types = []
    Insts = []
    for A,B in Hier:
        Types.append(A)
        Insts.append(B)
    return Types,Insts

def travelTimeBack(Net,Base,Hier,Path,Depth):
    if Net in ('gnd','vcc')  : return
    Mod = ENV[Base]
    if Net not in NETTABLES[Base]:
        logs.log_warning("no %s sig in %s" % (Net,Base))
        return
    List = NETTABLES[Base][Net]
    lprint("BACK %s %s" % (Net,Base))
    for Item in List:
        if Item[0] == 'input':
            if len(Path) == 1:
                Tys,Ins = path0(Hier)
                NextSig = '.'.join(Ins + [Inst,Pin,Sig])
                Was = currentLevel(NextSig)
                if Was<(Depth+1):
                    LEVELS[NextSig] = Depth+1
                    NewPath = Path + [NextSig]
                    PATHSB.append(NewPath) 
            elif (len(Hier) == 1):
                Tys,Ins = path0(Hier)
                NextSig = '.'.join(Ins + ['input',Net])
                Was = currentLevel(NextSig)
                if Was<(Depth+1):
                    LEVELS[NextSig] = Depth+1
                    NewPath = Path + [NextSig]
                    PATHSB.append(NewPath) 
            else:
                Opin = Item[2]
                Inst = Hier[-1][1]
                Hier = Hier[:-1]
                Type = Hier[-1][0]
                Mod = ENV[Type]
                _,_,Conns = Mod.INSTS[Inst]
                if Opin in Conns:
                    Sig = Conns[Opin]
                    Tys,Ins = path0(Hier)
                    NextSig = '.'.join(Ins + [Inst,Opin])
                    NewPath = Path + [NextSig]
                    travelTimeBack(Sig,Type,Hier,NewPath,Depth+1)

        elif isDriver(Item):
            Inst,Type,Pin0 = Item
            Obj = Mod.INSTS[Inst]
            if ('flipflop' in Type) and (Depth>1):
                Tys,Ins = path0(Hier)
                NextSig = '.'.join(Ins + [Inst,Pin0,Net])
                NewPath = Path + [NextSig]
                PATHSB.append(NewPath) 
            else:
                for Pin in Obj[2]:
                    if not Pin.startswith('q') and not Pin.startswith('x'):
                        Sig = Obj[2][Pin]
                        Tys,Ins = path0(Hier)
                        NextSig = '.'.join(Ins + [Inst,Pin,Sig])
                        Was = currentLevel(NextSig)
                        if Was<(Depth+1):
                            LEVELS[NextSig] = Depth+1
                            travelTimeBack(Sig,Base,Hier,Path + [NextSig],Depth+1)
                    
        elif Item[1] in ENV:
            Son = Item[1]
            Pin = Item[2]
            SonMod = ENV[Item[1]]
            if Pin in SonMod.NETS:
                Dir,_ = SonMod.NETS[Pin]
                if Dir == 'output':
                    Inst = Item[0]
                    Pin = Item[2]
                    Type = Item[1]
                    Son = ENV[Type]
                    if Pin in Son.NETS:
                        Dir,_ = Son.NETS[Pin]
                        if Dir == 'input':
                            Tys,Ins = path0(Hier)
                            NextSig = '.'.join(Ins + [Inst,Pin])
                            NewPath = Path + [NextSig]
                            Was = currentLevel(NextSig)
                            if Was < (Depth+1):
                                LEVELS[NextSig] = Depth+1
                                travelTimeBack(Pin,Type,Hier + [(Type,Inst)],NewPath,Depth+1)

def isDriver(Item):
    Inst,Type,Pin = Item
    if Type in BRICKS:
        return Pin.startswith('q') or Pin.startswith('x')
    return False

def travelTimeDeep(Net,Base,Hier,Path,Depth):
    Mod = ENV[Base]
    if Net not in NETTABLES[Base]:
        logs.log_warning("no %s sig in %s" % (Net,Base))
        return
    List = NETTABLES[Base][Net]
    if (Depth>200): 
        print(Depth,Base,"NET",Net,'path',Path,'  hier',len(Hier),'list',len(List))
        return
    for Item in List:
        if (Item[0] == 'output') and (Base == Top):
            NextSig = '%s.%s' % (Base,Item[2])
            NewPath = Path + [NextSig]
            Was = currentLevel(NextSig)
            if Was < (Depth+1):
                LEVELS[NextSig] = Depth+1
                PATHSF.append(NewPath)
#                lprint("TERMINALO %s %s %s " %(NewPath,'output','output'))
        if isFlopOut(Mod,Item) and (Item[0] != 'input') and (Item[0] != 'output'):
            if (len(Hier)>1):
                Pin = Item[2]
                Type = Item[1]
                Inst = Item[0]
                Tys,Ins = path0(Hier)
                Net = Mod.INSTS[Inst][2][Pin]
                NextSig = '.'.join(Ins + [Inst,Pin,Net])
                if 'input.input' in NextSig: breakIt()
                lprint("TERMINAL %d next=%s pin=%s type=%s hier=%s path=%s" %(Depth,NextSig,Pin,Type,Hier,Path))
                if Path[-1] != NextSig:
                    travelTimeDeep(Net,Base,Hier,[NextSig],0)

#                Was = currentLevel(NextSig)
#                if Was < (Depth+1):
#                    LEVELS[NextSig] = Depth+1
#                    lprint("TERMINAL %d %s %s %s %s" %(Depth+1,NextSig,NewPath,Pin,Type))
#                    PATHS.append(NewPath)
#                else:
#                    lprint("TERMINAL FAILED %d %s %s %s %s" %(Depth+1,NextSig,NewPath,Pin,Type))
        if (Item[0] == 'output') and (Base != Top):
            Opin = Item[2]
            Inst = Hier[-1][1]
            Hier = Hier[:-1]
            Type = Hier[-1][0]
            Mod = ENV[Type]
#            print(">>>>>",Net,Inst,Base,Top,Inst,Type)
            _,_,Conns = Mod.INSTS[Inst]
            if Opin in Conns:
                Sig = Conns[Opin]
                Tys,Ins = path0(Hier)
                NextSig = '.'.join(Ins + [Inst,Opin])
                if 'input.input' in NextSig: breakIt()
                NewPath = Path + [NextSig]
                travelTimeDeep(Sig,Type,Hier,NewPath,Depth+1)
        elif (Item[1] in ENV):
            Inst = Item[0]
            if Inst != 'input':
                Pin = Item[2]
                Type = Item[1]
                Son = ENV[Type]
                if Pin in Son.NETS:
                    Dir,_ = Son.NETS[Pin]
                    if Dir == 'input':
                        Tys,Ins = path0(Hier)
                        NextSig = '.'.join(Ins + [Inst,Pin])
                        if 'input.input' in NextSig: breakIt()
                        NewPath = Path + [NextSig]
                        Was = currentLevel(NextSig)
                        if Was < (Depth+1):
                            LEVELS[NextSig] = Depth+1
                            travelTimeDeep(Pin,Type,Hier + [(Type,Inst)],NewPath,Depth+1)
            
        elif isBrickInput(Item):
            Opins = matchingOutPins(Item,Base)
            Kind = Item[1]
            Inst = Item[0]
            if 'flipflop' in Kind:
                Opins = matchingOutPins(Item,Base,True)
                for Opin in Opins:
                    Tys,Ins = path0(Hier)
                    Type,_,Conns = Mod.INSTS[Inst]
                    Osig = Conns[Opin]
                    NextSig = '.'.join(Ins + [Inst,Opin,Osig])
                    if 'input.input' in NextSig: breakIt()
                    NewPath = Path + [NextSig]
                    Was = currentLevel(NextSig)
                    if Was < (Depth+1):
                        PATHSF.append(NewPath)
                        LEVELS[NextSig] = Depth+1
#                        lprint("TERMINALF %s %s %s" % (NewPath,Opin,Type))
            else:
                for Opin in Opins:
                    Type,_,Conns = Mod.INSTS[Item[0]]
                    Osig = Conns[Opin]
                    Tys,Ins = path0(Hier)
                    NextSig = '.'.join(Ins + [Inst,Opin,Osig])
                    if 'input.input' in NextSig: breakIt()
                    Was = currentLevel(NextSig)
#                    print("NEXTSIG",NextSig,Was,Depth)
                    if Was < (Depth+1):
                        LEVELS[NextSig] = Depth+1
                        travelTimeDeep(Osig,Base,Hier,Path+[NextSig],Depth+1)
                        

def matchingOutPins(Item,Base,includeQ = False):
    Mod = ENV[Base]
    Conns = Mod.INSTS[Item[0]][2]
    Type = Item[1]
    Pin  = Item[2]
    if Type not in BRICKS:
        logs.log_error('matchingOutPins got %s' % Type)
        return []
    Res = []
    for PP in Conns.keys():
        if PP.startswith('x'):
            Res.append(PP)
        if includeQ and PP.startswith('q'):
            Res.append(PP)
    return Res 

            



def isBrickInput(Item):
    Inst,Type,Pin = Item
    if (Type in BRICKS):
        if Pin[0] in ['x','q']: return False
        if Pin[0] in ['a','b','c','d','e','f','g','h']: return True
        if Pin.startswith('no'): return True
        if Pin.startswith('ye'): return True
        if Pin.startswith('pos'): return True
        if Pin.startswith('en'): return True
        if Pin.startswith('clk'): return True
        if Pin.startswith('rst'): return True
        if Pin.startswith('sel'): return True
        logs.log_error('TYPE %s pin %s not qualified' % (Type,Pin))
        return False
    logs.log_error('TYPE %s pin %s not qualified' % (Type,Pin))
    return False
            
def isFlopOut(Mod,Item):
    return Item[2].startswith('q')
def isInput(Item):
    Inst,Type,Pin = Item
    if Inst == 'output':
        return Type != Top
    elif (Type in ENV):
       Son = ENV[Type]
       Dir,_ = Son.NETS[Pin]
       return Dir == 'input'
    elif (Type in BRICKS):
        if Pin[0] == 'q': return False
        if Pin[0] in ['a','b']: return True
        if Pin.startswith('no'): return True
        if Pin.startswith('ye'): return True
        if Pin.startswith('pos'): return True
        if Pin.startswith('en'): return True
        if Pin.startswith('clk'): return True
        if Pin.startswith('rst'): return True
        if Pin.startswith('sel'): return True
        logs.log_error('TYPE %s pin %s not qualified' % (Type,Pin))
        return False
    logs.log_error('TYPE %s pin %s not qualified' % (Type,Pin))
    return False

def buildCross(Base,Mod):
    if Base not in NETTABLES: NETTABLES[Base] = {}
    Down = []
    for Inst in Mod.INSTS:
        Type,_,Conns = Mod.INSTS[Inst]
        for Pin in Conns:
            Net = Conns[Pin]
            if Net not in NETTABLES[Base]: NETTABLES[Base][Net] = []
            NETTABLES[Base][Net].append( (Inst,Type,Pin) )
            if (Type in ENV) and (Type not in NETTABLES) and (Type not in Down):
                Down.append(Type)
    for Net in Mod.NETS:
        Dir,_ = Mod.NETS[Net]
        if Net not in NETTABLES[Base]: NETTABLES[Base][Net] = []
        if Dir == 'output':
            NETTABLES[Base][Net].append( ('output',Base,Net) )
        if Dir == 'input':
            NETTABLES[Base][Net].append( ('input',Base,Net) )
    for Type in Down:
        Son = ENV[Type]
        buildCross(Type,Son)



def isFlopOut_old(Mod,Net):
    if Net in Mod.NETS:
        Dir,_ = Mod.NETS[Net]
        if Dir == 'output': return True

def getStarts(Mod,includeInputs=False):
    Res = []
    if includeInputs:
        for Net in Mod.NETS:
            Dir,_ = Mod.NETS[Net]
            if Dir == 'input':
                Res.append(Net)
            
    for Inst in Mod.INSTS:
        Type,Prms,Conns = Mod.INSTS[Inst]
        if 'flipflop' in Type:
            for Pin in Conns:
                if Pin.startswith('q'):
                    Sig = Conns[Pin]
                    Res.append(Sig)
    return Res


    



def compatible(Wrd,What,What2,What3):
    if What not in Wrd: return False
    if What2 and (What2 not in Wrd): return False
    if What3 and (What3 not in Wrd): return False
    return True

HIER = {}
def buildHierarchy():
    if len(list(HIER.keys()))>0: return
    HIER[Top] = Top
    buildHierarchy__(Top,Top)
    
    
def buildHierarchy__(Top,Path):
    if Top not in ENV: return
    Mod = ENV[Top]
    for Inst in Mod.INSTS:
        Type,Params,Conns = Mod.INSTS[Inst]
        Deep = Path + '.' + Inst
        HIER[Deep] = Type,Params,Conns
        buildHierarchy__(Type,Deep)


def my_importing(Fname):
    sys.path += ['.']
    Orig = Fname
    if (len(Fname)>2)and(Fname[-3:]=='.py'):
        Fname = Fname[:-3]
    if ('/' in Fname):
        wrds2 = Fname.split('/')
        Fname = wrds2[-1]
        Path = '/'.join(wrds2[:-1])
        Path = os.path.abspath(Path)
        sys.path += [Path]

    what = 'import %s'%(Fname)
    That = importlib.import_module(Fname)
    ENV[Fname] = That




def splitLine(line):
    wrds = line.split()
    Wrds = [] 
    state = 'idle'
    for Wrd in wrds:
        if (state=='idle'):
            if (Wrd[0] == '"')and(Wrd[-1]!='"'):
                Token = Wrd
                state = 'work'
            else:
                Wrds.append(Wrd)
        elif (state=='work'):
            Token += ' '+Wrd
            if Wrd[-1]=='"':
                Wrds.append(Token)
                Token = '' 
                state = 'idle'
    if state == 'work':
        Wrds.append(Token)
    return Wrds 

def cleanTiming():
    global LEVELS,PATHS
    LEVELS = {}
    PATHS = []
#    DB['starts'] = {}


def execute_terminal_commands(): 
    Intr = cmdxClass()
    Intr.prompt='?:'
    Intr.cmdloop('hello')
        
COMMANDS = '''
    timing
    pwd
    ls
    top
    cd
    find
    exfind
    import
    source
    starts
    hier
    unused
    filter
    inst
    clean
    fromto
'''.split()
COMMANDS += BRICKS

HELPSTRING = '''
    help will print this
    quit will exit
    1. loads database of synthesized rtl in bricks gate level.
    2. lets You ask questions. like timing paths, names of hierarchy

    filter 0  : disable print filters (default)
    filter 1  : enable print filters
    filter + str0 str1 ....  : strings must appear in print
    filter - str0 str1 ...  : strings must not to appear in print
    unused : list signals with connectivity of one (usually not driving anyone)
    inst instname  : will print all instances that their name matches instname (instname in fullinstname)
    hier mask : print all hierarchies where mask appears
    clean :  remove found paths
    more coming
'''

def accepted(Txt):
    Ok = True
    if not DB['filter']: return True
    for Mask in DB['filters+']:
        if Mask not in Txt: Ok = False
    for Mask in DB['filters-']:
        if Mask in Txt: Ok = False
    return Ok

def quiting():
    lprint('thanks and see you again')
    Sfile.close()
    Lfile.close()
    sys.exit()

if __name__ == '__main__': main()
