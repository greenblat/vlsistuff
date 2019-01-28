#! /usr/bin/python

import os,sys,string,types
VERSION = '14oct2015'
from arrow import make_arrow
def main():
    if ('-help' in sys.argv)or('-h' in sys.argv)or(len(sys.argv)==1):
        print Example
        return
    Fname = sys.argv[1]
    Foutname = 'plotted'
    if '-o' in sys.argv:
        ind  = sys.argv.index('-o')
        Foutname = sys.argv[ind+1]
    File = open(Fname)
    readfile(File)
    if Db.sigs.keys()==[]:
        print 'no signals defined.exiting'
        quit()
    Db.Ps = postscriptClass.postscriptClass('%s.ps'%Foutname,Db)
    Db.Svg = svgClass.svgClass('%s.svg'%Foutname,Db)
    Db.Png = pngClass.pngClass('%s.png'%Foutname,Db)
    Db.Plot = plotClass.plotClass(Db,Db.Ps,Db.Svg,Db.Png)
    Db.Plot.VERSION = VERSION
    Db.Ps.VERSION = VERSION
    if 'muly' in Db.params:
        Db.Plot.muly = Db.params['muly']
        Db.Plot.disty = Db.Plot.disty * Db.params['muly']
    if 'disty' in Db.params:
        Db.Plot.disty = Db.params['disty']
    if 'mulx' in Db.params:
        Db.Plot.mulx = Db.params['mulx']
    Db.build()
    Db.explicit()
    Db.shrink_explicit()
#    Db.dump()
    Db.plot()
    Db.Plot.close()

def readfile(File):
    lNum=0
    while 1:
        line = File.readline()
        if line=='':
            return
        lNum += 1
        if '//' in line:
            line = line[:line.index('//')]

        line = string.replace(line,'(',' ( ')
        line = string.replace(line,')',' ) ')
        wrds = string.split(line)
        if wrds!=[]:
            if wrds[0]=='include':
                try:
                    File2 = open(wrds[1])
                    readfile(File2)
                    File2.close()
                except:
                    print 'cannot open file "%s"'%wrds[1]
            else:
                intify(wrds)
                Expr = gather_opens(wrds)
                if Expr!=[]:
                    use_expr(Expr,line,lNum)

def intify(List):
    for ind,Item in enumerate(List):
        if Item[0] in '0123456789':
            if '.' in Item:
                List[ind]=float(eval(Item))
            else:
                List[ind]=int(eval(Item,Db.params))
        

def gather_opens(wrds):
    List = wrds[:]
    opens=0
    for X in List:
        if X=='(': opens += 1
        elif X==')': opens -= 1
        if (opens<0):
            print 'error! unbalanced (-) opens/closes %s'%str(wrds)
            return []
    if (opens>0):
        print 'error! unbalanced (+) opens/closes %s'%str(wrds)
        return []


    while ')' in List:
        ind = List.index(')') 
        strt = ind
        while List[ind]!='(':
            ind -= 1
        Part = List[ind+1:strt]
        List = List[:ind]+[Part]+List[strt+1:]
    return List
    
class databaseClass:
    def __init__(self):
        self.sigs={}
        self.params={}
        self.params['arrow']=[]
        self.params['vmark']=[]
        self.params['color']={}
        self.params['color']['sig'] = (0,0,0)
        self.params['color']['bus'] = (0,0,0)
        self.params['color']['x'] = (1,0,0)
        self.params['color']['z'] = (0.5,0.5,0)
        self.params['color']['vmark'] = (0.5,0,0)
        self.params['color']['arrow'] = (0.5,0.5,0)
        self.params['color']['vline'] = (0.5,0,0.5)
        self.params['color']['vgrid'] = (0.9,0.9,0.9)
        self.lastTime = 0
        self.display=[]
        self.marks={}
        self.sigLens={}
        self.ScaleX = 1
    def getColor(self,What):
        if What in self.params['color']:
            Color = self.params['color'][What]
            return Color
        return (0,0,0)

    def recordMark(self,Sig,Name,X,Y):
        self.marks[(Sig,Name)]=(X,Y)
    def dump(self):
        for Sig in self.sigs:
            self.sigs[Sig].dump()
        for Param in self.params:
            print 'param %s %s'%(Param,self.params[Param])
    def explicit(self):
        for Sig in self.sigs:
            Time = self.sigs[Sig].explicit()
            if type(Time)==types.IntType:
                self.lastTime = max(self.lastTime,Time)

    def shrink_explicit(self):
        if 'range' not in self.params: return
        (From,To,ScaleX) = self.params['range']
        if ScaleX==1: return
        To = self.compute(To)
        print 'to',To
        From = self.compute(From)
        self.params['range'] = (From/ScaleX,To/ScaleX,1)
        self.lastTime = self.lastTime/ScaleX

        for Sig in self.sigs:
            List = self.sigs[Sig].expl
            for ind,Item in enumerate(List):
                if type(Item[0])in [types.IntType,types.FloatType]:
                    LL = list(Item)
                    LL[0] = 1.0*LL[0]/ScaleX
                    LL[1] = 1.0*LL[1]/ScaleX
                    List[ind]=tuple(LL)
                elif Item[0] in ['mark','break']:
                    LL = list(Item)
                    LL[1] = 1.0*LL[1]/ScaleX
                    List[ind]=tuple(LL)
                else:
                    print 'error for ilia fix shrink',Sig,Item

                



    def build(self):
        dones=1
        while (dones>0):
            dones=0
            for Sig in self.sigs:
                self.activeSig=Sig
                if self.sigs[Sig].full==[]:
                    Raw = self.sigs[Sig].raw
                    Full = self.expand(Raw)
                    if Full:
                        self.sigs[Sig].full=Full
                        dones += 1
    def invert(self,List):
        Res=[]
        for Item in List:
            if type(Item)==types.ListType:
                if (type(Item[0])==types.IntType):
                    rr = Item[:]
                    if (Item[1]==0):
                        rr[1]=1
                    else:
                        rr[1]=0
                    Res.append(rr)
                elif (Item[0]=='mark'):
                    Res.append(Item)
                elif (Item[0]=='color'):
                    Res.append(Item)
                else:
                    return False
            elif Item=='break':
                Res.append(Item)
                
        return Res
            
    def expand(self,Raw):
        if type(Raw)==types.StringType:
            if Raw=='break':
                return [Raw]
            if Raw in self.sigs:
                if self.sigs[Raw].full==[]: return False
                return self.sigs[Raw].full[:]
            else:
                print 'error! raw=%s not in sigs'%Raw
                return False

        if type(Raw)!=types.ListType:
            print 'error! strange raw list "%s" %s for sig %s'%(str(Raw),type(Raw),self.activeSig)
            return False

        try:
            Val = eval(str(Raw[0]),Db.params)
            Raw[0]=Val
        except:
            pass


        if (str(Raw[0]) in Db.params):
            Val =  Db.params[Raw[0]]
            if type(Val)==types.IntType:
                Raw[0]=Val
        if Raw[0] in ['invert','not']:
            Wave = Raw[1:]
            Part = self.expand(Wave)
            if not Part: return False
            Inverted = self.invert(Part)
            if not Inverted: return False
            return Inverted
        if Raw[0] == 'color':
            return [Raw]
        if type(Raw[0])==types.IntType:
            return [Raw]
            
        if Raw[0]=='delay':
            By = Raw[1]
            if len(Raw)==2:
                Val = 0
            elif len(Raw)==3:
                Val = Raw[2]
            else:
                print 'error! bad delay %s'%str(Raw)
                return False
            Wave = [[By,0]]+Raw[2:]
            Part = self.expand(Wave)
            return Part
        if (Raw[0]=='mark'):
            return [Raw]
            
        if Raw[0]=='repeat':
            By = Raw[1]
            Wave = Raw[2:]
            Part = self.expand(Wave)
            if not Part: return False
            More = Part * By
            return More
            

        if Raw[0] in ['and','or','xor']:
            Part1 = self.expand(Raw[1])
            Part2 = self.expand(Raw[2])
            if not Part1 or not Part2: return False
            if Raw[0]=='and':
                Lax = andList(Part1,Part2)
            elif Raw[0]=='or':
                Lax = orList(Part1,Part2)
            elif Raw[0]=='xor':
                Lax = xorList(Part1,Part2)
            return Lax

            
        Full=[]
        for Item in Raw:
            More=self.expand(Item)
            if not More: return False
            Full.extend(More)
        return Full

    def plot(self):
        if 'display' in self.params:
            Display = self.params['display']
        else:
            Display = self.display
        Display = Display[:]
        Display.reverse()
        Len = 0
        for Sig in Display:
            if Sig=='*':
                pass
            elif Sig not in self.sigs:
                print 'error! "%s" sig not in defined'%Sig
            else:
                Len = max(Len,len(Sig))
        Db.Plot.waveOffset = Len*0.8
        if 'range' in self.params:
            (From,To,ScaleX) = self.params['range']
            To = self.compute(To)
            for Sig in Display:
                if Sig=='*':
                    pass
                elif Sig not in self.sigs:
                    print 'error! %s sig not in defined'%Sig
                else:
                    self.sigs[Sig].limit(From,To)
            self.ScaleX = ScaleX
            print 'range limit %s %s last=%s scalex=1/%.1f'%(From,To,self.lastTime,ScaleX)
            if type(To)==types.IntType:
                self.lastTime=To
        
        Db.Plot.setScale(self.lastTime,len(Display))


        for Sig in Display:
            if Sig=='*':
                Db.Plot.skipY()
            elif Sig not in self.sigs:
                print 'error! %s sig not in defined'%Sig
            else:
                Db.Plot.plot(Sig,self.sigs[Sig].expl,self.getColor('sig'))
        
        if 'vgrid' in self.params:
            (Start,Step)=self.params['vgrid']
            Start = Start/self.ScaleX
            Step = Step/self.ScaleX
            Db.Plot.vgrid(Start,Step,self.lastTime,self.getColor('vgrid'))

        for Where in self.params['vmark']:
            if len(Where)>=2:
                X = self.compute(Where[1])
                print 'vmark %s at %s %s'%(Where[0],Where[1],X)
                if type(X) in [types.IntType,types.FloatType]:
                    Db.Plot.vline(X,self.getColor('vmark'),(0.8,0.2))
                    Db.Plot.text(X,'up',Where[0],self.getColor('vmark'))
            else:
                print 'error! vmark needs a name and computable number. it got "%s"'%(str(Where))
        for (M0,M1) in self.params['arrow']:
            Mark0 = M0[1]
            Mark1 = M1[1]
            X0Y0 = self.findMark(Mark0)
            X1Y1 = self.findMark(Mark1)
            if (not X0Y0) or (not X1Y1):
                print 'error! arrow marks not both present %s %s marks: %s'%(Mark0,Mark1,self.marks.keys())
            else:
                X0,Y0 = X0Y0
                X1,Y1 = X1Y1
                Color=(0,0.4,0.4)

                X0 += (Db.Plot.trans/2)
                Y0 += (Db.Plot.muly/2)
                Y1 += (Db.Plot.muly/2)

                Db.Plot.aline(X0,Y0,X1,Y1,self.getColor('arrow'))

                (X2,Y2),(X3,Y3) =  make_arrow(X0,Y0,X1,Y1,0.5)

                Db.Plot.aline(X1,Y1,X2,Y2)
                Db.Plot.aline(X1,Y1,X3,Y3)
#                Db.Plot.fcircle(X1,Y1+(Db.Plot.muly/2),0.2,self.getColor('arrow'))

    def findMark(self,Mark):
        if '.' in Mark:
            MM = tuple(string.split(Mark,'.'))
        else:
            MM = Mark
        for Rec in self.marks.keys():
            if (MM==Rec): return self.marks[MM]

        for Rec in self.marks.keys():
            if (MM==Rec[1]): return self.marks[Rec]
        return False



    def compute(self,Expr):
        if (type(Expr)==types.IntType):
            return Expr
        if (type(Expr)==types.ListType):
            if len(Expr)==1:
                Ex = Expr[0]
                return self.compute(Ex)

            if Expr[0]=='mark':
                Mark = Expr[1]
                X0Y0 = self.findMark(Mark)
                if X0Y0: return X0Y0[0]

            if Expr[0]=='len':
                Sig = Expr[1]
                if Sig not in self.sigs:
                    print 'error! len of undefined signal "%s"'%Sig
                    return 'missing'
                return self.sigs[Sig].lastTime


        print 'error! missing compute expr',Expr
        return 'missing'





class sigClass:
    def __init__(self,Name,Raw):
        self.Name = Name
        self.raw = Raw
        self.full = []
        self.expl = []
    def dump(self):
        print 'sig %s %s'%(self.Name,self.raw)
        print 'sig %s expnd %s'%(self.Name,self.full)
        print 'sig %s expli %s'%(self.Name,self.expl)
    def explicit(self):
        LastTime=0
        for Item in self.full:
            if type(Item[0])==types.IntType:
                self.expl.append((LastTime,LastTime+Item[0],Item[1]))
                LastTime += Item[0]
            elif (Item[0]=='mark'):
                if len(Item)==2:
                    self.expl.append(('mark',LastTime,Item[1]))
                elif len(Item)==3:
                    self.expl.append(('mark',LastTime,Item[1],Item[2]))
                else:
                    print 'sigClass error %s'%(str(Item))
            elif (Item[0]=='color'):
                self.expl.append(('color',LastTime,Item[1]))
            elif (Item=='break'):
                self.expl.append(('break',LastTime,0))
            else:
                print 'strange in wave of class %s %s %s'%(self.Name,Item,self.full)
        self.lastTime=LastTime
        return LastTime
    def limit(self,From,To):
        Ind = 0
        while Ind<len(self.expl):
            Item = self.expl[Ind]
            if Item[0]=='mark':
                if (Item[1]<From)or(Item[1]>To):
                    self.expl.pop(Ind)
                else:
                    Ind += 1
            elif (type(Item[0])==types.IntType):
                if (Item[1]<From)or(Item[0]>To):
                    self.expl.pop(Ind)
                elif (Item[0]<From):
                    Item = (From,Item[1],Item[2])
                    self.expl[Ind]=Item
                    Ind += 1
                elif (Item[1]>To):
                    Item = (Item[0],To,Item[2])
                    Ind += 1
                else:
                    Ind += 1
            else:                    
               Ind += 1
                    
        


def use_expr(Expr,line,Num):
    if Expr[0]=='sig':
        Name = Expr[1]
        Sig = sigClass(Name,Expr[2:])
        Db.sigs[Name]=Sig
        Db.display.append(Name)
    elif Expr[0]=='vgrid':
        Db.params['vgrid'] = (Expr[1],Expr[2])
    elif Expr[0]=='display':
        if 'display' in Db.params:
            Db.params['display'].extend(Expr[1:])
        else:
            Db.params['display'] = Expr[1:]
    elif Expr[0]=='vmark':
        Db.params['vmark'].append(Expr[1:])
    elif Expr[0]=='range':
        if len(Expr)==3:
            Db.params['range'] = (Expr[1],Expr[2],1)
        elif len(Expr)==4:
            Db.params['range'] = (Expr[1],Expr[2],Expr[3])
    elif Expr[0]=='limit':
        Db.params['range'] = (Expr[1],Expr[2])
    elif Expr[0]=='arrow':
        if len(Expr)!=3:
            print 'error! arrow needs two points. "%s"'%(str(Expr))
        else:
            Db.params['arrow'].append((Expr[1],Expr[2]))
    elif Expr[0]=='color':
        Who = Expr[1]
        if type(Expr[2])==types.StringType:
            Clr = getColor(Expr[2])
            Db.params['color'][Who]=(Clr[0],Clr[1],Clr[2])
        elif (len(Expr)==5):
            Db.params['color'][Who]=(Expr[2],Expr[3],Expr[4])
        else:
            print 'error! color spec is strange "%s"'%(string.join(Expr,' '))
    elif Expr[0]=='set':
        Db.params[Expr[1]]=Expr[2]
    elif (len(Expr)==3)and(Expr[1]=='='):
        Db.params[Expr[0]]=Expr[2]
    else:
        print 'line #%d: %s was not used'%(Num,line[:-1])

def mergeList(Pa,Pb,Func):
    Res = []
    Time = 0
    Paa = Pa[:]
    Pbb = Pb[:]
    while (Paa!=[])and(Pbb!=[]):
        if Paa[0] in ['mark','color','break']:
            Res.append(Paa[0])
            Paa.pop(0)
        elif Pbb[0] in ['mark','color','break']:
            Res.append(Pbb[0])
            Pbb.pop(0)
        elif Paa[0][0] in ['mark','color','break']:
            Res.append(Paa[0])
            Paa.pop(0)
        elif Pbb[0][0]==['mark','color','break']:
            Res.append(Pbb[0])
            Pbb.pop(0)
        else:
            Ta = Paa[0][0]
            Tb = Pbb[0][0]
            TT = min(Ta,Tb)
            if Ta<Tb:
                ItemA = Paa.pop(0)
                ItemB = Pbb[0][:]
                ItemB[0]=Tb-Ta
                Pbb[0]=ItemB
            elif (Ta>Tb):
                ItemB = Pbb.pop(0)
                ItemA = Paa[0][:]
                ItemA[0]=Ta-Tb
                Paa[0]=ItemA
            else:
                ItemA = Paa.pop(0)
                ItemB = Pbb.pop(0)
            Val = Func(ItemA[1],ItemB[1])
            Res.append([TT,Val])
    return Res

def andItem(Val0,Val1):
    if Val0==0:
        return 0
    if Val1==0:
        return 0
    return Val0

def orItem(Val0,Val1):
    if Val0==0:
        return Val1
    if Val1==0:
        return Val0
    return Val0

def xorItem(Val0,Val1):
    if Val0==Val1:
        return 0
    return 1

def andList(Pa,Pb):
    return mergeList(Pa,Pb,andItem)
def orList(Pa,Pb):
    return mergeList(Pa,Pb,orItem)
def xorList(Pa,Pb):
    return mergeList(Pa,Pb,xorItem)


import postscriptClass
import svgClass
import pngClass
import plotClass

Db = databaseClass()
#Ps = postscriptClass.postscriptClass('plotted.ps',Db)
#Svg = svgClass.svgClass('plotted.svg',Db)
#Png = pngClass.pngClass('plotted.png',Db)
#Plot = plotClass.plotClass(Db,Ps,Svg,Png)
#Plot.VERSION = VERSION
#Ps.VERSION = VERSION


def getColor(Text):
    if Text=='red': return (1,0,0)
    if Text=='black': return (0,0,0)
    if Text=='white': return (1,1,1)
    if Text=='green': return (0,1,0)
    if Text=='blues': return (0,0,1)
    if Text=='yellow': return (0.8,0.8,0)
    return (0.3,0.3,0.3)





Example = '''
//  this is example file. type it to a file and activate this script with the name of this file:
//  like:   waveformer.py <file.name>
//  it will produce file called "plotted.ps"  . the format is postscript. You can use ghostview or similar
//  to turn it to png or jpeg or whatever.
//     also produced is "plotted.svg" - this can be viewed by any browser.
//     also produced is "plotted.png"  - png is like jpeg picture. lowest quality though.
// if You dont like "plotted" name, add -o yourlikingname  ex:   invoke:  waveformer.py <wafefilename> -o cucu
// all files will be called cucu.ps cucu.svg and so on. (cucu is just an example)
// 
// now the format of the file:


// this is comment

sig rst (5 0) (100 1)            // signal called "rst" will stay "0" for 5 points and the "1" for 100 points
sig clk (repeat 20 (3 0) (3 1)) // this will repeat 20 times 0-3pt 1-3pt
sig aaa    (3 0) (3 1) (3 0) break (5 "idle") (3 "work") (3 "idle") (4 z) (5 0) (5 x)
    // each pair ( duration value) . duration is integer. value can be 0,1,z,x,String,up,down
// up,down creates nice pattern.

//variables = setups
muly = 1.0  // scale Y axis: higher value will stretch the Y dimension.
mulx = 1.0  // scale X axis: higher value will stretch the X dimension.

dur = 5
dur2 = dur*2

sig bbb   (dur*3 0) break (10 1)     // break will display break pattern.
sig ccc   (10 0) (color red) (10 1) (color green) (10 0) (5 z)

// wave can be modified :    (invert ccc) inverts the waveform
sig newsig  (and (invert ccc) (aaa))     // logical operation on waveforms
sig dly     (delay 5 newsig)             // same wave, but delayed for 5 points

sig ddd (5 0) (mark m0) (5 1)


// other graphics
vgrid 0 3    // pale vertical grid starts at point 0 and drawn every 3 points
vmark name (mark mmm0)    // put verical line at location of mark mm0
arrow (mark m0) (mark dly.x1)  // draw arrow from location of mark "m0" to "x1". if mark appears more than once, prepend the sig name.



// setups
include file.name // includes file 
color sig 0 0 0   // signals will be displayed in this color (black)
color vmark 0 1 0
color bus 1 0 0
range 0 (len aaa)  Scale       // limit display from point 0 to length of waveform amb2. it can also be just integer, or reference of mark.
// scale is optional in range. it DIVIDES the X values, so the plot is shorter and "squarer"
display rst clk aaa bbb ccc newsig ddd ....    // optional line. if given will display only this list of signals.





// this file has many errors!!  it is on purpose.

'''

main()
