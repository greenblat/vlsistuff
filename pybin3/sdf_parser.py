#! /usr/bin/env python3.10
import os,sys,string
TB = 'tb.dut'
sys.path.append('/Users/iliagreenblat/verification_libs3')
import logs
logs.Tb = False
from skywater import CellLib
def hashit(LL):
    return str(LL)
Dones = []
class cellClass:
    def __init__(self,List):
        self.Inst = 'none'
        self.Type = 'none'
        self.Interconnects = {}
        self.Iopaths = []
        self.work(List)
    def work(self,List):
        for Item in List:
            if Item[0] == 'CELLTYPE': 
                self.Type = Item[1]
            elif Item[0] == 'INSTANCE':
                if len(Item) == 2:
                    self.Inst = Item[1].replace(' ','')
                else:
                    self.Inst = self.Type.replace(' ','')
                print("CELL",self.Type,self.Inst)
            elif Item[0] == 'DELAY':
                if (len(Item)==2)and(Item[1][0] == 'ABSOLUTE'):
                    self.work_delay(Item[1][1:])
                else:
                    logs.log_error("Item0 %s" % Item[0],0,False)
            elif Item[0] == 'TIMINGCHECK':
                pass
            else:
                logs.log_error("Item1 %s" % Item[0],0,False)
                
    def work_delay(self,List):
        for Item in List:
            if Item[0] == 'INTERCONNECT':
                Src = Item[1]
                Dst = Item[2]
                Dlys = Item[3]
                Res = []
                for X in Dlys: 
                    if X != ':': Res.append(X)
                Dly = eval(Res[0])
                self.Interconnects[(Src,Dst)] = Dly
            elif Item[0] == 'PORT':
                pass
            elif Item[0] == 'IOPATH':
                Src = Item[1]
                Dst = Item[2]
                try:
                    Up = eval(Item[3][0])
                except:
                    Up = 0
                try:
                    Down = eval(Item[4][0])
                except:
                    Down = 0
                if (Down<0)and(Up>=0): Down = Up
                if (Up<0)and(Down>=0): Up = Down
                if (Up<0): Up = 0
                if (Down<0): Down = 0
                self.Iopaths.append(("TRUE",Src,Dst,Up,Down))
            elif Item[0] == 'COND':
                Dst = Item[-1][2]
                Src = Item[-1][1]
                try:
                    Up = eval(Item[-1][3][0])
                except:
                    Up = 0
                try:
                    Down = eval(Item[-1][4][0])
                except:
                    Down = 0
                if (Down<0)and(Up>=0): Down = Up
                if (Up<0)and(Down>=0): Up = Down
                if (Up<0): Up = 0
                if (Down<0): Down = 0
                Cond = Item[1:-1]
                Cond = list(map(hashit,Cond))
                Cond = ''.join(Cond)
                Expr = normalizeExpr(Cond)
                self.Iopaths.append((Expr,Src,Dst,Up,Down))
            else:
                logs.log_error("work_delay %s" % Item[0],0,False)

    def create_interconnects(self,Fout):
        for Src,Dst in self.Interconnects:
            Delays = self.Interconnects[(Src,Dst)]
            X = Src.split('/')
            if len(X) == 1:
                Srca = [Src,'input']
            else:
                Srca = X
            X = Dst.split('/')
            if len(X) == 1:
                Dsta = [Dst,'output']
            else:
                Dsta = X
            Dly = int(eval(str(Delays))*1000)
            Fout.write('INTERCONNECTS.append(("%s","%s","%s","%s",%s,%s))\n' % (Srca[0],Srca[1],Dsta[0],Dsta[1],Dly,Dly))


    def create_vcode(self,Fout,Ftbl):
        self.Type = self.Type.strip()
        Fname = 'dly_'+self.Type
        Inst = self.Inst.replace('\\','')
        Inst = Inst.replace('.','_')
        Inst = Inst.replace(' ','')
        Inst = Inst.replace('[','_')
        Inst = Inst.replace(']','_')

        Dsts = []
        for Cond,Src,Dst,Up,Down in self.Iopaths:
            if Dst not in Dsts: Dsts.append(Dst)
        Dsts.sort()

        Srcs = []
        for Cond,Src,Dst,Up,Down in self.Iopaths:
            if Src not in Srcs: Srcs.append(Src)
        Srcs.sort()
        for Dst in Dsts:
            if self.Type not in Dones:
                Fout.write('def dly_%s_%s(Instance,Pin):\n' % (self.Type,Dst))
                Fout.write('    Instance = logs.bin2str(Instance)\n')
                Fout.write('    if Instance=="": return\n')
                Fout.write('    Pin = logs.bin2str(Pin)\n')
                Fout.write('    debugx(Instance,Pin)\n')
            for Cond,Src,Dstx,Up,Down in self.Iopaths:
                
                if (Dst == Dstx):
                    if (Cond == "TRUE"):
                        if self.Type not in Dones:
                            if type(Src) is str:
                                Fout.write('    if (Pin=="%s"): Dly0,Dly1 = DELAYTABLE[(Instance,"%s","%s",2)]\n' % (Src,Dst,Src))
                                Ftbl.write('DELAYTABLE[("%s.%s","%s","%s",2)] = %s,%s\n' % (TB,Inst,Dst,Src,int(1000*Up),int(1000*Down)))
                            elif Src[0] == 'posedge':
                                Psrc = Src[1]
                                Fout.write('    if (Pin=="%s")and conditionTrue(Instance,"%s"): Dly0,Dly1 = DELAYTABLE[(Instance,"%s","%s",1)]\n' % (Psrc,Psrc,Dst,Psrc))
                                Ftbl.write('DELAYTABLE[("%s.%s","%s","%s",1)] = %s,%s\n' % (TB,Inst,Dst,Psrc,int(1000*Up),int(1000*Down)))
                            elif Src[0] == 'negedge':
                                Psrc = Src[1]
                                Fout.write('    if (Pin=="%s")and conditionTrue(Instance,"!%s"): Dly0,Dly1 = DELAYTABLE[(Instance,"%s","%s",0)]\n' % (Psrc,Psrc,Dst,Psrc))
                                Ftbl.write('DELAYTABLE[("%s.%s","%s","%s",0)] = %s,%s\n' % (TB,Inst,Dst,Psrc,int(1000*Up),int(1000*Down)))

                    else:
                        if self.Type not in Dones:
                            if type(Src) is str:
                                Fout.write('    if (Pin=="%s") and conditionTrue(Instance,"%s"): Dly0,Dly1 = DELAYTABLE[(Instance,"%s","%s",2)]\n' \
                                %(Src,''.join(Cond),Dst,Src))
                                Ftbl.write('DELAYTABLE[("%s.%s","%s","%s",2)] = %s,%s\n' % (TB,Inst,Dst,Src,int(1000*Up),int(1000*Down)))
                            elif Src[0] == 'posedge':
                                Psrc = Src[1]
                                Fout.write('    if (Pin=="%s") and conditionTrue(Instance,"%s&%s"): Dly0,Dly1 = DELAYTABLE[(Instance,"%s","%s",1)]\n' \
                                %(Psrc,Psrc,''.join(Cond),Dst,Psrc))
                                Ftbl.write('DELAYTABLE[("%s.%s","%s","%s",1)] = %s,%s\n' % (TB,Inst,Dst,Psrc,int(1000*Up),int(1000*Down)))
                            elif Src[0] == 'negedge':
                                Psrc = Src[1]
                                Fout.write('    if (Pin=="%s") and conditionTrue(Instance,"!%s&%s"): Dly0,Dly1 = DELAYTABLE[(Instance,"%s","%s",0)]\n' \
                                %(Psrc,Psrc,''.join(Cond),Dst,Psrc))
                                Ftbl.write('DELAYTABLE[("%s.%s","%s","%s",0)] = %s,%s\n' % (TB,Inst,Dst,Psrc,int(1000*Up),int(1000*Down)))

            if self.Type not in Dones:
                Fout.write("    veri.force('%s.Dly0' % Instance,str(Dly0))\n")
                Fout.write("    veri.force('%s.Dly1' % Instance,str(Dly1))\n")
                    
        Dones.append(self.Type)




    def create_code(self,Fout):
        Inst = self.Inst.replace('\\','')
        Inst = Inst.replace('.','_')
        Inst = Inst.replace(' ','')
        Inst = Inst.replace('[','_')
        Inst = Inst.replace(']','_')
        Fout.write('def table_%s(self,Fired):  #%s\n' % (Inst,self.Type))
        Srcs = []
        for Cond,Src,Dst,Up,Down in self.Iopaths:
            if Src not in Srcs: Srcs.append(Src)
        Srcs.sort()
        for Src in Srcs:
            Fout.write('    if ("%s" == Fired):\n' % Src)
            for Cond,Srcx,Dst,Up,Down in self.Iopaths:
                if Srcx == Src:
                    if (Cond == "TRUE"):
                        Fout.write('        self.send("%s",%s,%s)\n' % (Dst,Up,Down))
                    else:
                        Fout.write('        if self.conditionTrue("%s"):\n' % ' '.join(Cond))
                        Fout.write('            self.send("%s",%s,%s)\n' % (Dst,Up,Down))
            
        Srcs = {}
        Keys = []
        for  (Src,Dst) in self.Interconnects:
            if Src not in Srcs: 
                Srcs[Src] = []
                Keys.append(Src)
            Srcs[Src].append((Dst,self.Interconnects[(Src,Dst)]))

        Keys.sort()
        for Src in Keys:
            DstDly = Srcs[Src]
            Dst,Dly = DstDly[0]
            Src = prep(Src)
            Dst = prep(Dst)
            Fout.write('    if (%s == Fired):\n' % Src)
            Fout.write('        self.sendconn(%s,%s)\n' % (Dst,Dly))
            for Dst,Dly in DstDly[1:]:
                Dst = prep(Dst)
                Fout.write('        self.sendconn(%s,%s)\n' % (Dst,Dly))
                    
def prep(In):
    In = In.replace('\\','')
    In = In.replace('.','_')
    In = In.replace('[','_')
    In = In.replace(']','_')
    In = In.replace(' ','')
    if "/" in In:
        ww = In.split("/")
        Pin = ww[-1]
        Path = '_'.join(ww[:-1])
        return '("%s","%s")' % (Path,Pin)
    return '"%s"' % In


CELLS = {}
def main():
    Fname = sys.argv[1]
    File = open(Fname)
    Line = File.read()
    Line = Line.replace('(',' ( ')
    Line = Line.replace(')',' ) ')
    Line = Line.replace('::',' : 0 : ')
    Line = Line.replace('"',' " ')
    Toks = Line.split()
    Toks = gather0(Toks)
    Toks = gather1(Toks)
    build_db(Toks)
    Fout = open('cells_vcode.py','w')
    Fout.write('from delays_vcode import DELAYTABLE\n')
    Fout.write('import veri\n')
    Fout.write('import logs\n')
    Fout.write('from sdf_utils import debugx\n')
    Fout.write(CONDITION)
    Ftbl = open('delays_vcode.py','w')
    Fic = open('interconnects.py','w')
    Fic.write('INTERCONNECTS = []\n')
    Ftbl.write('DELAYTABLE = {}\n')
    for Cell in CELLS:
        CELLS[Cell].create_vcode(Fout,Ftbl)
        CELLS[Cell].create_interconnects(Fic)
    
    maxDelays()
    Fout.close()
    Ftbl.close()
    Fic.close()
    return

    Fout = open('cells_code.py','w')
    Dones = []
    for Cell in CELLS:
        if CELLS[Cell].Type not in Dones:
            Type = CELLS[Cell].Type
            Type = Type.replace(' ','')
            generateCell(Type,Fout)
            Dones += Type
    Fout.write('INSTANCES = {}\n')
    for Cell in CELLS:
        Type = CELLS[Cell].Type
        Cell = prep(Cell)
        Fout.write('INSTANCES[%s] =  %s(%s,table_%s)\n' % (Cell,Type,Cell,Cell.replace('"','')))
    Fout.close()        


def maxDelays():
    DLY = {}
    for Cell in CELLS:
        Path = CELLS[Cell].Iopaths
        Dly = 0
        for _,_,X,Dly0,Dly1 in Path:
            Max  = max(Dly0,Dly1)
            Dly = max(Dly,Max)
            if (Cell,X) in DLY:
                Was = DLY[(Cell,X)]
                if Dly>Was:
                    DLY[(Cell,X)] = Dly
            else:
                DLY[(Cell,X)] = Dly
    LL = []
    for  Cell,X in DLY:
        Dly = DLY[(Cell,X)] 
        LL.append((Dly,Cell,X))
    LL.sort()
    for Dly,Cell,X in LL:
        print(">>>>>>",Dly,Cell,X)



def generateCell(Type,Fout):
    if Type not in CellLib: 
        print('type "%s"' % Type)
        return
    Desc = CellLib[Type]
    Txt = STRCELL
    Txt = Txt.replace('CELL',Type)
    Txt = Txt.replace('TYPE',Type)
    Pins = ''
    for Pin in Desc.pinOrder:
        Pins +=  '        self.pins["%s"] = pinClass("%s")\n' % (Pin,Desc.Pins[Pin])
    Txt = Txt.replace('PINS',Pins)        
    Fout.write(Txt)


STRCELL = '''
class CELL:
    def __init__(self,Inst,Table):
        self.Type = TYPE
        self.Inst = Inst
        self.Table = Table
        self.pins = {}
PINS
    def receive(self,Msg): 
    def send(self,Pin,Dly):
        
'''




def build_db(Toks):
    for Item in Toks:
        if type(Item) is list:
            Key = Item[0]
            if Key in Keys0:
                logs.setVar(Key,Item[1])
            elif (Key == 'CELL'):
                Cell = cellClass(Item[1:])
                CELLS[Cell.Inst] = Cell
                

Keys0 = '''
SDFVERSION
DESIGN
DATE
VENDOR
PROGRAM
VERSION
DIVIDER
VOLTAGE
PROCESS
TEMPERATURE
TIMESCALE
'''.split()

def gather1(Toks):
    Stack =  [ ['top'] ]
    for Tok in Toks:
        if (Tok == '('):
            Stack.append([])
        elif (Tok == ')'):
            Stack[-2].append(Stack[-1])
            Stack.pop(-1)
        else:
            Stack[-1].append(Tok)
    return Stack[0][1]



def normalizeExpr(Cond):
    X = Cond.replace('&&','  & ')
    X = X.replace('==1\'b0',' @ ')
    X = X.replace('==1\'b1','')
    ww = X.split()
    res = ww[:]
    for ind,Tok in enumerate(ww):
        if Tok == '@':
            res[ind] = res[ind-1]
            res[ind-1] = '!'
    return ''.join(res)        



def gather0(Toks):
    Res = []
    state = 'idle'
    for tok in Toks:
        if state=='idle':
            if tok == '"':
                state = 'gather'
                part = ''
            else:
                Res.append(tok)
        elif state=='gather':
            if (tok == '"'):
                Res.append(part)
                part=''
                state = 'idle'
            else:   
                part += ' '+tok

    return Res

CONDITION = '''
def conditionTrue(Instance,Cond):
    return True

'''

if __name__ == '__main__': main()
